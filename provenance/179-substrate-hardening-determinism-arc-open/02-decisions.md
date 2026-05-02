---
session: 179
title: substrate-hardening-determinism-arc-open — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Ship 7-migration substrate-hardening arc per S179 operator-named-mandate; engine v48 to v49; T-33 single-use-nonce precheck gate plus 6 supporting hardening migrations 033-039.

**Kind:** schema_migration.  **Outcome:** adopt engine_version `engine-v49`.

**Why.**

- (operator_directive) S179-open operator named insufficient substrate hardening + non-determinism as failure mode and explicitly precluded DV-S109-1 ceremony-subtraction + DV-S152-1 typed-observation pathway as deferral bases. [DV-S171-1]
- (deliberation) P-1 architect maximal program scoped to in-session shipping 4 migrations + 4 T-NN gates establishes the upper bound the synthesis adopts then refines per dependency-ordering critique. [P-28-P-1]
- (deliberation) P-2 codex cross-family preserves DV-S176-1 D-27 read-write separation and contributes decision_precheck_sources child table for per-source digest making consumption observable. [P-28-P-2]
- (deliberation) P-3 adversary surfaces the load-bearing coupling error precheck-before-NULL-tightening renders NULL-cite supports as exception-noise inside the very context body the gate exists to surface, self-defeating. [P-28-P-3]
- (deliberation) P-4 codex skeptic cross-family contributes single-use-nonce consumed inside submit write_tx closing the fire-and-forget gaming pattern timestamp-window predicates admit. [P-28-P-4]
- (deliberation) P-5 pragmatist names FR-handoff pattern for multi-session arc and identifies §7 review-loop bandwidth as principal constraint on in-session migration count. [P-28-P-5]
- (prior_decision) DV-S176-1 ships substrate-gate T-32 as supersedes-of-DV-S175-1 backfire establishing prose-and-discipline reproduces the failure modes the kernel defends against; the same lesson promotes precheck-discipline to substrate at T-33. [DV-S176-1]
- (engine_feedback) EF-S179-1 seal-grade enumerates 4 single-frame counterfactuals including kind-aware T-33 admit predicate adopted as synthesis-original carve-out. [EF-S179-1]

**Effects.**

- adds_migration migration 033 harness alias objects-registration; closes OI-S125-1
- adds_migration migration 034 legacy_unresolved_cites quarantine plus nullable-cite backfill
- adds_migration migration 035 decision_prechecks plus decision_precheck_sources plus T-33 single-use-nonce gate
- adds_migration migration 036 typed-cite T-34 BEFORE INSERT cited_object_id NOT NULL on new rows
- adds_migration migration 037 sessions.slug UNIQUE T-15-CALIBRATED rebuild; closes OI-S122-1
- adds_migration migration 038 spec_clauses source_decision_v2_id NOT NULL plus backfill; closes OI-086-001
- adds_migration migration 039 atom-length widening to 480 chars on three named cliffs; closes OI-S177-1
- bumps_engine engine-v48 to engine-v49
- closes_issue OI-086-003 — OI-086-003 closes by-mechanism via T-34 NOT NULL on new rows plus 034 quarantine for legacy
- closes_issue OI-086-001 — OI-086-001 closes by-mechanism via 038 NOT NULL backfill on spec_clauses traceability
- closes_issue OI-S122-1 — OI-S122-1 closes by-mechanism via 037 sessions.slug UNIQUE
- closes_issue OI-S125-1 — OI-S125-1 closes by-mechanism via 033 harness alias objects-registration
- closes_issue OI-S177-1 — OI-S177-1 closes by-mechanism via 039 atom-length 480 on three named cliffs
- modifies prompts/development.md v21 to v22 amends section 5 with T-33 mandatory precheck clause

**Rejected alternatives.**

- **R-1.1.** Ship P-1 maximal 4-migration shape (032-035) bundling cite-NULL backfill into the precheck migration as one big-bang T-33..T-36 quad without dependency-staged ordering.
  - (inferior_tradeoff) P-3 surfaced coupling error precheck-rendered context body before NULL-tightening renders NULL-cite supports as exception noise training agents to ignore the gate signal, self-defeating.
  - (breaks_invariant) Bundling cite-NULL backfill with precheck table creates rollback-cliff if backfill fails mid-migration where precheck shape is already deployed.
- **R-1.2.** Ship P-3 minimum shape (3 migrations: NULL-tightening + spec_clause FK + slug-UNIQUE + precheck) routing SHOW-CONTEXT walker, LIMIT-ENTRY rate-shaping, and review-loop substrate enforcement entirely to S180 sealed deliberation.
  - (operator_override) S179 operator-named-mandate at session-open admits substantive scope beyond P-3 minimum; substrate-property defense holds for walker plus rate-shaping plus review-loop but not for slug-UNIQUE plus atom-length plus traceability.
- **R-1.3.** Ship P-5 explicit 4-session arc (S179 3 migrations + S180-S183 staged FR-handoff) deferring 4 of 7 migrations to follow-up sessions despite operator mandate.
  - (operator_override) S179 mandate compresses multi-session arc; S180 deferral defense is review-loop bandwidth not infeasibility per P-3 test; 7-migration shape passes by per-migration reviewer.
- **R-1.4.** Ship handler-internal precheck transparently with no separate CLI roundtrip; the submit handler computes the receipt and persists it without agent invocation.
  - (violates_gate) Defeats SHOW-CONTEXT scope at convening time; operator named the agent as the consumer of context body and handler-internal automation prevents agent exposure path enforcement.
- **R-1.5.** Ship timestamp-window-only precheck without single-use-nonce admitting one precheck row to service many decision-records within the window.
  - (inferior_tradeoff) Admits fire-and-forget gaming where agent runs precheck once and submits many decisions without re-exposure; P-2 plus P-4 cross-family convergent on single-use-nonce structural answer to that gaming class.
- **R-1.6.** Ship blanket NOT NULL on decision_supports.cited_object_id without legacy_unresolved_cites quarantine.
  - (breaks_invariant) P-2 plus P-3 plus P-4 plus P-5 convergent C-2 legacy NULL rows already violate the predicate; blanket trigger refuses migration apply or retroactively invalidates committed decision-records breaking write-ahead provenance.
- **R-1.7.** Defer the entire arc per DV-S109-1 ceremony-subtraction or DV-S152-1 typed-observation pathway requiring recurrence pressure before substrate enforcement.
  - (operator_override) S179 operator-named-mandate explicitly precluded both deferral bases at session-open per DV-S171-1 admissibility clause; same shape as DV-S176-1 carrying DV-S175-1 backfire-recovery operator-named-mandate forward.
