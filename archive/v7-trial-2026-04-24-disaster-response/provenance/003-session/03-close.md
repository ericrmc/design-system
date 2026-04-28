---
session: 003
title: Session 003 close — system-model v2 multi-view + ASM-19 split
date: 2026-04-24
status: complete
engine_version: engine-v7
---

# Session 003 close

## 1. What this session did

Executed the Session 001 §5.1 first-class minority activation
direction, committed by Session 002 D-019. Produced v2 of the
upstream system-model artefact in multi-view form; split `ASM-19`
in the assumption ledger per Session 002 D-018 flag; forwarded a
v1.1 impact list to Session 004+. v1 single-document model-form
is preserved as a superseded file.

Artefacts produced / revised this session:

- `applications/001-disaster-response/system-model.md` v2 — multi-
  view form per D-021. Seven sections: §1 canonical ID registry
  (subsumption of v1 six-section structure into one-line-per-entry
  tables + key attributes); §2 V-Chain (per-`SVC-*` dependency
  walks, with 13 service blocks covering `SVC-01` through
  `SVC-15`); §3 V-Cohort (cohort × service matrix with `POP-12`
  oxygen-dependent / CPAP-dependent subrow-treatment per D-024,
  cohort-shaped silences `SIL-02`/`SIL-03`/`SIL-19`/`SIL-20`
  inline with affected `POP-*` per 01B discipline); §4 V-External
  (`EXT-*` rows with explicit `ASM-19a` recipient-reliability-
  basis + `ASM-19b` delivery-reliability-basis + `fallback-if-
  fails` columns; cross-reference discipline per §5.8); §5
  coverage audit (ID-drift-prevention block); §6 v1.1
  implications forward-list (flags `RSK-014`, `RSK-019`, `ACT-
  005`, `RSK-015`, `RSK-008`, contingent `RSK-004` for Session
  004+); §7 honest limits and anti-laundering record. Frontmatter
  `version: 2`, `supersedes: system-model-v1.md`,
  `validation: workspace-only`, `last-revised-session: 003`.
  File is 5,220 words body content — well under the 8,000-word
  readability heuristic.
- `applications/001-disaster-response/system-model-v1.md` —
  verbatim copy of v1 system model with frontmatter amendment per
  D-025: `status: superseded`, `superseded-by: system-model.md`,
  `superseded-session: 003`, supersession-reason naming §5.1
  activation (D-019) and Session 003 adoption (D-021 + D-025).
  3,628 words body content.
- `applications/001-disaster-response/assumption-ledger.md` —
  revised to v1.1 per D-023 + D-028. `ASM-19` marked superseded by
  D-023 (original row preserved verbatim in-table for provenance
  per D-017 immutability discipline applied to split-rather-than-
  deleted) with a note directing Session 003+ citations to
  `ASM-19a` and/or `ASM-19b` with paired-posture per §5.8. Two new
  rows added: `ASM-19a` recipient-reliability + `ASM-19b`
  delivery-reliability with full falsifier and review-trigger
  columns. Two new `EXT-SURVEY-*` rows added: `EXT-SURVEY-11`
  enterprise-architecture multi-view pattern (adopt-with-reason
  shallowly); `EXT-SURVEY-12` systems-dependency modelling frames
  (declined-Session-003). Frontmatter `status: v1.1`,
  `last-revised-session: 003`.

Both artefacts carry `validation: workspace-only` per D-028 (which
reaffirms Session 001 DEC-07 and Session 002 D-020).

## 2. Deliberation summary

Four-perspective cross-family deliberation (`cross_model: true`):

| Perspective | Kind | Raw | Manifest |
|---|---|---|---|
| 01A System-Model Reviser | claude-subagent | `01A-perspective-system-model-reviser.md` | `manifests/system-model-reviser.manifest.yaml` |
| 01B Vulnerability Advocate (continuity) | claude-subagent | `01B-perspective-vulnerability-advocate.md` | `manifests/vulnerability-advocate.manifest.yaml` |
| 01C Adversarial Skeptic (continuity) | claude-subagent | `01C-perspective-adversarial-skeptic.md` | `manifests/adversarial-skeptic.manifest.yaml` |
| 01D Outsider | non-anthropic-model (OpenAI via codex exec, model id `gpt-5.5`) | `01D-perspective-outsider.md` | `manifests/outsider.manifest.yaml` |

Synthesis: `01-deliberation.md`. Decisions: `02-decisions.md`. 8
decisions (D-021 through D-028). Every substantive decision
declares `**Triggers met:**` and `**Triggers rationale:**` per MAD
v4 §Trigger-Coverage Annotation Schema (decisions D-026, D-027
tagged `[none]` per their forwarding/record nature; the other six
tagged with `d016_3` or `[d016_3, d016_4]`). No `d023_*` triggers
fired on any decision (no kernel modification; no MAD or
validation-approach Tier-2 revision; no OI-004 state change);
non-Claude participation invoked at operator discretion per MAD v4
§Recommended clause.

**Session 001 §5.1 single-document-form dissent DISCHARGED.** The
preserved minority's adopted revision direction (multi-view model
form, per Session 002 D-019 activation) was executed this session
by adoption of `system-model.md` v2 per D-021. §5.1 minority text
remains preserved at `[archive: provenance/001-session/
01-deliberation.md]` §5.1 for provenance continuity.

**§5.2 / §5.3 / §5.4 warrant-check (per D-027):** all three
preserved unchanged; not activated this session. Reasoning recorded
in `00-assessment.md` §3 and in `02-decisions.md` D-027.

**Four new first-class minorities preserved** for Session 004+:

- **§5.5 Session 003 POP-12 canonical-split minority** (01A + 01B
  convergent). Activation warrant: within 3 sessions, count-closure
  evidence for oxygen-dependent or CPAP-dependent sub-cohorts OR
  subrow-treatment unworkability in Session 004+ risk-register
  v1.1 work.
- **§5.6 Session 003 Adversarial Skeptic view-catalogue-inflation
  watchpoint** (01C). Activation warrant: any Session 004+
  proposal of a fourth or fifth view lacking a concrete Session
  002+ re-derivation-cluster justification.
- **§5.7 Session 003 Outsider supplementary derivation-index
  alternative** (01D frame-completion). Activation warrant: within
  4 sessions, multi-view v2 proves costly / view-catalogue
  inflation fires / readers prefer registry to views.
- **§5.8 Session 003 Vulnerability Advocate + Adversarial Skeptic
  ASM-19 shared-counterparty cross-reference discipline** (01B +
  01C convergent). Activation warrant: any Session 004+ artefact
  claiming partial-address on `ASM-19a` or `ASM-19b` without
  stating its posture toward the paired row.

## 3. Tier 1 validation result

`tools/validate.sh`: **Passed: 84 | Failed: 0 | Warnings: 0 |
Result: PASS**.

Checks out-of-scope for this session per validator gating
(unchanged from Sessions 001/002; same engine-feedback
`EF-001-validator-gates-in-external-workspaces.md` observation
applies):

- Checks 14/15 (triggers_met coverage): session-number-gated ≥
  006; Session 003 is pre-adoption by the self-development source
  workspace's chronology. This session included
  `**Triggers met:**` and `**Triggers rationale:**` on every
  substantive decision; the validator simply does not enforce at
  session < 6 in this workspace's counter.
- Checks 16/17/19 (OI-004 criterion-4 schema): gated ≥ 021; this
  session's Outsider manifest carries the v4 fields per discipline.
  No OI-004 narrowing claim made.
- Check 18 (OI-004 closure-retrospective): out-of-scope; no
  retrospective artefact present.
- Check 20 (default-read budget): session-number-gated ≥ 022;
  Session 003 is pre-adoption by gate. No per-file concerns
  surfaced manually — all default-read files well under any
  plausible ceiling (SESSION-LOG 346 words, `open-issues/index.md`
  152 words; active specifications well within v4 8K hard / 6K
  soft ceilings; current-session provenance files under budget
  individually, with `01-deliberation.md` ~3.8K and `02-decisions
  .md` ~3.6K the largest).
- Checks 21, 22 (archive-pack integrity and citation): presence-
  gated; no archive-packs created in this workspace this session.
  Citations of the form `[archive: provenance/001-session/*]` and
  `[archive: provenance/002-session/*]` appear in this session's
  provenance as references to closed-session files that are
  archive-surface by exclusion; the validator's check 22 pattern-
  matches `archive/<slug>/` directory references, not closed-
  session file references, so these citations are out-of-scope for
  the automated check but honoured in spirit per `read-contract.md`
  §6.

## 4. Tier 2 guided assessment

**Q1. Provenance continuity.** Session 003 read Session 001's and
Session 002's `03-close.md` in full (both within the 6-session
retention window per `read-contract.md` v4 §1 item 7 / §2c).
Session 002's `02-decisions.md` and `01-deliberation.md` §5.1–§5.4
were read via explicit archive-surface citation per
`read-contract.md` §6. Session 001's `02-decisions.md` and
`01-deliberation.md` §5.1 were read for the activation-warrant
text. Session 001 and Session 002 raw perspective files were NOT
read in full; no Session 003 decision turned on a raw-output claim
absent from the synthesis or decision records. Declared in
`00-assessment.md` §1 honest-limits; reaffirmed here for Q9.

All prior decisions referenced in this session are cited by ID:
D-001 (first-class `SIL-*`); D-003 (cohort individuation); D-005
+ D-006 (attribute-indexed; no pretrained clinical numbers);
D-007 (`POP-12` sub-cohort decomposition); D-009 (scope-split
handing downstream work to subsequent sessions); D-010 (four-link
traceability); D-011 (risk-register schema); D-017 (state-
descriptors framing); D-018 (`ASM-19` split flag); D-019 (§5.1
activation); D-020 + DEC-07 + CON-02 (validation posture); D-024
(this session's POP-12 subrow-treatment decision explicitly cites
D-007's count-silence grounds). No Session 001 or 002 decision was
re-proposed without acknowledgment. Session 003 **executes**
Session 002 D-019 activation rather than re-litigating it; the
deliberation's scope was shape-of-revision, not whether-to-revise.

**Q2. Specification consistency.** The eight active specifications
plus both prompts plus `PROMPT.md` plus `tools/validate.sh` form a
self-consistent engine-v7 load; no contradictions or conflicting
assumptions affected Session 003's work. The supersession-chain
discipline used for `system-model.md` v2 is consistent with
`specifications/workspace-structure.md` v5 §applications
regularisation clause (copy-plus-reference semantically equivalent
to supersession-chain form A; v1 preserved verbatim as a separate
file). The `validation: workspace-only` label on v2 is consistent
with `methodology-kernel.md` v6 §7 and `reference-validation.md`
v3 §8 (no reference-provisional or domain-validated claim made;
fictional scenario precludes both).

**Q3. Adversarial quality.** 01C Adversarial Skeptic provided
genuine challenge throughout. Concrete instances:

- Declined to propose a view count [`01C`, Q1]: *"I decline to
  propose a view count. Naming '3 views' or '5 views' is exactly
  the laundering surface I flagged in my Session 001 §5.1
  proposal and that the Reviser will be tempted to close this
  session."* Forced the deliberation to ground any view proposal
  in a specific Session 002 re-derivation cluster rather than in
  "completeness" or "symmetry" — this discipline is adopted as
  §5.6 preserved minority and as the v2 §7 honest-limits record.
- On POP-12 split (Q4), named the split's motivation as pretrained
  clinical knowledge subject to `ASM-20` anti-laundering:
  *"If the Reviser can state the split rationale without invoking
  any clinical time-constant from pretraining, the split is
  independent of count and may proceed. If the rationale is
  'oxygen-dependence is more time-critical than CPAP-dependence,'
  that rationale uses pretrained clinical knowledge (`ASM-20`
  territory)."* This argument was load-bearing for D-024: 2-of-4
  in favour of canonical split (01A + 01B) rejected in favour of
  subrow-treatment (01C + 01D cross-family convergence).
- On ASM-19 split (Q3), named the separable-tractability-illusion
  risk: *"Splitting `ASM-19` into `ASM-19a` and `ASM-19b` creates
  the appearance of separable tractability. The two aspects share
  a counterparty (`EXT-01`)."* The cross-reference discipline
  01C proposed was adopted verbatim as the §5.8 preserved minority
  and as a load-bearing condition of the split in D-023.
- Did not concede. Its Honest Limits section explicitly names
  what its decline-to-propose posture cannot adjudicate without
  Session 002 raw perspective outputs; this is signal (honest
  epistemic disclosure), not concession.

**Q4. Meaningful progress.** This session produced one substantive
v2 artefact (`system-model.md` v2, 5,220 words, fully multi-view)
that downstream Sessions 004+ can operate on; executed the §5.1
activation warrant the workspace pre-committed to three sessions
ago (Session 001 01C dissent → Session 002 activation via 23 re-
derivation instances → Session 003 adoption); adjudicated a
genuine 2-of-4 vs 2-of-4 POP-12 split disagreement with cross-
family weighting; split `ASM-19` with cross-reference-enforcement
discipline; forwarded an explicit v1.1 impact list to Session 004+.
The cross-perspective disagreements (01A+01B vs 01C+01D on POP-12
canonical split; 01A's subsumption vs 01B's parallel-retention of
v1; 01C's view-count decline vs the other three's affirmative
counts) were genuine and recorded, not smoothed into a single
synthesis voice. Four new first-class minorities preserved;
§5.1 discharged by execution. Progress is meaningful, not
ceremonial.

**Q5. Specification-reality alignment.** Not directly addressable
from within an external-problem application's Session 003; this
question bears more on the self-development workspace. Session 003
does observe that the engine's own validator gates (session ≥ 006
for triggers_met, session ≥ 021 for criterion-4 checks, session ≥
022 for default-read budget) create discipline-not-enforced windows
in external-problem workspaces that Session 001's `EF-001` already
flagged; no additional engine-feedback raised this session on the
same observation, which remains pending operator transport.

**Q6. Cross-model evidence (paired with check 13).** The session
records `cross_model: true`. Concrete evidence distinguishing the
Outsider from a Claude subagent with an edited manifest:

- **Invocation transcript preserved verbatim at
  `provenance/003-session/codex-outsider-raw-output.log`** (313
  lines). Contains the codex CLI preamble identifying provider
  (`openai`), workdir, model self-report (`gpt-5.5`), and the full
  user prompt + model response (two copies — a streamed copy and
  a final post-`tokens used` copy from line 213 onwards).
- **CLI command recorded in manifest:**
  `cat codex-outsider-prompt.txt | codex exec --sandbox read-only > codex-outsider-raw-output.log 2>&1`,
  per Sessions 001/002 precedent. No `--model` override used;
  codex defaulted to account's current model (self-reported as
  `gpt-5.5`).
- **Wall-clock separation:** the three Claude subagents (01A, 01B,
  01C) launched via the Agent tool, with 01A completing in ~94s,
  01B in ~80s, 01C in ~79s (per Agent completion notifications).
  The codex exec ran as a separate background process
  (run_in_background=true); its completion notification arrived
  mid-way through the Claude subagent sequence as a distinct
  task-id (`bd63xhnwv`) with its own output log.
- **Content-level distinguishing features:** the Outsider's
  response uses markdown styling differently from the Claude
  subagents (shorter sections, fewer dense sub-lists, different
  use of paragraph breaks — consistent with Sessions 001/002
  Outsider style). Its Q1 "frame-completion contribution" proposed
  a structurally-different alternative (leave v1 intact + add a
  separate `derivation-index.md`); this alternative was not raised
  by any of the three Claude perspectives and is preserved as §5.7
  first-class minority. Its Q4 "expose as subrows under canonical
  POP-12" converged with 01C's decline-canonical-split position,
  providing the cross-family weighting that was load-bearing for
  D-024.
- **Prompt file preserved verbatim at
  `provenance/003-session/codex-outsider-prompt.txt`.**

No edit of the Outsider's raw output occurred after submission
(`output_edited_after_submission: false` in manifest; frontmatter
wrapper added, body byte-identical to log's post-`tokens used`
copy lines 213–313). The cross-model claim is upheld.

**Q7. Trigger-coverage plausibility (paired with checks 14/15).**
All eight decisions declare triggers. Reading each:

- D-021 (v2 shape) — `[d016_3, d016_4]`. 4-perspective genuine
  disagreement on subsumption vs parallel-retention, on 3rd view
  composition (evidence/silence dedicated vs distributed), on
  external-actor dedicated view vs attribute-exposure; d016_4 is
  load-bearing for every Session 004+ reproduction. Plausible.
- D-022 (ID discipline) — `[d016_3]`. 4-of-4 convergent but
  reasoning-paths-distinct (01A's linter, 01B's coverage audit,
  01C's registry-regeneration test, 01D's ID coverage checklist);
  not a trivial decision. Plausible.
- D-023 (ASM-19 split) — `[d016_3]`. 4-of-4 convergent on
  splitting but falsifier details disagreed (ETA slip >50% vs
  >25%; review cadences varied). Plausible.
- D-024 (POP-12 subrow-treatment) — `[d016_3, d016_4]`. Clean
  2-of-4 vs 2-of-4 split with cross-family weighting decisive.
  d016_4: cohort-individuation is 01B's red line per Session 001
  D-003; load-bearing. Plausible.
- D-025 (migration form) — `[d016_3]`. 4-of-4 against form C
  (git-only), convergent on form A/B with minor semantic variance.
  Plausible.
- D-026 (v1.1 forward-list) — `[none]`. Forwarding record, not a
  substantive multi-agent decision. Plausible.
- D-027 (warrant-check records) — `[none]`. Warrant evaluation
  under MAD v4 §Preserve dissent is evidence-bound activation
  review, not a new decision. Plausible.
- D-028 (validation posture reaffirmation) — `[d016_3]`. While
  workspace-only is plainly correct per CON-02 + DEC-07 + D-020,
  the specific reaffirmation language and continuity claim are
  reasonable-disagreement targets. Plausible.

No `**Non-Claude participation:**` skip annotations used (session
has a non-Claude Outsider); no `d023_*` triggers declared (no
kernel/MAD/VA-tier-2/OI-004-state changes). Consistent.

No mismatches or weak reasons flagged.

**Q8. OI-004 closure-retrospective substantive adequacy.** Skip —
no `oi-004-retrospective.md` artefact in this workspace (external
application does not track OI-004; tracking lives in self-
development source workspace).

**Q9. Read-contract adherence (paired with check 22).**

- (a) Default-read surface enumeration per `read-contract.md` v4
  §1 was followed at session open. Files read: `MODE.md`; all
  eight active specs; `PROMPT.md`; `prompts/development.md`;
  `prompts/application.md`; `SESSION-LOG.md`; `open-issues/
  index.md`; Session 001's and Session 002's `03-close.md` (both
  inside the 6-session retention window); the current session's
  provenance directory (populated incrementally as the session
  progressed); `tools/validate.sh`. `engine-feedback/INDEX.md` was
  not read (does not exist; `engine-feedback/outbox/` holds
  Session 001's `EF-001` file but external-problem workspaces do
  not default-read outbox files per `read-contract.md` v4 §1 item
  9).
- (b) Archive-surface records relied on for load-bearing claims
  were cited via `[archive: path]` convention. Specifically:
  `[archive: provenance/001-session/02-decisions.md]` for Session
  001 D-001, D-003, D-005, D-006, D-007, D-009, D-010 citations;
  `[archive: provenance/001-session/01-deliberation.md]` §5.1 for
  the §5.1 minority text (source of this session's activation
  direction); `[archive: provenance/002-session/02-decisions.md]`
  for D-011, D-017, D-018, D-019, D-020 citations;
  `[archive: provenance/002-session/01-deliberation.md]` §5.2,
  §5.3, §5.4 for the Session 002 preserved-minority activation
  warrants evaluated in `00-assessment.md` §3. Application
  artefacts (`risk-register.md`, `response-plan.md`) are not
  archive-surface — they are application-scope content read
  directly per `prompts/application.md` §Read.
- (c) Non-reads of relevant archive records: Session 001 raw
  perspective files (`01A`–`01D`, `codex-outsider-raw-output.log`)
  and Session 002 raw perspective files (`01A`–`01E`,
  `codex-outsider-raw-output.log`) were not read in full. The
  synthesis + decision records are sufficient for Session 003's
  work; no specific Session 003 decision turned on a raw-output
  claim absent from the synthesis or decision records. This
  non-read is declared here per `read-contract.md` v4 §6 honest-
  limits discipline.

No witness-dumping pattern; no silent skips.

## 5. v2 artefacts produced

- `applications/001-disaster-response/system-model.md` v2 — 5,220
  words body, seven sections (canonical registry + V-Chain +
  V-Cohort + V-External + coverage audit + v1.1 forward-list +
  honest limits). `validation: workspace-only`. `supersedes:
  system-model-v1.md`.
- `applications/001-disaster-response/system-model-v1.md` —
  verbatim v1 preserved with superseded frontmatter; 3,628 words
  body. Byte-identical to v1 content except frontmatter.
- `applications/001-disaster-response/assumption-ledger.md` v1.1
  — `ASM-19` marked superseded (original row preserved);
  `ASM-19a` + `ASM-19b` new rows with full falsifier / review-
  trigger metadata; `EXT-SURVEY-11` + `EXT-SURVEY-12` new rows
  recording this session's external-frame survey. 3,570 words
  body.

The downstream artefacts (`risk-register.md`, `response-plan.md`)
were not modified this session per Session 001 D-009 increment-
boundary discipline; they remain at Session 002's v1. Session 004+
may revise per D-026 v1.1 forward-list.

## 6. State of decisions-not-taken after Session 003

Per Session 002 close §6, Session 003 was expected to address six
items:

| Session 002 forwarded item | Session 003 resolution |
|---|---|
| `system-model.md` revision toward multi-view form (D-019 activation direction) | **Resolved** — D-021 + D-025 adoption of v2 multi-view shape with supersession-chain preservation of v1 |
| `ASM-19` split into recipient-reliability vs delivery-reliability (D-018 flag) | **Resolved** — D-023 split into `ASM-19a` + `ASM-19b` with cross-reference discipline per §5.8 |
| `POP-12` internal CPAP-vs-oxygen sub-individuation | **Resolved** — D-024: decline canonical split on `ASM-20` laundering grounds; adopt subrow-treatment in v2 §3; §5.5 preserved minority for canonical-split reconsideration on count-closure or subrow-unworkability |
| Numeric thresholds for state descriptors | Deferred (as expected) — blocked on domain-review input; no domain-review available; remains deferred |
| Mortuary capacity resolution (`SIL-22`; `ACT-021`) | Not engaged this session — remains silence; `ACT-021` remains the reconnaissance action in the plan |
| Governance legitimacy (`SIL-23`) | Not engaged this session — remains silence; flagged in v2 §4 V-External as touched-by silence on `EXT-01` |

Session 003 forwards its own decisions-not-taken to Session 004+
(recorded in `02-decisions.md` §Decisions not taken):

- `RSK-014`, `RSK-019`, `ACT-005`, `RSK-015`, `RSK-008`, (and
  contingent `RSK-004`) v1.1 revisions per D-026 forward-list.
- `POP-12` canonical-split re-consideration per §5.5 activation
  warrant.
- Derivation-index supplementary artefact per §5.7 activation
  warrant.
- Settlement-local topology promotion to view-status per any
  Session 004+ evidence concentrating there (not a warrant; an
  optional direction for Session 004+).
- Mortuary capacity (`SIL-22`) and governance legitimacy
  (`SIL-23`) remain open as Session 002+ forwarded silences.
- Numeric thresholds for state descriptors remain deferred.

## 7. Open issues

No new OIs opened in this workspace. The four first-class
minorities added to the deliberation record this session (§5.5,
§5.6, §5.7, §5.8) are tracked in-spec via MAD v4 §Preserve dissent
activation warrants, not as open issues. Activation of any warrant
in a future session would produce either a revision deliberation
or a new OI at that point.

No new engine-feedback files raised this session. Session 001's
`EF-001-validator-gates-in-external-workspaces.md` remains in
`engine-feedback/outbox/` pending operator transport to the self-
development source workspace; its observation is reinforced by
this session's repeated out-of-scope-gating of checks 14/15/16/17/
19/20 (for the third consecutive session of an external-problem
workspace that does meet the underlying discipline but is pre-
adoption by the validator's gate constants).

## 8. Development-provenance files amended this session

Per WX-35-1 forward convention, this session's claimed amendments
to development-provenance files are verified below.

- `SESSION-LOG.md` — one-row append with Session 003 entry.
  **Verification:** file currently contains the Session 003 row
  (confirmed by `tools/validate.sh` check 6 PASS; re-run after
  edit showed 84 pass / 0 fail / 0 warn). Claim stands; the edit
  is present. Commit status unverified this turn (operator may
  commit at their own cadence); not skipping hooks or amending.

No `open-issues/OI-*.md` edits (no active OIs in this workspace).

## 9. Next session open — what the orchestrator should address first

Session 004 should open by:

1. Reading the default-read surface per `read-contract.md` v4 §1
   (now including Session 001's, Session 002's, and Session 003's
   `03-close.md`, all three within the 6-session retention window).
2. Reading `system-model.md` v2 in full (now multi-view); also
   reading `assumption-ledger.md` v1.1 (for the `ASM-19a`/`ASM-19b`
   split and the two new `EXT-SURVEY-*` rows); also reading the
   v1 `risk-register.md` and `response-plan.md` (which have not
   been revised).
3. Reading each `01X-perspective-*.md` file in
   `provenance/003-session/` by explicit archive-reference when
   its content bears on a specific Session 004+ decision (they
   are archive-surface once Session 003 closes).
4. Assessing the v1.1 forward-list (D-026): which of `RSK-014`,
   `RSK-019`, `ACT-005`, `RSK-015`, `RSK-008` should be revised
   in Session 004, and in what order. This is the session's
   primary Produce target candidate.
5. Assessing the §5.5, §5.6, §5.7, §5.8 activation warrants:
   - §5.5 (POP-12 canonical split): has count-closure evidence
     arrived? has subrow-treatment failed in any v1.1 work?
   - §5.6 (view-catalogue-inflation): any proposal of a new view?
     If yes, apply 01C's test.
   - §5.7 (supplementary derivation-index): is the multi-view v2
     proving costly to maintain?
   - §5.8 (ASM-19 cross-reference discipline): any artefact this
     session addressing only `ASM-19a` or only `ASM-19b` without
     paired posture statement?
6. Assessing the Session 002 forwarded silences still open:
   `SIL-22` mortuary capacity; `SIL-23` governance legitimacy.
   Session 004 may choose to engage either if scope admits.
7. Convening perspectives for the v1.1 risk-register / response-
   plan revision work. Suggested roster (continuity bias noted):
   - a fresh **Risk Analyst** (or Revision Analyst) — new,
     generative;
   - **Vulnerability Advocate** (continuity; now fourth session)
     — may need rotation consideration if cohort-individuation
     continues to be the red line;
   - **Adversarial Skeptic** (continuity) — may need rotation or
     refreshed role framing if §5.6 watchpoint is the primary
     adversarial target;
   - **Outsider** (non-Claude recommended; same `codex exec`
     transport or operator-chosen alternative).
8. Producing v1.1 of whichever artefacts the Session 004 increment
   targets (risk-register most likely per D-026 `RSK-014`/`RSK-019`
   priority; response-plan `ACT-005` + external-actor fallback
   review also strong candidates).
