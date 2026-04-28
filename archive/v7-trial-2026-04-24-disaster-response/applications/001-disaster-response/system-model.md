---
title: Laurel Delta system model — v2 (multi-view)
originating_session: 001
artefact_kind: system-model
domain: disaster-response
engine_version: engine-v7
validation: workspace-only
version: 2
status: current
supersedes: system-model-v1.md
created: 2026-04-24
last-revised-session: 003
---

# Laurel Delta system model — v2

This is a multi-view revision of the Laurel Delta system model at
**T0** (~36h post-cyclone-landfall). v2 supersedes v1 per Session
003 D-021 + D-025; v1 is preserved verbatim at `system-model-v1.md`
with `status: superseded`. The supersession was authorised by the
activation of Session 001 §5.1 first-class minority at Session 002
close (23 re-derivation instances across 5 perspectives; D-019).

**Reading guide.** The document has seven sections. §1 is the
canonical ID registry — the ID-of-record for every `POP-*`,
`INF-*`, `SVC-*`, `DEP-*`, `EXT-*`, `SIL-*` entry. §2–§4 are three
views that project the registry along the axes Session 002
repeatedly re-derived. §5 is a mechanical coverage-audit block.
§6 forwards v1.1 implications to Session 004+. §7 records honest
limits and the anti-laundering discipline.

**ID discipline (per Session 003 D-022).** v1 IDs remain canonical.
Views cite existing IDs; no view-scoped derived IDs are minted.
Composite references like `[SVC-03 × POP-09]` or chain-walks
`SVC-03 ⇐ INF-04 ⇐ INF-30 ⇐ INF-32` are reading conveniences, not
IDs. Only registry IDs are citable from `risk-register.md` or
`response-plan.md`.

**Anti-laundering (per Session 003 D-021 §7 + Q7 synthesis).** The
"views" pattern used in this document is acknowledged as Zachman-
adjacent enterprise-architecture pattern, adopted-with-reason
shallowly. See §7 for the 4-of-4 surveyed-and-declined frames
(UN/IASC, lifelines, ICS/NIMS, DoDAF/ArchiMate/causal-loop) and
the load-bearing test for any future view addition: *"which
Session 002+ re-derivation instance is this view closing?"*

---

## §1. Canonical ID registry

The registry is the ID-of-record. Every view in §2–§4 cites from
here. v1's six-section form (`POP-*` / `INF-*` / `SVC-*` / `DEP-*`
/ `EXT-*` / `SIL-*` subsections) is preserved verbatim at
`system-model-v1.md` (superseded); §1 of v2 is a distilled registry
with each row at one line + key attributes inline.

**v1 → v2 reconciliation.** No v1 ID is added, removed, or renamed.
Attribute enrichments this session (per D-024 `POP-12` subrow-
treatment): none change IDs; the sub-structure is exposed in §3
V-Cohort, not in §1. `ASM-19` split per D-023 is recorded in the
**assumption ledger**, not in this system-model; §4 V-External
exposes the `ASM-19a` / `ASM-19b` reference structure here.

### §1.1 Populations (`POP-*`)

| ID | Count | Settlement | Key attribute | Time-to-harm cohort? |
|---|---|---|---|---|
| `POP-01` | ~62,000 | Merrow Port | Total; includes `POP-02` per `ASM-01` | no |
| `POP-02` | ~9,000 (T0 unknown per `ASM-02`) | Merrow Port | Migrant-worker dormitory; 2 non-majority languages (`GIV-04`) | silence-cohort |
| `POP-03` | ~58,000 | South Latch | Total; dispersed smallholdings + 2 aged-care clusters | no |
| `POP-04` | ~80,000 | Kellan Rise | Total; mixed urban-residential | no |
| `POP-05` | unknown (`SIL-01`) | outer-islets | Fishing community; informal VHF pre-disaster (`GIV-05`) | silence-cohort |
| `POP-06` | ~18,000 | district-wide | Displaced T0+36h; dynamic (`ASM-03`) | no |
| `POP-07` | ~18,000 | district-wide | Aged 70+; majority not institutional (`ASM-04`) | no |
| `POP-08` | unknown (`SIL-02`) | South Latch | Institutionally housed aged; `INF-12`+`INF-13` | **yes** (1-3 days) |
| `POP-09` | ~1,200 | South Latch | Dialysis-centre patients; driver: dialysis interval (`ASM-20`) | **yes** (1-3 days) |
| `POP-10` | ~220 | Merrow Port | Regional dialysis patients; non-overlap with `POP-09` per `ASM-05` | **yes** (1-3 days; invertible to hours per `SIL-09`) |
| `POP-11` | unknown (`SIL-03`) | Merrow Port | Neonatal unit occupants; driver: life support (`ASM-20`) | **yes** (hours) |
| `POP-12` | unknown (`ASM-06`) | district-wide | CPAP / home-oxygen dependents; sub-structure exposed in §3 per D-024 | **yes** (hours oxygen / 1-3 days CPAP, state-descriptor per D-024 + `ASM-20`) |
| `POP-13` | unknown (`ASM-06`) | district-wide | Insulin-dependent; cold-chain dependent | **yes** (1-3 days; driver: cold-chain + resupply, `ASM-20`) |
| `POP-14` | unknown (`ASM-06`) | district-wide | Refrigerated-biologic-dependent (e.g., cancer therapies) | **yes** (3-7 days; cliff-edged per `[01C, Session 002 Q2]`) |
| `POP-15` | unknown (`ASM-06`) | district-wide | Other refrigerated-med dependents; residual after `POP-13`+`POP-14` | **yes** (window-unknown) |
| `POP-5K-parent` | ~5,000 | district-wide | Powered-medical-equipment parent aggregate; `POP-12`–`POP-15` are sub-cohorts | — (parent) |
| `POP-16` | unknown subset of `POP-03` | South Latch | Dispersed smallholding residents; flood-access-constrained (`DEP-05`) | no |
| `POP-17` | ~27,000 | Merrow Port | Residents not on `INF-06` backup-well rotation; arithmetic per `ASM-07` | no (but 1-3 days water-supply band — see `RSK-011`) |

### §1.2 Infrastructure (`INF-*`)

Each row records T0 status with explicit `epistemic source` (brief-
stated vs brief-silence vs inferred per 01C Session 001 T0-is-
reported-not-physical principle).

| ID | Label | Settlement | T0 status | Source |
|---|---|---|---|---|
| `INF-01` | Merrow Port regional hospital (~450 beds incl. neonatal) | Merrow Port | on generator | brief-stated |
| `INF-02` | Kellan Rise secondary hospital (~280 beds) | Kellan Rise | unaffected | brief-stated |
| `INF-03` | South Latch primary-care clinic | South Latch | unknown (`SIL-10`) | brief enumeration only |
| `INF-04` | South Latch dialysis centre | South Latch | inaccessible | brief-stated |
| `INF-05` | Merrow Port drinking-water treatment plant | Merrow Port | salt-intruded; decontamination assessment underway | brief-stated |
| `INF-06` | Backup wells | Merrow Port | operational; ~35K rotation | brief-stated (potability = `ASM-08`) |
| `INF-07`–`INF-10` | Coastal substations A-D | Merrow Port area | 2-of-4 degraded (which: `SIL-12`); 2-of-4 operational (`ASM-09`) | brief-stated |
| `INF-11` | Grid coverage (Merrow Port + South Latch) | Merrow Port, South Latch | out; 3-7 day restoration per utility (`ASM-10`) | brief-stated |
| `INF-12` | South Latch aged-care cluster A | South Latch | unknown (`SIL-11`) | brief enumeration |
| `INF-13` | South Latch aged-care cluster B | South Latch | unknown (`SIL-11`) | brief enumeration |
| `INF-14` | Freight rail bridge | Merrow Port — interior | damaged but passable; carries `INF-17` | brief-stated |
| `INF-15` | Highway bridge into Merrow Port | Merrow Port | intact; 24-tonne (`CON-04`; persistence `ASM-11`) | brief-stated |
| `INF-16` | Sea access | Merrow Port | degraded, salvage-required | brief-stated |
| `INF-17` | Fibre-optic trunk to Kellan Rise | carried by `INF-14` | service state unknown; `ASM-12` couples to `INF-14` | brief-silence (operational state) |
| `INF-18` | Cellular coverage | district-wide | impaired (inferred from `INF-11`); `SIL-16` | inferred |
| `INF-19` | VHF networks (outer islets) | outer-islets | post-surge operability unknown (`ASM-13`) | brief-silence (post-surge) |
| `INF-20` | Air access (runway) | settlement unknown (`SIL-14`) | degraded, runway debris | brief-stated |
| `INF-21` | Levee (South Latch) | South Latch | T0 state unstated (`SIL-15`) | brief-silence |
| `INF-22` | Shelter stock | district-wide | capacity strained; operators/locations/capacities unknown (`SIL-17`) | brief-stated |
| `INF-30` | Regional hospital generator | Merrow Port | operational T0; fuel buffer unknown (`SIL-09`) | inferred from `INF-01` state |
| `INF-31` | Other generators | district-wide | unknown (`SIL-13`) | brief-silence |
| `INF-32` | Generator fuel supply chain | district-wide | unenumerated (`SIL-18`); actors/routes/cadences unknown | brief-silence |

### §1.3 Services (`SVC-*`)

| ID | Label | Delivering `INF-*` | Consuming `POP-*` | T0 continuity |
|---|---|---|---|---|
| `SVC-01` | Acute hospital care | `INF-01` (on generator), `INF-02` | all settlements | degraded in Merrow Port |
| `SVC-02` | Primary care | `INF-03` | `POP-03` | unknown (`SIL-10`) |
| `SVC-03` | Haemodialysis | `INF-04` (inaccessible), `INF-01` (overflow for `POP-10`) | `POP-09`, `POP-10` | partial |
| `SVC-04` | Potable water | `INF-05` (failed), `INF-06` (partial, ~35K) | `POP-17` gap, `POP-02` inclusion uncertain | partial (~27K gap per `ASM-07`) |
| `SVC-05` | Electrical supply | `INF-07`–`INF-11` + `INF-30`/`INF-31` | all settlement populations | out in Merrow Port + South Latch |
| `SVC-06` | Shelter | `INF-22` | `POP-06` | strained |
| `SVC-07` | Inter-settlement road transport | `INF-14`, `INF-15` | district-wide | degraded |
| `SVC-08` | Cold chain (refrigerated medication) | `INF-11` + on-site refrigeration (not enumerated) | `POP-13`, `POP-14`, `POP-15` | at-risk (power-dependent per `ASM-16`) |
| `SVC-09` | Neonatal care | `INF-01` | `POP-11` | on-generator-dependent |
| `SVC-10` | Aged-care continuity | `INF-12`, `INF-13` + informal care circles (`SIL-19`) | `POP-08`, `POP-07` | unknown |
| `SVC-11` | Sea transport | `INF-16` | outer-islets, supply logistics | degraded; salvage-first |
| `SVC-12` | Air transport | `INF-20` | district-wide external | degraded |
| `SVC-13` | Telecommunications | `INF-17`, `INF-18`, `INF-19` | all settlement populations; `POP-05` via `INF-19` only | degraded / unknown |
| `SVC-14` | Salvage (sea-access prerequisite) | to be resourced | prerequisite for `SVC-11` | not-yet-active |
| `SVC-15` | Public information / risk communication | `INF-17`, `INF-18`, possibly `INF-19` | district-wide; `POP-02` requires non-majority-language channels (`ASM-18`, `SIL-20`) | unknown coverage |

### §1.4 Dependencies (`DEP-*`)

Typed edges. Relationship types: `supplies`, `powers / enables`,
`routes`, `carries (co-located / shared-fate)`, `service-blocked-
by-infrastructure`, `delivers`, `backs-up (generator → hospital)`,
`conditional-habitability`, `communicates-via`, `receives-request-
from`, `owns-restoration-estimate`, `information-reach`,
`institutional-anchor`. Full enumeration preserved in v1 `§5.
DEP-*`; v2 §2 V-Chain exposes the dependency chains this registry
supports. Every `DEP-*` ID remains canonical; see `system-model-
v1.md` §5 for the row-by-row typed-edge table.

Summary (for citation convenience):

| ID | From → To | Type |
|---|---|---|
| `DEP-01` | `INF-11` → `SVC-05` | supplies |
| `DEP-02` | `SVC-05` → `POP-5K-parent` + `POP-12`..`POP-15` | powers / enables (inferred `ASM-14`) |
| `DEP-03` | `INF-05` → `SVC-04` baseline | supplies (currently failed) |
| `DEP-04` | `INF-06` → `SVC-04` backup | supplies (~35K rotation) |
| `DEP-05` | flooded areas → physical access | constrains |
| `DEP-06` | `INF-15` (24-t) → `SVC-07` | routes |
| `DEP-07` | `INF-14` → `SVC-07` | routes (damaged-passable) |
| `DEP-08` | `INF-14` → `INF-17` | carries (shared-fate) |
| `DEP-09` | `INF-04` inaccessible → `POP-09` gap | service-blocked-by-infrastructure |
| `DEP-10` | `INF-01` → `SVC-09` | delivers |
| `DEP-11` | `INF-30` → `INF-01` | backs-up |
| `DEP-12` | `INF-32` → `INF-30` | supplies fuel (`ASM-15`) |
| `DEP-13` | `SVC-05` → `SVC-08` | powers / enables (`ASM-16`) |
| `DEP-14` | `INF-21` levee → `POP-03` | conditional-habitability |
| `DEP-15` | `INF-17` → `SVC-13` Kellan Rise | supplies-connectivity |
| `DEP-16` | `INF-01` ↔ `INF-02` | referral (`ASM-17`) |
| `DEP-17` | `INF-22` → `SVC-06` | delivers |
| `DEP-18` | `SVC-15` → `POP-02` | information-reach (`ASM-18`) |
| `DEP-19` | `POP-02` → dormitory operators | institutional-anchor (`SIL-21`) |
| `DEP-20` | `INF-19` → `POP-05` | communicates-via |
| `DEP-21` | `EXT-01` → Laurel Delta local government | receives-request-from |
| `DEP-22` | `EXT-02` → `INF-11` | owns-restoration-estimate |

### §1.5 External interfaces (`EXT-*`)

| ID | Label | Role | Reliability attributes |
|---|---|---|---|
| `EXT-01` | Nivaro central government | Plan-recipient + response-authoriser + resource-source | recipient per `ASM-19a` + delivery per `ASM-19b` (see §4) |
| `EXT-02` | Local utility | Power-restoration authority | reports 3–7-day estimate per `ASM-10` |
| `EXT-03` | Highland interior | Reached via Kellan Rise + `INF-14` | not modelled internally |

### §1.6 First-class silences (`SIL-*`)

Silences remain first-class entries per Session 001 D-001. v2
distributes silence citations inline in §3 V-Cohort (for cohort-
shaped silences) and §2 V-Chain (for infrastructure/service
silences) per 01B + 01C discipline — silences co-locate with what
they silence. This registry table is the recoverable flat list
per 01B's list-shape concern ([`01B`, Q5]); the list-shape
information (24 silences clustering around medical-fragility and
care-topology cohorts) is preserved here and in v1 `§7 SIL-*`.

| ID | Silence | Touches |
|---|---|---|
| `SIL-01` | Outer-islet fishing community count | `POP-05` |
| `SIL-02` | Aged-care cluster A+B resident counts | `POP-08`, `INF-12`, `INF-13` |
| `SIL-03` | Neonatal unit occupancy | `POP-11`, `SVC-09` |
| `SIL-04` | Pregnancy / early-infant populations outside neonatal unit | — |
| `SIL-05` | Mental-health / substance-dependence continuity cohorts | — |
| `SIL-06` | Children under 5 as distinct cohort | — |
| `SIL-07` | Disability cohorts beyond powered-equipment users | — |
| `SIL-08` | Undocumented-persons cohort | — |
| `SIL-09` | Generator fuel status at `INF-01` | `INF-30`, `INF-32` |
| `SIL-10` | T0 state of South Latch primary-care clinic | `INF-03`, `SVC-02` |
| `SIL-11` | Flood status of aged-care clusters | `INF-12`, `INF-13` |
| `SIL-12` | Which 2 of 4 substations are degraded | `INF-07`–`INF-10` |
| `SIL-13` | Other generators across district | `INF-31` |
| `SIL-14` | Settlement hosting airport runway | `INF-20` |
| `SIL-15` | State of the South Latch levee | `INF-21` |
| `SIL-16` | Degree of cellular degradation | `INF-18` |
| `SIL-17` | Shelter operators, locations, specific capacities | `INF-22`, `SVC-06` |
| `SIL-18` | Generator fuel supply chain actors, routes, cadences | `INF-32` |
| `SIL-19` | Informal care-circle topology for non-institutional `POP-07` | `SVC-10` |
| `SIL-20` | Language-channel coverage for `POP-02` | `SVC-15`, `DEP-18` |
| `SIL-21` | Dormitory operators / labour contractors | `POP-02`, `DEP-19` |
| `SIL-22` | Mortuary capacity / mass-casualty handling | — |
| `SIL-23` | Governance legitimacy (language-minority representation, migrant legal status, `EXT-01` reliability) | `EXT-01` |
| `SIL-24` | Home / private / cross-district dialysis patients outside `POP-09`+`POP-10` | `SVC-03` |

---

## §2. V-Chain — per-service dependency view

Each `SVC-*` gets a block showing its upstream infrastructure /
service / external / assumption dependencies and the cohort reach
downstream, with time-to-harm at the weakest cohort annotated.
Session 002's 23 re-derivation instances concentrated on chains of
this shape; §2 closes them natively.

Convention: chain-walk notation `A ⇐ B` reads "A is supplied by B"
(so `SVC-03 ⇐ INF-04` reads "dialysis service is supplied by
dialysis centre infrastructure"). Downstream cohort reach in `→`
notation. Silences inline in `[SIL-*]` brackets; assumptions inline
in `{ASM-*}` braces; external couplings in `<EXT-*>` angle brackets.

### §2.1 `SVC-03` — Haemodialysis

- **Upstream:** `INF-04` (South Latch centre; inaccessible) ⇐
  `DEP-05` (flood access) / `DEP-09` (infrastructure-blocks-
  service). Alt path: `INF-01` Merrow Port regional ⇐ `DEP-11`
  (`INF-30` generator) ⇐ `DEP-12` (`INF-32` fuel) ⇐ `{ASM-15}` +
  `[SIL-09]` + `[SIL-18]`.
- **Cross-coupling:** `INF-02` Kellan Rise referral via `DEP-16`
  (`{ASM-17}`) routed on `SVC-07` / `DEP-06` (`INF-15`) /
  `DEP-07` (`INF-14`).
- **Downstream cohort reach:** → `POP-09` (~1,200, 1-3 days) →
  `POP-10` (~220, 1-3 days, invertible to hours per `[SIL-09]`).
- **Weakest cohort time-to-harm:** 1-3 days qualitative (hours if
  `INF-30` fuel exhausts and `{ASM-15}` cannot replenish).
- **Silences touched:** `[SIL-09]`, `[SIL-18]`, `[SIL-24]` (home/
  private dialysis patients outside `POP-09`+`POP-10`).
- **External:** `<EXT-01>` for any medevac / mobile-dialysis
  escalation; reliability per `ASM-19b`.

### §2.2 `SVC-08` — Cold chain

- **Upstream:** `SVC-05` ⇐ `INF-11` (grid out) OR `INF-31` (on-
  site generators; `[SIL-13]`) ⇐ `{ASM-16}` (`SVC-08` depends on
  `SVC-05`). Fallback: `INF-30` (hospital generator backfill, via
  `[SIL-09]`).
- **Downstream cohort reach:** → `POP-13` (insulin, 1-3 days,
  `{ASM-20}` qualitative) → `POP-14` (biologic, 3-7 days, cliff-
  edged) → `POP-15` (residual, window-unknown).
- **Weakest cohort time-to-harm:** 1-3 days.
- **Silences touched:** `[SIL-07]` (disability cohorts beyond
  powered-equipment users), `[SIL-13]`, `[SIL-18]`.
- **External:** `<EXT-01>` for air-lift cold-chain escalation;
  reliability per `ASM-19b`.

### §2.3 `SVC-09` — Neonatal care

- **Upstream:** `INF-01` ⇐ `DEP-10` (delivers) ⇐ `DEP-11`
  (`INF-30`) ⇐ `DEP-12` (`INF-32`) ⇐ `{ASM-15}` + `[SIL-09]` +
  `[SIL-18]`.
- **Downstream cohort reach:** → `POP-11` (count `[SIL-03]`,
  hours-band, driver: life support per `{ASM-20}`).
- **Weakest cohort time-to-harm:** hours.
- **Silences touched:** `[SIL-03]`, `[SIL-09]`, `[SIL-18]`,
  `[SIL-04]` (pregnancy / early-infant outside neonatal unit).
- **Referral fallback:** `INF-02` Kellan Rise via `DEP-16` +
  `SVC-07`/`INF-15`.

### §2.4 `SVC-01` — Acute hospital care

- **Upstream (Merrow Port):** `INF-01` ⇐ `INF-30` ⇐ `INF-32` ⇐
  `{ASM-15}`+`[SIL-09]`+`[SIL-18]`. Cold-chain and neonatal co-
  located at `INF-01` (shared fate on `INF-30` exhaustion).
- **Upstream (Kellan Rise):** `INF-02` unaffected.
- **Downstream cohort reach:** all settlement populations; acute-
  surge via `DEP-16` `{ASM-17}` referral; hours-band for critically
  ill any cohort.
- **Weakest cohort time-to-harm:** hours (for any patient in
  `INF-01` at T0).
- **Silences touched:** `[SIL-09]`, `[SIL-18]`.

### §2.5 `SVC-04` — Potable water

- **Upstream:** `INF-05` (failed, salt-intruded) ⇐ `DEP-03`.
  Backup: `INF-06` (wells serving ~35K) ⇐ `DEP-04` ⇐ `{ASM-08}`
  (potability untested).
- **Downstream cohort reach:** → `POP-17` (~27K gap per `{ASM-07}`
  arithmetic) → `POP-02` (inclusion in 35K uncertain).
- **Weakest cohort time-to-harm:** 1-3 days (WHO-comparable
  qualitative band, per `{ASM-20}` no-pretrained-numbers).
- **Silences touched:** (decontamination timeline silence; not
  registered as discrete `SIL-*` per v1 but explicit in §6 forward-
  list for Session 004+).

### §2.6 `SVC-05` — Electrical supply

- **Upstream:** `INF-07`–`INF-10` (2-of-4 degraded per `[SIL-12]`;
  `{ASM-09}`) ⇐ `INF-11` ⇐ `<EXT-02>` utility (`ASM-10` 3-7d
  estimate) ⇐ `DEP-22`.
- **Downstream cohort reach (direct):** all settlement populations.
  **Indirect via `DEP-02`:** `POP-5K-parent` + `POP-12`..`POP-15`
  (`{ASM-14}` powered-medical coupling).
- **Weakest cohort time-to-harm (indirect):** hours (oxygen subset
  of `POP-12`; see §3).
- **Silences touched:** `[SIL-12]`, `[SIL-13]`.

### §2.7 `SVC-07` — Inter-settlement road transport

- **Upstream:** `INF-15` (24-t, `{CON-04}`, persistence `{ASM-11}`)
  ⇐ `DEP-06`; `INF-14` (damaged-passable) ⇐ `DEP-07`.
- **Downstream cohort reach (enabling):** every referral path
  (`DEP-16` `ASM-17`); supply delivery to every cohort.
- **Silences touched:** none specific; `{ASM-11}` persistence is
  the structural assumption.

### §2.8 `SVC-13` — Telecommunications

- **Upstream:** `INF-17` (fibre, carried by `INF-14` per `DEP-08`
  shared-fate; service state unknown per `{ASM-12}`) ⇐ `DEP-15`
  to Kellan Rise. `INF-18` (cellular; impaired per `[SIL-16]`).
  `INF-19` (VHF outer islets; post-surge state `[ASM-13]`).
- **Downstream cohort reach:** all settlement populations; `POP-05`
  via `INF-19` only (`DEP-20` `communicates-via`).
- **Weakest cohort time-to-harm:** window-unknown; compound-harm
  for `POP-02` (info-starvation per `{ASM-18}`).
- **Silences touched:** `[SIL-16]`, `[SIL-20]`.
- **Shared-fate cascade (critical):** if `INF-14` further degrades,
  `INF-17` fails with it; Kellan Rise `SVC-13` loss then degrades
  `DEP-16` inter-hospital referral per `{ASM-17}`, which touches
  `SVC-03` / `SVC-09` / `SVC-01`.

### §2.9 `SVC-06` — Shelter

- **Upstream:** `INF-22` (strained) ⇐ `DEP-17`.
- **Downstream cohort reach:** `POP-06` (~18K, `{ASM-03}`
  baseline).
- **Weakest cohort time-to-harm:** 3-7 days (compound if
  unresolved).
- **Silences touched:** `[SIL-17]` (operators, locations,
  capacities).

### §2.10 `SVC-10` — Aged-care continuity

- **Upstream (institutional):** `INF-12`+`INF-13` (flood state
  `[SIL-11]`; occupancy `[SIL-02]`).
- **Upstream (informal):** care circles per `[SIL-19]` (unmapped
  topology; 01B's load-bearing silence).
- **Downstream cohort reach:** `POP-08` (institutional, `[SIL-02]`
  count); `POP-07` (non-institutional via informal care circles).
- **Weakest cohort time-to-harm:** 1-3 days; accelerates under
  concurrent `SVC-04` + `SVC-05` + `SVC-08` outages.
- **Silences touched:** `[SIL-02]`, `[SIL-11]`, `[SIL-19]`.

### §2.11 `SVC-11` / `SVC-12` / `SVC-14` — Sea / air / salvage

- **Upstream:** `INF-16` sea (degraded, `SVC-14` prerequisite);
  `INF-20` air (runway debris, `[SIL-14]` settlement).
- **Downstream cohort reach:** `POP-05` outer-islets (access-
  modality); district-wide logistics.
- **Silences touched:** `[SIL-14]`.
- **External:** `<EXT-01>` for salvage coordination / air
  reconnaissance fallback.

### §2.12 `SVC-15` — Public information / risk communication

- **Upstream:** `INF-17`, `INF-18`, possibly `INF-19` (for `POP-05`
  reachability). Language-channel coverage for `POP-02` per
  `{ASM-18}` + `[SIL-20]`; `[SIL-21]` dormitory-operator identity.
- **Downstream cohort reach:** district-wide; `POP-02` subject to
  non-majority-language channel gap.
- **Weakest cohort time-to-harm:** compound over 10-day horizon
  (info-starvation); no acute hours-band.
- **Silences touched:** `[SIL-20]`, `[SIL-21]`.

### §2.13 `SVC-02` — Primary care

- **Upstream:** `INF-03` (`[SIL-10]` T0 state unknown).
- **Downstream cohort reach:** `POP-03` South Latch.
- **Silences touched:** `[SIL-10]`.

---

## §3. V-Cohort — cohort × service view

Rows are `POP-*` (and cohort-shaped silence entries that mask
invisible populations). Columns are the load-bearing consumed
services. Cells hold `DEP-*` + `ASM-*` + `SIL-*` citations with
time-to-harm per cell. `POP-12` is exposed with oxygen-dependent
and CPAP-dependent subrows per D-024 (not canonical split; each
subrow tagged `{ASM-20}` state-descriptor).

Top-tier individuated medical-fragility cohorts appear first. Table
structure reads: `POP-* | SVC-03 dial | SVC-08 cold | SVC-09 neo |
SVC-05 power | SVC-04 water | SVC-10 aged-care | SVC-06 shelter |
SVC-13 telecom | SVC-15 info | time-to-harm band`.

### §3.1 Medical-fragility cohorts (Tier 1, per risk-register D-012)

| Cohort | SVC-03 dial | SVC-08 cold | SVC-09 neo | SVC-05 power | SVC-04 water | SVC-10 aged | SVC-06 shelter | SVC-13 tele | SVC-15 info | Time-to-harm |
|---|---|---|---|---|---|---|---|---|---|---|
| `POP-08` institutional-aged (South Latch) | — | (medication) | — | hospital-dependent / `INF-31` | baseline | `DEP-17`/`SIL-11` | no | `SVC-10` dep | reachable via staff | 1-3 days |
| `POP-09` South Latch dialysis | `DEP-09` `INF-04` / `ASM-17` `INF-02` | — | — | baseline | baseline | — | — | baseline | baseline | 1-3 days |
| `POP-10` Merrow Port regional dialysis | `INF-01` via `DEP-11`+`DEP-12` | — | — | `INF-30` fuel-dep `{ASM-15}` | baseline | — | — | baseline | baseline | 1-3 days (invertible to hours on `[SIL-09]`) |
| `POP-11` neonatal (`[SIL-03]` count) | — | — | `DEP-10` `INF-01` | `INF-30` fuel-dep | baseline | — | — | baseline (`INF-17` via `[DEP-15]`) | — | **hours** `{ASM-20}` |
| `POP-12` (oxygen subrow, `{ASM-20}` state-descriptor per D-024) | — | — | — | `DEP-02` `INF-11` / `INF-31` | baseline | — | — | baseline | baseline | **hours (state-descriptor; oxygen-dependent subgroup)** |
| `POP-12` (CPAP subrow, `{ASM-20}` state-descriptor per D-024) | — | — | — | `DEP-02` `INF-11` / `INF-31` | baseline | — | — | baseline | baseline | 1-3 days (state-descriptor; CPAP-dependent subgroup) |
| `POP-13` insulin | — | `DEP-13` `SVC-05` → `SVC-08` | — | (via `SVC-08`) | baseline | — | — | baseline | baseline | 1-3 days `{ASM-20}` |
| `POP-14` biologic | — | `DEP-13` (cliff-edged per `[01C, S002 Q2]`) | — | (via `SVC-08`) | baseline | — | — | baseline | baseline | 3-7 days |
| `POP-15` other refrigerated-med | — | `DEP-13` | — | (via `SVC-08`) | baseline | — | — | baseline | baseline | window-unknown `{ASM-20}` |

Count silences for this tier: `POP-08` (`[SIL-02]`), `POP-11`
(`[SIL-03]`), `POP-12`/`POP-13`/`POP-14`/`POP-15` (`{ASM-06}` sub-
distribution of `POP-5K-parent`).

### §3.2 Cohort-silence cohorts (Tier 2)

| Cohort | Key dependencies | Time-to-harm / harm-shape |
|---|---|---|
| `POP-02` migrant-worker dormitory (T0 occupancy `{ASM-02}`) | `SVC-15` via `DEP-18` `{ASM-18}`; `SVC-04` (inclusion in 35K uncertain); `SVC-06` | spans 10-day horizon; compound info-starvation per `[SIL-20]` |
| `POP-05` outer-islets (count `[SIL-01]`) | `SVC-13` via `INF-19` only; `SVC-11` via salvage; `SVC-12` air (degraded); district services accessible only via `SVC-07`/`SVC-11`/`SVC-12` | window-unknown; visibility-failure mode per `[01E, Session 002 Q2]` |

### §3.3 Aggregate populations (Tier 3)

| Cohort | Key dependencies | Time-to-harm |
|---|---|---|
| `POP-03` South Latch | `SVC-04`, `SVC-05`, `SVC-06`, habitability conditional on `INF-21` levee per `DEP-14` `[SIL-15]` | window-unknown (conditional) |
| `POP-04` Kellan Rise | `SVC-01` `INF-02` unaffected | low acute — rear-area; dependencies via `SVC-13` `DEP-15` to Merrow Port |
| `POP-06` displaced | `SVC-06` (strained, `{ASM-03}`); `SVC-04`/`SVC-05` via shelter | 3-7 days |
| `POP-17` water-supply gap | `SVC-04` (not in 35K rotation) | 1-3 days |

### §3.4 Cohort-shaped silences (inline with above, explicit)

Per 01B's load-bearing concern (silences are cohorts too):

- `[SIL-02]` aged-care cluster resident counts — masks `POP-08`
  sizing.
- `[SIL-03]` neonatal unit occupancy — masks `POP-11` sizing; does
  NOT mask existence (`SVC-09` triggered on presence of any neonate
  at `INF-01`).
- `[SIL-19]` informal care-circle topology — masks `POP-07` non-
  institutional support.
- `[SIL-20]` language-channel coverage — masks `POP-02`
  reachability.
- `[SIL-04]`–`[SIL-08]` (pregnancy, mental-health, under-5s,
  disability-not-powered, undocumented) — mask cohorts not
  individuated at v1 because the brief does not enumerate them;
  Session 004+ may lift any of these to first-class `POP-*` if
  evidence surfaces.

---

## §4. V-External — external-actor view

Rows `EXT-*`, with explicit recipient / delivery reliability
columns per D-023 split of `ASM-19`. Cross-reference between
`ASM-19a` and `ASM-19b` is enforced per §5.8 minority (this
session): any artefact that addresses one aspect must explicitly
state its posture toward the other.

| EXT ID | Role | Recipient-reliability basis | Delivery-reliability basis | Fallback-if-fails |
|---|---|---|---|---|
| `EXT-01` Nivaro central government | Plan-recipient, response-authoriser, resource-source (`DEP-21`) | `ASM-19a` (10-day plan has fillable recipient; falsifier: no named recipient / ack channel absent / repeated non-response / broadcast-to-ack round-trip failure; review trigger: T0+24h + on `EXT-01` comms event) | `ASM-19b` (delivery on committed actions; falsifier: ETA slip >25% OR silent cancellation OR actor-side dependency failure OR first attempted delivery regardless of outcome; review trigger: T0+12h + first attempted delivery + every `STR-*` review gate) | internal-execute or `(accepted: wait-and-replan)` per `response-plan.md` §External dependencies summary; paired-posture statement required when addressing either `ASM-19a` or `ASM-19b` alone |
| `EXT-02` Local utility | Power-restoration authority (`DEP-22`) | not applicable (utility is delivery-only; recipient-role held by `EXT-01`) | `ASM-10` (3-7d restoration estimate; falsifier: any revision or non-progress) | `(accepted: wait-and-replan)` per `response-plan.md` `ACT-008` |
| `EXT-03` Highland interior | Reached via Kellan Rise + `INF-14` | not modelled (out-of-scope per brief) | not modelled | via `SVC-07` road-import (for fuel per `ACT-007` fallback path) |

**Silences touched by §4:** `[SIL-23]` governance legitimacy (for
`EXT-01`).

**v1.1 forward (per D-026):** `RSK-019` currently references
`ASM-19` as a single row; post-D-023 split, `RSK-019` is under-
specified and should split into `RSK-019a` / `RSK-019b` OR carry
both premises with paired-row posture per §5.8.

---

## §5. Coverage audit

Per D-022 ID discipline: every registry ID must appear in at least
one view (or be flagged `catalogue-only`); every view row must
resolve to a registry ID. This section is the mechanical drift-
prevention block.

**ID coverage by family:**

- `POP-*`: all 18 entries (`POP-01` through `POP-17` + `POP-5K-
  parent`) appear in §3 V-Cohort (or at least in §3.3 aggregate
  table for non-medical-fragility cohorts). Tier-1 medical-
  fragility cohorts (`POP-08`..`POP-15`) individuated per D-003 +
  D-024 subrow treatment.
- `INF-*`: all 22 entries (`INF-01`–`INF-22`, `INF-30`, `INF-31`,
  `INF-32`) appear in §2 V-Chain upstream enumerations or in §1.2
  registry (`INF-03` `SIL-10`, `INF-18`/`INF-19`/`INF-20`/`INF-21`
  status-unclear entries carried at registry level + cited in §2
  chains that depend on them).
- `SVC-*`: all 15 entries (`SVC-01`–`SVC-15`) receive a §2 V-Chain
  block except `SVC-02` primary care which is noted in §2.13 due
  to `[SIL-10]` status uncertainty.
- `DEP-*`: 22 entries listed in §1.4; each appears in at least one
  §2 chain-walk or §3 dependency cell.
- `EXT-*`: all 3 entries (`EXT-01`/`02`/`03`) appear in §4 V-
  External.
- `SIL-*`: 24 entries listed in §1.6; each appears inline in
  either §2 (infrastructure/service silences) or §3.4 (cohort-
  shaped silences) or §4 (`[SIL-23]` governance). `SIL-04`–
  `SIL-08` (cohorts-unenumerated-at-v1) are catalogue-only at §1.6
  and are flagged for Session 004+ if any cohort is lifted.

**Orphan check:** no view-row cites a non-registry ID. Composite-
reference conveniences (`[SVC-03 × POP-09]`, chain-walks) are
legible as combinations of registry IDs and do not constitute
orphan citations.

**Non-mechanical note:** this audit is a workspace-internal
discipline pending tooling. A future session may implement a
linter check against this §5 (analogous to `tools/validate.sh`
checks but scoped to application artefacts); such tooling would
live outside the engine-definition file set per
`specifications/engine-manifest.md` §3.

---

## §6. v1.1 implications forward-list (for Session 004+)

Per Session 003 D-026, the following v1 risk-register and response-
plan rows are flagged for Session 004+ v1.1 revision
consideration. v2 exposes their thinness; v2 does not fix them
(Session 001 D-009 increment-boundary discipline; revisions are
Session 004+ scope).

| v1 row | Thinness exposed by v2 | Candidate v1.1 direction | Perspective agreement |
|---|---|---|---|
| `RSK-014` (generator-fuel multi-downstream) | `cohort_affected` blank at v1; §2.1/§2.3/§2.4 enumerate cascade to `POP-09` / `POP-10` / `POP-11` / general hospitalised | per-downstream sub-risks OR explicit downstream-cohort list citing §2 chains | 4-of-4 |
| `RSK-019` (`EXT-01` counterparty reliability) | conflates `ASM-19a` + `ASM-19b` post-split | split to `RSK-019a`/`RSK-019b` OR paired-row posture per §5.8 | 4-of-4 |
| `ACT-005` (cold-chain POP-13/14/15) | §2.2 + §3.1 expose differing time-to-harm per sub-cohort | per-cohort sub-actions OR explicit time-to-harm triage within action | 4-of-4 |
| `RSK-015` (freight-rail-bridge + fibre shared-fate) | §2.8 makes shared-fate explicit | citation update likely; full decomposition not required | 3-of-4 |
| `RSK-008` (aged-care cluster welfare) | §2.10 + §3.1 expose multi-service dependency | decompose into per-dependency sub-risks | 3-of-4 |
| `RSK-004` (`POP-12` power dependency; dual window at v1) | §3.1 subrow-treatment per D-024 exposes oxygen/CPAP differentiation via state-descriptors | contingent on §5.5 canonical-split minority activation | 2-of-4 (01A + 01B); not activated this session |

Session 004+ is free to order these revisions, bundle them, or
defer specific items. The flag is the forward-list itself, not a
sequencing commitment.

---

## §7. Honest limits and anti-laundering record

**Anti-laundering record (per D-021 §7 + Q7 synthesis).** The v2
shape uses a "canonical registry + views" pattern acknowledged as
Zachman-adjacent enterprise-architecture pattern, adopted-with-
reason shallowly per 4-perspective Q7 consensus. The warrant for
adoption is the Session 002 §5.1 activation evidence (23 re-
derivation instances), not the Zachman / TOGAF / C4 authorities.

4-of-4 surveyed-and-declined-as-structure this session:

- **UN/IASC cluster catalogue** (`EXT-SURVEY-02`). v2 `SVC-*` chain
  index is not a cluster catalogue and does not rename services
  into external cluster headings.
- **Lifelines / critical-infrastructure-sector taxonomies**
  (`EXT-SURVEY-04`). v2 `INF-*` IDs typed by function-in-scenario,
  not by lifeline sector.
- **ICS/NIMS** (`EXT-SURVEY-01`). v2 has no incident-command or
  section-taxonomy structure.
- **DoDAF / ArchiMate / causal-loop diagrams**. v2 uses plain
  `A ⇐ B` chain notation, not DoDAF boxes, ArchiMate glyphs, or
  feedback-loop diagrams.

New surveyed rows to be added to `assumption-ledger.md`:
`EXT-SURVEY-11` (enterprise-architecture multi-view pattern;
adopt-with-reason shallowly) + `EXT-SURVEY-12` (systems-dependency
modelling frames; surveyed-and-decline).

**Load-bearing test for future view additions (adopted verbatim
from 01C [`01C`, Q7]):** *"for every view the Reviser proposes, ask
'which Session 002+ re-derivation instance is this view closing?'
If the answer is 'completeness' or 'symmetry' or 'it seemed
natural,' it's laundered."* Any Session 004+ proposal of a fourth
or fifth view must survive this test or be rejected. This is the
§5.6 preserved first-class minority (this session).

**`ASM-20` flag preserved across v2:** all time-to-harm bands
remain qualitative `{ASM-20}`-tagged state descriptors; no
pretrained clinical numbers are imported. The `POP-12` subrow-
treatment explicitly records its hours-band / days-band
differentiation as state-descriptor per D-024, not as a clinical
fact.

**Honest limits:**

- **No domain-actor; no reference case.** Validation is
  `workspace-only` per Session 001 DEC-07 + Session 002 D-020 +
  Session 003 D-028. v2 is coherent, cohort-individuating, and
  anti-laundering; v2 is not correctness-validated against any
  real-world system.
- **v2 is a shape revision, not a completeness revision.** All 24
  `SIL-*` silences carried from v1 remain open; v2 makes them more
  visible (inline co-location) but does not close any.
- **`POP-12` canonical split deferred.** Per D-024, the hours/days
  differentiation exposed in §3.1 is state-descriptor, not
  canonical cohort split. §5.5 preserved minority (01A + 01B) may
  activate if count-closure evidence arrives OR subrow-treatment
  proves unworkable in Session 004+.
- **Settlement-local topology not exposed as a view.** D-006
  (settlement-as-attribute) not reversed. Settlement appears at
  registry level only. Session 002 re-derivation evidence did not
  concentrate on settlement-level reasoning; if Session 004+
  evidence concentrates there, settlement-local could be promoted
  (would require a Session 004+ decision with warrant).
- **Downstream `risk-register.md` and `response-plan.md` remain at
  v1.** v2 exposes their thinness per §6; v2 does not fix them.
  Session 004+ is expected to produce v1.1 revisions of the named
  rows.
- **§5.1 activation is discharged by this adoption.** The Session
  001 Adversarial Skeptic multi-view minority has been activated
  (Session 002) and executed (Session 003). Its minority text
  remains preserved at `[archive: provenance/001-session/
  01-deliberation.md]` §5.1 for provenance continuity. Four new
  minorities preserved this session (§5.5 `POP-12` canonical
  split; §5.6 view-catalogue-inflation watchpoint; §5.7
  supplementary derivation-index alternative; §5.8 `ASM-19`
  cross-reference discipline) are logged in `[archive:
  provenance/003-session/01-deliberation.md]` §3.
- **Cross-family signal.** Four-perspective deliberation with one
  non-Claude Outsider (same `codex exec` transport as Sessions
  001 + 002). MAD v4 §Limitations applies: single non-Claude
  participant narrows OI-004 less than its presence suggests; no
  OI-004 narrowing claim made (external-problem workspace, OI-004
  tracked in source workspace).
