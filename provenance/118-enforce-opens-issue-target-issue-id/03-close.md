---
session: 118
title: enforce-opens-issue-target-issue-id — close
engine_version_at_close: engine-v34
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S118 ships engine-v34: opens_issue effects now require target_issue_id at submit time via T-31 trigger and handler alias resolution, mirroring closes_issue at engine-v28.

## Engine version

- engine-v33 to engine-v34.
## What was done

- Migration 022 adds T-31 trigger refusing opens_issue effects with NULL target_issue_id and bumps current_engine_version to engine-v34.
- _submit_decision_record opens_issue branch resolves target alias to target_issue_id and refuses unless resolved issue has status=open.
- closes_issue branch gains symmetric defensive null-guard on cur_status fetchone (iter-3 parity finding).
- prompt-development v7 documents opens_issue target-required surface; engine-manifest v34 stanza explains T-31 and rationale.
## State at close

- T-31 trigger present, smoke-tested against direct-INSERT and handler paths; reviewer loop converged at iter-4 clean.
- Eight legacy NULL target_issue_id opens_issue rows persist; chain-walk regex fallback remains live for them per migration 022 known-limitation note.
## Open issues

- No new issues opened by S118; FR-S117-9 disposed; EF-S117-1 disposed.
## What the next session should address

- Address next highest-priority forward reference or open issue from orient queue; FR-S116-9 watches for second instance of under-exploration pattern.
- Consider a sandboxed test harness or --dry-run mode for write-path submits per EF-S118-1 friction; smoke-testing decision-record handlers leaks rows.
## Validator at close

- tools/validate.sh passes; bin/selvedge validate --precommit returns ok; reviewer iter-4 confirmed clean.
