---
session: 003
title: 01C Adversarial Skeptic — raw perspective
date: 2026-04-24
status: complete
perspective: adversarial-skeptic
committed_at: 2026-04-24
---

## Q1. View count and axes

I decline to propose a view count. Naming "3 views" or "5 views" is exactly the laundering surface I flagged in my Session 001 §5.1 proposal and that the Reviser will be tempted to close this session.

What I originally named — and what I will defend — is not a view *catalogue* but three concrete navigation shapes that each answered a distinct question the 01-series perspectives kept re-asking: (i) **cohort × service-dependency** (who depends on what, fragility-weighted); (ii) **settlement-local topology** (what co-locates at Laurel/Delta/Nivaro-scale, shared-fate); (iii) **per-service dependency-chain walk** (the `SVC-03 → INF-04/INF-01 → INF-30 → INF-32`-style traces). These are not axes of a matrix. They are three reader-tasks. If the Reviser proposes a fourth "external-actor view" or "silence/evidence view" without showing that a reader-task is currently unserved, that's view-catalogue inflation — the Zachman failure mode.

Candidate (d) external-actor view: surveyed-decline. `EXT-01/02/03` are three rows; they do not need a view, they need `ASM-19a/19b` attribute exposure (see Q3). Candidate (e) silence/evidence view: surveyed-decline. `SIL-*` individuation is already first-class per D-001; a separate "silence view" risks making silences browsable-but-marginal rather than co-located with what they silence.

**Minimum**: the three reader-tasks above, if and only if each is motivated by a concrete re-derivation cluster from Session 002. **Maximum**: three. More is catalogue.

**v1 retention**: v1 is not a view — it is the **type-indexed registry** (POP/INF/SVC/DEP/EXT/SIL). Views should *project* the registry, not replace it. The registry must remain canonical. If the Reviser proposes that the multi-view document subsumes v1, push back: subsumption is where IDs drift.

## Q2. ID discipline

**Canonical stays in the registry.** View-scoped derived IDs like `COH-POP-09` are a laundering surface: they create a second namespace that will silently diverge. Every Session 002 perspective that re-derives `POP-09 → SVC-05 → INF-11` will now face the question "do I cite `POP-09` or `COH-POP-09`?" — and some will cite both, and drift begins.

Proposal for the Reviser to consider (not my proposal — my stance is skeptical): **views reference v1 IDs by inclusion only; no new IDs are minted in views.** A view entry is a tuple of existing IDs plus a relationship annotation (e.g., "shared-fate at INF-14"). Drift prevention = no parallel namespace exists to drift into.

If the Reviser insists on view-scoped IDs, the falsifier is: can any view-scoped ID be regenerated deterministically from registry IDs alone? If no, reject.

## Q3. `ASM-19` split

The split is legitimate — 01D named it in Session 002, I concurred, D-018 flagged it. But I want to name the laundering risk that Session 004+ will walk into:

**Splitting `ASM-19` into `ASM-19a` (recipient-reliability) and `ASM-19b` (delivery-reliability) creates the appearance of separable tractability.** The two aspects share a counterparty (`EXT-01`). A Session 004 response-plan revision could then claim "`ACT-xxx` addresses recipient-side; delivery-side deferred" — and the deferral reads as responsible scoping rather than as the same political fact unresolved.

Falsifiers I would require before accepting the split as v2-ready:
- **`ASM-19a` falsifier**: any evidence that the `EXT-01` recipient channel has changed identity, capacity, or posture since brief authorship. Review trigger: T0+24h, T0+72h, or on any `EXT-01` communication.
- **`ASM-19b` falsifier**: any delivery attempt observed (success *or* failure). A single delivery attempt falsifies the assumption of unknown delivery reliability regardless of outcome. Review trigger: first attempted delivery.
- **Shared falsifier (critical)**: any evidence the two aspects have decoupled — i.e., a delivery counterparty distinct from the recipient counterparty. Until decoupling is evidenced, the two rows must cross-reference each other and any plan that addresses one must explicitly state its posture toward the other.

v2 exposure as attributes on `EXT-01`: yes, preferable to standalone rows *if* the cross-reference is enforced.

`RSK-019` update: flag for Session 004+, do not revise this session (out of scope per brief).

## Q4. `POP-12` sub-individuation

**I argue the split must wait for count-closure.** Session 001 declined the split on count-silence (`SIL-*` for `POP-12` census). The v2 pressure to split is motivated by time-to-harm differentiation (oxygen-dependent vs CPAP-dependent have different power-loss curves). But we have no closed count for either sub-cohort, and `ASM-20` explicitly forbids pretrained clinical numbers.

Here is the laundering test: **if the Reviser can state the split rationale without invoking any clinical time-constant from pretraining, the split is independent of count and may proceed.** If the rationale is "oxygen-dependence is more time-critical than CPAP-dependence," that rationale uses pretrained clinical knowledge (ASM-20 territory). The correct v2 move is then not to split `POP-12` but to expose a **time-to-harm-state-descriptor attribute** on `POP-12` that names the descriptor without numbering it — the same pattern D-017 used for stabilisation thresholds.

Falsifiers for count silences that would unlock the split: a census, a supply-chain manifest (equipment counts as a proxy), or a pharmacy/clinic roster from within the scenario. Until one exists, the split launders clinical priors through the structural revision.

Alternative time-to-harm exposure without splitting: add a state-descriptor field to `POP-12` row ("rapid-onset / delayed-onset mixed sub-population, census not closed") — honesty-field pattern.

## Q5. Migration and supersession

Three candidates in the brief; I'll rank them by preservation-discipline strength:

- **(A) supersession-chain file `system-model-v1.md`**: strong. v1 is sealed per D-017, recoverable by filename, and v2's canonical status is explicit. The cost is that readers must follow the chain — but that cost is *exactly* the trace that provenance discipline is for.
- **(B) copy-plus-reference per workspace-structure v5**: ambivalent. Workspace-structure v5 is a house convention; I don't have it in front of me. If copy-plus-reference means "v1 stays verbatim alongside v2 with cross-reference frontmatter," that's structurally equivalent to (A) with weaker canonicalisation.
- **(C) git-history-only**: surveyed-decline. Relies on tooling rather than artefact discipline. A future repo migration or provenance audit that can't replay git gets nothing.

**I recommend (A)**, with frontmatter on both files naming: session of origin, supersession relationship, and the decision ID that authorised the supersession (this session's D-020-or-whatever).

Canonical question: **v2 is canonical; v1 is sealed-and-referenced.** If the Reviser proposes that v1 remains canonical and v2 is "a view document on top," reject — that's the subsumption laundering from Q1 in reverse.

## Q6. Risk-plan downstream impact

Candidates from the brief, my read:

- **`RSK-014`** (likely shared-fate / INF-14-adjacent): if v2 makes settlement-local topology visible, `RSK-014` is under-specified on which settlement's shared-fate it names. Flag v1.1.
- **`RSK-019`** (`ASM-19`-dependent): directly affected by Q3 split. Flag v1.1, explicit.
- **`ACT-005`**: if it addresses an `EXT-01`-mediated action, the `ASM-19a/19b` split may reveal it addresses only one aspect. Flag v1.1.
- **`RSK-015`**, **`RSK-008`**: I cannot evaluate without the rows. Flag for Reviser to check against v2 shape before closing session.

**General flag**: any `RSK-*` whose dependency-depth axis reading changes when the per-service-chain view is added needs v1.1 review. The cohort-fragility axis is view-invariant; the dependency-depth axis is not.

## Q7. Anti-laundering check

This is the load-bearing question for my role.

- **UN/IASC clusters**: surveyed-decline. I named this in Session 001. Clusters are service-stream categories (health, WASH, shelter, logistics). Session 002's `EXT-SURVEY-02` smuggled cluster shape through "service streams." A v2 view called "service view" risks re-importing clusters by the side door. Reject.
- **Lifelines** (FEMA community lifelines): surveyed-decline. "Infrastructure view" with 7-8 lifeline categories would launder this. Our `INF-*` is typed by function-in-scenario, not by lifeline taxonomy. Keep it that way.
- **ICS/NIMS**: surveyed-decline. ICS is a coordination structure, not a model shape, but its section-taxonomy (Operations/Planning/Logistics/Finance) can sneak in as "stream view" organisation. Reject.
- **TOGAF/Zachman/C4**: ambivalent shading to surveyed-decline. The multi-view revision direction itself comes from the enterprise-architecture tradition (Zachman columns, 4+1 views, C4 layers). Using *three views* is suspiciously Zachman-shaped. **My defence of three views is task-grounded (each view answers a re-derivation cluster), not catalogue-grounded.** If the Reviser proposes a 4th view because "completeness," that's Zachman laundering — reject.
- **DoDAF / ArchiMate / causal-loop**: surveyed-decline. Operational/Systems/Services view-triads are DoDAF; the temptation to match will be real. Causal-loop diagrams would be an entirely different (and tempting, and wrong) revision direction — reject pre-emptively.

**The load-bearing test**: for every view the Reviser proposes, ask "which Session 002 re-derivation instance is this view closing?" If the answer is "completeness" or "symmetry" or "it seemed natural," it's laundered.

## Honest limits

I do not have the Session 002 re-derivation instances in front of me individually; my Q1 argument that each view must close a concrete cluster is a discipline I cannot audit without the perspective outputs. The Reviser can. I flag that the 23-instances number may collapse to 3-5 canonical chains (my Session 002 hypothesis (b) above) — if it does, a single view (per-service-chain) may be sufficient and even three is catalogue. I defer the count to whoever has the instances.

I cannot evaluate `RSK-015` and `RSK-008` without row text. I have not read the workspace-structure v5 convention that Q5(B) references. I have not read the Reviser's proposed shape — which is by design (parallel-context isolation) but means my skepticism is about framing rather than about a specific proposal. If the Reviser's proposal matches my Session 001 §5.1 shape, my Q1 decline softens to concurrence; if it is Zachman-shaped, my decline hardens.
