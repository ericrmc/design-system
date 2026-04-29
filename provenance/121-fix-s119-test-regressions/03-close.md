---
session: 121
title: fix-s119-test-regressions — close
engine_version_at_close: engine-v34
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S121 restored 153/153 pytest pass; wired pytest into tools/validate.sh; deleted obsolete md-glob tests with OI-S121-1 carrying the substrate-direct rewrite intent.

## Engine version

- engine-v34 (no bump; test/tooling restoration only).
## What was done

- Fixed 7 test_migrate.py imports (_t15_violations now imported from selvedge.migrations after S119 refactor).
- Updated 2 test_monitor_external status tests to substrate-direct ef_rows packet shape per S110 rewrite.
- Deleted 8 md-glob harvest-ef tests plus _seed_ef_files helper; opened OI-S121-1 to track substrate-direct rewrite.
- Wired uv run pytest --no-header into tools/validate.sh with mktemp-isolated log; iter-2 review clean.
## State at close

- 153/153 pytest passing; validate.sh 17/0 incl pytest; engine-v34 unchanged.
## Open issues

- OI-S121-1 (substrate-direct harvest-ef test rewrite) opened MEDIUM; no other new issues.
## What the next session should address

- Address OI-S121-1 by writing substrate-direct harvest-ef tests (peer engine_feedback seeding via _peer_submit; ledger idempotency; since-session filter).
- Or proceed with next FR/OI from orient queue: OI-S104-2 (decision_effects.effect_kind deletes) or OI-S105-1 (third validation sense).
## Validator at close

- tools/validate.sh 17 ok / 0 fail incl pytest 153 passed; selvedge validate --precommit ok.
