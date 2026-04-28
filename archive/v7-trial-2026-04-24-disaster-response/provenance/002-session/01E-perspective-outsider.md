---
session: 002
title: Perspective — Outsider
date: 2026-04-24
status: complete
perspective: Outsider
committed_at: 2026-04-24
---

# Perspective: Outsider

## Methodology context acknowledgement (one sentence)

I am contributing an independent cross-family Outsider perspective for Session 002, reasoning from the shared brief and treating external emergency-management frameworks as non-governing unless explicitly surveyed.

## Q1. Risk register minimum structural sufficiency

The v1 risk register should be small enough to be maintained during a 10-day response, but structured enough that the response plan can trace every action back to a named risk and every risk back to cohorts, services, dependencies, assumptions, and silences.

Minimum fields:

- `risk_id`: use `RISK-002-###`, because these are Session 002 downstream artefacts and future sessions need stable references.
- `short_name`: terse operational label.
- `risk_statement`: condition plus consequence, not a vague topic. Example form: “If `INF-04` remains inaccessible and referral transport is insufficient, `POP-09` misses haemodialysis, causing acute avoidable harm.”
- `primary_cohort_refs`: explicit `POP-*` references. `POP-09`, `POP-10`, `POP-11`, `POP-12`, `POP-13`, `POP-14`, and `POP-15` must remain separate where the mechanism of harm differs. `POP-5K-parent` can appear only as a parent grouping, not as the risk-bearing object.
- `secondary_population_refs`: broader affected groups such as `POP-06`, `POP-17`, `POP-16`, or `POP-05`.
- `service_refs`: `SVC-*` references directly at risk, such as `SVC-03`, `SVC-04`, `SVC-08`, `SVC-09`, `SVC-10`, `SVC-13`.
- `infrastructure_refs`: `INF-*` nodes involved in the failure path.
- `dependency_refs`: `DEP-*` edges when the risk exists because a relationship is fragile, such as `DEP-09`, `DEP-11`, `DEP-12`, `DEP-13`, `DEP-14`, or `DEP-15`.
- `time_to_harm_window`: qualitative only, matching `DEC-06` and `ASM-20`. I would use values like `already active`, `hours`, `T0-T0+72h`, `T0+72h-T0+10d`, and `unknown-urgent`.
- `current_state`: what is known at T0+36h from the brief.
- `uncertainty_refs`: relevant `SIL-*`, `ASM-*`, or unknowns. The risk register must preserve uncertainty rather than smooth it over.
- `tripwires`: observable changes that require immediate response-plan adjustment. Example: “generator fuel below 24h” for `INF-30` / `INF-32`.
- `linked_actions`: response-plan action IDs once drafted.
- `residual_risk_note`: brief statement of what remains unsafe even after planned actions.

I would leave out numeric likelihood scores, monetary loss estimates, mortality estimates, and detailed clinical time-to-harm values. They would imply evidentiary precision the workspace does not have. I would also leave out agency ownership unless the plan has a clear local counterpart, because `EXT-01` is only assumed reliable under `ASM-19`, while many local operational capacities are unstated.

The register should not use a generic “vulnerable persons” field. It should force cohort individuation. Dialysis interruption for `POP-09` is not the same risk as neonatal generator dependency for `POP-11`, home oxygen dependency for `POP-12`, insulin continuity for `POP-13`, biologic refrigeration for `POP-14`, or aged-care continuity for `POP-08`.

## Q2. Prioritisation method

I would use a hybrid ordering: first by time-to-harm for named cohorts and services, then by dependency criticality where one failing node cascades into several harms, then by uncertainty that could hide immediate harm.

The first ordering principle should be time-to-harm, but only after preserving cohort identity. `POP-09` South Latch dialysis patients with `INF-04` inaccessible and `DEP-09` blocking `SVC-03` belong near the top. `POP-11` neonatal occupants at `INF-01`, if present, also belong near the top because `SVC-09` depends on `INF-01`, `INF-30`, and `INF-32`. `POP-12` CPAP / home-oxygen users are also not safely deferrable under grid outage `INF-11`. These are not interchangeable even if all could be called “medical fragility.”

The second ordering principle is dependency criticality. Some risks are important because they are multipliers. `INF-30` hospital generator and `INF-32` fuel supply chain condition `SVC-01`, `SVC-09`, and potentially referral capacity from Merrow Port to Kellan Rise under `ASM-17`. `INF-05` salt intrusion and `INF-06` backup wells condition `SVC-04` for `POP-17`. `INF-14` carrying `INF-17` under `DEP-08` and `DEP-15` may turn a transport infrastructure problem into a telecommunications problem for Kellan Rise and the wider response.

The third ordering principle is uncertainty with plausible acute harm. Unknown outer-islet status `POP-05` and `INF-19`, unknown aged-care cluster status `POP-08` / `INF-12` / `INF-13`, and unknown neonatal occupancy `POP-11` are not lower priority merely because the counts are unknown. Unknown count is not low impact; it is a visibility failure.

I would not use likelihood-times-impact as the primary ordering. It looks disciplined, but in this workspace it would mostly encode confidence theatre: likelihoods are not measured, impacts are not calibrated, and the highest-risk cohorts are precisely those with weak data. I would still allow a plain-language “expected direction” note, but not a matrix score.

This gives up a single clean total ranking. The plan may need a top band of concurrent risks rather than ranks 1 through 20. That is acceptable. A false total order would be less useful than a defensible partial order with named simultaneity.

## Q3. Response plan minimum structural sufficiency

The response plan should be organized as concurrent operational streams with phased review gates, not as one linear action list. A linear plan would hide the fact that dialysis continuity, hospital generator fuel, potable water, shelter, aged-care checks, outer-islet contact, and communications restoration must move at the same time.

Minimum structure:

- `action_id`: use `ACT-002-###`.
- `stream`: examples include medical continuity, potable water, shelter and displacement, access and transport, telecommunications and information, infrastructure stabilization, and unknown-status discovery.
- `action_statement`: specific action with an observable output.
- `risk_refs`: one or more `RISK-002-###`.
- `cohort_refs`: explicit `POP-*`, never only aggregate.
- `service_refs`: `SVC-*`.
- `infrastructure_dependency_refs`: `INF-*` and `DEP-*` where relevant.
- `time_window`: intended start and review point within the 10-day horizon.
- `preconditions`: actions or facts required first.
- `blocks_or_enables`: action-to-action dependencies.
- `decision_trigger`: what would cause continuation, escalation, branch, or cancellation.
- `minimum_success_observable`: what must be true to count the action as done.
- `uncertainty_refs`: assumptions and silences the action is meant to test or reduce.

The plan should include explicit discovery actions, not treat assessment as background. For example, confirm `INF-30` fuel status and `INF-32` replenishment path; identify which `INF-07`-`INF-10` substations are degraded; contact `POP-05` via `INF-19` or alternate route; determine `INF-12` / `INF-13` status; identify `POP-11` neonatal occupancy; map `POP-12` home oxygen and `POP-13` insulin needs. These are response actions because unresolved uncertainty can cause harm.

I would leave out detailed staffing rosters, procurement quantities, clinical protocols, and engineering repair methods. The workspace does not provide enough operational data to specify them responsibly. The plan can say “establish dialysis transport/referral schedule for `POP-09` using `ASM-17` road referral where feasible,” but it should not invent session lengths, patient transport ratios, or clinical thresholds.

The plan should branch where dependencies are unresolved. For `POP-09`, branch on whether road referral to `INF-02` is feasible under `ASM-17`; if not, escalate mobile dialysis, alternate access, or central-government support. For `SVC-04`, branch on whether `INF-06` backup wells can continue serving 35K and whether `POP-17` can be supplied by tanker, bottled water, or restored treatment from `INF-05`. For `SVC-13`, branch on whether `INF-17` is operational despite `INF-14` damage.

## Q4. Sub-windows as operational compartments

I would treat `WIN-acute` and `WIN-stab` as review gates and planning lenses, not hard compartments.

The actual trade-off is this: hard compartments make command review easier, but they can distort actions that must begin in the acute period and continue through stabilization. Dialysis continuity for `POP-09`, generator fuel for `INF-30` / `INF-32`, potable water for `POP-17`, and shelter for `POP-06` do not respect a clean T0+72h boundary. If they are artificially placed in only one window, the plan may understate handoff risk.

Letting actions span windows freely has the opposite failure mode. It can create “ongoing” actions with no accountability or decision point. A line item that says “continue potable water support through day 10” is too vague unless it has review gates, tripwires, and observable outputs.

So the plan should use `WIN-acute` for life-preserving stabilization and unknown-status discovery, then require a formal T0+72h review to decide what continues, scales, hands off, or stops. `WIN-stab` should then focus on continuity, restoration, and reducing dependence on emergency workarounds.

In practice:

- Actions may span both windows.
- Every spanning action needs a T0+72h review criterion.
- Some actions should be acute-only, such as initial contact with `POP-05` or immediate aged-care welfare checks for `POP-08`.
- Some actions should start acute but mature in stabilization, such as water distribution for `POP-17`, cold-chain support for `POP-14` / `POP-15`, and communications restoration for `SVC-13`.
- The T0+72h gate should ask whether hidden cohorts have been found, not merely whether service averages improved.

## Q5. Inherited decisions-not-taken from Session 001

**(a) Cohort prioritisation: partial order.**

I would use a partial order, not a total order and not a refusal to rank. A total order would create false precision across incomparable harms. Refusal to rank would avoid the hardest decision the response plan exists to support.

The top band should include cohorts with plausible near-term irreversible harm and blocked services: `POP-09` South Latch dialysis patients, any confirmed `POP-11` neonates dependent on `INF-01` / `INF-30`, `POP-12` home oxygen or CPAP users without power, and `POP-08` institutional aged clusters if flooded or isolated. `POP-13`, `POP-14`, and `POP-15` should be separately tracked because insulin access and refrigerated biologics have different logistics and harm mechanisms.

The partial order should also elevate unknown-status cohorts where invisibility could mask acute harm: `POP-05`, `POP-08`, and `POP-11`.

**(b) `POP-05` outer-islets: first-class settlement.**

I would treat `POP-05` as a first-class settlement for Session 002. It has distinct geography, access mode, communications dependency `INF-19`, and count uncertainty. Calling it a special-case cohort risks subordinating it to Merrow Port or the general displaced population. The uncertainty around count is a reason to make it visible, not a reason to demote it.

The plan can note that its governance and service structure are under-specified, but the risk register should carry outer-islet risks directly.

**(c) Definition of “stabilised” at T0+10d.**

At T0+10d, “stabilised” should mean the response has moved from uncontrolled acute failure to managed continuity with named residual risks. It should not mean normality, full recovery, or all services restored.

Observable criteria:

- `POP-09` dialysis continuity: every known South Latch dialysis patient has a confirmed treatment pathway, transport path, or documented exception requiring escalation; `POP-10` Merrow Port dialysis continuity separately confirmed.
- `POP-11` neonatal care: occupancy status known; if occupied, power, referral, and clinical continuity are confirmed through `INF-01`, `INF-30`, `INF-32`, or transfer to `INF-02`.
- `POP-12` home oxygen / CPAP: known high-dependency users have power, oxygen supply, charging, shelter placement, or clinical referral.
- `POP-13`, `POP-14`, `POP-15`: insulin and refrigerated-medication continuity has a functioning cold-chain workaround or replacement pathway, tied to `SVC-08`.
- `POP-08`: `INF-12` and `INF-13` status known; residents have water, power, medication, staffing, evacuation, or shelter continuity.
- `POP-05`: contact established or failed-contact escalation documented with a live search/access plan; VHF `INF-19` status assessed or bypassed.
- `SVC-04`: Merrow Port potable-water provision covers `POP-17` not on backup-well rotation, or the gap is quantified and under active supply plan.
- `SVC-05`: grid restoration is not required to be complete, but critical facilities and medical cohorts have backup power or relocation arrangements.
- `SVC-06`: `POP-06` displaced population has shelter capacity that is not merely “strained” but allocated, monitored, and connected to medical and language needs.
- `SVC-13` / `SVC-15`: public information reaches `POP-02` language groups through verified channels or named fallback channels.
- Critical dependencies have owners and tripwires: `INF-30`, `INF-32`, `INF-05`, `INF-06`, `INF-14`, `INF-17`, `INF-21`.

The assumptions I had to make are that “known” can be operationally established within the workspace’s planned actions, that local or central actors can maintain lists without importing a new identity system, and that treatment pathways can be verified without specifying clinical protocols.

**(d) `EXT-01` central-government counterparty: accept, flag, insist on fallback.**

Accept for planning, flag as assumption, and insist on fallback for critical actions. `ASM-19` allows the plan to treat `EXT-01` as a reliable counterparty, but no critical path should depend on central government as the only path where near-term harm is plausible.

For example, central support may be needed for fuel, air clearance, medical evacuation, water logistics, or outer-islet access. But `POP-09`, `POP-11`, `POP-12`, `POP-08`, and `POP-17` cannot wait for an untested external handoff without local bridging actions.

## Q6. Validation claims at Session 002 close

Under workspace-only validation (`CON-02`), Session 002 can legitimately claim internal coherence, traceability, and disciplined uncertainty handling. It can claim that each risk in the register is grounded in brief-provided populations, infrastructure, services, dependencies, assumptions, and silences. It can claim that the response plan covers the named first-class cohorts and does not collapse medical fragility into `POP-5K-parent`. It can claim that actions are linked to risks, cohorts, services, dependencies, time windows, and review triggers.

It can also claim process rigor: the deliberation considered multiple perspectives; used stable IDs; respected Session 001 decisions such as `DEC-05`, `DEC-06`, and `ASM-20`; and preserved assumptions rather than converting them into facts.

It cannot claim field validity. It cannot claim that the plan would save a particular number of lives, meet clinical standards, satisfy legal duties, or match Nivaro’s actual institutional capacity. It cannot claim that the selected ordering is objectively correct in the real world. It cannot claim that `ASM-08` backup wells are truly potable, that `ASM-17` road referral is actually feasible, that `ASM-19` central-government reliability will hold, or that utility restoration under `ASM-10` will occur inside 3-7 days.

It also cannot claim completeness. The silences are too material: generator fuel status, aged-care cluster status, outer-islet count, neonatal occupancy, language-channel coverage, informal care networks, mortuary capacity, and levee condition all limit evidentiary rigor.

The specific gravitation to resist is the tendency to treat a well-structured plan as an operationally validated plan. A risk register with excellent cross-references is still only workspace-valid unless checked against responders, affected communities, domain experts, or observed field data.

## Q7. Where the single-model form is distorting your work

I saw several places where a single model is too flat for the work Session 002 needs.

First, cohort-to-service dependency needs a view that is cohort-centered, not infrastructure-centered. To reason about `POP-09`, `POP-10`, `POP-11`, `POP-12`, `POP-13`, `POP-14`, and `POP-15`, I needed to see time-to-harm, service dependency, location, power dependency, transport dependency, and fallback pathway side by side. The single model lists these elements, but it does not expose a medical-continuity view cleanly.

Second, access geography needs its own view. `POP-05`, `POP-16`, `INF-15`, `INF-16`, `INF-20`, and flood-receding conditions interact differently across Merrow Port, South Latch, Kellan Rise, and the outer islets. A single list of infrastructure nodes does not reveal which cohorts are reachable by road, sea, air, one-at-a-time flood access, or not at all.

Third, shared-fate dependencies need a network view. `INF-14` is a rail bridge, but because it carries `INF-17` under `DEP-08`, damage may affect telecommunications `SVC-13` and Kellan Rise connectivity through `DEP-15`. This is exactly the kind of risk that can be missed if infrastructure is read as an asset list rather than a dependency graph.

Fourth, uncertainty needs a live discovery view. `SIL-*` items are first-class, but the model summary does not show which silences could hide acute cohort harm versus which are lower-order planning gaps. Session 002 needs a view that ranks unknowns by plausible harm window.

Fifth, “stabilised” needs an outcomes view. The model is good at naming components, but less good at showing what observable state each component must reach by T0+10d. I had to derive stabilisation criteria outside the model form.

These are not fatal flaws, but they count toward the §5.1 minority watch because they required re-deriving dependencies or views not cleanly exposed by the single model.

## External inputs surveyed (if any)

No new external framework is proposed for application.

I deliberately did not apply ICS/NIMS, UN/IASC cluster logic, Sphere minimums, lifelines doctrine, triage colour-coding, or likelihood-impact matrix orthodoxy as governing frameworks. Where my answer resembles standard practice, such as using review gates, action IDs, or risk fields, I am treating those as generic record-keeping structures and grounding the actual choices in the brief’s `POP-*`, `INF-*`, `SVC-*`, `DEP-*`, and `ASM-*` content.

## Honest limits

This perspective cannot know what the other four perspectives will converge on, so my frame-check is anticipatory rather than responsive. I also cannot validate clinical urgency, engineering feasibility, transport capacity, or local governance arrangements from the workspace alone. My strongest claim is structural: Session 002 should preserve cohort individuation, avoid false quantitative precision, make unknown-status discovery operational, and define T0+10d stabilisation as observable managed continuity rather than recovery.
