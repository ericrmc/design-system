#!/usr/bin/env bash
# bootstrap-external-workspace.sh — minimal external-application bootstrap.
# Ships the source workspace's current engine-definition file set (per
# specifications/engine-manifest.md §3) plus all migrations on disk; the
# resulting target inherits whatever engine version the source is at.
#
# Per S106 D-2 (DV-S106-2): copies the engine-definition file set, the selvedge
# Python package and shell shim, the migrations, the PreToolUse hook, the Claude
# Code settings, and tools/validate.sh into a fresh target path; runs
# `bin/selvedge init` to apply all migrations; updates workspace_metadata to mark
# the workspace as external-problem with the supplied workspace_id and the
# source's current engine version; writes MODE.md; creates an empty brief.md
# stub. Excludes (per S106 P-3 minimalist case): aliases.yaml seed, .mcp.json,
# retrieval substrate, README scaffolds, slot-templated brief.
#
# Usage:
#   tools/bootstrap-external-workspace.sh <target-path> <application-slug> [workspace-id]
#
# Refuses to overwrite an existing target. Slug must be kebab-case.

set -euo pipefail

# -----------------------------------------------------------------------------
# 1. Argument validation
# -----------------------------------------------------------------------------

if [[ $# -lt 2 || $# -gt 3 ]]; then
  cat >&2 <<USAGE
Usage: $0 <target-path> <application-slug> [workspace-id]

  <target-path>       Absolute or relative path for the new workspace.
                      MUST NOT already exist.
  <application-slug>  Kebab-case slug for applications/001-<slug>/.
  [workspace-id]      Optional; defaults to "selvedge-<slug>".

This script implements DV-S106-2 (S106 minimal v31 bootstrap scope):
engine-definition files plus selvedge package plus migrations plus hook
plus settings plus validate.sh; bin/selvedge init; workspace_metadata
post-init UPDATE for external-problem mode.
USAGE
  exit 1
fi

TARGET="$1"
SLUG="$2"
WORKSPACE_ID="${3:-selvedge-$SLUG}"

if [[ -e "$TARGET" ]]; then
  echo "ERROR: target path already exists: $TARGET" >&2
  echo "       Bootstrap refuses to overwrite. Choose a new path or remove the existing one." >&2
  exit 2
fi

# Partial-failure cleanup: if any step after directory creation fails (init,
# UPDATE, MODE.md, brief stub, smoke test), remove the half-built target so
# the operator can re-run cleanly. Defends S107 review-finding-81 medium.
# The trap installs only AFTER the existence check above so it does not fire
# on the early refusal-to-overwrite path.
_TARGET_CLEANUP="$TARGET"
trap '_rc=$?; if [[ $_rc -ne 0 && -d "$_TARGET_CLEANUP" ]]; then echo "" >&2; echo "FAILURE: removing half-built $_TARGET_CLEANUP (rc=$_rc); rerun once cause is fixed." >&2; rm -rf "$_TARGET_CLEANUP"; fi' EXIT

if ! [[ "$SLUG" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "ERROR: slug must be kebab-case (lowercase letters, digits, hyphens): $SLUG" >&2
  exit 3
fi

# Workspace-id is interpolated into the post-init SQL UPDATE; validate to the
# same kebab-case shape as slug so it cannot inject a `'` and break out of the
# quoted SQL literal. Defends against the S107 review-finding-80 critical.
if ! [[ "$WORKSPACE_ID" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "ERROR: workspace-id must be kebab-case (lowercase letters, digits, hyphens): $WORKSPACE_ID" >&2
  exit 3
fi

# Resolve SOURCE_ROOT to the source workspace this script lives in.
SOURCE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Source must have a substrate to read the current engine version from.
if ! command -v sqlite3 >/dev/null 2>&1; then
  echo "ERROR: sqlite3 CLI not on PATH; required to read source workspace_metadata and seed target." >&2
  exit 4
fi

if [[ ! -f "$SOURCE_ROOT/state/selvedge.sqlite" ]]; then
  echo "ERROR: source substrate not found at $SOURCE_ROOT/state/selvedge.sqlite" >&2
  exit 5
fi

ENGINE_V="$(sqlite3 "$SOURCE_ROOT/state/selvedge.sqlite" \
  "SELECT value FROM workspace_metadata WHERE key='current_engine_version'")"

if [[ -z "$ENGINE_V" ]]; then
  echo "ERROR: could not read current_engine_version from source workspace_metadata" >&2
  exit 6
fi

TODAY="$(date +%Y-%m-%d)"

echo "=== Selvedge external-application bootstrap (engine-v31 minimal) ==="
echo "Source workspace:  $SOURCE_ROOT"
echo "Target workspace:  $TARGET"
echo "Application slug:  $SLUG"
echo "Workspace id:      $WORKSPACE_ID"
echo "Engine version:    $ENGINE_V"
echo "Date:              $TODAY"
echo ""

# -----------------------------------------------------------------------------
# 2. Create directory tree
# -----------------------------------------------------------------------------

mkdir -p "$TARGET" \
         "$TARGET/specifications" \
         "$TARGET/prompts" \
         "$TARGET/selvedge" \
         "$TARGET/state/migrations" \
         "$TARGET/tools/hooks" \
         "$TARGET/.claude" \
         "$TARGET/applications/001-$SLUG" \
         "$TARGET/bin" \
         "$TARGET/provenance"

# -----------------------------------------------------------------------------
# 3. Copy engine-definition files (per engine-manifest.md §3)
# -----------------------------------------------------------------------------

echo "[3] Copying engine-definition files..."

cp "$SOURCE_ROOT/PROMPT.md"                                "$TARGET/PROMPT.md"
cp "$SOURCE_ROOT/prompts/development.md"                   "$TARGET/prompts/development.md"
cp "$SOURCE_ROOT/prompts/application.md"                   "$TARGET/prompts/application.md"

for spec in methodology workspace engine-manifest; do
  cp "$SOURCE_ROOT/specifications/${spec}.md"              "$TARGET/specifications/${spec}.md"
done
# constraints.md was subtracted at engine-v32 (DV-S109-1, S109); kept out of bootstrap per S133 DV-S133-1.

cp "$SOURCE_ROOT/selvedge/__init__.py"                     "$TARGET/selvedge/__init__.py"
cp "$SOURCE_ROOT/selvedge/cli.py"                          "$TARGET/selvedge/cli.py"
cp "$SOURCE_ROOT/bin/selvedge"                             "$TARGET/bin/selvedge"
chmod +x "$TARGET/bin/selvedge"

cp "$SOURCE_ROOT"/state/migrations/*.sql                   "$TARGET/state/migrations/"

cp "$SOURCE_ROOT/tools/validate.sh"                        "$TARGET/tools/validate.sh"
chmod +x "$TARGET/tools/validate.sh"

cp "$SOURCE_ROOT/tools/hooks/refuse-substrate-md.py"       "$TARGET/tools/hooks/refuse-substrate-md.py"
chmod +x "$TARGET/tools/hooks/refuse-substrate-md.py"

cp "$SOURCE_ROOT/.claude/settings.json"                    "$TARGET/.claude/settings.json"

echo "    Copied: PROMPT.md, 2 prompts, 3 specs, selvedge package (cli.py + __init__.py), bin/selvedge,"
echo "    $(ls "$TARGET/state/migrations/" | wc -l | tr -d ' ') migrations, validate.sh, refuse-substrate-md.py hook, .claude/settings.json."
echo ""

# -----------------------------------------------------------------------------
# 4. Write MODE.md before init (workspace_root() resolves via MODE.md presence)
# -----------------------------------------------------------------------------

cat > "$TARGET/MODE.md" <<MODEEOF
---
mode: external-problem
workspace_id: $WORKSPACE_ID
created_session: 001
engine_version_at_creation: $ENGINE_V
application_brief: applications/001-$SLUG/brief.md
---

# Workspace mode marker

This workspace is an **external-problem application** of the Selvedge engine.
Created $TODAY by tools/bootstrap-external-workspace.sh from the source
self-development workspace, loading engine at \`$ENGINE_V\`.

The application's context lives in \`applications/001-$SLUG/brief.md\` per the
\`application_brief\` pointer above. The operator populates that file before
Session 001 begins.

PROMPT.md §Dispatch reads \`workspace_metadata.mode\` (substrate) at session
load; this file is the human-readable mirror.
MODEEOF

echo "[4] MODE.md written (must precede init: workspace_root() resolves on it)."
echo ""

# -----------------------------------------------------------------------------
# 5. Run bin/selvedge init in the target (applies all migrations)
# -----------------------------------------------------------------------------

echo "[5] Running bin/selvedge init in target..."
( cd "$TARGET" && bin/selvedge init ) >/dev/null
echo "    Substrate initialised; all migrations applied."
echo ""

# -----------------------------------------------------------------------------
# 6. UPDATE workspace_metadata for external-problem mode
# -----------------------------------------------------------------------------
#
# Migration 007 seeds workspace_id='selvedge-self-development' and
# mode='self-development'; migration 011 seeds current_engine_version pinned
# to whatever it shipped at. For an external workspace these need to be
# rewritten post-init. Use sqlite3 directly because there is no submit kind
# for workspace_metadata; the role_write_capabilities row for `__cli__`
# UPDATE on workspace_metadata is seeded by migration 011, but T-12 is an
# application-layer check inside the CLI handlers — direct SQL bypasses it,
# which is the right thing here because the bootstrap runs before any
# session can be opened.

echo "[6] Updating workspace_metadata for external-problem mode..."

sqlite3 "$TARGET/state/selvedge.sqlite" <<SQL
UPDATE workspace_metadata SET value='external-problem'        WHERE key='mode';
UPDATE workspace_metadata SET value='$WORKSPACE_ID'           WHERE key='workspace_id';
UPDATE workspace_metadata SET value='$ENGINE_V'               WHERE key='current_engine_version';
UPDATE workspace_metadata SET value='0'                       WHERE key='init_session_offset';
INSERT OR REPLACE INTO workspace_metadata (key, value)
  VALUES ('application_brief', 'applications/001-$SLUG/brief.md');
SQL

echo "    workspace_metadata: mode=external-problem, workspace_id=$WORKSPACE_ID,"
echo "    current_engine_version=$ENGINE_V, init_session_offset=0,"
echo "    application_brief=applications/001-$SLUG/brief.md"
echo ""

# -----------------------------------------------------------------------------
# 7. Create empty brief.md stub (no slot template per S106 D-2 / P-3 case)
# -----------------------------------------------------------------------------

cat > "$TARGET/applications/001-$SLUG/brief.md" <<BRIEFEOF
---
title: Application 001 — $SLUG
status: brief-pending
engine_version_at_creation: $ENGINE_V
created: $TODAY
---

# Application brief — $SLUG

(This stub is intentionally empty. The operator authors the brief content
directly: problem statement, constraints, stakeholders, success condition,
initial state. No slot template is provided — templates bias what gets
written.)
BRIEFEOF

echo "[7] Empty brief stub created at applications/001-$SLUG/brief.md."
echo ""

# -----------------------------------------------------------------------------
# 8. Smoke test: run validate.sh in target
# -----------------------------------------------------------------------------

echo "[8] Smoke test: running tools/validate.sh in target..."
( cd "$TARGET" && bash tools/validate.sh ) || {
  echo ""
  echo "WARNING: validate.sh reported failures. At fresh-bootstrap state some"
  echo "checks may fail because no provenance exists yet; review the output"
  echo "above and confirm failures are state-dependent, not bootstrap defects."
}
echo ""

# -----------------------------------------------------------------------------
# 9. Print next-steps
# -----------------------------------------------------------------------------

cat <<NEXT
=== Bootstrap complete ===

Next steps for the operator:
  1. cd $TARGET
  2. Author $TARGET/applications/001-$SLUG/brief.md (problem, constraints,
     stakeholders, success condition, initial state).
  3. git init && git add -A && git commit -m "Bootstrap $ENGINE_V"
  4. Open Claude Code in $TARGET; PROMPT.md dispatches to prompts/application.md
     via workspace_metadata.mode and MODE.md.
  5. Session 001 begins.

Engine-feedback flow:
  Methodology-level friction during a session lands as files in
  $TARGET/engine-feedback/ (the directory is created on first feedback record
  per workspace.md §engine-feedback). Operator copies those files into the
  source workspace's substrate via bin/selvedge submit engine-feedback for
  triage.
NEXT
