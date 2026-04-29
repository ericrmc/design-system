---
session: 125
title: reference-harness-substrate-kind — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: P-4 assumption_basis (load-bearing assumptions with origin session and status) is absent from the schema; only world_constraint and surrogate_frame are captured.
  - **fixed.** Migration 024 adds reference_harness_assumptions table per P-4 schema; harness-assumption handler captures origin_session and status.
- **high**: T-32 seal-immutability covers BEFORE INSERT only; UPDATE and DELETE on sealed harness sub-tables are unguarded and can rewrite or destroy evidence.
  - **fixed.** Migration 024 adds T-32 BEFORE UPDATE and BEFORE DELETE triggers on all sub-tables; trigger UPDATE is admitted only for the firing transition on a sealed harness.
- **high**: Falsification trigger firing does not auto-transition parent harness status to reopened; logical state and DB state can diverge.
  - **fixed.** Migration 024 adds T-37 AFTER UPDATE cascade trigger that promotes parent harness status sealed -> reopened atomically when fired_at moves NULL -> NOT NULL.
- **high**: Harness alias is not registered in objects so [RH-...] cross-citation from decision-records would fail T-01.
  - **adjudicated.** Mirrors the issues precedent (migration 009); cross-citation via [RH-...] requires widening objects.object_kind, deferred to OI-S125-1.
- **medium**: reference_harnesses table allows UPDATE of non-status columns on sealed rows; T-33 only guards status transitions.
  - **fixed.** Migration 024 adds T-36 refusing UPDATE of non-lifecycle columns on sealed harnesses.
- **medium**: Falsification trigger expiry_sessions distance is not enforced; triggers can fire on a harness whose expiry has elapsed.
  - **adjudicated.** Expiry-window enforcement scoped out per migration 023 commentary; tracked as OI-S125-2 to block bin/selvedge harness expire CLI work.
- **medium**: Load-bearing claim broken result has no automatic OI emission per spec; application-layer gap unrecorded.
  - **adjudicated.** Application-layer concern outside the substrate kind; tracked as OI-S125-3 for post-pilot work.
- **medium**: Falsification trigger fired_at + reopened_session_id pair CHECK constraint is not exercised by the test suite.
  - **fixed.** test_trigger_pair_check_constraint added in test_reference_harness.py exercising the fired_at + reopened_session_id pair CHECK refusal.
## Iteration 2

- **critical**: T-36 admits silent rewrite of sealed_at/sealed_session_id/expired_at/reopened_session_id outside status transitions; sealed timeline can be falsified.
  - **fixed.** Migration 025 strengthens T-36 to admit lifecycle column writes only on a status-transitioning UPDATE; standalone rewrites refused. Test test_t36_lifecycle_columns_immutable_outside_transition covers.
- **high**: Reopened harness blocks new trigger registration and additional trigger fires; multi-event replay on same harness is impossible by schema.
  - **adjudicated.** Design choice: one harness equals one stress cycle; replay equals new harness. Tracked as OI-S125-4 for pilot-driven re-evaluation.
- **high**: T-32 trigger UPDATE guard requires status=sealed; once T-37 cascade flips status to reopened no further trigger can fire on the same harness.
  - **adjudicated.** Same design as 152: trigger fires once per harness; subsequent events recorded on a new harness. OI-S125-4.
- **medium**: reference_harnesses parent row has no BEFORE DELETE trigger; sealed harness can be deleted wholesale, destroying all child evidence via FK action.
  - **fixed.** Migration 025 adds T-38 BEFORE DELETE refusing delete on any harness past open. Test test_t38_no_delete_after_open covers.
- **medium**: test_reference_harness lacks coverage of assumption UPDATE/DELETE seal-immutability and second-trigger-after-reopen failure.
  - **fixed.** Tests test_t32_assumptions_no_update_after_seal and test_t32_assumptions_no_delete_after_seal added; second-fire-after-reopen omitted by design (OI-S125-4).
- **low**: test_t37_trigger_fire_cascades_to_reopened only checks reopened_session_id IS NOT NULL; does not verify it equals the firing session.
  - **fixed.** test_t37_trigger_fire_cascades_to_reopened tightened to assert reopened_session_id equals the firing session id from the fixture.

## Terminal passes

- **iteration 1** — findings @ `44cb56b`
  - Iteration 1 surfaced 4 high and 3 medium findings; addressed via migration 024 hardening and follow-up issues OI-S125-1/2/3.
- **iteration 2** — findings @ `44cb56b`
  - Iter 2 surfaced 1 critical (T-36 lifecycle gap) + 1 medium (parent DELETE) fixed via migration 025; 2 high adjudicated as design (OI-S125-4).
- **iteration 3** — clean @ `44cb56b`
  - Iteration 3 verifies T-36 and T-38 close iter-2 critical and medium; OI-S125-4 adjudication enforced; 20 tests substantive; no new defects.
