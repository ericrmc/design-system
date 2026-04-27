#!/usr/bin/env bash
# Selvedge minimal structural validator.
#
# Reports presence of the active engine-definition file set and basic workspace
# integrity. The validator is intentionally minimal at engine-v16; the successor
# design (sessions 077-078) will replace this with a database-backed validator
# that runs pre-commit rather than at the end of a session.
#
# Exit codes: 0 on full pass, 1 if any required file is missing.

set -u

cd "$(dirname "$0")/.."

PASS=0
WARN=0
FAIL=0

ok()    { echo "  ok    $1"; PASS=$((PASS+1)); }
warn()  { echo "  warn  $1"; WARN=$((WARN+1)); }
fail()  { echo "  fail  $1"; FAIL=$((FAIL+1)); }

require() {
  if [ -e "$1" ]; then ok "$1"; else fail "$1 (required)"; fi
}

optional() {
  if [ -e "$1" ]; then ok "$1"; else warn "$1 (optional, missing)"; fi
}

echo "== Selvedge minimal validator (engine-v16) =="

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

echo
echo "Workspace identity:"
require "MODE.md"

echo
echo "Workspace directories:"
require "provenance"
optional "applications"
optional "engine-feedback"
optional "open-issues"
optional "archive"

echo
echo "Latest session check:"
LATEST_SESSION_DIR=$(ls -d provenance/*/ 2>/dev/null | sort | tail -1)
if [ -n "$LATEST_SESSION_DIR" ]; then
  if [ -f "${LATEST_SESSION_DIR}00-assessment.md" ]; then
    ok "${LATEST_SESSION_DIR}00-assessment.md"
  else
    warn "${LATEST_SESSION_DIR}00-assessment.md (latest session lacks assessment)"
  fi
  if [ -f "${LATEST_SESSION_DIR}03-close.md" ]; then
    ok "${LATEST_SESSION_DIR}03-close.md (session closed)"
  else
    warn "${LATEST_SESSION_DIR}03-close.md (latest session not yet closed)"
  fi
else
  warn "no provenance directories found"
fi

echo
echo "Summary: $PASS ok / $WARN warn / $FAIL fail"

if [ "$FAIL" -gt 0 ]; then
  exit 1
fi
exit 0
