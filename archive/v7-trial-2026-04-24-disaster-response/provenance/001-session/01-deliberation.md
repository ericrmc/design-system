---
session: 001
title: Deliberation synthesis — Session 001
date: 2026-04-24
status: complete
synthesiser: "Claude Code orchestrator (claude-opus-4-7), distinct from all four perspective subagents (a5c1bc27ff0684fc8, a3376ba8ddc4c923e, ab7b902a107f1d71c) and distinct from the Outsider codex exec session (019dbdc3-c3c3-7063-8ee0-811abf99a6b2)"
participants_family: cross-model
cross_model: true
non_claude_participants: 1
oi004_qualifying_participants: []
---

# Deliberation synthesis — Session 001

## Participants and independence

Four perspectives reasoned independently on a byte-identical shared
brief (`01-brief-shared.md` §1–§3, §5–§6) with role-specific stance
sections appended (§4, per-perspective). Claude-family subagents were
launched in parallel via the Agent tool; the non-Claude Outsider was
invoked via `codex exec` in a separate process. No perspective saw
another's output before committing its own.

Listed in file-order (A, B, C, D):

- **01A — Systems Modeller** (Claude subagent). Constructive stance;
  proposes scaffolding for the two artefacts.
- **01B — Vulnerability Advocate** (Claude subagent). Vigilant stance;
  surfaces cohorts and dependencies at risk of being flattened.
- **01C — Adversarial Skeptic** (Claude subagent). Challenge stance;
  refuses to propose structure, names laundering and framing risks.
- **01D — Outsider** (non-Claude, OpenAI via codex exec). Cross-family
  stance; frame-check and independent Q1–Q6 answers.

Synthesiser (this file) is the Claude Code orchestrator, which was not
a perspective in the deliberation. Per MAD v4 §Synthesis: citations to
perspective claims use `[source-file, Q#]`; claims not directly sourced
to any raw perspective are marked `[synth]`.

## Convergence vs coverage

The synthesis distinguishes **convergence** (multiple perspectives
independently reached a similar position) from **coverage** (only one
perspective raised a point).

### Q1 — System model: minimum structural sufficiency

**Convergence [4-of-4]: typed/keyed elements with dependencies and T0
state.** All four agree the model should enumerate populations,
infrastructure, and services as keyed entries, with explicit
relationships/dependencies and state at T0.

- 01A proposes `POP-*`, `INF-*`, `SVC-*`, `DEP-*`, `EXT-*` tables
  [`01A-perspective-systems-modeller.md`, Q1].
- 01B insists cohorts appear as named entries with vulnerability
  attributes: *"if Session 002 opens the model and drafts a response
  plan that addresses roads, power, water, and shelter in that order —
  can the model still tell them, unprompted, that there is a dialysis
  cohort approaching a 72-hour threshold and a neonatal ward on
  generator?"* [`01B-perspective-vulnerability-advocate.md`, Q1].
- 01C permits entities/relationships/states as necessary but limits
  inclusion to what the brief explicitly supplies
  [`01C-perspective-adversarial-skeptic.md`, Q1].
- 01D proposes a typed dependency map with categories (places/zones,
  population groups, health services, lifeline infrastructure, access/
  movement, service capacities, governance/information) and
  relationship types (dependency, substitution, capacity/bottleneck)
  [`01D-perspective-outsider.md`, Q1].

**Convergence [3-of-4]: services separated from infrastructure.** 01A,
01B, 01D all argue for a `SVC-*` layer distinct from `INF-*`. The
argument is load-bearing: a service can fail while its infrastructure
stands (hospital with no potable water) or vice versa (backup wells
replacing a treatment plant); the response plan needs both handles.
01C does not oppose but does not endorse — prefers to keep the model
minimal and treats services as derivable from entities + relationships.

**Convergence [4-of-4]: out-of-scope list is required.** All four
converge on an explicit "what is not in the model" section. 01C calls
this an *"explicit 'what is not in the model' register"*
[`01C`, Q1]. 01A calls it *"a list of what v1 does not deliver"*
[`01A`, Q3]. 01B calls for *"silences/unknowns as first-class
entries"* [`01B`, Q1]. 01D endorses *"relevant exclusions from v1,
with reasons"* [`01D`, Q3].

**Coverage — 01B (single-perspective): time-to-harm clocks as a
relationship category.** The Vulnerability Advocate argues each
medical-fragility cohort carries a time constant (dialysis interval,
oxygen cylinder duration, insulin thermal tolerance, generator fuel
runtime) and that omitting this category produces a model Session 002
"will silently rebuild from scratch, probably worse"
[`01B`, Q1]. Not directly endorsed by 01A/01C/01D (though 01A names a
"capacity dimension" column as a softer placeholder and 01D includes
*"time horizons to failure where known or clearly unknown"* as a
system-model element [`01D`, Q1]). **Preserved as a first-class
content requirement** — see D-005 below.

**Divergence — 01C: premise challenge.** The Adversarial Skeptic
challenges the premise that v1 is a single monolithic model:
*"'Minimum structural sufficiency' is already a framing that assumes
a single model with a spine. A v1 that is a single object with a
single taxonomy is itself a design choice"* [`01C`, Q1]. 01C suggests
the session might instead produce three settlement-local models plus
a dependency overlay, or a population-indexed view alongside an
infrastructure-indexed view.

**Synthesis position:** adopt the single-document form (01A, 01B, 01D
converged direction) for v1 on pragmatic grounds — Session 002 needs
one artefact to key against — **while recording 01C's challenge as
§5.1 preserved first-class minority** per MAD v4 §Preserve Dissent.
If Session 002 or subsequent sessions find the single-document form
distorts their work (e.g., producing a risk register that
systematically ignores cross-cutting cohorts in favour of per-
settlement risks), 01C's multi-view proposal is the preferred
revision direction.

### Q2 — Assumption ledger: shape and scope

**Convergence [4-of-4]: table, not list; multi-column schema.** All
four converge on a table with per-row auditability. The column sets
proposed vary in detail but overlap substantially:

| Column (normalised) | Sources |
|---|---|
| `id` | 01A, 01B, 01C, 01D |
| `statement` | 01A, 01B, 01C, 01D |
| `type` (assumption / constraint / given / decision) | 01A, 01B, 01C, 01D |
| `source` (brief-quote / inferred / chosen) | 01A, 01B, 01C, 01D |
| `rationale` or `basis` | 01A, 01B, 01C |
| `model_refs` / `dependents` (what depends on it) | 01A, 01B, 01C, 01D |
| `falsifier` / `falsification condition` | 01A, 01B, 01C, 01D |
| `review_trigger` | 01A, 01B, 01D |
| `status` / `confidence` | 01A, 01B, 01C |

01B is emphatic on two columns: *"The `Dependents` column is the one
I will not negotiate on"* and *"The `Falsification condition` column
forces the session to state what observation would disprove the
assumption — an assumption with no falsification condition is a
belief in costume"* [`01B`, Q2]. 01A concurs:
*"The `model_refs` and `affected_if_false` columns are the load-
bearing ones for auditability"* [`01A`, Q2]. Synthesis adopts both
as required columns; synthesis rationale marked `[synth]`: these are
the columns that convert the ledger from narrative to audit
instrument.

**Convergence [4-of-4]: distinguish assumption / constraint / given /
decision.** All four perspectives separate these four concepts. 01A's
formulation [Q2] and 01C's formulation [Q2] are compatible; 01B and
01D concur. Adopted (D-002).

**Convergence [3-of-4]: assumptions about brief reliability.** Three
perspectives name assumptions the brief asks the session to make that
are not brief-explicit:

- The fibre-trunk service state follows the rail-bridge structural
  state [01A, Q2].
- Backup wells serve *potable* (not just available) water [01B, Q2].
- Generator fuel at Merrow Port regional is sufficient for the 3–7-
  day restoration window [01B, Q2].
- The 1,200 + 220 dialysis cohorts are non-overlapping [01B, Q2].
- Backup-well rotation will continue for the plan horizon [01A, Q2].
- The bridge's 24-tonne rating survives for the 10-day window
  [01A, Q2].

01D concurs on all these classes of assumption without providing the
same list [01D, Q2]. Adopted: the ledger's seed entries draw from
these plus any that the deliberation did not surface.

### Q3 — Upstream-downstream dependency

**Convergence [4-of-4]: four-link traceability chain.** Session 002
must be able to trace any plan action through: action → risk →
affected service → supporting infrastructure → underlying
assumptions. 01A articulates this explicitly
[`01A`, Q3]; 01B agrees with specific cohort non-negotiables
[`01B`, Q3]; 01C adds an exclusion list and statement of
undecided-upstream items [`01C`, Q3]; 01D concurs via its emphasis on
*"stable, meaningful identifiers so downstream sessions can cite them
precisely"* [`01D`, Q3].

**Convergence [4-of-4]: evidentiary tagging on every model claim.**
01C names it *"brief-sourced, inferred, assumed, or decided — no bare
assertions"* [`01C`, Q3]; 01A calls for ledger entries for every
non-brief-quoted assertion [`01A`, Q3]; 01B requires the cohort
enumeration to carry its provenance into Session 002 intact
[`01B`, Q3]; 01D calls for *"provenance tags on values copied from
the brief vs. inferred vs. assumed"* [`01D`, Q3].

**Coverage — 01B (single-perspective): cohort individuation hand-off
must survive.** *"If the hand-off loses the individuation — if
'population cohorts' collapses into 'affected populations: 200K' —
the response plan will optimise for averages, and the averages kill
the dialysis patients"* [`01B`, Q3]. Adopted as a structural
constraint on the v1 system model (D-003 below).

### Q4 — Choice vs given (anti-laundering)

**Convergence [4-of-4]: the 10-day horizon is a request-frame, not a
physical fact.** All four perspectives flag this as requiring explicit
acknowledgement rather than silent absorption.

- 01A: flag for survey *"what does 'stabilised' mean at T0+10d,
  against which the plan is judged?"* [`01A`, Q4].
- 01B: *"time-to-harm clocks for some cohorts (dialysis, cold-chain
  biologics) are shorter than 10 days"* [`01B`, Q4].
- 01C: *"That is a request artefact, not a physics-imposed horizon.
  Dialysis failure is measured in days; fibre-trunk loss is measured
  in months"* [`01C`, Q4].
- 01D: *"the 10-day window was requested; it is not derived"*
  [`01D`, Q4].

**Adopted (D-004):** the ledger records the 10-day horizon as
`type: given-flagged-for-survey` with `source: brief-requested-frame`
rather than as a physical constraint. Sub-windows within the 10-day
frame that reflect different time-to-harm clocks are exposed in the
system model (D-005).

**Convergence [3-of-4]: the settlement-first axis is a choice.** 01A,
01B, 01C flag that using Merrow Port / South Latch / Kellan Rise as
the model's primary index privileges a spatial view over a cohort
view. 01D does not directly address this but includes *"places /
zones"* and *"population groups"* as parallel categories
[`01D`, Q1], implying the settlement partition is not the sole axis.

**Adopted (D-006):** the system model does not use settlements as its
primary index. Populations, infrastructure, and services are keyed
independently; geographic attributes (including settlement) are
recorded as attributes on entries. The ledger records this as a
session decision `DEC-01` with rejected alternative `settlement-
indexed primary axis`.

**Convergence [3-of-4]: the ~5K powered-medical cohort should be
decomposed.** 01A, 01B, and 01D surface that the aggregate bundles
failure profiles with very different time-to-harm constants.

**Adopted (D-007):** the `POP-*` table decomposes the ~5K into named
sub-cohorts where the brief permits (CPAP/home-oxygen; insulin-
dependent; refrigerated-biologic-dependent; other refrigerated-med
dependents). Where the brief does not permit reliable decomposition,
sub-cohorts are recorded as `count: unknown` with an assumption-
ledger entry linking back.

**Additional flags (coverage, not convergence):**

- 01B flags: whether the ~9K seasonal migrant-worker figure represents
  current T0 occupancy or peak-season headcount [`01B`, Q4].
- 01B flags: characterisation of the fishing community as VHF-only
  determines whether it is treated as *reachable-with-effort* or
  *unreachable-by-default* [`01B`, Q4].
- 01C flags: "response-and-stabilisation" as verb pair (vs recovery,
  vs protection-of-vulnerable, vs political-accountability)
  [`01C`, Q4].
- 01C flags: central-government-counterparty reliability presumed
  [`01C`, Q4].
- 01C flags: brief's headline numbers as reported-with-unknown-
  provenance [`01C`, Q4].

**Adopted:** each of these enters the ledger as an accepted input
with `type: given-flagged-for-survey` and a brief rationale. They are
not re-litigated as choices in this session; they are made visible.

### Q5 — Coverage gaps

**Convergence [4-of-4]: structurally missing from any naive v1 —**

| Gap | Sources |
|---|---|
| Fibre trunk as a service vector (not only as an asset) | 01A, 01B, 01C, 01D |
| Generator fuel supply chain for Merrow Port regional hospital | 01A, 01B, 01C, 01D |
| Cold-chain as a service distinct from electricity | 01A, 01B, 01D |
| Migrant-worker language-channel coverage | 01A, 01B, 01C, 01D |
| Aged-care clusters as distinct site-nodes (not just population attribute) | 01A, 01B, 01C |
| Neonatal unit as sub-service of regional hospital | 01A, 01B, 01C |
| Inter-hospital referral capacity edge | 01A, 01B |
| VHF reach between Merrow Port and outer islets | 01A, 01B |
| Levee state (South Latch is "levee-dependent"; T0 state unstated) | 01C |
| Shelter operators as institutional actors | 01C |
| Salvage as pre-service for sea access | 01A |

**Convergence [3-of-4]: unknowns that must be recorded as first-class
rather than omitted —**

- Outer-islet fishing community count (01B, 01C, 01D).
- Neonatal unit occupancy count (01B, 01C).
- Current occupancy of migrant-worker dormitories vs displaced (01B).
- Aged-care cluster flood status (01B, 01C).
- Informal care circles for non-institutionalised over-70s
  (01B explicitly; 01C via governance/vulnerability silence).

**Coverage — single-perspective (01C): brief's silences.** 01C
specifically names: mortuary capacity / mass-casualty handling;
governance legitimacy (language-minority representation, migrant-
worker legal status); mental-health / substance-dependence continuity
(the last also 01B). These are named in the model as explicit
silences rather than imputed.

**Coverage — single-perspective (01B): informal care circles.**
*"Infrastructure-oriented modelling has no handle for 'the neighbour
who usually brings Mrs K her groceries.' This relationship category
is what keeps elderly people alive in the first 72 hours of a flood"*
[`01B`, Q5]. Adopted as a named `silence` entry in the v1 model
(care-circle topology, unmapped).

### Q6 — Validation claims Session 001 can make

**Convergence [4-of-4] on legitimate claims —** internal coherence;
brief-coverage for what is included; auditability via ledger
cross-references; multi-perspective independence satisfied;
structural sufficiency for hand-off to Session 002.

**Convergence [4-of-4] on what cannot be claimed —** correctness
against reality (territory is fictional, no ground truth);
completeness (v1 is not exhaustive); numerical precision (brief-
inherited imprecisions persist); prioritisation correctness (v1 does
not rank); plan sufficiency (deferred to Session 002); domain-expert
endorsement (explicitly precluded by brief).

**Coverage — 01C (single-perspective): process-rigor-is-not-
evidentiary-rigor clause.** *"Passing through nine activities
constitutes external-world validity. Process rigor is not evidentiary
rigor"* [`01C`, Q6]. The close statement incorporates this caveat.
Adopted.

**Coverage — 01C, 01D: deliberation-is-not-diverse caveat.** 01C and
01D both surface that three of four agents are Claude-family and that
none of the four is a Laurel Delta resident or practitioner; "cross-
model" in the sense MAD v4 uses applies but the Outsider-as-single-
non-Claude-participant narrows less than its presence suggests
(see MAD v4 §Limitations explicitly). Adopted into the close note.

## External inputs surveyed (anti-laundering record)

Multiple perspectives surfaced the same public-corpus frameworks as
pretrained material they were surfacing rather than applying:

| Framework | Surfaced by |
|---|---|
| Incident Command System / NIMS / ICS / IMS | 01A, 01C, 01D |
| UN/IASC cluster approach | 01A, 01C, 01D |
| Sphere Handbook minimum standards | 01A, 01C, 01D |
| Lifelines / critical-infrastructure sector taxonomies | 01A, 01C, 01D |
| Hospital emergency preparedness / continuity planning | 01A, 01D |
| Vulnerability indices (SoVI-style composites) | 01B, 01C |
| MoSCoW / RAID-log conventions | 01A |
| Maximum-tolerable-downtime / RTO/RPO | 01A |
| Maslow-style hierarchies of need | 01C |
| Whole-of-community framings | 01C |
| Triage colour-coding | 01B |

**Adopted:** none of these frameworks is applied in the v1 artefacts.
Each is cited in the assumption ledger under
`external-surveyed-not-applied` if any v1 structural choice could
plausibly have come from it, so the audit trail records the choice.

01C predicted: *"I predict the Systems Modeller perspective is at
high risk of importing at least the critical-infrastructure-sector
taxonomy and the cluster-style service partition without surveying"*
[`01C`, External inputs surveyed]. 01A did surface exactly these
frameworks and declined to apply them [`01A`, External inputs
surveyed]. The adversarial prediction was visibly correct about the
gravitational pull and visibly correct that 01A would feel it; 01A's
explicit surveying (not application) confirms the anti-laundering
discipline held.

## Refusals and honest limits preserved

- **01B refusal:** decline to let cohort individuation be laundered
  into risk-register-only concern [`01B`, Honest limits]. Adopted —
  cohorts are first-class in the v1 system model.
- **01C refusal:** decline to treat T0 reported figures as physical
  facts [`01C`, Honest limits]. Adopted — T0 states in the model
  carry an `epistemic source` attribute.
- **01C refusal:** decline to treat "the system model" as singular
  before surveying alternatives [`01C`, Honest limits]. Preserved as
  §5.1 first-class minority with activation warrant.
- **01C refusal:** decline to produce structure [`01C`, Honest
  limits]. Respected — the synthesis does not treat 01C's absence of
  proposed structure as concession.
- **01B, 01C, 01D limits:** model independence is not satisfied by
  process independence when three of four agents share training
  lineage. Session close note makes this explicit.
- **01D limit:** could not access PROMPT.md or OI-015 directly;
  reasoned from the brief's summary. The orchestrator has full access
  to these documents and has not corrected any 01D claim that
  depended on the summary only.
- **01A limit:** reasoned about structure, not content; declined to
  pre-populate the model. That pre-population is the Produce
  activity, which the synthesis hands off to the Produce step
  (v1 artefacts).

## First-class preserved minorities (per MAD v4 §Preserve dissent)

**§5.1 — Adversarial Skeptic single-document-form dissent (Session
001).** Position: a v1 produced as a single monolithic model with a
single taxonomy is a design choice, not a default. Source:
[`01C-perspective-adversarial-skeptic.md`, Q1] and [`01C`, Honest
limits]. Rejected in favour of the single-document convergence of
01A/01B/01D on pragmatic grounds ([synth]: one artefact for
Session 002 to key against). **Activation warrant:** if Session 002
or subsequent sessions find the single-document form systematically
distorts their work (e.g., risk register that ignores cross-cutting
cohorts in favour of per-settlement risks, or response plan that
optimises for infrastructure without adequate population-side
auditing), 01C's multi-view proposal is the preferred revision
direction. Concretely, if Session 002 produces 3 or more risks that
require re-deriving dependencies because the single model doesn't
expose them, this minority activates.

## Limitations

This deliberation was conducted per MAD v4; the Limitations note from
that specification applies and is summarised here for the record:

- Three of four perspectives are Claude-family subagents; the
  Outsider is one non-Claude participant from OpenAI via `codex exec`.
  Cross-model is claimed (`cross_model: true`) but the MAD v4
  Limitations note applies: *"A single non-Claude participant narrows
  OI-004 less than its presence suggests"*
  [`specifications/multi-agent-deliberation.md` §Limitations].
  No OI-004 narrowing claim is made by this session.
- Three of four perspectives share training lineage; shared blind
  spots are likely. The Outsider's surfacing of the same
  disaster-response canon as the Claude subagents (ICS, cluster
  approach, Sphere, etc.) is evidence that these frameworks are
  broadly cross-family-saturated in public corpora, not that any
  specific framework was silently imported by one family.
- Brief-writing has no adversary: all four perspectives received the
  same brief (byte-identical §1–§3, §5–§6) and the orchestrator's
  framing choices propagate into all perspectives identically. The
  shared brief itself was not adversarially reviewed before the
  deliberation ran.
- This synthesis is performed by a single Claude model (the
  orchestrator), which is the single-agent re-entry point the MAD v4
  Limitations note flags. Synthesis conventions (citation, quote-
  over-paraphrase, `[synth]` markers, dissent preservation) reduce
  but do not eliminate this risk.
- The fictional nature of the problem means no external-world
  evidence of any kind is available; Workspace validation only
  applies (Domain validation is precluded by the brief; reference-
  validation substitute does not apply as no documented proven
  solution exists to compare against).

## Proposed decisions forwarded to Decide

- **D-001** — system model structural shape: adopt five keyed-table
  sections (`POP-*`, `INF-*`, `SVC-*`, `DEP-*`, `EXT-*`) plus an
  explicit `SILENCE-*` section for first-class unknowns and an
  explicit "Out of scope for v1" section.
- **D-002** — assumption ledger structural shape: single Markdown
  table with required columns per the convergence list above.
  Distinguish assumption / constraint / given / decision via `type`.
- **D-003** — cohort individuation: named medical-fragility cohorts
  (dialysis, neonatal, CPAP/home-oxygen, insulin-dependent,
  refrigerated-biologic-dependent) are first-class `POP-*` entries.
- **D-004** — time-frame posture: 10-day horizon recorded as
  accepted-brief-frame with explicit sub-windows exposed in the model
  (e.g., 0–72h acute, 72h–10d stabilisation).
- **D-005** — time-to-harm clocks: `POP-*` entries carry a
  `time_to_harm` attribute where the cohort is medical-fragility;
  values from pretrained clinical knowledge are declined at v1;
  attribute is `unknown, to be supplied` where the brief does not
  specify.
- **D-006** — model axis: populations, infrastructure, services are
  keyed independently (not settlement-indexed); settlement is an
  attribute on entries.
- **D-007** — ~5K powered-medical decomposition: sub-cohorts where
  brief permits, with `count: unknown` entries preserved.
- **D-008** — validation posture: workspace validation only;
  close-note explicit about what Session 001 does not claim
  (completeness, correctness, numerical precision, domain-expert
  endorsement, plan sufficiency).
- **D-009** — scope for Session 001: system model + assumption ledger
  only; risk register and response plan deferred to Session 002.
- **D-010** — session 002 hand-off: the v1 artefacts carry stable IDs
  (e.g., `POP-07`, `INF-03`, `ASM-12`), evidentiary tags on every
  non-brief-quoted claim, and explicit silence entries.

These proposed decisions are forwarded to the Decide activity
(`02-decisions.md`).
