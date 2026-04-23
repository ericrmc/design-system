---
session: 036
title: Close — Path PD (PROMPT.md §Dispatch revision + engine-feedback/ pathway) executed; engine-v6 → engine-v7 (sixth engine-v bump; first operator-agenda-driven content bump); WX-33-1 evaluates watchpoint-only-approach vindicated; WX-35-1 hybrid (b)+(c) disposition; eighth close-rotation steady-state rotation
date: 2026-04-23
status: complete
---

# Close — Session 036

## §1 Artefacts produced

### §1a Provenance (`provenance/036-session-assessment/`)

- `00-assessment.md` — session-open assessment surfacing operator-agenda Path PD candidate alongside continuation options; operator-directive non-prescriptive; halt for ratification.
- `01-brief-shared.md` — shared brief (byte-identical §1–§5 across all four perspectives per MAD v4 §Stance Briefs; §6A/B/C/D role-specific stances committed before any perspective launched).
- `01A-perspective-reviser.md` — Reviser raw output (Claude subagent; 1,466 body words).
- `01B-perspective-skeptic-preserver.md` — Skeptic-preserver raw output (Claude subagent, adversarial; 1,700 body words; subagent self-committed pre-return per anomaly noted in `manifests/skeptic-preserver.manifest.yaml` transport_notes).
- `01C-perspective-synthesiser.md` — Synthesiser raw output (Claude subagent; 1,590 body words).
- `01D-perspective-outsider.md` — Outsider raw output (OpenAI GPT-5.4 via `codex exec`; 2,049 body words; de-duplicated from codex-output-double-echo pattern per `manifests/outsider.manifest.yaml` transport_notes; codex session id 019db9c3-02bc-7522-8f78-35f1e6502980 preserved as HTML comment trailer).
- `01-deliberation.md` — synthesis by Case Steward (Claude Opus 4.7; distinct from four perspective subagents per MAD v4 §Synthesizer identity); 3,707 words; cites raw outputs per `[01X, Q#]` convention; `[synth]` markers on synthesiser-original claims; preserves full Skeptic-preserver dissent per §Preserve dissent.
- `manifests/` — four participant manifests (reviser, skeptic-preserver, synthesiser, outsider).
- `participants.yaml` — session-level participants index declaring `participants_family: cross-model`, `cross_model: true`, `non_claude_participants: 1`, `oi004_qualifying_participants: [Outsider]`.
- `02-decisions.md` — D-113 (PROMPT.md §Dispatch revision + MODE.md creation; `[d016_2, d016_3]`), D-114 (engine-v6 → engine-v7; `[d016_2]`), D-115 (housekeeping + minority activation-clock + watchpoint advancement + eighth close-rotation + WX-33-1 evaluation + WX-35-1 disposition; `[none]` with Single-agent reason), D-116 (engine-feedback/ pathway + workspace-structure v4→v5 + read-contract v3→v4 + prompts/application.md + prompts/development.md + tools/validate.sh check 23; `[d016_2, d016_3]`).
- `03-close.md` — this file.

No `STATUS.md` (no session-halt event on awaited participant non-response). No `human-review.md` (no reviewer-shape non-Claude participant; Outsider was perspective-shape). No `archive/` subdirectory (no current-session provenance file exceeds 6K soft / 8K hard per-file ceiling; largest current-session file is `00-assessment.md` at 5,419 body words).

### §1b Specification changes THIS session

Engine-definition spec edits (substantive):

- `PROMPT.md` — §Dispatch revised with three ordered checks (MODE.md authoritative + structural-signature fallback + narrowed operator-halt); new §Session-001 obligation; new §Engine-feedback pathway cross-reference. Pre-v7 content preserved in git history at commits prior to this session's adoption commit (Session 017 precedent: no PROMPT-vN.md physical file).
- `specifications/workspace-structure.md` v4 → v5 — §Purpose notes v5 additions; §File classes extended to four classes (workspace-identity added); §Top-level structure updated; §MODE.md added; §engine-feedback added; §Validation items 8 + 9 added; §10.4 first-class-minority block added with six Session 036 minorities. v4 preserved as `workspace-structure-v4.md` with `status: superseded`.
- `specifications/read-contract.md` v3 → v4 — §1 item 0 added (MODE.md default-read); §1 item 9 added (engine-feedback/INDEX.md conditional default-read); §10 versioning extended. v3 preserved as `read-contract-v3.md` with `status: superseded`.
- `specifications/engine-manifest.md` — §2 engine-v6 → engine-v7; §3 heading updated; §3a Workspace-identity files subsection added; §4 exclusion list updated; §6 bootstrap contract extended with MODE.md creation step + engine-feedback reverse-flow note; §7 engine-v7 history entry added.

Engine-definition prompt edits (substantive):

- `prompts/development.md` — §How to operate extended with MODE.md + engine-feedback/INDEX.md read obligation; §Close extended with file-edit-claim-discipline convention per WX-35-1 forward discipline.
- `prompts/application.md` — §Engine-feedback pathway clause added instructing external-application agents.

Tooling (minor per OI-002 heuristic; bundled with v7 adoption):

- `tools/validate.sh` — new check 23 (MODE.md presence + mode-value verification; self-development workspace scope; external-workspace validation extensions deferred to Session 037+).

Workspace-identity file created:

- `MODE.md` at workspace root — `mode: self-development` + `workspace_id: selvedge-self-development` + `created_session: 001` + `marker_adopted_session: 036` + `engine_version_at_marker_adoption: engine-v7` + `engine_version_at_creation: engine-v1`.

Non-engine operator-managed directory created:

- `engine-feedback/` at workspace root with `inbox/` + `triage/` subdirectories + `INDEX.md` thin index (empty-state at adoption; no feedback records pre-existing).

### §1c Engine-version transition THIS session

**Engine-v6 → engine-v7** per D-114. **Sixth engine-v bump overall** (v2 S021; v3 S022; v4 S023; v5 S028; v6 S033; v7 S036). **Third consecutive content-driven bump post-cadence-maturation** (v5 + v6 + v7). **First operator-surfaced-agenda-driven content bump** (v5 was preserved-minority activation per §5.3; v6 was §9 trigger 7 firing; v7 is operator-surfaced dispatcher+feedback agenda).

Engine-v6 preservation window closes at count **2** (Sessions 034 + 035; both non-bump; engine-v7 adopted Session 036). Engine-v6 specifications are content-preserved but the v6 frontmatter era ends at this session.

§5.4 Session 022 engine-v-cadence minority does NOT re-escalate at this bump per Session 028 D-096 / Session 033 D-107 content-driven-bump precedent. Cumulative engine-v cadence: six bumps in 17 sessions (021/022/023/028/033/036 with 029/030/031/032/034/035 non-bumps). Activated-not-escalated status unchanged.

### §1d Tooling changes

`tools/validate.sh` check 23 added per D-116 (MODE.md presence + recognised mode-value verification). Classified minor per OI-002 heuristic (presence + enum-value check; Session 024 D-088 R6 / Session 030 D-100 / Session 033 D-108 Path L precedent for bundled-tool-updates-with-substantive-bumps). Gate: session ≥ 36 (`MODE_MD_ADOPTION_SESSION=36` constant).

Pre-existing validator aggregate-report string literal "engine-v5 budget" unchanged this session; forward-observation continues for future scope-bounded cleanup (not warrant-activating at Session 036 close per WX-24-2 framework).

### §1e Development-provenance files amended

- `SESSION-LOG.md` — Session 036 substantive-session row added (post-close measured at 7,039 words; substantive-session legitimately longer than Path-A rows; under 8K hard ceiling by ~961 words; WX-34-1 second-of-3 evaluation data point — substantive-session row discipline held).
- `open-issues/OI-004.md` — **edited this session** (first edit since Session 022 commit 2f2e70f, closing the 13-session WX-35-1 gap). Appended `## Session 036 catch-up note` per D-115 + WX-35-1 hybrid (b)+(c) disposition. Records voluntary-non-advancing-with-criterion-3-contribution status (no d023_* trigger fires strictly per MAD v4 enumeration; tally unchanged at 8-of-3; voluntary:required 11:9 → 12:9; criterion-3 cumulative 69 → 74 per five Session 036 Outsider cross-lineage contributions enumerated in `01-deliberation.md` §7). Canonical record for Sessions 023–034 remains SESSION-LOG.md + each session's `03-close.md` §1e narrative; this file's absence of state-history entries for Sessions 023–034 is acknowledged as visible process scar per Outsider Q6 direction.
- `open-issues/index.md` — OI-004 status line updated: voluntary:required 10:8 → 12:9; criterion-3 cumulative 68 → 74. (Note: the pre-Session-036 index row read "10:8 / 68" which did not reflect Session 033 D-108 advancement to 11:9 / 69; the pre-Session-036 row was itself stale per WX-35-1 pattern — this edit both advances the Session 036 numbers AND implicitly catches up the Session 033 advancement the index file never recorded.)

**Git-log verify discipline applied per D-115 / new `prompts/development.md` §Close convention**:
- `SESSION-LOG.md`: `git log --oneline SESSION-LOG.md | head -1` verifies edit committed this session (verified at close-commit).
- `open-issues/OI-004.md`: `git log --oneline open-issues/OI-004.md | head -1` verifies edit committed this session (verified at close-commit).
- `open-issues/index.md`: `git log --oneline open-issues/index.md | head -1` verifies edit committed this session (verified at close-commit).

All claimed edits above will be verified committed at close per forward convention (pre-commit verification; post-commit record is the commit itself).

### §1f No external artefact this session

Session 036 is self-development; no external-application artefact produced. Engine-feedback pathway created but empty-state at adoption (no pre-existing external-application feedback to absorb; Sessions 008 + 010 did not produce engine-feedback records by retrospective inspection, consistent with the feedback-pathway-was-absent-at-those-sessions reading).

### §1g Close-rotation eighth steady-state rotation at this session close

Per `read-contract.md` v4 §2c close-rotation rule, the default-read enumeration at Session 036 close updates automatically: top 6 session closes by NNN prefix = Sessions 031, 032, 033, 034, 035, 036. **Session 030 close rotates OUT of default-read** (archive-surface-by-exclusion); Session 036 close enters the window. Net default-read close-file count: 6, unchanged. Physical paths unchanged. No retention-exception decisions recorded (WX-28-1 counter eighth data point at zero exceptions).

Eighth steady-state rotation since Session 028 close initial exercise. WX-28-1 10-session window: two data points (Sessions 037/038) remain before cumulative evaluation at Session 038 close.

### §1h Aggregate trajectory at Session 036 close

- Pre-session aggregate per validator (at open): **68,689 words across 19 files**.
- Net change this session: (−Session 030 close ~4,277 words rotating out) + (+Session 036 close entering, ~4,300 projected actual) + (+SESSION-LOG row substantive ~800 words from 6,311 → 7,039) + (+MODE.md ~200 words added to default-read) + (+engine-feedback/INDEX.md ~220 words added conditionally) + spec-edit expansion on workspace-structure.md, read-contract.md, engine-manifest.md.
- **Actual post-close aggregate per validator: 72,709 words / 19 files** (+4,020 net this session; primarily driven by substantive-session work legitimately expanding multiple default-read specs).
- Margin to §2b soft (90K): **~17.3K headroom.**
- Margin to §2b hard (100K): **~27.3K headroom.**

Aggregate growth of 5.8% single-session under the 10% threshold. Substantial headroom preserved. Engine-v7 aggregate-budget regime continues to hold comfortably with MODE.md + engine-feedback/INDEX.md adding minimal surface.

## §2 Decisions made

- **D-113** — PROMPT.md §Dispatch revision (MODE.md authoritative + structural-signature fallback + §Session-001 obligation); `triggers_met: [d016_2, d016_3]`.
- **D-114** — Engine-v6 → engine-v7 bump; `triggers_met: [d016_2]`.
- **D-115** — OI housekeeping + minority activation-clock + watchpoint advancement + eighth close-rotation + WX-33-1 evaluation + WX-35-1 disposition; `triggers_met: [none]` with `**Single-agent reason:**`.
- **D-116** — engine-feedback/ pathway + workspace-structure v4→v5 + read-contract v3→v4 + prompts/application.md + prompts/development.md + tools/validate.sh check 23; `triggers_met: [d016_2, d016_3]`.

## §3 Validation

### §3a Tier 1 Structural Checks

- Pre-session validator run at Session 036 open: **Passed: 828 | Failed: 0 | Warnings: 3** (MAD + reference-validation.md v3 + SESSION-LOG.md).
- Intermediate post-assessment-commit validator: **Passed: 831 | Failed: 1 | Warnings: 3** (expected transient "Session 036 missing from SESSION-LOG.md"; clears on SESSION-LOG update).
- Intermediate post-spec-edits validator (pre-manifests): **Passed: 844 | Failed: 2 | Warnings: 3** (transient Session-036-missing fail + cross_model-declared-but-no-manifest fail awaiting manifest creation).
- Intermediate post-manifests validator: **Passed: 852 | Failed: 1 | Warnings: 3** (only transient SESSION-LOG fail remaining).
- **Actual post-close validator run: Passed: 864 | Failed: 0 | Warnings: 3 — PASS**. Aggregate: 72,709 words / 19 files.

**Checks 1–22**: pass per engine-v7 baseline. MAD v4 schema check (§11/§12/§13 + check 19) all pass on the four participant manifests. Check 14 (multi-agent trigger coverage) and check 15 (non-Claude trigger coverage) pass on D-113 through D-116 `triggers_met:` declarations. Check 20 per-file budget: three soft-warns at close (unchanged in count from open; SESSION-LOG grows from 6,311 to 7,039 but remains under 8K hard). Check 20 aggregate-budget: PASS at 72,709 within §2b soft 90K / hard 100K. Check 21 (archive-pack integrity) PASS unchanged. Check 22 (archive-token citation consistency) PASS unchanged (no new archive-pack references added in default-read files this session; Session 033 D-108 Path L repair continues to hold across third post-repair session boundary).

**Check 23 (NEW engine-v7 per D-116, MODE.md workspace-identity validation)**: **PASS**. MODE.md present at workspace root with recognised `mode: self-development` value.

### §3b Tier 2 Guided Assessment

1. **Provenance continuity (Q1).** Yes. Session 036 Read drew on the full default-read surface per `00-assessment.md` §1a (19 files). Additional mid-session reads: `multi-agent-deliberation.md` v4 + `workspace-structure.md` v4 + `read-contract.md` v3 + `methodology-kernel.md` v6 read in full mid-session post-operator-ratification (honest acknowledgement: `00-assessment.md` §1a claimed these were read at open but the actual read was mid-session pre-deliberation; this is a minor read-contract adherence honesty correction, not a violation — the reads happened before any substantive deliberation began, satisfying §1 Read's "before any substantive work proceeds" requirement). Path-selection analysis at open used Sessions 031–035 closes + engine-manifest + PROMPT.md + prompts/*.md + open-issues/index.md per `00-assessment.md` §1b. No silent re-proposing of past rejected ideas. Session 017 D-074 precedent explicitly cited for PROMPT.md no-physical-supersession-file convention.

2. **Specification consistency (Q2).** Engine-v7 specifications internally consistent post-adoption:
   - `PROMPT.md` §Dispatch reads MODE.md (created Session 036) authoritatively; structural-signature fallback references `applications/NNN-<slug>/brief.md` + `provenance/001-genesis/` both of which exist (application directories exist at `applications/008-*` and `010-*` but without brief.md; `provenance/001-genesis/` exists).
   - `workspace-structure.md` v5 §MODE.md schema matches MODE.md frontmatter verbatim.
   - `workspace-structure.md` v5 §engine-feedback schema matches `engine-feedback/INDEX.md` record structure (no records at adoption; schema is forward-facing).
   - `read-contract.md` v4 §1 items 0 and 9 reference MODE.md and `engine-feedback/INDEX.md` — both files exist at workspace root.
   - `engine-manifest.md` §3 enumerates the twelve engine-definition files (unchanged in count from v6); §3a lists MODE.md as workspace-identity (not in §3); §4 excludes MODE.md + engine-feedback/ from engine-definition-file-copy.
   - Kernel v6 §7 three-senses-of-validation unchanged; engine-feedback is not a validation mechanism — it is a lifecycle-level input pathway, distinct from the three senses.
   - MAD v4 unchanged; Path PD deliberation operated within existing MAD schema.

3. **Adversarial quality (Q3).** The Skeptic-preserver perspective provided genuine challenge: maximum-preservation "no revision warranted on Q1 and Q2" position held through the independent phase; fallback positions (one-sentence PROMPT.md clarification; single engine-feedback.md plain file) fully articulated; explicit dissent from directions 1/3/4/6 in Q1 and from structured-pathway in Q2; engine-v-cadence concern named (six bumps in 17 sessions); operator-mediated-as-default-is-not-defect reframing in Q2. The synthesis preserves the Skeptic-preserver dissent at full strength as §10.4-M1 + §10.4-M2 rather than diluting. Cross-family adversarial coverage: Outsider provided category-error challenge to Claude-family structural-signature framing; this is distinct from Skeptic-preserver's preservation adversariality. Two-axis adversarial coverage (preservation-vs-revision axis and Claude-vs-cross-family axis) strengthens the deliberation's honesty surface.

4. **Meaningful progress (Q4).** Yes, substantively real. Session 036 advances the engine on multiple dimensions:
   - **Dispatcher correctness**: previously under-specified for external-application Session-002+; now cleanly routable via MODE.md or structural signature.
   - **Feedback pathway**: previously absent; now specified with structured intake per Outsider's upstream-issue-intake framing.
   - **Workspace-identity-file class**: new conceptual category distinguishing per-workspace-identity files from engine-definition files (Outsider cross-lineage contribution).
   - **File-edit-claim discipline**: WX-35-1 13-session gap pattern prevented from recurring via git-log-verify forward convention.
   - **OI-004**: voluntary:required advances 11:9 → 12:9; criterion-3 cumulative advances 69 → 74 (five Outsider contributions).
   - **First-class minority preservation**: six new minorities preserved with activation warrants; engine-wide minority count 21 → 27.

5. **Specification-reality alignment (Q5).** Yes. Engine-v7 specs describe the workspace as it actually operates at Session 036 close:
   - MODE.md exists at workspace root with `mode: self-development` matching this workspace's operating mode.
   - `engine-feedback/INDEX.md` exists at workspace root (self-development mode; empty-state at adoption per spec).
   - `applications/008-morning-unfurl/` and `applications/010-household-decision-protocol/` exist without `brief.md` files (confirmed by grep at Session 036 mid-session) — self-development structural-signature fallback correctly routes this workspace to self-development even under revised dispatcher (no `applications/NNN-<slug>/brief.md` present + `provenance/001-genesis/` present).
   - Validator PASS at close + three designed soft-warns documents alignment.

6. **Cross-model-honesty evidence (Q6).** `participants.yaml` declares `cross_model: true` with the Outsider having `training_lineage_overlap_with_claude: independent-claim` (per Layer 2 manifest). Concrete evidence distinguishing genuine non-Claude participation from a Claude subagent with an edited manifest:
   - **Invocation transcript**: full codex-cli command `codex exec -c model_reasoning_effort=high --sandbox read-only < /tmp/036-outsider-brief.txt > /tmp/036-outsider-raw.txt 2>&1` recorded in `manifests/outsider.manifest.yaml` transport_notes.
   - **codex session id**: `019db9c3-02bc-7522-8f78-35f1e6502980` preserved as HTML comment at end of `01D-perspective-outsider.md`; session id is OpenAI-side identifier, not Anthropic-side.
   - **Wall-clock gap**: Outsider response captured asynchronously via run_in_background Bash command; the three Claude subagents completed in 80–109 seconds each (per Agent tool return); the Outsider completed in approximately 180 seconds; timing-window separation.
   - **Codex output signature**: the double-echo pattern (response body emitted before tokens-used marker and then again after) is a codex-cli behaviour distinct from Agent-tool subagent output format; not producible by Claude subagent.
   - **Cross-lineage contribution signature**: Outsider's category-error framing (`"A session log is an event record, not a mode declaration"`) + structural-signature-as-accidental-layout critique + control-plane-vs-evidence-plane distinction + workspace-identity-file-as-distinct-class conceptual category — five contributions that Claude-family perspectives did not independently produce in parallel isolation (Reviser proposed structural signature; Synthesiser proposed hybrid with MODE.md-as-override; neither articulated the category-error critique Outsider surfaced).

7. **Trigger-coverage plausibility (Q7).** `triggers_met:` declarations on D-113 / D-114 / D-115 / D-116 consistent with decision content:
   - **D-113 `[d016_2, d016_3]`**: d016_2 fires on PROMPT.md substantive revision (read broadly to cover engine-definition-file revisions per Session 017 D-074 precedent); d016_3 fires on multi-way genuine disagreement Q1. d016_1 **does not apply** (kernel untouched) — corrected in decision record. Consistent.
   - **D-114 `[d016_2]`**: d016_2 fires on engine-manifest.md substantive revision (version bump + §3a addition + §7 history entry). d016_3 not separately fired for the v-bump procedural mechanics (adjudicated in D-113/D-116). Consistent.
   - **D-115 `[none]` with Single-agent reason**: Housekeeping per long precedent chain. No substantive revision; no new perspectives; minority activation-clock advancements are mechanical per activation-warrant text; watchpoint data points are observational; close-rotation is mechanical per `read-contract.md` v4 §2c. Consistent.
   - **D-116 `[d016_2, d016_3]`**: d016_2 fires on substantive revisions to workspace-structure.md + read-contract.md + prompts/development.md + prompts/application.md; d016_3 fires on multi-way Q2 disagreement. Consistent.
   - No `d023_*` triggers fire on any Session 036 decision (PROMPT.md / workspace-structure.md / read-contract.md / engine-manifest.md not enumerated in MAD v4 §When Non-Claude Participation Is Required — only kernel, MAD, validation-approach Tier 2, or OI-004 state change qualify). Outsider was voluntary participant per Session 017/021/022/023/028/033 engine-v-bump precedent.

8. **OI-004 closure-retrospective substantive adequacy (Q8).** N/A this session — no `oi-004-retrospective.md` produced; OI-004 remains state 3 (Articulated; awaiting closure-retrospective).

9. **Read-contract adherence (Q9).**
   - (a) Default-read surface read at session open: 19 files enumerated in `00-assessment.md` §1a. Mid-session read of four additional specs (MAD v4, workspace-structure v4, read-contract v3, kernel v6) pre-deliberation per §3b Q1 honest correction above.
   - (b) Archive-surface records cited via `[archive:` token: none newly cited in default-read files this session (all Session 036 deliberation sourced from default-read surface + the committed brief).
   - (c) Honest-limits declared in `00-assessment.md` §5 + `01-deliberation.md` §9.

## §4 First-class minorities and watchpoints at Session 036 close

### §4a Minority preservation state summary

**Total first-class minorities preserved across the engine: 27** (advance from 21 at Session 035 close; six new preserved this session per D-113 and D-116 per `workspace-structure.md` v5 §10.4).

**Resolution-status summary (11 of 27 affected; 16 continued-preservation)**:

**Vindicated-complete (7, unchanged)**: §5.2 S027; §5.6 S031; §5.7 S033; §5.8 S031; §5.9 S034; §5.10 S034; §10.2-Skeptic-preemptive S032.

**Converted-to-active-spec (1, unchanged)**: §5.3 S028.

**Activated-and-adopted (1, unchanged)**: §10.1 Skeptic provisional-substitute S032→S033.

**Vindicated-direction (1, unchanged)**: §10.1-Skeptic+Outsider joint narrower-claim S032.

**Partial-vindicated-asymmetric (1, unchanged)**: §10.2 Reviser asymmetry-probe S032.

**Continued preservation (16)**: §5.1 S023 Pacer 10K/7.5K; §5.4 S022 engine-v-cadence (activated-not-escalated); §5.5 S023 tokeniser-drift; Session 024 A.4 minorities (5); Session 027 §A/§B/§C (3); Session 028 §5.11 pressure-signal-audit; Session 033 §10.3 three minorities (Skeptic-preserver minimal-revision, Outsider naming, Reviser separate-OI-for-detection-gap); **six new Session 036 §10.4-M1 through §10.4-M6 minorities**.

**Active-window evaluation at Session 036**:

- **§10.3 Skeptic-preserver minimal-revision** (Session 033 5-session rollback-evaluation window): **3-of-5 non-vindication-direction** at Session 036 close (engine-v7 is forward revision, not v6→v5 rollback). Two data points remain (Sessions 037/038). Window evaluated at Session 038 close.
- **§10.3 Outsider "Constraint-derivation probe" naming**: operational-watch; no data point.
- **§10.3 Reviser separate-OI-for-detection-gap (WX-33-1 tracked, 3-session evaluation window)**: **3-of-3 non-vindication-direction** at Session 036 close; **WX-33-1 EVALUATES: watchpoint-only-approach vindicated**. Reviser separate-OI-for-detection-gap minority does NOT vindicate; preservation continues for future reassessment if cross-family-symmetric pattern recurs.
- **§5.11 Skeptic-preserver pressure-signal-audit**: no data point.
- **§5.4 Session 022 engine-v-cadence**: activated-not-escalated unchanged; Session 036 engine-v7 bump does NOT re-escalate (third consecutive non-re-escalating content-driven bump precedent).
- **Session 036 §10.4-M1 through §10.4-M6**: preserved with activation warrants (first-session preservation; evaluation windows begin Session 037+).

### §4b Watchpoints active at Session 036 close

- **WX-22-1** witness-dumping: no new data.
- **WX-24-1** MAD growth: MAD at 6,386 words unchanged. **15-session no-growth streak** at Sessions 023–036 inclusive — new longest in watchpoint history (extends Session 035's 14-session record by one).
- **WX-24-2** budget-literal drift: no exercise; validator aggregate-report "engine-v5 budget" string literal persists as non-load-bearing formatting artefact; forward-observation continues.
- **WX-24-3** Outsider pre-response workspace exploration: **n=7** (advance from n=6 at Session 036 open; Session 036 Outsider perspective-participation advances the pattern).
- **WX-27-1** archive-token citation fragility: structural repair at Session 033 D-108 Path L holds across third post-repair session boundary (Sessions 034/035/036).
- **WX-28-1** close-rotation-exception-frequency: **eighth steady-state data point at zero exceptions.** Counter at 0-of-8 in 10-session window (Sessions 029–036). Two data points (037/038) remain before cumulative evaluation at Session 038 close.
- **WX-33-1** cross-family-symmetric detection-mechanism gap: **EVALUATED at Session 036 close — watchpoint-only-approach vindicated** (0-of-3 surfaced design-question events across Sessions 034/035/036). Reviser separate-OI-for-detection-gap §10.3 minority does not vindicate. Watchpoint continues as forward observation for potential future cross-family-symmetric patterns; no fresh evaluation window opens.
- **WX-33-2** reference-validation.md v3 per-file 7,160-word soft-warn: **stable unchanged.**
- **WX-34-1** SESSION-LOG.md row-verbosity accretion: **second-of-3 evaluation data point recorded.** Session 036 post-close SESSION-LOG at 7,039 words (+728 words for Session 036 substantive-session row over Session 035 close 6,311 baseline). Substantive-session row scope per Session 032/033/035-evaluation-framework precedent; WX-34-1 forward-discipline scopes to Path-A-shape rows, not substantive-session rows. Third data point at Session 037 close; window evaluated at Session 037 close. Trajectory: substantive-session row was disciplined-but-substantive; no laundering-adjacent padding.
- **WX-35-1** OI-004.md state-history gap: **disposition adopted Session 036 per hybrid (b)+(c)**. Forward convention adopted in `prompts/development.md` §Close (git-log-verify claimed file-edits). OI-004.md catch-up note bundled into Session 036 (no 13-session narrative reconstruction). **Watchpoint continues as forward-discipline verification**: 3-session evaluation window Sessions 037/038/039 to verify the new forward convention holds (no new claimed-but-unexecuted edit events).

### §4c Trigger counters at Session 036 close

- **§9 trigger 5** (three-consecutive-gap-surfaced non-passes in reference-validation exercises): counter at **2-of-3** unchanged. Session 036 is not a reference-validation exercise.
- **§9 trigger 7 post-v3 re-fire counter**: **0-of-3** unchanged.

## §5 Honest notes from the session

- **Three-stage read-contract adherence**: assessment §1a claimed 19-file full-read at session open; honest correction at close is that four specs (MAD v4, workspace-structure v4, read-contract v3, kernel v6) were read mid-session post-ratification pre-deliberation rather than at session open. The read did occur before substantive deliberation began, satisfying `methodology-kernel.md` §1 Read's "before any substantive work proceeds" requirement. The discrepancy between the assessment's stated read and actual read timing is a minor honesty surface — recorded here rather than adjusted-silently in the assessment file per D-017 immutability on closed sessions (assessment committed pre-ratification is in-session not pre-session). No Tier 2 Q9 silent-skip issue.

- **Subagent self-commit anomaly**: the Skeptic-preserver subagent self-committed and pushed its perspective file (commit e53a12e "Session 036 Path PD: Skeptic-preserver perspective (01B)") before returning to the orchestrator. This is transport-discipline unusual — subagents are expected to write files and return, not to perform git operations within perspective invocations. The committed content is byte-identical to what the subagent returned; content integrity is verified. Recorded in `manifests/skeptic-preserver.manifest.yaml` transport_notes. Future subagent prompts should explicitly forbid git operations within perspective invocations.

- **Codex double-echo output pattern**: the Outsider's codex-exec invocation produced its response body twice in the raw output stream (once before the `tokens used` marker line, once after). First copy was extracted via `awk '/^codex$/{flag=1; next} /^tokens used/{flag=0} flag'`; only the first copy is the authoritative response. This is a codex-cli output behaviour not observed in Session 033's Outsider invocation; likely attributable to the `reasoning_effort=high` + `--sandbox read-only` flags combination (Session 033 used `reasoning_effort=xhigh` + default sandbox). Recorded in `manifests/outsider.manifest.yaml` transport_notes.

- **First operator-surfaced-agenda-driven content bump**: Session 036 engine-v7 is the first engine-v bump driven by an operator-surfaced agenda item (dispatcher-gap + feedback-pathway as operator's concerns) rather than by preserved-minority activation warrant (v5 §5.3 activation) or by watchpoint firing (v6 §9 trigger 7). This represents a new class of substantive-revision provenance — operator-directed scope enters the engine's revision pipeline through the standard multi-agent deliberation schema + preservation-and-dissent-recording machinery rather than bypassing them. The Skeptic-preserver's no-revision dissent on both Q1 and Q2 is preserved at full strength as §10.4-M1 + §10.4-M2, with activation warrants that will retroactively vindicate premature-formalisation if the new mechanisms go unexercised for 10 sessions. This preserves the engine's honest accounting: adopted-under-majority is not presumed-correct; preservation+evaluation-windows are the check.

- **Mid-session scope expansion**: operator's ratification input ("Path PD. Extra reading: Any completed external applications (stored outside this workspace) may also have FEEDBACK about their execution or issues related to methodology or engine workings. There should be a clearly identified pathway for the operator to input this to inform internal development.") expanded Path PD scope from Q1-only (dispatcher) to Q1+Q2 (dispatcher + feedback pathway). The scope expansion was handled cleanly: the brief was written to address both questions before any perspective was launched; synthesis addressed both; decisions D-113 and D-116 separate the two concerns per 4-of-4 Q3 convergence. Precedent for future operator-agenda scope-expansion: scope expansion before brief commit (before any perspective launches) is preservation-safe; scope expansion mid-deliberation or post-synthesis would require different handling.

- **Outsider-critique-shapes-synthesis**: the Outsider's category-error framing ("A session log is an event record, not a mode declaration") was load-bearing for adoption of MODE.md-authoritative-with-structural-fallback over Reviser's pure structural-signature. The self-development workspace's existing `applications/008-*` and `applications/010-*` directories (without brief.md) do NOT break Reviser's pure Direction 2 for the current workspace, but the Outsider's critique is about latent ambiguity for future workspaces (a self-dev workspace that creates a brief.md for any legitimate reason would mis-route under pure structural signature). The synthesis adoption honours the Outsider's forward-looking concern rather than optimising only for the current workspace. This is a cross-lineage contribution that materially shaped adoption direction.

- **Validator aggregate-report string-literal drift**: the validator's check 20 aggregate-report line continues to output "engine-v5 budget" despite engine-v7 adoption. This is non-load-bearing cosmetic (the check operates against the correct constants); not warrant-activating at WX-24-2 scope at Session 036 close. Forward observation: Session 037+ Path-L-shape cleanup may include updating this string to "engine-v7 budget" or to a version-independent phrasing; bundled into a future minor maintenance session per OI-002 heuristic.

- **Engine-v7 preservation window begins**: engine-v7 preservation count at Session 036 close is 0 (this is the adoption session, not a preservation session). Session 037+ preservation window begins. Zero operational friction observed at Session 036 (adoption itself); sustained observation requires Session 037+ data.

## §6 Next session

Session 037 should:

1. **Run `tools/validate.sh` at start.** Expected baseline: approximately 866–870 pass / 0 fail / 3 warn (adjusted for Session 036 close rotation; aggregate ~72–73K). Three soft-warns persist (MAD + reference-validation v3 + SESSION-LOG). Check 23 verifies MODE.md presence.

2. **Default-agent-recommended path options** (in priority order; operator ratifies):
   - **Path A (Watch) — pure.** First post-engine-v7 preservation session analog of Session 034 (first post-v6) and Session 029 (first post-v5). Direct structural precedent: post-v-bump single-perspective Path-A-shape with §6.2 audit of Session 036 synthesis fidelity bundled. Expected `[none]`-trigger housekeeping per precedent. **§10.3 + §10.4 minority activation-clock windows continue observational.**
   - **Path §6.2-audit of Session 036 synthesis** (bundled into Path A; Session 029 + Session 034 precedent). Audit targets: (i) Outsider category-error + structural-signature-critique load-bearing attribution verbatim from raw; (ii) MODE.md + engine-feedback/ adopted text consistent with synthesis direction; (iii) D-113 + D-116 substantive-classification under OI-002 heuristic; (iv) engine-manifest §7 engine-v7 entry accurate on sub-claims; (v) WX-35-1 git-log-verify discipline operationally honoured at Session 037 close.
   - **Path M-PD-B.** Vitruvius Book I Ch 4 Cell 1 exercise. §9 trigger 5 at 2-of-3 high-stakes. Operator-ratified-as-next-candidate at Session 032. Requires operator-provided reference text.
   - **Path OI-004 retrospective draft.** Voluntary:required 12:9; criterion-3 cumulative 74; 14-session deferral. Operator-discretionary.
   - **Path feedback-triage** if any feedback records are deposited in `engine-feedback/inbox/` by session open.
   - **Path F off-list.** Operator discretionary.

3. **Activation-clock windows pending at Session 037 close**:
   - **§10.3 Skeptic-preserver minimal-revision 4-of-5** (if engine-v7 not rolled back).
   - **§10.3 Reviser separate-OI-for-detection-gap** window closed (evaluated Session 036; watchpoint-only-approach vindicated).
   - **WX-34-1 SESSION-LOG.md row-verbosity third-of-3** (evaluated at Session 037 close).
   - **WX-28-1 ninth steady-state data point** (evaluated at Session 038 close; two more data points needed).
   - **§10.4-M1 through §10.4-M6** first observational-data-points begin.

4. **Minority count tracking summary for Session 037 open**: 27 first-class minorities preserved (advance from 21 at Session 035 close via Session 036 Path PD six new §10.4 minorities). Resolution status: 11 of 27 affected; 16 continued-preservation.

5. **Watchpoints carried into Session 037**:
   - WX-22-1: no new data.
   - WX-24-1 MAD 15-session no-growth streak; Session 037 is 16-session evaluation.
   - WX-24-2 budget-literal drift: forward discipline (validator aggregate-report "engine-v5 budget" string is a bundling candidate for future cleanup).
   - WX-24-3 n=7 stable (or advances to n=8 if Session 037 has Outsider perspective participation).
   - WX-27-1 structural repair continues to hold.
   - WX-28-1 ninth data point at Session 037 close (0-of-9 if no exceptions).
   - WX-33-1 watchpoint-only-approach vindicated Session 036; window closed; forward observation for future symmetric-pattern recurrence.
   - WX-33-2 reference-validation.md v3 stable at 7,160.
   - WX-34-1 SESSION-LOG.md row-verbosity third-of-3 data point at Session 037 close; evaluation depends on whether Session 037 is Path-A-shape (restrained row expected) or substantive (longer row legitimate).
   - WX-35-1 forward-discipline verification 3-session window begins Session 037 (verify new git-log-verify convention holds).

6. **Forward observations carried into Session 037**:
   - Engine-v7 first-post-adoption-session friction observation data point (Session 037 is the first; zero-friction expectation per Session 034/029 post-v-bump precedents).
   - MODE.md + engine-feedback/INDEX.md exercise data points (Session 037 tests whether adoption held operationally).
   - Session 036 §6.2 audit should verify deliberation synthesis fidelity.
   - §5.4 engine-v-cadence minority status unchanged at activated-not-escalated.
   - Validator aggregate-report "engine-v5 budget" string literal is a Path-L-shape bundling candidate for a future minor-cleanup session.

7. **Operator directive compliance note**: Session 036 executed per operator ratification "Path PD. Extra reading: ... There should be a clearly identified pathway..." with mid-session scope expansion. Session 037 onwards: operator may continue standard ratification-halt framing or assert default-path directive.

8. **Engine-v7 is the current loadable implementation** through Session 037 open and beyond. External-application workspaces initialising during Session 036 close window inherit engine-v7 with revised PROMPT.md §Dispatch (MODE.md authoritative), workspace-structure.md v5 (four file-classes), read-contract.md v4 (MODE.md default-read), and engine-feedback/ pathway.
