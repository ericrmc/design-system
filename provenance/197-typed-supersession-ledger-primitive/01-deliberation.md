---
session: 197
title: typed-supersession-ledger-primitive — deliberation
generated_by: selvedge export
---

# Deliberation

## D-5 — OI-S196-2 typed-supersession-ledger v1 schema and submit-kind shape

sealed_at: 2026-05-04T09:30:02.129Z

### P-1 (anthropic)

### P-2 (openai)

### P-3 (anthropic)

### Synthesis

**Synthesis: ship typed-supersession-ledger v1 via objects-FK polymorphism + 5-value enum + soft-deprecation of decision_effects.supersedes + object-registration of ledger rows + in-session prompt-development amendment.**

**Convergence (3-of-3).**

C-1 polymorphism via objects.object_id FK; no source_kind/target_kind discriminator. P-1 explicit (artefacts already in objects.alias graph). P-2 explicit (validate source/target through objects registry). P-3 implicit (FK to objects). Composes natively with chain_walks T-32 over objects.alias.

C-2 reject 7-value enum overbreadth as starting-point. P-1 push back (5-value tighter). P-2 small enum. P-3 hard-tighten to 4. Codex EF-S197-1 7-value-set is starting point not binding.

C-3 migrate the 1 historical decision_effects.supersedes row in-session. P-1 backfill in-session. P-2 migrate preserving original row id. P-3 atomic-or-nothing migration. No dual-channel-write end-state.

C-4 reject forward-FK to C-4 stakeholder-event table at v1. All 3 omit. Migration adds optional FK column when C-4 lands; v1 reason_atom bounds risk.

C-5 CHECK source != target refusing self-supersession at insert; UNIQUE(source,target,relation_kind).

**Divergence.**

D-1 enum cardinality 4 vs 5 vs small-unspecified. Adopt P-1 5-value {supersedes-fully, supersedes-partial, bounded-by, replaces-mechanism, retracted-by}: disaster-recovery arc + EF-S196-2 explicitly named bounded-by relations (EF-S196-2 itself bounds DV-S190-2). P-3 4-value preserved as M-1 minority + watch-trigger.

D-2 object-registration eagerness. Adopt P-2 path: register supersession_ledger rows as objects (alias SL-S<wno>-<seq>) so they participate in objects.alias graph and can be cited from decision-record supports via existing _resolve_alias_to_object_id. P-3 defer-until-citation-evidence preserved as M-1 minority component.

D-3 decision_effects.supersedes end-state. Adopt P-1+P-2 soft-deprecation: keep CHECK enum value admissible for historical replay; route NEW writes through ledger via handler discipline. P-3 hard-cutover preserved as M-1 minority + watch-trigger if dual-channel persists.

**Minorities preserved.**

M-1 P-3 dead-channel watch-trigger: 0 inserts across N>=5 future sessions => watch-FR for deletion-or-graduation. Pinned as forward-direction.

M-2 P-3 NO new CLI query surface at v1. Adopt; chain-walk + existing tooling suffices until citation evidence demands.

M-3 P-2 add basis=prior_object to decision_supports for SL citation. Defer to v2; v1 reuses basis=prior_decision since _resolve_alias_to_object_id resolves SL aliases via objects.alias.

**Counterfactuals.**

CF-1 hard-cutover BOTH channels at v1: addressed-in-synthesis (P-2 replay-parity + refs.supersedes hot in spec-version handler bound v1 to asymmetric cutover).

CF-2 relation_metadata JSON column or notes TEXT escape hatch: nilled-by-exclusion barred-by-constraint (M-3 S194 schema-correctness threshold + P-3 explicit rejection).

**Bias-toward-build-now applied per EF-S196-2.** No watch-FR deferral; ship v1 in S197. P-3 watch-triggers (M-1) record predicted failure modes for calibration-EF graduation, not v1 deferral basis.

### Synthesis points

- **convergence C-1.** Polymorphism via objects.object_id FK; no source_kind/target_kind discriminator columns.
- **convergence C-2.** Reject 7-value enum overbreadth as starting point; closed CHECK enum admit at v1.
- **convergence C-3.** Migrate the 1 historical decision_effects.supersedes row in-session; no dual-channel writes.
- **convergence C-4.** Reject forward-FK to C-4 stakeholder-event table at v1; let C-4 add origin column when it lands.
- **convergence C-5.** CHECK source!=target refusing self-supersession; UNIQUE on (source,target,relation_kind).
- **divergence D-1.** Enum cardinality: P-1 5-value; P-3 4-value tight; P-2 small unspecified. Synthesis adopts P-1 5-value with P-3 watch-trigger.
- **divergence D-2.** Object-registration: P-2 mandatory SL-S<wno>-<seq>; P-1 implicit; P-3 defer-until-citation. Adopts P-2 register at v1.
- **divergence D-3.** decision_effects.supersedes end-state: P-1 keep readable; P-2 compat projection; P-3 hard-cutover. Adopts P-1+P-2 soft-deprecation; P-3 minority pinned.
- **minority M-1.** P-3 dead-channel watch-trigger: 0 inserts across N>=5 sessions surfaces watch-FR for deletion-or-graduation.
- **minority M-2.** P-3 NO new query CLI surface at v1; chain-walk + existing tooling suffices until citation evidence demands.
- **minority M-3.** P-2 forward-direction: add basis=prior_object to decision_supports for SL citation; v1 reuses basis=prior_decision via _resolve_alias_to_object_id.
