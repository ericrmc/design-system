#!/usr/bin/env bash
# update-external-workspace.sh — propagate engine updates to an existing
# external-problem workspace.
#
# Per S133 DV-S133-1: ships the engine-definition file set from this source
# workspace to a target external workspace, applies any new migrations, and
# preserves all application content and per-workspace state. Refuses if the
# target has an open session or is not in external-problem mode.
#
# Usage:
#   tools/update-external-workspace.sh <target-path>           # dry-run (default)
#   tools/update-external-workspace.sh <target-path> --apply   # actually update
#
# Engine-definition file list per specifications/engine-manifest.md §3. Update
# SHIP_FILES and SUBTRACTED_FILES below when the manifest's file set changes.
# Last reviewed: engine-v39 (S133).

set -euo pipefail

# -----------------------------------------------------------------------------
# 1. Argument validation
# -----------------------------------------------------------------------------

if [[ $# -lt 1 || $# -gt 2 ]]; then
  cat >&2 <<USAGE
Usage: $0 <target-path> [--apply]

  <target-path>  Path to the external workspace to update.
  --apply        Actually perform the update. Default: dry-run.

Refuses if target has an open session or is not external-problem mode.
USAGE
  exit 1
fi

TARGET="$1"
APPLY_FLAG="${2:-}"
DRY_RUN=1
if [[ "$APPLY_FLAG" == "--apply" ]]; then
  DRY_RUN=0
elif [[ -n "$APPLY_FLAG" ]]; then
  echo "ERROR: unrecognised argument: $APPLY_FLAG (only --apply is supported)" >&2
  exit 1
fi

# -----------------------------------------------------------------------------
# 2. Resolve SOURCE_ROOT (the workspace this script lives in)
# -----------------------------------------------------------------------------

SOURCE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

if ! command -v sqlite3 >/dev/null 2>&1; then
  echo "ERROR: sqlite3 CLI not on PATH; required to read substrate metadata." >&2
  exit 2
fi

if [[ ! -f "$SOURCE_ROOT/state/selvedge.sqlite" ]]; then
  echo "ERROR: source substrate missing: $SOURCE_ROOT/state/selvedge.sqlite" >&2
  exit 2
fi

# -----------------------------------------------------------------------------
# 3. Pre-flight checks on target
# -----------------------------------------------------------------------------

if [[ ! -d "$TARGET" ]]; then
  echo "ERROR: target is not a directory: $TARGET" >&2
  exit 3
fi

# Resolve to absolute path so subsequent operations are unambiguous.
TARGET="$(cd "$TARGET" && pwd)"

if [[ "$TARGET" == "$SOURCE_ROOT" ]]; then
  echo "ERROR: target is the source workspace itself; refusing self-update." >&2
  exit 3
fi

if [[ ! -f "$TARGET/MODE.md" ]]; then
  echo "ERROR: target lacks MODE.md (not a Selvedge workspace): $TARGET" >&2
  exit 4
fi

if [[ ! -f "$TARGET/state/selvedge.sqlite" ]]; then
  echo "ERROR: target lacks substrate: $TARGET/state/selvedge.sqlite" >&2
  exit 5
fi

TARGET_MODE="$(sqlite3 "$TARGET/state/selvedge.sqlite" \
  "SELECT value FROM workspace_metadata WHERE key='mode'" 2>/dev/null || echo "")"
if [[ "$TARGET_MODE" != "external-problem" ]]; then
  echo "ERROR: target mode is '$TARGET_MODE'; refusing to update non-external-problem workspace." >&2
  echo "       This tool only updates external-problem workspaces. Self-development" >&2
  echo "       workspaces author their own engine via spec-version submits." >&2
  exit 6
fi

OPEN_COUNT="$(sqlite3 "$TARGET/state/selvedge.sqlite" \
  "SELECT COUNT(*) FROM sessions WHERE status='open'")"
if [[ "$OPEN_COUNT" != "0" ]]; then
  echo "ERROR: target has $OPEN_COUNT open session(s); refusing to update mid-session." >&2
  echo "       Close the session(s) first via bin/selvedge submit session-close." >&2
  exit 7
fi

# -----------------------------------------------------------------------------
# 4. Read source and target engine versions
# -----------------------------------------------------------------------------

SOURCE_V="$(sqlite3 "$SOURCE_ROOT/state/selvedge.sqlite" \
  "SELECT value FROM workspace_metadata WHERE key='current_engine_version'")"
TARGET_V="$(sqlite3 "$TARGET/state/selvedge.sqlite" \
  "SELECT value FROM workspace_metadata WHERE key='current_engine_version'")"

if [[ -z "$SOURCE_V" ]]; then
  echo "ERROR: could not read current_engine_version from source substrate." >&2
  exit 2
fi
if [[ -z "$TARGET_V" ]]; then
  echo "ERROR: could not read current_engine_version from target substrate." >&2
  exit 5
fi

# -----------------------------------------------------------------------------
# 5. Engine-definition file set (per engine-manifest.md §3)
# -----------------------------------------------------------------------------
#
# Update SHIP_FILES when the manifest's Active spec or executable engine pieces
# change. Update SUBTRACTED_FILES when a previously-shipped file is subtracted
# from the engine; the script removes such files from targets that retain them
# from older bootstraps.

SHIP_FILES=(
  "PROMPT.md"
  "prompts/development.md"
  "prompts/application.md"
  "specifications/methodology.md"
  "specifications/workspace.md"
  "specifications/engine-manifest.md"
  "selvedge/__init__.py"
  "selvedge/cli.py"
  "bin/selvedge"
  "tools/validate.sh"
  "tools/update-external-workspace.sh"
  "tools/hooks/refuse-substrate-md.py"
  ".claude/settings.json"
)

SUBTRACTED_FILES=(
  "specifications/constraints.md"   # subtracted at engine-v32 (DV-S109-1, S109)
)

# Files that should have +x after copy. Match against the path exactly.
EXECUTABLE_FILES=(
  "bin/selvedge"
  "tools/validate.sh"
  "tools/update-external-workspace.sh"
  "tools/hooks/refuse-substrate-md.py"
)

is_executable_file() {
  local f="$1"
  local x
  for x in "${EXECUTABLE_FILES[@]}"; do
    [[ "$x" == "$f" ]] && return 0
  done
  return 1
}

# -----------------------------------------------------------------------------
# 6. Plan: enumerate changed files, files to remove, new migrations
# -----------------------------------------------------------------------------

CHANGED_FILES=()
MISSING_FROM_SOURCE=()
for f in "${SHIP_FILES[@]}"; do
  if [[ ! -f "$SOURCE_ROOT/$f" ]]; then
    MISSING_FROM_SOURCE+=("$f")
    continue
  fi
  if [[ ! -f "$TARGET/$f" ]] || ! cmp -s "$SOURCE_ROOT/$f" "$TARGET/$f"; then
    CHANGED_FILES+=("$f")
  fi
done

REMOVE_FILES=()
for f in "${SUBTRACTED_FILES[@]}"; do
  if [[ -f "$TARGET/$f" ]]; then
    REMOVE_FILES+=("$f")
  fi
done

# Migrations to apply: source migrations not present in target migration directory.
# The migrate runner in bin/selvedge does its own sha256 drift detection on
# already-applied migrations; we only need to copy new migration FILES into
# place so the runner can see them.
NEW_MIGRATIONS=()
shopt -s nullglob
for src_mig in "$SOURCE_ROOT"/state/migrations/*.sql; do
  base="$(basename "$src_mig")"
  if [[ ! -f "$TARGET/state/migrations/$base" ]]; then
    NEW_MIGRATIONS+=("$base")
  fi
done
shopt -u nullglob

# -----------------------------------------------------------------------------
# 7. Print plan
# -----------------------------------------------------------------------------

echo "=== update-external-workspace plan ==="
echo "Source: $SOURCE_ROOT ($SOURCE_V)"
echo "Target: $TARGET ($TARGET_V)"
echo ""

if [[ ${#MISSING_FROM_SOURCE[@]} -gt 0 ]]; then
  echo "WARNING: ${#MISSING_FROM_SOURCE[@]} engine-definition file(s) listed in SHIP_FILES are missing from the source:"
  for f in "${MISSING_FROM_SOURCE[@]}"; do echo "  ? $f"; done
  echo "         Update SHIP_FILES in this script if the file set has changed." >&2
  echo ""
fi

echo "Files to update: ${#CHANGED_FILES[@]}"
for f in "${CHANGED_FILES[@]}"; do echo "  M $f"; done
echo ""
echo "Files to remove (subtracted from engine): ${#REMOVE_FILES[@]}"
for f in "${REMOVE_FILES[@]}"; do echo "  D $f"; done
echo ""
echo "New migrations to apply: ${#NEW_MIGRATIONS[@]}"
for m in "${NEW_MIGRATIONS[@]}"; do echo "  + $m"; done
echo ""

if [[ ${#CHANGED_FILES[@]} -eq 0 && ${#REMOVE_FILES[@]} -eq 0 && ${#NEW_MIGRATIONS[@]} -eq 0 ]]; then
  echo "Target is already up to date."
  exit 0
fi

if [[ "$DRY_RUN" == "1" ]]; then
  echo "Dry-run; no changes made. Re-run with --apply to update."
  exit 0
fi

# -----------------------------------------------------------------------------
# 8. Apply
# -----------------------------------------------------------------------------

echo "=== Applying ==="

for f in "${CHANGED_FILES[@]}"; do
  mkdir -p "$(dirname "$TARGET/$f")"
  cp "$SOURCE_ROOT/$f" "$TARGET/$f"
  if is_executable_file "$f"; then
    chmod +x "$TARGET/$f"
  fi
done

for f in "${REMOVE_FILES[@]}"; do
  rm "$TARGET/$f"
done

for m in "${NEW_MIGRATIONS[@]}"; do
  cp "$SOURCE_ROOT/state/migrations/$m" "$TARGET/state/migrations/$m"
done

if [[ ${#NEW_MIGRATIONS[@]} -gt 0 ]]; then
  echo ""
  echo "Running bin/selvedge migrate --apply in target..."
  ( cd "$TARGET" && bin/selvedge migrate --apply )
fi

# -----------------------------------------------------------------------------
# 9. Post-update verification
# -----------------------------------------------------------------------------

NEW_TARGET_V="$(sqlite3 "$TARGET/state/selvedge.sqlite" \
  "SELECT value FROM workspace_metadata WHERE key='current_engine_version'")"

echo ""
echo "=== Update complete ==="
echo "Target engine-version: $TARGET_V → $NEW_TARGET_V"
echo "Files updated:         ${#CHANGED_FILES[@]}"
echo "Files removed:         ${#REMOVE_FILES[@]}"
echo "Migrations applied:    ${#NEW_MIGRATIONS[@]}"
echo ""

if [[ "$NEW_TARGET_V" != "$SOURCE_V" ]]; then
  echo "NOTE: target engine-version ($NEW_TARGET_V) differs from source ($SOURCE_V)."
  echo "      This is expected when the source's most recent engine bump did not" >&2
  echo "      ship a new migration (e.g. spec-version-only sessions); the target's" >&2
  echo "      current_engine_version updates only via migrations or engine-manifest" >&2
  echo "      atomic-propagation, both of which require a fresh substrate write." >&2
  echo "      To force alignment, the operator may run a manual UPDATE on" >&2
  echo "      workspace_metadata.current_engine_version after auditing the diff." >&2
  echo ""
fi

echo "Next: run 'bash tools/validate.sh' in the target to confirm coherence."
