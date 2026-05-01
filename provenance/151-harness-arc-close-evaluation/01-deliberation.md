---
session: 151
title: harness-arc-close-evaluation — deliberation
generated_by: selvedge export
---

# Deliberation

## D-19 — reference_harness disposition at disaster-response arc close: promote / retire / scope-change

sealed_at: 2026-05-01T11:22:57.881Z

### P-1 (anthropic)

**Position.** C (Scope-change): keep reference_harness workspace-experimental, fix five ergonomic frictions, and tighten structural-condition trigger before any kernel-promotion vote.

**schema_sketch.**
- Promote atom_type=finding ceiling from 240 to substrate general envelope (or split finding_short/finding_long if uniformity is load-bearing) — addresses friction #2.
- Add harness_assumptions.origin_session_id resolution rule: handler MUST NOT rebind when the field is explicitly populated; bind-on-null only — addresses friction #1.
- Add harness_visibility_link association atom (optional, multi-valued) from a harness claim to deliberation atoms supplying supports/effects/alternatives discipline — addresses friction #5.
**cli_surface.**
- Add --dry-run to all harness-* submit kinds; validate atom-length, alias format, and FK resolution before mid-submit refusal — friction #4.
- Update CHECK error message on alias mis-format to name RH-SNNN-N explicitly with one example — friction #3, cheap.
- No new submit kind, no third validation sense at kernel layer yet; the handler stays workspace-experimental.
**migration_path.**
- Migration 026: relax atom_type=finding length ceiling (or split type); back-compat read for existing rows.
- Migration 027: harness_assumptions.origin_session_id bind-on-null handler change; no row rewrite.
- Migration 028: introduce harness_visibility_link association atom; nullable, optional; no back-fill required.
- Engine bump v37 to v38 on 026; v38 to v39 on 028. 027 is handler-only, no engine bump.
**what_not.**
- Not proposing kernel-promotion to a third validation sense at this arc-close.
- Not proposing retirement or substrate-kind tombstoning.
- Not proposing to subtract the workspace-experimental layer from reference_harness or shift other primitives onto it.
- Not proposing to canonicalise the four sub-types or 5–6 closure shapes; that is a separate kernel-layer typed-conflict-primitive deliberation.
**open_question.**
- What structural-condition trigger criterion will the engine use to fire reference_harness non-discretionarily in a future arc, as a substrate-enforced predicate over arc-state?
- Without that predicate, kernel-promotion is premature even if a second arc replicates — the third sense needs an engine-detectable fire-condition, not an operator-declared one.
**risk.**
- Failure mode of (C) is indefinite deferral: workspace-experimental becomes a permanent holding pen and second-arc replication never gets prioritised.
- Mitigation: bind (C) to an explicit re-evaluation gate at the close of the next structural-gap arc, and require the trigger-criterion question be resolved before that re-evaluation.
**what_lost.**
- Versus status quo: small migration cost (026–028) and one engine bump cycle.
- Versus (A): forgo the cleaner methodology-spec story kernel-promotion would tell, and keep the workspace-experimental cognitive overhead for one more arc.
- Versus (B): keep the substrate-kind surface area and the 240-char-class friction the harness imposes on agent attention.
- Net: cost is bounded, paid in migrations and one arc of patience, against single-arc-overfit insurance and a real trigger-criterion answer.

### P-2 (openai)

**Position.** C (Scope-change): keep reference_harness as a promising validation instrument under structural absence, but explicitly reject kernel-grade promotion on one-arc evidence.

**schema_sketch.**
- Keep the substrate kind, but split current submission session from assumption origin session so harness_assumptions.origin_session_id cannot silently rebound during cross-arc use.
- Add an explicit structural_trigger enum or constrained field, such as fictional_domain, future_domain, inaccessible_domain, and domain_actor_absent_by_design.
- Expand atom_type=finding length to match the substrate general envelope, since the 240-char ceiling degraded specificity during pilot use.
- Add a decision-to-deliberation trace field for kind=substantive artefacts so supports/effects/alternatives discipline is reconstructable without external reader knowledge (RH-S147-1 strain).
- Do not encode the four observed conflict sub-types as kernel primitives yet; store them as typed observations pending another arc.
**cli_surface.**
- Add harness-submit --dry-run or equivalent preflight for atom length, alias format, enum validity, and load-bearing/result consistency.
- Improve CHECK and handler errors so the accepted RH-SNNN-N alias form is named directly, avoiding the HRN-to-RH learning failure.
- Add an explicit origin flag, such as --origin-session, whose behavior is shown before submit and is not overwritten by the handler.
- Add a trigger declaration prompt for the structural condition, requiring the operator to state why no domain-actor can fire.
- Add a trace prompt for substantive decisions when the harness relies on deliberation atoms not visible in the artefact-set.
**migration_path.**
- Migration 026 should separate current session ownership from assumption origin identity, backfilling existing harness rows from recorded pilot/session metadata where unambiguous.
- Migration 027 should widen atom_type=finding storage and update validation constraints to the general substrate envelope.
- Migration 028 should add structural_trigger and nullable decision trace fields, then backfill known disaster-response pilots with the appropriate structural condition.
- Migration 029 should add any indexes needed for querying harness claims by trigger, load-bearing status, and result.
- CLI and handler changes should land after 026 and 028, otherwise dry-run would validate against the old ambiguous shape.
**what_not.**
- Not proposing promotion to a kernel third validation sense at this close.
- Not proposing retirement or tombstoning; RH-S137-1, RH-S146-1, RH-S147-1 show value beyond diagnostic setup.
- Not proposing 0-broken be treated as proof of correctness; a self-grading harness can be useful without being independent validation.
- Not proposing to canonicalise source-vs-source, demand-vs-supply, plan-vs-resource, and contested-authority as final kernel conflict primitives.
- Not proposing to widen harness firing to ordinary arcs where operator-validation or domain-actor receipt is available.
**open_question.**
- Is the harness validating contradiction-detection, or validating a disciplined internal review protocol that happens to catch contradictions?
- A second arc should test whether the same mechanism finds issues under different artefact genres, not just disaster-response closure patterns.
- Conflict sub-type evidence across RH-S139-1, RH-S140-1, and RH-S143-1 is suggestive but not yet enough to decide kernel ontology.
**risk.**
- The risk of scope-change is institutional drag: workspace-experimental primitives can become permanent without facing a promotion or retirement threshold.
- Tightening triggers may under-sample edge cases where the harness would have exposed useful contradictions, especially in hybrid arcs with partial actor access.
- Adding schema and CLI ceremony could make operators optimize for passing harness form rather than making falsifiable contradiction claims.
- Trace additions may blur the boundary between artefact content and deliberation metadata if not kept narrow.
**what_lost.**
- Compared with immediate promotion, this loses the chance to make structural-domain absence a first-class kernel validation pathway now.
- Future sessions carry experimental overhead, including explicit trigger declarations and migration maintenance.
- Compared with status quo, the proposal removes some looseness: operators have less freedom to use the harness as a general reflective review tool.
- Cost is acceptable: pilots show real signal but not enough independence; RH-S148-1 and RH-S149-1 strains support retention, not promotion.

### P-3 (anthropic)

**Position.** B (Retire with tombstone): the harness has paid its dividend in findings, not mechanism; harvest the signals and let the next typed-conflict primitive be born clean.

**schema_sketch.**
- None additive. Tombstone the reference_harness substrate kind (migrations 023–025) by marking it retired-readonly in a new migration 026.
- Existing pilot atoms (RH-S137-1 … RH-S149-1) remain queryable as historical evidence; new kind=harness-* submissions refused at the handler with a pointer to the retire-rationale atom.
- No new columns, enums, or FKs; frictions 1–4 (240-char ceiling, origin_session_id ambiguity, missing --dry-run) evaporate once the kind stops accepting submissions.
**cli_surface.**
- Subtract, do not add. Retire harness-assumption, harness-claim, harness-grade, harness-pilot submit kinds at the handler boundary; keep read paths (list/show) for provenance.
- No new submit kind replaces them. The kind=substantive decision flow (visibility-gap friction 5) is unaffected and should be addressed in its own seam.
**migration_path.**
- Migration 026 only: reference_harness.status enum gains retired; default flips; handler guard added. No backfill, no data move, no schema rename.
- Order: (i) land retire-rationale atom citing this deliberation and the 8-pilot table, (ii) ship 026, (iii) update methodology.md kernel cautions to record harness retired post-arc.
- Engine bump engine-v38 marks the retirement; no v39 follow-on implied by this path.
**what_not.**
- Not proposing deletion of pilot atoms; they are evidence, not debt.
- Not proposing a replacement third validation sense; the typed-conflict-primitive question is unresolved and should remain so here.
- Not proposing promotion-with-conditions framed as soft-promote; that is just A wearing Bs clothes.
- Not rolling visibility-gap friction (RH-S147-1 strain, RH-S146-1 dissent) into harness disposition; it is a separate kernel question about deliberation-atom reachability.
- No change to the operator-validation / domain-actor-receipt pair. Two senses, not three.
**open_question.**
- What is the structural-condition trigger for the next primitive? The harness fired on lacks-domain-actor, which conflates fictional, future-facing, and contested-authority cases.
- The 8 pilots produced 4 sub-types of conflict and 5–6 closure shapes; that data is the input to a typed-conflict-primitive design, but the design itself is out of scope for D-1.
- Cannot resolve here whether the successor primitive should be conflict-shape-typed (sub-type-first) or closure-shape-typed (resolution-first); the choice matters.
**risk.**
- The dominant failure mode of retire is premature subtraction: a different-structural-condition arc might surface contradiction patterns the 8 disaster-response pilots did not.
- Mitigation is partial only: the tombstone is reversible (un-retire in migration 027), but agent-side per-claim grading discipline degrades fast once the substrate stops enforcing shape.
- Honest cost: we may re-derive 30–40% of the harness mechanism in 6–10 sessions if the next arc forces it.
**what_lost.**
- Versus C (scope-change), retire loses cheap insurance of having the harness available if a non-disaster-response arc needs it.
- Versus C, retire loses ergonomic-fix work already half-scoped against frictions 1–4, which becomes sunk.
- Versus C, retire loses some agent-discipline reinforcement; per-claim grading is a useful muscle the substrate enforced.
- Versus A (promote), retire loses kernel-elevation of a 0%-break, 92%-survive validator that did work.
- Honest counter: it worked is not the kernel needs it forever; the harness was scaffolding for a kernel question now ripe to ask directly. Subtract scaffolding; ask the question.

### Synthesis

Three perspectives convened on reference_harness disposition at disaster-response arc close. P-1 anthropic primary and P-2 openai cross-family converged on (C) scope-change: keep workspace-experimental, address five ergonomic frictions (origin_session_id rebind, finding atom-length 240 ceiling, undocumented RH- alias format, missing harness-* dry-run, visibility-gap from artefact-set to deliberation atoms), tighten the structural-condition trigger to a substrate-detectable predicate, and gate kernel-promotion to a second structurally-gap arc's evidence. P-3 anthropic adversarial-minimalist honestly converged on (B) retire-with-tombstone: the harness's value is in the typed-conflict-primitive findings it forced into view (4 sub-types, 5-6 closure shapes, lesson-internalisation observability) not the mechanism, and any retention adds kernel surface the typed-conflict-primitive work will have to reconcile with. Convergence majority adopts (C); P-3 (B) is preserved as documented minority M-1 with the typed-conflict-primitive seam opened as separate OI per P-3's strongest argument that bundling visibility-gap and sub-type-canonicalisation into harness disposition is exactly the accumulation pressure to resist. Cross-family P-2 contributed the contradiction-detection-vs-disciplined-review-protocol distinction and the structural_trigger enum proposal (fictional_domain / future_domain / inaccessible_domain / domain_actor_absent_by_design); both are folded into the scope-change action set. All three perspectives reject canonicalising the four sub-types or 5-6 closure shapes as kernel primitives on this evidence; that question is opened as OI-S151-2. Visibility-gap (RH-S147-1 strain, RH-S146-1 dissent) is opened as OI-S151-3 separate from harness disposition. Re-evaluation gate at next structurally-gap arc close is opened as OI-S151-4 with explicit predicate that the structural-trigger criterion must be substrate-detectable before that re-evaluation, not after. DV-S124-3 deferred-decision resolves through this synthesis (kernel-promotion deferred to next arc evidence with scope-change adopted in the interim). OI-S124-1 closes with scope-change disposition.

### Synthesis points

- **convergence C-1.** P-1 anthropic and P-2 openai converged on scope-change C: keep workspace-experimental, address five ergonomic frictions, gate kernel-promotion to second-arc evidence.
- **convergence C-2.** All three perspectives reject canonicalising 4 sub-types or 5-6 closure shapes as kernel primitives on single-arc evidence; that is a separate seam.
- **convergence C-3.** Visibility-gap from artefact-set to deliberation atoms is acknowledged by all three as a separate seam beyond harness disposition.
- **minority M-1.** P-3 honestly converged on B retire-with-tombstone: harness value lives in findings forced into view not mechanism; retention adds kernel surface typed-conflict work must reconcile with.
