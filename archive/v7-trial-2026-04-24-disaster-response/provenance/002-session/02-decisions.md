---
session: 002
title: Decisions — Session 002
date: 2026-04-24
status: complete
---

# Decisions — Session 002

Each decision is traceable to the synthesis in `01-deliberation.md`
and to the raw perspective files cited inline. Triggers per MAD v4
§Trigger-Coverage Annotation Schema. This session is ≥ 006; the
schema applies. No decision in this session carries a `d023_*`
trigger (none modify `methodology-kernel.md`, none create or revise
`multi-agent-deliberation.md`, none touch `validation-approach.md`
Tier-2 content, none assert a change in OI-004 state). Non-Claude
participation was invoked at operator discretion per MAD v4
§Recommended clause; it is not required on any decision below.

## D-011: Risk register schema

**Triggers met:** [d016_3]

**Triggers rationale:** Reasonable practitioners disagree on risk-
register column sets; four constructive perspectives proposed
overlapping-but-distinct schemas and the Adversarial Skeptic declined
to propose while enumerating column-level laundering surfaces. Not
kernel- or spec-modifying; not operator-marked load-bearing.

**Decision:** The v1 risk register at
`applications/001-disaster-response/risk-register.md` carries these
columns per row:

| Column | Purpose |
|---|---|
| `risk_id` | `RSK-NNN` zero-padded flat sequence; never reshuffled |
| `title` | Short noun phrase |
| `description` | One to three sentences in condition→consequence form, naming at least one `POP-*` / `INF-*` / `SVC-*` as the consequence's addressee |
| `cohort_affected` | `POP-*` list; plural-allowed; composite-only (`POP-5K-parent` alone) forbidden when sub-cohorts apply |
| `infrastructure_affected` | `INF-*` list |
| `service_affected` | `SVC-*` list; at least one of INF/SVC required |
| `dependency_chain` | `DEP-*` list; optional but encouraged for multi-edge pathways |
| `time_to_harm_window` | Closed qualitative vocabulary: `hours` / `1-3 days` / `3-7 days` / `7-10 days` / `post-horizon` / `window-unknown`. `hours`-band rows carry mandatory visual flag |
| `premises` | `ASM-*` / `GIV-*` / `CON-*` list |
| `silence_dependencies` | `SIL-*` list; risks reasoning through silences must cite them |
| `evidence_state` | `brief-stated` / `inferred` / `assumed` / `silent` (01D's "honesty field") |
| `linked_actions` | `ACT-*` list; bidirectional with response plan |
| `status` | `open` / `monitoring` / `mitigated` / `retired` |
| `session_introduced` | `002` for every v1 row |

**Mandatory cohort-individuation check (validation-time):** every
cohort `POP-08`, `POP-09`, `POP-10`, `POP-11`, `POP-12`, `POP-13`,
`POP-14`, `POP-15` must appear in at least one `RSK-*` row's
`cohort_affected` cell. This is a workspace-internal mechanical
check; failure is a drafting error to be fixed before session close.

**No severity band column at v1** per 01D objection that any ordinal
severity imports triage colour-coding (`EXT-SURVEY-10`). The two-
axis partial order (D-012) produces ordering without a score cell.

**Why:** 5-of-5 convergence on (a) four-link traceability per D-010;
(b) rejection of numeric likelihood and likelihood×impact scoring;
(c) rejection of owner column at register scope; (d) qualitative-only
time-to-harm per DEC-06 and ASM-20; (e) first-class silence
references. 4-of-5 propose a schema; 1-of-5 (01D) declines and
contributes the laundering-surface enumeration [`01D`, Q1].
Adversarial visibility on the `evidence_state` field and on the
no-severity-column choice is specifically 01D's contribution.

**Rejected alternatives:**

- **Numeric likelihood / likelihood×impact scoring.** Rejected;
  workspace-only validation (CON-02) cannot produce calibrated
  probabilities, and ordinal scores collapse cohort individuation
  [`01D`, Q1].
- **Owner / accountable-party column.** Rejected; ownership belongs
  to the response plan's `ACT-*` rows; risk-owner assignment conflates
  `ASM-19` recipient-reliability with delivery-reliability [`01D`,
  Q1 point 4].
- **Severity band (`critical/high/moderate/watch`).** Rejected at
  column-level on 01D laundering-surface objection even though 01A
  proposed it as partition-derived label.
- **Numeric time-to-harm values.** Rejected per DEC-06 + ASM-20.
- **`<24h`/`24-72h`-style numerically-adjacent qualitative labels.**
  Rejected; vulnerable to pretrained-clinical-number laundering per
  01D [`01D`, Q1 point 3]. 01A/01C-style `hours`/`1-3 days` vocabulary
  adopted instead.

## D-012: Risk prioritisation method

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** d016_3: 5 perspectives proposed variants of
partial-order approaches with genuine disagreement about axis-
primacy. d016_4: prioritisation is load-bearing for the response
plan's action sequencing and for every cohort-scale resource
allocation decision; operator-adjacent load-bearing effect, analogous
to Session 001 D-003.

**Decision:** Risks are ordered by a **two-axis partial order kept
visible**: (i) **cohort-fragility axis** with tiers:

1. Individuated medical-fragility cohorts (`POP-08` institutionally-
   housed aged; `POP-09` South Latch dialysis; `POP-10` Merrow Port
   regional dialysis; `POP-11` neonatal; `POP-12` CPAP/home-oxygen;
   `POP-13` insulin-dependent; `POP-14` refrigerated-biologic;
   `POP-15` other refrigerated-med) — unranked cluster at the top
   per 01C.
2. Cohort-silence cohorts (`POP-05` outer-islets; `POP-02` migrant-
   worker dormitory with unknown T0 occupancy).
3. Aggregate populations (`POP-03`, `POP-04`, `POP-06`, `POP-17`).
4. Infrastructure / service-only risks without a pinned cohort.

(ii) **Dependency-depth axis**: within a cohort-fragility tier,
risks upstream in `DEP-*` chains (whose failure propagates) rank
above downstream-consequence risks at the same tier.

Risks are *not* collapsed to a single priority column. Risks that
rank high on both axes are unambiguously first-served. Risks that
rank high on one axis and low on the other are recorded at two-
dimensional cells; the response plan (D-013) reads both axes.

**Why:** 5-of-5 convergence on partial-order + rejection of
total-order + rejection of likelihood×impact. 01D's distinctive
argument that *"ranking risks by their proximity to a political
deadline privileges the deadline"* [`01D`, Q2] drove the synthesis
decision to keep both axes visible rather than selecting one as
primary. 01C's insistence that the top tier is an unranked cluster
[`01C`, Q5a] preserves cohort individuation against synthetic ordering
between `POP-09` and `POP-11` where data is absent.

**Rejected alternatives:**

- **Total order over all cohorts.** Rejected; forces false precision
  between cohorts with unknown counts (`POP-11`, `POP-12`, etc.)
  [5-of-5].
- **Refusal to rank.** Rejected; leaves ranking decision to operational
  layer where it becomes invisible, and hands the decision to whoever
  executes first (convenience-ranks beating harm-ranks) [`01C`, Q5a].
- **Pure time-to-harm ordering.** Rejected; privileges the political
  10-day horizon `GIV-01` as ranking frame [`01D`, Q2].
- **Single composite priority score (likelihood × impact).** Rejected
  per D-011 reasoning.

## D-013: Response plan shape

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** d016_3: the plan-shape question produced the
session's cleanest divergence — 3 concurrent-streams, 1 phased-
compartments, 1 decline-to-propose. d016_4: plan shape is load-
bearing for every downstream action decision; resolving it the wrong
way would misallocate the session's Produce budget.

**Decision:** The v1 response plan at
`applications/001-disaster-response/response-plan.md` is organised as
**concurrent streams**, not as phased compartments. Streams are
grounded in the `SVC-*` taxonomy already in the system model plus
cohort-facing streams that do not map to a single `SVC-*`:

| Stream | Scope |
|---|---|
| `STR-health-acute` | `SVC-01` acute care, `SVC-09` neonatal |
| `STR-dialysis-continuity` | `SVC-03`, cohorts `POP-09`, `POP-10` |
| `STR-cold-chain-and-medication` | `SVC-08`, cohorts `POP-13`, `POP-14`, `POP-15` |
| `STR-power-and-fuel` | `SVC-05`, `INF-01` generator `INF-30`, `INF-32` fuel chain |
| `STR-water` | `SVC-04`, `INF-05`, `INF-06`, cohort `POP-17` |
| `STR-shelter-and-displacement` | `SVC-06`, cohort `POP-06` |
| `STR-access-and-transport` | `SVC-07`, `SVC-11`, `SVC-12`, `SVC-14`, `INF-15`, `INF-14`, `INF-16`, `INF-20` |
| `STR-communications-and-language` | `SVC-13`, `SVC-15`, cohort `POP-02`, `INF-17`, `INF-18`, `INF-19` |
| `STR-aged-care-and-care-circles` | `SVC-10`, cohorts `POP-07`, `POP-08`, `SIL-19` informal care-circle topology |
| `STR-outer-islet-contact` | cohort `POP-05`, `INF-19`, plus access-modality via `SVC-11`/`SVC-12` |
| `STR-reconnaissance-and-silence-closure` | Actions whose primary output closes a `SIL-*` |

Action count target: **15–25 actions at v1**. Over-count is deferred
to v1.1; under-count is rejected because collapsing cohort-scale
actions hides individuation.

Action schema (each `ACT-NNN` row):

| Field | Purpose |
|---|---|
| `action_id` | `ACT-NNN` flat sequence |
| `stream` | One of the stream IDs above |
| `title` | Short action name |
| `description` | What is done, to what end |
| `cohort_served` | `POP-*` list; settlement-only targets rejected at authoring |
| `service_restored` | `SVC-*` list |
| `infrastructure_touched` | `INF-*` list |
| `risks_addressed` | `RSK-*` list (required; four-link chain) |
| `premises` | `ASM-*` / `GIV-*` list |
| `upstream_actions` | `ACT-*` list forming an acyclic DAG |
| `actor_class` | Role, not named individual; external actors tagged `(external: EXT-01)` etc. |
| `initiation_band` | `T0+0-24h` / `T0+24-72h` / `T0+72h-7d` / `T0+7-10d` / `silence-contingent` (01C's finer sub-windows) |
| `completion_criterion` | Observable post-condition, not procedural |
| `fallback_ref` | Optional `ACT-*` pointer to pre-declared fallback (required when `actor_class` is external) |
| `status` | `planned` / `in-progress` / `completed` / `deferred` |

Streams are grounded in internal `SVC-*` taxonomy per 01D's warning
that service-stream shapes silently launder UN/IASC clusters
(`EXT-SURVEY-02`). The stream *names* derive from the system model
service list + cohort-facing concerns, not from the cluster-approach
catalogue.

**Why:** 3-of-5 propose concurrent streams (01A, 01C, 01E); 1-of-5
(01B) proposes phased compartments; 1-of-5 (01D) declines. The
majority direction is adopted with 01D's anti-laundering guardrails
applied (stream names internal, not framework-named).

**Rejected alternatives:**

- **Phased plan with sub-windows as operational compartments.**
  Rejected on 4-of-5 convergence against compartments; preserved as
  **§5.2 first-class minority** (`01-deliberation.md` §Preserved
  minorities) with activation warrant.
- **Flat action list.** Rejected; hides cross-cutting concurrency and
  action-to-action dependencies.
- **Branching plan with contingencies.** Rejected; workspace-only
  validation cannot credibly specify branch-firing criteria [`01D`,
  Q3 point 4].
- **Service-stream grouping explicitly keyed to UN/IASC cluster
  names.** Rejected per 01D's `EXT-SURVEY-02` laundering warning.

## D-014: Sub-windows treatment

**Triggers met:** [d016_3]

**Triggers rationale:** d016_3: genuine disagreement on whether
sub-windows become operational compartments (01B) or review gates
(01A, 01C, 01D, 01E). Session 001 D-004 established sub-windows as
"orientation labels, not operational compartments" for the model;
this decision extends that to the plan. Not kernel- or spec-
modifying.

**Decision:** `WIN-acute` and `WIN-stab` are **review gates** in the
response plan, not operational compartments. Actions carry an
`initiation_band` field (finer than the two windows) but are not
assigned to windows as compartments. A scheduled review gate fires at
T0+72h to (i) re-check time-to-harm against observed state; (ii)
promote/demote `contingent-on-silence` risks whose silences have
resolved; (iii) confirm `WIN-stab` triggers remain valid. A secondary
**trigger-on-information** replan gate fires in parallel with the
clock: when 4 or more of the 8 named high-priority `SIL-*` have
resolved, an unscheduled replan gate fires. Gates are not phase
boundaries and do not invalidate ongoing actions.

**Why:** 4-of-5 against compartments (01A, 01C, 01D, 01E). 01D's
distinctive trigger-on-information argument [`01D`, Q4] adopted as
the secondary gate mechanism. 01C's finer initiation sub-windows
adopted as the action-schema field that preserves hours-band cohort-
vigilance without compartmentalisation.

**Rejected alternatives:**

- **Hard compartments** (01B position). Preserved as §5.2 first-class
  minority (same as D-013's §5.2 — the two decisions share the
  preservation).
- **Inert sub-windows** (01D's purest stance). Rejected; the review-
  gate role does minimum useful work.
- **Every-action-reviewed-at-every-boundary.** Rejected; decision
  cost per action is high and with one boundary degenerates to a
  single gate [`01B`, Q4].

## D-015: Cohort prioritisation

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** d016_3: Session 001 left this as a decision-
not-taken with clear reasonable disagreement; Session 002's 5
perspectives converged on partial-order but the framing of partial-
order itself admits multiple forms. d016_4: operator-adjacent load-
bearing per Session 001 D-009 split (which handed the question to
Session 002).

**Decision:** Cohort prioritisation is realised as the cohort-
fragility axis of D-012's two-axis partial order. The top tier is an
**unranked cluster** of individuated medical-fragility cohorts per
01C. Partial order between tiers is total; within a tier, ties are
honest and remain tied.

**Why:** 5-of-5 convergence on partial order. 01C's insistence that
the top-tier ordering between `POP-09` (~1,200) and `POP-11`
(unknown count) cannot be honestly ranked from the data [`01C`,
Q5a] is adopted as the reason for the unranked top-tier cluster.

**Rejected alternatives:**

- **Total order.** Rejected per D-012 reasoning.
- **Refusal to rank.** Rejected per 01C: *"refusal to rank is
  irresponsible when resources are finite"* [`01C`, Q5a].

## D-016: POP-05 outer-islets treatment

**Triggers met:** [d016_3]

**Triggers rationale:** d016_3: 5-way disagreement on framing (first-
class settlement / first-class cohort / both / silence-first / first-
class settlement again). The framing question directly affects how
many `RSK-*` and `ACT-*` rows `POP-05` appears in. Not kernel- or
spec-modifying.

**Decision:** `POP-05` is carried as a **first-class cohort in the
risk register** and as a **first-class settlement in the response
plan's access-modality view**, bounded to brief-enumerated access
infrastructure (`SVC-11` sea transport, `SVC-12` air transport,
`INF-19` VHF). Settlement-scale infrastructure absent from the brief
(no hospital, no treatment plant, no grid node) is recorded as silence
per Session 001's `SIL-*` discipline, not fabricated. Count-closure
is the first silence-closing action in `STR-reconnaissance-and-
silence-closure`.

**Why:** 01C's dual-treatment position [`01C`, Q5b] provides the
operational shape that preserves (i) 01A/01E's concern about not
subordinating outer-islets; (ii) 01B's concern about not fabricating
infrastructure; (iii) 01D's silence-first framing on count-closure
priority.

**Rejected alternatives:**

- **First-class settlement only** (01A, 01E). Rejected; 01B's concern
  about fabricating infrastructure holds at general-settlement scope.
- **First-class cohort only** (01B). Rejected; erases access-modality
  distinction.
- **Silence-first only, no settlement treatment** (01D). Preserved as
  §5.3 first-class minority.

## D-017: "Stabilised" at T0+10d

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** d016_3: genuine disagreement on whether the
plan can define stabilised criteria at all (01D refused) vs. the
specific observable criteria to adopt (01A, 01B, 01C, 01E proposed
differing lists). d016_4: the plan's success condition is load-bearing
for any session-close claim about completion; the framing affects
whether Session 002's close claims stabilisation-as-certified.

**Decision:** The plan's T0+10d closure field is a list of
**observable state descriptors** that will be true if the plan
executes, not a set of criteria that certify stabilisation. The
predicate "stabilised" is deferred to `EXT-01` Laurel Delta local
government as the brief's counterparty. State descriptors are derived
per-cohort and per-service from the 01A/01B/01C/01E proposals,
stripped of numeric thresholds per 01D objection.

The plan's T0+10d descriptors are recorded per-stream and per-cohort.
Example form: *"`POP-09` dialysis continuity confirmed for each known
patient via (a) restored `INF-04`, (b) referral to `INF-02`, or (c)
documented exception pending escalation"* — no threshold percentage,
per-cohort observability retained.

**Why:** 01D's state-descriptors framing [`01D`, Q5c] is the load-
bearing anti-laundering distinction. Thresholds like "≥95% of
`POP-09`" are imported numbers; the session has no basis for 95
rather than 90 or 85. The 4-of-5 substantive observable criteria
(01A, 01B, 01C, 01E) are all adoptable under the state-descriptors
framing without needing thresholds.

**Rejected alternatives:**

- **Numeric thresholds** (e.g., ≥95% coverage). Rejected per 01D.
- **No stabilisation criteria at all** (01D's strictest reading).
  Rejected as the plan owner-side interpretation, but preserved as
  §5.4 first-class minority for the certification-dissent specifically.
- **Stabilisation-as-plan-certified** (the framing 01D explicitly
  objects to). Rejected; session close explicitly states the plan
  cannot certify stabilisation.

## D-018: EXT-01 central-government counterparty treatment

**Triggers met:** [d016_3]

**Triggers rationale:** d016_3: 5-of-5 convergence on flag-and-
fallback, but perspectives disagreed on granularity (per-action vs
per-stream vs critical-path-only). Not kernel- or spec-modifying.

**Decision:** Every `ACT-*` row whose `actor_class` is external
(`EXT-01` or `EXT-02`) carries a `fallback_ref` to an internally-
executable alternative OR an explicit `(accepted: wait-and-replan)`
annotation. `ASM-19` (central-government reliability) is retained as
`live` but flagged in the assumption ledger for Session 003
reconsideration: the distinction 01D drew between reliability-as-
recipient and reliability-as-delivery-partner [`01D`, Q5d] is
recorded in the ledger as a new row `ASM-19-flag`.

**Why:** 5-of-5 convergence on flag + fallback. 01B's explicit
contradiction of `ASM-19` framing [`01B`, Q5d] is the concrete basis
for the Session 003 flag.

**Rejected alternatives:**

- **Accept `ASM-19` without fallback.** Rejected; `ASM-19` fail-at-
  T0+36h produces a plan that fails [`01B`, Q5d].
- **Blanket fallback-for-every-action** regardless of actor class.
  Rejected; too coarse and wastes fallback-specification budget on
  actions where local capacity is sole.
- **Per-stream fallback granularity** (01C). Merged into per-action
  granularity; fallback is per-ACT row, which is finer and
  intrinsically per-stream when the stream's actor is uniform.

## D-019: Session 001 §5.1 first-class minority — activation status

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** d016_3: whether the activation warrant fires
is a reasonable-disagreement question (how strictly is "re-derivation"
counted? what counts as an instance?). d016_4: operator load-bearing
for Session 003's agenda — activation names multi-view model as the
preferred revision direction for `applications/001-disaster-response/
system-model.md`.

**Decision:** The §5.1 first-class minority preserved in
`[archive: provenance/001-session/01-deliberation.md]` §5.1 is
**ACTIVATED** by this session. 23 independent instances of
re-derivation cost were named across 5 perspectives
(`01-deliberation.md` Q7 table); each perspective individually
exceeded the ≥3-instance activation warrant. The multi-view model
form is the preferred revision direction for Session 003 or later.

Session 002 does NOT revise `system-model.md` or D-001 in this
session. Activation names the direction; revision is subsequent-
session work. Session 002's Produce artefacts operate on the v1
single-document model as-is, acknowledging re-derivation cost in the
honest-limits note.

**Why:** 5-of-5 perspectives individually met the activation
threshold; cleanest empirical pattern is per-service dependency chain
(especially `SVC-03`/`SVC-08`) which every perspective named
independently.

**Rejected alternatives:**

- **Not activated** (pre-warrant threshold unmet). Rejected; 5-of-5
  above threshold is not a marginal case.
- **Activate AND revise in Session 002.** Rejected; Session 002's
  scope is risk register + response plan per D-009; revising the
  model mid-session collapses the Session-boundary increment
  discipline.
- **Activate AND defer to Session 004+** (skip Session 003). Rejected;
  the activation direction should be the next opportunity, not held.

## D-020: Session 002 validation posture

**Triggers met:** [d016_3]

**Triggers rationale:** d016_3: while the v1 direction is plainly
workspace-only per CON-02 and Session 001 DEC-07, the specific
language claims Session 002 can and cannot make is a reasonable-
disagreement question with 5-of-5 convergence but distinctive framing
contributions.

**Decision:** Session 002 artefacts carry frontmatter
`validation: workspace-only` per `methodology-kernel.md` v6 §7 and
`reference-validation.md` v3 §8. Reaffirms Session 001 DEC-07.

Legitimate close-of-session claims:
- Internal coherence (risk register ↔ system model ↔ assumption
  ledger; response plan ↔ risk register; four-link traceability
  D-010 closes on every row).
- Cohort-individuation preservation (mandatory check per D-011).
- Import-hygiene (no silent `EXT-SURVEY-*` application;
  `01-deliberation.md` External Inputs Surveyed table records the
  session's surveyed-and-declined framework inventory).
- Multi-perspective independence satisfied (5 perspectives, distinct
  contexts, parallel-commit for Claude subagents, separate-process
  invocation for Outsider).
- Cross-family signal present (1 non-Claude participant; same
  OpenAI-via-codex-exec transport as Session 001).
- Auditability via participant manifests + ledger cross-references.

Not claimed:
- Correctness against reality (fictional territory).
- Completeness (`SIL-*` outnumber resolutions; v1 is a floor).
- Plan feasibility (resource estimates absent).
- Priority-order operational correctness (partial order is defensible,
  not validated).
- Clinical accuracy of time-to-harm windows (ASM-20).
- `ASM-17` / `ASM-19` reliability across the horizon.
- Stabilisation-as-certified (D-017; counterparty predicate).
- Numerical precision beyond brief-inherited.
- Process-rigor-equals-evidentiary-rigor [01C, 01D caveats preserved].
- Cross-model deliberation narrowing beyond what 1 non-Claude
  participant can support (MAD v4 §Limitations applies; no OI-004
  narrowing claim).

**Why:** 5-of-5 convergence on these bounds. 01D's "next laundering
frontier" language [`01D`, Q6] preserved verbatim in the close note.

**Rejected alternatives:**

- **Claim reference-provisional.** Not applicable (no reference case
  for fictional scenario).
- **Claim domain-validated.** Explicitly precluded by brief (CON-02).
- **Claim correctness or completeness.** Not supported by the
  validation procedure.

## Decisions not taken (forward to Session 003 or later)

- **`system-model.md` revision toward multi-view form.** D-019
  activated the §5.1 minority but does not revise the model.
  Session 003's agenda should open with this question.
- **`ASM-19` recipient-vs-delivery distinction.** D-018 flagged the
  distinction; Session 003 should either formally split `ASM-19`
  into two rows or adopt 01D's language verbatim.
- **`POP-12` internal CPAP-vs-oxygen individuation.** 01C [`01C`, Q2]
  named the internal split as structurally invisible; Session 003
  could add a `POP-12a` / `POP-12b` sub-individuation if the multi-
  view revision (D-019) exposes it.
- **Numeric thresholds for state descriptors.** Intentionally absent
  at v1 per D-017 + 01D objection. If a future session has access to
  domain-review input (per ASM-20's review trigger), thresholds may
  become nameable.
- **Mortuary capacity / mass-casualty handling (`SIL-22`).** Silence
  surfaced Session 001; not resolved in Session 002. The reconnaissance
  stream may include an action, or it may remain silence.
- **Governance legitimacy (`SIL-23`).** Political layer; Session 002
  did not engage.

## Summary of non-Claude participation and OI-004 posture

Non-Claude participation: 1 participant (Outsider, OpenAI via `codex
exec`; model id `gpt-5.5` per codex CLI self-report; session id
`019dbe19-44f9-79f3-9ff6-8a58c77a3573`). Participation was
recommended-not-required per MAD v4 §When Non-Claude Participation Is
Required (no `d023_*` triggers fire on any decision above). Invoked
at operator discretion per Session 001 precedent. No OI-004 narrowing
claim made (`oi004_qualifying_participants: []` in
`participants.yaml`; this workspace is an external-problem
application distinct from the engine's self-development workspace
where OI-004 tracking lives per MAD v4 §Closure Procedure).
