---
title: Laurel Delta risk register — v1
originating_session: 002
artefact_kind: risk-register
domain: disaster-response
engine_version: engine-v7
validation: workspace-only
status: v1
created: 2026-04-24
last-revised-session: 002
---

# Laurel Delta risk register — v1

This register enumerates the risks Laurel Delta faces at T0+36h under
the 10-day response-and-stabilisation horizon (`GIV-01`). It is keyed
to the v1 system model (`system-model.md`) and v1 assumption ledger
(`assumption-ledger.md`), both produced Session 001. Schema per
Session 002 D-011. Prioritisation per D-012 (two-axis partial order,
cohort fragility × dependency depth, both kept visible). Frontmatter
`validation: workspace-only` per D-020.

**What this register does.** For each identified risk, it records the
cohort / infrastructure / service affected, the dependency chain, the
qualitative time-to-harm window, the assumption-ledger premises, the
silence dependencies, the evidence state behind the risk, and the
response-plan actions that address it. The register is a pivot
between `system-model.md` and `response-plan.md`.

**What this register does not do.** It does not assign numeric
likelihood, impact, severity-band scores, or owner fields. A risk-
list reader scanning for `priority: critical` will not find one.
Priority is the shape of the register (tiered cohort-fragility axis
+ dependency-depth axis) rather than a column. See D-011 rationale
and the Adversarial Skeptic raw-output
[`[archive: provenance/002-session/01D-perspective-adversarial-skeptic.md]`,
Q1] for the laundering argument behind this choice.

**§5.1 activation note.** Session 002 activated the §5.1 first-class
minority from Session 001 (single-document model form). Authoring
this register required re-deriving dependencies not cleanly exposed
by the flat model in at least 23 instances across the deliberation
(see D-019). This register is produced on the v1 single-document
model anyway; Session 003 should consider the multi-view revision.

## Summary table (all risks)

Cohort-fragility tiers per D-012:

- **T1** — individuated medical-fragility cohorts (top, unranked).
- **T2** — cohort-silence cohorts.
- **T3** — aggregate populations.
- **T4** — infrastructure-service-only risks without a pinned cohort.

Dependency-depth (shorthand: **Up** = upstream, **Down** = downstream,
**—** = single-edge or cohort-proximate):

| ID | Title | Tier | Time window | Dep-depth | Primary cohort(s) | Linked actions |
|---|---|---|---|---|---|---|
| `RSK-001` | South Latch dialysis gap — centre inaccessible | T1 | 1-3 days | — | `POP-09` | `ACT-003` |
| `RSK-002` | Merrow Port regional dialysis at risk from generator/fuel | T1 | 1-3 days (invertible to hours) | Down | `POP-10` | `ACT-004`, `ACT-007` |
| `RSK-003` | Neonatal care disruption — generator + occupancy silence | T1 | hours | Down | `POP-11` | `ACT-001`, `ACT-007` |
| `RSK-004` | CPAP/home-oxygen cohort power dependency | T1 | hours (oxygen subset), 1-3 days (CPAP subset) | Down | `POP-12` | `ACT-006` |
| `RSK-005` | Insulin cold-chain failure | T1 | 1-3 days | Down | `POP-13` | `ACT-005` |
| `RSK-006` | Refrigerated-biologic cold-chain failure | T1 | 3-7 days | Down | `POP-14` | `ACT-005` |
| `RSK-007` | Other refrigerated-med dependency | T1 | window-unknown | Down | `POP-15` | `ACT-005` |
| `RSK-008` | Aged-care cluster welfare — flood/occupancy silence | T1 | 1-3 days | — | `POP-08` | `ACT-016` |
| `RSK-009` | Outer-islet contact silence (count + access + VHF state) | T2 | window-unknown | — | `POP-05` | `ACT-018`, `ACT-013` |
| `RSK-010` | Migrant-worker language-channel gap | T2 | spans 10-day horizon | — | `POP-02` | `ACT-014` |
| `RSK-011` | Merrow Port potable-water gap for POP-17 | T3 | 1-3 days | Down | `POP-17` | `ACT-009`, `ACT-010` |
| `RSK-012` | Displaced-population shelter strain | T3 | 3-7 days | — | `POP-06` | `ACT-011` |
| `RSK-013` | South Latch habitability under levee silence | T3 | window-unknown | Up | `POP-03` | `ACT-019` |
| `RSK-014` | Regional-hospital generator fuel exhaustion | T4 | hours–days (unknown) | Up | — (multi-downstream) | `ACT-007` |
| `RSK-015` | Freight-rail-bridge + fibre-trunk shared-fate cascade | T4 | window-unknown | Up | — (multi-downstream) | `ACT-015` |
| `RSK-016` | South Latch levee state silence | T4 | window-unknown | Up | — (`POP-03` conditional) | `ACT-019` |
| `RSK-017` | Merrow Port water-treatment decontamination timeline unknown | T4 | 1-3 days | Up | — (`POP-17` downstream) | `ACT-009` |
| `RSK-018` | Coastal-substation degradation topology unknown | T4 | 3-7 days | Up | — (district grid) | `ACT-020` |
| `RSK-019` | EXT-01 central-government counterparty reliability | T4 | 1-3 days | Up | — (cross-cutting) | `ACT-022`, `ACT-023`, fallback-refs |
| `RSK-020` | Sea-access salvage prerequisite for outer-islet support | T4 | window-unknown | Up | — (`POP-05` downstream) | `ACT-013` |
| `RSK-021` | Non-institutional aged cohort informal care-circle topology unmapped | T4 | 1-3 days | — | `POP-07` (non-institutional) | `ACT-017` |
| `RSK-022` | Mortuary capacity / mass-casualty handling silence | T4 | window-unknown | — | — (uncohorted silence) | `ACT-021` |

**Cohort-individuation check (per D-011 validation rule):** every
individuated medical-fragility cohort listed below appears in ≥1
`RSK-*` row:
- `POP-08` → `RSK-008` ✓
- `POP-09` → `RSK-001` ✓
- `POP-10` → `RSK-002` ✓
- `POP-11` → `RSK-003` ✓
- `POP-12` → `RSK-004` ✓
- `POP-13` → `RSK-005` ✓
- `POP-14` → `RSK-006` ✓
- `POP-15` → `RSK-007` ✓

Check passes. No cohort collapsed into `POP-5K-parent`.

## Per-risk entries

### Tier 1 — individuated medical-fragility cohorts

#### RSK-001 — South Latch dialysis gap

- **Title:** South Latch dialysis gap — centre inaccessible.
- **Description:** If `INF-04` South Latch dialysis centre remains
  inaccessible (flood access via `DEP-05`) and inter-hospital
  referral (`ASM-17`) is not established in time, `POP-09` ~1,200
  dialysis patients miss scheduled sessions, causing acute
  avoidable harm on a days-scale clock.
- **Cohort affected:** `POP-09` (~1,200).
- **Infrastructure affected:** `INF-04` (inaccessible), `INF-02`
  (Kellan Rise hospital, potential referral destination).
- **Service affected:** `SVC-03` haemodialysis.
- **Dependency chain:** `DEP-09` (infrastructure-to-cohort block),
  `DEP-05` (flood access), `DEP-06` (`INF-15` highway bridge →
  `SVC-07` transport to Kellan Rise), `SVC-07` (inter-settlement
  road).
- **Time-to-harm window:** `1-3 days`.
- **Premises:** brief §Current state (`INF-04` inaccessible);
  `ASM-17` inter-hospital referral feasibility.
- **Silence dependencies:** `SIL-24` (home/private/cross-district
  dialysis patients outside `POP-09`+`POP-10` unknown).
- **Evidence state:** `brief-stated` (`INF-04` state) + `assumed`
  (referral feasibility).
- **Linked actions:** `ACT-003`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-002 — Merrow Port regional dialysis at risk

- **Title:** Merrow Port regional dialysis at-risk from generator/
  fuel chain.
- **Description:** `POP-10` ~220 dialysis patients are cared for at
  `INF-01` Merrow Port regional hospital, which is currently on
  generator (`INF-30`) with unknown fuel status. If `INF-30` fuel
  exhausts and `INF-32` supply chain cannot replenish in time,
  `SVC-03` at `INF-01` degrades and the cohort's time-to-harm
  inverts from `1-3 days` to `hours`.
- **Cohort affected:** `POP-10` (~220).
- **Infrastructure affected:** `INF-01`, `INF-30`, `INF-32`.
- **Service affected:** `SVC-03`, `SVC-05` (electrical supply to
  hospital).
- **Dependency chain:** `DEP-11` (generator backs up hospital),
  `DEP-12` (fuel chain to generator), `DEP-13` (power → cold chain,
  indirect for dialysis equipment).
- **Time-to-harm window:** `1-3 days` (flagged as invertible to
  `hours` pending `SIL-09` resolution).
- **Premises:** `ASM-15` (fuel chain exists), `GIV-01` (horizon).
- **Silence dependencies:** `SIL-09` (fuel status), `SIL-18` (fuel
  chain actors/routes).
- **Evidence state:** `inferred` (generator fuel exhaustion
  trajectory) from `brief-stated` (on-generator status) +
  `assumed` (`ASM-15` chain existence).
- **Linked actions:** `ACT-004`, `ACT-007`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-003 — Neonatal care disruption

- **Title:** Neonatal care disruption — generator + occupancy silence.
- **Description:** `POP-11` neonatal occupants at `INF-01` face
  hours-band harm under `SVC-09` neonatal-care disruption. Cohort
  size is unknown per `SIL-03`; cohort existence is the trigger, not
  cohort size. `DEP-10` couples `SVC-09` to `INF-01`, which depends
  on `INF-30` generator via `DEP-11`, which depends on `INF-32` fuel
  via `DEP-12`.
- **Cohort affected:** `POP-11` (count unknown).
- **Infrastructure affected:** `INF-01`, `INF-30`, `INF-32`.
- **Service affected:** `SVC-09`, `SVC-05`.
- **Dependency chain:** `DEP-10`, `DEP-11`, `DEP-12`.
- **Time-to-harm window:** `hours`.
- **Premises:** `ASM-15`; brief (`INF-01` on generator).
- **Silence dependencies:** `SIL-03` (occupancy), `SIL-09` (fuel
  status).
- **Evidence state:** `brief-stated` (unit exists + on generator) +
  `silent` (occupancy).
- **Linked actions:** `ACT-001`, `ACT-007`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-004 — CPAP/home-oxygen cohort power dependency

- **Title:** CPAP/home-oxygen cohort power dependency under grid
  outage.
- **Description:** `POP-12` sub-cohort of `POP-5K-parent` depends on
  powered equipment (CPAP or home oxygen concentrators). With
  `INF-11` grid out across Merrow Port + South Latch and `SVC-05`
  unavailable, the oxygen-dependent subset faces `hours`-band harm
  (oxygen supply exhausts faster than CPAP battery reserves), while
  the CPAP-dependent subset faces `1-3 days`-band harm. Count is
  unknown per `ASM-06` decomposition silence. The sub-cohort
  internal split (oxygen vs CPAP) is itself a §5.1 re-derivation
  instance [`01C`, Q7].
- **Cohort affected:** `POP-12` (count unknown); sub-cohorts not
  individuated at v1.
- **Infrastructure affected:** `INF-11` grid out.
- **Service affected:** `SVC-05`.
- **Dependency chain:** `DEP-02` (`SVC-05` powers powered-medical
  equipment; inferred per `ASM-14`).
- **Time-to-harm window:** `hours` (flagged, oxygen subset); also
  `1-3 days` (CPAP subset) — entry carries dual window per D-011
  per-cohort rule.
- **Premises:** `ASM-14`, `ASM-06`.
- **Silence dependencies:** `SIL-07` (disability cohorts beyond
  powered-equipment users unknown).
- **Evidence state:** `inferred` (coupling of power loss to cohort
  harm).
- **Linked actions:** `ACT-006`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-005 — Insulin cold-chain failure

- **Title:** Insulin cold-chain failure for insulin-dependent cohort.
- **Description:** `POP-13` insulin-dependent cohort depends on
  refrigerated insulin supply via `SVC-08` cold chain. With
  `INF-11` grid out, `SVC-08` is at-risk per `DEP-13` (`SVC-05`
  powers `SVC-08`). Harm window for insulin thermal tolerance is
  `1-3 days` qualitatively (pretrained clinical numeric values
  declined per `ASM-20`).
- **Cohort affected:** `POP-13` (count unknown).
- **Infrastructure affected:** `INF-11`.
- **Service affected:** `SVC-08`, `SVC-05`.
- **Dependency chain:** `DEP-13`.
- **Time-to-harm window:** `1-3 days`.
- **Premises:** `ASM-14`, `ASM-16`, `ASM-06`.
- **Silence dependencies:** `SIL-07`.
- **Evidence state:** `inferred`.
- **Linked actions:** `ACT-005`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-006 — Refrigerated-biologic cold-chain failure

- **Title:** Refrigerated-biologic cold-chain failure.
- **Description:** `POP-14` refrigerated-biologic-dependent cohort
  (cancer therapies, specialty biologics) faces cold-chain failure
  on a slower but cliff-edged clock — once `SVC-08` fails, the whole
  batch fails [`01C`, Q2]. Harm window `3-7 days` qualitatively.
- **Cohort affected:** `POP-14` (count unknown).
- **Infrastructure affected:** `INF-11`.
- **Service affected:** `SVC-08`, `SVC-05`.
- **Dependency chain:** `DEP-13`.
- **Time-to-harm window:** `3-7 days`.
- **Premises:** `ASM-14`, `ASM-16`, `ASM-06`.
- **Silence dependencies:** (none additional).
- **Evidence state:** `inferred`.
- **Linked actions:** `ACT-005`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-007 — Other refrigerated-med cohort dependency

- **Title:** Other refrigerated-med cohort dependency.
- **Description:** `POP-15` residual sub-cohort of `POP-5K-parent`
  for refrigerated-med dependents outside insulin + biologic
  categories. Brief does not specify composition; time-to-harm
  unknown.
- **Cohort affected:** `POP-15` (count unknown).
- **Infrastructure affected:** `INF-11`.
- **Service affected:** `SVC-08`, `SVC-05`.
- **Dependency chain:** `DEP-13`.
- **Time-to-harm window:** `window-unknown`.
- **Premises:** `ASM-14`, `ASM-16`, `ASM-06`.
- **Silence dependencies:** `SIL-07`.
- **Evidence state:** `silent` (on cohort composition and window).
- **Linked actions:** `ACT-005`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-008 — Aged-care cluster welfare

- **Title:** Aged-care cluster welfare under flood/occupancy silence.
- **Description:** `POP-08` institutionally-housed aged reside in
  `INF-12` and `INF-13` South Latch aged-care clusters, whose T0
  flood state is unknown (`SIL-11`) and resident counts are unknown
  (`SIL-02`). Welfare degradation (water, power, medication
  continuity, staffing) risk is `1-3 days` window qualitatively.
- **Cohort affected:** `POP-08` (count unknown).
- **Infrastructure affected:** `INF-12`, `INF-13`.
- **Service affected:** `SVC-10` aged-care continuity; `SVC-04`
  water; `SVC-05` power; `SVC-08` cold chain.
- **Dependency chain:** `DEP-05` flood access; `DEP-14` levee
  conditions habitability.
- **Time-to-harm window:** `1-3 days`.
- **Premises:** brief (clusters exist); `ASM-04` (majority of
  `POP-07` not in clusters — implies small cluster share but
  specific count unknown).
- **Silence dependencies:** `SIL-02`, `SIL-11`, `SIL-15`.
- **Evidence state:** `silent`.
- **Linked actions:** `ACT-016`.
- **Status:** `open`.
- **Session introduced:** 002.

### Tier 2 — cohort-silence cohorts

#### RSK-009 — Outer-islet contact silence

- **Title:** Outer-islet contact silence (count + access + VHF
  state).
- **Description:** `POP-05` outer-islet fishing community has
  unknown count (`SIL-01`), VHF pre-disaster but post-surge
  operability unknown (`ASM-13`), degraded sea access (`INF-16`),
  degraded air access (`INF-20`). Contact-silence itself is a risk
  vector — invisible cohorts can experience acute harm unnoticed.
- **Cohort affected:** `POP-05`.
- **Infrastructure affected:** `INF-19` (VHF), `INF-16` (sea
  access), `INF-20` (air).
- **Service affected:** `SVC-11` (sea transport), `SVC-12` (air
  transport), `SVC-13` (telecoms), `SVC-14` (salvage).
- **Dependency chain:** `DEP-20` (`INF-19` communicates to
  `POP-05`).
- **Time-to-harm window:** `window-unknown` — unknown count is not
  low-impact, it is a visibility failure [`01E`, Q2].
- **Premises:** `GIV-05` (informal VHF networks); `ASM-13`.
- **Silence dependencies:** `SIL-01`.
- **Evidence state:** `silent`.
- **Linked actions:** `ACT-018`, `ACT-013`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-010 — Migrant-worker language-channel gap

- **Title:** Migrant-worker cohort language-channel gap.
- **Description:** `POP-02` ~9K dormitory cohort uses two non-
  majority languages (`GIV-04`); T0 occupancy unknown (`ASM-02`);
  language-channel coverage for `SVC-15` risk communication
  unknown (`ASM-18`). Info-starvation harm compounds across the
  10-day horizon, not a discrete harm window [`01C`, Q2].
- **Cohort affected:** `POP-02` (~9K estimate; T0 occupancy unknown).
- **Infrastructure affected:** `INF-17`, `INF-18`, `INF-19`
  (comms infrastructure serving public information).
- **Service affected:** `SVC-15`.
- **Dependency chain:** `DEP-18`, `DEP-19`.
- **Time-to-harm window:** spans 10-day horizon (compound
  information starvation); entry flagged as `window-unknown` in
  acute band but active across the horizon.
- **Premises:** `GIV-04`, `ASM-02`, `ASM-18`.
- **Silence dependencies:** `SIL-20` (language-channel coverage),
  `SIL-21` (dormitory operators).
- **Evidence state:** `silent` (on channel coverage).
- **Linked actions:** `ACT-014`.
- **Status:** `open`.
- **Session introduced:** 002.

### Tier 3 — aggregate populations

#### RSK-011 — Merrow Port potable-water gap

- **Title:** Merrow Port potable-water gap for POP-17.
- **Description:** `POP-17` ~27K Merrow Port residents not on
  backup-well rotation are in water-supply gap. `INF-05` treatment
  plant salt-intruded (decontamination timeline not stated);
  `INF-06` backup wells serve ~35K on rotation; potability assumed
  but untested (`ASM-08`).
- **Cohort affected:** `POP-17` (~27K).
- **Infrastructure affected:** `INF-05`, `INF-06`.
- **Service affected:** `SVC-04`.
- **Dependency chain:** `DEP-03`, `DEP-04`.
- **Time-to-harm window:** `1-3 days`.
- **Premises:** `ASM-07` (arithmetic); `ASM-08` (potability).
- **Silence dependencies:** (none direct beyond treatment-timeline
  silence).
- **Evidence state:** `inferred` (derivation from brief arithmetic).
- **Linked actions:** `ACT-009`, `ACT-010`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-012 — Displaced-population shelter strain

- **Title:** Displaced-population shelter strain.
- **Description:** `POP-06` ~18K displaced per `ASM-03` baseline;
  `INF-22` shelter capacity "strained" per brief; operators,
  locations, specific capacities unknown (`SIL-17`).
- **Cohort affected:** `POP-06`.
- **Infrastructure affected:** `INF-22`.
- **Service affected:** `SVC-06`.
- **Dependency chain:** `DEP-17`.
- **Time-to-harm window:** `3-7 days` (shelter strain compounds
  without resolution).
- **Premises:** `ASM-03` (baseline stability).
- **Silence dependencies:** `SIL-17`.
- **Evidence state:** `brief-stated` (strained).
- **Linked actions:** `ACT-011`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-013 — South Latch habitability under levee silence

- **Title:** South Latch habitability contingent on levee state.
- **Description:** `POP-03` ~58K South Latch residents live in a
  settlement that is "levee-dependent" per brief; levee T0 state
  unstated (`SIL-15`). If `INF-21` has failed or is at risk of
  failing, `DEP-14` conditions `POP-03` habitability. The risk is
  conditional and its window depends on silence closure.
- **Cohort affected:** `POP-03`.
- **Infrastructure affected:** `INF-21`.
- **Service affected:** (habitability of settlement as a whole).
- **Dependency chain:** `DEP-14`.
- **Time-to-harm window:** `window-unknown`.
- **Premises:** brief (levee-dependent).
- **Silence dependencies:** `SIL-15`.
- **Evidence state:** `silent`.
- **Linked actions:** `ACT-019`.
- **Status:** `open`.
- **Session introduced:** 002.

### Tier 4 — upstream infrastructure / service-only risks

#### RSK-014 — Regional-hospital generator fuel exhaustion (upstream)

- **Title:** Regional-hospital generator fuel exhaustion — multi-
  downstream.
- **Description:** `INF-30` generator backs up `INF-01` regional
  hospital; fuel status `SIL-09`; fuel chain `INF-32` actors/
  routes `SIL-18`. Exhaustion of `INF-30` fuel cascades to `SVC-01`
  acute care, `SVC-09` neonatal, dialysis at `INF-01` (affects
  `POP-10`, `POP-11`), and potentially inter-hospital referral
  (`ASM-17` depends on sending hospital remaining functional).
- **Cohort affected:** — (risk is multi-downstream; touches `POP-10`,
  `POP-11`, general hospitalised patients).
- **Infrastructure affected:** `INF-01`, `INF-30`, `INF-32`.
- **Service affected:** `SVC-01`, `SVC-05` (hospital-local),
  `SVC-09`, `SVC-03`.
- **Dependency chain:** `DEP-11`, `DEP-12`.
- **Time-to-harm window:** `hours` (if fuel low) to `1-3 days` (if
  fuel buffer adequate). Flagged `window-unknown` pending `SIL-09`
  resolution.
- **Premises:** `ASM-15`.
- **Silence dependencies:** `SIL-09`, `SIL-18`.
- **Evidence state:** `silent`.
- **Linked actions:** `ACT-007`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-015 — Freight-rail-bridge + fibre shared-fate cascade

- **Title:** Freight-rail-bridge (`INF-14`) + fibre-trunk (`INF-17`)
  shared-fate cascade to Kellan Rise connectivity.
- **Description:** `INF-14` damaged but passable per brief; carries
  `INF-17` fibre trunk via `DEP-08` (shared-fate). `INF-17` service
  state unknown per `ASM-12`. Further degradation of `INF-14` (e.g.,
  structural failure under continued saturation) takes `INF-17` with
  it, losing `SVC-13` to Kellan Rise via `DEP-15`. Kellan Rise is
  the `ASM-17` referral destination for `INF-01`; if `SVC-13`
  fails, inter-hospital coordination for `POP-09` referral via
  `ASM-17` degrades.
- **Cohort affected:** — (multi-downstream via comms + referrals).
- **Infrastructure affected:** `INF-14`, `INF-17`.
- **Service affected:** `SVC-13`, `SVC-07` (road via `INF-14`
  carriage), `SVC-03` (via referral degradation).
- **Dependency chain:** `DEP-08`, `DEP-15`.
- **Time-to-harm window:** `window-unknown` (bridge "damaged but
  passable"; fibre state unstated).
- **Premises:** `ASM-12`.
- **Silence dependencies:** (fibre operational state unstated).
- **Evidence state:** `inferred`.
- **Linked actions:** `ACT-015`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-016 — South Latch levee state silence

- **Title:** South Latch levee state silence (upstream
  habitability).
- **Description:** Same physical asset as RSK-013's trigger,
  recorded as an upstream risk here because levee-state closure
  is a silence-closing action that conditionally enables multiple
  downstream risks (aged-care cluster access, dispersed smallholding
  safety, potable-water distribution routes). Duplication between
  RSK-013 and RSK-016 is intentional: RSK-013 is the cohort-facing
  view (`POP-03` habitability); RSK-016 is the infrastructure-
  upstream view. Both link to `ACT-019`.
- **Cohort affected:** — (conditional cohorts include `POP-03`,
  `POP-08`, `POP-16`).
- **Infrastructure affected:** `INF-21`.
- **Service affected:** (conditional, multi-service).
- **Dependency chain:** `DEP-14`.
- **Time-to-harm window:** `window-unknown`.
- **Premises:** brief.
- **Silence dependencies:** `SIL-15`.
- **Evidence state:** `silent`.
- **Linked actions:** `ACT-019`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-017 — Merrow Port water-treatment decontamination timeline unknown

- **Title:** Water-treatment decontamination timeline unknown.
- **Description:** `INF-05` salt-intruded; decontamination
  assessment underway per brief, but timeline not stated. If
  timeline exceeds the period that `INF-06` backup wells can
  sustain ~35K on rotation, `POP-17` water-supply gap widens and/or
  `INF-06` itself becomes capacity-constrained.
- **Cohort affected:** — (upstream of `POP-17`).
- **Infrastructure affected:** `INF-05`, `INF-06`.
- **Service affected:** `SVC-04`.
- **Dependency chain:** `DEP-03`, `DEP-04`.
- **Time-to-harm window:** `1-3 days`.
- **Premises:** `ASM-08`, `ASM-10` (utility reported-not-physical).
- **Silence dependencies:** (treatment timeline).
- **Evidence state:** `inferred`.
- **Linked actions:** `ACT-009`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-018 — Coastal-substation degradation topology unknown

- **Title:** Substation degradation topology unknown (grid
  restoration sequencing).
- **Description:** Brief states "2 of 4 coastal substations
  degraded" but does not identify which two (`SIL-12`); `INF-09`
  and `INF-10` inferred operational by arithmetic (`ASM-09`).
  Restoration sequencing depends on which substations are down.
  Risk is window-slow but upstream.
- **Cohort affected:** — (district grid affects all downstream).
- **Infrastructure affected:** `INF-07`, `INF-08`, `INF-09`, `INF-10`,
  `INF-11`.
- **Service affected:** `SVC-05`.
- **Dependency chain:** `DEP-01`.
- **Time-to-harm window:** `3-7 days` (per utility `ASM-10`
  estimate).
- **Premises:** `ASM-09`, `ASM-10`.
- **Silence dependencies:** `SIL-12`.
- **Evidence state:** `silent`.
- **Linked actions:** `ACT-020`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-019 — EXT-01 counterparty reliability (single-point dependency)

- **Title:** EXT-01 central-government counterparty reliability.
- **Description:** `ASM-19` grants `EXT-01` reliable as recipient
  of the 10-day plan. Any plan action that requires `EXT-01` as
  *delivery partner* (fuel logistics, sea/air lift, medical
  evacuation, national-guard inspection) depends on a *different*
  reliability claim that `ASM-19` does not substantiate [`01D`,
  Q5d]. If `EXT-01` fails at T0+36h with no fallback, any action
  premised on `ASM-19` collapses [`01B`, Q5d]. This risk is
  cross-cutting — it traverses `STR-power-and-fuel`,
  `STR-access-and-transport`, `STR-outer-islet-contact`, and
  `STR-reconnaissance-and-silence-closure`.
- **Cohort affected:** — (cross-cutting; ultimately touches every
  T1 cohort served by an external-dependent action).
- **Infrastructure affected:** (cross-cutting).
- **Service affected:** (cross-cutting).
- **Dependency chain:** `DEP-21`.
- **Time-to-harm window:** `1-3 days` (for actions whose
  `initiation_band` is acute and that depend on `EXT-01`).
- **Premises:** `ASM-19` (flagged for Session 003 split into
  recipient-reliability vs delivery-reliability).
- **Silence dependencies:** `SIL-23` (governance legitimacy).
- **Evidence state:** `assumed`.
- **Linked actions:** `ACT-022`, `ACT-023`; `fallback_ref` entries
  on every external-actor `ACT-*`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-020 — Sea-access salvage prerequisite

- **Title:** Sea-access salvage prerequisite for outer-islet
  support.
- **Description:** `SVC-14` salvage is a prospective service not
  yet active; `SVC-11` sea transport to outer islets (`POP-05`)
  cannot function until salvage completes on `INF-16` degraded
  sea access. If salvage slips, `POP-05` contact + material
  support depends entirely on `SVC-12` air transport (degraded,
  `INF-20` runway debris).
- **Cohort affected:** — (upstream of `POP-05`).
- **Infrastructure affected:** `INF-16`, `INF-20`.
- **Service affected:** `SVC-11`, `SVC-14`, `SVC-12`.
- **Dependency chain:** (prospective).
- **Time-to-harm window:** `window-unknown`.
- **Premises:** brief.
- **Silence dependencies:** `SIL-14` (airport runway settlement).
- **Evidence state:** `inferred`.
- **Linked actions:** `ACT-013`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-021 — Informal care-circle topology unmapped

- **Title:** Informal care-circle topology for non-institutional aged
  unmapped.
- **Description:** `POP-07` majority aged 70+ are not institutionally
  housed per `ASM-04` inference; their welfare during the 10-day
  horizon depends on informal care circles ("the neighbour who
  usually brings Mrs K her groceries") which are `SIL-19` unmapped.
  `SVC-10` aged-care continuity at the community level is
  infrastructure-less.
- **Cohort affected:** `POP-07` (non-institutional subset).
- **Infrastructure affected:** — (no formal infrastructure for
  informal care).
- **Service affected:** `SVC-10`.
- **Dependency chain:** — (social topology, not physical).
- **Time-to-harm window:** `1-3 days`.
- **Premises:** `ASM-04`.
- **Silence dependencies:** `SIL-19`.
- **Evidence state:** `silent`.
- **Linked actions:** `ACT-017`.
- **Status:** `open`.
- **Session introduced:** 002.

#### RSK-022 — Mortuary capacity / mass-casualty handling silence

- **Title:** Mortuary capacity / mass-casualty handling silence.
- **Description:** Brief is silent on fatalities and on mortuary
  infrastructure. Under a 2.8m surge with ~18K displaced and
  known-vulnerable cohorts exposed, mass-casualty handling capacity
  is a silence that cannot be assumed adequate. Surfaced by 01C
  Session 001 and carried forward; not resolved.
- **Cohort affected:** — (uncohorted silence; `uncohorted: true`
  flag).
- **Infrastructure affected:** — (unenumerated).
- **Service affected:** — (unenumerated).
- **Dependency chain:** —.
- **Time-to-harm window:** `window-unknown`.
- **Premises:** (none from brief).
- **Silence dependencies:** `SIL-22`.
- **Evidence state:** `silent`.
- **Linked actions:** `ACT-021`.
- **Status:** `open`.
- **Session introduced:** 002.

## Risks considered and not included at v1

- **Waterborne-disease outbreak risk in displaced population.**
  Considered; deferred because brief does not state waterborne-
  disease baseline and pretrained epidemiological numbers would
  launder (`ASM-20`). Session 003 or later may add if `INF-05`
  contamination triggers a formal assessment.
- **Mental-health / substance-dependence continuity risk.** Surfaced
  Session 001 as `SIL-05`; not pinned to a `POP-*` cohort at v1
  because the cohort is unenumerated.
- **Children-under-5 cohort-specific risk.** `SIL-06` silence; not
  individuated as `POP-*` at Session 001; deferred pending cohort
  definition.
- **Pregnancy / early-infant outside neonatal unit.** `SIL-04`
  silence; same reasoning.
- **Undocumented-persons cohort.** `SIL-08` silence; politically
  sensitive and unenumerated at v1.
- **Secondary-event risk (aftershock / second surge / vector-borne
  disease bloom).** Out of scope per Session 001 D-001 §Out of scope
  for v1.
- **Economic-flow disruption / commodity-pricing risk.** Out of
  scope per Session 001 §Out of scope.

These are recorded here so Session 003 knows what v1 chose not to
include, and why.

## Honest limits

- `POP-12` internal CPAP-vs-oxygen split (`01C`, Q2) is known to
  matter for time-to-harm but is not individuated at v1 per Session
  001 D-007 (counts unknown). RSK-004 carries dual window as a
  workaround; the cleaner fix is sub-individuation in a future
  session.
- `POP-08` cluster-specific risks (`INF-12` vs `INF-13`) are rolled
  into one entry; if the two clusters have differentially bad
  flood status, the risk profile differs. RSK-008 does not expose
  this; `ACT-016` reconnaissance will.
- `POP-05` outer-islet risk count: by D-016 dual treatment, the
  settlement-scale risks (RSK-009's access-modality) and cohort-
  scale risks (implicit, pending count) are merged into RSK-009
  because the count-silence means cohort-scale risks cannot be
  enumerated separately at v1. Post-count-closure, RSK-009 should
  split.
- Dependency-depth tags are qualitative not network-computed.
  Formal dependency-depth computation (e.g., transitive closure on
  `DEP-*`) would require the multi-view model (§5.1 activation
  direction) exposed as a graph.
- §5.1 activation note applies: dependencies named above were
  re-derived from the flat model in multiple instances. The
  register records what was derived, not the view that would have
  derived it natively.
