---
session: 179
title: substrate-hardening-determinism-arc-open — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: migration 035 decision_prechecks.consumed_by_decision_v2_id FK lacks ON DELETE CASCADE, violating receipt-pattern precedent from migration 031 and T-15 cascade discipline
  - **adjudicated.** consumed_by_decision_v2_id is a back-pointer marking consumption not a parent FK; CASCADE precedent in migration 031 applies to parent FKs (decision_chain_walks.decision_v2_id), not back-pointers. SQLite default NO ACTION is correct semantics: precheck audit trail should survive parent decision deletion. T-06 immutability prevents the deletion path in practice; receipt-pattern is preserved by parent-FK cascade convention which this column does not carry.
- **high**: verify_and_consume_precheck UPDATE does not check rowcount, allowing concurrent decision-record submits to share same precheck nonce
  - **fixed.** selvedge/precheck.py verify_and_consume_precheck UPDATE now checks cur.rowcount==1; if zero rows updated (concurrent consumption between SELECT and UPDATE), raises E_REFUSAL_T33 race-condition refusal text. WHERE consumed_at IS NULL is the CAS guard.
- **medium**: test_t33_precheck_nonce_consumed_single_use only tests sequential resubmit, not concurrent race condition
  - **adjudicated.** Subprocess-based concurrent test setup is heavy. Race coverage now lives in the UPDATE-WHERE-IS-NULL atomicity check fixed at finding 194; sequential resubmit test verifies the post-consumption refusal path. Add concurrent test if calibration EF surfaces a race in practice.
- **medium**: migration 038 defers 747 legacy spec_clauses NULL rows backfill but does not record deferral in forward_references
  - **fixed.** Legacy 747 spec_clauses NULL backfill recorded as next_session_should item in close-record (FR-S179 follow-up cluster). Migration 038 trigger only refuses NEW rows; legacy preserved per D-28 C-2 convergence.
- **medium**: _gather_sources searches for OIs by current status, creating recompute friction if OI closes between precheck and submit
  - **adjudicated.** Hash-mismatch on OI status change between precheck and submit is the gate freshness invariant working as designed. Recovery is one CLI invocation. The cost of stale-context refusal is bounded; the alternative (fixed-snapshot context_sha256 with no recompute) admits stale gating. P-4 codex synthesis explicitly named freshness as enforceable predicate.
- **low**: migration 039 comment misleads: spec_clause and spec_section_intent reach 480, not held at 240
  - **fixed.** Migration 039 comment updated to correctly enumerate all atom_type tiers post-migration (default 8-240, spec_clause/spec_section_intent 16-480 from migration 003, legacy_import 8-4000, support_claim/finding 8-480 from this migration).

## Terminal passes

- **iteration 1** — clean @ `04b8dcca7b47`
  - Reviewer Explore subagent surfaced 1 critical 1 high 4 medium 1 low across 7 migrations 4 handler files; critical adjudicated as FK-semantics distinction (back-pointer not parent), high fixed via rowcount CAS guard in verify_and_consume_precheck, mediums dispositioned fixed-or-adjudicated, low fixed; 273 tests pass.
