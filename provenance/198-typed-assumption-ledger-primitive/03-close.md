---
session: 198
title: typed-assumption-ledger-primitive — close
engine_version_at_close: engine-v54
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S198 ships typed-assumption-ledger v1 closing OI-S196-1 via DV-S198-1 (migration 049 + handlers + AR-S<wno>-<seq> + spec v4 amendment).

## Engine version

- engine-v53 to engine-v54.
## What was done

- Migration 049 STRICT assumption_ledger table with 6-status + 3-sub-type closed CHECK enums + four-field DV-S008-1 discipline.
- Handler selvedge/submit/assumption.py with assumption + assumption-status-update kinds + AR-S<wno>-<seq> object-registration.
- 20 tests in state/tests/test_assumption_ledger.py covering admit + refusal + status-update + transition-out paths.
- SPEC-prompt-development-v4 amends §8.5 audit-step A-NNN to AR-S<wno>-<seq>; surfaces new submit kinds + watch-triggers.
- DV-S198-1 sealed schema_migration kind with 9 supports + 4 effects + 7 alternatives + 10 chain-walks per T-32.
- Deliberation D-6 with 3 perspectives + 13 synthesis-points + 4 counterfactuals; capture subagent decomposed all bullets.
- Reviewer iter-2 clean: RF-75 fixed (test plus handler bug); RF-78 fixed (docstring); RF-76/77/79/80/81 adjudicated.
- AR-S198-1 lifted as engine-self demo: migration 048 sha-drift repair via direct UPDATE on schema_migrations.
## State at close

- OI-S196-1 closed; OI-S196-3 + OI-S196-4 + OI-S196-5 + OI-S196-6 + OI-S196-7 remain open from S196 triage.
- FR-S197-13 disposed; FR-S197-14 + FR-S197-15 + watch-FRs FR-S197-16/17 + others remain undisposed.
- EF-S198-1 disposed; EF-S198-2 audit-step + EF-S198-3 success-signal stay undisposed.
## Open issues

- OI-S196-3 + OI-S196-4 MEDIUM; OI-S196-5 + OI-S196-6 + OI-S196-7 medium/low; sequencing options preserved.
## What the next session should address

- OR pick OI-S196-5 prospective-scoping HIGH per FR-S197-14 highest-impact-per-line framing.
- OR pick OI-S196-7 prompt-development spec-clause amendment for EF-S196-2 bounded-scope as small spec-only candidate.
- OR pick OI-S196-3 closure-shape-enum as MEDIUM-OI burndown candidate coupled with OI-S196-1 ship for closure_shape integration.
- Future sessions citing DV-S190-2 graduation-discipline must also cite EF-S196-2 bounded-scope per FR-S196-15 binding.
- Watch FR-S197-1 + FR-S198-1 alias-collision via COUNT-seq under concurrent submitters; common pattern for ledger handlers.
- Watch FR-S198-2 status-mutation drift (M-1 minority): 0 status-update calls citing decisions across N>=5 sessions OR drift opens gate-promotion OI.
- Watch FR-S198-3 replay-via-decisions insufficiency (M-3 minority): calibration-EF naming history-reconstruction failure opens gate-promotion OI for assumption_status_changes table.
## Validator at close

- pytest 395 ok up 20 from S197 375; reviewer iter-2 clean; manifest-reconcile + validate.sh deferred to post-export.
