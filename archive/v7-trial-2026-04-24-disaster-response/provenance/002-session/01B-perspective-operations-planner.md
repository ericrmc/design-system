---
session: 002
title: Perspective — Operations Planner
date: 2026-04-24
status: complete
perspective: Operations Planner
committed_at: 2026-04-24
---

# Perspective: Operations Planner

## Methodology context acknowledgement

I am contributing the Operations Planner perspective to Session 002's independent phase under Selvedge `engine-v7`, reasoning only from the shared brief plus my role-specific stance, and preserving cohort individuation and the §5.1 minority activation warrant as binding.

## Q1. Risk register minimum structural sufficiency

The v1 risk register must be the *pivot table* between cohorts/services and the response plan. If it is not structured so every row can be converted into one or more plan actions with unambiguous addressees, it is decorative.

**Minimum columns (fields) for each risk row:**

1. `RSK-NN` — stable ID, zero-padded, assigned in creation order, never reused.
2. `title` — one short noun phrase ("dialysis gap, South Latch cohort").
3. `affected_cohorts` — list of `POP-*` IDs. *Plural, not singular.* A risk that affects `POP-09` and `POP-10` differently is recorded as either two rows or one row with two `time_to_harm` entries keyed by cohort. No settlement-only risks: if a row reads "Merrow Port", the author must name which `POP-*` within Merrow Port.
4. `affected_services` — list of `SVC-*` IDs that the risk degrades or removes.
5. `affected_infrastructure` — list of `INF-*` IDs whose state drives the risk.
6. `upstream_dependencies` — list of `DEP-*` IDs on whose shared-fate the risk depends (e.g., `DEP-08` `INF-14` carries `INF-17`).
7. `time_to_harm` — qualitative window, keyed per cohort when cohorts differ. Allowed values: `<24h`, `24–72h`, `72h–7d`, `7–10d`, `>10d`, `unknown-bounded`, `unknown-unbounded`. This is mandated by `DEC-06` (qualitative only, no pretrained clinical time values — `ASM-20`).
8. `silence_dependencies` — list of `SIL-*` IDs whose resolution would change the row (e.g., a generator-fuel-status risk names the generator-fuel `SIL-*` as a silence it is riding on).
9. `assumption_dependencies` — list of `ASM-*` IDs the row's plausibility rides on (e.g., `ASM-08` that backup wells are potable, not merely flowing).
10. `status_at_authoring` — `open`, `monitoring`, `contingent-on-silence`. A risk contingent on an unresolved silence cannot be closed by the plan; it can only be converted to `monitoring` when the silence is resolved.

**ID convention.** `RSK-NN` flat namespace. No cohort-prefixed IDs (`RSK-POP09-01`) because a risk frequently spans cohorts and the prefix lies. Cohort scope is carried in `affected_cohorts`, not in the key.

**Cross-reference conventions.** Every row cites at least one `POP-*`, one `SVC-*`/`INF-*`, and one `ASM-*`/`SIL-*`. Four-link traceability (D-010) is enforced at authoring: all legs populated before a row counts v1-complete.

**Time-to-harm rules.** (i) Qualitative only. (ii) Per-cohort when windows differ (a cold-chain failure threatens `POP-13` on a different clock than `POP-14`). (iii) `unknown-bounded` (within 10 days, unlocalised) is distinguished from `unknown-unbounded` (may sit outside 10 days). `unknown-bounded` schedules as if `<72h` until a silence closes; `unknown-unbounded` triggers a silence-closing action, not a mitigation.

**What I leave out.** Likelihood × impact scoring (false precision under `ASM-20`; declined, see External inputs). Owner column (belongs on actions; risk-ownership orphans cohorts). Residual-risk rating (not meaningful under `CON-02`).

## Q2. Prioritisation method

I propose a **two-key hybrid**: primary key **cohort time-to-harm** (shortest first, per `POP-*`); secondary key **dependency depth** (upstream-risks whose resolution unblocks multiple downstream risks float within a time-to-harm band).

Time-to-harm ordering honours `DEC-05` and the Session 001 01B "averages kill the dialysis patients" position — `POP-09` (~1,200, per `DEP-09`) shares a band with `POP-11` neonatal and `POP-13` insulin-dependent, not with `POP-04` general Kellan Rise. Dependency-depth keeps upstream levers visible: a generator-fuel risk (`INF-32` → `INF-30` → `INF-01` via `DEP-11`, `DEP-12`) stages early within its band even if its own harm window is longer.

I decline likelihood × impact scoring (risk-matrix pattern, declined per §6). I decline refusal-to-rank: the plan needs order, and deferring order to the plan author smuggles prioritisation into an unauditable place.

**What this gives up.** Rows in the same band with the same dependency depth stay tied — I accept tying as honest. Small cohorts (e.g., `POP-11`) sit equal with larger ones (`POP-09`); this is what `DEC-05` was preserved to do. A large-but-slower settlement-scale dependency can sit behind a smaller cohort-acute risk; delaying `POP-09` to serve `POP-04` is the laundering the brief forbids.

## Q3. Response plan minimum structural sufficiency

This is my primary question. I propose the plan be **phased with sub-windows as operational compartments** (Q4), with **concurrent service-family streams within each phase**, and **explicit dependency edges between actions**.

**Shape.** Not flat, not branching. Two phases mapped to `WIN-acute` (T0–72h) and `WIN-stab` (72h–10d). Within each phase, parallel streams grouped by service-family:

- S-HEALTH: `SVC-01`, `SVC-02`, `SVC-03`, `SVC-09`, `SVC-10`.
- S-LIFELINE: `SVC-04`, `SVC-05`, `SVC-08`.
- S-ACCESS: `SVC-07`, `SVC-11`, `SVC-12`, `SVC-14`.
- S-SHELTER: `SVC-06` for `POP-06` ~18K.
- S-INFO: `SVC-13`, `SVC-15` (language-channel-aware per `POP-02`, `ASM-18`).
- S-SILENCE: actions whose primary output closes a `SIL-*`.

Service-family grouping (not settlement grouping) is deliberate: settlement tracks re-aggregate cohorts (`POP-09` and `POP-10` both fall under `SVC-03` but live in different settlements; settlement-first loses the cross-settlement transfer path).

**Action schema (minimum per row):**

1. `ACT-NN` — stable ID, flat namespace.
2. `stream` — S-HEALTH / S-LIFELINE / S-ACCESS / S-SHELTER / S-INFO / S-SILENCE.
3. `phase` — `WIN-acute` or `WIN-stab`.
4. `actor_class` — role, not named individual (e.g., "local EMS coordinator", "utility field crew"). Where `EXT-01` cooperation is assumed, annotated `(external: EXT-01)` and a fallback is required (Q5d).
5. `target_cohort_or_service` — list of `POP-*`/`SVC-*`/`INF-*` IDs. **Settlement-only targets rejected at authoring.** A water action in Merrow Port must name `POP-17` (~27K not on backup-well rotation) and/or `POP-12`/`POP-13`/`POP-14` and/or `POP-02` — not "Merrow Port residents".
6. `trigger` — clock (`T0+NNh`) or state (`when INF-05 salt-intrusion sampled`, `when SIL-<id> resolved`). Exactly one per action; "ASAP" is rejected.
7. `completion_criterion` — observable post-condition against `INF-*`/`SVC-*` state or cohort-coverage ratio. Examples: "`INF-30` fuel-buffer ≥ 72h documented"; "`SVC-03` accessible to ≥ 900 of `POP-09` via transport to `INF-02`"; "`POP-02` risk-communication coverage in both non-majority languages confirmed". No criterion → not admitted.
8. `upstream_actions` — list of `ACT-*` IDs whose criteria must hold first. Makes the plan a DAG, not a list.
9. `risk_ids_addressed` — required for four-link traceability.
10. `assumptions_relied_on` — list of `ASM-*` IDs. If `ASM-17` later fails, every action citing it is flagged for re-derivation.
11. `fallback_ref` — optional `ACT-NN` pointing to a pre-declared fallback (Q5d).

**Sequencing.** Within each phase, actions ordered by trigger time, with `upstream_actions` edges providing precedence. A visible ordering inside each phase is minimum; creation-order tables are not sufficient.

**Dependencies.** `upstream_actions` edge list per row. Resulting DAG must be acyclic; cycles are resolved at synthesis.

**Action count.** Target **18–24 actions**. Six streams × ~2 actions per phase × 2 phases = 24 ceiling; S-SILENCE will have fewer. Below ~15, cohort coverage collapses (folding `POP-09`/`POP-10`/`POP-11`/`POP-12`/`POP-13`/`POP-14` into one action is the laundering failure). Above ~30, the plan is unauditable under workspace-only validation. Surplus becomes a named v1.1 deferred slate, not inflated v1.

**What I leave out.** Resource-budget columns (no basis under `CON-02`; nominal numbers invite false confidence — class carried on actor; quantity stays silent). Cost estimates (same). Named individuals / named external counterparties (actors stay at class; `EXT-01`/`EXT-02`/`EXT-03` are tags, not signatories).

## Q4. Sub-windows as operational compartments

I argue for **operational compartments with one explicit review gate at the `WIN-acute` → `WIN-stab` boundary** (T0+72h).

Reasoning: `D-004` called the windows orientation labels for the *model*, which does not execute. The *plan* executes; time-to-harm windows (`DEC-06`) cluster around 72h — the natural joint between "kills before we can think again" and "can sequence deliberately". Refusing to reify the joint forces the reader to re-derive it at run-time, which is the opposite of operational.

- **Inert** smuggles sequencing back into the reader.
- **Review-every-action-at-every-boundary** adds decision cost per action and, with one boundary, degenerates to one gate anyway.
- **Branching** cannot credibly name branch conditions under `CON-02`.

Each action carries a `phase`; the plan declares one review gate at T0+72h. Gate purpose is narrow: (i) re-check time-to-harm against observed state; (ii) promote/demote `contingent-on-silence` risks whose silences resolved; (iii) confirm `WIN-stab` triggers remain valid given `WIN-acute` completion. Not a replan — replan belongs to Session 003.

## Q5. Inherited decisions-not-taken from Session 001

**(a) Cohort prioritisation.** **Partial order.** A total order over all `POP-*` is not defensible: `POP-09` (~1,200) and `POP-11` (unknown count) cannot be ordered against each other when one count is missing; honest order is "both before `POP-04`", not "one before the other". Refusal-to-rank leaves the plan author to order tacitly — the laundering failure. I adopt the partial order induced by Q2: cohorts sharing a time-to-harm band are equivalence-classed; dependency-depth breaks ties within a band; remaining ties stay tied. Assumption named: `time_to_harm` is determined qualitatively via handler judgement, per `ASM-20` / `DEC-06`.

**(b) `POP-05` outer-islets.** **First-class cohort, not first-class settlement.** The three named settlements anchor distinct `INF-*`/`POP-*` constellations; `POP-05` has only `INF-19` (VHF, post-surge state unknown) named, and its count is unknown. Promotion to settlement status would require naming infrastructure we lack. Treatment: keep as first-class cohort with an S-SILENCE action ("establish count and access channel for `POP-05` via `INF-19` or sea/air"). At least one `RSK-NN` and one `ACT-NN`; no settlement phasing track.

**(c) Definition of "stabilised" at T0+10d.** Observable criteria I propose, each convertible to a plan completion-criterion:

1. `SVC-03` haemodialysis: ≥ 90% of `POP-09` (target ~1,080 of ~1,200) receiving dialysis on their clinically-indicated schedule, via transport to `INF-02` Kellan Rise or restored `INF-04` access. (Assumption named: the handler-reported figure ~1,200 is stable enough — inherits `ASM-03`-class stability.)
2. `SVC-04` potable water: `POP-17` (~27K not on backup-well rotation) on a declared potable-water plan (tankered, bottled, or restored `INF-05`), with coverage logged.
3. `SVC-05` power: `INF-01` regional hospital off generator OR generator fuel buffer ≥ 7d documented (spans past T0+10d); `INF-30`/`INF-32` relationship surfaced, not inferred.
4. `SVC-01` acute care: no cohort shares a ward-to-population ratio that would be recorded as overflow under `INF-01` + `INF-02` normal operating assumptions (qualitative — we cannot import a numeric overflow threshold).
5. `SVC-06` shelter: `POP-06` (~18K displaced) in accommodation with declared duration ≥ 14d (i.e., not day-to-day), language-accessible for `POP-02`.
6. `SVC-08` cold chain: `POP-14`/`POP-15` refrigerated-medication dependents have a confirmed cold-chain custody path (`SVC-05` powering `SVC-08` per `DEP-13` — or an explicit ice/courier fallback).
7. `POP-05` outer-islets: count established; channel of contact confirmed; medical-fragility sub-cohorts within `POP-05` enumerated or declared still-silent.
8. All `SIL-*` flagged as blocking a `WIN-stab` action are either closed or re-classified as `unknown-unbounded` with explicit acceptance.

Assumption I had to name: that "stabilised" is a process-observable property at T0+10d, not an outcome-measured one. Under `CON-02` we have no way to measure outcomes; we can only observe state.

**(d) `EXT-01` central-government.** **Flag dependency, insist on fallback.** No action assumes `EXT-01` cooperation by default; where an actor_class is external, the action carries a `fallback_ref` to a non-external alternative that at least partially discharges the completion criterion. Fallback patterns:

- Fuel (`INF-32` → `INF-30`): primary central-government logistics; fallback `EXT-02` utility supplier and/or road-import via `INF-15` (intact, 24-tonne) from `EXT-03` highland interior.
- Inter-hospital transfer (`INF-01`↔`INF-02`, `ASM-17`): primary local EMS + central coordination; fallback private/volunteer fleet dispatched by local EMS.
- `POP-05` access: primary central sea/air; fallback local fishery vessels under degraded `INF-16`.

This contradicts `ASM-19`. I flag it: `ASM-19` should not be load-bearing for a 10-day plan — if it fails at T0+36h with no pre-written fallback, the plan fails. Session 002 decisions should record disagreement with `ASM-19`'s framing.

## Q6. Validation claims at Session 002 close

Under `CON-02` (workspace-only), Session 002 can claim:

- **Process-rigor.** Register and plan are internally traceable: every action cites ≥1 risk, every risk cites cohort + service/infra + assumption, four-link chain (`D-010`) closes. `upstream_actions` DAG is acyclic. Every action has a state-expressed completion criterion. No silence silently resolved — S-SILENCE action or logged "accepted silence".
- **Individuation.** `POP-09`, `POP-10`, `POP-11`, `POP-12`, `POP-13`, `POP-14`, `POP-15` each appear as first-class targets on ≥1 action, per `DEC-05`.
- **Import-hygiene.** No framework (ICS/NIMS, Sphere, cluster, SoVI, MoSCoW, RTO/RPO, Maslow, triage colour) silently applied; all surveyed in `EXT-SURVEY-*`.
- **Completeness-relative-to-artefacts.** Every `POP-*`/`SVC-*`/`INF-*` in the summarised keys is addressed or explicitly deferred with a silence reference.

What **cannot** be claimed: that the plan will work (no empirical validation); that time-to-harm windows are correctly bounded (handler-reported, unchecked); that cohort counts are correct (several unknown); that prioritisation matches operational reality; that `ASM-17` or `ASM-19` hold across the horizon; that the plan is complete (silences outnumber resolutions; v1 is a floor).

Process rigor is not evidentiary rigor. The session close must state this in its own voice.

## Q7. Where the single-model form is distorting your work

Instances where I needed a view the single model does not expose cleanly:

1. **Per-cohort phasing view.** For each `POP-*` I needed `(time_to_harm, relevant SVC-*, relevant INF-*, blocking SIL-*)` as a cross-section. Recoverable for `POP-09`; for `POP-12`/`POP-13`/`POP-14` inside `POP-5K-parent` I re-derived the cohort-to-service binding because parent and individuated children both appear without a flattening.
2. **Per-service dependency chain.** `DEP-*` edges are named individually but no service-rooted transitive chain is exposed. Tracing `SVC-03` → `INF-04` + `INF-02` (via `ASM-17`) + `SVC-05` (implied) + `SVC-07` (implicit) required re-derivation.
3. **Per-settlement action concentration.** To check load-balance on actor classes per locality I needed a settlement → (cohorts, infra, services-used) view. Not exposed; reconstructed by filtering.
4. **Silence-to-risk incidence matrix.** For Q5c criterion 8 I needed `SIL-*` × `POP-*`/`SVC-*`. The 24 `SIL-*` are enumerated but not indexed; recovered manually.

Four re-derivations. Per the activation warrant (≥3), this perspective contributes to §5.1 activation. I record the count and defer the multi-view decision to synthesis.

## External inputs surveyed

- **ICS/NIMS actor roles.** Surveyed for actor_class. Declined: ICS carries an actor-authority topology not validated against Nivaro. `EXT-SURVEY-01`.
- **Risk matrix (L×I 5×5).** Surveyed for Q1/Q2. Declined: no base-rate data; scoring is decorative.
- **Gantt/PERT.** Surveyed for Q3. Applied only the DAG idea (acyclic `upstream_actions`); declined numeric durations/critical-path.
- **Sphere minima.** Surveyed for Q5c. Declined numeric thresholds per `ASM-20` / `EXT-SURVEY-03`; kept qualitative criteria.
- **Humanitarian Cluster system.** Surveyed for stream grouping. Declined cluster names; used `SVC-*`-grounded families.

## Honest limits

- Actor-class lists are generic; I cannot ground them in Nivaro's actual civil-service/health-system organisation.
- Action count 18–24 is a design-space argument; a fixed N needs other perspectives' risk counts.
- My partial cohort order may produce unbreakable ties at plan-authoring; Q5a may need revisiting.
- Choice of T0+72h single gate (vs. a second at ~T0+7d) rests on low-confidence inference from the summarised keys' time-to-harm clustering.
- Q5d fallback stance contradicts `ASM-19`; synthesis must resolve, not paper over.
- I did not see other perspectives' outputs; my stream-shape and action-count proposals may conflict with the Adversarial Skeptic's or the Outsider's, and I accept synthesis may select against mine.
