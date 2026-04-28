---
session: 002
title: Shared brief — Session 002 deliberation
date: 2026-04-24
status: complete
---

# Shared brief — Session 002 deliberation

This is the byte-identical shared content every perspective in the
Session 002 deliberation received. The role-specific stance section
(§4) is appended to this brief per-perspective and is the only section
that varies between briefs. Preserved for auditability per MAD v4
§Stance Briefs.

## §1. Methodology context

You are contributing one perspective to a multi-agent deliberation run
under the **Selvedge engine** at `engine-v7`. The methodology is
specified across `specifications/` (kernel, multi-agent-deliberation,
read-contract, validation-approach, workspace-structure, identity,
reference-validation, engine-manifest). This workspace is an
**external-problem application** of the engine; the application brief
is at `applications/001-disaster-response/brief.md`.

**This is Session 002.** Session 001 produced v1 of the upstream
artefacts (system model + assumption ledger). Session 002 is to produce
v1 of the downstream artefacts (risk register + response plan). Your
perspective's output will be synthesized with four other perspectives'
outputs into a single deliberation record, and the synthesis will be
decided-on in `02-decisions.md`. The decisions will govern what the
session's Produce activity writes to disk.

**Anti-laundering (PROMPT.md).** Do not import ideas from outside the
process. If an insight you surface comes from pretrained corpora
(emergency-management frameworks, disaster-response textbooks,
published plans), introduce it as an explicit *surveyed-but-not-
applied* input. Do not silently absorb it. The assumption ledger has
an `EXT-SURVEY-*` row pattern for surveyed-and-declined frameworks;
Session 002 extends it as needed.

**Cohort individuation is non-negotiable.** Session 001's D-003 (and
01B's *"the averages kill the dialysis patients"* position, preserved
in `[archive: provenance/001-session/01-deliberation.md]` Q3) means
any risk or action that collapses the medical-fragility cohorts into
a single aggregate is a laundering failure, not a simplification.

**§5.1 first-class minority watch.** Session 001 preserved the
Adversarial Skeptic's dissent against the single-document model form
as §5.1 first-class minority
[`[archive: provenance/001-session/01-deliberation.md]` §5.1]. The
activation warrant: *if Session 002 produces ≥3 risks requiring
re-derivation of dependencies because the single model doesn't expose
them, the multi-view proposal becomes preferred revision direction.*
You are asked to notice instances where the model is insufficient for
your work; each such instance counts toward activation.

## §2. Problem statement

**Laurel Delta** (fictional country of **Nivaro**) is 36 hours past
landfall of a late-season cyclone. Three settlements — **Merrow Port**
(~62K, coastal, industrial fishery, 450-bed regional hospital),
**South Latch** (~58K, low-lying agricultural plain, levee-dependent,
primary-care clinic + dialysis centre serving ~1,200), **Kellan Rise**
(~80K, upland, 280-bed secondary hospital) — plus an outer-islet
fishing community (count unknown). Approximately 200,000 affected.

T0 state (per `applications/001-disaster-response/brief.md`):
surge peaked ~2.8m above MHT; lower Merrow Port + two thirds of South
Latch flooded, water receding unevenly; ~18K displaced; grid out in
Merrow Port + South Latch; drinking-water treatment plant in Merrow
Port salt-intruded; Merrow Port regional hospital on generator; Kellan
Rise hospital unaffected; South Latch dialysis centre inaccessible;
highway bridge into Merrow Port intact at 24-tonne rating; sea and
air access degraded. Utility estimates 3–7 days to partial grid
restoration.

Local government has requested a **10-day response-and-stabilisation
plan**. Session 002 produces v1 of the **risk register** and v1 of the
**response plan**.

**Available upstream artefacts.** Reason from the summarised keys
below (byte-identical content is provided to every perspective in this
deliberation, including the Outsider). Do not read the full
`system-model.md` or `assumption-ledger.md` files during the
independent phase — the summarised keys below are the deliberation's
anchor for artefact content. Full artefacts remain on disk for the
synthesis and Produce steps.

### System-model summarised keys

- `POP-01` Merrow Port total ~62K; `POP-02` dormitory cohort ~9K (two
  non-majority languages; T0 occupancy unknown);
  `POP-03` South Latch total ~58K; `POP-04` Kellan Rise total ~80K;
  `POP-05` outer-islet fishing (count unknown); `POP-06` displaced
  ~18K T0.
- `POP-07` aged 70+ ~18K district-wide; `POP-08` institutionally
  housed aged in South Latch clusters (count unknown).
- `POP-09` South Latch dialysis patients ~1,200 (centre inaccessible);
  `POP-10` Merrow Port regional dialysis patients ~220;
  `POP-11` Merrow Port neonatal occupants (count unknown);
  `POP-12` CPAP / home-oxygen (count unknown, sub-cohort of ~5K);
  `POP-13` insulin-dependent (unknown, sub-cohort of ~5K);
  `POP-14` refrigerated-biologic dependents (unknown, sub-cohort);
  `POP-15` other refrigerated-med dependents (unknown);
  `POP-5K-parent` powered-medical aggregate ~5K.
- `POP-16` South Latch dispersed smallholding residents (one-at-a-
  time access under flood); `POP-17` Merrow Port residents not on
  backup-well rotation ~27K (arithmetic).
- `INF-01` Merrow Port regional hospital (on generator; fuel status
  unknown); `INF-02` Kellan Rise hospital (unaffected);
  `INF-03` South Latch primary-care clinic (T0 state unknown);
  `INF-04` South Latch dialysis centre (inaccessible);
  `INF-05` Merrow Port water treatment plant (salt-intruded);
  `INF-06` backup wells (serving ~35K on rotation);
  `INF-07`–`INF-10` four coastal substations (2 degraded, which 2
  unknown); `INF-11` grid (out in Merrow Port + South Latch);
  `INF-12`, `INF-13` two South Latch aged-care clusters (T0 state
  unknown); `INF-14` freight rail bridge (damaged but passable;
  carries fibre trunk `INF-17`); `INF-15` highway bridge (intact,
  24-tonne); `INF-16` sea access (degraded, salvage-required);
  `INF-17` fibre-optic trunk to Kellan Rise (operational state
  unknown); `INF-18` cellular (impaired); `INF-19` outer-islet VHF
  (post-surge operability unknown); `INF-20` air access (degraded,
  runway debris); `INF-21` South Latch levee (state unstated);
  `INF-22` shelter stock (strained); `INF-30` regional hospital
  generator; `INF-31` other district generators (unenumerated);
  `INF-32` generator fuel supply chain (unenumerated).
- `SVC-01` acute hospital care; `SVC-02` primary care;
  `SVC-03` haemodialysis; `SVC-04` potable water;
  `SVC-05` electrical supply; `SVC-06` shelter;
  `SVC-07` inter-settlement road transport; `SVC-08` cold chain;
  `SVC-09` neonatal care; `SVC-10` aged-care continuity;
  `SVC-11` sea transport; `SVC-12` air transport;
  `SVC-13` telecommunications; `SVC-14` salvage;
  `SVC-15` public information / risk communication.
- `DEP-*` key edges: `DEP-08` `INF-14` carries `INF-17` (shared-fate);
  `DEP-09` `INF-04` inaccessibility blocks `POP-09` dialysis;
  `DEP-11` `INF-30` backs up `INF-01`; `DEP-12` `INF-32` supplies
  `INF-30` fuel (inferred); `DEP-13` `SVC-05` powers `SVC-08` cold
  chain (inferred); `DEP-14` `INF-21` levee conditions `POP-03`
  habitability; `DEP-15` `INF-17` supplies `SVC-13` to Kellan Rise
  via `INF-14` carriage.
- `EXT-01` Nivaro central government; `EXT-02` local utility;
  `EXT-03` highland interior.
- `SIL-*` 24 first-class silences (generator fuel status, aged-care
  cluster flood status, outer-islet count, neonatal occupancy,
  informal care-circle topology, mortuary capacity, language-channel
  coverage, etc.).

### Assumption-ledger summarised keys

- `GIV-01` 10-day horizon (brief-requested frame, not physically
  derived).
- `CON-02` validation available: workspace-only (no domain-actor, no
  reference case).
- `ASM-03` ~18K displaced figure stable enough for planning baseline.
- `ASM-08` backup wells potable (not just available).
- `ASM-10` utility 3–7 day restoration is a reported estimate.
- `ASM-15` generator fuel supply chain exists; coupled to `INF-30`.
- `ASM-17` inter-hospital referral (`INF-01`↔`INF-02`) possible via
  road.
- `ASM-18` language-channel coverage for `POP-02` T0 unknown.
- `ASM-19` `EXT-01` central-government reliable counterparty.
- `ASM-20` no pretrained clinical time-to-harm values imported.
- `DEC-05` cohort individuation (named medical-fragility as first-
  class).
- `DEC-06` time-to-harm attribute on `POP-*` with qualitative windows
  only.
- `EXT-SURVEY-01`–`EXT-SURVEY-10` declined frameworks: ICS/NIMS,
  UN/IASC cluster, Sphere, lifelines, SoVI vulnerability indices,
  MoSCoW, RTO/RPO, Maslow, whole-of-community, triage colour-coding.

### Cross-reference conventions

Every risk or action you propose should cite the
`POP-*` / `INF-*` / `SVC-*` / `DEP-*` / `ASM-*` IDs it depends on.
Four-link traceability (per Session 001 D-010): action → risk →
service/infrastructure → assumption.

## §3. Design questions

Each perspective answers Q1–Q7 in order. Your answers will be used in
synthesis; disagreements with other perspectives are preserved, not
resolved by paraphrase.

**Q1 — Risk register minimum structural sufficiency.** What is the
*minimum* structure the v1 risk register must carry to be useful to
the response plan and to future sessions? Name the columns or fields,
the ID convention, the cross-reference conventions, and the rules for
treating time-to-harm windows. Be explicit about what you would leave
out and why.

**Q2 — Prioritisation method.** How should risks be ordered? Options
include: time-ordered by `POP-*.time_to_harm` window; cohort-first
(individuated medical-fragility cohorts before aggregate populations);
dependency-depth (upstream-risks ranked above downstream-consequence
risks); likelihood-×-impact scoring; refusal to rank (list only);
a hybrid. Argue for the method you would adopt and name what it gives
up.

**Q3 — Response plan minimum structural sufficiency.** What is the
*minimum* structure the v1 response plan must carry? Name the shape
(action list, phased plan, concurrent streams, branching plan); how
actions are keyed; how actions reference cohorts and services;
how actions are sequenced within the 10-day horizon; how dependencies
between actions are recorded. Be explicit about what you would leave
out and why.

**Q4 — Sub-windows as operational compartments.** The system model
names `WIN-acute` (T0–T0+72h) and `WIN-stab` (T0+72h–T0+10d) as
orientation labels, not operational compartments (D-004). Should the
response plan treat them as operational compartments (actions assigned
to one window or the other)? As review gates (every action reviewed at
window boundaries)? As inert (ignore)? Something else?

**Q5 — Inherited decisions-not-taken from Session 001.** Session 001
`02-decisions.md` §Decisions-not-taken listed four items. State your
position on each:
- **(a) Cohort prioritisation.** Should v1 impose a total order,
  partial order, or refuse to rank?
- **(b) `POP-05` outer-islets first-class settlement?** Structural
  status on par with Merrow Port / South Latch / Kellan Rise, or
  special-case cohort?
- **(c) Definition of "stabilised" at T0+10d.** What observable
  criteria would make the plan's success condition checkable?
- **(d) `EXT-01` central-government counterparty treatment.**
  Accept reliability, flag dependency, insist on fallback?

**Q6 — Validation claims at Session 002 close.** What can the session
legitimately claim for the v1 risk register + response plan under
workspace validation only (CON-02 / DEC-07 forbid domain-validated
and reference-provisional claims)? What *cannot* be claimed? Be
specific about where process rigor is not evidentiary rigor.

**Q7 — Where the single-model form is distorting your work.** Session
001 preserved the Adversarial Skeptic's §5.1 minority: the single-
document system-model form was a design choice, not a default. As you
worked through Q1–Q6, name any instance where you found yourself
needing a view the single model doesn't expose cleanly (e.g., a
settlement-local cross-section, a per-service dependency chain, a
population-indexed flattening). Each named instance counts toward
§5.1 activation.

## §4. Role-specific stance

*(varies per perspective — appended below this line in each raw output)*

## §5. Response format

Produce a single Markdown document structured as:

```
# Perspective: <role name>
## Methodology context acknowledgement (one sentence)
## Q1. [answer]
## Q2. [answer]
...
## Q7. [answer]
## External inputs surveyed (if any)
## Honest limits
```

Length target: 1,800–3,000 words total (stay under the 6,000-word
soft warning on a per-file basis). Cite `POP-*`, `INF-*`, `SVC-*`,
`DEP-*`, `ASM-*`, etc. IDs where they apply. Quote other perspectives
only if you saw their output (you should not — the deliberation is
independence-preserving).

## §6. Constraint on external imports

Reason primarily from this brief and from the system model +
assumption ledger referenced above. If your reasoning draws on
pretrained disaster-response or emergency-management knowledge, name
the framework in the *External inputs surveyed* section and state
whether you are proposing to apply it or to decline it. Silent
application is the laundering failure this brief exists to prevent.
