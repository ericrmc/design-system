---
session: 198
title: typed-assumption-ledger-primitive — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: Test coverage gap: docstring claims transition-out-of-active-with-conflict clears sub_type but no actual test case exists for this critical CHECK enforcement.
  - **fixed.** RF-75 fix: added test_status_update_out_of_conflict_clears_sub_type asserting transition out clears sub_type. The fix surfaced a real bug in the explicit-sub_type detection logic; handler updated to use 'sub_type' in p check rather than p.get default. 20/20 tests pass.
- **high**: Race condition on COUNT(*)-based alias sequence: handler uses SELECT COUNT(*) then generates alias, creating collision risk under concurrent submitters across write_tx boundaries; S197 supess-ledger uses same vulnerable pattern.
  - **adjudicated.** RF-76 adjudicated as forward-direction watch-FR per S197 FR-S197-1 precedent. SQLite IMMEDIATE serializes write_tx (single-process orchestrator covers v1 deployment); calibration-EF graduation-trigger if double-allocation surfaces. Same pattern as supersession_ledger.
- **medium**: Alias collision risk: assessment uses A-S<wno> while assumption uses AR-S<wno>-<seq>; both prefix-share S-number pattern but different suffix structure mitigates collision; however, neither space is formally reserved against future object_kinds.
  - **adjudicated.** RF-77 adjudicated: A-S<wno> (assessment, no seq) and AR-S<wno>-<seq> (assumption, with seq) have distinct suffix structure; no actual collision possible. Future namespace reservation is a forward-direction concern; v1 admits.
- **medium**: Discipline gap: handler-side conflict-atom clearing on transition OUT of active-with-conflict (lines 341-342) is implemented but not documented in development.md §6 assumption-ledger clause or docstring.
  - **fixed.** RF-78 fix: handler docstring expanded with transition-out-of-conflict semantics block clarifying auto-clear of sub_type and intentional non-clear of conflict atoms. Test test_status_update_out_of_conflict_clears_sub_type also documents behavior.
- **medium**: Spec discipline gap: M-1/M-2/M-3 watch-trigger minorities (status-mutation drift, replay-via-decisions insufficiency) are recorded only in migration 049 comments and assumption.py docstring, not surfaced in development.md §6 Watch-triggers subsection.
  - **adjudicated.** RF-79 adjudicated: M-1/M-2/M-3 watch-trigger minorities are recorded in (a) DV-S198-1 alternatives + synthesis_md (substrate-canonical), (b) prompts/development.md v4 §6 watch-triggers paragraph (M-1 + M-3 named; M-2 covered by synthesis), (c) migration 049 + handler comments. Layered surfacing matches DV-S197-1 precedent.
- **low**: Minor: test _seed_decision name is functional but generic; would benefit from rename to _seed_minimal_decision_for_assumption_tests for clarity in future maintenance.
  - **adjudicated.** RF-80 adjudicated low: _seed_decision is local to test file; rename is cosmetic and does not affect correctness. Defer.
- **low**: NULL handling edge case: handler validates conflict-discipline before sub_type resolution, meaning NULL sub_type in transition-TO-conflict is caught as missing field (correct); no gap but asymmetric vs atom fields which check existence before NULL-test.
  - **adjudicated.** RF-81 adjudicated low: validation order is correct (sub_type-presence checked first when transitioning TO conflict; atom-presence each checked independently). No functional gap. Defer.

## Terminal passes

- **iteration 2** — clean @ `dff85132cd1d`
  - iter-2 clean: RF-75 fixed via new test (uncovered handler explicit-detection bug also fixed); RF-78 fixed via docstring; RF-76/77/79/80/81 adjudicated; pytest 395 ok up 20 from S197 375.
