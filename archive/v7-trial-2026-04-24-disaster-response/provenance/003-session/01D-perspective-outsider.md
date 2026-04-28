---
session: 003
title: 01D Outsider — raw perspective
date: 2026-04-24
status: complete
perspective: outsider
committed_at: 2026-04-24
---

## Q1

I would not treat D-019 as a mandate for a view catalogue. Its wording is narrower: *"The multi-view model form is the preferred revision direction for Session 003 or later."* Preferred direction is not proof that five views are needed. The empirical signal from Session 002 is mainly per-service chain re-derivation: `SVC-03` dialysis through `INF-04`/`INF-01`, generator/fuel chains via `INF-30`/`INF-32`, cold-chain `SVC-08` through power, and telecoms `SVC-13` through `INF-17`/`INF-14`.

My proposed v2 shape is four parts:

1. **Canonical ID register**: a compact preservation layer for all `POP-*`, `INF-*`, `SVC-*`, `DEP-*`, `EXT-*`, `SIL-*`. This subsumes v1’s six-section form rather than keeping it as the main reading path.
2. **Dependency-chain index**: organised by `SVC-*`, with downstream `POP-*`, upstream `INF-*`, `DEP-*`, `EXT-*`, `ASM-*`, and touching `SIL-*`. This directly answers the 23 Session 002 re-derivations.
3. **Cohort-service matrix**: organised by `POP-*`, especially `POP-08` through `POP-15`, showing consumed services and highest-risk upstream dependencies.
4. **External and silence exposure view**: `EXT-*` roles and `SIL-*` first-class entries grouped by affected IDs, not buried in notes.

I would make settlement-local topology a secondary attribute inside the above unless the actual v1 text shows multiple chains where location, not service dependency, was the source of confusion. Session 001 D-006 chose “settlement as attribute, not axis”; overriding that needs a stronger warrant than the brief provides.

Frame-completion contribution: a structurally different alternative would be to leave `system-model.md` v1 intact and add a separate `derivation-index.md` keyed to Session 002 decision/re-derivation instances. That may be cleaner than recasting the whole model as “views”. But because Session 003’s increment specifically asks for `system-model.md` v2, I would incorporate the derivation index as the dominant v2 reading path.

## Q2

v1 IDs remain canonical. I would avoid new durable row IDs like `COH-POP-09` unless the row represents a genuinely new entity or assumption. Most view rows should be keyed by existing IDs, for example:

`POP-09 | consumes SVC-03 | upstream INF-04, INF-02, SVC-07, INF-15 | assumptions ASM-11 | silences SIL-*`

That row is not a new object; it is a projection over canonical objects. The discipline should be stated in frontmatter or a “model discipline” section: only `POP-*`, `INF-*`, `SVC-*`, `DEP-*`, `EXT-*`, `SIL-*`, and ledger IDs are canonical; view rows are non-canonical rearrangements.

To prevent drift, I would add a mechanical cross-reference table: every canonical ID appears exactly once in the canonical register and may appear many times in views. The v2 model should include a short “ID coverage checklist” by family: `POP-* all present`, `INF-* all present`, etc. That is not perfect enforcement, but it is much better than relying on reader memory under session pressure.

## Q3

`ASM-19` should split because “fillable recipient” and “delivery partner reliability” fail in different ways.

`ASM-19a`, recipient-reliability: the 10-day plan has a central-government counterparty able to receive, interpret, and act on requests.  
Falsifier: no named recipient, no acknowledged channel, or repeated non-response inside the plan’s review window.

`ASM-19b`, delivery-reliability: actions requiring `EXT-01` as an operational delivery partner can actually receive tasking, allocate resources, and execute deliveries.  
Falsifier: `EXT-01` acknowledges requests but cannot move supplies, staff, permissions, or transport at the required time.

Both need review triggers. `ASM-19a` should trigger on contact failure or ambiguous ownership. `ASM-19b` should trigger on missed delivery commitments or inability to provide delivery-path evidence.

The v2 external view should expose these separately as `EXT-01 recipient role` and `EXT-01 delivery role`, not as one reliability attribute. `RSK-019` should be flagged for Session 004+ update to reference both, because the brief says it is cross-cutting and traverses four streams.

## Q4

I lean against making `POP-12a` and `POP-12b` fully canonical at v2 unless the actual v1 `POP-12` row already contains enough internal structure to avoid invented counts. Session 001 D-007 declined the split on count-silence grounds tied to `ASM-06`; that was a good anti-laundering move. Session 002 [01C, Q2] then showed the split is structurally invisible, but “invisible” does not necessarily mean “new canonical cohorts required.”

I would expose the differentiation inside the cohort-service matrix as subrows under canonical `POP-12`:

`POP-12 oxygen-dependent subgroup | hours-band | count unresolved by ASM-06/SIL-*`  
`POP-12 CPAP-dependent subgroup | 1-3 days band | count unresolved by ASM-06/SIL-*`

If the team chooses canonical split anyway, the falsifier for each count silence is the same kind of closure evidence: a verified roster, provider list, or household-level enumeration separating oxygen dependence from CPAP dependence. Without that, `POP-12a` and `POP-12b` risk looking more precise than the workspace permits.

## Q5

Use copy-plus-reference. Preserve v1 as `applications/001-disaster-response/system-model-v1.md` with `status: superseded`, and let `system-model.md` become canonical v2. Git history alone is too implicit for a provenance-heavy workspace.

v1 frontmatter should add:

```yaml
status: superseded
superseded-by: system-model.md
superseded-session: 003
```

v2 frontmatter should add:

```yaml
status: current
version: v2
supersedes: system-model-v1.md
last-revised-session: 003
```

A `version-history:` list is better if the engine expects repeated revisions, but `supersedes:` is enough for this increment. The important point is that the chain is legible without reading git history.

## Q6

Yes. A chain-native v2 will make several v1 risk/action rows look thin.

`RSK-014` is the clearest. If generator fuel has multiple downstream effects across `POP-10`, `POP-11`, and `SVC-01`, then a blank `cohort_affected` becomes visibly under-specified once v2 shows shared upstream nodes like generator/fuel dependencies.

`RSK-019` should split or at least expand its dependency references after the `ASM-19a`/`ASM-19b` distinction. A single `EXT-01` reliability concern will no longer be specific enough if v2 distinguishes recipient failure from delivery failure.

`ACT-005` also becomes thinner if cold chain spans `POP-13`, `POP-14`, and `POP-15` with different time windows. The v2 chain view would naturally show that one action is carrying several distinct windows and downstream cohorts.

`RSK-015` looks like another follow-on candidate because freight rail bridge and fibre shared-fate link transport and telecom dependencies. If `SVC-13` telecoms depends on `INF-17` fibre via `INF-14` bridge carriage, sparse dependency text will understate the coupling.

`RSK-008` aged-care cluster welfare may need a richer chain if `POP-*` aged-care cohorts depend on welfare checks, access, communications, power, and referral transport. I would flag these for Session 004+, not edit them in Session 003.

## Q7

The biggest laundering risk is the word “views” itself. It can quietly import enterprise-architecture habits: TOGAF, Zachman, C4-style diagrams, DoDAF, ArchiMate, or generic systems-modelling notation. I am not proposing adoption of those frames. My proposed “views” are workspace-local indexes over existing IDs, justified only by Session 002’s 23 re-derivation instances and [Session 001 01-deliberation.md §5.1].

UN/IASC clusters resemble a service-family organisation. This was surveyed and declined at v1 as `EXT-SURVEY-02`; I would continue to decline it. The v2 `SVC-*` chain index is not a cluster catalogue and should not rename services into external cluster headings.

Lifelines or critical-infrastructure-sector taxonomies resemble the `INF-*` upstream grouping. This was surveyed and declined at v1 as `EXT-SURVEY-04`; I would decline adoption again. The model should keep v1 `INF-*` IDs and local dependencies.

ICS/NIMS resembles an external-actor/roles view. It was surveyed and declined at v1 as `EXT-SURVEY-01`; do not use it to structure `EXT-01`.

Causal-loop diagrams and formal systems-dependency modelling are adjacent to the dependency-chain index. I am ambivalent but not proposing adoption. A plain table keyed by `SVC-*`, `POP-*`, and `DEP-*` is enough.

## Honest limits

I cannot verify exact v1 row wording, exact `SIL-*` identifiers touching `POP-12`, or the full text of `RSK-014`, `RSK-019`, `ACT-005`, `RSK-015`, and `RSK-008` from the brief alone. I am relying on the supplied summaries and examples. I also cannot know whether settlement-local topology deserves first-class status without seeing how often Session 002 reasoning actually depended on place rather than service-chain depth.
