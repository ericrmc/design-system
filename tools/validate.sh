#!/usr/bin/env bash
# Selvedge structural validator (engine-v19, session 083).
#
# File-presence check on the active engine-definition set, then delegate substrate
# integrity to `selvedge validate --precommit`. Intended to gate git-commit.
#
# Exit codes: 0 on full pass, 1 on any failure (file-presence or substrate).

set -u

cd "$(dirname "$0")/.."

PASS=0
FAIL=0

ok()    { echo "  ok    $1"; PASS=$((PASS+1)); }
fail()  { echo "  fail  $1"; FAIL=$((FAIL+1)); }

require() { [ -e "$1" ] && ok "$1" || fail "$1 (required)"; }

echo "== Selvedge validator (engine-v19) =="

echo
echo "Active engine-definition files:"
require "PROMPT.md"
require "prompts/development.md"
require "prompts/application.md"
require "specifications/methodology.md"
require "specifications/constraints.md"
require "specifications/workspace.md"
require "specifications/engine-manifest.md"
require "tools/validate.sh"
require "state/migrations/001-initial.sql"
require "state/migrations/002-tighten-deliberation-immutability.sql"
require "selvedge/cli.py"
require "bin/selvedge"

echo
echo "Workspace identity:"
require "MODE.md"

echo
echo "Workspace directories:"
require "provenance"

echo
echo "Substrate (selvedge validate --precommit):"
if [ -f "state/selvedge.sqlite" ]; then
  if bin/selvedge validate --precommit; then
    PASS=$((PASS+1))
  else
    fail "selvedge validate --precommit"
  fi
else
  echo "  warn  state/selvedge.sqlite missing — substrate not yet initialised (run 'bin/selvedge init')"
fi

echo
echo "Latest session check:"
LATEST_SESSION_DIR=$(ls -d provenance/*/ 2>/dev/null | sort | tail -1)
if [ -n "$LATEST_SESSION_DIR" ]; then
  [ -f "${LATEST_SESSION_DIR}00-assessment.md" ] && ok "${LATEST_SESSION_DIR}00-assessment.md" \
    || echo "  warn  ${LATEST_SESSION_DIR}00-assessment.md missing"
  [ -f "${LATEST_SESSION_DIR}03-close.md" ] && ok "${LATEST_SESSION_DIR}03-close.md (closed)" \
    || echo "  warn  ${LATEST_SESSION_DIR}03-close.md missing (session may still be open)"
fi

echo
echo "Summary: $PASS ok / $FAIL fail"
[ "$FAIL" -gt 0 ] && exit 1
exit 0
