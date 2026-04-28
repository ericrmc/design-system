---
title: Laurel Delta response plan — v1
originating_session: 002
artefact_kind: response-plan
domain: disaster-response
engine_version: engine-v7
validation: workspace-only
status: v1
created: 2026-04-24
last-revised-session: 002
---

# Laurel Delta response plan — v1

This plan enumerates 23 actions organised as concurrent service-
family streams for the 10-day response-and-stabilisation horizon
(`GIV-01`) following cyclone landfall at T0 (~36h before session
open). Each action is keyed to risks in `risk-register.md` and to
`POP-*`/`INF-*`/`SVC-*`/`DEP-*`/`ASM-*` entries in `system-model.md`
and `assumption-ledger.md`. Schema per Session 002 D-013; shape per
D-013 (concurrent streams, not phased compartments — 01B dissent
preserved as §5.2 first-class minority
`[archive: provenance/002-session/01-deliberation.md]` §5.2).
Frontmatter `validation: workspace-only` per D-020.

## On "stabilised" at T0+10d

Per D-017, the plan's T0+10d closure field is not a stabilisation-
certifying predicate; it is a list of **observable state descriptors
that will be true if the plan executes**. The predicate "stabilised"
is reserved for `EXT-01` Laurel Delta local government (the brief's
counterparty). State descriptors are listed per action as
`completion_criterion`; the aggregate T0+10d descriptor list is
assembled in §State descriptors at T0+10d below. No numeric
thresholds are named, per 01D's anti-laundering objection
`[archive: provenance/002-session/01D-perspective-adversarial-skeptic.md]`
Q5c.

## Sub-windows: review gates, not compartments

Per D-014, `WIN-acute` (T0–T0+72h) and `WIN-stab` (T0+72h–T0+10d) are
**review gates**, not operational compartments. Actions carry an
`initiation_band` field (finer grain: `T0+0-24h`, `T0+24-72h`,
`T0+72h-7d`, `T0+7-10d`, `silence-contingent`). Actions may span
windows; `initiation_band` says when the action starts, not where it
lives.

Two replan gates are scheduled:

- **`ACT-022`** — time-triggered gate at **T0+72h**. Every acute-
  initiated action reviewed; silences that have closed propagate into
  updated risk-register rows; `WIN-stab` triggers reconfirmed.
- **`ACT-023`** — information-triggered gate that fires when
  **≥4 of 8 priority `SIL-*` resolve**. Priority `SIL-*`: `SIL-01`
  (outer-islet count), `SIL-03` (neonatal occupancy), `SIL-09`
  (`INF-30` fuel status), `SIL-11` (aged-care cluster flood status),
  `SIL-12` (substation topology), `SIL-15` (levee state), `SIL-20`
  (language-channel coverage), `SIL-22` (mortuary capacity).

## Streams

| Stream | Scope | Actions |
|---|---|---|
| `STR-health-acute` | `SVC-01`, `SVC-09`, `INF-01` posture | `ACT-001`, `ACT-002` |
| `STR-dialysis-continuity` | `SVC-03`; `POP-09`, `POP-10` | `ACT-003`, `ACT-004` |
| `STR-cold-chain-and-medication` | `SVC-08`; `POP-13`, `POP-14`, `POP-15` | `ACT-005` |
| `STR-power-and-fuel` | `SVC-05`; `INF-30`, `INF-32`; `POP-12` power | `ACT-006`, `ACT-007`, `ACT-008` |
| `STR-water` | `SVC-04`; `INF-05`, `INF-06`; `POP-17` | `ACT-009`, `ACT-010` |
| `STR-shelter-and-displacement` | `SVC-06`; `POP-06` | `ACT-011` |
| `STR-access-and-transport` | `SVC-07`, `SVC-11`, `SVC-12`, `SVC-14`; `INF-15`, `INF-16` | `ACT-012`, `ACT-013` |
| `STR-communications-and-language` | `SVC-13`, `SVC-15`; `INF-17`, `INF-18`; `POP-02` | `ACT-014`, `ACT-015` |
| `STR-aged-care-and-care-circles` | `SVC-10`; `POP-07`, `POP-08` | `ACT-016`, `ACT-017` |
| `STR-outer-islet-contact` | `POP-05`, `INF-19` | `ACT-018` |
| `STR-reconnaissance-and-silence-closure` | Silence-closing actions across all streams | `ACT-019`, `ACT-020`, `ACT-021`, `ACT-022`, `ACT-023` |

Stream names are grounded in the `SVC-*` taxonomy of `system-model.md`
+ cohort-facing concerns from the ledger, not in UN/IASC cluster
catalogue. See D-013 rationale.

## Summary table (all actions)

| ID | Title | Stream | Initiation band | Cohort served | Risks addressed |
|---|---|---|---|---|---|
| `ACT-001` | POP-11 neonatal continuity confirmation | `STR-health-acute` | `T0+0-24h` | `POP-11` | `RSK-003` |
| `ACT-002` | INF-01 on-generator operating posture + referral readiness | `STR-health-acute` | `T0+0-24h` | — | `RSK-002`, `RSK-003`, `RSK-014` |
| `ACT-003` | POP-09 dialysis transport/referral schedule | `STR-dialysis-continuity` | `T0+0-24h` | `POP-09` | `RSK-001` |
| `ACT-004` | POP-10 dialysis continuity at INF-01 | `STR-dialysis-continuity` | `T0+0-24h` | `POP-10` | `RSK-002` |
| `ACT-005` | Cold-chain custody pathway for POP-13/14/15 | `STR-cold-chain-and-medication` | `T0+24-72h` | `POP-13`, `POP-14`, `POP-15` | `RSK-005`, `RSK-006`, `RSK-007` |
| `ACT-006` | Power continuity for POP-12 CPAP/oxygen users | `STR-power-and-fuel` | `T0+0-24h` (oxygen), `T0+24-72h` (CPAP) | `POP-12` | `RSK-004` |
| `ACT-007` | INF-30 fuel status + INF-32 resupply (with fallback) | `STR-power-and-fuel` | `silence-contingent` (SIL-09) | — | `RSK-002`, `RSK-003`, `RSK-014` |
| `ACT-008` | Grid restoration monitoring | `STR-power-and-fuel` | `T0+24-72h` | — | `RSK-018` |
| `ACT-009` | INF-06 potability verification + INF-05 decontamination monitoring | `STR-water` | `T0+0-24h` | — | `RSK-011`, `RSK-017` |
| `ACT-010` | Interim potable-water supply for POP-17 | `STR-water` | `T0+24-72h` | `POP-17` | `RSK-011` |
| `ACT-011` | POP-06 shelter stabilisation | `STR-shelter-and-displacement` | `T0+0-24h` | `POP-06` | `RSK-012` |
| `ACT-012` | INF-15 bridge 24-tonne persistence verification | `STR-access-and-transport` | `T0+72h-7d` (ASM-11 review) | — | `RSK-001` (supporting), `RSK-014` |
| `ACT-013` | INF-16 sea-access salvage initiation | `STR-access-and-transport` | `T0+24-72h` | `POP-05` | `RSK-009`, `RSK-020` |
| `ACT-014` | POP-02 migrant-worker risk-comm coverage (2 languages) | `STR-communications-and-language` | `T0+0-24h` | `POP-02` | `RSK-010` |
| `ACT-015` | INF-17 fibre monitoring + alternate comms planning | `STR-communications-and-language` | `T0+24-72h` | — | `RSK-015` |
| `ACT-016` | INF-12 + INF-13 aged-care cluster survey | `STR-aged-care-and-care-circles` | `T0+0-24h` | `POP-08` | `RSK-008` |
| `ACT-017` | POP-07 informal care-circle mapping | `STR-aged-care-and-care-circles` | `T0+24-72h` | `POP-07` (non-institutional) | `RSK-021` |
| `ACT-018` | POP-05 count + medical-fragility enumeration via INF-19 | `STR-outer-islet-contact` | `T0+0-24h` | `POP-05` | `RSK-009` |
| `ACT-019` | INF-21 levee state confirmation | `STR-reconnaissance-and-silence-closure` | `T0+0-24h` | — | `RSK-013`, `RSK-016` |
| `ACT-020` | Substation degradation identification | `STR-reconnaissance-and-silence-closure` | `T0+24-72h` | — | `RSK-018` |
| `ACT-021` | SIL-22 mortuary capacity / mass-casualty assessment | `STR-reconnaissance-and-silence-closure` | `T0+0-24h` | — | `RSK-022` |
| `ACT-022` | T0+72h time-triggered replan gate | `STR-reconnaissance-and-silence-closure` | `T0+72h-7d` (fires at T0+72h) | — | `RSK-019` |
| `ACT-023` | Information-triggered replan gate | `STR-reconnaissance-and-silence-closure` | `silence-contingent` (fires at ≥4 of 8 priority SIL resolved) | — | `RSK-019` |

**Cohort-coverage check.** Every individuated medical-fragility cohort
appears on ≥1 `ACT-*` row's `cohort_served` cell:
- `POP-08` → `ACT-016` ✓
- `POP-09` → `ACT-003` ✓
- `POP-10` → `ACT-004` ✓
- `POP-11` → `ACT-001` ✓
- `POP-12` → `ACT-006` ✓
- `POP-13`, `POP-14`, `POP-15` → `ACT-005` ✓

## Per-action entries

### STR-health-acute

#### ACT-001 — POP-11 neonatal continuity confirmation

- **Description:** Confirm `POP-11` occupancy at `INF-01` neonatal
  unit (close `SIL-03`); if occupied, verify power continuity
  (`INF-30` fuel + `INF-32` resupply via `ACT-007`) and clinical-
  team readiness; if transfer to `INF-02` Kellan Rise indicated,
  activate via `ASM-17` road referral on `INF-15`.
- **Cohort served:** `POP-11`.
- **Service restored:** `SVC-09`.
- **Infrastructure touched:** `INF-01`, `INF-30`; conditionally
  `INF-02`, `INF-15`.
- **Risks addressed:** `RSK-003`.
- **Premises:** `ASM-15`, `ASM-17`.
- **Upstream actions:** `ACT-007` (fuel assurance).
- **Actor class:** hospital clinical lead + local EMS coordinator.
- **Initiation band:** `T0+0-24h`.
- **Completion criterion:** `POP-11` occupancy status known; if
  occupied, each neonate has a documented pathway: (a) `INF-01`
  continuity confirmed through T0+10d via `INF-30`+`INF-32`
  supply, or (b) transfer to `INF-02` completed, or (c) exception
  documented and pending escalation.
- **Fallback ref:** `ACT-002` (referral readiness).
- **Status:** `planned`.

#### ACT-002 — INF-01 on-generator posture + referral readiness

- **Description:** Maintain `INF-01` regional hospital operating on
  `INF-30` generator for the acute window; establish bidirectional
  `INF-01`↔`INF-02` referral readiness per `ASM-17` via `INF-15`
  road; document inter-hospital comms path (contingent on `SVC-13`
  to Kellan Rise per `ACT-015`).
- **Cohort served:** — (cross-cutting; benefits `POP-10`, `POP-11`,
  general hospitalised population).
- **Service restored:** `SVC-01`.
- **Infrastructure touched:** `INF-01`, `INF-02`, `INF-30`, `INF-15`.
- **Risks addressed:** `RSK-002`, `RSK-003`, `RSK-014`.
- **Premises:** `ASM-17`, `CON-04`.
- **Upstream actions:** `ACT-007` (fuel), `ACT-012` (bridge
  verification for ASM-11).
- **Actor class:** hospital incident command + local EMS.
- **Initiation band:** `T0+0-24h`, continuing through horizon.
- **Completion criterion:** `INF-01`-to-`INF-02` referral pathway
  documented with transport timing and per-case triage; `INF-30`
  generator operating with fuel-status updates per `ACT-007`.
- **Fallback ref:** `(accepted: wait-and-replan)` if `INF-15` bridge
  fails and no sea/air alternative is operational; escalate via
  `ACT-022` gate.
- **Status:** `planned`.

### STR-dialysis-continuity

#### ACT-003 — POP-09 dialysis transport/referral schedule

- **Description:** Establish dialysis continuity for `POP-09` ~1,200
  South Latch patients whose centre `INF-04` is inaccessible
  (`DEP-09`). Primary path: road referral to `INF-02` Kellan Rise via
  `INF-15` (24-tonne, intact per `CON-04`; persistence per `ASM-11`).
  Each patient receives a scheduled alternate-site slot or documented
  exception.
- **Cohort served:** `POP-09`.
- **Service restored:** `SVC-03`.
- **Infrastructure touched:** `INF-02`, `INF-15`; `INF-04` (long-term
  target).
- **Risks addressed:** `RSK-001`.
- **Premises:** `ASM-17`, `CON-04`, `ASM-11`.
- **Upstream actions:** `ACT-002`, `ACT-012`.
- **Actor class:** local EMS + hospital dialysis coordination.
- **Initiation band:** `T0+0-24h`.
- **Completion criterion:** `POP-09` dialysis continuity confirmed
  for each known patient via (a) restored `INF-04` access, (b)
  referral to `INF-02`, or (c) documented exception pending
  escalation. No numeric threshold per D-017.
- **Fallback ref:** mobile dialysis unit request (`EXT-01`
  dependency; `(external: EXT-01)` tagged, fallback-to-`ACT-022`
  gate if unavailable).
- **Status:** `planned`.

#### ACT-004 — POP-10 dialysis continuity at INF-01

- **Description:** Maintain `POP-10` ~220 dialysis continuity at
  `INF-01` during on-generator operation. Risk is power-dependent
  per `RSK-002`; action's viability is contingent on `ACT-007` fuel
  assurance.
- **Cohort served:** `POP-10`.
- **Service restored:** `SVC-03`.
- **Infrastructure touched:** `INF-01`.
- **Risks addressed:** `RSK-002`.
- **Premises:** `ASM-15`.
- **Upstream actions:** `ACT-007`.
- **Actor class:** hospital dialysis coordination.
- **Initiation band:** `T0+0-24h`.
- **Completion criterion:** `POP-10` dialysis continues per pre-
  cyclone cadence; each missed or delayed session documented with
  reason.
- **Fallback ref:** referral to `INF-02` via `ACT-002` pathway if
  `INF-01` generator fails; `(accepted: wait-and-replan)` for
  non-acute scheduling if referral overwhelmed.
- **Status:** `planned`.

### STR-cold-chain-and-medication

#### ACT-005 — Cold-chain custody pathway for POP-13/14/15

- **Description:** Establish cold-chain custody for refrigerated
  medications (insulin for `POP-13`, biologics for `POP-14`, other
  refrigerated meds for `POP-15`) via (a) on-site refrigeration at
  backup-powered sites (e.g., Kellan Rise hospital `INF-02`, shelter
  sites with generators from `INF-31`); (b) ice / courier relay for
  distributed cohorts; (c) external cold-chain air lift via
  `EXT-01` where volume justifies.
- **Cohort served:** `POP-13`, `POP-14`, `POP-15`.
- **Service restored:** `SVC-08`.
- **Infrastructure touched:** `INF-02`, `INF-31` (where enumerated
  during reconnaissance), other on-site refrigeration points.
- **Risks addressed:** `RSK-005`, `RSK-006`, `RSK-007`.
- **Premises:** `ASM-14`, `ASM-16`, `ASM-06`.
- **Upstream actions:** `ACT-006` (power), `ACT-007` (fuel where
  on-site refrigeration is generator-backed).
- **Actor class:** community pharmacy / medication registry + local
  EMS.
- **Initiation band:** `T0+24-72h`.
- **Completion criterion:** `POP-13`, `POP-14`, `POP-15` each have
  a documented cold-chain custody path for the duration of the
  10-day horizon; custody gaps are documented per affected cohort.
- **Fallback ref:** ice/courier relay is the fallback path for (a);
  `(external: EXT-01)` tagged on (c); further fallback is
  `(accepted: wait-and-replan)` for non-acute sub-cohorts (`POP-15`
  under `window-unknown`).
- **Status:** `planned`.

### STR-power-and-fuel

#### ACT-006 — Power continuity for POP-12 CPAP/oxygen users

- **Description:** Identify known `POP-12` users by cohort sub-
  category (oxygen-dependent, CPAP-dependent) and arrange power
  continuity via (a) home-generator provision from `INF-31`
  unenumerated stock; (b) shelter placement with collective
  generator; (c) hospital-level admission for acute subset.
  Oxygen-dependent subset is hours-band; CPAP-dependent subset is
  1-3 days band (per `RSK-004` dual window).
- **Cohort served:** `POP-12`.
- **Service restored:** `SVC-05` (local).
- **Infrastructure touched:** `INF-31`; shelter sites (`INF-22`).
- **Risks addressed:** `RSK-004`.
- **Premises:** `ASM-14`.
- **Upstream actions:** `ACT-007` (for any shared-pool fuel).
- **Actor class:** community health + shelter coordinators.
- **Initiation band:** `T0+0-24h` (oxygen subset); `T0+24-72h`
  (CPAP subset).
- **Completion criterion:** Known `POP-12` oxygen-dependent users
  each have a documented power/oxygen continuity pathway (home
  generator, shelter placement, or hospital admission); CPAP-
  dependent users have power plans at initiation_band T0+24-72h.
- **Fallback ref:** `(accepted: wait-and-replan)` for CPAP subset
  only if oxygen subset fully covered.
- **Status:** `planned`.

#### ACT-007 — INF-30 fuel status + INF-32 resupply

- **Description:** Determine `INF-30` regional-hospital generator
  fuel buffer (close `SIL-09`); establish `INF-32` fuel supply
  chain (close `SIL-18`) with resupply cadence sufficient for the
  10-day horizon. Primary fuel-chain actor via `EXT-01` central-
  government logistics; fallback via `EXT-02` utility supplier and
  road-import from `EXT-03` highland interior via `INF-15`.
- **Cohort served:** — (upstream).
- **Service restored:** `SVC-05` at `INF-01`.
- **Infrastructure touched:** `INF-30`, `INF-32`.
- **Risks addressed:** `RSK-002`, `RSK-003`, `RSK-014`.
- **Premises:** `ASM-15`.
- **Upstream actions:** —.
- **Actor class:** hospital facilities + fuel logistics; `(external:
  EXT-01)` for primary path.
- **Initiation band:** `silence-contingent` on `SIL-09`; action
  begins immediately and converts to continuity-monitoring upon
  `SIL-09` closure.
- **Completion criterion:** `INF-30` fuel buffer ≥72h documented at
  first pass; at T0+72h gate, buffer ≥7d documented or replenishment
  cadence scheduled to maintain ≥72h rolling buffer through T0+10d.
- **Fallback ref:** `EXT-02` utility-supplier diversion (`(external:
  EXT-02)` tagged); road-import from `EXT-03` via `INF-15` per
  `ACT-012` persistence.
- **Status:** `planned`.

#### ACT-008 — Grid restoration monitoring

- **Description:** Track `EXT-02` utility restoration progress
  against the `ASM-10` 3-7 day estimate. Report at T0+72h and
  T0+5d checkpoints. Revise `ASM-10` or escalate if restoration
  slips.
- **Cohort served:** — (district-wide downstream).
- **Service restored:** `SVC-05`.
- **Infrastructure touched:** `INF-07`–`INF-11`.
- **Risks addressed:** `RSK-018`.
- **Premises:** `ASM-10`.
- **Upstream actions:** `ACT-020`.
- **Actor class:** local utility coordinator; `(external: EXT-02)`.
- **Initiation band:** `T0+24-72h`.
- **Completion criterion:** Grid restoration progress reported at
  T0+72h gate and T0+5d; `ASM-10` promoted (restoration on track) or
  revised (restoration delayed) at each report.
- **Fallback ref:** `(accepted: wait-and-replan)` — grid restoration
  is outside workspace control; the plan does not provide a
  parallel path to utility restoration.
- **Status:** `planned`.

### STR-water

#### ACT-009 — INF-06 potability verification + INF-05 decontamination monitoring

- **Description:** Test `INF-06` backup wells for potability
  (verify `ASM-08`); monitor `INF-05` treatment-plant salt-intrusion
  decontamination assessment and publish timeline.
- **Cohort served:** — (upstream `POP-17`).
- **Service restored:** `SVC-04`.
- **Infrastructure touched:** `INF-05`, `INF-06`.
- **Risks addressed:** `RSK-011`, `RSK-017`.
- **Premises:** `ASM-08`.
- **Upstream actions:** —.
- **Actor class:** local water utility + health department.
- **Initiation band:** `T0+0-24h`.
- **Completion criterion:** `INF-06` potability tested (`ASM-08`
  confirmed or revised); `INF-05` decontamination timeline
  published.
- **Fallback ref:** if `INF-06` fails potability, `ACT-010` scales
  up without the 35K baseline.
- **Status:** `planned`.

#### ACT-010 — Interim potable-water supply for POP-17

- **Description:** Supply `POP-17` ~27K Merrow Port residents not on
  backup-well rotation via tankered, bottled, or restored `INF-05`
  pathways. Exact modality depends on `ACT-009` outcomes.
- **Cohort served:** `POP-17`.
- **Service restored:** `SVC-04`.
- **Infrastructure touched:** `INF-22` (staging), `INF-15` (supply
  route).
- **Risks addressed:** `RSK-011`.
- **Premises:** `ASM-07` (arithmetic).
- **Upstream actions:** `ACT-009`.
- **Actor class:** local EMS + central-government logistics;
  `(external: EXT-01)` for tankered supply at scale.
- **Initiation band:** `T0+24-72h`.
- **Completion criterion:** `POP-17` on a declared potable-water
  plan (tankered, bottled, or restored `INF-05`); coverage logged
  at neighbourhood scale.
- **Fallback ref:** local dispersal via private water vendors if
  `EXT-01` logistics unavailable; `(accepted: wait-and-replan)` for
  non-distribution of potable water after 72h is not acceptable —
  escalate via `ACT-022` gate.
- **Status:** `planned`.

### STR-shelter-and-displacement

#### ACT-011 — POP-06 shelter stabilisation

- **Description:** Stabilise `POP-06` ~18K displaced into
  accommodation with declared tenure ≥14d (extending past horizon),
  language-accessible for `POP-02`, connected to medical-cohort
  needs where residents are on medical-fragility cohorts (`POP-09`–
  `POP-15`).
- **Cohort served:** `POP-06`.
- **Service restored:** `SVC-06`.
- **Infrastructure touched:** `INF-22`.
- **Risks addressed:** `RSK-012`.
- **Premises:** `ASM-03` (baseline displaced figure).
- **Upstream actions:** —.
- **Actor class:** shelter coordinators + local social services;
  `(external: EXT-01)` for transitional-shelter funding.
- **Initiation band:** `T0+0-24h`.
- **Completion criterion:** `POP-06` accommodated with declared
  tenure extending past T0+10d; language-accessibility for `POP-02`
  documented; medical-fragility residents cross-referenced to
  cohort-specific actions.
- **Fallback ref:** extended transitional shelter (tent cities);
  evacuation to Kellan Rise for unhoused subset via `ACT-003`/
  `ACT-012` transport path.
- **Status:** `planned`.

### STR-access-and-transport

#### ACT-012 — INF-15 bridge 24-tonne persistence verification

- **Description:** Engineering reinspection of `INF-15` highway
  bridge at T0+72h per `ASM-11` review trigger; confirm or revise
  24-tonne rating (`CON-04`).
- **Cohort served:** — (upstream).
- **Service restored:** `SVC-07`.
- **Infrastructure touched:** `INF-15`.
- **Risks addressed:** supports `RSK-001`, `RSK-014`.
- **Premises:** `CON-04`, `ASM-11`.
- **Upstream actions:** —.
- **Actor class:** engineering inspection team.
- **Initiation band:** `T0+72h-7d` (triggered by `ASM-11` review).
- **Completion criterion:** `INF-15` 24-tonne rating verified or
  revised; `ASM-11` promoted to `CON-04` or retired; rating report
  published.
- **Fallback ref:** if rating degrades, `ACT-003` and other
  transport-dependent actions replan via `ACT-022` gate.
- **Status:** `planned`.

#### ACT-013 — INF-16 sea-access salvage initiation

- **Description:** Initiate salvage on `INF-16` degraded sea access
  (stand up `SVC-14`) to enable `SVC-11` small-vessel traffic to
  outer islets. Enables `POP-05` physical access in support of
  `ACT-018`.
- **Cohort served:** `POP-05` (downstream).
- **Service restored:** `SVC-11`, `SVC-14`.
- **Infrastructure touched:** `INF-16`.
- **Risks addressed:** `RSK-009`, `RSK-020`.
- **Premises:** —.
- **Upstream actions:** —.
- **Actor class:** salvage contractors + harbourmaster; `(external:
  EXT-01)` for salvage funding/coordination.
- **Initiation band:** `T0+24-72h`.
- **Completion criterion:** `INF-16` sea access cleared for small-
  vessel traffic to outer islets; `SVC-14` stood up; first
  successful small-vessel transit logged or exception documented.
- **Fallback ref:** degrade to weather-permitting operations via
  private fishery vessels only; further fallback is to `ACT-018`
  VHF-only contact or `EXT-01` air reconnaissance.
- **Status:** `planned`.

### STR-communications-and-language

#### ACT-014 — POP-02 risk-comm coverage in two languages

- **Description:** Establish `SVC-15` risk communication coverage
  for `POP-02` migrant-worker dormitory cohort in both non-majority
  languages noted per `GIV-04`. Channels to be identified via
  dormitory-operator liaison (whose identity is `SIL-21`, partially
  closed by this action).
- **Cohort served:** `POP-02` (~9K estimate; T0 occupancy unknown
  per `ASM-02`).
- **Service restored:** `SVC-15`.
- **Infrastructure touched:** `INF-17`, `INF-18` (as carriers of
  public-information channels).
- **Risks addressed:** `RSK-010`.
- **Premises:** `GIV-04`, `ASM-02`, `ASM-18`.
- **Upstream actions:** —.
- **Actor class:** local public-information team + dormitory-
  operator liaison + community translators.
- **Initiation band:** `T0+0-24h`.
- **Completion criterion:** `POP-02` risk-communication channel
  coverage confirmed in both non-majority languages; dormitory-
  operator channels named and documented; `ASM-18` closed (promoted
  to `CON-*` or retired as unclosable within horizon).
- **Fallback ref:** in-person communication via community
  translators if broadcast channels unavailable.
- **Status:** `planned`.

#### ACT-015 — INF-17 fibre monitoring + alternate Kellan Rise comms

- **Description:** Monitor `INF-17` fibre-trunk operational state
  (close `ASM-12`); plan alternate `SVC-13` path to Kellan Rise
  (satellite uplink, VHF relay, or physical courier) if fibre
  degrades. Shared-fate risk with `INF-14` per `DEP-08`.
- **Cohort served:** — (upstream; enables inter-hospital coordination
  `ACT-002` and `ACT-003`).
- **Service restored:** `SVC-13`.
- **Infrastructure touched:** `INF-14`, `INF-17`.
- **Risks addressed:** `RSK-015`.
- **Premises:** `ASM-12`.
- **Upstream actions:** —.
- **Actor class:** ISP/carrier + emergency-coordination liaison;
  `(external: EXT-01)` for satellite comms standby.
- **Initiation band:** `T0+24-72h`.
- **Completion criterion:** `INF-17` operational state assessed;
  alternate comms pathway named and exercised at least once.
- **Fallback ref:** physical courier via `INF-15` road; VHF relay
  via pre-disaster `INF-19`-analogue setup.
- **Status:** `planned`.

### STR-aged-care-and-care-circles

#### ACT-016 — INF-12 + INF-13 aged-care cluster survey

- **Description:** Physical survey of `INF-12` + `INF-13` aged-care
  clusters in South Latch to establish flood status (close
  `SIL-11`), resident counts (close `SIL-02`), and continuity-of-
  service state (water, power, medication, staffing). Initiate
  evacuation if cluster-habitability degraded.
- **Cohort served:** `POP-08`.
- **Service restored:** `SVC-10`.
- **Infrastructure touched:** `INF-12`, `INF-13`.
- **Risks addressed:** `RSK-008`.
- **Premises:** —.
- **Upstream actions:** —.
- **Actor class:** community health + local EMS + flood-access
  teams.
- **Initiation band:** `T0+0-24h` (silence-closing priority).
- **Completion criterion:** `INF-12` + `INF-13` flood status known;
  `POP-08` resident counts established; water / power / medication /
  staffing continuity confirmed OR evacuation initiated per
  cluster-level finding.
- **Fallback ref:** evacuation to Kellan Rise via `ACT-002`
  referral path; `(accepted: wait-and-replan)` for partial-data
  findings requiring second pass.
- **Status:** `planned`.

#### ACT-017 — POP-07 informal care-circle mapping

- **Description:** Map `POP-07` non-institutional aged's informal
  care-circle topology (close `SIL-19`) at neighbourhood scale.
  Identify at-risk individuals whose usual support may be absent
  due to displacement or access loss.
- **Cohort served:** `POP-07` (non-institutional subset per
  `ASM-04`).
- **Service restored:** `SVC-10` (community-scale).
- **Infrastructure touched:** —.
- **Risks addressed:** `RSK-021`.
- **Premises:** `ASM-04`.
- **Upstream actions:** —.
- **Actor class:** community health + neighbourhood liaisons +
  local-government social services.
- **Initiation band:** `T0+24-72h`.
- **Completion criterion:** `POP-07` care-circle topology mapped
  at neighbourhood scale (not individual); at-risk individuals
  flagged for welfare check.
- **Fallback ref:** welfare-check by roving teams if liaisons
  unavailable.
- **Status:** `planned`.

### STR-outer-islet-contact

#### ACT-018 — POP-05 count + medical-fragility enumeration

- **Description:** Establish contact with outer-islet fishing
  community; determine count (close `SIL-01`); enumerate medical-
  fragility sub-cohorts within `POP-05`; assess `INF-19` VHF
  operability (close `ASM-13`). Primary channel: VHF attempt; if
  VHF fails, sea access via `ACT-013`; further fallback: air
  reconnaissance via `EXT-01`.
- **Cohort served:** `POP-05`.
- **Service restored:** `SVC-13` to outer islets.
- **Infrastructure touched:** `INF-19`.
- **Risks addressed:** `RSK-009`.
- **Premises:** `ASM-13`, `GIV-05`.
- **Upstream actions:** `ACT-013` (if VHF fails).
- **Actor class:** fishery coordinators + community radio operators;
  `(external: EXT-01)` air liaison as fallback.
- **Initiation band:** `T0+0-24h` (information-urgent).
- **Completion criterion:** `POP-05` count established OR failed-
  contact escalation documented with live search/access plan;
  medical-fragility sub-cohorts within `POP-05` enumerated OR
  declared still-silent with stated reason.
- **Fallback ref:** `ACT-013` sea path; further fallback `EXT-01`
  air; `(accepted: wait-and-replan)` for any sub-cohort that
  remains uncontactable after both sea and air attempts — escalate
  to `ACT-022`/`ACT-023` gates.
- **Status:** `planned`.

### STR-reconnaissance-and-silence-closure

#### ACT-019 — INF-21 levee state confirmation

- **Description:** Engineering inspection of `INF-21` South Latch
  levee (close `SIL-15`). Determine intact / compromised / failed
  state; publish structural report. This silence gates conditional
  habitability for `POP-03` per `DEP-14`.
- **Cohort served:** — (upstream conditional for `POP-03`,
  `POP-08`, `POP-16`).
- **Service restored:** — (habitability of South Latch).
- **Infrastructure touched:** `INF-21`.
- **Risks addressed:** `RSK-013`, `RSK-016`.
- **Premises:** —.
- **Upstream actions:** —.
- **Actor class:** engineering inspection + flood authority.
- **Initiation band:** `T0+0-24h` (silence-closing priority).
- **Completion criterion:** `INF-21` levee state reported (intact /
  compromised / failed); `SIL-15` closed; if compromised or failed,
  downstream replan via `ACT-022` / `ACT-023`.
- **Fallback ref:** aerial assessment via `EXT-01` if ground access
  unsafe.
- **Status:** `planned`.

#### ACT-020 — Substation degradation identification

- **Description:** Identify which 2 of `INF-07`–`INF-10` coastal
  substations are degraded (close `SIL-12`); refine `ASM-09`.
  Enables `ACT-008` grid-restoration monitoring sequencing.
- **Cohort served:** —.
- **Service restored:** — (enables `SVC-05`).
- **Infrastructure touched:** `INF-07`, `INF-08`, `INF-09`,
  `INF-10`.
- **Risks addressed:** `RSK-018`.
- **Premises:** `ASM-09`.
- **Upstream actions:** —.
- **Actor class:** utility field crew; `(external: EXT-02)`.
- **Initiation band:** `T0+24-72h`.
- **Completion criterion:** Substation topology published; `ASM-09`
  refined; `SIL-12` closed.
- **Fallback ref:** utility self-report if field access degraded.
- **Status:** `planned`.

#### ACT-021 — Mortuary capacity / mass-casualty assessment

- **Description:** Assess mortuary capacity and mass-casualty
  handling readiness (close `SIL-22`). Surface whether additional
  mass-casualty infrastructure is required for the horizon.
- **Cohort served:** — (uncohorted silence).
- **Service restored:** —.
- **Infrastructure touched:** — (unenumerated).
- **Risks addressed:** `RSK-022`.
- **Premises:** —.
- **Upstream actions:** —.
- **Actor class:** local public-health + forensic services;
  `(external: EXT-01)` for mass-casualty logistics escalation.
- **Initiation band:** `T0+0-24h` (silence-closing priority).
- **Completion criterion:** Mortuary capacity reported; mass-
  casualty handling plan triggered or documented as absent (latter
  escalates to `ACT-022`).
- **Fallback ref:** `(external: EXT-01)` for mass-casualty
  logistics; further fallback is adjacent-jurisdiction capacity
  request.
- **Status:** `planned`.

#### ACT-022 — T0+72h time-triggered replan gate

- **Description:** Scheduled replan gate at T0+72h. Re-check time-
  to-harm against observed state for every `ACT-*` still open;
  promote/demote `contingent-on-silence` risks whose silences have
  resolved; confirm `WIN-stab` triggers remain valid. Not a full
  replan — replan belongs to Session 003. This is a structured
  check-in point inside the 10-day horizon.
- **Cohort served:** —.
- **Service restored:** —.
- **Infrastructure touched:** —.
- **Risks addressed:** `RSK-019` (cross-cutting gate against
  `ASM-19` failure).
- **Premises:** —.
- **Upstream actions:** all acute-initiated actions.
- **Actor class:** operational command (local + `EXT-01` liaison);
  workspace-analogue is a Session 003 trigger.
- **Initiation band:** `T0+72h-7d` (fires at T0+72h).
- **Completion criterion:** Gate-minutes document per-action
  status; risk-register rows promoted/demoted; escalations tagged
  for session-003 consideration.
- **Fallback ref:** —.
- **Status:** `planned`.

#### ACT-023 — Information-triggered replan gate

- **Description:** Information-triggered replan gate. Fires when
  ≥4 of 8 priority `SIL-*` (see §Sub-windows above) have resolved.
  Purpose: same as `ACT-022` but anchored to information state
  rather than to clock. May fire before, at, or after T0+72h.
  Per 01D's [`01D`, Q4] trigger-on-information argument.
- **Cohort served:** —.
- **Service restored:** —.
- **Infrastructure touched:** —.
- **Risks addressed:** `RSK-019`.
- **Premises:** —.
- **Upstream actions:** the silence-closing actions `ACT-007`,
  `ACT-016`, `ACT-018`, `ACT-019`, `ACT-020`, `ACT-021`.
- **Actor class:** operational command.
- **Initiation band:** `silence-contingent`.
- **Completion criterion:** Replan executed under updated
  information state; gate-minutes document which silences closed
  and what replan changes resulted.
- **Fallback ref:** if fewer than 4 silences close by T0+10d, `ACT-023`
  does not fire; its non-firing is itself a signal (information-
  poor horizon) for Session 003.
- **Status:** `planned`.

## State descriptors at T0+10d

Per D-017, these are observable state descriptors that will be true
if the plan executes. They are not stabilisation-certifying criteria;
"stabilised" is `EXT-01`'s predicate. No numeric thresholds.

- **Dialysis continuity.** `POP-09` dialysis continuity confirmed
  for each known patient via (a) restored `INF-04`, (b) referral
  to `INF-02`, or (c) documented exception pending escalation.
  `POP-10` dialysis continuity confirmed at `INF-01` or via
  referral.
- **Neonatal continuity.** `POP-11` occupancy known; if occupied,
  each neonate has a documented continuity pathway.
- **Powered-medical continuity.** `POP-12` known oxygen-dependent
  users have power/oxygen continuity pathway; known CPAP-dependent
  users have power continuity pathway. Cohort sub-individuation
  remains `SIL-07`-gapped.
- **Cold-chain continuity.** `POP-13`, `POP-14`, `POP-15` each
  have documented cold-chain custody path, or documented custody
  gap with impact record.
- **Aged-care cluster continuity.** `INF-12` + `INF-13` flood
  status known; `POP-08` resident counts established; continuity
  of service confirmed OR evacuation completed.
- **Informal care-circle topology.** `POP-07` non-institutional
  care-circle topology mapped at neighbourhood scale.
- **Potable water.** `POP-17` on a declared potable-water plan with
  coverage logged.
- **Power / fuel.** `INF-01` off generator OR `INF-30` fuel buffer
  ≥7d documented with replenishment cadence; `INF-32` supply
  chain named.
- **Grid restoration.** `ASM-10` 3-7 day estimate verified or
  revised with published new timeline.
- **Shelter.** `POP-06` accommodated with declared tenure past
  T0+10d, language-accessible for `POP-02`.
- **Access infrastructure.** `INF-15` bridge 24-tonne rating
  verified or revised; `INF-16` sea-access salvage status reported.
- **Telecommunications.** `INF-17` fibre operational state assessed;
  `SVC-13` to Kellan Rise assured via primary or alternate pathway.
- **Risk communication.** `POP-02` language-channel coverage
  confirmed; `ASM-18` closed.
- **Outer-islet contact.** `POP-05` count established OR failed-
  contact documented with live plan; medical-fragility sub-cohorts
  enumerated or declared still-silent.
- **Levee.** `SIL-15` closed; `INF-21` state reported.
- **Substations.** `SIL-12` closed; substation topology published.
- **Mortuary.** `SIL-22` closed; mortuary capacity reported.
- **All `SIL-*` flagged as blocking a `WIN-stab` action** either
  closed or re-classified as `unknown-unbounded` with explicit
  acceptance.

The aggregation of these descriptors into "stabilised" or "not
stabilised" is a counterparty predicate; the plan does not claim
aggregation.

## External dependencies summary

Actions with `actor_class` tagged `(external: EXT-01)` or
`(external: EXT-02)`:

| Action | External actor | Fallback |
|---|---|---|
| `ACT-003` (secondary path) | `EXT-01` mobile dialysis | `ACT-022` gate escalation |
| `ACT-005` (tertiary path) | `EXT-01` cold-chain air lift | ice/courier relay (within action) |
| `ACT-007` (primary path) | `EXT-01` fuel logistics | `EXT-02` utility supplier + road-import via `EXT-03` |
| `ACT-008` | `EXT-02` grid restoration | `(accepted: wait-and-replan)` |
| `ACT-010` | `EXT-01` tankered supply | local private water vendors |
| `ACT-011` | `EXT-01` transitional-shelter funding | extended transitional (tent) shelter |
| `ACT-013` | `EXT-01` salvage coordination | weather-permitting fishery vessels |
| `ACT-015` | `EXT-01` satellite comms standby | physical courier via `INF-15` |
| `ACT-018` (fallback) | `EXT-01` air reconnaissance | `(accepted: wait-and-replan)` |
| `ACT-020` | `EXT-02` utility field crew | utility self-report |
| `ACT-021` (escalation) | `EXT-01` mass-casualty logistics | adjacent-jurisdiction request |

Every external-actor action carries either an explicit fallback or an
`(accepted: wait-and-replan)` annotation per D-018.

## Honest limits

- **Resource quantities are absent.** The plan does not name
  headcount, vehicle counts, fuel volumes, or budget lines. No
  workspace basis per `CON-02`. If a future session gains access to
  resource inventory, a v2 plan can specify.
- **Completion criteria are state-descriptors, not thresholds.** Per
  D-017 and 01D anti-laundering objection, no numeric percentages
  appear. An external reader who expects "≥95% coverage" formulations
  will find the plan less prescriptive than typical emergency-
  management plans. This is intended.
- **Actor classes are generic.** Named individuals and named
  institutions are absent. The plan does not commit `EXT-01` to
  specific operational authority beyond what `ASM-19`
  recipient-reliability permits.
- **Sequencing within bands is not computed.** Actions within the
  same `initiation_band` are concurrent unless an `upstream_actions`
  edge is explicit. No critical-path analysis.
- **Plan does not claim feasibility.** Per `CON-02`, workspace
  validation cannot assess whether `POP-09` ~1,200 dialysis patients
  can *actually* be transported to `INF-02` via `INF-15` in the
  required cadence. The plan specifies what must happen; whether it
  can happen is a domain question.
- **§5.1 activation impact.** Some actions address risks whose
  dependency chains required re-derivation from the single-document
  model (notably `ACT-005` cold-chain spanning `POP-13`/`POP-14`/
  `POP-15` with differing sub-cohort windows, and `ACT-007` fuel-
  chain whose `INF-32` details remain `SIL-18`). Session 003 may
  consider re-producing the plan against a multi-view model per
  D-019.
- **`ASM-19` single-point dependency.** The fallback annotations
  soften the exposure but do not eliminate it. If `EXT-01` fails
  broadly (not only on one action path), the fallbacks compound
  toward `(accepted: wait-and-replan)` and the plan's effective
  coverage degrades. This is the `RSK-019` cross-cutting risk.
- **Plan is v1, not v1.1 or v2.** Over-count deferred per D-013
  (15-25 action target); any risk not addressed by an action at v1
  is not necessarily absent in scope, only in specification.
