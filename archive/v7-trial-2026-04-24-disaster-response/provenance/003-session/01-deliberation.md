---
session: 003
title: Deliberation synthesis — Session 003 (system-model v2 multi-view revision)
date: 2026-04-24
status: complete
engine_version: engine-v7
synthesizer: Claude (Claude Code, Opus 4.7, session orchestrator)
participants_family: cross-model
cross_model: true
non_claude_participants: 1
oi004_qualifying_participants: []
---

# Deliberation synthesis — Session 003

Synthesis of four perspective raw outputs against the seven design
questions in `01-brief-shared.md` §3. Citations are per
`specifications/multi-agent-deliberation.md` v4 §Synthesis: `[01A,
Q1]` etc. for raw perspective outputs; `[synth]` for synthesiser-
original framing not directly sourced; `[archive: path]` for prior-
session material.

Perspectives are presented in alphabetical order by role (01A
Reviser, 01B Vulnerability Advocate, 01C Adversarial Skeptic, 01D
Outsider) per MAD v4 §Synthesis order-anchoring.

## 1. Convergence / disagreement map

### Q1 — View count and axes

**Strong convergence (4-of-4):**
- Per-service dependency chain as a view is unanimous.
  `SVC-*`-indexed, showing upstream `INF-*` / `DEP-*` / `EXT-*` /
  `ASM-*` / `SIL-*` and downstream cohort reach. Directly closes
  Session 002's 23 re-derivation instances. Named by 01A as §B
  [`01A`, Q1], 01B as V-Chain [`01B`, Q1], 01C as reader-task (iii)
  [`01C`, Q1], 01D as "dependency-chain index" [`01D`, Q1].
- Cohort × service matrix/view. Rows `POP-*` (especially `POP-08`
  through `POP-15`); columns services or consumed-by. 01A's §C
  [`01A`, Q1], 01B's V-Cohort [`01B`, Q1], 01C's reader-task (i)
  [`01C`, Q1], 01D's matrix [`01D`, Q1].
- v1 IDs remain canonical (see Q2).
- Every v1 ID must survive v2 adoption — either in a preserved
  registry section within v2 or in a recoverable v1 artefact.
- Settlement-local topology **as a view** is not warranted by
  Session 002 evidence. D-006 (settlement-as-attribute) is not
  reversed. 01A rejects outright [`01A`, Q1]; 01B accepts but does
  not push [`01B`, Q1]; 01D defers to concrete evidence [`01D`,
  Q1]; 01C names it as one of three original §5.1 reader-tasks but
  does not insist on it if the evidence doesn't concentrate there
  [`01C`, Q1 + Honest limits].

**Genuine disagreement on v1 retention form:**
- 01A: v1 is **subsumed** as the canonical ID catalogue §A of v2;
  the single-document form is retained *as the catalogue* not
  alongside v2. Rationale: *"a parallel base-plus-views scheme
  doubles the maintenance surface and invites drift between v1
  prose and v2 tables"* [`01A`, Q1].
- 01B: v1 is **non-negotiably retained alongside v2** as a "flat
  index appendix". Rationale: *"the flat §7 SIL-* list is the
  single most compact artefact in the workspace that says 'here is
  everything we do not know about vulnerable populations'. Its
  list-shape is information"* [`01B`, Q5]; the cohort×service view
  distribution of silences would lose that list-shape unless v1
  survives as a unit.
- 01C: v1 is the **type-indexed registry**; views project it; the
  registry must remain canonical; subsumption risks ID drift
  [`01C`, Q1]. Functionally equivalent to 01B's position in effect
  (v1 preserved as recoverable unit) though framed differently.
- 01D: v1's six-section form is **subsumed** as the canonical ID
  register of v2; v1 preserved in the workspace via copy-plus-
  reference [`01D`, Q1 + Q5]. Functionally equivalent to 01A's
  position.

Shape of disagreement: **subsumption-with-file-preservation (01A +
01D) vs. parallel-retention (01B + 01C-de-facto)**. Both sides
preserve v1 as a recoverable file; the difference is whether the
*canonical* registry inside v2 is the SAME text as v1 or a distilled
subsumption.

**Disagreement on silence/evidence treatment:**
- 01A: dedicated §D evidence & silence index in v2. Fourth section
  of v2 in addition to catalogue + 2 views [`01A`, Q1].
- 01B: silences distributed inline inside V-Cohort (`SIL-02`,
  `SIL-03`, `SIL-19`, `SIL-20` as cohort-shaped silences alongside
  `POP-*` rows) [`01B`, Q1].
- 01C: silences distributed inline into whichever view touches
  their affected element; *"a separate silence view risks making
  silences browsable-but-marginal rather than co-located with what
  they silence"* [`01C`, Q1].
- 01D: silences combined with external-actor view into §4 "External
  and silence exposure view" [`01D`, Q1].

Shape of disagreement: all four want silence visibility; split on
whether silences deserve their own section (01A + 01D) vs. inlined
distribution (01B + 01C).

**Disagreement on external-actor treatment:**
- 01A: external-actor information folded into §D evidence/silence
  index, not a standalone view [`01A`, Q1].
- 01B: dedicated V-External view with recipient / delivery sub-
  columns [`01B`, Q1]. Load-bearing for the `ASM-19` split.
- 01C: `EXT-01`/`02`/`03` are three rows; do not need a view;
  attribute-exposure in the registry suffices [`01C`, Q1].
- 01D: combined external + silence exposure view [`01D`, Q1].

**Count convergence window:** 3 views + canonical registry is the
narrowest convergence across 01A + 01B + 01D, and is compatible
with 01C's three-reader-task defence. The three views are the two
strong-convergence views (V-Chain, V-Cohort) plus one "exposure"
view whose internal composition is contested.

### Q2 — ID discipline

**Strong 4-of-4 convergence:**
- v1 IDs (`POP-*`, `INF-*`, `SVC-*`, `DEP-*`, `EXT-*`, `SIL-*`)
  remain canonical after v2 adoption [`01A`, Q2; `01B`, Q2;
  `01C`, Q2; `01D`, Q2].
- **No view-scoped derived IDs** (no `COH-POP-09`, no
  `CHAIN-SVC-03`). Rationale convergent: creates parallel namespace
  that silently diverges. 01C framing: *"as soon as the view has
  its own ID namespace, people start reasoning in view-IDs and the
  cross-reference rots"* [`01C`, Q2]. 01B framing: *"A `POP-09`
  row in V-Cohort is `POP-09`; it is the same entity, shown in a
  different arrangement"* [`01B`, Q2].
- Composite references like `[SVC-03 × POP-09]` or chain-walks
  `SVC-03 ⇐ INF-04 ⇐ INF-30 ⇐ INF-32` are **reading conveniences,
  not IDs** (4-of-4).
- Drift prevention is **mechanical not disciplinary**: a coverage
  audit block asserts every canonical ID appears in at least one
  view (or is flagged catalogue-only), and every ID appearing in
  any view exists in the registry. 01A proposes a linter-style
  check [`01A`, Q2]; 01B proposes a coverage-audit block at the
  top of v2 [`01B`, Q2]; 01D proposes an "ID coverage checklist"
  by family [`01D`, Q2]; 01C: "can any view-scoped ID be
  regenerated deterministically from registry IDs alone?" [`01C`,
  Q2].

No disagreement on Q2.

### Q3 — `ASM-19` split

**Strong 4-of-4 convergence on splitting** per D-018 flag. Both
rows carry independent falsifiers and review triggers. Convergent
falsifier structure:

| Row | Falsifier (synthesis over perspectives) | Review trigger |
|---|---|---|
| `ASM-19a` recipient-reliability | no named recipient; acknowledged channel absent; repeated non-response within stated response window; broadcast-to-ack round-trip fails for any named cohort | T0+24h baseline; on any `EXT-01` communication event |
| `ASM-19b` delivery-reliability | any committed delivery slips stated ETA by >25% (01B) / >50% (01A); any silent cancellation; any actor-side dependency failure (01B); first attempted delivery regardless of outcome (01C) | first attempted delivery (01C); every `STR-*` review gate (01B); T0+12h (01B) |

Numeric ETA threshold differs: 01A says >50% [`01A`, Q3]; 01B says
>25% [`01B`, Q3]. **Synthesis position [synth]:** adopt the more
conservative >25% per 01B, on the grounds that delivery-reliability
is load-bearing for plan actions and looser tolerance would permit
`ASM-19b` to survive multiple failed deliveries.

**01C's load-bearing cross-reference discipline [`01C`, Q3]:**
*"Splitting `ASM-19` into `ASM-19a` and `ASM-19b` creates the
appearance of separable tractability. The two aspects share a
counterparty (`EXT-01`). A Session 004 response-plan revision
could then claim 'ACT-xxx addresses recipient-side; delivery-side
deferred' — and the deferral reads as responsible scoping rather
than as the same political fact unresolved."* Mitigation: the two
rows must cross-reference each other, and any artefact that
addresses one must explicitly state its posture toward the other.
This is adopted verbatim as a condition of the split.

**v2 exposure:** 3-of-4 favour attribute columns on `EXT-01` in
the external-actor treatment (01A, 01B, 01D). 01C concurs if the
cross-reference is enforced [`01C`, Q3]. Adopted.

**`RSK-019` downstream update:** 4-of-4 agree this is Session 004+
v1.1 work, explicitly flagged by every perspective. Not revised
this session per scope.

### Q4 — `POP-12` sub-individuation

**Genuine 2-of-4 vs 2-of-4 split:**

SPLIT now:
- 01A: split into `POP-12a` (oxygen) / `POP-12b` (CPAP) at v2.
  New `SIL-POP-12a-count` / `SIL-POP-12b-count` silences. Rationale:
  the cohort×service matrix exposes the differential time-to-harm;
  dual-window treatment on `RSK-004` is evidence of mis-shape
  [`01A`, Q4].
- 01B: SPLIT aggressively. *"The argument against splitting in
  Session 001 was count-silence. That argument was valid for a flat
  cohort list where every row implied a count. It is not valid in
  V-Cohort where time-to-harm is a structural axis: with time-to-
  harm as an axis, a cohort whose members sit in two wildly
  different bands is structurally mis-shapen."* [`01B`, Q4]

DECLINE split; expose sub-structure without canonical split:
- 01C: *"If the Reviser can state the split rationale without
  invoking any clinical time-constant from pretraining, the split
  is independent of count and may proceed. If the rationale is
  'oxygen-dependence is more time-critical than CPAP-dependence,'
  that rationale uses pretrained clinical knowledge (`ASM-20`
  territory). The correct v2 move is then not to split `POP-12`
  but to expose a time-to-harm-state-descriptor attribute on
  `POP-12`"* [`01C`, Q4].
- 01D: *"I lean against making `POP-12a` and `POP-12b` fully
  canonical at v2 unless the actual v1 `POP-12` row already
  contains enough internal structure to avoid invented counts.
  Session 001 D-007 declined the split on count-silence grounds
  tied to `ASM-06`; that was a good anti-laundering move."* Exposes
  sub-structure as subrows under canonical `POP-12` labelled
  `oxygen-dependent subgroup` / `CPAP-dependent subgroup`, each
  annotated with `count unresolved by ASM-06/SIL-*` [`01D`, Q4].

Cross-family weighting: 01D is the single non-Claude participant;
its position aligns with 01C's (decline canonical split). The
Claude subagents split 1-1 (01A + 01B for split; 01C against).
Cross-family weighting per Session 002 D-017 precedent: cross-
family convergence (01C + 01D) on the laundering argument is
load-bearing on a question where the laundering-vs-structure trade-
off is the central issue.

**Synthesis position [synth]:** decline full canonical split at v2;
adopt 01C / 01D subrow-treatment as the compromise. Rationale: the
`ASM-20` laundering risk 01C named is load-bearing — the split's
motivation is clinical time-to-harm (hours vs days), which is
exactly the pretrained-clinical-knowledge `ASM-20` forbids
importing. Count-silence has not closed. The subrow treatment
preserves time-to-harm differentiation honestly (with state-
descriptor language per 01C + `count unresolved` labels per 01D)
without creating two canonical cohorts whose individuation exceeds
workspace evidence.

01A + 01B's split-now position is preserved as a first-class
minority (§5.1, this session) with activation warrant.

### Q5 — Migration and supersession

**Strong 4-of-4 convergence on rejecting git-history-only (form
C).** 4-of-4 prefer explicit file-preservation chain, with minor
semantic variance between "supersession-chain" (form A per brief)
and "copy-plus-reference per workspace-structure v5" (form B).
Functionally equivalent: v1 retained verbatim at
`applications/001-disaster-response/system-model-v1.md` with
`status: superseded`; v2 takes canonical filename
`applications/001-disaster-response/system-model.md`.

Frontmatter convergence (merging 01A, 01B, 01C, 01D proposals):

```yaml
# v1 frontmatter additions
status: superseded
superseded-by: system-model.md
superseded-session: 003
supersession-reason: §5.1 multi-view activation warrant fired at Session 002 close (D-019)
```

```yaml
# v2 frontmatter additions
supersedes: system-model-v1.md
version: 2
last-revised-session: 003
```

Preserved `validation: workspace-only` (unchanged from v1 per kernel
v6 §7; 01A [`01A`, Q5]).

### Q6 — Risk-plan downstream impact

**Convergent v1.1 candidate list for Session 004+ forwarding:**

| v1 row | v2 exposes what thinness? | Perspective agreement |
|---|---|---|
| `RSK-014` (generator-fuel multi-downstream) | `cohort_affected` currently blank; v2 V-Chain enumerates every downstream cohort | 4-of-4 [`01A`, `01B`, `01C`, `01D`, Q6] |
| `RSK-019` (`EXT-01` cross-cutting) | conflates `ASM-19a`/`ASM-19b` post-split | 4-of-4 |
| `ACT-005` (cold-chain POP-13/14/15) | V-Chain + V-Cohort expose differing time-to-harm per sub-cohort | 4-of-4 |
| `RSK-015` (freight-rail-bridge + fibre shared-fate) | V-Chain makes shared-fate explicit | 3-of-4 (01A, 01B citation-update-only; 01D, 01C flag) |
| `RSK-008` (aged-care cluster welfare) | V-Cohort exposes multi-service dependency | 3-of-4 (01A, 01B, 01D; 01C declines without row text) |
| `RSK-004` (if POP-12 split adopted) | dual-window evidence of mis-shape | 01A + 01B (contingent on split; not activated since split declined) |

All flagged for Session 004+ v1.1; none revised this session per
scope. The aggregate flag is: the multi-view v2 adoption creates
a non-trivial v1.1 queue for Session 004+ — an honest consequence
of the activation direction, not a defect of the revision.

### Q7 — Anti-laundering check

**Strong 4-of-4 surveyed-decline:**
- **UN/IASC clusters** (`EXT-SURVEY-02`): 4-of-4 decline. 01C
  framing specifically: *"A v2 view called 'service view' risks
  re-importing clusters by the side door"* [`01C`, Q7].
- **Lifelines / critical-infrastructure-sector taxonomies**
  (`EXT-SURVEY-04`): 4-of-4 decline. 01B flag: *"if the Reviser
  starts collapsing `INF-*` into sector buckets to make V-Chain
  'cleaner', that's laundering"* [`01B`, Q7].
- **ICS/NIMS** (`EXT-SURVEY-01`): 4-of-4 decline.
- **DoDAF / ArchiMate / causal-loop**: 4-of-4 decline.

**Mixed on TOGAF / Zachman / C4:**
- 01A: ambivalent-leaning-adopt-with-reason. *"Zachman's 'views on
  the same underlying model' pattern is the closest pretrained
  analogue. The warrant for adoption is the §5.1 activation
  evidence, not Zachman's authority. If a future session finds this
  resemblance is doing more taxonomic work than acknowledged, it
  warrants re-examination."* [`01A`, Q7]
- 01B: adopt-with-reason shallowly — pattern only, not taxonomy
  [`01B`, Q7].
- 01C: ambivalent-shading-surveyed-decline. *"Using three views is
  suspiciously Zachman-shaped. My defence of three views is task-
  grounded (each view answers a re-derivation cluster), not
  catalogue-grounded. If the Reviser proposes a 4th view because
  'completeness,' that's Zachman laundering — reject."* [`01C`,
  Q7]
- 01D: *"The biggest laundering risk is the word 'views' itself. It
  can quietly import enterprise-architecture habits."* Declines
  framework adoption; uses "views" as workspace-local label only
  [`01D`, Q7].

**Synthesis position [synth]:** the "views" pattern is acknowledged
as Zachman-adjacent; this acknowledgement is load-bearing content
in v2 and is cited when any fourth view is proposed in a future
session. **Load-bearing test (adopted from 01C):** *"for every view
the Reviser proposes, ask 'which Session 002 re-derivation instance
is this view closing?' If the answer is 'completeness' or 'symmetry'
or 'it seemed natural,' it's laundered."* [`01C`, Q7]. This test is
recorded in v2's honest-limits section as the discipline against
future view-catalogue inflation.

## 2. Session 003 synthesised v2 shape

Combining the strong-convergence elements with the adjudicated
disagreements, the synthesis position [synth] for v2 shape is:

**Three views + canonical registry + preserved v1 file.**

1. **§1 — Canonical ID registry.** Single-document subsumption of
   v1's six-section type-indexed structure, carrying every `POP-*`,
   `INF-*`, `SVC-*`, `DEP-*`, `EXT-*`, `SIL-*` entry with one-line
   canonical definition + key attributes. ID-of-record; every view
   cites from here. v1 file preserved separately at
   `system-model-v1.md` per Q5 decision; §1 of v2 is a distilled
   registry, not a verbatim copy — v1's §7 `SIL-*` flat list shape
   is recoverable from the preserved v1 file, addressing 01B's
   list-shape concern [`01B`, Q5] while avoiding the parallel-
   retention drift 01A flagged [`01A`, Q1].
2. **§2 — V-Chain (per-service dependency).** One block per `SVC-*`
   showing upstream `INF-*` / `SVC-*` / `DEP-*` / `EXT-*` / `ASM-*`
   and touching `SIL-*`; downstream cohort reach annotated; time-
   to-harm at the weakest cohort annotated. Addresses the 23
   Session 002 re-derivation instances directly.
3. **§3 — V-Cohort (cohort × service matrix).** Rows `POP-*`
   (especially `POP-08`–`POP-15`); columns consumed services with
   `DEP-*` / `ASM-*` / `SIL-*` annotations and time-to-harm per
   cell. `POP-12` exposed with oxygen-dependent / CPAP-dependent
   subrows per Q4 synthesis (no canonical split). `SIL-02`,
   `SIL-03`, `SIL-19`, `SIL-20` appear as cohort-shaped silence
   rows inside V-Cohort per 01B [`01B`, Q1].
4. **§4 — V-External (external-actor view).** Rows `EXT-01`–`EXT-
   03` with explicit `recipient-reliability-basis` (citing
   `ASM-19a`) and `delivery-reliability-basis` (citing `ASM-19b`)
   columns; `fallback-if-fails` column; cross-reference between
   `ASM-19a`/`ASM-19b` enforced per 01C cross-reference
   discipline [`01C`, Q3]. Addresses D-018 flag and makes the
   counterparty-reliability distinction structurally visible
   rather than ledger-only.
5. **§5 — Coverage audit.** Mechanical cross-reference block per
   Q2 synthesis. Asserts every registry ID appears in ≥1 view or
   is flagged catalogue-only; every view row resolves to a
   registry ID. Automatic drift-prevention.
6. **§6 — v1.1 implications forward-list.** Per Q6 synthesis,
   names `RSK-014`, `RSK-019`, `ACT-005`, `RSK-015`, `RSK-008`
   (and `RSK-004` contingent on any future `POP-12` canonical
   split) as Session 004+ candidate revisions.
7. **§7 — Honest limits and anti-laundering record.** Names the
   Zachman / EA-view-pattern resemblance explicitly per Q7
   synthesis; records the load-bearing test (01C); preserves the
   `ASM-20` laundering flag on any clinical time-to-harm claim
   (per 01B [`01B`, Q7]); names the 4-of-4 surveyed-declined
   frames.

Settlement-local topology is **not a fourth view** (D-006 not
reversed; Session 002 re-derivation evidence does not concentrate
there). Settlement remains an attribute on registry entries. 01C's
reader-task (ii) for settlement-local topology is addressed at the
registry level (attribute visibility) rather than as a dedicated
view.

## 3. Preserved first-class minorities (per MAD v4 §Preserve dissent)

Continuing from Sessions 001 and 002:

**§5.1 — Session 001 Adversarial Skeptic single-document-form
dissent.** Status: activated at Session 002; adopted as this
session's revision direction; discharged by Session 003 adoption of
multi-view v2. The minority text remains preserved at
`[archive: provenance/001-session/01-deliberation.md]` §5.1 for
provenance continuity.

**§5.2 — Session 002 Operations Planner phased-plan-with-
compartments dissent.** Warrant evaluated at Session 003 open (see
`00-assessment.md` §3): not activated; preserved unchanged;
evaluable only when operational planning is re-executed.

**§5.3 — Session 002 Adversarial Skeptic POP-05 silence-first
framing dissent.** Warrant evaluated: not activated; preserved
unchanged; evaluable only when POP-05 reconnaissance operational
evidence accrues.

**§5.4 — Session 002 Adversarial Skeptic stabilisation-as-
certification dissent.** Warrant evaluated: not activated; Session
003 did not re-read plan T0+10d descriptors as certifying and did
not re-introduce numeric thresholds; preserved unchanged.

New this session:

**§5.5 — Session 003 POP-12 canonical-split minority.** Position
(01A + 01B convergent): `POP-12` should split into `POP-12a`
(oxygen-dependent, hours-band) and `POP-12b` (CPAP-dependent,
days-band) as first-class cohorts at v2, with new count-silences
`SIL-POP-12a-count` and `SIL-POP-12b-count`. Rationale: time-to-
harm as a structural axis in V-Cohort makes a dual-time-window
cohort "structurally mis-shapen"; the dual-window treatment on
`RSK-004` is evidence of the mis-shape. Source:
`[01A, Q4]` + `[01B, Q4]`. Rejected in favour of 01C/01D subrow-
treatment on laundering grounds (`ASM-20` forbids pretrained
clinical time-constants; the split's motivation is clinical time-
to-harm).
**Activation warrant:** if within 3 sessions post-003 (Sessions
004–006) either (a) count-closure evidence arrives for oxygen-
dependent or CPAP-dependent sub-cohorts from within-scenario
sources (registry, pharmacy, supply-chain manifest), OR (b) the
subrow-treatment proves unworkable in Session 004+ risk-register
v1.1 work (e.g., `RSK-004` dual-window cannot be cleanly
decomposed without creating canonical sub-cohorts), the
canonical-split position becomes the preferred revision direction
for a v2.1 update.

**§5.6 — Session 003 Adversarial Skeptic view-catalogue-inflation
watchpoint.** Position (01C): *"My defence of three views is task-
grounded (each view answers a re-derivation cluster), not
catalogue-grounded. If the Reviser proposes a 4th view because
'completeness,' that's Zachman laundering — reject."* Source:
`[01C, Q7]`. Not a dissent per se (01C partially concurs with the
3-view shape; specific decline-to-propose covers the count, not the
shape), but a preservation-of-discipline watchpoint.
**Activation warrant:** if any Session 004+ proposes a fourth or
fifth view whose justification is "completeness" / "symmetry" /
"it seemed natural" rather than a specific Session 003+ re-
derivation cluster, the view-catalogue-inflation concern is
vindicated and the new view must survive 01C's "which specific
re-derivation instance is this view closing?" test or be rejected.

**§5.7 — Session 003 Outsider supplementary derivation-index
alternative.** Position (01D frame-completion contribution): *"A
structurally different alternative would be to leave
`system-model.md` v1 intact and add a separate
`derivation-index.md` keyed to Session 002 decision/re-derivation
instances. That may be cleaner than recasting the whole model as
'views'."* Source: `[01D, Q1]`. Rejected in favour of multi-view
system-model v2 (the session's pre-committed direction per D-019;
the brief explicitly called for `system-model.md` v2 shape rather
than a supplementary artefact).
**Activation warrant:** if within 4 sessions post-003 the multi-
view v2 shape proves more costly to maintain than expected (e.g.,
view-catalogue inflation under §5.6 OR coverage-audit failures
across ≥2 sessions OR readers preferring the registry §1 to the
views), the Outsider's supplementary-index alternative becomes the
preferred direction: revert v2's registry to v1 plus a standalone
`derivation-index.md`.

**§5.8 — Session 003 Vulnerability Advocate + Adversarial Skeptic
ASM-19 shared-counterparty cross-reference discipline.** Position
(01B + 01C convergent): the `ASM-19a` / `ASM-19b` split is
legitimate but creates the appearance of separable tractability;
the two rows must cross-reference each other, and any artefact
(risk, action, future plan) that addresses one aspect must
explicitly state its posture toward the other. Source: `[01B,
Q3]` (in-action fallback-if-fails attribute) + `[01C, Q3]` (shared
falsifier: decoupling evidence).
**Activation warrant:** if any Session 004+ artefact claims
partial-address on `ASM-19a` (or `19b`) without stating its
posture toward the paired row, the shared-counterparty concern is
vindicated and the split is read as providing the separable-
tractability illusion 01C flagged. Remediation: require paired-
row posture statement in every artefact touching either row.

Engine-wide minority count at Session 003 close (external-problem
workspace scope): §5.1 (activated-and-discharged), §5.2, §5.3,
§5.4 carried from Session 002, plus §5.5, §5.6, §5.7, §5.8 added
this session = **8 first-class minorities in this workspace's
deliberation record** (4 inherited + 4 new; §5.1 is in discharged
state).

## 4. Limitations

This deliberation was conducted per MAD v4; the Limitations note
from that specification applies and is summarised for the record:

- Three of four perspectives are Claude-family subagents (01A, 01B,
  01C); the Outsider 01D is one non-Claude participant from OpenAI
  via `codex exec` (same transport as Sessions 001 + 002).
  `cross_model: true`; the MAD v4 Limitations note applies: *"A
  single non-Claude participant narrows OI-004 less than its
  presence suggests"* [`multi-agent-deliberation.md`
  §Limitations]. No OI-004 narrowing claim is made by this session.
- Two of four perspectives (01B Vulnerability Advocate, 01C
  Adversarial Skeptic) share continuity with Sessions 001 + 002.
  Shared reasoning priors across three consecutive sessions are
  real and not fully mitigated by parallel-context brief-
  independence. This is the third consecutive session with the
  same non-Claude transport and the same two continuity roles.
- The Outsider was given a summarised brief (the shared brief plus
  supplementary context summarising v1 artefact shapes) rather
  than the full v1 artefact text. The Outsider's Honest limits
  section flags this explicitly: *"I cannot verify exact v1 row
  wording, exact SIL-* identifiers touching POP-12, or the full
  text of RSK-014, RSK-019, ACT-005, RSK-015, and RSK-008 from
  the brief alone."* [`01D`, Honest limits]. This is the same
  constraint all Claude perspectives operated under (identical
  context); the Outsider's reasoning is on identical context to
  the Claude subagents.
- The synthesis is performed by the session orchestrator (a single
  Claude instance), which is the single-agent re-entry point the
  MAD v4 Limitations note flags. Synthesis conventions (citation,
  `[synth]` markers, quote-over-paraphrase, dissent preservation,
  alphabetical order anchoring) reduce but do not eliminate this
  risk.
- The fictional nature of the problem precludes Domain validation;
  workspace-only validation applies (`CON-02`, Session 001 DEC-07
  reaffirmed).
- Session 001 and Session 002 raw perspective files were not read
  in full this session; synthesis + decision records carried the
  load-bearing claims. No Session 003 decision depends on a raw-
  output claim absent from synthesis or decision records. This is
  declared per `read-contract.md` v4 §6 honest-limits discipline.

## 5. External inputs surveyed this session

Per `specifications/multi-agent-deliberation.md` v4 §6 Stance Briefs
Constraint on external imports and per PROMPT.md anti-silent-import
rule, external frames surfaced via Q7:

| Frame | Source | Disposition |
|---|---|---|
| UN/IASC clusters | `[EXT-SURVEY-02]` at v1 | Surveyed-and-decline (4-of-4); re-confirmed at v2 |
| Lifelines / critical-infrastructure-sector taxonomies | `[EXT-SURVEY-04]` at v1 | Surveyed-and-decline (4-of-4); re-confirmed at v2 |
| ICS/NIMS | `[EXT-SURVEY-01]` at v1 | Surveyed-and-decline (4-of-4); re-confirmed at v2 |
| Sphere Handbook minimum standards | `[EXT-SURVEY-03]` at v1 | Surveyed-and-decline (not engaged at Q7; implicit carry-forward) |
| Critical-infrastructure sector taxonomies | `[EXT-SURVEY-04]` at v1 | Same as Lifelines; see above |
| Vulnerability indices (SoVI-style) | `[EXT-SURVEY-05]` at v1 | Surveyed-and-decline (not engaged; implicit carry-forward) |
| RAID-log / MoSCoW conventions | `[EXT-SURVEY-06]` at v1 | Surveyed-and-decline (not engaged; implicit carry-forward) |
| Maximum-tolerable-downtime / RTO / RPO | `[EXT-SURVEY-07]` at v1 | Surveyed-and-decline (not engaged; implicit carry-forward) |
| Maslow-style hierarchies of need | `[EXT-SURVEY-08]` at v1 | Surveyed-and-decline (not engaged; implicit carry-forward) |
| Whole-of-community framings | `[EXT-SURVEY-09]` at v1 | Surveyed-and-decline (not engaged; implicit carry-forward) |
| Triage colour-coding | `[EXT-SURVEY-10]` at v1 | Surveyed-and-decline (not engaged; implicit carry-forward) |
| TOGAF / Zachman / C4 — multi-view enterprise-architecture pattern | NEW this session; surfaced by 01A, 01B, 01C, 01D at Q7 | **Adopt-with-reason (shallow pattern use only)**. The "views on canonical model" pattern is used in v2 shape; specific view catalogues from these frameworks are not adopted. 01C's load-bearing test (*"which re-derivation instance is this view closing?"*) is recorded in v2 §7 as the discipline against future view-catalogue inflation. New `EXT-SURVEY-11` entry for ledger. |
| DoDAF / ArchiMate / causal-loop | NEW this session; surfaced by 01C, 01D at Q7 | Surveyed-and-decline. New `EXT-SURVEY-12` entry for ledger. |

Ledger update implied: two new `EXT-SURVEY-*` rows (`EXT-SURVEY-11`
enterprise-architecture-multi-view-pattern;
`EXT-SURVEY-12` systems-dependency-modelling-frames) to be added to
`assumption-ledger.md` alongside the `ASM-19` split.

## 6. Proposed decisions forwarded to Decide

The synthesis surfaces the following decisions for recording in
`02-decisions.md`:

- **D-021: system-model v2 shape.** Three views (V-Chain, V-Cohort,
  V-External) + canonical registry + preserved v1 file + coverage
  audit + v1.1 implications list + honest limits. Direction:
  subsumption-with-file-preservation (01A/01D) in effect with 01B
  list-shape concern addressed via preserved v1 file.
- **D-022: ID discipline.** v1 IDs canonical; no view-scoped derived
  IDs; composite references are reading conveniences; mechanical
  coverage audit in §5.
- **D-023: ASM-19 split.** `ASM-19` → `ASM-19a` (recipient-
  reliability) + `ASM-19b` (delivery-reliability) with convergent
  falsifiers + cross-reference-enforcement (01C discipline).
  `RSK-019` update flagged for Session 004+.
- **D-024: POP-12 sub-individuation — decline canonical split;
  adopt subrow-treatment.** §5.5 canonical-split minority preserved.
- **D-025: Migration form.** Supersession-chain (form A /
  functionally-B); v1 preserved verbatim; v2 takes canonical
  filename; frontmatter-chain explicit.
- **D-026: Downstream v1.1 forward-list.** `RSK-014`, `RSK-019`,
  `ACT-005`, `RSK-015`, `RSK-008`, (contingent `RSK-004`).
- **D-027: §5.2/§5.3/§5.4 warrant-check records.** All three
  preserved unchanged; not activated this session.
- **D-028: Validation posture.** Reaffirms `validation: workspace-
  only` per Session 001 DEC-07 and Session 002 D-020;
  `reference-provisional` and `domain-validated` unavailable to
  this application.

Decisions are logged in `02-decisions.md` with `**Triggers met:**`
and `**Triggers rationale:**` per MAD v4 §Trigger-Coverage
Annotation Schema.
