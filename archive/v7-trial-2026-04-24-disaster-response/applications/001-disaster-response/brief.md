---
title: Application 001 — disaster-response
originating_session: 001
engine_version: engine-v7
status: brief-populated
created: 2026-04-24
workspace_id: selvedge-disaster-response
---

# Application brief — disaster-response


## Problem statement
**Laurel Delta**, a low-lying island-and-estuary district in the invented country **Nivaro**. The setting is fictional; no real geography or public disaster case is imported, so the executing sessions must reason from the brief rather than leaning on memorised domain knowledge (anti-laundering per PROMPT.md external-imports rule).

Laurel Delta has three main settlements:
- **Merrow Port** (coastal, ~62K, working harbour + industrial fishery; dense waterfront tenements; one regional hospital with ~450 beds including a neonatal unit).
- **South Latch** (low-lying agricultural plain, ~58K, dispersed smallholdings + two aged-care clusters; levee-dependent; one primary-care clinic + one dialysis centre serving ~1,200 patients).
- **Kellan Rise** (upland approach, ~80K, mixed urban-residential; one secondary hospital ~280 beds; principal road-access to the highlands).

Total affected population: approximately **200,000**.

- ~9% over age 70 (~18K).
- ~2.5% dependent on powered medical equipment (~5K) — CPAP, home oxygen, refrigerated medications (insulin, biologics).
- ~1,200 dialysis-dependent in South Latch; regional hospital handles ~220 more.
- Migrant-worker seasonal housing near Merrow Port industrial fishery (~9K) — low-quality dormitories; two languages other than the majority.
- Dispersed fishing community on outer estuary islets — informal VHF-radio networks; no reliable cellular coverage even pre-disaster.
- One freight rail bridge connecting Merrow Port to the interior; this bridge also carries a major fibre-optic trunk serving Kellan Rise.

A late-season cyclone has crossed Laurel Delta approximately 36 hours before Session 001 opens. Current observable state:

- Storm surge peaked ~2.8m above mean high tide; lower Merrow Port and two thirds of South Latch are flooded; water is receding unevenly.
- Approximately 18,000 people are displaced; shelter capacity strained.
- Grid power is out across Merrow Port and South Latch; two of four coastal substations degraded; partial restoration estimated 3-7 days by local utility.
- The primary drinking-water treatment plant in Merrow Port has salt-water intrusion; decontamination assessment underway; backup wells serve ~35K on rotation.
- Hospital continuity risk: Merrow Port regional hospital on generator; Kellan Rise secondary hospital unaffected; dialysis centre in South Latch inaccessible.
- Road access: the freight rail bridge damaged but passable; one highway bridge into Merrow Port intact at 24-tonne rating; sea access degraded (salvage required); air access degraded (runway debris).
- Local government in Laurel Delta has requested from central government a **10-day response-and-stabilisation plan** that Session 001 will produce v1 of.

## Constraints

Domain: fictional self-contained scenario; no real geography or public disaster case is referenced; no practitioner or real emergency-management standard is consulted.

Time: Laurel Delta local government has requested a 10-day response-and-stabilisation plan.

Stakeholder: the artefact is produced from inside this workspace without external consultation.

## Stakeholders

Affected population: ~200,000 across Merrow Port (~62K), South Latch (~58K), Kellan Rise (~80K); vulnerability profile per the  problem statement above.

Plan recipients: Laurel Delta local government; Nivaro central- government emergency coordinator.

Validators: no domain-actor is available for this fictional scenario. Validation is qualitative multi-agent: the session's  artefacts are claimed valid under internal coherence, cross- artefact consistency, and adversarial-probe sufficiency. There is no real-world reference case against which to validate.

## Success condition

The response plan addresses the 10-day response-and-stabilisation requirement under the T0 state described above. Produced v1  artefacts (system model, assumption ledger, risk register, response plan) are internally consistent with each other and cite assumptions explicitly (no premise used implicitly).

## Initial state

No prior materials. Session 001 starts from the problem statement above. Read the engine-definition files, this brief, and `session-inputs/session-001-input.md` 
