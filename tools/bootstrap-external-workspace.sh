#!/usr/bin/env bash
# bootstrap-external-workspace.sh
#
# Creates a fresh external-problem application workspace inheriting the Selvedge
# engine at its current version. Implements the engine-manifest.md §6 minimal
# external-application initialisation contract end-to-end.
#
# Usage:
#   bootstrap-external-workspace.sh <target-path> <application-slug> [workspace-id]
#
#   <target-path>       Absolute or relative path for the new workspace.
#                       MUST NOT already exist.
#   <application-slug>  Short kebab-case slug for applications/001-<slug>/.
#   [workspace-id]      Optional; defaults to "selvedge-<slug>".
#
# What this script does (in order):
#   1. Validates arguments and refuses to overwrite an existing path.
#   2. Creates the target directory tree.
#   3. Copies the engine-definition files per engine-manifest.md §3.
#      SKIPS: superseded spec versions (*-v1.md, *-v2.md, ...); SESSION-LOG.md;
#      open-issues/; provenance/; applications/; engine-feedback/; MODE.md;
#      CLAUDE.md; this script itself; .git/; .claude/; .serena/.
#   4. Writes MODE.md with mode: external-problem + required metadata +
#      application_brief pointer, per PROMPT.md §Session-001 obligation.
#   5. Scaffolds empty development-provenance (SESSION-LOG.md header,
#      open-issues/index.md header, empty open-issues/resolved/ and provenance/).
#   6. Creates applications/001-<slug>/brief.md stub derived from
#      prompts/application.md §This application's context slot template.
#   7. Creates engine-feedback/outbox/ with a README naming the
#      workspace-structure.md v5 §engine-feedback schema.
#   8. Runs validate.sh in the new workspace as a smoke test (pre-Session-001
#      run; some checks may report failures that are expected at empty-workspace
#      state and will resolve once Session 001 produces provenance).
#   9. Prints next-steps for the operator.
#
# After this script runs:
#   - Operator populates applications/001-<slug>/brief.md, replacing each
#     <<slot>> placeholder with application-specific content.
#   - Operator runs `git init && git add -A && git commit` in the new workspace
#     (the script does not initialise git — that is the operator's choice of
#     remote, author, signing, etc.).
#   - Operator opens Claude Code in the new workspace; the engine's PROMPT.md
#     dispatcher loads prompts/application.md automatically via MODE.md.
#   - Session 001 executes per prompts/application.md.
#
# Engine-feedback flow (for operator awareness):
#   - During any session in the new workspace, if methodology-level friction
#     arises, the session writes a feedback file to engine-feedback/outbox/
#     using naming convention EF-<session>-<slug>.md per
#     specifications/workspace-structure.md v5 §engine-feedback.
#   - Between sessions, the operator copies the outbox file verbatim into the
#     self-development source workspace at engine-feedback/inbox/. The outbox
#     file in the external workspace is preserved as the originating witness.
#   - The self-development workspace's next session triages the inbox record
#     per its normal Assess activity.
#
# This script is ANCILLARY TOOLING, not an engine-definition file. It is NOT
# enumerated in engine-manifest.md §3 and is NOT copied into external workspaces
# by itself. External workspaces that later need to spawn further workspaces can
# copy this script manually from the source self-development workspace.

set -euo pipefail

# -----------------------------------------------------------------------------
# 1. Argument validation
# -----------------------------------------------------------------------------

if [[ $# -lt 2 || $# -gt 3 ]]; then
  cat >&2 <<EOF
Usage: $0 <target-path> <application-slug> [workspace-id]

  <target-path>       Absolute or relative path for the new workspace.
                      MUST NOT already exist.
  <application-slug>  Short kebab-case slug for applications/001-<slug>/.
  [workspace-id]      Optional; defaults to "selvedge-<slug>".

See the header of this file for the full bootstrap contract per
engine-manifest.md §6.
EOF
  exit 1
fi

TARGET="$1"
SLUG="$2"
WORKSPACE_ID="${3:-selvedge-$SLUG}"

# Resolve SOURCE_ROOT to the self-development workspace this script lives in.
SOURCE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Refuse to overwrite.
if [[ -e "$TARGET" ]]; then
  echo "ERROR: target path already exists: $TARGET" >&2
  echo "       Bootstrap refuses to overwrite. Choose a new path or remove the existing one." >&2
  exit 2
fi

# Validate slug shape.
if ! [[ "$SLUG" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "ERROR: application slug must be kebab-case (lowercase letters, digits, hyphens): $SLUG" >&2
  exit 3
fi

TODAY="$(date +%Y-%m-%d)"

# Derive current engine version from the source's engine-manifest.md §2.
# The line being matched looks like: **`engine-v7`** (established Session 036 ...
ENGINE_V="$(grep -m1 -E '^\*\*`engine-v[0-9]+`\*\*' "$SOURCE_ROOT/specifications/engine-manifest.md" \
           | sed -E 's/.*`(engine-v[0-9]+)`.*/\1/')"

if [[ -z "$ENGINE_V" ]]; then
  echo "ERROR: could not derive engine version from engine-manifest.md §2" >&2
  exit 4
fi

echo "=== Selvedge external-application bootstrap ==="
echo "Source workspace:     $SOURCE_ROOT"
echo "Target workspace:     $TARGET"
echo "Application slug:     $SLUG"
echo "Workspace id:         $WORKSPACE_ID"
echo "Engine version:       $ENGINE_V"
echo "Date:                 $TODAY"
echo ""

# -----------------------------------------------------------------------------
# 2. Create target directory tree
# -----------------------------------------------------------------------------

mkdir -p "$TARGET" \
         "$TARGET/specifications" \
         "$TARGET/prompts" \
         "$TARGET/tools" \
         "$TARGET/open-issues/resolved" \
         "$TARGET/provenance" \
         "$TARGET/applications/001-$SLUG" \
         "$TARGET/engine-feedback/outbox"

# -----------------------------------------------------------------------------
# 3. Copy engine-definition files (engine-manifest.md §3)
# -----------------------------------------------------------------------------

echo "[3] Copying engine-definition files..."

# 3a. PROMPT.md
cp "$SOURCE_ROOT/PROMPT.md" "$TARGET/PROMPT.md"

# 3b. Prompts (development template copied per §3 — all engine-definition prompts
# travel together so an external workspace retains the full three-file set).
cp "$SOURCE_ROOT/prompts/development.md" "$TARGET/prompts/development.md"
cp "$SOURCE_ROOT/prompts/application.md" "$TARGET/prompts/application.md"

# 3c. Active-status specifications only (exclude *-v1.md, *-v2.md, ... superseded files per §4).
SPEC_FILES=(
  methodology-kernel.md
  multi-agent-deliberation.md
  validation-approach.md
  workspace-structure.md
  identity.md
  reference-validation.md
  read-contract.md
  engine-manifest.md
)
for spec in "${SPEC_FILES[@]}"; do
  cp "$SOURCE_ROOT/specifications/$spec" "$TARGET/specifications/$spec"
done

# 3d. Validator
cp "$SOURCE_ROOT/tools/validate.sh" "$TARGET/tools/validate.sh"
chmod +x "$TARGET/tools/validate.sh"

echo "    engine-definition files copied (12 files per engine-manifest §3)."
echo ""

# -----------------------------------------------------------------------------
# 4. Write MODE.md (workspace-identity per workspace-structure.md v5 §MODE.md
#    and PROMPT.md §Session-001 obligation)
# -----------------------------------------------------------------------------

echo "[4] Writing MODE.md..."

cat > "$TARGET/MODE.md" <<EOF
---
mode: external-problem
workspace_id: $WORKSPACE_ID
created_session: 001
engine_version_at_creation: $ENGINE_V
application_brief: applications/001-$SLUG/brief.md
---

# Workspace mode marker

This workspace is an **external-problem application** of the Selvedge engine.
Created $TODAY by bootstrap-external-workspace.sh from the self-development
source workspace, loading engine at \`$ENGINE_V\`.

See \`PROMPT.md\` §Dispatch for how this file is consumed at session load.
See \`specifications/workspace-structure.md\` §MODE.md for the normative schema.
See \`specifications/engine-manifest.md\` §3a for the workspace-identity file class.

The application's context lives in \`applications/001-$SLUG/brief.md\` per the
\`application_brief\` pointer above. The operator populates that file before
Session 001 begins.
EOF

echo "    MODE.md written."
echo ""

# -----------------------------------------------------------------------------
# 5. Scaffold empty development-provenance
# -----------------------------------------------------------------------------

echo "[5] Scaffolding development-provenance..."

cat > "$TARGET/SESSION-LOG.md" <<'EOF'
# Session Log

Thin one-line-per-session index. Canonical per-session detail lives in
`provenance/NNN-title/03-close.md` per `specifications/read-contract.md` v4 §1
and `specifications/workspace-structure.md` v5 §SESSION-LOG.md. This file is
default-read surface and must remain under the per-file budget in
`read-contract.md` §2.

| Session | Date | Title | One-sentence decision-surface summary |
|---------|------|-------|---------------------------------------|
EOF

cat > "$TARGET/open-issues/index.md" <<'EOF'
# Open Issues — Index

Active and resolved issues, one-line status summaries. Full per-OI detail lives
in `open-issues/OI-NNN.md`; resolved issues in `open-issues/resolved/OI-NNN.md`.

This file is the default-read surface entry point per
`specifications/read-contract.md` §1. Per-OI files are default-read when
relevant to the current session's work; otherwise they are accessed by explicit
reference per `read-contract.md` §6.

## Active issues

| OI | Title | Surfaced | Status |
|----|-------|----------|--------|
| (none at Session 001) | | | |

## Resolved issues

| OI | Title | Resolved | Session |
|----|-------|----------|---------|
| (none at Session 001) | | | |

## Conventions

- **Issue numbering** is strictly append-only: OI-001 is first, OI-002 second,
  etc. Numbers are never reused.
- **Status** values in per-OI files are canonical; this index's Status column
  is a one-line summary that may abbreviate.
- **Resolution** does not delete the issue; it moves the file to `resolved/`
  with frontmatter `status: resolved`.
EOF

echo "    SESSION-LOG.md + open-issues/index.md written; provenance/ empty."
echo ""

# -----------------------------------------------------------------------------
# 6. Create applications/001-<slug>/brief.md stub
#    Mirrors the slot structure in prompts/application.md §This application's context
# -----------------------------------------------------------------------------

echo "[6] Creating application brief stub..."

cat > "$TARGET/applications/001-$SLUG/brief.md" <<EOF
---
title: Application 001 — $SLUG
originating_session: 001
engine_version: $ENGINE_V
status: brief-stub
created: $TODAY
workspace_id: $WORKSPACE_ID
---

# Application brief — $SLUG

This brief is the primary input to every session's Read activity for this
application, per \`prompts/application.md\` §This application's context. The
operator populates each section below before Session 001 begins by replacing
every \`<<...>>\` placeholder with concrete content.

Once populated, this file is the domain-scope slot the dispatcher points at via
\`MODE.md\` frontmatter \`application_brief: applications/001-$SLUG/brief.md\`.

## Problem statement

<<Replace this placeholder with one to three paragraphs describing what is being
designed, for whom, and under what constraints. Name the problem the application
exists to work on. If the scenario is fictional, state so explicitly.>>

## Constraints

<<Enumerate domain constraints, time constraints, and stakeholder constraints
concretely. If constraints are expected to change across sessions (e.g., "each
session invalidates prior assumptions; infrastructure, demand, coordination, or
communications may shift"), describe the change mechanism here so subsequent
sessions know how to interpret the shifts.>>

## Stakeholders

<<Who holds the problem. Who will receive the artefact. Who validates. If a
domain-actor is available, name them and describe how evidence is obtained. If
no domain-actor is available, state whether Reference validation per
\`specifications/reference-validation.md\` is feasible, or whether validation is
qualitative via multi-agent deliberation (see \`prompts/application.md\`
§Validate).>>

## Success condition

<<State as observable evidence, not as internal properties. What must the
artefact(s) do for this application to be considered successful? If the
application is intended as an engine stress-test (e.g., testing behaviour under
changing constraints), name that goal here alongside the artefact success
criteria.>>

## Initial state

<<Any materials, references, partial work, or prior context the application
starts with. If starting from scratch, state "no prior materials; starting from
the problem statement." If the scenario is fictional and self-contained, state
that explicitly — reference-validation Cell 1 does not apply in that case.>>

## Session arc (optional)

<<If the operator has a planned session cadence (e.g., "4–5 sessions with
changing constraints each session"), outline the general shape here. Session
001 will refine this into a concrete work plan via Assess and Decide activities.
The arc may include expected artefact types (system model, assumptions log,
response plan, risk register, decision trees) and the mechanism by which each
subsequent session's inputs differ from the prior session's.>>

## Notes for Session 001

<<Optional: any hints, preferences, or constraints that Session 001's
orchestrator should read first. Example: "Validation will be qualitative
multi-agent deliberation throughout; do not attempt reference-validation."
Example: "First session should Decide the artefact set before any Produce
activity.">>
EOF

echo "    applications/001-$SLUG/brief.md stub written."
echo ""

# -----------------------------------------------------------------------------
# 7. Create engine-feedback/outbox/ with README
# -----------------------------------------------------------------------------

echo "[7] Creating engine-feedback/outbox/..."

cat > "$TARGET/engine-feedback/outbox/README.md" <<EOF
# Engine-feedback outbox

Per \`specifications/workspace-structure.md\` v5 §engine-feedback, this
directory is the **outbox** for methodology-level feedback observed during this
external application's execution. Non-engine operator-managed content; not
copied when the engine is cloned.

## When to write a feedback file

During any session in this workspace, if an engine-level concern surfaces — an
unclear specification, a kernel §7 activity ambiguity, a \`multi-agent-deliberation.md\`
field that is awkward in this domain's practice, a reference-validation exercise
gap, a dispatcher edge case, or any equivalent methodology-level friction —
record the observation as a feedback file here.

Feedback files are **out-of-scope for this application's own deliberation**
(whose work is the domain artefact) but **in-scope for engine/methodology
improvement** by the self-development source workspace's triage process.

## File naming

\`EF-<session-number>-<short-slug>.md\` — for example, \`EF-002-dispatch-edge-case.md\`.

## Frontmatter schema (copy into each feedback file)

\`\`\`yaml
---
feedback_id: EF-NNN-<slug>
source_workspace_id: $WORKSPACE_ID
source_session: NNN
created_at: <ISO-8601 timestamp>
reported_by: operator | application-agent
target: engine | methodology | other
target_files: [<paths-to-affected-engine-files>]
severity: blocker | friction | observation
status: outbound
---
\`\`\`

## Body sections

\`## Observation\` — what happened in this application.
\`## Why It Matters\` — what engine/methodology behaviour was implicated.
\`## Suggested Change\` — optional; concrete change proposal if the feedback
                       author has one.
\`## Evidence\` — links, copied snippets, or file-and-line references.
\`## Application-Scope Disposition\` — why this application did or did not
                                    resolve locally.

## Return flow

Between sessions, the operator copies each completed feedback file verbatim
from this outbox to the self-development source workspace at:

    <source-workspace>/engine-feedback/inbox/EF-<same-name>.md

The file in this outbox is preserved as the originating witness; the inbox copy
in the source workspace is the triage target. The engine does not specify
automated cross-workspace transport — the operator is the transport per
workspace-structure.md v5 §engine-feedback return semantics.

The self-development workspace's \`engine-feedback/INDEX.md\` tracks intake /
triage / resolution status across all mediated feedback records.
EOF

echo "    engine-feedback/outbox/README.md written."
echo ""

# -----------------------------------------------------------------------------
# 8. Smoke-test validator in the new workspace
# -----------------------------------------------------------------------------

echo "[8] Running validate.sh smoke test in new workspace..."
echo "    (Some checks will fail or skip — pre-Session-001 workspaces are expected"
echo "     to have no provenance yet. These failures resolve once Session 001 runs.)"
echo ""

if bash "$TARGET/tools/validate.sh" >/dev/null 2>&1; then
  echo "    validate.sh: PASS on bootstrapped workspace."
else
  VALIDATOR_STATUS="$?"
  echo "    validate.sh: exit $VALIDATOR_STATUS (non-zero acceptable pre-Session-001)."
  echo "    Run \`bash $TARGET/tools/validate.sh\` manually to see the report."
fi
echo ""

# -----------------------------------------------------------------------------
# 9. Next steps
# -----------------------------------------------------------------------------

cat <<EOF
============================================================
Bootstrap complete.
============================================================

Target workspace:    $TARGET
Engine version:      $ENGINE_V
Workspace id:        $WORKSPACE_ID
Application slug:    $SLUG

Next steps for the operator:

  1. Populate the application brief:
       \$EDITOR $TARGET/applications/001-$SLUG/brief.md

     Replace each <<...>> placeholder with application-specific content.
     The brief is the primary input Session 001 will Read.

  2. Initialise git in the new workspace (your choice of remote, author, signing):
       cd $TARGET
       git init
       git add -A
       git commit -m "Bootstrap external-problem workspace at $ENGINE_V"

  3. Open Claude Code in the new workspace. The dispatcher reads MODE.md and
     loads prompts/application.md. Session 001 begins per that prompt.

  4. If engine/methodology friction arises during any session, write a feedback
     file to $TARGET/engine-feedback/outbox/ (see README there for schema).
     Between sessions, copy the file into:
       $SOURCE_ROOT/engine-feedback/inbox/

     The self-development workspace's next session will triage it.

============================================================
EOF
