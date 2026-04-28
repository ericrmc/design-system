---
title: Laurel Delta system model — v1 (superseded)
originating_session: 001
artefact_kind: system-model
domain: disaster-response
engine_version: engine-v7
validation: workspace-only
status: superseded
superseded-by: system-model.md
superseded-session: 003
supersession-reason: §5.1 multi-view activation warrant fired at Session 002 close (D-019); v2 adopted Session 003 per D-021 + D-025
created: 2026-04-24
last-revised-session: 001
---

# Laurel Delta system model — v1

This document is a typed dependency map of Laurel Delta at **T0**
(approximately 36 hours post-cyclone-landfall), produced in Session
001 per `provenance/001-session/02-decisions.md` D-001. It is an
**input to Session 002's risk register and response plan**, not a
plan itself.

**Scope.** Populations, infrastructure, services, dependencies,
external interfaces, and first-class silences/unknowns. No risk
scoring, no prioritisation, no action allocation — those are Session
002's work per D-009. No numeric values for time-to-harm clocks or
service capacities are imported from pretrained distributions per
anti-laundering discipline; `unknown` is the honest value where the
brief is silent.

**Indexing.** Populations, infrastructure, and services are keyed
independently (`POP-*`, `INF-*`, `SVC-*`); settlement is an attribute
on entries, not a top-level organising axis (D-006). Dependencies
(`DEP-*`) are typed edges between model elements.

**Every row has a stable ID.** IDs are the primitive downstream work
keys against per D-010.

**Cross-reference conventions.** `brief:§X` points to the application
brief (`applications/001-disaster-response/brief.md`); `ASM-*`,
`CON-*`, `GIV-*`, `DEC-*` point to the assumption ledger
(`assumption-ledger.md`).

## 1. Time-frame

Per D-004, the 10-day horizon is recorded as `GIV-01` in the ledger
(given-flagged-for-survey). Two orientation sub-windows are exposed
so downstream risk and plan work can align with different time-to-
harm clocks:

| Window ID | Label | Range | Notes |
|---|---|---|---|
| `WIN-acute` | Acute window | T0 to ~T0+72h | Shortest time-to-harm clocks fall inside this window (see `POP-*` `time_to_harm` attributes). |
| `WIN-stab` | Stabilisation window | ~T0+72h to T0+10d | Brief's named horizon per `GIV-01`. |

These windows are orientation labels, not operational compartments.
The brief's 10-day frame covers both.

## 2. POP-* — Population cohorts

Cohorts are named, attribute-indexed, and decomposed per D-003 and
D-007. Settlement totals are listed in their own sub-table for
completeness but are not the model's primary axis (D-006).

### 2.1 Structural populations (settlement totals)

| ID | Label | Count | Settlement | Source | Notes |
|---|---|---|---|---|---|
| `POP-01` | Merrow Port total population | ~62,000 | Merrow Port | brief:§Territory | Includes `POP-02` dormitory cohort (`ASM-01`: overlap structure). |
| `POP-02` | Merrow Port migrant-worker dormitory cohort | ~9,000 | Merrow Port | brief:§Territory | Two non-majority languages; seasonal housing (`ASM-02`: current T0 occupancy not stated). |
| `POP-03` | South Latch total population | ~58,000 | South Latch | brief:§Territory | Dispersed smallholdings + two aged-care clusters. |
| `POP-04` | Kellan Rise total population | ~80,000 | Kellan Rise | brief:§Territory | Mixed urban-residential. |
| `POP-05` | Outer-islet fishing community | unknown | outer-islets | brief:§Territory | Count not stated; `SIL-01` records this. |
| `POP-06` | Displaced persons (T0) | ~18,000 | district-wide | brief:§Current state | Shelter capacity strained; dynamic figure (`ASM-03`: stability for planning). |

### 2.2 Age cohorts

| ID | Label | Count | Settlement | Source | Notes |
|---|---|---|---|---|---|
| `POP-07` | Aged 70+ | ~18,000 | district-wide | brief:§Additional populations | Most not in `POP-08` (`ASM-04`: institutional-vs-distributed split not stated; inferred majority distributed). |
| `POP-08` | Institutionally housed aged (South Latch aged-care clusters) | unknown | South Latch | brief:§Territory | Two clusters; resident count not stated (`SIL-02`); clusters themselves as sites are `INF-12`, `INF-13`. |

### 2.3 Medical-fragility cohorts (individuated per D-003, decomposed per D-007)

| ID | Label | Count | Settlement | Source | `time_to_harm` | Notes |
|---|---|---|---|---|---|---|
| `POP-09` | South Latch dialysis-centre patients | ~1,200 | South Latch | brief:§Territory | window: days (conservative); driver: "dialysis interval"; source: `pretrained-clinical-knowledge-declined` | Centre (`INF-04`) inaccessible T0 (`DEP-09`). |
| `POP-10` | Merrow Port regional dialysis patients | ~220 | Merrow Port | brief:§Additional populations | window: days; driver: dialysis interval; source: `pretrained-clinical-knowledge-declined` | Cared for at `INF-02`; (`ASM-05`: non-overlap with `POP-09`). |
| `POP-11` | Merrow Port regional neonatal unit occupants | unknown | Merrow Port | brief:§Territory | window: hours to days; driver: "neonatal life support"; source: `to-be-supplied-by-domain-review` | Unit is `SVC-09`; occupancy count not stated (`SIL-03`). |
| `POP-12` | CPAP / home-oxygen dependents | unknown | district-wide | brief:§Additional populations (subset of ~5K) | window: hours to days; driver: "power / oxygen cylinder resupply"; source: `pretrained-clinical-knowledge-declined` | Sub-cohort of `POP-5K-parent` (see below). |
| `POP-13` | Insulin-dependent cohort | unknown | district-wide | brief:§Additional populations (subset of ~5K) | window: 1–5 days; driver: "cold-chain + resupply"; source: `pretrained-clinical-knowledge-declined` | Sub-cohort. |
| `POP-14` | Refrigerated-biologic-dependent cohort | unknown | district-wide | brief:§Additional populations (subset of ~5K) | window: days; driver: "cold-chain continuity"; source: `pretrained-clinical-knowledge-declined` | Sub-cohort. |
| `POP-15` | Other refrigerated-med dependents | unknown | district-wide | brief:§Additional populations (subset of ~5K) | window: unknown; driver: unknown; source: `unknown` | Sub-cohort; residual after 12–14. |
| `POP-5K-parent` | Powered-medical-equipment dependent cohort (parent) | ~5,000 | district-wide | brief:§Additional populations | — | Parent aggregate per D-007; `POP-12` through `POP-15` are its sub-cohorts with `count: unknown` each (`ASM-06`: sub-cohort size distribution not stated). |

### 2.4 Access-constrained cohorts

| ID | Label | Count | Settlement | Source | Notes |
|---|---|---|---|---|---|
| `POP-16` | South Latch dispersed smallholding residents | unknown subset of `POP-03` | South Latch | brief:§Territory | One-homestead-at-a-time access under flood (`DEP-05`). |
| `POP-17` | Merrow Port residents not on backup-well rotation | ~27,000 (arithmetic: 62K − 35K served by `INF-06`) | Merrow Port | brief:§Current state | `ASM-07`: brief arithmetic; residents-as-distinct-from-dormitory not disaggregated. |

**Silenced / absent cohorts** (see `SIL-*` section): pregnancy and
early-infant populations outside the neonatal unit (`SIL-04`);
mental-health / substance-dependence continuity cohorts (`SIL-05`);
children under 5 as a distinct cohort (`SIL-06`); disability cohorts
beyond powered-equipment users (`SIL-07`); undocumented persons as a
distinct cohort (`SIL-08`).

## 3. INF-* — Infrastructure elements

Infrastructure state is recorded with `epistemic_source` per the
Adversarial Skeptic's T0-is-reported-not-physical principle
[`provenance/001-session/01C-perspective-adversarial-skeptic.md`, Q1].

### 3.1 Health

| ID | Label | Settlement | T0 status | Epistemic source | Source | Notes |
|---|---|---|---|---|---|---|
| `INF-01` | Merrow Port regional hospital (~450 beds incl. neonatal) | Merrow Port | on generator | brief statement | brief:§Territory + §Current state | Fuel status `unknown` (`SIL-09`); delivers `SVC-01`, `SVC-08`, `SVC-09`, `SVC-03` (dialysis overflow). |
| `INF-02` | Kellan Rise secondary hospital (~280 beds) | Kellan Rise | unaffected | brief statement | brief:§Territory + §Current state | Delivers `SVC-01` for Kellan Rise and possible surge for `INF-01`. |
| `INF-03` | South Latch primary-care clinic | South Latch | unknown T0 state (brief silent) | brief enumeration | brief:§Territory | `SIL-10`: T0 state not stated. |
| `INF-04` | South Latch dialysis centre | South Latch | inaccessible | brief statement | brief:§Current state | Serves `POP-09`. |
| `INF-12` | South Latch aged-care cluster A | South Latch | unknown T0 state | brief enumeration | brief:§Territory | Houses part of `POP-08`; flood state `SIL-11`. |
| `INF-13` | South Latch aged-care cluster B | South Latch | unknown T0 state | brief enumeration | brief:§Territory | Houses part of `POP-08`; flood state `SIL-11`. |

### 3.2 Water

| ID | Label | Settlement | T0 status | Epistemic source | Source | Notes |
|---|---|---|---|---|---|---|
| `INF-05` | Merrow Port drinking-water treatment plant | Merrow Port | salt-intruded; decontamination assessment underway | brief statement (reported) | brief:§Current state | Treatment-timeline not stated. |
| `INF-06` | Backup wells | Merrow Port (serves) | operational, rotation serving ~35K | brief statement (reported) | brief:§Current state | Potability assumed (`ASM-08`). |

### 3.3 Power

| ID | Label | Settlement | T0 status | Epistemic source | Source | Notes |
|---|---|---|---|---|---|---|
| `INF-07` | Coastal substation A | Merrow Port area | degraded | brief statement (utility-reported) | brief:§Current state | 2-of-4 substations degraded per brief; specific identification (A vs B) `SIL-12`. |
| `INF-08` | Coastal substation B | Merrow Port area | degraded | brief statement (utility-reported) | brief:§Current state | See `INF-07` note. |
| `INF-09` | Coastal substation C | Merrow Port area | operational (inferred) | brief arithmetic | brief:§Current state | 2-of-4 remaining; `ASM-09`: distribution of degradation not stated. |
| `INF-10` | Coastal substation D | Merrow Port area | operational (inferred) | brief arithmetic | brief:§Current state | See `INF-09` note. |
| `INF-11` | Grid coverage — Merrow Port + South Latch | Merrow Port, South Latch | out | brief statement | brief:§Current state | Restoration 3–7 days per utility estimate (`ASM-10`). |
| `INF-30` | Regional hospital generator | Merrow Port | operational T0 | inferred from `INF-01` on-generator state | brief:§Current state | Fuel supply (`INF-32`) and consumption rate not stated (`SIL-09`). |
| `INF-31` | Other generators (district-wide) | district-wide | unknown T0 state | none | — | `SIL-13`: brief does not enumerate other generators; implied absence is an inference, not a fact. |

### 3.4 Transport

| ID | Label | Settlement | T0 status | Epistemic source | Source | Notes |
|---|---|---|---|---|---|---|
| `INF-14` | Freight rail bridge | Merrow Port — interior | damaged but passable | brief statement (reported) | brief:§Current state | Carries `INF-17` fibre trunk via `DEP-12`. |
| `INF-15` | Highway bridge into Merrow Port | Merrow Port | intact, 24-tonne rating | brief statement | brief:§Current state | Persistence over 10-day window `ASM-11`. |
| `INF-16` | Sea access | Merrow Port | degraded, salvage required | brief statement | brief:§Current state | Salvage service `SVC-14` is pre-requisite. |
| `INF-20` | Air access (runway) | location not specified in brief | degraded, runway debris | brief statement | brief:§Current state | Settlement hosting runway `SIL-14`. |
| `INF-21` | Levee — South Latch | South Latch | T0 state not stated | brief silence | brief:§Territory (levee-dependent) | `SIL-15`: state unknown; brief says South Latch is "levee-dependent". |

### 3.5 Communications

| ID | Label | Settlement | T0 status | Epistemic source | Source | Notes |
|---|---|---|---|---|---|---|
| `INF-17` | Fibre-optic trunk to Kellan Rise | Merrow Port — interior — Kellan Rise | T0 service state unknown | brief silence on operational state | brief:§Territory | Physically carried by `INF-14`; `ASM-12`: service state follows structural state. |
| `INF-18` | Cellular coverage — district | district-wide | impaired per grid/power outages (inferred) | inferred from `INF-11` | — | `SIL-16`: brief does not quantify cellular degradation; pre-disaster cellular absent on outer islets only. |
| `INF-19` | VHF networks — outer islets | outer-islets | pre-disaster: informal/operational; T0: unknown | brief silence on post-surge state | brief:§Territory | `ASM-13`: post-surge VHF operability not stated. |

### 3.6 Shelter

| ID | Label | Settlement | T0 status | Epistemic source | Source | Notes |
|---|---|---|---|---|---|---|
| `INF-22` | Shelter stock | district-wide | capacity strained | brief statement | brief:§Current state | Operators, locations, specific capacities `SIL-17`. |

### 3.7 Logistics / supply

| ID | Label | Settlement | T0 status | Epistemic source | Source | Notes |
|---|---|---|---|---|---|---|
| `INF-32` | Generator fuel supply chain | district-wide | not enumerated | brief silence | — | `SIL-18`: routes, cadences, operators not specified; regional-hospital generator fuel clock is the leading concern. |

## 4. SVC-* — Services

Services are the functions populations consume; they ride on
infrastructure but can fail independently.

| ID | Label | Delivering `INF-*` | Consuming `POP-*` | T0 continuity status | Capacity dimension | Notes |
|---|---|---|---|---|---|---|
| `SVC-01` | Acute hospital care | `INF-01` (degraded — on generator), `INF-02` (operational) | all settlement populations | degraded-in-Merrow-Port | beds | `INF-01` → `INF-02` referral via `DEP-16` implied; not stated. |
| `SVC-02` | Primary care | `INF-03` | `POP-03` | unknown | visits/day | See `SIL-10`. |
| `SVC-03` | Haemodialysis | `INF-04` (inaccessible), `INF-01` (for `POP-10`) | `POP-09`, `POP-10` | partial — `POP-09` not served | dialysis-slots | |
| `SVC-09` | Neonatal care | `INF-01` | `POP-11` | on-generator (power-dependent) | beds | |
| `SVC-10` | Aged-care continuity | `INF-12`, `INF-13`; plus informal care circles (`SIL-19`) | `POP-08`, `POP-07` | unknown | places / visits | |
| `SVC-04` | Potable water | `INF-05` (failed), `INF-06` (partial) | `POP-17` (not served by `INF-06`), `POP-02` (inclusion uncertain) | partial — ~35K served on rotation; ~27K gap | litres/day | `ASM-08` potability; `DEC-02` below on 27K arithmetic. |
| `SVC-05` | Electrical supply | `INF-07`–`INF-11` | all settlement populations | out-in-Merrow-Port-and-South-Latch | kWh | Underpins `SVC-08`. |
| `SVC-08` | Cold chain (refrigerated medication) | `INF-11` + on-site refrigeration (not enumerated) | `POP-13`, `POP-14`, `POP-15` | at-risk (grid out; no generator backfill enumerated beyond `INF-30`) | — | Service distinct from raw power per D-decomposition reasoning. |
| `SVC-06` | Shelter | `INF-22` | `POP-06` | strained | shelter-places | Operators not modelled. |
| `SVC-07` | Inter-settlement road transport | `INF-14` (damaged-passable), `INF-15` (intact 24-t) | district-wide | degraded | tonnage / vehicles | |
| `SVC-11` | Sea transport | `INF-16` | outer-islets (`POP-05`), supply logistics | degraded; salvage-first | — | Depends on `SVC-14`. |
| `SVC-12` | Air transport | `INF-20` | district-wide external | degraded | — | |
| `SVC-13` | Telecommunications | `INF-17`, `INF-18`, `INF-19` | all settlement populations; `POP-05` via `INF-19` only | degraded / unknown | — | |
| `SVC-14` | Salvage (sea-access prerequisite) | to be resourced | prerequisite for `SVC-11` | not-yet-active | — | Named as prospective service per D-001 `SIL-*`/out-of-scope rationale; not modelled in detail at v1. |
| `SVC-15` | Public information / risk communication | `INF-17`, `INF-18`, possibly `INF-19` | district-wide; `POP-02` requires non-majority-language channels | unknown coverage | languages, channels | `SIL-20`: language-channel coverage of `POP-02` not stated. |

## 5. DEP-* — Dependencies / relationships

Typed edges between model elements. Only relationships the brief
explicitly states are tagged `source: brief`; inferred couplings are
tagged `source: inferred` and are load-bearing only if an
assumption-ledger entry supports them. Rejected: `source: domain-
canon` (anti-laundering).

| ID | From | To | Relationship type | Source | Notes |
|---|---|---|---|---|---|
| `DEP-01` | `INF-11` | `SVC-05` | supplies | brief | |
| `DEP-02` | `SVC-05` | `POP-5K-parent` + `POP-12` through `POP-15` | powers / enables | inferred (`ASM-14`) | Brief does not state the coupling explicitly but it is the defining meaning of "powered medical equipment". |
| `DEP-03` | `INF-05` | `SVC-04` (baseline supply) | supplies | brief | Currently failed. |
| `DEP-04` | `INF-06` | `SVC-04` (backup supply) | supplies | brief | ~35K served on rotation. |
| `DEP-05` | Flooded lower Merrow Port + two thirds South Latch | physical access | constrains | brief | Affects `POP-16`, `INF-04`, possibly `INF-12`/`INF-13`. |
| `DEP-06` | `INF-15` (24-t) | `SVC-07` | routes | brief | Primary road artery. |
| `DEP-07` | `INF-14` | `SVC-07` | routes | brief | Damaged but passable. |
| `DEP-08` | `INF-14` | `INF-17` | carries (co-located / shared-fate) | brief | The single-bridge / two-service coupling. |
| `DEP-09` | `INF-04` inaccessible | `POP-09` dialysis-service gap | service-blocked-by-infrastructure | brief | |
| `DEP-10` | `INF-01` | `SVC-09` | delivers | brief | Neonatal on regional generator chain. |
| `DEP-11` | `INF-30` | `INF-01` | backs-up (generator → hospital) | brief | |
| `DEP-12` | `INF-32` | `INF-30` | supplies fuel to | inferred (`ASM-15`) | Supply chain not enumerated. |
| `DEP-13` | `SVC-05` | `SVC-08` | powers / enables | inferred (`ASM-16`) | Cold chain → power; named as distinct services per D-007 decomposition and 01A/01B convergence. |
| `DEP-14` | `INF-21` levee | `POP-03` habitability | conditional-habitability | brief (stated) | "South Latch is levee-dependent" per brief:§Territory. |
| `DEP-15` | `INF-17` | `SVC-13` to Kellan Rise | supplies-connectivity | brief | Via `INF-14` carriage (`DEP-08`). |
| `DEP-16` | `INF-01` ↔ `INF-02` | patient referral | referral | inferred (`ASM-17`) | Plausible; not brief-stated. |
| `DEP-17` | `INF-22` | `SVC-06` | delivers | brief | |
| `DEP-18` | `SVC-15` | `POP-02` (via non-majority languages) | information-reach | inferred (`ASM-18`) | Channel mapping is `SIL-20`. |
| `DEP-19` | `POP-02` | dormitory operators (not modelled) | institutional-anchor | brief silence | `SIL-21`: operators are unmodelled institutional actors. |
| `DEP-20` | `INF-19` | `POP-05` | communicates-via | brief | Informal VHF pre-disaster. |
| `DEP-21` | `EXT-01` | Laurel Delta local government | receives-request-from | brief | The 10-day plan request. |
| `DEP-22` | `EXT-02` | `INF-11` | owns-restoration-estimate | brief | 3–7 days. |

## 6. EXT-* — External interfaces

| ID | Label | Role | Source | Notes |
|---|---|---|---|---|
| `EXT-01` | Nivaro central government | Plan-recipient, response-authoriser, resource-source | brief:§Current state | Internals not modelled; `ASM-19`: reliability of counterparty presumed. |
| `EXT-02` | Local utility | Power-restoration authority; reports 3–7-day estimate | brief:§Current state | Internals not modelled. |
| `EXT-03` | Highland interior | Reached via Kellan Rise road + `INF-14` | brief:§Territory | Internals not modelled. |

## 7. SIL-* — First-class silences (per D-001)

Unknowns the brief does not resolve, recorded as first-class entries
rather than omitted. Session 002 knows which risks it is reasoning
about with partial information.

| ID | Silence | Affected `POP-*` / `INF-*` / `SVC-*` | Notes |
|---|---|---|---|
| `SIL-01` | Outer-islet fishing community count | `POP-05` | Brief describes topology (VHF, islets) but not size. |
| `SIL-02` | Aged-care cluster A+B resident counts | `POP-08`, `INF-12`, `INF-13` | Two clusters named; resident counts not stated. |
| `SIL-03` | Neonatal unit occupancy | `POP-11`, `SVC-09` | Unit exists; occupancy not stated. |
| `SIL-04` | Pregnancy / early-infant populations outside neonatal unit | — | Not mentioned; likely present in 200K pop. |
| `SIL-05` | Mental-health / substance-dependence continuity cohorts | — | Not mentioned. |
| `SIL-06` | Children under 5 | — | Not mentioned as distinct cohort. |
| `SIL-07` | Disability cohorts beyond powered-equipment users | — | Not mentioned. |
| `SIL-08` | Undocumented-persons cohort | — | Not mentioned; migrant-worker cohort `POP-02` is brief-stated, but undocumented status is not. |
| `SIL-09` | Generator fuel status at `INF-01` | `INF-30`, `INF-32` | Leading concern; not stated. |
| `SIL-10` | T0 state of South Latch primary-care clinic | `INF-03`, `SVC-02` | Not stated. |
| `SIL-11` | Flood status of aged-care clusters | `INF-12`, `INF-13` | Institutional anchors possibly compromised. |
| `SIL-12` | Which 2 of 4 substations are degraded | `INF-07` through `INF-10` | Distribution matters for repair sequencing. |
| `SIL-13` | Other generators across district | `INF-31` | Brief does not enumerate. |
| `SIL-14` | Settlement hosting airport runway | `INF-20` | Brief says "air access degraded" but not where. |
| `SIL-15` | State of the South Latch levee | `INF-21` | "Levee-dependent" stated; levee condition not. |
| `SIL-16` | Degree of cellular degradation | `INF-18` | Implied but not quantified. |
| `SIL-17` | Shelter operators, locations, specific capacities | `INF-22`, `SVC-06` | "Capacity strained" stated; internals not. |
| `SIL-18` | Generator fuel supply chain actors, routes, cadences | `INF-32` | Not enumerated. |
| `SIL-19` | Informal care-circle topology for non-institutional `POP-07` | `SVC-10` | 01B's load-bearing silence — "the neighbour who usually brings Mrs K her groceries". |
| `SIL-20` | Language-channel coverage for `POP-02` migrant-worker cohort | `SVC-15`, `DEP-18` | Two non-majority languages noted; channels reaching them T0 not stated. |
| `SIL-21` | Dormitory operators / labour contractors as institutional information holders | `POP-02`, `DEP-19` | Unmodelled actor category. |
| `SIL-22` | Mortuary capacity / mass-casualty handling | — | Brief silent on fatalities. |
| `SIL-23` | Governance legitimacy (language-minority representation, migrant-worker legal status, central-government counterparty reliability) | `EXT-01` | Political layer present in brief only as background. |
| `SIL-24` | Home-dialysis / private-clinic / cross-district dialysis patients outside `POP-09` + `POP-10` | `SVC-03` | 1,420 may not be all dialysis patients. |

## 8. Out of scope for v1

Elements intentionally not modelled in v1, with rationale:

- **Economic flows, commodity pricing, upstream supply chains.** No
  T0 data in brief; inventing values creates false precision.
- **Organisational chart / command structure.** v1 does not model
  "who reports to whom". Response plan (Session 002) may need to.
- **Risk scores, likelihood/impact ratings, prioritisation.** Session
  002's risk register is the natural location.
- **Response actions / task allocation.** Session 002's response
  plan.
- **Time-evolution beyond T0.** v1 is a snapshot. Trajectories belong
  in the risk register.
- **Scenario branches ("if levee fails", "if bridge fails").** Risk-
  register work.
- **Detailed patient-level or household-level records.** Model
  aggregates at cohort level, not individual level.
- **Pre-disaster baseline metrics beyond what the brief provides.**
  Do not backfill from imagined normals.
- **Weather forecast / secondary-event modelling.** Defer to risk
  register.
- **Specific numeric values for time-to-harm clocks.** v1 carries
  qualitative `window` labels with source tags only.

## 9. Hand-off to Session 002

This model carries stable IDs for every entry. The assumption ledger
(`assumption-ledger.md`) cross-references every non-brief-quoted
claim. Every `POP-*`, `INF-*`, `SVC-*`, `DEP-*`, `EXT-*`, `SIL-*`
ID is available for Session 002 to cite in risk entries and response
actions.

**Unresolved / inherited-open items for Session 002 per D-009 /
decisions-not-taken:**

- Prioritisation among cohorts (v1 does not rank).
- Definition of "stabilised" at T0+10d.
- Whether `POP-05` outer-islets is a first-class settlement.
- Treatment of `EXT-01` central-government counterparty's reliability.
- All `SIL-*` entries remain open.
- All sub-cohort counts for `POP-12` through `POP-15` remain
  `unknown`.
