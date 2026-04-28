---
session: 002
title: Deliberation synthesis — Session 002
date: 2026-04-24
status: complete
synthesiser: "Claude Code orchestrator (claude-opus-4-7), distinct from all four Claude-subagent perspectives (a0541468dc4abb3c6, acaf18d77e63349bf, aabe3ded1ff27501a, a2bc0cfbe37b56418) and distinct from the Outsider codex exec session (019dbe19-44f9-79f3-9ff6-8a58c77a3573)"
participants_family: cross-model
cross_model: true
non_claude_participants: 1
oi004_qualifying_participants: []
---

# Deliberation synthesis — Session 002

## Participants and independence

Five perspectives reasoned independently on the byte-identical shared
brief at `01-brief-shared.md` (§1–§3, §5, §6) with role-specific
stance sections appended (§4, per-perspective). Claude-family
subagents were launched in parallel via the Agent tool; the non-Claude
Outsider was invoked via `codex exec` in a separate process. No
perspective saw another's output before committing its own.

| # | Perspective | Kind | Raw | Stance |
|---|---|---|---|---|
| 01A | Risk Analyst | claude-subagent | `01A-perspective-risk-analyst.md` | Constructive — propose register schema, surface prioritisation method |
| 01B | Operations Planner | claude-subagent | `01B-perspective-operations-planner.md` | Constructive — propose plan shape, action schema, sequencing |
| 01C | Vulnerability Advocate | claude-subagent | `01C-perspective-vulnerability-advocate.md` | Continuity — cohort individuation survives |
| 01D | Adversarial Skeptic | claude-subagent | `01D-perspective-adversarial-skeptic.md` | Continuity — refuse structure; name laundering surfaces |
| 01E | Outsider | non-anthropic-model (OpenAI via codex exec) | `01E-perspective-outsider.md` | Cross-family — frame-check on prioritisation and plan logic |

Synthesiser (this file) is the Claude Code orchestrator, not a
perspective. Per MAD v4 §Synthesis: claims attributing a position to a
perspective cite `[source-file, Q#]`; claims not directly sourced are
marked `[synth]`.

## Convergence vs coverage

### Q1 — Risk register minimum structural sufficiency

**Convergence [4-of-5 propose schema; 1-of-5 refuses on role grounds].**
01A, 01B, 01C, 01E propose schemas; 01D declines (role-consistent)
and enumerates laundering surfaces any schema must survive
[`01D`, Q1]. All five converge that the schema must carry four-link
traceability per D-010 (risk → service/infrastructure → cohort →
assumption/silence).

**Column convergence (across 01A, 01B, 01C, 01E):**

| Column class | Convergence | Rationale |
|---|---|---|
| Stable flat ID (`RSK-NNN` / `RSK-NN` / `RISK-002-###`) | 4-of-4 propose | No semantic prefix; not reshuffled on re-sort [`01D`, Q1 point 6] |
| Cohort-affected (`POP-*` list) | 4-of-4 | Plural, never singular-aggregate [`01B`, Q1] |
| Infrastructure-affected (`INF-*` list) | 4-of-4 | |
| Service-affected (`SVC-*` list) | 4-of-4 | At least one of INF/SVC required |
| Dependency chain (`DEP-*` list) | 3-of-4 (01A, 01B, 01E) | |
| Qualitative time-to-harm window | 4-of-4 | Per DEC-06 and ASM-20 |
| Assumption premises (`ASM-*`/`GIV-*`/`CON-*`) | 4-of-4 | |
| Silence premises / silence-dependency (`SIL-*`) | 4-of-4 | *"an honesty field — the inverse of an impact score"* [`01D`, Q1 accept-list] |
| Risk description (condition → consequence) | 4-of-4 | Not a topic label |
| Status | 3-of-4 (01A, 01B, 01C, 01E endorse; 01D rejects at v1) | 01D: *"'status' implies monitoring implies delivery organisation; this is a planning session"* [`01D`, Q1] |
| Linked actions (`ACT-*`) | 3-of-4 (01A, 01C, 01E) | Bidirectional with plan |

**Convergent rejections (5-of-5 reject):**

- **Numeric likelihood / likelihood×impact scoring.** 01A: *"calibrated
  probabilities… any number would be a fabrication presented as
  precision"* [`01A`, Q1]. 01B: *"false precision under ASM-20"*
  [`01B`, Q1]. 01C: *"A 1–5 × 1–5 matrix invites averaging and
  rank-by-product"* [`01C`, Q1]. 01D: *"A likelihood column has no
  base-rate population in this brief"* [`01D`, Q1 point 2]. 01E: *"no
  numeric likelihood scores… mortality estimates"* [`01E`, Q1].
- **Owner/accountable-party column at v1.** 01A: *"Ownership belongs
  to the response plan"* [`01A`, Q1]. 01B: *"belongs on actions;
  risk-ownership orphans cohorts"* [`01B`, Q1]. 01C: *"premature at
  v1"* [`01C`, Q1]. 01D: *"Owner assignment is fiction…`ASM-19`
  granted `EXT-01` reliable as recipient; writing `owner: EXT-01`
  transmutes reliability-as-recipient into reliability-as-delivery-
  partner"* [`01D`, Q1 point 4]. 01E: *"agency ownership unless the
  plan has a clear local counterpart"* [`01E`, Q1].
- **Residual-risk-post-mitigation column.** 01B, 01C. 01D independently
  rejects "status" column which captures same concern.
- **Numeric time-to-harm values.** 5-of-5 reject; all cite DEC-06 +
  ASM-20.

**Divergence — severity/priority band labels.** 01A proposes a
derived `severity_band` (`critical/high/moderate/watch`) populated
only after Q2's partition-and-sort is applied [`01A`, Q1 field 11].
01B does not carry an explicit severity column. 01C objects to
ordinal severity bands as inviting flattening [`01C`, Q1 leave-out].
01D warns *"the instant you write `impact: high`, you collapse `POP-09`
and `POP-11` and `POP-12` into one ordinal bucket. That is the exact
move `DEC-05` refused"* [`01D`, Q1 point 1]. 01E does not carry a
severity column (uses `short_name` + partition).

**Synthesis position.** Schema adopted: flat `RSK-NNN` ID; columns
`title`, `description` (condition→consequence), `cohort_affected`,
`infrastructure_affected`, `service_affected`, `dependency_chain`,
`time_to_harm_window` (closed qualitative vocabulary), `premises`
(`ASM-*`/`GIV-*`/`CON-*`), `silence_dependencies` (`SIL-*`),
`linked_actions` (bidirectional with plan), `evidence_state`
(`brief-stated` / `inferred` / `assumed` / `silent` — 01D's Q1
accept-list extension), `status` (01D concern preserved: status
limited to `open`/`monitoring`/`mitigated`/`retired`, no
monitoring-infrastructure implied by v1's use), `session_introduced`.
**No severity band column at v1** — 01D's objection held; the
partition-and-sort of Q2 produces ordering without a score-cell,
eliminating the laundering surface 01D named.

**Closed vocabulary for `time_to_harm_window`.** Adopted:
`hours` / `1-3 days` / `3-7 days` / `7-10 days` / `post-horizon` /
`window-unknown`. This is the 01A and 01C variant; rejects 01B's
numerically-styled `<24h`/`24–72h` (01D-vulnerable to
pretrained-number laundering) and 01E's window-label-style
`T0–T0+72h`/`T0+72h–T0+10d` (which conflate sub-window labels with
clinical time-to-harm). `hours`-band entries require a mandatory
visual flag per 01C's Q1 point 4 rationale — the register must not
bury the few hours-band entries in a long list.

### Q2 — Prioritisation method

**Convergence [5-of-5]: partial order, not total order; not
likelihood×impact.** Every perspective rejected both a single-scalar
total order and likelihood×impact scoring. Every perspective endorsed
some form of partial order.

**Convergence [4-of-5 on two-axis structure]:** cohort-fragility axis
× dependency-depth axis kept visible [01A partitions with dependency
tiebreak; 01B two-key hybrid with time-to-harm and dependency-depth;
01C hours-band top tier + dependency-depth within remainder; 01D
two-axes-kept-visible explicitly]. 01E proposes three-key hybrid
(time-to-harm, dependency criticality, uncertainty-with-acute-harm)
[`01E`, Q2].

**Divergence — primary axis.** 01A and 01C treat cohort individuation
/ cohort fragility as the first axis (partition by cohort class, then
sort by time). 01B and 01E treat time-to-harm as the first axis
within the cohort-preserved frame. 01D argues both axes should be
visible without declaring a primary: *"A risk that is high on both
is unambiguously first. A risk that is high on cohort fragility but
low on dependency depth is clearly urgent but not propagating. A risk
that is high on dependency depth but touches only aggregate
populations can be ranked lower"* [`01D`, Q2].

**Distinctive 01D argument.** *"I reject time-ordering by
`POP-*.time_to_harm` as the sole method, because it naturalises the
10-day horizon (`GIV-01`) as the ranking frame. The 10-day horizon
is request-frame, not physics; I flagged this in Session 001. A
dialysis cohort's harm window is physiological, not political.
Ranking risks by their proximity to a political deadline privileges
the deadline"* [`01D`, Q2]. This is a novel frame not surfaced in
the constructive perspectives; the synthesis honours it.

**Synthesis position.** Adopt **two-axis partial order with both axes
visible**: (i) cohort-fragility axis (individuated medical-fragility
cohorts `POP-09` through `POP-15` + `POP-08` at the top as an
unranked cluster [`01C`, Q2]; cohort-silence cohorts `POP-05` and
`POP-02` second; aggregate populations third); (ii) dependency-depth
axis (upstream `DEP-*` positions rank above downstream consequences
within a fragility band). Cells where both axes rank a risk high
become unambiguously first-served. Cells where the two axes disagree
become **explicit two-dimensional cells in the register** — no
collapse to a single score. The plan (Q3) reads both axes; the
register does not publish a `priority` column.

**What this gives up (per 01A, 01B, 01C, 01D consensus):** a clean
single total sort column; operator-dictate of *what to do first if
the boat only fits 20*. 01C: *"that question the plan cannot answer
from the brief's data, and pretending otherwise is the worse
failure"* [`01C`, Q2 partial-order rationale]. Accepted.

### Q3 — Response plan minimum structural sufficiency

**Plan-shape divergence.** 3-of-5 (01A, 01C, 01E) propose concurrent
streams, not phased. 1-of-5 (01B) proposes phased with sub-windows as
compartments + concurrent streams within each phase. 1-of-5 (01D)
declines, warning both phased and service-stream forms launder prior
frameworks (phased launders D-004; service-streams launder UN/IASC
clusters `EXT-SURVEY-02`).

**Stream-family structure (3-of-3 who propose concurrent streams):**
All three concurrent-stream proposals organise by service family,
differing in naming:

- 01A: `STR-water`, `STR-dialysis-continuity`, `STR-power/fuel`,
  `STR-shelter`, `STR-comms/silence-closure`, `STR-aged-care`,
  `STR-neonatal`, `STR-outer-islet-contact`, `STR-salvage/access`,
  `STR-public-information`.
- 01C: Stream C (Cohort-sustaining), Stream I (Infrastructure-
  restoring), Stream S (Service-continuity), Stream P (Population-
  specific non-medical), Stream R (Reconnaissance / silence-closing).
- 01E: medical continuity; potable water; shelter and displacement;
  access and transport; telecommunications and information;
  infrastructure stabilization; unknown-status discovery.

01D's warning (the service-stream shape *is* UN/IASC-cluster-adjacent)
must be answered: the synthesis adopts the streams but grounds them
in the `SVC-*` taxonomy already in the system model, not in the
cluster-approach `EXT-SURVEY-02`. The streams' names derive from the
SVC-list + cohort list the ledger produced; adoption is anchored in
internal artefacts, not in the external framework.

**Convergent action-schema (4-of-5 — 01A, 01B, 01C, 01E):**
- Flat `ACT-NNN` ID.
- `cohort_served` / `target_cohort` (`POP-*` list) — mandatory non-
  empty, settlement-only targets rejected.
- `service_restored` (`SVC-*`) / `infrastructure_touched` (`INF-*`).
- `risks_addressed` (`RSK-*`) — required for four-link traceability.
- `premises` (`ASM-*`).
- `predecessors` / `upstream_actions` (action-DAG).
- `completion_criterion` — observable, not procedural. 01C: *"'Dialysis
  evacuation plan drafted' is not a criterion; 'N patients from POP-09
  receiving dialysis at alternate site, N=?' is"* [`01C`, Q3]. 01B:
  *"No criterion → not admitted"* [`01B`, Q3].
- `actor_class` — role, not named individual. 01D objection
  [`01D`, Q1 point 4] honoured: actor_class does not bind owners.
- `fallback_ref` — 01B proposes; adopted per Q5(d) consensus.

**Action count.** 01B proposes 18–24 [`01B`, Q3]; 01A does not
prescribe; 01C implies similar-order; 01E implies similar. Synthesis
adopts **15–25 actions at v1** as the working range, with over-count
deferred to v1.1.

**Synthesis position on plan shape.** Adopt **concurrent streams,
not phased**, with sub-windows as review gates (Q4) rather than as
compartments. This is 3-of-5 convergence against 01B's compartment
proposal. 01B's compartment argument (*"refusing to reify the joint
forces the reader to re-derive it at run-time"* [`01B`, Q4]) is
preserved as first-class minority §5.2 below.

### Q4 — Sub-windows as operational compartments

**Convergence [4-of-5 against operational compartments; 1-of-5 for].**

- 01A: review gates, not compartments [`01A`, Q4].
- 01B: operational compartments with a single T0+72h review gate
  [`01B`, Q4]. Dissent.
- 01C: review gates + finer sub-windows for action initiation
  [`01C`, Q4]. Proposes T0+0–24h / T0+24–72h / T0+72h–7d / T0+7–10d
  as initiation sub-windows.
- 01D: inert-to-semi-active; trigger-on-information rather than
  trigger-on-time [`01D`, Q4]. Stronger dissent against compartment
  promotion.
- 01E: review gates + planning lenses, not compartments [`01E`, Q4].

**Distinctive 01C contribution.** The finer-grained initiation sub-
windows are an axis different from compartmentalisation: *"An action
initiated in the 0–24h band may run to T0+10d; the band says when it
starts, not where it lives"* [`01C`, Q4]. This preserves cohort-
vigilance on the hours-band risks without reviving D-004's
compartment logic.

**Distinctive 01D contribution.** *"'review at T0+72h' will be read
as 'phase gate at T0+72h', and the acute/stab distinction returns
through the side door. I prefer the plan record a *replan trigger*
rather than a *phase boundary* — the trigger fires when N of the
named silences resolve, not when the clock reaches 72h. Trigger-on-
information is less corruptible than trigger-on-time"* [`01D`, Q4].

**Synthesis position.** Adopt review-gates-not-compartments
(4-of-5). Adopt 01C's finer initiation sub-windows as an action-
schema field (`initiation_band` within {`T0+0-24h`, `T0+24-72h`,
`T0+72h-7d`, `T0+7-10d`, `silence-contingent`}). Adopt 01D's
trigger-on-information as a **secondary** review trigger alongside
the time-keyed T0+72h gate — a silence-resolution count (e.g.,
"when 4 of the 8 `SIL-*` named `Priority` are resolved") fires
replan-triggers in parallel with the clock. 01B's compartment
position preserved as §5.2 first-class minority.

### Q5(a) Cohort prioritisation

**Convergence [5-of-5]: partial order.** No perspective proposed a
total order; no perspective proposed a pure refusal-to-rank.

- 01A: partition-scheme partial order [`01A`, Q5a].
- 01B: partial order via time-to-harm-band equivalence classing
  [`01B`, Q5a].
- 01C: partial order, *"refusal to rank is irresponsible when
  resources are finite"* [`01C`, Q5a].
- 01D: two-axis partial order with both axes visible [`01D`, Q5a].
- 01E: partial order with top band of concurrent risks [`01E`, Q5a].

**Synthesis position.** Adopted per Q2 structure.

### Q5(b) POP-05 outer-islets status

**Divergence [5-way split on settlement-vs-cohort framing].**

| Position | Perspective | Rationale |
|---|---|---|
| First-class settlement | 01A, 01E | [`01A`, Q5b]: count-silence is surfacing, not downgrade. [`01E`, Q5b]: *"Calling it a special-case cohort risks subordinating it"* |
| First-class cohort, not settlement | 01B | [`01B`, Q5b]: *"Promotion to settlement status would require naming infrastructure we lack"* |
| BOTH settlement AND cohort | 01C | [`01C`, Q5b]: dual-treatment preserves access-modality + count-silence |
| First-class silence with probable population | 01D | [`01D`, Q5b]: *"does the session know there are people there to plan for?… structural co-equal status is a claim about capacity-to-plan-for, and the session does not yet have the capacity"* |

**Synthesis position [synth].** Adopt 01C's dual treatment as the
operational shape: `POP-05` is carried as a **first-class cohort in
the risk register AND a first-class settlement in the plan's
access-modality view**. This preserves (i) 01A/01E's concern about
not subordinating outer-islets; (ii) 01B's concern about not
fabricating infrastructure; (iii) 01C's split between the two
axes; (iv) 01D's count-silence-first framing is honoured by making
count-closure the first silence-closing action in the plan's
reconnaissance stream.

01B's specific concern ("settlement status requires infrastructure we
lack") is answered by limiting the settlement treatment to
**access-modality infrastructure** (`SVC-11` sea, `SVC-12` air,
`INF-19` VHF), which the brief does enumerate. Settlement-scale
hospital / treatment-plant / grid infrastructure is absent for
`POP-05` — the model records that absence as silence, not fabricates
it.

01D's "capacity-to-plan-for" concern preserved as §5.3 first-class
minority below.

### Q5(c) Definition of "stabilised" at T0+10d

**Divergence [4-of-5 propose observable criteria; 1-of-5 refuses].**

- 01A: 6 multi-criteria observables grounded in system-model IDs
  [`01A`, Q5c].
- 01B: 8 observable criteria, each converting to a plan completion-
  criterion [`01B`, Q5c].
- 01C: 7 observable criteria: *"'stabilised' is not 'pre-cyclone
  normal'. It is 'no cohort is silently degrading'"* [`01C`, Q5c].
- 01D: *"The plan cannot define 'stabilised' without either (i)
  importing Sphere or equivalent (`EXT-SURVEY-03`), or (ii) the
  perspective itself legislating a definition the brief did not grant…
  The plan can produce a list of state descriptors that will be true
  at T0+10d if the plan executes, and leave the judgement of whether
  those descriptors aggregate to 'stabilised' to `EXT-01` or whoever
  owns that judgement"* [`01D`, Q5c]. Declines observable criteria as
  stabilisation-certifying; accepts state-descriptors framing.
- 01E: detailed observable criteria per cohort, framed as *"managed
  continuity with named residual risks"* [`01E`, Q5c].

**Distinctive 01D argument.** *"I will concretely object if any other
perspective proposes numeric thresholds (e.g., '≥95% of POP-09
receiving dialysis'). Ninety-five is an imported number"* [`01D`,
Q5c]. 01B's criterion 1 explicitly names ≥90% of `POP-09`
[`01B`, Q5c point 1]; 01A does not name a threshold. This is a
specific laundering flag that Session 002's Produce activity must
address.

**Synthesis position [synth].** Adopt 01D's **state-descriptors
framing** as the load-bearing distinction: the plan's T0+10d closure
field is not a "stabilised" predicate; it is a list of observable
state descriptors that will be true at T0+10d if the plan executes.
The descriptors derive from 01A/01B/01C/01E's cohort-specific
criteria, stripped of numeric thresholds per 01D objection. The
predicate "stabilised" is deferred to `EXT-01` / Laurel Delta local
government as counterparty.

Concretely, a plan criterion of the 01B form *"≥ 90% of POP-09"* is
rewritten as *"POP-09 dialysis continuity confirmed for each known
patient via (a) restored INF-04, (b) referral to INF-02, or (c)
documented exception pending escalation"* — no threshold, per-cohort
observability retained.

01D's dissent on criteria *as* stabilisation claims preserved as
§5.4 first-class minority below.

### Q5(d) EXT-01 central-government counterparty

**Convergence [5-of-5]: flag dependency + insist on fallback for
each dependent action.** Every perspective rejected accepting
`ASM-19` as load-bearing without recording dependency and providing
fallback paths.

- 01A: per-action fallback via `premises` column triage [`01A`, Q5d].
- 01B: primary/fallback action refs, contradicts `ASM-19`'s framing
  [`01B`, Q5d].
- 01C: per-stream fallback [`01C`, Q5d].
- 01D: fallback OR accept "wait and replan" as legitimate fallback;
  plan cannot certify `EXT-01` reliability [`01D`, Q5d].
- 01E: accept for planning, flag as assumption, critical-path fallback
  required [`01E`, Q5d].

**Synthesis position [synth].** Adopt flag-and-fallback. Actions
whose `actor_class` is external (`EXT-01` or `EXT-02`) must carry a
`fallback_ref` to an internally-executable alternative OR an
explicit `(accepted: wait-and-replan)` annotation. The assumption
ledger's `ASM-19` is retained as `live` but flagged: a successor
session should consider revising `ASM-19` to explicitly distinguish
reliability-as-recipient from reliability-as-delivery-partner (01D's
distinction [`01D`, Q5d]).

### Q6 — Validation claims at Session 002 close

**Convergence [5-of-5]. Can be claimed:** internal coherence,
traceability-chain closure (D-010), cohort-individuation preservation,
import-hygiene (no silent `EXT-SURVEY-*` application), silence-as-
first-class, cross-reference integrity.

**Convergence [5-of-5]. Cannot be claimed:** correctness against
reality; completeness; plan feasibility; clinical-accuracy of time-
to-harm windows; that `ASM-17` / `ASM-19` will hold in execution;
stabilisation-as-certified; priority-order-as-operationally-correct.

**Distinctive language preserved.** 01D: *"The MAD mechanism filters
certain failure modes; it is not a substitute for the validation
modes it is not… Artefacts that look operationally validated are the
next laundering frontier"* [`01D`, Q6]. 01C: *"A reader who conflates
[process rigor with evidentiary rigor] has mistaken the methodology
for the answer"* [`01C`, Q6]. Both preserved in the close note.

### Q7 — §5.1 first-class minority activation

**Instances named per perspective:**

| Perspective | Count | Instances |
|---|---|---|
| 01A | 5 | Per-settlement cross-section (×2), per-service dependency chain, population-indexed view of silences, infrastructure-by-state cross-section |
| 01B | 4 | Per-cohort phasing view, per-service dependency chain, per-settlement action concentration, silence-to-risk incidence matrix |
| 01C | 5 | Cohort × settlement cross-section, cohort × service dependency chain, silence-adjacency map, access-modality cross-section for POP-05, cohort-sub-structure inside POP-12 |
| 01D | 4 | Settlement-local cross-section for Merrow Port, per-service dependency chain for SVC-03, population-indexed flattening for medical fragility, shared-fate view for INF-14/INF-17 |
| 01E | 5 | Cohort-centered dependency view, access-geography view, shared-fate network view, live-uncertainty-discovery view, outcomes view for stabilisation |

**Total: 23 independent instances across 5 perspectives; 5-of-5 each
above the ≥3 threshold.**

**Common re-derivation pattern (convergence across all 5):**
per-service dependency chain (especially around `SVC-03` haemodialysis
for `POP-09` and around cold-chain `SVC-08` for `POP-13`/`POP-14`/
`POP-15`). This is the cleanest empirical case that the single-model
form required re-derivation.

**Synthesis position [synth].** The §5.1 first-class minority from
Session 001's `[archive: provenance/001-session/01-deliberation.md]`
§5.1 is **ACTIVATED** by this deliberation. The activation warrant
("if Session 002 produces ≥3 risks requiring re-derivation of
dependencies because the single model doesn't expose them, the multi-
view proposal becomes preferred revision direction") is comfortably
cleared on all 5 independent perspectives' reporting.

Session 002 does NOT revise the Session 001 system-model D-001 in
this session — activation names the preferred revision direction;
revision is the next session's work. Session 002 records activation
and forwards the direction to Session 003 for consideration. Session
002's own Produce artefacts (risk-register + response-plan) operate
on the v1 single-document model as-is, acknowledging the re-
derivation cost.

## External inputs surveyed (anti-laundering record)

Frameworks surfaced by perspectives during Session 002; all declined.

| Framework | Surfaced by | Disposition |
|---|---|---|
| ISO-31000 enterprise risk management columns (likelihood / impact / owner / controls / residual) | 01A | Declined; schema uses D-010 four-link instead |
| Bowtie / fault-tree diagrams | 01A | Declined; `DEP-*` edges sufficient |
| ICS/NIMS actor-authority topology | 01B | Declined (already `EXT-SURVEY-01`); no actor-class binding beyond role |
| 5×5 L×I risk matrix | 01B (also 01D as laundering warning) | Declined (already `EXT-SURVEY-06`) |
| Gantt / PERT numeric durations / critical path | 01B | DAG pattern adopted (upstream_actions edges); numeric durations declined |
| Sphere minima | 01B, 01D (warning) | Declined (already `EXT-SURVEY-03`); no numeric thresholds |
| Humanitarian Cluster system service grouping | 01B, 01D (warning) | Streams are `SVC-*`-grounded, not cluster-named (already `EXT-SURVEY-02`) |
| Triage colour-coding | 01D (warning), 01C | Declined (already `EXT-SURVEY-10`); `critical` severity label specifically rejected |
| MoSCoW adjacency | 01D (warning) | Declined (already `EXT-SURVEY-06`) |
| START / JumpSTART clinical triage | 01C | Named-and-declined; cohort partial order derived from DEC-05/DEC-06 |
| Qualitative severity vocabulary (`critical/high/moderate/watch`) | 01A | Declined as schema column per 01D objection — partition-and-sort replaces it |

All recorded in the assumption ledger on Produce as new `EXT-SURVEY-*`
rows where they extend Session 001's record.

## Refusals and honest limits preserved

- **01D refusal to propose schema.** Respected; 01D's laundering-
  surface enumeration is load-bearing content, not a concession-gap.
- **01D refusal to propose plan shape.** Respected.
- **01D objection to observable stabilisation criteria as
  stabilisation-certifying.** Adopted — criteria reframed as state
  descriptors (Q5c synthesis).
- **01C cohort-individuation vigilance.** Adopted at schema
  level (mandatory cohort-affected field with composite-plus-sub-cohort
  rule).
- **01A Q7 limit on stabilised criteria.** *"I may have missed a
  criterion that would only become visible under a per-settlement
  cross-section"* [`01A`, Honest limits]. Preserved.
- **01B Q5d explicit contradiction of ASM-19.** *"ASM-19 should not be
  load-bearing for a 10-day plan — if it fails at T0+36h with no
  pre-written fallback, the plan fails. Session 002 decisions should
  record disagreement with ASM-19's framing"* [`01B`, Q5d]. Decision
  record acknowledges this and carries it forward for Session 003.
- **01C cohort × service dependency sub-view.** Named as §5.1
  re-derivation instance; counts toward activation.
- **01D continuity anti-laundering pressure.** Preserves the
  methodology's cross-boundary anti-laundering discipline.
- **01E cross-family framing check.** No spurious convergence
  detected; cross-family divergences (on axis-primacy in Q2; on
  POP-05 framing in Q5b; on "stabilised" observables in Q5c) are
  genuine.

## Composition fields (for participants.yaml)

- `participants_family: cross-model` (Claude subagents + Outsider).
- `cross_model: true`.
- `non_claude_participants: 1` (Outsider via codex exec,
  provider: openai).
- `oi004_qualifying_participants: []`. Session 002 of an external-
  problem workspace; no OI-004 narrowing claim made (OI-004 closed
  at Session 041 in the self-development source workspace per
  `multi-agent-deliberation.md` v4 §Closure Procedure; forward-
  semantic narrowing claims need to be made in that workspace, not
  this one).

## First-class preserved minorities (per MAD v4 §Preserve dissent)

**§5.1 — Session 001 Adversarial Skeptic single-document-form
dissent — ACTIVATED at Session 002.** Activation via 23 independent
instances across 5 perspectives; cleanest empirical pattern is
per-service dependency chain. Status: activated; multi-view model
form is preferred revision direction for Session 003. Minority text
remains at `[archive: provenance/001-session/01-deliberation.md]`
§5.1.

**§5.2 — Session 002 Operations Planner phased-plan-with-compartments
dissent.** Position: the sub-windows `WIN-acute` / `WIN-stab` should
be treated as operational compartments with a single T0+72h review
gate, not as review gates only. Rationale: *"time-to-harm windows
cluster around 72h — the natural joint between 'kills before we can
think again' and 'can sequence deliberately'. Refusing to reify the
joint forces the reader to re-derive it at run-time, which is the
opposite of operational"* [`01B`, Q4]. Source:
`[01B-perspective-operations-planner.md, Q4]`. **Activation warrant:**
if Session 003 or a later session finds that the review-gates-not-
compartments choice has produced a plan that is read as a flat list
of concurrent actions without observable time-structure, and if the
reader requires the compartment joint to be re-derived at run-time in
≥2 operational-planning instances, 01B's compartment position becomes
the preferred revision direction for the response plan's phase-shape.

**§5.3 — Session 002 Adversarial Skeptic POP-05 silence-first framing
dissent.** Position: POP-05 should not be promoted to settlement
structural status because *"the session does not yet have the
capacity to plan for it… structural co-equal status is a claim about
capacity-to-plan-for"* [`01D`, Q5b]. The synthesis adopted a dual
(settlement + cohort) treatment bounded to access-modality
infrastructure; 01D's concern about capacity-to-plan remains open.
Source: `[01D-perspective-adversarial-skeptic.md, Q5b]`. **Activation
warrant:** if the POP-05 reconnaissance action (`ACT-*` in the
plan's reconnaissance stream) fails to close the count-silence within
the 10-day window, or if the plan's outer-islet access-modality
actions produce ≥2 follow-on silences they cannot themselves close,
01D's silence-first framing becomes preferred revision direction and
the settlement treatment would be demoted to cohort-plus-silence only.

**§5.4 — Session 002 Adversarial Skeptic stabilisation-criteria-as-
certification dissent.** Position: observable criteria for
stabilisation, even stripped of numeric thresholds, remain session-
legislated definitions of a brief-reserved semantic; the plan should
produce *state descriptors that will be true if the plan executes*
and leave stabilisation-predicate certification to `EXT-01`
[`01D`, Q5c]. The synthesis adopted the state-descriptors framing
(Q5c), which substantially vindicates 01D's position, but retains
per-cohort criteria as the plan's T0+10d closure field. **Activation
warrant:** if an external reader of the plan (whether `EXT-01`, a
future session, or an operator) reads the T0+10d state-descriptor
list and interprets it as stabilisation-certifying (i.e., treats plan
completion as having achieved stabilisation), 01D's dissent activates
and the plan should be revised to strip cohort criteria entirely from
the closure field. Alternative activation: if any future session's
revision of the criteria re-introduces numeric thresholds, 01D's
dissent re-activates.

## Limitations

This deliberation was conducted per MAD v4; the Limitations note from
that specification applies and is summarised for the record:

- Four of five perspectives are Claude-family subagents; the Outsider
  is one non-Claude participant from OpenAI via `codex exec`.
  `cross_model: true`; the MAD v4 Limitations note applies: *"A single
  non-Claude participant narrows OI-004 less than its presence
  suggests"* [`multi-agent-deliberation.md` §Limitations]. No OI-004
  narrowing claim is made by this session.
- Shared-brief artefact summaries are byte-identical across all five
  perspectives; none read the full `system-model.md` or
  `assumption-ledger.md` during the independent phase. This preserves
  parallel context but means detail in the full artefacts not carried
  into the summary is invisible to all perspectives equally.
- Three of five perspectives share training lineage with the
  Session 001 perspectives (Vulnerability Advocate and Adversarial
  Skeptic continuity; orchestrator). Shared blind spots continuing
  from Session 001 are not reset by Session 002.
- The synthesis is performed by a single Claude model (the
  orchestrator), which is the single-agent re-entry point the MAD v4
  Limitations note flags. Synthesis conventions (citation, quote-over-
  paraphrase, `[synth]` markers, dissent preservation) reduce but do
  not eliminate this risk.
- The fictional nature of the problem precludes Domain validation;
  workspace validation only applies (CON-02, DEC-07 reaffirmed).
- The Outsider was given a summarised upstream artefact text in its
  prompt; the summary is the same that appears in the committed
  `01-brief-shared.md`. The Outsider's reasoning is therefore on
  identical context to the Claude subagents.

## Proposed decisions forwarded to Decide

- **D-011** — Risk register schema: adopt the converged column set;
  no severity band column at v1; closed-vocabulary time-to-harm;
  mandatory cohort-individuation check (every cohort `POP-09` through
  `POP-15` plus `POP-08` cited in ≥1 risk entry).
- **D-012** — Risk prioritisation method: two-axis partial order
  (cohort fragility × dependency depth) with both axes visible in the
  register; no single-column priority score.
- **D-013** — Response plan shape: concurrent streams, not phased;
  streams grounded in `SVC-*` taxonomy; 01B compartment minority
  preserved as §5.2.
- **D-014** — Sub-windows treatment: review gates, not operational
  compartments; secondary trigger-on-information replan gate per 01D;
  01C's finer initiation-bands adopted as action-schema field.
- **D-015** — Cohort prioritisation: partial order (5-of-5
  convergence), realised via D-012's cohort-fragility axis.
- **D-016** — `POP-05` outer-islets: dual treatment (first-class
  cohort in register + first-class settlement in plan's access-
  modality view, bounded to brief-enumerated infrastructure). 01D
  silence-first framing preserved as §5.3.
- **D-017** — "Stabilised" at T0+10d: state-descriptors framing (01D);
  per-cohort criteria retained as T0+10d closure field without
  numeric thresholds. 01D certification-dissent preserved as §5.4.
- **D-018** — `EXT-01` treatment: flag dependency + fallback required
  on every `ACT-*` whose actor_class is external. `ASM-19`
  recipient-vs-delivery distinction flagged for Session 003.
- **D-019** — §5.1 Session 001 minority activation status: ACTIVATED.
  Multi-view model form is preferred revision direction for Session
  003. Session 002 does not revise D-001.
- **D-020** — Session 002 validation posture: workspace-only
  (reaffirm CON-02 / DEC-07). Artefacts carry `validation:
  workspace-only` in frontmatter; process-rigor-vs-evidentiary-rigor
  distinction explicit in close note.

These proposed decisions are forwarded to the Decide activity
(`02-decisions.md`).
