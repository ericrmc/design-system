#!/usr/bin/env bash
# Round-trip test (079 D-11 step 5).
#   open S<n> → write decision (1 alt + 1 ref) → close → reopen
#   → expect T-06 refusal on UPDATE of the closed decision.
#
# Runs against a *throwaway* substrate at state/tests/round_trip.sqlite to avoid
# touching the workspace's primary substrate. Exit 0 on pass, 1 on fail.

set -u

cd "$(dirname "$0")/../.."

DB="state/tests/round_trip.sqlite"
export SELVEDGE_WORKSPACE="$PWD"

# Override db_path by running the CLI with a local override env. Since the CLI hard-codes
# state/selvedge.sqlite under workspace_root, simulate "fresh workspace" by snapshot+swap.
PRIMARY="state/selvedge.sqlite"
PRIMARY_BACKUP="state/selvedge.sqlite.round-trip-backup"

cleanup() {
  if [ -f "$PRIMARY_BACKUP" ]; then
    mv "$PRIMARY_BACKUP" "$PRIMARY"
  fi
}
trap cleanup EXIT

if [ -f "$PRIMARY" ]; then
  cp "$PRIMARY" "$PRIMARY_BACKUP"
fi
rm -f "$PRIMARY" "$PRIMARY"-wal "$PRIMARY"-shm

PASS=0
FAIL=0

step() { echo; echo "== $1 =="; }
ok()   { echo "  pass  $1"; PASS=$((PASS+1)); }
bad()  { echo "  FAIL  $1"; FAIL=$((FAIL+1)); }

step "init substrate"
bin/selvedge init --force >/dev/null && ok "init" || bad "init"

step "open S001 (fresh substrate; T-10 requires contiguous from 1)"
bin/selvedge submit session-open --payload '{
  "session_no": 1,
  "slug": "round-trip",
  "mode": "self-development",
  "workspace_id": "selvedge-self-development",
  "engine_version_at_open": "engine-v17",
  "kind": "spec_only"
}' >/dev/null && ok "session-open" || bad "session-open"

step "write a prerequisite spec_version (target for the decision's [SPEC-…] ref)"
# Produce a hashable file under state/tests/.
mkdir -p state/tests/round-trip-spec
echo "round-trip prerequisite spec body" > state/tests/round-trip-spec/spec.md
SHA=$(shasum -a 256 state/tests/round-trip-spec/spec.md | awk '{print $1}')
bin/selvedge submit spec-version --payload "{
  \"session_no\": 1,
  \"spec_id\": \"round-trip-spec\",
  \"version\": 1,
  \"body_path\": \"state/tests/round-trip-spec/spec.md\",
  \"body_sha256\": \"$SHA\"
}" >/dev/null && ok "spec-version SPEC-round-trip-spec-v1" || bad "spec-version"

step "write decision with 1 alternative and 1 ref (parsed from body_md)"
bin/selvedge submit decision --payload '{
  "session_no": 1,
  "kind": "substantive",
  "title": "Round-trip exemplar",
  "body_md": "This decision references [SPEC-round-trip-spec-v1] in its body to exercise T-01 alias parsing.",
  "alternatives": [
    {"label": "R-1.1", "summary": "alternative considered and rejected",
     "rejection_reason_md": "rejected because round-trip test only needs one alternative and a single ref"}
  ]
}' && ok "decision insert" || bad "decision insert"

step "close S001"
bin/selvedge submit session-close --payload '{
  "session_no": 1,
  "engine_version_at_close": "engine-v17"
}' >/dev/null && ok "session-close" || bad "session-close"

step "verify closed-decision row is mutable from outside the CLI: T-06 must refuse"
# Direct sqlite3 attempt. Expect refusal text to contain E_REFUSAL_T06.
SQL_OUT=$(sqlite3 "$PRIMARY" "UPDATE decisions SET title='mutated' WHERE decision_no=1 AND session_id=(SELECT session_id FROM sessions WHERE session_no=1);" 2>&1) || true
echo "$SQL_OUT" | grep -q "E_REFUSAL_T06" \
  && ok "T-06 refused UPDATE on closed decision" \
  || { bad "T-06 did not refuse: $SQL_OUT"; }

# And the same via the alternative row (T-06 covers decision_alternatives).
SQL_OUT2=$(sqlite3 "$PRIMARY" "UPDATE decision_alternatives SET summary='mutated' WHERE decision_id=(SELECT decision_id FROM decisions WHERE session_id=(SELECT session_id FROM sessions WHERE session_no=1));" 2>&1) || true
echo "$SQL_OUT2" | grep -q "E_REFUSAL_T06" \
  && ok "T-06 refused UPDATE on closed decision_alternative" \
  || { bad "T-06 did not refuse on alt: $SQL_OUT2"; }

step "verify ref was recorded"
N_REFS=$(sqlite3 "$PRIMARY" "SELECT COUNT(*) FROM refs;" 2>&1)
[ "$N_REFS" = "1" ] && ok "1 ref recorded" || bad "expected 1 ref, got $N_REFS"

step "verify validate --precommit passes against closed-session substrate"
bin/selvedge validate --precommit >/dev/null && ok "validate clean" || bad "validate failed"

echo
echo "round-trip: $PASS pass / $FAIL fail"
[ "$FAIL" -gt 0 ] && exit 1
exit 0
