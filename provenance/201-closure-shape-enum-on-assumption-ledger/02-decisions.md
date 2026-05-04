---
session: 201
title: closure-shape-enum-on-assumption-ledger — decisions
generated_by: selvedge export
---

# Decisions

## D-1. S201 ships closure-shape enum on assumption_ledger v1 closing OI-S196-3 by-mechanism via migration 051 + handler validation + 5-canonical-shape closed CHECK + status-shape coupling.

**Kind:** substantive.  **Outcome:** adopt process_rule `closure-shape-enum-on-assumption-ledger-v1`.

**Why.**

- (operator_directive) Bare-prompt auto-proceed mode under starvation-breaker (S200 was kind=procedural only); §1.5 mandates priority-2 MEDIUM-OI burndown; OI-S196-3 selected as most tractable. [A-S201]
- (engine_feedback) EF-S196-2 bounded-scope binding precludes watch-FR or spec-only deferral for engine primitives evidenced by operator-curated multi-session disaster-recovery synthesis. [EF-S196-2]
- (prior_decision) DV-S198-1 typed-assumption-ledger v1 ship pattern: T-15-CALIBRATED rebuild + handler-side actionable refusal + closed CHECK + role_write_capabilities INSERT precedent reused at migration 051. [DV-S198-1]
- (prior_decision) DV-S196-1 deliverable-mining triage opened OI-S196-3 with the 5 canonical closure shapes from disaster-recovery arc retrospective; closure-shape primitive named here. [DV-S196-1]
- (prior_decision) DV-S081-1 substrate-loss-defense + DV-S189-1 markdown-only-recovery establish disaster-recovery arc as operator-curated synthesis source for engine primitives ship. [DV-S081-1]
- (deliberation) D-S201-1 3-perspective deliberation (P-1 schema-minimality + P-2 codex shape-consult + P-3 adversarial-overbreadth) sealed with 5 convergence + 2 divergence + 2 minority + 3 counterfactuals. [P-8-P-1]
- (deliberation) P-2 codex gpt-5.5 high-reasoning shape-consult returned SHIP-WITH-NAMED-EDITS; 5 named edits all integrated into migration + handler. [P-8-P-2]
- (deliberation) P-3 adversarial spec-only-ship stance preserved as M-2 minority watch-trigger; 5-shape overbreadth concern preserved as M-1 minority watch-trigger. [P-8-P-3]

**Effects.**

- adds_migration 051-assumption-ledger-closure-shape-v1.sql T-15 rebuild + 5-value CHECK + 4 status-shape coupling CHECKs
- modifies selvedge/submit/assumption.py: closure_shape on insert + status-update with actionable refusals + auto-clear
- bumps_engine engine-v55 to engine-v56
- closes_issue OI-S196-3 — OI-S196-3 closure-shape enum primitive shipped

**Rejected alternatives.**

- **R-1.1.** Ship METHODOLOGY-SPEC ONLY (P-3 stance): amend prompt-development to name 5 shapes as authoring vocabulary; no closure_shape column, no migration, no watch-FR.
  - (operator_override) EF-S196-2 binds DV-S190-2 graduation-discipline against watch-FR or spec-only deferral for engine primitives evidenced by operator-curated multi-session arcs; the disaster-recovery arc IS that synthesis.
- **R-1.2.** Land closure_shape on issues.status AND assumption_ledger AND close_records in same migration to amortize ceremony and unify closure ontology across artefact kinds.
  - (too_large_for_session) Codex P-2 + P-1 convergence: faux-unification risk; issue-resolution and session-lifecycle have divergent semantics; cross-artefact extension preserved as forward-direction once C-4/C-6 ship.
- **R-1.3.** Add a closure_note TEXT free-form column alongside the 5-shape enum to capture nuance the closed enum cannot express.
  - (breaks_invariant) DV-S020-5 disaster-recovery arc rejected partial-by-component and posture-downgrade closures; M-3 S194 schema-correctness threshold barred TEXT escape hatches; closed-set replay determinism preserved.
- **R-1.4.** Require closure_shape='supersession' (NOT NULL) when status='superseded' instead of admitting NULL or 'supersession'.
  - (inferior_tradeoff) P-1 + P-2 convergence: superseded already encodes the event; double-encoding without evidence forces backfill on existing rows; preserved as v2 tightening if calibration-EF surfaces operator confusion.
- **R-1.5.** Allow closure_shape on status='invalidated' as a 6th 'invalidated' shape value or coerce one of the 5 onto it.
  - (inferior_tradeoff) P-2 named invalidation as ontologically distinct from closure (disproven by direct evidence); semantic-stretching would launder ontology and bar future invalidation_shape vocabulary.
- **R-1.6.** Add closure_shape via ALTER TABLE ADD COLUMN with CHECK at column level instead of T-15-CALIBRATED rebuild.
  - (breaks_invariant) SQLite ALTER ADD COLUMN cannot land cross-column CHECKs (status-shape coupling spans status + closure_shape); rebuild is the only path that lands all 4 coupling CHECKs cleanly.
- **R-1.7.** Defer ship pending second multi-session arc evidence beyond the disaster-recovery arc (graduation-discipline watch-FR-then-graduation pathway).
  - (violates_gate) EF-S196-2 bounded-scope binding: graduation-discipline does not authorize watch-FR deferral for primitives evidenced by completed multi-session application arcs; would re-open creep S196 closed.
