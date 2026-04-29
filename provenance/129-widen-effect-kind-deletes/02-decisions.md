---
session: 129
title: widen-effect-kind-deletes — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Widen decision_effects.effect_kind CHECK to admit deletes (engine-v37 to engine-v38) closing OI-S104-2.

**Kind:** schema_migration.  **Outcome:** adopt migration `026-effect-kind-admit-deletes.sql`.

**Why.**

- (prior_decision) DV-S104-6 opened OI-S104-2 noting the methodology-vs-substrate vocabulary gap surfaced by P-2 in S104 D-8 deliberation. [DV-S104-6]
- (constraint) Methodology coding-review-loop predicate names produces, modifies, or deletes executable logic; substrate must admit deletes for honest provenance.
- (prior_decision) Migration 015 ratified the calibrated table-rebuild pattern for non-destructive CHECK widening on this same table; widening admits strictly more rows. [DV-S098-1]

**Effects.**

- adds_migration 026-effect-kind-admit-deletes.sql
- bumps_engine engine-v37 to engine-v38 via current_engine_version UPDATE in migration 026
- closes_issue OI-S104-2 — widens effect_kind CHECK to admit deletes per migration 026

**Rejected alternatives.**

- **R-1.1.** Leave the gap; record delete-executable sessions as effect_kind=modifies and rely on the decision title to convey the deletion.
  - (violates_gate) Methodology distinguishes deletes; conflating with modifies misrepresents provenance and erodes traceability the engine claims to enforce.
- **R-1.2.** Bump engine-manifest spec version alongside the CHECK widening to record the vocabulary expansion as a named manifest event.
  - (redundant_with_existing) current_engine_version bump already records the engine-vN flip; the CHECK widening calibrates substrate to existing methodology language and adds no new manifest capability.
