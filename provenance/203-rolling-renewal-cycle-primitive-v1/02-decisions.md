---
session: 203
title: rolling-renewal-cycle-primitive-v1 — decisions
generated_by: selvedge export
---

# Decisions

## D-1. S203 ships C-6 rolling-renewal cycle primitive v1: standalone cycle_ledger polymorphic via objects-FK with assumption-only allowlist; cycle row IS proof of observation; reuse closure_shape from S201; closes OI-S196-6 by-mechanism.

**Kind:** schema_migration.  **Outcome:** adopt migration `cycle-ledger-v1`.

**Why.**

- (deliberation) D-9 sealed at S203 with 5 convergence + 2 divergence + 3 minority synthesis points; 3 counterfactuals all dispositioned; codex P-3 middle-ground adopted on knots 1+3+6. [P-9-P-3]
- (engine_feedback) EF-S202-1 codex shape-consult per FR-S196-16 ratifies SINGLE-SHIP at the coding-session level + 6-knot stances + priority-ordering load-bearing knots 1+3+6. [EF-S202-1]
- (engine_feedback) EF-S196-2 bounded-scope binding precludes watch-FR or evidence-deferral for engine primitives evidenced by completed multi-session arc + operator-curated synthesis. [EF-S196-2]
- (prior_decision) DV-S202-1 kind=procedural sealed meta-then-coding split at S202 recording knot inventory + cross-app generalization; this session ships against pre-loaded substrate. [DV-S202-1]
- (prior_decision) DV-S198-1 typed-assumption-ledger v1 ship pattern T-15-CALIBRATED rebuild + handler-side actionable refusal + closed CHECK enum + role_write_capabilities INSERT inline reused at v1 here. [DV-S198-1]
- (prior_decision) DV-S197-1 typed-supersession-ledger polymorphism-via-objects-FK precedent extended to cycle_ledger v1 with narrow object_kind allowlist gate via trigger. [DV-S197-1]
- (prior_decision) DV-S201-1 closure-shape-on-assumption-ledger v1 with no-premature-unification binding; cycle_ledger reuses closure_shape via parent assumption FK lookup not own column. [DV-S201-1]

**Effects.**

- adds_migration migration 052 cycle_ledger v1 STRICT + objects rebuild admit cycle + indexes + allowlist trigger T-42
- bumps_engine engine v56 to v57 cycle_ledger v1 ship
- closes_issue OI-S196-6 — OI-S196-6 C-6 rolling-renewal cycle substrate-promoted

**Rejected alternatives.**

- **R-1.1.** Ship AR-child-only at v1 per P-1 schema-minimality: cycle_ledger.assumption_id INTEGER NOT NULL REFERENCES assumption_ledger; not polymorphic-via-objects-FK at v1.
  - (inferior_tradeoff) P-1 stance preserved as M-1 minority watch-trigger; polymorphic-with-assumption-only-allowlist at v1 honors AR-S202-1 cross-app generalization signal + DV-S197-1 polymorphism precedent.
- **R-1.2.** Ship broad allowlist [assumption, issue, decision_v2] at v1 per P-2 cross-app aggressive polymorphism stance.
  - (inferior_tradeoff) P-2 stance preserved as M-2 minority watch-trigger; assumption-only allowlist at v1 honors codex priority-ordering and ships polymorphism shape without speculating on subject_kind-specific semantics.
- **R-1.3.** Ship typed cycle_trigger child rows at v1 per P-3 codex stance on knot 4: typed counters firing when N reached.
  - (too_large_for_session) Knot 4 codex priority-ordering deferrable-v2; v1 ships cycles without typed triggers; calibration-EF graduation pathway opens v2 cycle_trigger child table per DV-S152-1 typed-observation precedent.
- **R-1.4.** Ship hybrid substantial classifier at v1 with both cited reason atom AND substrate-detected diff metadata per P-3 hybrid stance.
  - (too_large_for_session) P-1 simpler-cited stance + codex priority-ordering deferrable-v2 on knot 2; engine-side diff metadata is speculation pre-evidence; defer per ceremony-subtraction.
- **R-1.5.** Hard-cutover migration deprecating assumption_ledger.sub_type=rolling-renewal channel at v1 ship.
  - (preserves_legacy_path) CF-1 counterfactual addressed-in-synthesis as M-3 minority watch-trigger; soft-deprecation per S197 precedent admits dual-channel for replay; hard-cutover triggered by calibration-EF if dual-channel persists.
- **R-1.6.** Defer C-6 v1 ship pending second-arc cross-application evidence (subscription/compliance/ML calibration) before primitive ship.
  - (violates_gate) EF-S196-2 bounded-scope binding precludes watch-FR or evidence-deferral; codex S196 ratification + 21-session disaster-recovery arc + operator mandate at S202 turn satisfies bound.
- **R-1.7.** Ship cycle_ledger.closure_shape as own column at v1 with cycle-specific path enum disjoint from S201 closure_shape.
  - (breaks_invariant) CF-3 counterfactual nilled-by-exclusion barred-by-DV-S201-1 no-premature-unification + closure_shape adoption per C-2; reuse via parent assumption FK lookup at query time.
