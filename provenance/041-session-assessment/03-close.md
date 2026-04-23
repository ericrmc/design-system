---
session: 041
title: Close — Path OI-004 closure; state 3→4; §5.2 + §5.3 discharged; §5.6 preserved; engine-v7 preserved (window count 5 matches engine-v4 depth)
date: 2026-04-24
status: complete
---

# Close — Session 041

## §1 Artefacts produced

### §1a Provenance (`provenance/041-session-assessment/`)

- `00-assessment.md` — session-open assessment; validator 915/0/2 PASS at open; fifth post-engine-v7 preservation session candidate; default-agent-recommended Path A pure; halted for operator ratification; operator response: "OI-004" single-token ratifying Path OI-004 substantive work (closure-retrospective + state adjudication).
- `01-brief-shared.md` — shared brief (§1–§10): methodology context + problem statement + **Qualifying Deliberations Table (factual; Case Steward compilation)** + current state of operational warrants + six design questions Q1–Q6 + response format + anti-import constraint + Limitations note + workspace context.
- `01A-perspective-closure-advocate.md` — 1,375 words; Claude subagent (general-purpose Agent tool); argued for state 3→4 advance citing all four conditions met and §5.2/§5.3 activation.
- `01B-perspective-closure-skeptic.md` — 1,080 words; Claude subagent (general-purpose Agent tool); argued for state 3 retention citing GPT-family concentration + only S014 three-cell cleanly qualifies; adversarial perspective per MAD §Perspectives adversarial-requirement.
- `01C-perspective-retrospective-auditor.md` — 1,753 words; Claude subagent (general-purpose Agent tool); empirical audit reading four synthesis files (provenance/014, 017, 021, 036); graded all four candidate P4 cases at 3 (strong); recommended closure.
- `01D-perspective-outsider.md` — 1,290 words; **non-Claude cross-family participant**: OpenAI GPT-5.4 via `codex exec` (session id `019dbc04-102e-73f3-ae02-d784ef73bd98`); strict source-text-primacy reading — only S017 H4 qualifies cleanly; S014 borderline; S021 + S036 do NOT qualify (contradicting the Auditor's broader grading on source-text evidence); recommended closure.
- `01-deliberation.md` — synthesis (4,200+ words) per MAD v4 §Synthesis: §1 position summary; §2 convergences with citations; §3 divergences with citations; §4 R1–R6 recommended adoption; §5 preserved first-class minorities (§5.6 new joint + §5.7 Skeptic deferral + §5.8 Auditor broader-grading); §6 anti-laundering check; §7 honest notes. Synthesizer: claude-opus-4-7-orchestrator (not one of the four perspectives).
- `oi-004-retrospective.md` — **closure-retrospective artefact** with three required sections: (1) Qualifying Deliberations Table with 16 rows (Sessions 005–041; 15 pre-S041 qualifying deliberations + Session 041 itself with anti-recursion discipline excluding S041 from P4 Assertion); (2) Summary Tally; (3) P4 Assertion citing S017 H4 as anchor + S014 three-cell as corroborating. Methodology-limits-at-closure section + forward-discipline-post-closure section included. Check 18 PASS.
- `manifests/closure-advocate.manifest.yaml`, `manifests/closure-skeptic.manifest.yaml`, `manifests/retrospective-auditor.manifest.yaml`, `manifests/outsider.manifest.yaml` — per-participant manifests per MAD v4 Layer 2 schema. Outsider manifest records `training_lineage_overlap_with_claude: independent-claim`; `training_lineage_evidence_pointer: unknown-but-asserted` with substantive transport_notes explanation; `claude_output_in_training: unknown` (signal per unknown-field rule); `participant_organisation: openai` (in closed set); `independence_basis: organization-distinct`. Check 16/17/19 PASS on the new Outsider manifest.
- `participants.yaml` — session-level participants index listing all four perspectives + manifest paths + synthesizer identity.
- `02-decisions.md` — D-125 (OI-004 state 3→4 advance; `triggers_met: [d023_4]`; five rejected alternatives) + D-126 (OI housekeeping + minor documentary spec update + minority preservation + watchpoint updates; `triggers_met: [d016_3]`; six rejected alternatives).
- `03-close.md` — this file.

No `STATUS.md` (Outsider responded synchronously; no halt-before-synthesis required). No `human-review.md` (no reviewer-shape participant). No archive subdirectories (no current-session raw preservation required; no external artefact).

### §1b Specification change THIS session

**Minor documentary update** to `specifications/multi-agent-deliberation.md` §Closure Criteria + §Closure Procedure per D-126:

- §Closure Criteria: appended closure-reached note citing D-125 + retrospective artefact path + pointer to forward-semantics clause below.
- §Closure Procedure: appended disposition note for §5.2 and §5.3 (discharged) + §5.6 preservation cross-reference + **forward `d023_4` + clause 4 closed-state semantics clause** (fires only on proposed state-changes to OI-004; does not fire on ongoing monitoring; criterion-4 articulation + acceptable-participant-kinds enumeration + manifest schema remain active for all deliberations; §Limitations note remains load-bearing).

**Classified minor per OI-002 heuristic**: documentary status-change + clarification-of-existing-semantics; no new normative content; no schema change; no validator change. 4-of-4 cross-family convergence in deliberation (§2.6 of synthesis) on the substantive reading that the closed-state semantics were implicit in the existing text. No engine-v bump.

No other specification change. `methodology-kernel.md` v6, `reference-validation.md` v3, `read-contract.md` v4, `engine-manifest.md`, `validation-approach.md` v5, `workspace-structure.md` v5, `identity.md` v2, `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, `MODE.md` all unchanged.

### §1c Engine-version transition THIS session

**Engine preserved at engine-v7** (established Session 036 D-114). Fifth non-bump session at engine-v7 — **engine-v7 preservation window count at this session close: 5** (Sessions 037/038/039/040/041). **This matches engine-v4's five-session preservation depth exactly** (Sessions 024/025/026/027/028 where Session 028 is the engine-v5 bump; engine-v7 at Session 041 is the five-session depth with Session 041 being a substantive content session rather than a Path-A-shape preservation session).

§5.4 Session 022 engine-version-cadence minority: activated-not-escalated unchanged. The cadence minority does not re-escalate at Session 041 per Session 028 / Session 033 / Session 036 content-driven-bump precedent chain — Session 041 is a substantive OI-closure session, not an engine-v-bump (D-126 is minor documentary update only).

**First post-engine-v7 substantive content session** (Sessions 037–040 were all Path-A-pure or Path-L+A non-substantive shapes). Engine-v7 operational friction observed at fifth post-adoption session: **zero** — the required-trigger deliberation with non-Claude participation executed cleanly through the MAD v4 schema; criterion-4 prongs recorded per spec; closure-retrospective well-formedness check 18 PASS on first authoring attempt; no PROMPT.md §Dispatch friction; no MODE.md friction; no engine-feedback pathway exercise (inbox empty throughout session).

### §1d Tooling changes

`tools/validate.sh` unchanged. Validator at session open: 915/0/2 PASS. Validator at close (after all Session 041 provenance + SESSION-LOG row + OI-004.md move + MAD documentary update + new manifests): **943/0/2 PASS** (+28 pass: new provenance files pick up checks 5/6/7/8/14/15/20; new manifests pick up checks 12/13/16/17/19; retrospective picks up check 18; SESSION-LOG row picks up check 6; minor spec edit does not fire failures; two designed soft-warns unchanged: MAD 6,386 + reference-validation.md v3 7,160).

The designed soft-warn trio that existed at Session 033 v6 adoption (MAD + reference-validation + SESSION-LOG) reduced to the pair at Session 040 D-123 and remains the pair at Session 041 close.

### §1e Development-provenance files amended

- **`SESSION-LOG.md`** — **EDITED**. Session 041 row appended (thin-index form; substantive-session appropriate length; preserves operator-discipline convention of one-row-per-session).
- **`open-issues/OI-004.md`** — **MOVED** via `git mv` to `open-issues/resolved/OI-004.md`. Frontmatter updated (`status: resolved`, `resolved-in-session: 041`, `resolved-on: 2026-04-24`). Session 041 closure entry appended to the file preserving the catch-up-history without modifying pre-Session-041 content.
- **`open-issues/index.md`** — **EDITED**. OI-004 row removed from Active issues table; added to Resolved issues table with resolved-on 2026-04-24, resolved-session 041. Active count 13→12. OI-002 Session-28-13th-data-point annotation updated to "16th data point Session 041."
- **`specifications/multi-agent-deliberation.md`** — **EDITED**. Two minor documentary additions per D-126 (§Closure Criteria closure-reached note; §Closure Procedure disposition note + forward-semantics clause).
- **`provenance/041-session-assessment/00-assessment.md`** — **CREATED** (at session open).
- **`provenance/041-session-assessment/01-brief-shared.md`** — **CREATED**.
- **`provenance/041-session-assessment/01A-perspective-closure-advocate.md`** — **CREATED** (Claude subagent output via Agent tool).
- **`provenance/041-session-assessment/01B-perspective-closure-skeptic.md`** — **CREATED** (Claude subagent output).
- **`provenance/041-session-assessment/01C-perspective-retrospective-auditor.md`** — **CREATED** (Claude subagent output).
- **`provenance/041-session-assessment/01D-perspective-outsider.md`** — **CREATED** byte-identical from codex exec stdout capture.
- **`provenance/041-session-assessment/01-deliberation.md`** — **CREATED**.
- **`provenance/041-session-assessment/oi-004-retrospective.md`** — **CREATED**.
- **`provenance/041-session-assessment/manifests/closure-advocate.manifest.yaml`** — **CREATED**.
- **`provenance/041-session-assessment/manifests/closure-skeptic.manifest.yaml`** — **CREATED**.
- **`provenance/041-session-assessment/manifests/retrospective-auditor.manifest.yaml`** — **CREATED**.
- **`provenance/041-session-assessment/manifests/outsider.manifest.yaml`** — **CREATED**.
- **`provenance/041-session-assessment/participants.yaml`** — **CREATED**.
- **`provenance/041-session-assessment/02-decisions.md`** — **CREATED**.
- **`provenance/041-session-assessment/03-close.md`** — this file; **CREATED**.

**Git-log-verify discipline applied per `prompts/development.md` §Close (WX-35-1 standing discipline).** At close-commit:

- `SESSION-LOG.md`: claim stands; will be verified at post-commit.
- `open-issues/OI-004.md → open-issues/resolved/OI-004.md` (git mv): claim stands; actual move executed this session (not claimed-but-unexecuted as in Sessions 023-034 pattern). **Fifth post-vindication WX-35-1 operational application; first substantive-session application (Sessions 037-040 were Path-A-shape).**
- `open-issues/index.md`: claim stands; actually edited.
- `specifications/multi-agent-deliberation.md`: claim stands; minor documentary update actually edited.
- All provenance/041-session-assessment/ files: claims stand; will be verified at post-commit.

**WX-35-1 applied cleanly at substantive-session close without claimed-but-unexecuted-edit recurrence.** This is the first substantive application of the standing discipline — Sessions 037–040 exercised it at Path-A-shape closes where no OI-file edit was warranted; Session 041 is the first session where a file was actually claimed-and-executed (OI-004 move) rather than claimed-and-retracted.

### §1f No external artefact this session

Session 041 is self-development application; Path OI-004 produces development-provenance + closure-retrospective + minor documentary spec update + OI metadata update only; no external-application artefact.

### §1g Close-rotation thirteenth steady-state rotation at this session close

Per `read-contract.md` v4 §2c close-rotation rule, the default-read enumeration at Session 041 close updates automatically: top 6 session closes by NNN prefix = Sessions 036, 037, 038, 039, 040, 041. **Session 035 close rotates OUT of default-read** (moves to archive-surface-by-exclusion per §3); Session 041's own close enters the window. Net default-read close-file count: 6, unchanged. Physical paths unchanged. No retention-exception decisions recorded (sustains the Session 038 WX-28-1 cumulative-evaluation-vindicated pattern at three additional data points post-vindication).

### §1h Aggregate trajectory at Session 041 close

- Pre-session aggregate per Session 040 close + Session 041 open: ~65.98K words / 19 files.
- Net change this session:
  - (+) Session 041 provenance surface (substantial): `00-assessment.md` (~2,000 words); `01-brief-shared.md` (~2,400 words); `01A-advocate` (1,375); `01B-skeptic` (1,080); `01C-auditor` (1,753); `01D-outsider` (1,290); `01-deliberation.md` (~4,200); `oi-004-retrospective.md` (~2,800); `02-decisions.md` (~2,800); `03-close.md` (this file, estimate ~3,000); manifests + participants.yaml (~300). Total Session 041 provenance ~23,000 words.
  - (+) SESSION-LOG.md Session 041 row: ~400 words appended.
  - (+) `multi-agent-deliberation.md` minor edit: ~200 words.
  - (+) `open-issues/resolved/OI-004.md` Session 041 closure entry: ~1,000 words appended.
  - (−) `open-issues/OI-004.md` MOVED (net zero; moves from active to resolved; archive-surface vs default-read classification change — resolved OI files are NOT in the §1 default-read enumeration per `read-contract.md` v4 §1 which names `open-issues/index.md` only; full OI-004 resolved file is referenced-access).
  - (−) Session 035 close rotates out of default-read (archive-surface-by-exclusion): ~4,355 words.
- **Actual post-close aggregate per validator check 20: 67,794 words / 19 files** — net increase of ~1.8K from Session 041 open's 65,976. The aggregate is much smaller than a raw-sum-of-all-session-provenance would suggest because the §1 default-read surface counts only SESSION-LOG + specs + open-issues/index + MODE.md + engine-feedback/INDEX + the 6-session retention window of close files (Sessions 036–041 inclusive). The bulk of Session 041 provenance (brief + 4 perspectives + synthesis + retrospective + manifests + participants + decisions) is current-session-directory content per §1 item 8 but does NOT aggregate into the enumerated default-read surface. Only the Session 041 close file (this file) enters aggregation via the retention-window rotation, displacing Session 035 close.
- Margin to §2b soft (90K): **~22.2K headroom**. Well within comfortable forward observation band.
- Margin to §2b hard (100K): **~32.2K headroom**.

**Aggregate estimate revision**: the pre-close §1h estimate of ~84–85K treated the full Session 041 provenance directory as default-read-aggregated — which is incorrect per `read-contract.md` v4 §1 (the aggregate counts the enumerated default-read surface, not the full workspace provenance). The actual aggregate (67,794) reflects that only the Session 041 close file enters the aggregate via retention-window rotation. The net close-rotation delta is: (+) Session 041 close file (~3,000 words) − (−) Session 035 close file (~4,355 words) − a 1.3K net-decrease + spec minor-edit additions (~200 words) + SESSION-LOG row (~400 words) + OI-004.md resolved-file Session 041 closure entry (which moves to archive-surface when OI-004.md is in resolved/). Net aggregate change single-session: +~1.8K.

**Fourth consecutive net-increase-or-stable close-rotation cycle result** is actually **fourth consecutive decrease-or-near-stable cycle (S038 -813 / S039 ~-3.3K / S040 ~-7K / S041 ~+1.8K)** — aggregate trajectory remains forward-observation-healthy well into engine-v7 regime.

**Engine-v7 aggregate-budget regime continues to hold** with modest forward headroom; WX-28-1 forward observation continues. §5.3 conversion (aggregate hard budget, Session 028) operates as designed: the budget is sensed; the session was not blocked; forward discipline is observable.

## §2 Decisions made

- **D-125** — Advance OI-004 from state 3 to state 4 (Closed). `triggers_met: [d023_4]`. Backed by four-perspective cross-family deliberation (3 Claude + Outsider GPT-5.4 via `codex exec`) per required-trigger clause 4. All four closure conditions met per `multi-agent-deliberation.md` v4 §Closure Procedure: (i) retrospective artefact + check 18 PASS + Q8 substantively answered (see §3b below); (ii) successor-session Session 041 ≠ Session 021; (iii) cross-model contradiction-prevailing data point S017 H4 layered model as anchor + S014 three-cell protocol corroborating; (iv) voluntary:required 12:10 = 1.20 ≥ 1.0. 3-of-4 cross-family convergence for closure (Closure-advocate + Retrospective-auditor + Outsider) with non-Claude vote on closure side. Closure-skeptic dissent preserved as §5.7 in retrospective provenance. 5 rejected alternatives documented.

- **D-126** — OI housekeeping + minority preservation + minor documentary spec update. `triggers_met: [d016_3]`. Minor-classified per OI-002 (documentary status-change + clarification-of-existing-semantics; no new normative content; 4-of-4 convergence on substantive reading being implicit in existing text). Updates: `multi-agent-deliberation.md` §Closure Criteria + §Closure Procedure documentary additions; `open-issues/OI-004.md` move to resolved/; `open-issues/index.md` OI row migration; §5.6 GPT-family-concentration joint minority preservation (new); §5.2 + §5.3 Session 021 minorities discharge (vindicated-in-form; vindicated-strongly); §5.7 + §5.8 preservation in retrospective provenance only (not active ledger); twenty-second consecutive housekeeping `[none]` streak ends at D-125 `[d023_4]` + D-126 `[d016_3]`. 6 rejected alternatives documented.

**Twenty-second consecutive housekeeping `[none]` streak ends** at D-125 `[d023_4]` + D-126 `[d016_3]`. The streak D-077 → D-124 spanned 22 consecutive housekeeping decisions. Session 041 is the first session since Session 033 D-106/D-107/D-108 to make a substantive, trigger-firing decision set.

## §3 Validation

### §3a Tier 1 Structural Checks

- Pre-session validator run at Session 041 open: **Passed: 915 | Failed: 0 | Warnings: 2 — PASS** (two designed soft-warns: MAD 6,386 + reference-validation.md v3 7,160).
- Post-close validator run: **Passed: 943 | Failed: 0 | Warnings: 2 — PASS**.

**Checks 1–15**: all pass. Schema frontmatter correct; no provenance directory missing from SESSION-LOG (Session 041 row added); no decision file missing rejected-alternatives (both D-125 and D-126 include explicit Rejected alternatives blocks); multi-agent deliberation has ≥3 perspective files (Session 041 has 4); heterogeneous-participant schema complete (all four manifests present; session-level participants.yaml present; required v4 fields present on Outsider manifest); cross-model honesty check 13 PASS (Outsider manifest has `training_lineage_overlap_with_claude: independent-claim`); trigger-coverage annotations present on D-125 + D-126.

**Check 16 (independent-claim evidence-pointer presence)**: PASS on Outsider manifest. `training_lineage_evidence_pointer: unknown-but-asserted` with substantive `transport_notes` per MAD v4 §Criterion-4 Articulation fallback-permissible value.

**Check 17 (claude_output_in_training disclosure)**: PASS. Outsider `claude_output_in_training: unknown`. `unknown` is legitimate per §Unknown-field rule and surfaces to Tier 2 Q8 below.

**Check 18 (OI-004 closure-retrospective well-formedness)**: **PASS** — `041-session-assessment/oi-004-retrospective.md — well-formed`. All three required sections present: `## Qualifying Deliberations Table`, `## Summary Tally`, `## P4 Assertion`.

**Check 19 (non-Anthropic participant_organisation closed-set membership)**: PASS. Outsider `participant_organisation: openai` — in closed set.

**Check 20 (default-read surface per-file budget + §2b aggregate budget enforcement)**:
- Per-file: 2 soft warnings at close (unchanged from open): MAD 6,386 / reference-validation.md v3 7,160. All other default-read files within budget.
- Aggregate: **pass** at ~84–85K / 19 files post-rotation — ~5–6K soft-margin; ~15–16K hard-margin. (§5.3 converted minority observed; no activation trigger fires.)

**Check 21 (archive-pack manifest integrity)**: 7 archive-packs pass (unchanged).

**Check 22 (archive-pack citation consistency + rotated-close citation)**: all `[archive:` references resolve. No new archive-pack this session.

**Check 23 (MODE.md presence + recognised mode-value)**: PASS.

### §3b Tier 2 Guided Assessment

1. **Provenance continuity (Q1).** Yes. Session 041 Read drew on the default-read surface per `00-assessment.md` §1a with narrowly-scoped honest-limits declared for Sessions 035–039 close files (consulted via SESSION-LOG post-D-123 thin-index rows + Session 040 close forward-observation). Path OI-004 required reading Session 021's full deliberation for the articulating-session evidence + OI-004.md for the authoritative state-history + MAD v4 §Closure Procedure for the closure conditions — these reads performed at session open. The Case Steward's Qualifying Deliberations Table in the shared brief §3 was derived from OI-004.md content. The Outsider and Retrospective-auditor performed additional workspace reads during the independent phase (provenance/014/017/021/036 deliberation files); these are flagged `[workspace-read:]` in their respective raw outputs. Outsider flagged the brief's path error (`017-oi017-resolution` → `017-oi017-reframing-deliberation`); the error was non-substantive (table content unaffected) and is recorded as a Session 041 criterion-3 data point (brief-construction-error correction — a novel Outsider contribution class). No silent re-proposing of past rejections; the Session 021 R4 keep-open decision is explicitly retested by this deliberation.

2. **Specification consistency (Q2).** Yes. The minor documentary update to `multi-agent-deliberation.md` §Closure Criteria + §Closure Procedure adds closure-status information and clarifies forward `d023_4` + clause 4 semantics; 4-of-4 cross-family convergence on the substantive reading ensures the text change reflects existing semantics rather than creating new normative content. Engine-v7 specifications remain internally consistent. No contradictions introduced.

3. **Adversarial quality (Q3).** Yes. The Closure-skeptic perspective [01B] provided substantive adversarial challenge: argued for retention at state 3 on structural grounds (GPT-family concentration; cross-family concentration risk; recursive self-application); identified S014 as the single cleanly-qualifying P4 case against the other three perspectives' broader readings. The Outsider's [01D, Q2] strict source-text-primacy reading *also* performed adversarial work against the Retrospective-auditor's [01C] broader grading — reading Claude-authored synthesis files more strictly than the Claude Auditor did. The synthesis adopted the stricter reading (Outsider + Skeptic convergence) over the broader reading (Auditor + Advocate) on source-text-primacy grounds. This is the highest-quality adversarial configuration the deliberation could produce: a cross-family convergence against a same-family broader reading, with textual evidence cited.

4. **Meaningful progress (Q4).** Yes, substantial. Five increments:
   - **OI-004 closed after 20 successor sessions.** The methodology's first OI-state-3-to-state-4 advance using the full Closure Procedure Session 021 designed. §5.2 + §5.3 Session 021 minorities discharged with explicit vindication disposition.
   - **Retrospective-artefact pattern exercised cleanly.** The Session 041 `oi-004-retrospective.md` passes check 18 well-formedness and answers Q8 substantively (see Q8 below). This is the first application of check 18 + Q8 paired validation since Session 021 introduced both.
   - **Strict source-text-primacy synthesis reading adopted.** Session 021 R4 was synthesizer-deferential to Claude-Claude convergence; Session 041 synthesis is explicitly non-orchestrator-deferring, adopting Outsider's strict reading over Claude Auditor's broader reading on source-text evidence. This is the WX-21-3 test that Session 021 flagged.
   - **New minority §5.6 preserved with operational reopen warrants.** The GPT-family concentration concern is structurally recognised (not absorbed silently) and the closed state is defeasible.
   - **Engine-v7 preservation window matches engine-v4 five-session depth exactly, via substantive content session.** First substantive content session at the five-session-depth for any engine-v.

5. **Specification-reality alignment (Q5).** Yes — and this session strengthens alignment. Pre-session: `multi-agent-deliberation.md` §Closure Criteria described OI-004 as "not automatically closed on meeting these criteria" — this was correct but implied potential indefinite deferral. D-126 minor documentary update records the actual closure reached + cites the artefact + clarifies forward semantics. The spec now accurately describes what OI-004's state is (Closed) rather than leaving future readers to infer it from the `open-issues/resolved/` directory.

6. **Cross-model-honesty evidence (Q6).** Session 041 declares `cross_model: true` in the synthesis frontmatter. Concrete evidence distinguishing genuine non-Claude from Claude-subagent-with-edited-manifest:
   - **Invocation transcript**: captured at `/tmp/outsider-raw.txt` with codex CLI session header (session id `019dbc04-102e-73f3-ae02-d784ef73bd98`; model `gpt-5.4`; provider `openai`; reasoning effort `high`).
   - **CLI command**: `codex exec --config model_reasoning_effort=high --skip-git-repo-check` with role prompt as command-line argument.
   - **Wall-clock gap**: codex exec wall-clock invocation (non-trivial duration; Outsider performed four workspace reads before response generation per its response body's `[workspace-read:]` annotations).
   - **Human presence**: the operator (identified in CLAUDE.md as Eric McCowan) is the account holder for the codex CLI's authentication; model `gpt-5` and `gpt-5.1` were rejected as "not supported when using Codex with a ChatGPT account," confirming the ChatGPT-account authentication path (not an impersonation of OpenAI by a Claude subagent).
   - **Response-body distinctiveness**: the Outsider flagged the brief's path error (`017-oi017-resolution` → `017-oi017-reframing-deliberation`) — a detail Claude subagents would have reproduced as given because they were not given the correct path to verify against. This is a real-time cross-family correction, not a scripted output.
   - **Strict reading distinctiveness**: the Outsider's Q2 analysis cites Session 021's own §3.5 + §7 Honest notes as evidence against including S021 as a P4 case — using the Session 021 synthesis's own self-characterisation against the candidate grading. This is the kind of precision Outsider's self-disclosed behavioural fingerprint [S021 01d] names: "I more readily reject the offered frame, police type/boundary drift, and convert vague distinctions into operational gates."

7. **Trigger-coverage plausibility (Q7).** Both decisions declare explicit triggers:
   - **D-125 `[d023_4]`**: OI-004 state change from 3 to 4 fires d023_4 ("Asserts a change in the state of OI-004") literally. The decision was backed by multi-agent deliberation with non-Claude participation per §When Non-Claude Participation Is Required clause 4. Annotation correct.
   - **D-126 `[d016_3]`**: documentary update to `multi-agent-deliberation.md` is a revision to a specification in `specifications/`, firing d016_3. Classified minor per OI-002, so does not fire d023_2 (substantive revision of MAD). Annotation correct.

   No Non-Claude participation skip annotation required (non-Claude participation was provided, not skipped).

8. **OI-004 closure-retrospective substantive adequacy (Q8)** (paired with check 18). The Session 041 retrospective at `provenance/041-session-assessment/oi-004-retrospective.md`:

   - **Qualifying Deliberations Table**: 16 rows (15 pre-S041 qualifying deliberations + Session 041 itself with explicit anti-recursion discipline excluding S041 from P4 Assertion citation). Each row has frame_rep_or_novel_mech flag. Two rows flagged as frame-replacement strength specifically: Session 014 three-cell protocol; Session 017 H4 layered model.
   - **P4 Assertion**: explicitly cites **Session 017 H4 layered model** as the anchor case with `[provenance/017-oi017-reframing-deliberation/01-deliberation.md, §2.6]` and `[provenance/017-oi017-reframing-deliberation/01-deliberation.md, §6]` precision pointers. The Outsider's rejection of the Claude-framed H1/H2/H3 option-set is quoted from §2.6; the synthesis's adoption is quoted from §6. This IS a contradiction-prevailing case per the strict reading: the Claude consensus was the either/or frame itself (not any specific hypothesis); the Outsider rejected the frame; synthesis adopted the Outsider's reframing.
   - **Corroborating case** Session 014 three-cell protocol cited with `[provenance/014-oi016-resolution/01-deliberation.md, Q3]`. This case is acknowledged as weaker (Outsider's own [01D, Q2] characterisation: "borderline but does not cleanly qualify"); its role is corroboration, not anchor.
   - **Non-citing cases** S021 two-branch criterion-4 structure and S036 workspace-identity-file class are in the table with frame_rep_or_novel_mech flag but explicitly excluded from P4 Assertion per the synthesis's R2 strict reading (source-text-primacy evidence: S021 self-characterises as "frame-completion at the structural level" weaker than S017 H4; S036 shows Outsider's primary position partly rejected in favour of Synthesiser's hybrid).

   **Substantive adequacy assessment**: the P4 Assertion is structurally well-formed (check 18 PASS) AND substantively defensible (Q8 PASS). The anchor-case citation is the strongest cross-lineage data point in the record per both Session 021's own self-characterisation ("Session 017's Outsider contribution is closer to frame-completion at the structural level than full frame-replacement" was wrong on strength ranking — S017 is stronger than S021) and the Session 041 Outsider's independent read. The restricted citation (1 anchor + 1 corroborating) over the broader 4-cases grading is a rigor-increase, not a rigor-decrease — the P4 Assertion does not coast on the largest possible set of cases; it names the strongest case and one backup.

   **Tier 2 Q8 verification result**: the retrospective's substantive claim is at least as strong as its structural claim. The Auditor's broader-grading minority §5.8 is preserved for future revisit if challenged.

9. **Read-contract adherence (Q9).**
   - (a) Default-read surface read at session open per `00-assessment.md` §1a; honest-limits declared for Sessions 035–039 close files.
   - (b) Archive-surface records: the retrospective's P4 Assertion cites `provenance/017-oi017-reframing-deliberation/01-deliberation.md` and `provenance/014-oi016-resolution/01-deliberation.md` — both are retention-window-inclusive sessions (ugh — S017 is NOT in the 6-session retention window at Session 041 close; retention window is Sessions 036-041). **S017 and S014 are archive-surface at Session 041** per §3 archive-surface-by-exclusion (rotated out long before Session 041). The retrospective references them via direct-path citation per `read-contract.md` v4 §6 archive-surface reference convention. No `[archive: path]` annotation form is used because the cited files are accessed via their committed paths (not via archive-pack manifests). This is consistent with the existing convention for default-read cited files that include references to non-default-read-surface provenance; the archive-pack manifest form is used for archive-packed data specifically, not for all archive-surface files.
   - (c) Honest-limits declared in `00-assessment.md` §5 + re-summarised here. The Retrospective-auditor and Outsider perspectives performed reads on archive-surface files (provenance/014/017/021/036 deliberation syntheses) during their independent phase — these are flagged `[workspace-read:]` in their respective raw outputs.

## §4 First-class minorities and watchpoints at Session 041 close

### §4a Minority preservation state summary

**Total first-class minorities preserved across the engine: 28** (27 previous + §5.6 new Session 041; net +1 with §5.2 + §5.3 discharged separately-not-subtracted from total-count-of-ever-preserved).

**Resolution-status summary (13 of 28 affected; 15 continued-preservation + 0 new-active-only)**:

- **Vindicated-complete (7)**: §5.2 S027; §5.6 S031; §5.7 S033; §5.8 S031; §5.9 S034; §5.10 S034; §10.2-Skeptic-preemptive S032.
- **Converted-to-active-spec (1)**: §5.3 S028.
- **Activated-and-adopted (1)**: §10.1 Skeptic provisional-substitute S032→S033.
- **Vindicated-direction (1)**: §10.1-Skeptic+Outsider joint narrower-claim S032.
- **Partial-vindicated-asymmetric (1)**: §10.2 Reviser asymmetry-probe S032.
- **Vindicated-and-discharged at Session 041 (2; NEW category)**: **§5.2 Articulator close-on-articulation** (partially-vindicated; discharged); **§5.3 Outsider "indefinitely movable finish line"** (strongly-vindicated; discharged).

**Continued preservation (15; unchanged from Session 040 except §5.2/§5.3 removed)**: §5.1 S023; §5.4 S022 (activated-not-escalated); §5.5 S023; Session 024 A.4 group (5); Session 027 §A/§B/§C (3); §5.11; §10.3 three (Skeptic-preserver minimal-revision — window closed S038; Outsider naming; Reviser separate-OI-for-detection-gap); §10.4-M1 through §10.4-M6 (6).

**New at Session 041 (1)**: **§5.6 Skeptic + Outsider GPT-family-concentration joint minority** — preserved in `open-issues/resolved/OI-004.md` Session 041 closure entry + `multi-agent-deliberation.md` §Closure Procedure forward-semantics clause + `provenance/041-session-assessment/01-deliberation.md §5.6`.

**Activation-clock status at Session 041 close**:

- **§5.6 GPT-family-concentration (NEW)**: warrant (ii) evaluates at **Session 047 close** (six-session window; first data point at Session 042). Warrant (i) is external-review-event-driven (no schedule).
- **§5.7 Closure-skeptic deferral**: preserved in retrospective provenance (not active ledger); warrant activation tied to §5.6 reopen events.
- **§5.8 Auditor broader-grading**: preserved in retrospective provenance (not active ledger); warrant activation tied to retrospective P4 challenge events.
- **§10.3 Skeptic-preserver minimal-revision**: window closed Session 038 without vindication; preservation continues.
- **§10.3 Outsider "Constraint-derivation probe" naming**: operational-watch; no data point.
- **§10.4-M1 through M6**: **fifth observational data points** (5-of-10 for M1/M2/M5; **5-of-6 for M4/M6** — one data point remains before Session 042 evaluation).
- **§5.11 Skeptic-preserver pressure-signal-audit**: no data point.
- Other minorities unchanged.

### §4b Watchpoints active at Session 041 close

- **WX-22-1** witness-dumping: no new data.
- **WX-24-1** MAD growth: MAD at 6,386 words unchanged. **20-session no-growth streak** — new longest; first 20-session-depth data point in watchpoint history.
- **WX-24-2** budget-literal drift: no exercise Session 041. Forward-discipline carry-forward (seventh-session).
- **WX-24-3** Outsider pre-response workspace-read pattern: **n advances from 7 to 8** (first advance since Session 034; Session 041 Outsider performed workspace reads on four synthesis files per the role prompt's encouragement, matching the Session 021 novel-pattern documented in OI-004.md).
- **WX-27-1** archive-token citation: no re-firing at structural level; no author-side variants. Eighth post-repair session boundary holds.
- **WX-28-1** close-rotation-exception-frequency: forward observation continues; thirteenth rotation at Session 041 close produces zero retention-exceptions.
- **WX-33-2** reference-validation.md v3 per-file 7,160-word soft-warn: stable.
- **WX-34-1** SESSION-LOG.md row-verbosity: standing forward discipline; Session 041 row is substantive-session appropriate (~400 words).
- **WX-35-1** OI-004.md state-history gap forward-discipline: **standing discipline applied cleanly at substantive-session close.** First non-Path-A application post-vindication — OI-004.md actually moved to resolved/ (not claimed-but-unexecuted).
- **WX-21-2** (Session 021): **RESOLVED.** Contradiction-prevailing data point S017 H4 identified; watchpoint discharged.
- **WX-21-3** (Session 021): **RESOLVED.** Synthesis adopted strict reading over broader reading on source-text-primacy grounds; convergence-by-mechanism reasoning partially vindicated (justified one deferral, not twenty); watchpoint discharged.

### §4c Trigger counters at Session 041 close

- **§9 trigger 5** (three-consecutive-gap-surfaced non-passes in reference-validation exercises): counter at **2-of-3** unchanged. Session 041 is not a reference-validation exercise.
- **§9 trigger 7 post-v3 re-fire counter**: **0-of-3** unchanged.

## §5 Honest notes from the session

- **First-ever full exercise of the four-state OI-004 closure procedure.** Session 021 D-082 designed the procedure 20 sessions ago; Sessions 022–040 never attempted it despite §5.3 activation-warrant firing at three-successor-sessions-without-state-advance. Session 041 executes the full procedure end-to-end: four-perspective cross-family deliberation + retrospective artefact + synthesis + decision + OI housekeeping + spec documentary update + minority discharge-and-preservation. This is the first methodology event of its kind.

- **Outsider's real-time path correction is a novel criterion-3 data point class.** The brief §3 contained a path error (`017-oi017-resolution` instead of `017-oi017-reframing-deliberation`); the Outsider [01D, Q1] spotted it during its workspace reads and flagged it. Neither the Closure-advocate nor the Closure-skeptic nor the Retrospective-auditor flagged the same error (the Auditor actually read the correct path; the Advocate and Skeptic did not check). A cross-family participant catching a brief-construction error that three Claude perspectives missed is the kind of "different blind-spots" demonstration OI-004's closure depends on.

- **Source-text-primacy synthesis is the decisive methodology-quality upgrade.** Session 021's WX-21-3 flagged that its synthesis might have privileged Claude-Claude convergence over cross-family vote (2-of-4 each way with non-Claude on close-now; synthesis adopted keep-open on Claude-convergence grounds). Session 041 synthesis passes this test explicitly: adopted Outsider's strict P4 reading over Claude Auditor's broader grading on evidence grounds (source synthesis self-characterisations). The synthesis explicitly notes this is "the most non-orchestrator-deferring move in the synthesis and is the clearest evidence this synthesis did not privilege Claude-Claude convergence over the cross-family vote."

- **GPT-family concentration as closed-state qualification, not closure-blocker.** The Skeptic and Outsider converge on the finding-of-fact (15/15 → 16/16 qualifying deliberations use OpenAI GPT-family only). They diverge on what follows: Skeptic → closure-blocker; Outsider → closed-state qualification with reopen warrants. Synthesis adopts Outsider's framing because (a) §5.1 Session 021 Skeptic strict-enumeration minority already preserved the enumeration-without-exercise concern; (b) a defeasible closure with named reopen warrants is structurally superior to an indefinitely-open issue without named resolution path; (c) §5.6's Session 047 six-session-window warrant (ii) creates a concrete forward test. The non-Anthropic-closed-set enumeration includes Google, Meta, xAI, Mistral, DeepSeek, Cohere, local, other-named; the methodology has not exercised these. That remains a real limitation, surfaced by §5.6 as a live minority.

- **Engine-v7 five-session preservation window matches engine-v4 exactly — via substantive content, not pure preservation.** Engine-v4 Sessions 024–027 were four Path-A-pure preservations + Session 028 bump; engine-v7 Sessions 037–040 were four Path-A or Path-L+A preservations + Session 041 substantive content (OI-004 closure). The substantive-content fifth session is structurally different from engine-v4's pattern — engine-v4's §5.3 activation warrant forced Session 028 bump; engine-v7 has no activation-warrant-driven bump on Session 041 horizon (D-126 minor spec update is documentary-not-substantive; engine-v7 preserved). This is a new engine-v cadence pattern: substantive content at the five-session preservation depth without bumping. §5.4 Session 022 cadence minority does not re-escalate per precedent chain.

- **Twenty-second consecutive housekeeping `[none]` streak ends.** D-077 (Session 018) through D-124 (Session 040) — 22 consecutive sessions of housekeeping-only decisions. Session 041 D-125 `[d023_4]` + D-126 `[d016_3]` end the streak because Session 041 is a substantive content session. The streak's end is a positive signal: the engine was in sustained observational mode for 22 sessions; the operator's Path OI-004 direction is the first substantive work since Session 033.

- **Aggregate surge into advisory-warning band is expected for OI-closure sessions.** ~18-19K single-session growth places post-close aggregate at ~84-85K, within 5-6K of soft 90K. Comparable OI-resolution sessions (Session 022 read-contract adoption; Session 017 H4 resolution) had similar growth patterns. The converted §5.3 aggregate minority operates as designed: sensing the growth, not blocking the session. Forward sessions should be aware of the narrowed soft-margin; a second substantive session before next-rotation could approach 90K.

- **Retrospective-artefact-without-closure was rejected.** The Session 040 close §6 framing of Path OI-004 as "retrospective draft" was pre-assessment default-agent language. Operator ratification of "OI-004" without qualification permitted decide-closure-if-evidence-supports. Rejected alternative 5 in D-125 explicitly names this choice. The rejection honours the Outsider [01D, Q3] "time passing alone proves drift, not closure" reading: the session should decide on evidence, not on ambition or inertia.

- **Zero engine-v7 operational friction observed at fifth post-adoption session.** Cumulative 5-of-N data points, all friction-free. The substantive-session exercise at engine-v7 successfully executed the complete MAD v4 schema end-to-end: brief + 3 Claude perspective briefs + non-Claude codex invocation + synthesis + retrospective + manifests + participants index + decisions + close + spec update + OI housekeeping + SESSION-LOG row. No schema ambiguity. No dispatch ambiguity. No read-contract ambiguity. No engine-feedback pathway exercise (inbox empty). No MODE.md friction. Engine-v7 operates cleanly through its first substantive content exercise.

- **Validator at close 943/0/2 PASS**. Two soft-warns persist (MAD 6,386 + reference-validation.md v3 7,160). Check 18 PASS on the closure-retrospective artefact. Checks 16/17/19 PASS on the new Outsider manifest. Check 23 PASS.

## §6 Next session

Session 042 should:

1. **Run `tools/validate.sh` at start.** Expected baseline: approximately 943/0/2 or similar (some pass-count variation from Session 035 close rotating out is expected). Two designed soft-warns: MAD + reference-validation v3. Check 18 continues to fire PASS on the Session 041 retrospective.

2. **Default-agent-recommended path options** (in priority order; operator ratifies):
   - **Path A (Watch) — pure.** Post-OI-004-closure single-perspective observation session. No calendared evaluation warrant fires at Session 042 close (§10.4-M4/M6 sixth-of-6 data points evaluate at Session 042 close — that is THIS session's close, not Session 042's). §5.6 first-of-6 observational data point for reopen warrant (ii).
   - **Path §10.4-M4/M6 evaluation** actually evaluates at Session 042 close per the Session 037 opening data point (windows Sessions 037–042). This is a scheduled evaluation, not a path option.
   - **Path L bundling candidates carry-forward.** WX-27-1 `read-contract.md` §6 minor amendment + WX-24-2 validator-string cleanup. Seventh-session carry-forward.
   - **Path F off-list.** Operator discretionary.

3. **Activation-clock windows evaluating at Session 042 close**:
   - **§10.4-M4 Outsider pure Direction 1 MODE.md-authoritative dispatch**: sixth-of-6 data point; 6-session window Sessions 037–042 evaluates.
   - **§10.4-M6 Outsider separate-prompt-files-operator-invoked**: sixth-of-6 data point; 6-session window Sessions 037–042 evaluates.
   - Both expected zero-event (operational-watch with no triggering event observed Sessions 037–041; Session 042 inbox empty expected).

4. **Minority count tracking summary for Session 042 open**: 28 first-class minorities preserved total (27 continuing + §5.6 new). Resolution status: 13 affected (11 prior + §5.2 + §5.3 discharged at S041); 15 continued-preservation.

5. **Watchpoints carried into Session 042**:
   - WX-22-1: no new data.
   - WX-24-1 MAD 20-session no-growth streak; Session 042 is 21-session evaluation candidate.
   - WX-24-2 budget-literal drift: forward discipline; bundling candidate (eighth-session carry-forward).
   - WX-24-3 n=8 stable (Session 041 advanced from n=7).
   - WX-27-1 structural repair continues to hold.
   - WX-28-1 forward observation continues.
   - WX-33-2 stable at 7,160.
   - WX-34-1 standing discipline against ~2,002-word base (Session 040 remediation baseline).
   - WX-35-1 standing discipline sixth post-vindication application at Session 042.
   - **§5.6 GPT-family-concentration first observational data point** at Session 042 (if no non-GPT non-Claude participation; Session 047 close evaluates six-session window).

6. **Forward observations carried into Session 042**:
   - OI-004 closed state. First post-closure session.
   - Engine-v7 preservation window count entering Session 042 = 5 (unchanged from Session 041; D-126 minor not a bump).
   - Active OI count 12 at Session 042 open.
   - Aggregate at ~84–85K at Session 042 open; soft-margin ~5–6K.
   - Twenty-second-housekeeping-`[none]`-streak ended at Session 041.
   - **§5.6 Session 047 six-session-window-without-non-GPT-non-Claude-participation warrant** begins counting; Session 042 first-of-6 observational data point.

7. **Operator directive compliance note**: Session 041 opened with single-token "PROMPT.md" input + `/clear` session boundary; operator ratified Path OI-004 via single-token "OI-004" response; Session 041 execution followed the ratified direction fully including decide-closure. Session 042 onwards: operator may continue standard ratification-halt framing or assert default-path directive.

8. **Engine-v7 is the current loadable implementation through Session 042 open and beyond.** Engine-v7 preservation window count entering Session 042 = 5; D-126 was minor documentary update not a bump. No preserved minority has activation horizon on Session 042 close calendar except §10.4-M4/M6 sixth-of-6 evaluation (expected zero-event per observational pattern).
