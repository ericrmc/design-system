---
session: 013
phase: P3 — multi-axis allocation under scarcity
issued_at: T+192h post-cyclone (Day 8 of 10-day response window)
issuer: Operator (Laurel Delta Emergency Coordinator's office, via Nivaro central government liaison)
input_kind: reveal-with-day7-followup
do_not_edit_prior_sessions: true
---

# Session 013 input — multi-axis scarcity at Day 8

## Read this first

This input has two layers. **Layer A is the Day-7+ data delivery** the S011/S012 close-records named as required for next session. The data is delivered here; values are factual deliveries, not editorial choices. **Layer B is three new scarcity axes** the response plan has not yet enumerated. Each Layer-B axis carries finite supply against multiple demands the response plan has already authored.

The combination is the test: each demand, taken alone, can be satisfied from current resource. **Together, no allocation simultaneously satisfies all of them.** The agent's task is to record the tradeoff explicitly, not to allocate-and-move-on. The substrate's `decision_v2` rows are the natural surface for capturing first-class allocation conflicts; whether the existing decision-record shape is sufficient or whether a new substrate primitive is warranted is itself a second-order question worth surfacing in engine-feedback.

Prior session provenance (S001 through S012) is closed and **must not be edited**. New decisions belong to S013. The `[ACTIVE-WITH-CONFLICT]` four-field discipline (with sub-type annotations as authored at S011 / DV-S011-5) is the available shape; whether it covers multi-demand allocation conflicts cleanly is for the agent to judge — and to surface as engine-feedback if the shape strains.

## Layer A — Day-7+ chase results

### A-1 — A-017 cold-chain warehouse fuel-hours verification report (T+170h)

Utility/Logistics Team Lead delivered the verification report at T+170h, inside the 2-hour deadline DV-S011-4 set.

- **Reported fuel-hours-remaining at T+170h: 14 hours** (cascade clock advances from T+185h to **T+184h**; one hour earlier than planned).
- **Sustained-load consumption rate**: ~1 hour of fuel per 1 hour elapsed under refrigeration load (steady; no degradation).
- **Same-circuit-as-A-006 question**: warehouse generator is on a **separate logistical chain** from the hospital generator. Different fuel supplier contract, different tanker pool. Confirms the dual-line resupply discipline DV-S011-4 anticipated; does not allow tanker-shared-trip.
- **Independent secondary refrigerated stock at Merrow Port Regional pharmacy**: ~6 hours of equivalent capacity (small in-pharmacy fridge, not a logistical alternative for cohort-level supply).

Field action already taken under A-017 contingency-3 pre-stage: warehouse fuel tanker dispatched T+172h via highway bridge; **arrived T+178h** (cycle time within the 2.5h convoy window). Warehouse refilled to ~28 hours run-time.

### A-2 — Day-6 + Day-7 crossing-log delivered (T+180h)

Bridge Scheduling Officer delivered the rolling crossing-log analysis at T+180h, including Day-7 partial-day data through T+180h.

- **Day 6: 6.7h** consecutive bridge hours (above 6h floor).
- **Day 7 (T+168h to T+180h, partial 12h window): 6.4h** projected to 24h equivalent (above 6h floor).
- **Trailing-3-days indicator at this delivery**: Day 4 = 6.2h, Day 5 = 5.4h, Day 6 = 6.7h. Variance = **0.95h** (Day 5 low, Days 4 and 6 closer to mean).

Per A-009b closure path (a) (≤ 0.5h variance across three consecutive days within the evaluation window): **convergence threshold not met**. A-009b remains `[ACTIVE-WITH-CONFLICT]`. The S012 rejection of folding (DV-S012-1) is preserved.

### A-3 — Next 24h-cycle satellite-uplink allocation review (T+190h, F-4 follow-on)

Provincial coordination meeting at T+190h reduced Laurel Delta's allocation. **Allocation worsened**:

- **Previous (T+166h to T+190h)**: 2 satellite passes per day (1 optical, 1 radar) + 4 hours per day high-priority uplink.
- **New (T+190h to T+214h)**: **1 satellite pass per day (radar only — optical pass redirected to a higher-priority adjacent district that has a search-and-rescue active phase) + 4 hours per day high-priority uplink** (uplink unchanged).
- **Reason cited**: search-and-rescue prioritisation in adjacent district plus continued oversubscription.

Per A-018 failure-case contingency, this triggers Emergency Coordinator escalation to Nivaro central-government emergency liaison: **central-government re-allocation appeal** is the documented escalation channel. The appeal does not block any other action; it runs in parallel.

If the next 24h-review (T+214h) shows further reduction, A-018 closure path (b) — response-plan re-scoping — becomes canonical per A-018's three-consecutive-cycles trigger.

### A-4 — Cold-chain warehouse status (sustained, T+178h to T+192h)

Refrigerated stock integrity confirmed by Hospital Pharmacy Director at T+178h (post-tanker-arrival). Warehouse generator on resumed steady-state at T+178h. Cascade-clock paused on the immediate concentrate/anticoagulant deadlines (T+191h anticoagulant, T+215h concentrate), but a **new cascade-clock condition** opens (see Layer B).

## Layer B — Three new scarcity axes (Day-8 reveal)

The response plan has used "central government dispatch" and "provincial-level allocation" as if each were a single axis with bounded queue. Three of those axes are now revealed as **competing for finite supply against multiple demands the plan has already authored** at S001 through S011.

### F-5 — Potable water rotation wells partially compromised

- **Trigger.** Provincial Geospatial Office reading and Maritime Officer field report at T+186h: tidal back-flow event (the same cycle that flooded the port-side substation in F-3) reached two of the four currently-rotating backup wells in the Merrow Port + South Latch periphery, contaminating their immediate intake.
- **Source — Utility operator field report (T+187h), confirmed by Maritime Officer (T+188h).** The two compromised wells served approximately **14,000** of the ~35,000 currently on rotation. Rotation now reduces to **two wells serving ~21,000**, leaving the remaining ~14,000 (previously served by the compromised wells) without backup-well coverage.
- **Cumulative water-supply gap**. Merrow Port population 62K + South Latch 58K = 120K. External tanker supply confirmed for ~120K demand; backup wells previously off-set ~35K (not to substitute, but to reduce tanker-rationing pressure). With wells reduced to 21K coverage: **incremental tanker-supply demand for the previously-well-served 14K is now on the central-government tanker convoy queue**, alongside the existing ~85K Merrow Port-and-South-Latch external-supply demand and Phase-2-revised hospital-grade purified supply demands.
- **System-model node implicated.** "Water treatment plant — Merrow Port" parent — partial mitigation prose is now operationally outdated; previously-compromised partial mitigation had two-of-four-wells-degraded baseline at v1, now revised. Two **new sub-nodes** (or a refined parent prose) for each well's status.
- **Assumption implicated.** A-011 (South Latch potable water) is **not invalidated** but its failure-case contingency (extend tanker convoy coverage) is now the live action.

### F-6 — Generator transfer-switch parts inventory rationed

- **Trigger.** Utility operator parts request at T+188h to Provincial Energy Office: Port-side substation restoration (per F-3) requires **4 transfer-switch units**. The provincial parts depot reports current inventory at **2 units immediately available across all three affected districts**.
- **Source — Provincial Energy Office inventory log (T+189h), forwarded by Nivaro central government liaison (T+190h).** Adjacent districts have submitted requests as well; total demand across three districts at the next 7-day window is **9 transfer-switch units**. Inventory: 2. The next supply shipment is gated on manufacturer dispatch from outside Nivaro; estimated arrival in **5–7 business days** (i.e., outside the 10-day response window unless airfreighted on emergency-supply priority).
- **Allocation implication.** Of the 2 units immediately available: zero, one, or two could be allocated to Laurel Delta's port-side substation (per F-3). The decision is provincial-level. With zero allocation: port-side substation restoration delayed beyond response-plan window; cold-chain warehouse remains on dual-line resupply discipline indefinitely. With one allocation: partial restoration; halved capacity. With two allocations: full restoration possible if Laurel Delta wins the inter-district arbitration.
- **System-model node implicated.** "Power substation — Merrow Port port-side" — restoration timeline parameter is now contingent on parts-allocation arbitration, not on flood-recession alone.
- **Assumption implicated.** Implicit. Add new A-NNN (registered-vs-implicit gap-closure pattern, single-source: provincial inventory; **NOT ACTIVE-WITH-CONFLICT** unless agent judges arbitration conflict admits source-vs-source semantics — operator does not pre-judge).

### F-7 — Medevac slots Kellan Rise → provincial hospital rationed

- **Trigger.** Provincial hospital (the regional Level-3 facility serving Laurel Delta + adjacent districts via medevac) advised at T+184h: critical-care capacity at **78% utilisation**, with 6 of 32 beds available; refusing routine transfers; Laurel Delta allocated **6 medevac slots per 24-hour window** (down from the informal "as-needed" arrangement implicit through Day 7).
- **Source — Provincial hospital duty officer (T+184h), confirmed via Nivaro central government liaison (T+185h).** Allocation reviewed every 24h; can be increased temporarily on central-government request for life-safety surge events.
- **Demand against allocation.** Three competing demands have already been authored into the response plan at S001 through S011 and now compete for the 6-slot/24h envelope:
  1. **Original dialysis patient evacuation queue** (per response-plan §Phase 1 Priority 2 + Day-3 Indicator 1 + Day-7 Item 1 escalation): residual high-acuity patients not absorbed by Kellan Rise dialysis, tracked at Day 7 evaluation against Item 1 thresholds.
  2. **Air-corridor ambulance Slot-2 augmentation** (DV-S011-1; uses helicopter sortie capacity which shares the same medevac fleet). Currently active.
  3. **Cold-chain redirect contingency** (A-017 failure-case contingency-1: Kellan Rise pharmacy; ground-transport not necessarily medevac, but if highway bridge operational floor breaks again the same medevac fleet is the substitute). Currently dormant but pre-staged.
  4. **Cold-chain substitute-supply ingress** (A-017 failure-case contingency-2: fresh stock dispatched via the activated air-corridor; uses the same air-corridor capacity that medevac slots flow through). Currently dormant.
- **System-model node implicated.** New node — **Provincial-level medevac slot allocation** — sized parallel to "Provincial-level satellite-uplink resource allocation" (the F-4 / S011 precedent). Sub-type annotation question: rolling-renewal expiry like A-018, or single-event closure like A-005. Operator does not pre-judge.
- **Assumption implicated.** Implicit. Add new A-NNN with the discipline DV-S011-5 established for A-018.

## The forced tradeoff (the §3d test)

**Read each in isolation.** Each of the items below could be satisfied alone from the current resource envelope. Read them simultaneously, and not all can.

- **Fuel for hospital generator (A-006)** + **fuel for cold-chain warehouse (A-017)** → highway-bridge resupply slots, sized at the 6h operational floor with 1.5h reserve. Two parallel lines; doable solo, tight together.
- **Air-corridor ambulance Slot-2 augmentation (DV-S011-1)** + **medevac slots dialysis evacuation residuals** + **A-017 contingency-2 cold-chain ingress (if fired)** → 6 medevac slots / 24h. **Sum of demands exceeds supply** if all three are active simultaneously.
- **Transfer-switch units for port-side substation restoration (F-6)** → **2 units available across 3 districts; Laurel Delta needs 4 to fully restore**. Even maximum allocation (2/2 to Laurel Delta) covers half the substation; full restoration delayed beyond Day 10.
- **Satellite uplink hours (A-018)** + **uplink for medevac coordination (F-7) + A-006/A-017 fuel-tanker dispatch coordination (A-012)** → 4h/day uplink window. Three asks against a single window; routine-vs-critical prioritisation forced.
- **External-tanker water demand (A-011 / F-5)** + **central-government tanker pool used for fuel resupply (A-006 / A-017)** → central-government tanker dispatch capacity is finite; the queue order matters.

The asks are real; the supply is limited; the operator does not pre-judge any allocation. The agent decides.

## Prior assumptions implicated (consolidated)

- **A-009b** — A-009b path-(a) closure NOT eligible (Layer A-2 0.95h variance); folding rejection from DV-S012-1 preserved.
- **A-017** — fuel-hours verified at 14h (advanced cascade clock to T+184h); tanker dispatched and warehouse refilled to ~28h; cascade clock paused but resumes if next tanker is delayed beyond ~T+200h.
- **A-018** — allocation worsened (Layer A-3 1 pass + 4h vs prior 2 + 4h); failure-case contingency triggers central-government re-allocation appeal; rolling-renewal continues.
- **A-011** — failure-case contingency (extend tanker convoy coverage to South Latch) is now live action per F-5.
- **A-012** — central-government dispatch is now the single-shared queue across (mobile dialysis, water tanker, fuel tanker, transfer-switch parts, cold-chain substitute supply, medevac surge requests). The "24h dispatch / 36–48h arrival" assumption applied to one ask each; under multi-ask competition for the same dispatch capacity, the assumption does not state how queueing is resolved.
- **Implicit (F-6 / F-7)** — two new A-NNN entries needed: transfer-switch parts allocation and medevac-slot allocation. Shape discipline per DV-S011-4 / DV-S011-5 — agent decides whether ACTIVE-WITH-CONFLICT (with sub-type annotations) or A-006-shape.

## Constraints on this session

1. **Do not edit prior session provenance.** S001–S012 close-records, decisions, and provenance markdown are immutable. New decisions belong to S013.
2. **Make the tradeoff explicit.** Where two or more demands compete for the same finite supply, the response-plan revision and the assumption-ledger entry must name the competing demands, the supply envelope, and the chosen prioritisation with rationale. Narrative-only revision is laundering.
3. **Cite the cascade-event trigger in every change.** F-5 / F-6 / F-7 anchors plus the source role and timestamp.
4. **Supersession-ledger update for every status change AND for every new A-NNN entry.** Include parent-node lineage when a new system-model node is added (per S011 discipline). The supersession-ledger discipline is now load-bearing.
5. **Cross-artefact citation discipline** unchanged. Every response-plan revision cites the system-model node IDs and assumption IDs it depends on; risk-register entries cite the F-N anchor.
6. **Conflict-shape discipline.** The sub-type annotation pattern from DV-S011-5 is available; whether F-6 (parts allocation) and F-7 (medevac slot allocation) admit the four-field shape with sub-type annotation, or whether multi-axis allocation conflicts surface a different shape, is for the agent to judge — and to record as engine-feedback if the existing shape strains.
7. **Air-corridor activation status.** DV-S011-1 air-corridor is currently active. Any action that consumes air-corridor capacity (medevac slots, cold-chain ingress, ambulance Slot-2 augmentation) is competing against the same finite envelope; explicit prioritisation in response-plan section.
8. **No new domain content beyond Layer A and Layer B.** The agent does not invent new field signal.

## Engine-surface signals the operator is watching for

These are not constraints on the agent — they are what the operator is reading the artefacts for. Disclosed to remove ambiguity about why the reveal is shaped this way.

- Whether the agent **records the tradeoff as first-class structure** (substrate decision rows with explicit alternative-rejection reasons; assumption-ledger entries with both-source citation extended to demand-vs-supply) or compresses to narrative paragraphs (constraints §2 failure-as-cheap, §3 cross-family value-conflict).
- Whether the conflict-shape discipline (DV-S008-1 / DV-S011-5 sub-type annotations) generalises to multi-demand allocation, or whether multi-axis surfaces a third shape limit beyond plan-vs-resource and rolling-renewal — third-arc-friction evidence point for OI-S124-1 arc-close re-evaluation.
- Whether **cross-family deliberation is convened** for the prioritisation decision (the synthesis at S124 named cross-family at-minimum P4 and P6, more often if budget allows; multi-axis allocation-under-scarcity has the cross-family value-conflict shape methodology §When-to-convene names).
- Whether the agent treats F-5 / F-6 / F-7 as **independent reveals** (each separately processed) or as **multi-axis** (the §3d test is the simultaneity).
- Whether the substrate's existing decision-record shape (decisions_v2 with supports / effects / alternatives / alternative_rejections) is sufficient for recording the value-conflict, or whether the agent surfaces a shape limit warranting a new substrate primitive.

## Out of scope

- Phase 3 / Day-10 transition-report content (P5 phase territory).
- Recovery-plan content. The 10-day window remains the frame.
- Stakeholder authority questions (P4 phase territory; not surfaced here).
- Aftershock-driven secondary structural failures beyond F-1 already-revealed (P5 phase territory).
- New domain incidents beyond F-5 / F-6 / F-7.

## Closing protocol for this session

Per prompts/application.md and per this arc's anti-laundering criteria: produce ≥ 1 engine-feedback row capturing what the multi-axis allocation shape revealed about the engine. The operator transports it back to self-development via `monitor-external harvest-ef`.

Engine-feedback this session is expected to land on at least one of:
- whether the substrate's existing decision-record shape is sufficient for first-class value-conflict recording, or whether a new primitive is warranted (cites EF-S008-1 / EF-S011-1 typed-conflict-primitive question, third-arc-friction evidence)
- whether cross-family deliberation activated for the prioritisation decision and whether the family-mix surfaced a frame the single-family reading would have missed
- whether the multi-axis simultaneity was recorded as a single tradeoff structure or as independent reveals

Other observations are welcome.
