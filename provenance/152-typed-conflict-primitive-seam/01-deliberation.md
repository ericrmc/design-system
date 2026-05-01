---
session: 152
title: typed-conflict-primitive-seam — deliberation
generated_by: selvedge export
---

# Deliberation

## D-20 — Typed-conflict-primitive seam: should sub-types and closure shapes become kernel primitives?

sealed_at: 2026-05-01T11:57:00.588Z

### P-1 (anthropic)

**Position.** Choose (C) hybrid typed-observation unenumerated: count instability across arcs precludes kernel enums but the vocabulary did productive work, so add nullable opt-in kind atoms without closed lists.

**schema_sketch.**
- Add two nullable text columns conflict_kind and closure_kind to the existing active_with_conflict-shaped substrate row post DV-S151-1.
- No CHECK constraint, no foreign key to an enum table, no NOT NULL — empty/NULL is the default and remains valid for any entry not opting in.
- No new table; harness substrate kind retains free-text observation columns unchanged with kind columns alongside as a structurally-typed lexically-open slot.
**cli_surface.**
- submit handler accepts optional --conflict-kind <atom> and --closure-kind <atom> flags as opaque non-empty whitespace-trimmed length-bounded strings with no enum check.
- view renders the kind atom inline next to the conflict/closure annotation if present; no new submit-kind verb is added.
- No validation of the atom value against any list; methodology spec mentions the slot exists as a typed observation pathway without naming canonical values.
**migration_path.**
- Single migration adds the two nullable columns to the existing harness substrate row.
- Order: this migration runs after the OI-S151-1 ergonomic-fix coding session lands; ergonomic-fix migration is #N and this is #N+1.
- Backfill is empty-string/NULL default — no historical re-categorisation of A-018, A-020, A-022, A-017 entries.
- Arc-close annotations from RH-S148-1 and RH-S149-1 stay as free-text in original fields; new columns only populate from new entries onward.
**what_not.**
- Not proposing a conflict_subtype enum with the four S149 values.
- Not proposing a closure_shape enum with the five or six EF-S147-1 values.
- Not proposing methodology spec text that names canonical sub-types or closure shapes.
- Not proposing migration of historical entries to populate the kind atoms.
- Not proposing substrate-kind-elevation that would make the harness itself the kernel-layer carrier of the taxonomy.
- Not proposing cross-arc reconciliation rules — different arcs may use overlapping or disjoint atom values and the kernel does not arbitrate.
**open_question.**
- When a second arc populates conflict_kind and closure_kind, what triggers the graduation review where (C) might be reconsidered for promotion to (A)?
- Trigger options: count threshold (e.g. >=2 arcs with overlapping vocabulary), stability threshold (no retrospective re-fold across N reflective passes), or operator-decision-only?
- This deliberation cannot settle the trigger — it requires evidence of how the typed-observation slot behaves cross-arc, which does not yet exist.
**risk.**
- Free-form kind atom degenerates into ad-hoc tag soup: every arc invents its own vocabulary, no convergence emerges, slot becomes weakly-informative metadata no one reads.
- Failure mode is silent — slot fills with values that do not cluster into anything supporting an enum, and (C) becomes a permanent halfway house.
- Mitigation hook: graduation-review question must be answered before the second arc completes, otherwise the slot signal is wasted.
**what_lost.**
- Versus (A): no methodology-spec naming of sub-types means future arc-plans cannot reference contested-authority closure pattern with kernel-grounded citation; vocabulary stays arc-internal.
- Versus (B): one extra migration, two extra columns, small CLI-surface increase the kernel must maintain for possibly never-used capacity if no second arc populates it.
- Versus status quo: substrate gains structurally-typed slots the kernel must keep schema-stable across migrations even if mostly NULL — small ongoing maintenance cost in exchange for retaining interpretive signal.

### P-2 (openai)

**Position.** Choose C hybrid typed-observation unenumerated: labels are useful observations but not closed kernel primitives; repeated single-arc use justifies a data pathway, not a frozen taxonomy.

**schema_sketch.**
- Add nullable string/atom fields such as conflict_kind and closure_kind where conflict and closure observations are recorded.
- Do not add enum constraints for source-vs-source, plan-vs-resource, demand-vs-supply, contested-authority, or the 5-6 closure shapes.
- Validate only that supplied values are non-empty atoms with stable spelling.
- Preserve richer explanatory text separately, because the label alone is not yet reliable enough to carry meaning.
**cli_surface.**
- Add optional handler inputs for conflict_kind and closure_kind.
- The CLI should accept arbitrary atoms, not restrict to a baked-in list.
- Display observed kinds in read/show output so later arcs can compare patterns.
- Avoid help text that presents the disaster-response vocabulary as canonical kernel vocabulary.
**migration_path.**
- One migration should add nullable conflict_kind to the relevant active-conflict observation records.
- A second migration should add nullable closure_kind to closure/transition records.
- Order should be conflict first, closure second, because the sub-type field attaches to ongoing ACTIVE-WITH-CONFLICT entries before closure classification.
- Migration numbers should be assigned at implementation time after the settled repo migration head; not pre-named from this brief.
**what_not.**
- Not proposing kernel enums.
- Not proposing that demand-vs-supply be permanently retained or permanently folded; the 4->3->4 history is exactly why the kernel should not decide that now.
- Not proposing that disaster-response labels become required across other modes.
- Not treating blocked-by-counterparty or posture-downgrade-to-stable as universal closure theory on single-arc evidence (EF-S147-1).
**open_question.**
- Unresolved question is when accumulated typed observations become promotion-worthy.
- Would require at least a second arc in a materially different domain, with independent reuse or productive revision of the same labels.
- Hard part is deciding whether same label, different domain means genuine generality or only superficial vocabulary reuse.
**risk.**
- Main risk of C is quiet pseudo-standardisation.
- Once a kernel field exists, operators may copy the disaster-response atoms as if they were blessed types, even without enum enforcement.
- Could create a de facto taxonomy without the deliberative threshold that option A would require.
**what_lost.**
- Compared with B, this adds kernel surface area before the taxonomy is mature.
- Compared with A, loses immediate analytical neatness: queries cannot rely on a closed set, documentation cannot promise complete categories, downstream tooling must tolerate heterogeneity.
- Cost is acceptable because current evidence is internally unstable: conflict sub-types moved 4->3->4 across reflective passes and closure shapes moved 6->5 inside the same arc.
- Safer kernel move is to remember the observation without pretending the category system has settled.

### P-3 (anthropic)

**Position.** Choose (B) hold-as-external-application-discipline: kernel hosts arc-plans and conflict entries with provenance, not the kinds; single-arc oscillation is signal that the application still negotiates categories.

**schema_sketch.**
- None at the kernel layer.
- Disaster-response harness substrate kind (workspace-experimental reference_harness adopted at DV-S151-1) already carries labels as free-text artefact annotations on conflict_entry rows.
- No new column, no new table, no enum; substrate-as-shipped is sufficient with free-text notes accommodating plan-vs-resource, contested-authority etc as observations.
- If a second arc begins to use the same vocabulary, cost of revisiting is low — adding a nullable string column later is a forward-compatible migration.
**cli_surface.**
- None. No new submit-kind. No new handler.
- Existing submit-arc-plan and the harness record-conflict (workspace-experimental) continue to accept free text.
- No kernel-layer methodology slot is reserved either; reserving a slot is itself a commitment to fill it, and the methodology spec stays silent on conflict taxonomy and closure shape.
**migration_path.**
- None. No migration is required because no schema changes.
- If (B) is later overturned by second-arc evidence, the migration would be a single nullable-string-column addition (call it migration M-future-1, ordering trivial: append after current head).
- The non-action here is itself the cheapest reversible step.
**what_not.**
- Not proposing the application stop using the vocabulary — the harness should keep using plan-vs-resource, contested-authority etc internally as useful narrative scaffolding.
- Not proposing the methodology forbid the practice.
- Not proposing we delete the S148/S149 retrospective inventories from provenance — those remain valuable as the record of an unstable taxonomy.
- Not proposing (C) hybrid: an unenumerated typed slot still commits the kernel to the shape of the question (one-conflict-has-one-kind), which the F-7 medevac reclassification shows is itself contested.
**open_question.**
- What is the second-arc trigger? At what point would a future arc surfacing the same or near-same vocabulary force a re-examination?
- Honest answer: when two independent application arcs converge on overlapping subsets of these labels without methodology coordination — that is the natural-kind signal.
- Cannot resolve here whether the trigger should be operator-discretion or a numbered open-issue with a wake condition.
**risk.**
- Failure mode of (B) is vocabulary drift across arcs: a second arc reinvents resource-vs-resource or authority-conflict with slightly different semantics, losing comparability.
- By the time drift is noticed, two arcs of free-text annotation must be reconciled retrospectively — strain similar to RH-S148-1 but cross-arc.
- Mitigation: harness substrate kind preserves labels in queryable rows, so a future reconciliation pass is mechanical, not archaeological.
- Second risk: by not naming a re-examination trigger, (B) decays into permanent silence; addressable by opening successor open-issue (OI-S152-future) with explicit wake condition.
**what_lost.**
- Compared to (A): lose cross-arc analytical leverage that would exist if the kernel knew the vocabulary — show all contested-authority closures becomes free-text grep not typed query.
- Lose the methodology ability to teach the vocabulary to future arc designers; they will rediscover labels rather than inherit them.
- Compared to (C): lose the cheap escape hatch of typed-but-unenumerated observation.
- Honest cost: roughly one future session of reconciliation work if a second arc surfaces overlapping vocabulary.
- Weighed against (A) cost — kernel commitment to a 4-or-3-or-4 taxonomy plus migration on one-arc evidence — (B) loss is the smaller and more reversible bet; DV-S151-1 R-1.2 subtract rule applies.

### Synthesis

Three perspectives convened on whether the disaster-response arc's conflict sub-types and closure shapes should become kernel-layer typed primitives. P-1 anthropic primary and P-2 openai cross-family converged on (C) Hybrid typed-observation pathway with no closed enum: nullable opt-in conflict_kind / closure_kind atoms at the workspace-experimental harness substrate kind layer accept arbitrary non-empty values without enum constraint, kernel methodology stays agnostic to canonical vocabulary, and accumulated cross-arc evidence becomes possible without committing to a fixed taxonomy. P-3 anthropic adversarial-minimalist honestly converged on (B) hold-as-external-application-discipline: an unenumerated typed slot still commits the kernel to the one-conflict-has-one-kind shape that the F-7 medevac reclassification at RH-S148-1 showed is itself contested, reserving a slot is itself a commitment to fill it, and forward-compatible migration on second-arc evidence is the cheaper reversible path. All three perspectives concur in rejecting (A) immediate-promote: 4-to-3-to-4 sub-type oscillation across RH-S139-1 RH-S140-1 RH-S143-1 RH-S148-1 RH-S149-1 and 6-to-5 closure-shape fold across EF-S147-1 RH-S148-1 RH-S149-1 within a single arc constitute load-bearing count instability that precludes kernel-elevation under DV-S151-1 stage-gate-discipline; sub-types are plausibly domain-coupled (contested-authority endemic to authority-coordination). Convergence majority adopts (C) at the workspace-experimental layer with explicit constraints honouring P-3 minority: typed-observation columns live on the harness substrate kind not on kernel rows, methodology mentions the pathway as permitted but names no canonical values, the slot is opt-in with NULL as valid default, and a graduation-review trigger must be specified before second-arc evidence accumulates lest (C) decay into permanent halfway house. P-3 (B) preserved as documented minority M-1 with the substantive critique that even unenumerated typed slots commit to a question-shape the application has shown can be contested. Cross-family P-2 contributed the quiet-pseudo-standardisation risk reading: once a kernel field exists operators may copy disaster-response atoms as if they were blessed types even without enum enforcement; this risk is folded into the action set as a methodology-text constraint requiring explicit non-canonical wording when describing the typed-observation pathway. OI-S151-2 closes through this synthesis. Two follow-on issues open: OI-S152-1 typed-observation columns at workspace-experimental harness substrate kind to be added in OI-S151-1 ergonomic-fix coding session or successor; OI-S152-2 graduation-review trigger criteria for promoting (C) to (A) when second-arc evidence accumulates.

### Synthesis points

- **convergence C-1.** P-1 anthropic and P-2 openai converged on C hybrid typed-observation: nullable opt-in conflict_kind closure_kind at workspace-experimental layer no enum no canonical values.
- **convergence C-2.** All three perspectives reject A immediate-promote: 4-to-3-to-4 sub-type and 6-to-5 closure-shape count instability across single-arc reflective passes precludes kernel-elevation.
- **convergence C-3.** All three identify a future-arc graduation trigger as essential whether count-threshold stability-threshold or vocabulary-convergence; specific form differs but principle converges.
- **minority M-1.** P-3 honestly held B hold-external: unenumerated typed slot still commits kernel to one-conflict-has-one-kind shape contested at RH-S148-1; reserving a slot is itself commitment to fill it.
