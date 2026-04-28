---
session: 002
title: Perspective — Adversarial Skeptic
date: 2026-04-24
status: complete
perspective: Adversarial Skeptic
committed_at: 2026-04-24
---

# Perspective: Adversarial Skeptic

## Methodology context acknowledgement

I am contributing one perspective in the independent phase of a MAD v4 deliberation; I have not read any other perspective's output nor the full system model or ledger, and I am reasoning strictly from the shared brief's summarised keys plus my continuity stance from Session 001.

## Q1. Risk register minimum structural sufficiency

I decline to propose a schema. That refusal is the role. What I will contribute is the list of laundering surfaces any proposed schema must survive.

1. **Severity / impact column.** A `severity` or `impact` column without a defined unit imports an `EXT-SURVEY-*` framework. `DEC-05` says cohort individuation is first-class; the instant you write `impact: high`, you collapse `POP-09` (~1,200 dialysis, `INF-04` inaccessible) and `POP-11` (neonatal, count unknown) and `POP-12` (CPAP/home-oxygen, unknown) into one ordinal bucket. That is the exact move `DEC-05` refused. If other perspectives propose `impact`, I name it as re-importing triage colour-coding (`EXT-SURVEY-10`) through the back door.

2. **Likelihood column.** There is no base-rate population in this brief. `likelihood: medium` for `INF-32` fuel is fabricated — `SIL-*` records fuel status as first-class silence and `ASM-15` only grants the chain exists. I would rather the register carry an *evidence state* field (known / inferred / assumed / silent) than a likelihood figure.

3. **Time-to-harm.** `DEC-06` granted qualitative windows only; `ASM-20` forbade pretrained clinical numbers. A register with numerical hours-to-harm has imported silently, derived from a model that does not contain them, or hidden an assumption behind a number. Qualitative windows are defensible; numbers are not.

4. **"Owner" column.** Owner assignment is fiction. `ASM-19` granted `EXT-01` reliable as *recipient*; writing `owner: EXT-01` transmutes reliability-as-recipient into reliability-as-delivery-partner. See Q5(d).

5. **Cross-reference fields.** Four-link traceability (D-010) is the one structural commitment I endorse: `risk → service/infrastructure → cohort → assumption/silence`. A risk that does not name its `POP-*`/`INF-*`/`SVC-*`/`ASM-*`/`SIL-*` is a sentence, not an entry.

6. **ID convention.** I don't care about the format; `RISK-NNN` is fine. I care that IDs are allocated once and not reshuffled when the register re-sorts, because reshuffling destroys the audit trail from plan actions back to the risks they address.

Leave out: any column requiring an invented number (likelihood, severity, priority score); any column pretending ownership not granted; any "status" column at v1 (status implies monitoring implies delivery organisation; this is a planning session).

Would accept: a `silence-dependency` field naming the `SIL-*` a risk cannot be fully characterised without. The inverse of an impact score — an honesty field.

## Q2. Prioritisation method

This is the question most exposed to laundering, so I will spend words here.

I reject likelihood-×-impact. It is `EXT-SURVEY-*` adjacent to every one of the declined frameworks (ICS/NIMS, Sphere, SoVI). It requires numbers the ledger has already forbidden (`ASM-20`), and it collapses cohorts the ledger has already individuated (`DEC-05`).

I reject "triage" framing in any form. Colour-coding is `EXT-SURVEY-10`, already declined. The word "critical" as a risk level imports the same taxonomy.

I reject time-ordering by `POP-*.time_to_harm` window *as the sole method*, because it naturalises the 10-day horizon (`GIV-01`) as the ranking frame. The 10-day horizon is request-frame, not physics; I flagged this in Session 001. A dialysis cohort's harm window is physiological, not political. Ranking risks by their proximity to a political deadline privileges the deadline.

I reject refusal-to-rank *as a complete position*, because the plan has to know what to do first, and a register that offers no guidance is not serving the plan.

What I would accept is a **partial order driven by two independent axes kept visible**:

- *Cohort fragility* (individuated per `DEC-05`): `POP-09` (~1,200 inaccessible), `POP-11` (neonatal), `POP-12`–`POP-14` (powered-medical, refrigerated-biologic) rank above aggregate populations, as a rule. Not because they are "more important" in a values sense — that is a claim the session cannot make — but because their time-to-harm is shorter and less reversible, which is a *physical* claim the system model can support.

- *Dependency depth* (upstream-over-downstream): `INF-32` (generator fuel supply chain) ranks above `INF-30` (regional hospital generator) ranks above `SVC-01` (acute hospital care) ranks above `POP-11` (neonatal) — because a failure at `INF-32` propagates through all the downstream edges. This is a structural claim the `DEP-*` edges can support.

The two axes will disagree. That disagreement is information, not a bug. A risk that is high on both (e.g., `INF-32` fuel uncertainty, which is upstream AND whose failure touches `POP-09`/`POP-11`/`POP-12` within hours) is unambiguously first. A risk that is high on cohort fragility but low on dependency depth (e.g., `POP-09` direct access to `INF-04` dialysis centre) is clearly urgent but not propagating. A risk that is high on dependency depth but touches only aggregate populations (e.g., `INF-21` levee state → `POP-03`) can be ranked lower than the cohort-fragility-high-dependency-depth-low set.

What this gives up: a single sort order. The register cannot be collapsed to a list with a column called `priority`. The plan has to read the two-axis view and make the scheduling choice. That is the correct place for the political judgement to live, not inside the register.

## Q3. Response plan minimum structural sufficiency

I decline to propose a plan shape. I will name the laundering surfaces for whatever shape the other perspectives propose.

1. **"Phased plan" aligned to `WIN-acute` / `WIN-stab`.** D-004 already said these are orientation labels, not compartments. A plan that assigns actions to phases has promoted the labels against the session's own prior decision. See Q4.

2. **"Concurrent streams" by service (water / health / shelter / comms).** This is `EXT-SURVEY-02` UN/IASC clusters through the side door. Once you have a "health stream" you have a cluster. I would call this out wherever it appears.

3. **"Action list with owners".** See Q1 point 4 and Q5(d). The plan is not authorised to bind owners. Writing `owner: local health authority` pretends `EXT-01` has delegated specific operational authority the brief does not assert.

4. **"Branching plan" with contingencies.** Branches require probabilities or decision criteria to fire. The decision criteria would then need to be observable; we return to the "stabilised" problem (Q5(c)). I am skeptical of branching-plan proposals that do not specify how branches fire, because the unspecified branch is a hiding place for laundering.

5. **"Success criteria at T0+10d".** The brief asks for a 10-day response-and-stabilisation plan; *stabilisation* is its word. Whether someone is stabilised is a semantic question the plan cannot answer from inside itself. Any proposal that offers observable stabilisation criteria (e.g., "all displaced housed", "water potable to WHO standard", "dialysis resumed for ≥95% of `POP-09`") has derived those criteria from somewhere. If derived from pretrained frameworks (Sphere standards — `EXT-SURVEY-03`), it is laundering. If derived from the perspective's own judgement, it is the perspective legislating semantics the brief reserved. See Q5(c).

What I would accept: a plan that carries actions as entries with the same four-link traceability as the register (`action → risk → service/infrastructure → cohort → assumption/silence`), that does not commit owners, that names which `SIL-*` each action would need to resolve to be executable, and that is explicit about which actions are *unblocking other actions* vs. *delivering outcomes*. The unblocking/delivering distinction matters because unblocking-actions are often silence-resolution (e.g., "determine `INF-01` generator fuel state", resolving `SIL-*` generator-fuel-status), while delivering-actions are the ones people think of as "the plan".

What I would leave out: phase assignments; owner assignments; success criteria for "stabilised"; numeric time estimates the ledger has not earned; contingency branches without firing criteria.

## Q4. Sub-windows as operational compartments

D-004 already decided this, and my read is that the session is being invited to silently reverse the decision. My answer: **inert-to-semi-active**. The sub-windows are orientation labels. The plan should not assign actions to them as compartments, because that would make the labels operational — which D-004 refused — and it would import the Session 001 architecture into the plan unchallenged.

The weakest defensible use is as *review markers*: the register and plan are re-examined at ~T0+72h with the new information that has arrived by then (some of the 24 `SIL-*` silences may have resolved; `INF-21` levee state, `INF-01` generator fuel status, `POP-05` islet count, `INF-03` clinic state). This is not compartmentalisation; it is scheduled honesty about what Session 002 did not know.

But even this weak use has a risk: "review at T0+72h" will be read as "phase gate at T0+72h", and the acute/stab distinction returns through the side door. I prefer the plan record a *replan trigger* rather than a *phase boundary* — the trigger fires when N of the named silences resolve, not when the clock reaches 72h. Trigger-on-information is less corruptible than trigger-on-time.

## Q5. Inherited decisions-not-taken from Session 001

### (a) Cohort prioritisation

I argued above for a partial order along two axes (cohort fragility × dependency depth). A total order is the laundering move; refusal-to-rank is the abdication move; partial order with the two axes kept visible is the only honest position. Where the two axes both rank a cohort high (`POP-09`, `POP-11`, the powered-medical cohorts `POP-12`/`POP-13`/`POP-14` when `SVC-05` is out), the plan can read the order. Where they disagree, the plan owner makes the call and the disagreement is recorded. I do not accept that v1 must impose a total order; that framing is the laundering.

### (b) `POP-05` outer-islet status

The question is misframed. "First-class settlement" versus "special-case cohort" is a category question, but the prior question is: *does the session know there are people there to plan for?* `POP-05` is count-unknown. Any structural decision made now will either (i) privilege a population whose size is unknown, inflating its weight, or (ii) special-case it in a way that deprioritises it without evidence.

My position: `POP-05` stays first-class as *a silence with a probable population behind it*, not as a settlement-structural entity on par with Merrow Port. The plan needs an unblocking action ("establish count and state of `POP-05` via `INF-19` VHF or sea-access reconnaissance"), which itself is blocked by `INF-19` operability being unknown and `INF-16` sea access being degraded. Structural co-equal status is a claim about capacity-to-plan-for, and the session does not yet have the capacity.

### (c) Definition of "stabilised" at T0+10d

This is a semantic question the brief reserved. The plan cannot define "stabilised" without either (i) importing Sphere or equivalent standards (`EXT-SURVEY-03`), or (ii) the perspective itself legislating a definition the brief did not grant.

I push back on any proposal of observable criteria. The honest position: "stabilised at T0+10d" is an externally-defined success condition the session cannot check. The plan can produce a list of *state descriptors* that will be *true at T0+10d if the plan executes* — e.g., "`POP-09` receiving dialysis", "`INF-05` no longer salt-intruded or substituted by `INF-06`", "`POP-06` decreased below 18K" — and leave the judgement of whether those descriptors aggregate to "stabilised" to `EXT-01` or whoever owns that judgement. That is the correct division of labour. The session produces descriptors; the counterparty applies the stabilisation predicate.

I will concretely object if any other perspective proposes numeric thresholds (e.g., "≥95% of `POP-09` receiving dialysis"). Ninety-five is an imported number.

### (d) `EXT-01` central-government counterparty treatment

This is the political fact the session is being asked to pretend away. Repeating for clarity:

- `ASM-19` grants `EXT-01` is a reliable counterparty for *receiving the plan*.
- The plan will need `EXT-01` as *delivery partner* for anything requiring centrally-held resources (helicopter lift for `POP-05` reconnaissance; fuel supply `INF-32`; national-guard or equivalent for `INF-21` levee inspection).
- These are different reliability claims. The session cannot upgrade the first to the second by silence.

My position: **flag dependency AND insist on fallback**. Flag: every action that requires `EXT-01` delivery is marked so. Fallback: each such action carries a named alternative (even if the alternative is "wait and replan", which is a legitimate fallback). Accepting reliability without marking is the laundering move; I do not accept it.

Further: the plan owner is not the correct party to *certify* `EXT-01` as reliable delivery partner. That certification, if it happens, must come from outside the plan. The plan can name the dependency; it cannot wash it clean.

## Q6. Validation claims at Session 002 close

Under `CON-02` and `DEC-07`, the session can claim:

- Internal consistency with the system model v1 and assumption ledger v1, subject to four-link traceability (D-010).
- No silent import of declined frameworks (`EXT-SURVEY-01`–`EXT-SURVEY-10`) to the extent MAD anti-laundering caught them; any application is recorded as an `EXT-SURVEY-*` row.
- First-class silences (`SIL-*`) carried as structural, not absent.
- Cohort individuation (`DEC-05`) preserved.

The session **cannot claim**:

- That the plan would work if executed. Workspace validation is not operational validation.
- That cohort fragility windows are clinically calibrated; `ASM-20` forbade pretrained time-to-harm values.
- That `EXT-01` will behave as the plan assumes; `ASM-19` reliability-as-recipient is not reliability-as-delivery-partner.
- That "stabilised" is achieved at T0+10d. That is a counterparty predicate.
- That the 24 silences are survivable. The plan assumes some resolve favourably; that is not a claim they will.
- That risk prioritisation is operationally correct. The partial order is a process output, not a real-world first-move claim.

Process rigor grants auditability, laundering-surface visibility, traceability. Process rigor does not grant outcome validity, clinical calibration, counterparty reliability, or operational correctness. The MAD mechanism filters certain failure modes; it is not a substitute for the validation modes it is not. I insist this be stated plainly at session close. Artefacts that *look* operationally validated are the next laundering frontier.

## Q7. Where the single-model form is distorting your work

Activation watch. Tracking §5.1 activation warrant: ≥3 risks requiring re-derivation of dependencies because the single model doesn't expose them.

Instances I found while writing this:

1. **Settlement-local cross-section for Merrow Port.** To reason about whether a single loss of `INF-32` fuel simultaneously threatens `INF-01` (regional hospital generator `INF-30`), `INF-05` (would `SVC-05` power affect re-energising water treatment?), and `SVC-08` (cold chain, depending on `DEP-13`), I needed a Merrow Port-local view that the single model does not cleanly expose. I had to re-derive the dependencies from `DEP-08`/`DEP-11`/`DEP-12`/`DEP-13`/`DEP-15` one edge at a time. **Counts 1.**

2. **Per-service dependency chain for `SVC-03` haemodialysis.** `POP-09` ~1,200 dialysis + `INF-04` inaccessible + `ASM-17` inter-hospital referral via road to `INF-02` Kellan Rise dialysis capacity (which the model does not name as a capacity, only the hospital) + `INF-15` 24-tonne bridge carrying the referral + `SVC-05` Kellan Rise power (unaffected, but for how long if `INF-32` degrades?). Reasoning about this chain required pulling from five different `INF-*`/`DEP-*`/`ASM-*` entries. A per-service view would have made this native; the single model makes it archaeological. **Counts 2.**

3. **Population-indexed flattening for medical fragility.** The `POP-5K-parent` aggregate plus children `POP-12`/`POP-13`/`POP-14`/`POP-15` are structurally correct per `DEC-05`, but to reason about *what fraction of them depend on `SVC-05` electrical supply being restored versus cold-chain `SVC-08` being maintained versus `SVC-03` dialysis being resumed*, I needed a flattening the model does not provide. Each sub-cohort has a different service dependency; the aggregate hides it. **Counts 3.**

4. **Shared-fate view for `INF-14` freight rail bridge + `INF-17` fibre trunk.** `DEP-08` names this as shared-fate, but the consequence cascade (loss of `INF-14` → loss of `INF-17` → loss of `SVC-13` telecoms to Kellan Rise via `DEP-15`, which is the hospital coordinating `ASM-17` referrals, which are the fallback for `INF-04` inaccessibility, which is blocking `POP-09`) is *four edges long*. Reasoning through this re-derives the edges every time. **Counts 4.**

Per the activation warrant, I register ≥3 instances and claim §5.1 should move toward activation. A settlement-local view + per-service dependency view + cohort-indexed flattening would have made each of the above readable rather than derivable. I am not proposing the revised form here — proposing is not the skeptic's job — but I am concretely marking where the single form distorts.

## External inputs surveyed

I named several frameworks by category to warn against them. I am not proposing to apply any:

- Triage colour-coding (`EXT-SURVEY-10`, previously declined) — flagged as the laundering surface for "impact" and "critical" risk level columns.
- UN/IASC clusters (`EXT-SURVEY-02`, previously declined) — flagged as the laundering surface for service-stream plan shapes.
- Sphere standards (`EXT-SURVEY-03`, previously declined) — flagged as the laundering surface for observable "stabilised" criteria.
- Likelihood × impact risk scoring (MoSCoW adjacent, `EXT-SURVEY-06`; commercial risk register norm) — flagged as laundering surface for Q2 prioritisation.

All four are surveyed-and-named-so-I-can-refuse-them, not surveyed-and-applied.

## Honest limits

What I could not determine:

- Whether the two-axis partial order in Q2 is stable across more cohorts than the ones I named. I worked through `POP-09`/`POP-11`/`POP-12`–`POP-14` and aggregates; there may be pairs where fragility and dependency-depth disagree in ways my proposal does not handle.
- Whether my Q3/Q5(c) objection to "success criteria" is actionable for Produce. If the session must write *something* under stabilisation criteria, my answer constrains but does not fill.
- Whether the §5.1 warrant triggers now or records "progress toward activation". I named four instances; I believe ≥3 is met, but synthesis may apply the warrant differently.

My blind spots:

- Role-constrained. My characteristic failure mode is refusal-as-default rather than refusal-when-warranted. Readers should check whether my reasons name specific laundering surfaces (I tried) or merely gesture at "laundering".
- I cannot see other perspectives in the independent phase; if one proposes a schema that addresses my concerns (e.g., evidence-state column rather than likelihood; silence-dependency column), I have critiqued a straw-version. Synthesis resolves that.
- Continuity from Session 001 may over-index me on laundering as *the* failure mode. Underspecification-to-uselessness, risk inflation, and over-fragmentation of cohorts may not be caught by my stance; the Outsider and Integrator are better positioned for those.
