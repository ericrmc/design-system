#!/usr/bin/env bash
# Selvedge export_manifest reconciliation (engine-v52, FR-S190-1, sealed DV-S190-2 D-B FR-D).
#
# Two-pass divergence check between substrate-recorded export_manifest rows and
# the markdown files they describe on disk:
#
#   Pass 1 — manifest-row integrity. Every export_manifest row, regardless of
#     kind or session_no (NULL session_no rows like open_issues_index and
#     spec_versions_index included), must point to an existing file whose
#     bytes hash to the recorded sha256. Workspace-relative paths only;
#     absolute or path-traversing paths fail cleanly.
#
#   Pass 2 — L5 orphan discovery. For each post-engine-v52 session (substrate
#     evidence: any export_manifest row exists for that workspace_session_no),
#     any of the five L5 filenames present on disk that has no matching
#     manifest row is a stale-on-disk shape — the L5 close-time export should
#     have reconciled it.
#
# Exit codes: 0 on full pass, 1 on any divergence.
#
# Env-var overrides for testability:
#   SELVEDGE_WORKSPACE — workspace root (default: parent of bin/ tools/).
#   SELVEDGE_DB_PATH   — substrate sqlite path (default: $WORKSPACE/state/selvedge.sqlite).

set -u

WORKSPACE="${SELVEDGE_WORKSPACE:-}"
if [ -z "$WORKSPACE" ]; then
  WORKSPACE="$(cd "$(dirname "$0")/.." && pwd)"
fi
DB="${SELVEDGE_DB_PATH:-$WORKSPACE/state/selvedge.sqlite}"

if [ ! -f "$DB" ]; then
  echo "  warn  manifest-reconcile: $DB missing; skipping"
  exit 0
fi

if ! command -v sqlite3 >/dev/null 2>&1; then
  echo "  warn  manifest-reconcile: sqlite3 not on PATH; skipping"
  exit 0
fi

HAS=$(sqlite3 "$DB" "SELECT name FROM sqlite_master WHERE type='table' AND name='export_manifest';")
if [ "$HAS" != "export_manifest" ]; then
  echo "  warn  manifest-reconcile: export_manifest table absent; skipping"
  exit 0
fi

PASS=0
FAIL=0

sha_of() {
  if command -v shasum >/dev/null 2>&1; then
    shasum -a 256 "$1" | awk '{print $1}'
  else
    sha256sum "$1" | awk '{print $1}'
  fi
}

# Pass 1: manifest-row integrity.
MANIFEST_TSV=$(sqlite3 -separator $'\t' "$DB" \
  "SELECT path, sha256 FROM export_manifest ORDER BY path;")

while IFS=$'\t' read -r REL_PATH RECORDED_SHA; do
  [ -z "$REL_PATH" ] && continue
  case "$REL_PATH" in
    /*)
      echo "  fail  manifest-reconcile: absolute path rejected: $REL_PATH"
      FAIL=$((FAIL+1))
      continue
      ;;
    *..*)
      echo "  fail  manifest-reconcile: path-traversal rejected: $REL_PATH"
      FAIL=$((FAIL+1))
      continue
      ;;
  esac
  ABS_PATH="$WORKSPACE/$REL_PATH"
  if [ ! -f "$ABS_PATH" ]; then
    echo "  fail  manifest-reconcile: missing on disk: $REL_PATH"
    FAIL=$((FAIL+1))
    continue
  fi
  ACTUAL=$(sha_of "$ABS_PATH")
  if [ "$ACTUAL" != "$RECORDED_SHA" ]; then
    echo "  fail  manifest-reconcile: sha256 mismatch: $REL_PATH"
    FAIL=$((FAIL+1))
    continue
  fi
  PASS=$((PASS+1))
done <<<"$MANIFEST_TSV"

# Pass 2: L5 orphan discovery — only post-adoption sessions (session has any
# manifest row). Pre-engine-v52 sessions have no rows; their on-disk L5 files
# (if any historical exports landed there) are pre-adoption and out of scope.
#
# Implementation note: pre-fetch the full set of manifest paths once into a
# bash-local list, then test on-disk L5 paths via `grep -qxF` for fixed-string
# exact-match membership. No per-iteration sqlite3 call and no shell-string
# interpolation into SQL — eliminates the SQL-injection surface a slug
# carrying shell or SQL metacharacters could otherwise expose. Slug shape is
# validated app-side at `submit session-open` (kebab-case) but the substrate
# carries no SQL CHECK on it, so bash-layer defence is the second guard.
HAS_SESSIONS=$(sqlite3 "$DB" "SELECT name FROM sqlite_master WHERE type='table' AND name='sessions';")
if [ "$HAS_SESSIONS" = "sessions" ]; then
  COVERED=$(sqlite3 -separator $'\t' "$DB" \
    "SELECT DISTINCT m.session_no, s.slug \
     FROM export_manifest m \
     JOIN sessions s ON s.workspace_session_no = m.session_no \
     WHERE m.session_no IS NOT NULL;")
  ALL_MANIFEST_PATHS=$(sqlite3 "$DB" "SELECT path FROM export_manifest;")
  L5_FILES="05-engine-feedback.md 06-counterfactuals.md 07-fr-dispositions.md 08-prechecks.md 09-chain-walks.md"
  while IFS=$'\t' read -r WNO SLUG; do
    [ -z "$WNO" ] && continue
    # Reject WNO that is not a non-negative integer (defence against malformed
    # substrate rows; sessions.workspace_session_no is INTEGER but we do not
    # rely on the schema for the bash-layer guard).
    case "$WNO" in
      ''|*[!0-9]*)
        echo "  fail  manifest-reconcile: rejecting non-integer workspace_session_no: $WNO"
        FAIL=$((FAIL+1))
        continue
        ;;
    esac
    # Reject slug containing path-separator or shell-metachar characters; the
    # app-side handler enforces kebab-case but we defend in depth.
    case "$SLUG" in
      ''|*/*|*..*|*$'\n'*|*$'\t'*)
        echo "  fail  manifest-reconcile: rejecting malformed session slug: $SLUG"
        FAIL=$((FAIL+1))
        continue
        ;;
    esac
    SDIR="$WORKSPACE/provenance/${WNO}-${SLUG}"
    [ -d "$SDIR" ] || continue
    for FNAME in $L5_FILES; do
      DPATH="$SDIR/$FNAME"
      [ -f "$DPATH" ] || continue
      REL="provenance/${WNO}-${SLUG}/${FNAME}"
      if ! grep -qxF -- "$REL" <<<"$ALL_MANIFEST_PATHS"; then
        echo "  fail  manifest-reconcile: L5 orphan on disk: $REL"
        FAIL=$((FAIL+1))
      fi
    done
  done <<<"$COVERED"
fi

echo "  manifest-reconcile: $PASS rows ok / $FAIL divergent"
[ "$FAIL" -gt 0 ] && exit 1
exit 0
