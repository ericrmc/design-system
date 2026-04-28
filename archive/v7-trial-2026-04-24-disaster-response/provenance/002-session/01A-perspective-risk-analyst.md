---
session: 002
title: Perspective — Risk Analyst
date: 2026-04-24
status: complete
perspective: Risk Analyst
committed_at: 2026-04-24
---

# Perspective: Risk Analyst

## Methodology context acknowledgement

I accept the Session 002 brief's methodology constraints: reason from the shared brief plus upstream summarised keys, refuse silent import of pretrained emergency-management knowledge (any such import must be named and declined in the surveyed-inputs section per PROMPT.md anti-laundering), preserve cohort individuation (D-003 / DEC-05 — aggregation of medical-fragility cohorts into a single figure is a laundering failure rather than a simplification), and note each instance where the single-document system-model form was insufficient for risk identification (§5.1 activation counts).

## Q1. Risk register minimum structural sufficiency

The v1 risk register must be a **row-per-risk table** whose columns are chosen so each entry is (a) traceable four-ways per D-010 (action → risk → service/infrastructure → assumption), (b) linked to at least one concrete cohort or asset, and (c) carries its time-to-harm qualitatively without importing numeric windows.

I propose these minimum columns:

1. **`risk_id`** — zero-padded sequential ID with the prefix `RSK-` (e.g. `RSK-001`). Stable across sessions; never reused if a risk is retired — retired risks remain in the register with a status of `retired` and a `retired_in` session pointer. I reject sub-prefixing by severity band (`RSK-H-01` etc.) because severity must be allowed to change between sessions without an ID churn.
2. **`title`** — short human-readable phrase. Not a free-text narrative; the narrative goes into `description`.
3. **`description`** — one to three sentences stating the harm pathway in the form "if X then Y to Z", where Z is a cohort, service, or infrastructure node (not "to the population").
4. **`cohort_affected`** — one or more `POP-*` IDs from the system model. Empty only when the affected population is a silence (`SIL-*`), in which case the cell carries the `SIL-*` and an `uncohorted: true` flag that marks the entry for follow-up. A risk with no cohort and no silence pointer is rejected at schema validation.
5. **`infrastructure_affected`** — zero or more `INF-*` IDs. Zero is permitted only if the risk is purely about a cohort's exposure independent of any infrastructure node (e.g. an outer-islet silence risk); in that case an `infrastructure_affected_silence` flag must be set to surface the hole.
6. **`service_affected`** — zero or more `SVC-*` IDs. At least one of `infrastructure_affected` or `service_affected` must be non-empty — this is what prevents free-floating fears from being logged as risks.
7. **`dependency_chain`** — zero or more `DEP-*` IDs that the risk traverses. Blank is permitted but flagged: a risk whose harm pathway can't point to at least one dependency edge is frequently a sign that the dependency needs to be added to the system model, not that the risk is weak.
8. **`time_to_harm`** — qualitative band, one of a closed vocabulary fixed at v1: `hours`, `1-3 days`, `days`, `week+`, `window-unknown`. Per DEC-06 and ASM-20, numeric values (e.g. "36 hours", "72 hours") are forbidden unless the number appears in the brief's T0 state text (e.g. the utility's "3–7 days") and is carried as a *reported* figure with a source cell, not as clinical knowledge. `window-unknown` is a valid entry, not a drafting failure; it surfaces a silence.
9. **`time_to_harm_source`** — one of `brief-stated`, `assumption-ledger`, `inferred-from-dependency`, `silence`. Forces the register to declare *why* the window is what it is. A `brief-stated` pointer cites the brief statement; `assumption-ledger` cites `ASM-*`; `inferred-from-dependency` cites the `DEP-*` that drove the inference; `silence` cites `SIL-*`.
10. **`premises`** — one or more `ASM-*` / `GIV-*` / `CON-*` / `SIL-*` IDs that the risk depends on. This is the "assumption" edge of the four-link chain. If all premises are silences, the risk is flagged `premise-weak` so synthesis can see it.
11. **`severity_band`** — qualitative: `critical`, `high`, `moderate`, `watch`. Populated only when the prioritisation method (Q2) is applied; blank is acceptable at first write. Numeric likelihood×impact scores are explicitly excluded (see Q2).
12. **`status`** — `open`, `monitoring`, `mitigated`, `retired`, `escalated-to-action`.
13. **`linked_actions`** — one or more `ACT-*` IDs from the response plan. Bidirectional with the response plan's `risks_addressed` column. Blank at first write; populated as the response plan is drafted in the same session.
14. **`silence_pointers`** — any `SIL-*` IDs the risk surfaces but is not premised on (e.g. a risk about generator fuel exhaustion points to `SIL-*` for fuel status even if the premise is `ASM-15`).
15. **`session_introduced`** — `002` for every v1 row. Retained across sessions.
16. **`notes`** — free-text, sparingly used. For drafter's reasoning, not for re-stating columns above.

**Cross-reference conventions.** I keep the Session 001 D-010 four-link rule literal: every `RSK-*` row must resolve to (cohort or service/infrastructure) **and** at least one `ASM-*`/`GIV-*`/`CON-*`/`SIL-*` premise. The response plan's `ACT-*` rows close the loop by citing `RSK-*` IDs they address. I propose that the schema be validated at commit time (a workspace-internal check, not a domain check) — a row missing the required edges is a drafting failure to be fixed, not a partially-valid entry to be kept.

**What I would leave out of v1, and why.**

- **Numeric likelihood** (e.g. 0.3, "30%"). Workspace-only validation (CON-02) cannot support calibrated probabilities; any number would be a fabrication presented as precision. Qualitative severity bands are enough to drive sort order without claiming more than we know.
- **Numeric impact in lives / dollars / bed-days.** Same reasoning; ASM-20 rules out pretrained clinical time-to-harm numbers, and impact in lives would require the very clinical numerics we've declined.
- **Per-risk owner field.** Ownership belongs to the response plan (`ACT-*` rows have owners), not the register; duplicating it invites drift. The register tells you *what can go wrong*; the plan tells you *who is doing what about it*.
- **Mitigation description column.** Same reason — that is the response plan's job. The `linked_actions` column is sufficient cross-reference.
- **Numeric likelihood×impact score.** Rejected on grounds in Q2.
- **Free-text consequence column.** Folded into `description`. A separate column invites prose-drift where the narrative contradicts the cross-refs.

**Time-to-harm treatment.** Qualitative-only per DEC-06, closed vocabulary of five values as above, with `window-unknown` as a first-class legal value. The `time_to_harm_source` column forces the drafter to declare provenance. This is the anti-laundering discipline at the risk-entry granularity: without the source cell, pretrained clinical knowledge can re-enter the schema through a "plausible" qualitative window.

## Q2. Prioritisation method

I propose **a hybrid: cohort-first partition, then time-to-harm sort within each partition, with a dependency-depth tiebreak.** Severity band (`critical/high/moderate/watch`) is derived from this sort, not inserted independently.

- **Partition 1 — individuated medical-fragility cohorts** (`POP-09` dialysis South Latch, `POP-10` dialysis Merrow Port, `POP-11` neonatal, `POP-12` CPAP/home-oxygen, `POP-13` insulin-dependent, `POP-14` refrigerated-biologic, `POP-15` other refrigerated-med, `POP-08` institutionally-housed aged). Any risk whose `cohort_affected` includes one of these is in Partition 1.
- **Partition 2 — cohort-silence risks** (`POP-05` outer-islets, `POP-02` dormitory cohort with unknown T0 occupancy). These are second because the silence itself is a risk vector — we don't know who is exposed, and the cost of the silence can only be bounded by acting to close it.
- **Partition 3 — aggregate-population risks** (`POP-03`, `POP-04`, `POP-17`, `POP-06` displaced).
- **Partition 4 — infrastructure/service-only risks** (generator fuel exhaustion `INF-30`/`INF-32`; fibre trunk shared-fate on `INF-14`/`INF-17`; levee `INF-21`) that aren't yet pinned to a specific cohort but are service-upstream.

Within each partition, sort by `time_to_harm` (`hours` → `1-3 days` → `days` → `week+` → `window-unknown`). Tiebreak by dependency-depth: risks upstream in `DEP-*` chains (their failure propagates) rank above downstream-consequence risks at the same window.

**What this gives up, named honestly:**

- **It gives up comparability across partitions.** A Partition-3 aggregate risk with a `hours` window will sort below a Partition-1 `1-3 days` risk. This is a deliberate prior — I am asserting that cohort-individuation outranks window-tightness across partitions. A pure time-ordered sort would invert this; I reject pure time-ordering because it re-launders the aggregate-vs-individuated distinction D-003 was explicit about.
- **It gives up a single total order.** Within a partition, two risks with the same window and the same dependency depth are genuinely co-ranked — the register must be allowed to show ties. A total order would force a false distinction.
- **It gives up likelihood scoring.** Workspace validation cannot produce calibrated likelihoods. I prefer unranked-by-likelihood over false-precision-by-likelihood.
- **It gives up a clean refusal to rank.** Pure "list only" is insufficient because the response plan must know where to commit scarce capacity first; an ordered register is load-bearing for Q3.

**Rejection criteria for cohort prioritisation (per §4).** I reject: (a) any prioritisation scheme that requires numeric time-to-harm values (violates DEC-06/ASM-20); (b) any scheme that aggregates `POP-09`…`POP-15` into `POP-5K-parent` for scoring purposes (violates DEC-05); (c) any scheme that ranks `POP-05` outer-islets below known-count aggregate populations on the grounds that "we don't know how many there are" — unknown count is a silence to be surfaced, not a severity reducer; (d) any scheme that uses the single-document system model's listing order as an implicit priority order (the model lists POPs in the order they were enumerated, not the order they should be served).

## Q3. Response plan minimum structural sufficiency

My structural view (the Operations Planner will have the primary one):

- **Shape.** Concurrent streams, not phased plan, not pure action-list. Concurrent streams named by the service they restore or sustain (`STR-water`, `STR-dialysis-continuity`, `STR-power/fuel`, `STR-shelter`, `STR-comms/silence-closure`, `STR-aged-care`, `STR-neonatal`, `STR-outer-islet-contact`, `STR-salvage/access`, `STR-public-information`). Branching sub-plans permitted within a stream where an action's go/no-go depends on an unresolved silence closing (e.g. `STR-outer-islet-contact` branches on the VHF `INF-19` post-surge operability check).
- **Action keying.** `ACT-NNN` zero-padded sequential, stream-agnostic so an action can migrate between streams in revision without a rename.
- **Columns per action.** `act_id`, `title`, `stream`, `description`, `cohort_served` (`POP-*`), `service_restored` (`SVC-*`), `infrastructure_touched` (`INF-*`), `risks_addressed` (`RSK-*`), `premises` (`ASM-*`/`GIV-*`), `predecessors` (`ACT-*`), `owner_role` (role-keyed, not named individuals — workspace has no actor reality), `window_placement` (see Q4), `start_condition` (a testable condition, e.g. "generator fuel status `SIL-*` closed"), `success_criterion` (observable at action-close), `status`.
- **Sequencing within 10-day horizon.** Actions carry `window_placement` (see Q4) and `predecessors`. The plan does not carry Gantt-style absolute times — that would import a precision workspace validation cannot support. Sequence is relational (A before B) plus windowed (in `WIN-acute` or `WIN-stab`).
- **Dependencies between actions.** The `predecessors` column; optionally an `enables` mirror, but one direction is sufficient if validated.

**What I leave out, and why.** Resource-count columns (headcount, vehicle count, litre-per-day potable water targets). Every such number would be a pretrained import. Gantt-style absolute durations, same reason. Budget columns — not in the brief, not derivable.

## Q4. Sub-windows as operational compartments

Treat them as **review gates, not compartments.** D-004 already rules out their use as operational compartments; I see no reason for Session 002 to overturn that. An action's `window_placement` is an *expected* window (`in-acute`, `in-stab`, `spans-both`, `window-contingent`), and a review gate at T0+72h forces every open action to be reconfirmed, re-scheduled, or retired. Actions whose `start_condition` depends on silence-closure (outer-islet count, generator fuel state, aged-care cluster flood status) naturally cluster as `window-contingent` and come up at the gate.

Rejecting the compartment reading is important: compartmentalising would force a risk whose window is `days` into `WIN-stab` even when its dependency chain runs through `WIN-acute` infrastructure actions. The stream-plus-gate structure preserves the cross-window action without smuggling a false temporal cleanliness.

## Q5. Inherited decisions-not-taken from Session 001

**(a) Cohort prioritisation.** I propose a **partial order** at v1, not a total order. The partition scheme in Q2 is a partial order: within Partition 1, `POP-09` (1,200 dialysis patients, centre inaccessible per `INF-04`, dependency chain `DEP-09` confirmed) and `POP-11` (neonatal, occupancy unknown, `INF-01` on generator) are co-critical; forcing a total order between them would require clinical time-to-harm values we've declined. Between partitions, the order is total (Partition 1 before 2 before 3 before 4). Rejection criteria as stated in Q2.

**(b) `POP-05` outer-islets.** **First-class settlement**, not special-case cohort. The count being unknown is a silence (`SIL-*`) to be closed, not a downgrade. Treating it as a cohort rather than a settlement risks folding it into "the dispersed fragility cohorts" and losing the settlement-level view (hospital access, shelter capacity, food/water supply chain, comms via `INF-19` VHF) it needs. I accept that this creates a known asymmetry — we have a population count and infrastructure enumeration for Merrow Port, South Latch, Kellan Rise, and not for the outer islets — and the asymmetry should be surfaced as a risk, not resolved by downgrading.

**(c) Definition of "stabilised" at T0+10d.** Observable criteria I would propose for the plan's success condition:

- `SVC-03` (haemodialysis) available to `POP-09` (South Latch) and `POP-10` (Merrow Port) at a frequency consistent with the pre-cyclone schedule, via any route (restored `INF-04`, referral to `INF-02` Kellan Rise, or mobile/temporary dialysis). Not "some patients receiving care" — the cohort-individuation rule forbids the aggregate phrasing.
- `SVC-04` (potable water) restored for `POP-17` ~27K Merrow Port residents not on backup-well rotation, *or* a documented interim supply in place.
- `SVC-05` (electrical supply) at `INF-01` regional hospital either restored from grid or with confirmed fuel continuity for `INF-30` beyond the planning horizon.
- `SVC-13` (telecom) to Kellan Rise does not depend solely on `DEP-15` (`INF-17` via `INF-14` carriage).
- `SIL-*` for outer-islet count, neonatal occupancy, and aged-care cluster flood status are closed (whether the answer is good or bad).
- `POP-06` ~18K displaced (per `ASM-03` baseline) has a shelter-pathway observable — returned-home, transitional shelter, or evacuated — for each person, not an aggregate count.

"Stabilised" is a multi-criteria observable, not a scalar. A scalar would hide the cohort-individuation discipline.

**(d) `EXT-01` central-government counterparty.** **Flag dependency, require a fallback for each `ACT-*` that depends on it.** ASM-19 treats `EXT-01` as reliable, which is an assumption, not a given. Any response-plan action whose premises include ASM-19 must either have a documented fallback path or be flagged as single-point-of-dependency. I reject full acceptance (ASM-19 unchallenged) and I reject a blanket insistence-on-fallback-for-every-action (too coarse). Per-action triage via the `premises` column is the right granularity.

## Q6. Validation claims at Session 002 close

What can legitimately be claimed under CON-02 / DEC-07:

- **Structural sufficiency.** The register covers the cohort-individuation requirement; every row has four-link traceability; no aggregate-cohort laundering; time-to-harm treated qualitatively per DEC-06; premises named, including silences.
- **Methodology fidelity.** The register and plan were produced under the Selvedge engine's multi-agent deliberation, anti-laundering, and independence-preserving rules; silences are first-class; external frameworks were surveyed and declined visibly.
- **Internal consistency.** Cross-reference integrity holds (every `RSK-*` resolves to POP/INF/SVC/DEP/ASM IDs that exist; every `ACT-*.risks_addressed` resolves to an `RSK-*`; bidirectional link validated).
- **Cohort coverage.** No individuated medical-fragility cohort from the system model is absent from the register.

What **cannot** be claimed:

- **That the register is complete.** No domain actor reviewed it; no reference case was consulted (CON-02).
- **That the prioritisation is correct.** The prioritisation method is defensible from the brief, but workspace-only validation cannot test whether it *would actually* save the most harm.
- **That time-to-harm windows are clinically accurate.** ASM-20 rules out the clinical knowledge that would be needed.
- **That the response plan is feasible.** Feasibility requires resource estimates, actor commitments, and logistical reality — none available in workspace validation.
- **That `SIL-*` enumeration is exhaustive.** Silences about silences remain possible; the method surfaces known holes, not all holes.
- **That severity bands correspond to any real-world probability or impact.** They are partition-and-window derived, not calibrated.

Process rigor is not evidentiary rigor. The deliberation record proves the register was built without silent imports and with documented dissent; it does not prove the register is right.

## Q7. Where the single-model form is distorting your work

Instances counting toward §5.1 minority activation:

1. **Per-settlement cross-section for settlement-local risks.** To draft risks for South Latch specifically — dialysis centre inaccessibility (`INF-04`), levee state silence (`INF-21`), aged-care clusters (`INF-12`, `INF-13`), dispersed smallholding access (`POP-16`) — I wanted a view that showed *all* South-Latch-scoped `POP-*`/`INF-*`/`SVC-*`/`DEP-*` in one place. The single model forced me to repeatedly scan for the settlement suffix / locational cue across flat lists. For Merrow Port the same problem recurs (dormitory cohort `POP-02`, regional hospital `INF-01`, water plant `INF-05`, backup wells `INF-06`, generator `INF-30`, fuel chain `INF-32`). **Count: 2 instances** (one per settlement that needed cross-section to draft settlement-scoped risks).
2. **Per-service dependency chain for cold-chain and dialysis.** `DEP-13` ties `SVC-05` to `SVC-08`; `DEP-09` ties `INF-04` to `POP-09`. Drafting risks around cold-chain failure required tracing from `SVC-08` backwards through `DEP-13` to `SVC-05` to whichever of `INF-07`–`INF-11` powers the refrigeration, to `INF-32` fuel — a per-service dependency tree would have made this one-shot; the flat list required reconstruction. **Count: 1 instance.**
3. **Population-indexed view of `SIL-*`.** Several silences (outer-islet count, neonatal occupancy, dormitory T0 occupancy, `POP-12`/`POP-13`/`POP-14`/`POP-15` counts) are population-facing; I needed a population-by-silence view to draft the cohort-silence risk partition cleanly. The single model lists silences as a separate block, not indexed to `POP-*`. **Count: 1 instance.**
4. **Infrastructure-by-state cross-section at T0.** For operational-readiness risks (what is generator-dependent right now? what is silence-state right now?), an `INF-*` × T0-state cross-section would have been directly usable; I reconstructed it by scanning. **Count: 1 instance.**

That's **5 instances** where my risk-identification work wanted a view the single-document model didn't cleanly expose. Per the §5.1 activation warrant ("if Session 002 produces ≥3 risks requiring re-derivation of dependencies because the single model doesn't expose them, the multi-view proposal becomes preferred revision direction"), my work alone crosses the threshold. I am reporting instances of needing the view, not necessarily risks that failed to be written — but the re-derivation cost was real.

## External inputs surveyed

- **Risk-register column conventions from generic ISO-31000-style enterprise risk management.** Surfaced mentally while considering Q1 column list (likelihood, impact, risk score, owner, controls). **Declined.** Likelihood×impact scoring is incompatible with CON-02 workspace-only validation; the owner column duplicates response-plan ownership; controls duplicate response-plan `ACT-*` linkage. The four-link D-010 schema is the Selvedge-native alternative.
- **Bowtie / fault-tree dependency mapping.** Surfaced while considering dependency-depth prioritisation in Q2. **Declined as a formal framework**; the `DEP-*` edges already carry the same information without the diagrammatic overhead.
- **Stream-based concurrent-operations structure from generic incident-management.** Surfaced in Q3. **Declined as a framework** (ICS/NIMS is already on `EXT-SURVEY-01`); the stream shape I proposed is service-keyed from the system model's `SVC-*` list, not ICS-keyed, and should be recognised as such.
- **Qualitative severity band language (`critical/high/moderate/watch`).** Generic usage. **Retained as vocabulary** but not as framework — the bands are labels, not a scoring system.

## Honest limits

- I proposed a prioritisation partial-order and defended it on methodological grounds (cohort-individuation, refusal of false precision). I cannot demonstrate it is the *right* partial-order for saving the most harm; workspace-only validation forecloses that test.
- My "stabilised" criteria in Q5(c) are observable-in-principle but were chosen from the system-model key list; I may have missed a criterion that would only become visible under a per-settlement cross-section (Q7 instance 1).
- I did not propose a specific number of risk entries for the register. I believe the count should be emergent from applying the schema across the system model rather than targeted, and I may be wrong — a targeted count might surface missing risks that an emergent draft leaves uncovered.
- I leaned heavily on the system-model IDs as given; if the upstream enumeration missed an `INF-*` (e.g. mortuary capacity was named a silence but not assigned an `INF-*`), my register will mirror that miss.
- The Operations Planner will have a stronger Q3 answer. My structural view is compatible with a plan shape I haven't proposed in full.
- Blind spot: I am a non-adversarial perspective by design. The Adversarial Skeptic will likely challenge whether the register's schema itself launders precision (e.g. whether the closed qualitative vocabulary for `time_to_harm` is itself a pretrained import). I did not fully stress-test that objection.
