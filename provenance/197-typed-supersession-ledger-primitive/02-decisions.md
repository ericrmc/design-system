---
session: 197
title: typed-supersession-ledger-primitive — decisions
generated_by: selvedge export
---

# Decisions

## D-1. S197 ships supersession-ledger v1 typed cross-artefact primitive (objects-FK polymorphism + 5-value relation enum + soft-deprecation of decision_effects.supersedes); closes OI-S196-2.

**Kind:** schema_migration.  **Outcome:** adopt migration `048-supersession-ledger-v1`.

**Why.**

- (deliberation) P-1 schema-minimality stance argued objects-FK polymorphism + 5-value enum + reject 7-value codex starting set as un-audited. [P-5-P-1]
- (deliberation) P-2 backcompat-and-objects-graph stance argued ledger as canonical with compat projection for decision_effects.supersedes + replay parity tests. [P-5-P-2]
- (deliberation) P-3 adversarial stance pinned dead-channel watch-trigger + no-CLI-query-surface + hard-cutover preference; minorities preserved. [P-5-P-3]
- (engine_feedback) EF-S197-1 codex (gpt-5.5 xhigh) shape-consult returned SHIP-WITH-NAMED-EDITS naming objects-FK polymorphism + 7-value enum + omit C-4 origin column + in-session spec amendment. [EF-S197-1]
- (engine_feedback) EF-S196-2 bounded-scope binding precluded watch-FR deferral for engine primitives evidenced by 21-session arc + retrospective; bias-toward-build-now applies. [EF-S196-2]
- (engine_feedback) EF-S196-1 codex S196 sequencing named C-2 typed-supersession-ledger ship-first per biggest-schema-gap with C-4 anticipation in scope. [EF-S196-1]
- (prior_decision) DV-S081-1 substrate-loss-defense binds: typed primitive over objects.alias graph composes with chain_walks T-32; objects-FK polymorphism preserves substrate-canonical invariant. [DV-S081-1]
- (prior_decision) DV-S189-1 markdown-only-recovery binds: no synthetic-row backdating; legacy decision_effects.supersedes row migrated as typed row not reconstructed. [DV-S189-1]

**Effects.**

- creates supersession_ledger v1 table + handler + submit kind
- adds_migration 048-supersession-ledger-v1
- closes_issue OI-S196-2 — OI-S196-2 by-mechanism via v1 ship
- modifies prompt-development v3 surfacing supersession submit kind
- supersedes decision_effects.effect_kind=supersedes channel (soft-deprecation)

**Rejected alternatives.**

- **R-1.1.** Ship 7-value relation enum as codex EF-S197-1 starting set (supersedes/replaces/refines/deprecates/narrows/contradicts/withdraws).
  - (inferior_tradeoff) P-1 + P-3 audit found refines/contradicts/deprecates as commentary-shaped not supersession-shaped; admitting them risks generic-relations-table drift.
- **R-1.2.** Ship P-3 4-value tight enum (supersedes/replaces/narrows/withdraws) instead of P-1 5-value.
  - (inferior_tradeoff) Disaster-recovery arc + EF-S196-2 itself name bounded-by relations; 4-value enum would miss bounded-by + supersedes-partial cases evidenced today.
- **R-1.3.** Hard-cutover BOTH decision_effects.supersedes AND refs.supersedes channels at v1: drop CHECK values + migrate both legacy rows.
  - (too_large_for_session) P-2 replay-parity warning + refs.supersedes hot in spec-version handler; cutting refs forces in-session refactor outside OI-S196-2 scope.
- **R-1.4.** Defer ledger ship to second-arc evidence per DV-S190-2 graduation-discipline; ship watch-FR-only at v1 with substrate-receipt gate.
  - (violates_gate) EF-S196-2 bounded-scope binding precludes watch-FR deferral for primitives evidenced by completed 21-session arc + operator-curated synthesis + named recurrence.
- **R-1.5.** No object-registration of supersession_ledger rows at v1 per P-3 ceremony-subtraction stance; defer SL-S<wno>-<seq> aliases until citation evidence.
  - (breaks_invariant) Without object-registration ledger rows are unreachable from chain_walks T-32 graph; M-1 minority preserved but v1 must compose with existing chain-walk infrastructure.
- **R-1.6.** Add a relation_metadata JSON column or notes TEXT escape hatch for unmatched relation cases.
  - (breaks_invariant) M-3 S194 schema-correctness threshold + P-3 explicit rejection bar TEXT escape hatches; closed CHECK enum + migration discipline handles extension cleanly.
