---
session: 003
title: Decisions — Session 003
date: 2026-04-24
status: complete
---

# Decisions — Session 003

Each decision is traceable to the synthesis in `01-deliberation.md`
and to the raw perspective files cited inline. Triggers per MAD v4
§Trigger-Coverage Annotation Schema. This session is ≥ 006; the
schema applies. No decision in this session carries a `d023_*`
trigger (none modify `methodology-kernel.md`, none create or revise
`multi-agent-deliberation.md`, none touch `validation-approach.md`
Tier-2 content, none assert a change in OI-004 state). Non-Claude
participation (01D Outsider) was invoked at operator discretion per
MAD v4 §Recommended clause; it is not required on any decision
below.

## D-021: system-model v2 shape

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** d016_3: shape question produced genuine
disagreement across 4 perspectives — subsumption-with-file-
preservation (01A + 01D) vs. parallel-retention (01B +
01C-de-facto); 01C additionally declined to propose a count and
preserved view-catalogue-inflation skepticism. 4-of-4 surfaced
alternatives on whether silence/evidence and external-actor are
dedicated views, distributed, or attribute-level. d016_4: shape is
load-bearing for every Session 004+ reproduction of downstream
artefacts; the shape decision this session constrains all v1.1 work
Session 004+ will perform.

**Decision:** `system-model.md` v2 is produced with the seven-
section structure adopted from the deliberation synthesis
(`01-deliberation.md` §2):

1. **§1 — Canonical ID registry.** Subsumption of v1's six-section
   type-indexed structure into a compact registry carrying every
   `POP-*`, `INF-*`, `SVC-*`, `DEP-*`, `EXT-*`, `SIL-*` with one-
   line canonical definition + key attributes. ID-of-record.
2. **§2 — V-Chain (per-service dependency view).** One block per
   `SVC-*` showing upstream `INF-*`/`SVC-*`/`DEP-*`/`EXT-*`/
   `ASM-*` and touching `SIL-*`; downstream cohort reach
   annotated; time-to-harm at the weakest cohort annotated.
3. **§3 — V-Cohort (cohort × service view).** Rows `POP-*`
   (especially `POP-08`–`POP-15`); columns consumed services with
   `DEP-*`/`ASM-*`/`SIL-*` annotations and time-to-harm per cell.
   `POP-12` exposed with oxygen-dependent / CPAP-dependent
   subrows per D-024 (not canonical split). `SIL-02`, `SIL-03`,
   `SIL-19`, `SIL-20` appear as cohort-shaped silence rows
   alongside `POP-*` entries (01B discipline).
4. **§4 — V-External (external-actor view).** Rows `EXT-01`–
   `EXT-03` with explicit `recipient-reliability-basis` (citing
   `ASM-19a`) and `delivery-reliability-basis` (citing `ASM-19b`)
   columns; `fallback-if-fails` column; cross-reference between
   `ASM-19a`/`ASM-19b` enforced per D-023 + §5.8.
5. **§5 — Coverage audit.** Mechanical cross-reference block
   asserting every registry ID appears in ≥1 view (or is flagged
   catalogue-only) and every view row resolves to a registry ID.
6. **§6 — v1.1 implications forward-list.** Names `RSK-014`,
   `RSK-019`, `ACT-005`, `RSK-015`, `RSK-008` (and contingent
   `RSK-004`) as Session 004+ candidate revisions per D-026.
7. **§7 — Honest limits and anti-laundering record.** Records the
   Zachman / EA-view-pattern resemblance per Q7; preserves the
   `ASM-20` laundering flag on any clinical time-to-harm claim;
   names the 4-of-4 surveyed-declined frames; records 01C's load-
   bearing test for future view additions (*"which Session 002+
   re-derivation instance is this view closing?"*).

Settlement-local topology is **not** a fourth view. D-006 (settle-
ment-as-attribute) is not reversed; settlement remains a registry-
level attribute.

**Why:** Three-view shape with canonical registry is the narrowest
4-perspective convergence window (V-Chain unanimous; V-Cohort
3-of-4 + 01C-reader-task-iii; V-External 3-of-4 with 01C preferring
attribute-exposure which is functionally the same structure). The
subsumption-with-preserved-v1-file form addresses 01B's list-shape
concern via the separately-preserved v1 file rather than parallel
retention inside v2 (addresses 01A's drift concern). The external-
actor view is kept separate rather than folded into an evidence/
silence index to force the `ASM-19` split structural visibility
per D-018 + 01B [`01B`, Q3].

**Rejected alternatives:**

- **Four-view shape with dedicated evidence/silence view** (01A's
  §D). Rejected: 2-of-4 preferred distributed silences inline in
  the views touching affected elements (01B + 01C + partially 01D
  who combined external+silence). A dedicated silence view risks
  *"making silences browsable-but-marginal rather than co-located
  with what they silence"* [`01C`, Q1].
- **Four-view shape with settlement-local topology** (01C reader-
  task ii preserved from Session 001 §5.1 shape). Rejected:
  D-006 not reversed; Session 002 re-derivation evidence does not
  concentrate on settlement-level reasoning (the 23 instances were
  dominated by chain-walking and cohort-service lookup per 01A
  [`01A`, Q1]). Preserved as registry-level attribute.
- **Parallel retention: v1 flat index alongside v2 as base layer**
  (01B's non-negotiable position). Adopted in spirit (v1 preserved
  verbatim as `system-model-v1.md`) but not in form (v2's §1
  registry is a distilled subsumption, not a copy). The list-shape
  information 01B cites is recoverable from the preserved v1 file.
- **Replacement-only: v2 supersedes v1 with no preservation**.
  Rejected per D-025 (supersession-chain discipline).
- **01D supplementary derivation-index alternative.** Rejected: the
  brief called for `system-model.md` v2, not a new supplementary
  artefact. Preserved as §5.7 first-class minority with activation
  warrant.

## D-022: ID discipline in v2

**Triggers met:** [d016_3]

**Triggers rationale:** d016_3: alternatives exist (view-scoped
derived IDs like `COH-POP-09` vs inclusion-only citation vs hybrid).
The 4-of-4 convergence against derived IDs is a reasonable-
practitioner convergence across distinct reasoning paths; not a
trivial decision.

**Decision:** v1 IDs (`POP-*`, `INF-*`, `SVC-*`, `DEP-*`, `EXT-*`,
`SIL-*`) remain canonical after v2 adoption. View entries cite
existing IDs; no view-scoped derived IDs are minted. Composite
references such as `[SVC-03 × POP-09]` or chain-walks
`SVC-03 ⇐ INF-04 ⇐ INF-30 ⇐ INF-32` are **reading conveniences,
not IDs** — they do not get independent identity and are not
citable from `risk-register.md` or `response-plan.md`.

Drift prevention is **mechanical, not disciplinary**, realised as
the §5 coverage audit block: asserts every registry ID appears in
at least one view or is flagged `catalogue-only`; every view row
resolves to a registry ID; no orphaned citations.

**Why:** 4-of-4 perspectives [`01A`, Q2; `01B`, Q2; `01C`, Q2;
`01D`, Q2] converge on "canonical registry + inclusion-by-reference
+ mechanical audit". 01C's framing is load-bearing: *"as soon as
the view has its own ID namespace, people start reasoning in view-
IDs and the cross-reference rots"*. Mechanical audit replaces
disciplinary exhortation with checkable invariants that survive
session pressure.

**Rejected alternatives:**

- **View-scoped derived IDs** (e.g., `COH-POP-09`, `CHAIN-SVC-03`).
  Rejected as laundering surface: creates a parallel namespace that
  downstream artefacts will cite inconsistently. [`01C`, Q2 [01C
  laundering framing]]
- **Disciplinary-only drift prevention** (no coverage audit block).
  Rejected: 3 of 4 perspectives propose a mechanical check; 01C
  challenges the Reviser to show derived IDs can be regenerated
  deterministically from registry IDs (they can't, which is why
  no derived IDs).

## D-023: ASM-19 split into recipient-reliability + delivery-reliability

**Triggers met:** [d016_3]

**Triggers rationale:** d016_3: 4-of-4 convergence on splitting, but
falsifier details (ETA slip threshold: 01A's >50% vs 01B's >25%;
review-trigger cadence; whether to require shared falsifier for
decoupling) disagreed. Reasonable-practitioner disagreement on the
split's precise form.

**Decision:** `ASM-19` is split into two rows in
`assumption-ledger.md`:

- **`ASM-19a` recipient-reliability.** Statement: `EXT-01` Nivaro
  central government is a reliable counterparty for *receiving* the
  10-day plan and acknowledging its contents. **Falsifier:** no
  named recipient; acknowledged channel absent; repeated non-
  response inside a stated response window; broadcast-to-ack round-
  trip failure for any named cohort. **Review trigger:** T0+24h;
  on any `EXT-01` communication event.
- **`ASM-19b` delivery-reliability.** Statement: `EXT-01` Nivaro
  central government is a reliable *delivery partner* for actions
  the response plan assigns to central-government execution (fuel
  logistics, sea/air lift, medical evacuation, national-level
  inspection, etc.). **Falsifier:** any committed delivery slips
  stated ETA by **>25%**; any silent cancellation; any actor-side
  dependency (their own logistics, their own crew) fails; first
  attempted delivery regardless of outcome (the first observation
  ends the "unknown" state, per 01C [`01C`, Q3]). **Review
  trigger:** T0+12h baseline; first attempted delivery; every
  `STR-*` review gate.

**Shared discipline (adopted verbatim from 01C [`01C`, Q3]):** the
two rows must cross-reference each other, and any artefact (risk,
action, future plan) that addresses one aspect must explicitly
state its posture toward the other. This is the §5.8 cross-
reference discipline and is preserved as first-class minority for
Session 004+ enforcement.

**v2 exposure:** V-External (v2 §4) carries `ASM-19a` and `ASM-19b`
as distinct attribute columns on `EXT-01` with a `fallback-if-
fails` column.

**Downstream flag (Session 004+):** `RSK-019` currently references
`ASM-19` as a single row and is post-v2-adoption under-specified;
this is Session 004+ v1.1 work per D-026. Not revised this session
per scope.

**Why:** 4-of-4 perspectives support the split per D-018 flag; the
recipient-vs-delivery distinction was originated by 01D in Session
2 [`[archive: provenance/002-session/01D-perspective-adversarial-
skeptic.md]`, Q5d]. The >25% ETA slip threshold is adopted over
>50% on 01B's conservative-threshold grounds: delivery-reliability
is load-bearing for plan actions and looser tolerance permits
`ASM-19b` to survive multiple failed deliveries. The cross-
reference discipline addresses 01C's separable-tractability-
illusion concern.

**Rejected alternatives:**

- **Retain `ASM-19` as a single row.** Rejected per D-018 flag;
  4-of-4 support for the split in this session's deliberation.
- **Split without cross-reference enforcement.** Rejected per 01C's
  load-bearing concern: a Session 004 revision could claim "`ACT-
  xxx` addresses recipient; delivery deferred" as responsible
  scoping rather than as the same political fact unresolved. Cross-
  reference discipline adopted.
- **>50% ETA slip threshold** (01A). Rejected in favour of 01B's
  >25%; the more conservative threshold preserves `ASM-19b`'s
  watchdog role against a pattern of minor slips.

## D-024: POP-12 sub-individuation — decline canonical split

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** d016_3: genuine 2-of-4 vs 2-of-4 perspective
split; cross-family weighting (01C + 01D cross-family convergence
on the laundering argument) was load-bearing. d016_4: cohort-
individuation is load-bearing per Session 001 D-003 and is 01B's
red line; any decision that could be read as weakening cohort
visibility requires explicit rationale.

**Decision:** `POP-12` is NOT split into canonical `POP-12a` /
`POP-12b` cohorts at v2. Instead, v2 §3 (V-Cohort) exposes the
oxygen-dependent and CPAP-dependent sub-structure as subrows under
canonical `POP-12`:

```
POP-12  (canonical, count unknown per ASM-06)
  ↳ oxygen-dependent subgroup  |  hours-band time-to-harm (state descriptor, per ASM-20) |  count unresolved by ASM-06/SIL-*
  ↳ CPAP-dependent subgroup    |  1-3 days band time-to-harm (state descriptor, per ASM-20) |  count unresolved by ASM-06/SIL-*
```

The hours-band vs days-band distinction is recorded as a **state
descriptor** (01C framing, D-017 pattern), explicitly tagged
`ASM-20`-dependent (Session 001 anti-laundering discipline: no
pretrained clinical numbers; qualitative-only). No new `SIL-*` row
(no `SIL-POP-12a-count`, no `SIL-POP-12b-count`) is added; the
existing `ASM-06` assumption still covers sub-cohort size-
distribution silence.

**Why:** 01C's load-bearing laundering test [`01C`, Q4]: *"If the
Reviser can state the split rationale without invoking any clinical
time-constant from pretraining, the split is independent of count
and may proceed. If the rationale is 'oxygen-dependence is more
time-critical than CPAP-dependence,' that rationale uses pretrained
clinical knowledge (ASM-20 territory)."* The split's motivation in
01A and 01B is precisely the clinical time-to-harm differential,
which is `ASM-20` territory. 01D concurs [`01D`, Q4]: *"Without
closure evidence, `POP-12a` and `POP-12b` risk looking more precise
than the workspace permits."* Subrow-treatment preserves the time-
to-harm differentiation 01B values [`01B`, Q4] without importing
the pretrained clinical knowledge 01C flags.

Cross-family weighting is load-bearing here: 01C (Claude-family
Adversarial Skeptic) + 01D (non-Claude Outsider) convergence on the
laundering argument is stronger evidence than within-Claude-family
convergence of 01A + 01B on the structural argument, on a question
where the laundering-vs-structure tradeoff is the central issue.

**Rejected alternatives:**

- **Canonical split into `POP-12a` / `POP-12b` with new count-
  silences `SIL-POP-12a-count` / `SIL-POP-12b-count`** (01A + 01B
  convergent). Rejected on laundering grounds per 01C: the split's
  motivation requires a clinical time-constant that `ASM-20`
  forbids. Preserved as **§5.5 first-class minority** with
  activation warrant (if within 3 sessions count-closure evidence
  arrives OR the subrow-treatment proves unworkable in Session 004+
  risk-register v1.1 work, canonical-split becomes preferred
  direction).
- **Defer `POP-12` treatment entirely to a future session.**
  Rejected: the session's Produce target is v2, and 01B [`01B`, Q4]
  correctly argues that time-to-harm as a structural axis in
  V-Cohort makes the sub-structure unavoidable. Subrow-treatment
  is the minimum honest exposure.
- **Add `RSK-004` dual-window treatment without any v2 sub-
  structure.** Rejected: 01B's argument that the dual-window is
  evidence of mis-shape stands; v2 should expose sub-structure,
  just not as canonical cohorts.

## D-025: Migration and supersession form

**Triggers met:** [d016_3]

**Triggers rationale:** d016_3: three candidate forms in the brief;
4-of-4 perspectives reject form C (git-history-only); forms A and
B are functionally equivalent and chosen over C on explicit
preservation-discipline grounds.

**Decision:** Supersession-chain form (form A / functionally form
B). The migration is executed as follows:

1. `applications/001-disaster-response/system-model.md` (the v1
   file) is **copied verbatim** to
   `applications/001-disaster-response/system-model-v1.md`. The
   copy carries frontmatter amendment:

   ```yaml
   status: superseded
   superseded-by: system-model.md
   superseded-session: 003
   supersession-reason: §5.1 multi-view activation warrant fired at Session 002 close (D-019)
   ```

2. `applications/001-disaster-response/system-model.md` is
   overwritten with v2 content per D-021. Frontmatter:

   ```yaml
   supersedes: system-model-v1.md
   version: 2
   last-revised-session: 003
   validation: workspace-only
   ```
   (other existing frontmatter fields — `title`, `originating_
   session: 001`, `artefact_kind: system-model`, `domain: disaster-
   response`, `engine_version: engine-v7`, `created: 2026-04-24` —
   preserved from v1).

**Why:** 4-of-4 perspectives prefer explicit file-preservation
over git-history-only; 01D's framing: *"Git history alone is too
implicit for a provenance-heavy workspace"* [`01D`, Q5]; 01B's
framing: *"provenance artefacts in this workspace are read as
files, not as git diffs, and the §7 list must be retrievable
without tooling archaeology"* [`01B`, Q5]. 01C's ranking
explicitly prefers form A [`01C`, Q5]. The copy-plus-reference
clause in `specifications/workspace-structure.md` v5 §applications
regularisation and the Session 009 D-054 precedent support this
form (01A [`01A`, Q5]; semantically-equivalent to 01D's "copy-
plus-reference" position).

**Rejected alternatives:**

- **Form C — git-history-only with `last-revised-session: 003` on
  in-place replacement.** Rejected 4-of-4 on preservation-
  discipline grounds.
- **v1 remains canonical; v2 joins as "view document on top".**
  Rejected 01C explicitly [`01C`, Q5]: that would be subsumption
  laundering in reverse. v2 is canonical; v1 is sealed-and-
  referenced.
- **Replacement-only with no v1 file preservation.** Rejected:
  preservation discipline per `methodology-kernel.md` v6
  §Continuity Rules ("Do not overwrite silently. When a
  specification is revised, preserve the prior version and make
  the succession traceable").

## D-026: Downstream v1.1 forward-list for Session 004+

**Triggers met:** [none]

**Triggers rationale:** This is a forwarding record — an
enumeration of consequences of D-021+ for Session 004+ agenda
setting, not a new substantive decision. d016_3 does not apply
(convergent identification across 4 perspectives with no
substantive disagreement on list membership); d016_4 does not apply
(forward-looking agenda item, not this session's load-bearing
choice).

**Decision:** The following v1 rows are flagged for Session 004+
v1.1 revision consideration as consequences of v2 adoption. No
revisions occur this session per scope:

| v1 row | Thinness exposed by v2 |
|---|---|
| `RSK-014` (regional-hospital generator fuel exhaustion) | `cohort_affected` blank at v1; v2 §2 V-Chain enumerates every downstream cohort (`POP-10`, `POP-11`, `POP-09` via `INF-01` dialysis, general hospitalised). Candidate revision: per-downstream sub-risks or explicit downstream-cohort list citing the §2 chain. (4-of-4.) |
| `RSK-019` (`EXT-01` counterparty reliability — cross-cutting) | Post-D-023 split, conflates `ASM-19a` and `ASM-19b`. Candidate revision: split into `RSK-019a` / `RSK-019b` OR carry both premises with paired-row posture per §5.8. (4-of-4.) |
| `ACT-005` (cold-chain POP-13/14/15) | v2 §2 + §3 expose differing time-to-harm per sub-cohort. Candidate revision: per-cohort sub-actions, or explicit time-to-harm triage within the action. (4-of-4.) |
| `RSK-015` (freight-rail-bridge + fibre shared-fate) | v2 §2 makes shared-fate explicit; citation update likely rather than decomposition. (3-of-4; 01A [`01A`, Q6].) |
| `RSK-008` (aged-care cluster welfare) | v2 §3 exposes aged-care cohorts' multi-service dependency. Candidate revision: decompose into per-dependency sub-risks. (3-of-4.) |
| `RSK-004` (`POP-12` power dependency, dual window) | Contingent on §5.5 minority activation; if canonical split is later adopted, `RSK-004` splits too. Not activated this session. (2-of-4; 01A + 01B.) |

**Why:** The multi-view v2 adoption has honest downstream
consequences. Naming them now prevents silent drift between v2's
shape and v1 downstream artefacts. Session 004+ inherits this list
as an agenda-item candidate; Session 004+ is free to order the
revisions or defer specific items.

**Rejected alternatives:**

- **Revise `RSK-*` / `ACT-*` in this session.** Rejected per
  scope (brief §2): Session 003's Produce target is v2 system-
  model + ledger update; downstream revisions are Session 004+
  work. Session 001 D-009 increment-boundary discipline.
- **Leave downstream impact unflagged.** Rejected: silent drift
  risk.

## D-027: §5.2/§5.3/§5.4 warrant-check records

**Triggers met:** [none]

**Triggers rationale:** warrant evaluation is a per-session review
obligation against MAD v4 §Preserve dissent, not a substantive
decision in its own right. The evaluation's output (activate /
preserve-unchanged) is itself a consequence of the evidence
available this session, not a decision made by multi-agent
deliberation this session.

**Decision:** Per `00-assessment.md` §3 evaluation:

- **§5.2 (Operations Planner phased-compartments dissent):** not
  activated this session. Evaluable only in a session that
  re-produces or operationalises the response plan. Preserved
  unchanged.
- **§5.3 (Adversarial Skeptic POP-05 silence-first framing):** not
  activated this session. Evaluable only when POP-05 reconnaissance
  operational evidence accrues. Preserved unchanged.
- **§5.4 (Adversarial Skeptic stabilisation-as-certification):**
  not activated this session. Session 003 did not re-read plan
  T0+10d descriptors as certifying and did not re-introduce numeric
  thresholds. Preserved unchanged.

Four new minorities preserved this session (§5.5 POP-12 canonical
split; §5.6 view-catalogue-inflation watchpoint; §5.7 supplementary
derivation-index alternative; §5.8 ASM-19 shared-counterparty
cross-reference discipline) are logged in `01-deliberation.md` §3
with activation warrants.

**Why:** Warrant-check is per MAD v4 §Preserve dissent; activation
is evidence-bound. This session's evidence does not activate any of
§5.2/§5.3/§5.4; recording the non-activation with reasoning is
honest closure.

**Rejected alternatives:**

- **Skip warrant-check.** Rejected: `00-assessment.md` §6 item 5
  explicitly committed to this review.
- **Activate §5.2 preemptively "just in case".** Rejected: MAD v4
  §Preserve dissent requires activation-warrant evidence; preemptive
  activation would collapse the activation-warrant discipline into
  "activate on a hunch".

## D-028: Validation posture reaffirmation

**Triggers met:** [d016_3]

**Triggers rationale:** d016_3: while the direction is plainly
workspace-only per `CON-02` + Session 001 DEC-07 + Session 002
D-020, the specific reaffirmation language and the continuity claim
are reasonable-disagreement targets — a future session could argue
that the substantive v2 revision (a new model form) warrants a
fresh validation pathway rather than reaffirmation. Recording the
reaffirmation with explicit reasoning closes that ambiguity.

**Decision:** Session 003 v2 artefacts (v2 `system-model.md`; split-
bearing `assumption-ledger.md`) carry frontmatter
`validation: workspace-only` per `methodology-kernel.md` v6 §7 and
`reference-validation.md` v3 §8. This reaffirms Session 001 DEC-07
and Session 002 D-020. No `reference-provisional` claim is made (no
reference case exists for this fictional scenario; v2 is a shape
revision not a new external-facing artefact requiring a new
validation pathway). No `domain-validated` claim is made (no
domain-actor; `CON-02`).

Legitimate close-of-session claims (continuity with Session 002
D-020):

- Internal coherence: v2 registry § cites v1 IDs; views cite
  registry; coverage-audit §5 mechanically verifiable; every v1 ID
  cited in `risk-register.md` / `response-plan.md` resolves post-
  v2.
- Four-link traceability per Session 001 D-010 preserved: risk-
  register rows' `premises` + `silence_dependencies` + `dependency_
  chain` columns all still resolve to v2 registry IDs.
- Cohort-individuation preserved: every `POP-08` through `POP-15`
  appears in v2 §3 V-Cohort; `POP-12` subrow-treatment per D-024.
- Import-hygiene: two new `EXT-SURVEY-*` rows this session
  (`EXT-SURVEY-11`, `EXT-SURVEY-12`) for enterprise-architecture
  multi-view pattern + systems-dependency frames, both explicitly
  engaged and labelled (adopt-with-reason shallowly for the first;
  surveyed-decline for the second).
- Multi-perspective independence satisfied (4 perspectives, distinct
  contexts, parallel-commit for Claude subagents, separate-process
  invocation for Outsider).
- Cross-family signal present (1 non-Claude participant; same
  OpenAI-via-codex-exec transport as Sessions 001 + 002).

Not claimed (reaffirmed from Session 002 D-020):

- Correctness against reality (fictional territory; `CON-01`).
- Completeness (silences remain; v2 exposes them, does not close
  them).
- Plan feasibility (resource estimates absent).
- Priority-order operational correctness.
- Clinical accuracy of time-to-harm windows (`ASM-20`).
- `ASM-19a`/`ASM-19b` reliability across the horizon.
- Stabilisation-as-certified.
- Cross-model deliberation narrowing beyond what 1 non-Claude
  participant can support (MAD v4 §Limitations applies; no OI-004
  narrowing claim).

**Why:** v2 is a shape revision in the same application workspace;
no new validation basis exists (still no domain-actor; still no
reference case for the fictional scenario). Reaffirmation with
explicit list of new claims-not-made is honest closure.

**Rejected alternatives:**

- **Claim `reference-provisional`.** Not applicable (no reference
  case for fictional scenario; per Session 001 DEC-07 + Session 002
  D-020).
- **Claim `domain-validated`.** Explicitly precluded by brief
  (`CON-02`).
- **Claim v2 makes v1.1 downstream work non-required.** Rejected:
  v1 downstream artefacts remain at v1 status; v2 exposes thinness
  but does not fix it (D-026 forwards).

## Decisions not taken (forward to Session 004 or later)

- **`RSK-014`, `RSK-019`, `ACT-005`, `RSK-015`, `RSK-008`, (and
  contingent `RSK-004`) v1.1 revisions.** Per D-026, flagged for
  Session 004+ as candidate risk-register / response-plan
  revisions. Session 004+ may order, defer, or bundle.
- **`POP-12` canonical-split re-consideration.** Per D-024 + §5.5
  minority. Activation warrant: within 3 sessions, count-closure
  evidence OR subrow-treatment unworkability.
- **Derivation-index supplementary artefact.** Per §5.7 minority
  (01D's frame-completion). Activation warrant: within 4 sessions,
  multi-view v2 shape proves costly / view-catalogue inflation /
  reader preference for registry over views.
- **Settlement-local topology view** (01C original §5.1 reader-
  task ii). Carried at registry-attribute level; promotion to a
  standalone view would require Session 004+ evidence that
  settlement-level reasoning concentrates re-derivation cost in
  a way v2 §1 attribute-exposure does not address.
- **Mortuary capacity (`SIL-22`) / governance legitimacy
  (`SIL-23`)** — Session 002 forwarded items; remain decisions not
  taken. `ACT-021` in the plan is the reconnaissance action for
  `SIL-22`; `SIL-23` remains unaddressed.
- **Numeric thresholds for state descriptors** — Session 002
  forwarded as deferred-blocked on domain-review input. No domain-
  review available this application. Remains deferred.

## Summary of non-Claude participation and OI-004 posture

Non-Claude participation: 1 participant (Outsider 01D, OpenAI via
`codex exec`; model id `gpt-5.5` per codex CLI self-report at
`codex-outsider-raw-output.log` line 4). Participation was
recommended-not-required per MAD v4 §When Non-Claude Participation
Is Required (no `d023_*` triggers fired on any decision above).
Invoked at operator discretion per Sessions 001 + 002 precedent.
No OI-004 narrowing claim made (`oi004_qualifying_participants: []`
in `participants.yaml`; this workspace is an external-problem
application distinct from the engine's self-development workspace
where OI-004 tracking lives per MAD v4 §Closure Procedure).
