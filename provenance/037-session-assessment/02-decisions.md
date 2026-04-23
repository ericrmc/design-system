---
session: 037
title: Decisions — Path A (Watch) with §6.2 audit of Session 036 synthesis fidelity bundled; engine-v7 preserved; ninth close-rotation steady-state rotation
date: 2026-04-23
status: complete
---

# Session 037 Decisions

Session 037 executes **Path A (Watch) with §6.2 audit of Session 036 synthesis fidelity bundled** per operator "A" single-token ratification. First post-engine-v7 preservation session; direct structural analog of Session 029 (first post-v5 + audit of Session 028) and Session 034 (first post-v6 + audit of Session 033). Single-perspective non-substantive execution per MAD v4 §Perspectives adversarial-requirement scope (applies to deliberative work; Path-A-shape audit is mechanical verification, not multi-perspective reasoning).

See `provenance/037-session-assessment/00-assessment.md` for path-selection analysis and halt-for-ratification framing.

---

## D-117: Path A ratified + §6.2 audit of Session 036 synthesis fidelity all-clean across seven targets

**Triggers met:** [none]

**Single-agent reason:** Path-A-shape single-orchestrator audit execution per Session 029 D-098 / Session 034 D-109 direct precedent (post-engine-v-bump audit template). §6.2 audit is mechanical verification (quote-verbatim comparison against raw sources; cross-perspective absence check; precedent-chain check; file-state verification against synthesis claims); multi-agent deliberation is not triggered by audit work per MAD v4 §When Multi-Agent Deliberation Is Required (audit is not a substantive revision; no genuine-disagreement condition fires on verifying-past-work; audit findings do not modify the kernel or any specification).

**Decision:** Path A (Watch) with §6.2 audit of Session 036 synthesis fidelity ratified and executed. Audit findings all-clean across seven targets enumerated in `00-assessment.md` §3a:

### §6.2 audit findings

**(i) Outsider category-error framing attribution verbatim — CLEAN.**

Session 036 Outsider raw `provenance/036-session-assessment/01D-perspective-outsider.md` Q1 line 16: *"This is not merely a missing heuristic; it is a category error. A session log is an event record, not a mode declaration."* Synthesis `provenance/036-session-assessment/01-deliberation.md` §3b line 73 quotes: *"A session log is an event record, not a mode declaration."* with `[01D, Q1]` citation and `[synth]` marking. Synthesis §7 item 1 line 218 quotes the same passage verbatim with `[01D, Q1]` citation and explicitly names it a cross-lineage contribution. **Verbatim match on two quoting sites; attribution correct.**

**(ii) Outsider structural-signature-as-accidental-layout critique load-bearing — CLEAN.**

Outsider raw `[archive: ..01D-perspective-outsider.md, Q1 dissent paragraph]` line 47: *"Structural signatures are tempting because they avoid another file, but they encode accidental layout as identity. That will fail again when a future workspace has both self-development material and application material for legitimate reasons."* Synthesis `[archive: ..01-deliberation.md, §3c]` line 83 explicitly cites the critique as **load-bearing for rejecting Reviser's pure Direction 2** (structural-signature-only): *"The Outsider's critique that a pure structural signature 'encodes accidental layout as identity' is load-bearing [01D, Q1] — the self-development workspace has future latent ambiguity..."* Synthesis §7 item 2 line 220 quotes the critique verbatim with `[01D, Q1]` citation and names it a cross-lineage contribution Claude perspectives did not independently produce. **Load-bearing attribution verified; the critique materially shaped rejection of Reviser Direction 2 in favour of the MODE.md-authoritative hybrid.**

**(iii) MODE.md + engine-feedback/ adopted spec text consistent with synthesis direction — CLEAN.**

- `specifications/workspace-structure.md` v5 §MODE.md (lines 83–108) frontmatter schema matches synthesis §3c/§3d direction: `mode` + `workspace_id` + `created_session` + `engine_version_at_creation`; external-problem additionally `application_brief`; pre-existing workspace retroactive-adoption additionally `marker_adopted_session` + `engine_version_at_marker_adoption`. Classification: workspace-identity (not engine-definition) per Outsider `[01D, Q4]` direction adopted in synthesis. Validation: check 23 per D-116. Default-read: `read-contract.md` v4 §1 item 0.
- `specifications/workspace-structure.md` v5 §engine-feedback (lines 227–276): outbox-in-external / inbox+triage-in-self-development per synthesis §4c item 1 + Outsider `[01D, Q2]`. Frontmatter schema (lines 239–253) matches Outsider's per-record schema in synthesis §4c item 2. Triage schema (lines 258–268) matches synthesis §4c item 3. INDEX.md default-read in self-dev mode (line 270) matches synthesis §4c item 4. OI integration (line 272) matches §4c item 5. Retention (line 274) matches §4c item 6. Return semantics (line 276) matches Outsider direction.
- Simplification noted in synthesis §4c ("Simplifications from Outsider's full proposal: No `outbox/` subdirectory required") is consistent with actual file structure (`engine-feedback/` at external-workspace side takes `EF-*.md` files directly per workspace-structure.md v5 line 74; no outbox/ subdirectory; self-development side carries `inbox/` + `triage/` + `INDEX.md` per lines 233).

**Adopted spec text is consistent with synthesis direction including the documented Synthesiser-scope-bounding simplifications.**

**(iv) D-113 + D-116 substantive-classification under OI-002 heuristic — CLEAN.**

D-113 `triggers_met: [d016_2, d016_3]` (corrected in-record from initial [d016_1, d016_2, d016_3]; d016_1 removed because kernel untouched): d016_2 fires on PROMPT.md substantive revision (engine-definition file per engine-manifest §3; Session 017 D-074 precedent for PROMPT.md d016_* firing); d016_3 fires on multi-way genuine disagreement (seven directions + no-revision surfaced in deliberation). Consistent with decision content per §6.2 audit comparison of D-113 rationale against deliberation §3.

D-116 `triggers_met: [d016_2, d016_3]`: d016_2 fires on substantive revisions to workspace-structure.md (v4 → v5), read-contract.md (v3 → v4), and new §engine-feedback normative block. d016_3 fires on multi-way genuine shape disagreement on Q2 (OI-tag-only per Reviser; prose-file per Synthesiser; structured outbox/inbox/triage per Outsider; premature-do-nothing per Skeptic-preserver). Consistent with decision content.

**Substantive classification matches OI-002 heuristic + precedent chain** explicitly named in D-114 rationale (line 46): Session 017 D-074 (PROMPT.md split substantive + v-bumping) + Session 022 D-084 (read-contract.md creation substantive + v-bumping) + Session 033 D-106 (kernel §7 revision substantive + v-bumping). D-113 + D-116 extend this pattern for engine-v7.

**Honest note on D-113 in-record trigger correction**: the D-113 record includes a self-correction from initial [d016_1, d016_2, d016_3] to final [d016_2, d016_3] because kernel was not modified. This is a healthy in-record correction pattern (unlike Session 033 D-106 which did correctly fire d016_1 because kernel was modified; Session 036 D-113 correctly does NOT fire d016_1). The corrected triggers match the decision's actual scope.

**(v) engine-manifest.md §7 engine-v7 entry accurate on six sub-claims — CLEAN.**

Audit against actual file state:

- **Sub-claim 1 (PROMPT.md §Dispatch rewritten with three ordered checks + §Session-001 obligation + §Engine-feedback pathway cross-reference)**: verified in `PROMPT.md` lines 18–33 (three ordered checks), lines 37–52 (§Session-001 obligation), lines 60–62 (§Engine-feedback pathway cross-reference). **Accurate.**
- **Sub-claim 2 (workspace-structure.md v4 → v5 adds MODE.md class + §MODE.md + §engine-feedback + §10.4 six minorities)**: verified in `specifications/workspace-structure.md` v5 §MODE.md (lines 83–108), §engine-feedback (lines 227–276), §10.4 block (lines 282–298 with six minorities M1–M6). v4 preserved as `workspace-structure-v4.md` with `status: superseded` (confirmed by frontmatter inspection). **Accurate.**
- **Sub-claim 3 (read-contract.md v3 → v4 adds §1 item 0 MODE.md + §1 item 9 engine-feedback/INDEX.md conditional; §2/§2b/§2c/§4–§7 unchanged; v3 preserved)**: verified in `specifications/read-contract.md` v4 §1 item 0 (line 31), §1 item 9 (line 40). §2 per-file budget (line 46+), §2b aggregate budget (line 82+), §2c close-rotation (line 118+), §4–§7 archive-pack mechanism all unchanged from v3. v3 preserved as `read-contract-v3.md` with `status: superseded`. **Accurate.**
- **Sub-claim 4 (engine-manifest.md §2 → engine-v7; §3 heading + §3a + §4 + §6 + §7 updated)**: verified in `specifications/engine-manifest.md` §2 line 32 ("`engine-v7`"), §3 heading line 36 ("Engine-definition files at `engine-v7`"), §3a line 57+ (Workspace-identity files subsection naming MODE.md), §4 exclusion list (lines 75 + 80 include MODE.md + engine-feedback/), §6 item 4 (MODE.md creation step line 115), §6 engine-feedback reverse-flow note (line 123), §7 engine-v7 history entry (lines 145–167). **Accurate.**
- **Sub-claim 5 (prompts/application.md adds §Engine-feedback clause)**: verified in `prompts/application.md` §Engine-feedback pathway (lines 69–75). **Accurate.**
- **Sub-claim 6 (prompts/development.md adds engine-feedback/INDEX.md read obligation + WX-35-1 git-log-verification §Close convention)**: verified in `prompts/development.md` §How to operate engine-feedback/INDEX.md read clause (lines 19 + 21); §File-edit claim discipline at line 35+ for WX-35-1 forward convention. **Accurate.**

**All six sub-claims verified accurate against actual file state.**

**(vi) WX-35-1 git-log-verify discipline operationally honoured at Session 037 close — DEFERRED TO CLOSE.**

This audit target is forward-looking: the forward convention applies at session close to each file named in close §1e Development-provenance-files-amended. Session 037 close will apply `git log --oneline <path>` verification to SESSION-LOG.md + open-issues/OI-004.md + any other development-provenance files amended. Honest note documenting the verification result will appear in close §1e per the new convention from `prompts/development.md` §Close (added Session 036 per D-116). This audit cell is the first empirical data point on whether the convention operates cleanly post-adoption.

**(vii) §10.4 six minorities preservation verbatim-match raw sources — CLEAN.**

Audit against raw perspective files:

- **§10.4-M1 Skeptic-preserver no-revision Q1**: workspace-structure.md v5 §10.4-M1 faithfully represents Skeptic-preserver raw `[archive: ..01B-perspective-skeptic-preserver.md, Q1]` position. Raw line 16: *"no revision is warranted... The fallback at line 24... is not a failure mode. It is the dispatch resolution mechanism for exactly the cases §2a describes."* Raw line 18: *"The cost of falling through to fallback every session of an external application is one question-and-answer exchange at session open, which is cheap."* M1 captures both (no-revision-warranted + cheap-fallback-is-correct-behaviour). Activation warrant (10-session zero-exercise → retro-vindicate) aligns with synthesis §6 consolidation. **Clean.**
- **§10.4-M2 Skeptic-preserver premature-feedback-pathway Q2**: M2 faithfully represents raw `[archive: ..01B.., Q2]` line 30: *"feedback pathway is premature... Specifying a feedback mechanism in advance of a demonstrated need is speculating-ahead-of-evidence."* M2 captures the premature-formalisation + speculating-ahead-of-evidence + Sessions 008/010 closed-without-feedback grounds. **Clean.**
- **§10.4-M3 Reviser pure Direction 2 structural-signature dispatch**: M3 faithfully represents raw `[archive: ..01A-perspective-reviser.md, Q1]` lines 14 + 16. Raw line 14: *"The most coherent minimal revision is **Direction 2 (stable structural signature)** anchored on the presence or absence of `applications/NNN-<slug>/brief.md`."* Raw line 16: *"I reject **Direction 1 (MODE.md marker file)** as over-engineered. A new top-level file adds an engine-definition surface... We already have `applications/` as the structural signal; adding MODE.md duplicates state."* M3 captures both (Direction 2 preferred + MODE.md as duplicative-state over-engineering). **Clean.**
- **§10.4-M4 Outsider pure Direction 1 MODE.md-authoritative**: M4 faithfully represents raw `[archive: ..01D-perspective-outsider.md, Q1]` dissent against structural-signature-fallback. Raw line 47 is verbatim the critique M4 summarises: *"Structural signatures are tempting because they avoid another file, but they encode accidental layout as identity. That will fail again when a future workspace has both self-development material and application material for legitimate reasons."* Note: the Outsider's full Q1 position includes "operator-asserted at invocation" as primary (not pure-MODE.md-authoritative); M4 consolidates the dissent against the fallback, which is the load-bearing disagreement preserved. **Clean** (consolidation is faithful to the load-bearing dissent content).
- **§10.4-M5 Reviser OI-tag-only feedback pathway**: M5 faithfully represents raw `[archive: ..01A.., Q2]` line 36: *"The most coherent minimal pathway re-uses **open-issues (OIs) plus provenance**, with a single new convention: an OI raised in an external application's workspace may be tagged `scope: engine-feedback` in its frontmatter... No new directory. No new file type. No new tool."* M5 preserves the "no new directory / no new file type / no new tool" triple. **Clean.**
- **§10.4-M6 Outsider separate-prompt-files-operator-invoked**: M6 faithfully represents raw `[archive: ..01D.., Q5]` line 193: *"Separate prompt files with operator-selected invocation should be preserved more strongly than I expect others to do... Require the operator to invoke `PROMPT-development.md` or `PROMPT-external.md` directly. This is less elegant but more explicit, and explicit entrypoints are common in mature tooling."* M6 preserves the "explicit entrypoints are common in mature tooling" reason-giving and the specific file-naming direction. **Clean.**

**All six §10.4 minorities preserved at full strength from raw sources without dilution, including each minority's activation warrant.**

### Overall audit verdict

**All seven targets clean.** Session 036 synthesis fidelity verified across Outsider attribution (2 targets), adopted spec text (1 target), substantive-classification (1 target), engine-manifest v7 entry accuracy (1 target with 6 sub-claims), and minority preservation (1 target with 6 sub-minorities). Forward-looking WX-35-1 verification target deferred to this session's own close per convention. **Post-engine-v-bump audit pattern (Session 029 post-v5 + Session 034 post-v6 + Session 037 post-v7) holds across three consecutive instances — all-clean each time.** This is engine-cadence habit at this point.

**Rationale:** Path A with bundled §6.2 audit is the default-agent-recommended path per precedent chain (Session 029 D-098 post-v5 audit-all-clean + Session 034 D-109 post-v6 audit-all-clean). The pattern reflects engine maturity: substantive engine-v bumps produce clean synthesis under the established multi-perspective + synthesis-writer + operator-ratification discipline, and post-v-bump audit is the confirmatory check. Session 037 is the third consecutive all-clean post-v-bump audit.

**Rejected alternatives:**
- **Path A pure without §6.2 audit**: defers audit to Session 038+; not default-recommended because Session 037 is the natural slot (first post-v7 preservation session analog of Sessions 029 + 034).
- **Path M-PD-B Vitruvius Cell 1 exercise**: §9 trigger 5 at 2-of-3 makes this high-stakes; REJECT would fire trigger 5 + force anti-laundering pause per `reference-validation.md` v3 §7; also requires operator-provided reference text which operator did not surface at ratification.
- **Path OI-004 retrospective draft**: operator-discretionary; not default-recommended per long-deferral precedent (14 sessions since Session 022 criterion-4 articulation).
- **Path feedback-triage**: `engine-feedback/inbox/` and `triage/` both empty at session open; no triage warrant.

---

## D-118: OI housekeeping + minority activation-clock + watchpoint advancement + ninth close-rotation steady-state rotation

**Triggers met:** [none]

**Single-agent reason:** Pure housekeeping per long precedent chain (D-077 / D-091 / D-093 / D-095 / D-097 / D-099 / D-101 / D-103 / D-105 / D-108 / D-110 / D-112 / D-115 all `[none]`-classified). Eighteenth consecutive housekeeping `[none]` record (D-077 through D-118 unbroken). Minority activation-clock advancements are mechanical per each minority's activation-warrant text; watchpoint data points are observational; close-rotation is mechanical per `read-contract.md` v4 §2c.

**Decision:**

1. **OI-004 state unchanged** this session. Session 037 is Path A single-perspective non-substantive; no non-Claude participation; no OI-004 state change. Tally unchanged at **8-of-3** required. Voluntary:required unchanged at **12:9**. Criterion-3 cumulative unchanged at **74**. Third consecutive non-advancing required-trigger session since Session 033 advancement (Sessions 034 / 035 / 036 / 037 all non-advancing by perspective-participation; Session 036 was voluntary-non-advancing-with-criterion-3-contribution advancing voluntary:required but not tally). Update OI-004.md state-history per new forward convention from WX-35-1 hybrid (b)+(c) disposition (the Session 037 state-history-line is the second post-v7 application of the git-log-verify convention after Session 036's initial catch-up note).

2. **Minority activation-clock advancements**:
   - **§10.3 Skeptic-preserver minimal-revision (Session 033)**: Session 037 is fourth data point in 5-session rollback-evaluation window (Sessions 034–038). Session 037 executes Path A with audit; no engine-v7 → engine-v6 rollback proposed; no scope-statement strengthening rolled back. **Fourth non-vindication-direction data point (4-of-5); window continues through Session 038 (fifth data point; evaluation at Session 038 close).**
   - **§10.3 Outsider "Constraint-derivation probe" naming (Session 033)**: operational-watch continues. No external-reader misunderstanding event Session 037. No data point.
   - **§10.3 Reviser separate-OI-for-detection-gap (Session 033)**: evaluated Session 036; watchpoint-only approach vindicated; window closed. No further tracking.
   - **§5.11 Skeptic-preserver pressure-signal-audit (Session 028)**: no data point (no budget-firing event Session 037).
   - **§5.4 Session 022 engine-v-cadence**: activated-not-escalated; Session 037 is first post-v7 preservation session; no engine-v bump; §5.4 status unchanged.
   - **§10.4-M1 Skeptic-preserver no-revision Q1 (Session 036)**: first observational data point in 10-session zero-exercise window (Sessions 037–046). Session 037 did not exercise the new dispatcher for any new-workspace initialisation or external-application begin. **First zero-exercise data point (1-of-10 toward retroactive-vindication)**; window continues through Session 046.
   - **§10.4-M2 Skeptic-preserver premature-feedback-pathway Q2 (Session 036)**: first observational data point in 10-session zero-inbox window (Sessions 037–046). `engine-feedback/inbox/` empty at Session 037 open and at Session 037 close (no feedback deposited this session). **First zero-inbox data point (1-of-10 toward retroactive-vindication)**; window continues through Session 046.
   - **§10.4-M3 Reviser pure Direction 2 structural-signature dispatch (Session 036)**: operational-watch per activation warrant ("MODE.md burdensome across 3 workspaces → collapse"). No new-workspace initialisations this session. No data point.
   - **§10.4-M4 Outsider pure Direction 1 MODE.md-authoritative dispatch (Session 036)**: operational-watch per activation warrant ("structural-signature fallback ambiguous in practice >2 times within 6 sessions"). No dispatcher-fallback-ambiguity events this session. First observational data point in 6-session window (1-of-6 toward zero-ambiguity-events; fallback-needs-tightening-direction would require ambiguity-events-occurring).
   - **§10.4-M5 Reviser OI-tag-only feedback pathway (Session 036)**: 10-session window tracks "feedback-records-under-3-in-10-sessions → collapse to OI-tag". `engine-feedback/` records count: 0 at Session 037 close. First observational data point in 10-session window (1-of-10 toward zero-records-direction which would vindicate Reviser minority if cumulative count remains under 3).
   - **§10.4-M6 Outsider separate-prompt-files-operator-invoked (Session 036)**: operational-watch per activation warrant ("dispatcher ambiguity >6 sessions post-adoption"). No dispatcher ambiguity events this session. First observational data point (1-of-6 toward zero-ambiguity direction).

3. **Watchpoint advancement**:
   - **WX-22-1 witness-dumping pattern**: no new data.
   - **WX-24-1 MAD growth**: MAD unchanged at 6,386 words. **16-session no-growth streak** at Sessions 023–037 inclusive — new longest in watchpoint history (extends Session 036's 15-session record by one).
   - **WX-24-2 budget-literal drift**: no exercise this session. Validator aggregate-report "engine-v5 budget" string literal persists as non-load-bearing cosmetic; not warrant-activating.
   - **WX-24-3 Outsider pre-response workspace exploration**: n=7 stable (Session 037 Path A is single-perspective; no Outsider invocation).
   - **WX-27-1 archive-token citation fragility**: no re-firing (fourth post-repair session boundary holds; structural repair at Session 033 D-108 Path L holds across Sessions 034 / 035 / 036 / 037).
   - **WX-28-1 close-rotation-exception-frequency**: **ninth steady-state data point at zero exceptions** (0-of-9 in 10-session window). One data point (Session 038) remains before cumulative evaluation at Session 038 close.
   - **WX-33-1 cross-family-symmetric detection-mechanism gap**: evaluated Session 036 (watchpoint-only-approach vindicated); window closed; continues as forward observation for potential future symmetric-pattern recurrence. No data point.
   - **WX-33-2 reference-validation.md v3 per-file 7,160-word soft-warn**: stable unchanged.
   - **WX-34-1 SESSION-LOG.md row-verbosity accretion**: **third-of-3 evaluation data point** recorded at Session 037 close. Session 037 is Path-A-shape (forward-discipline scopes to Path-A rows per Session 034 close §5 framework). Session 037 row constructed with restrained verbosity per WX-34-1 forward discipline; SESSION-LOG.md post-close measured at close per validator check 20. **Three-session evaluation window closes**: cumulative evaluation Session 037 close. Vindication direction: if SESSION-LOG.md stays under 8K hard + Path-A row stayed restrained (not multi-sentence accretion), row-verbosity forward discipline has operated cleanly across the 3-session window (Sessions 035 Path-A restrained + Session 036 substantive legitimate + Session 037 Path-A restrained).
   - **WX-35-1 OI-004.md state-history gap forward-discipline verification**: **first-of-3 data point** in 3-session verification window (Sessions 037 / 038 / 039). Session 037 applies the new `prompts/development.md` §Close git-log-verify convention to the two development-provenance files amended this session (SESSION-LOG.md + OI-004.md). Expected result: both verified-committed this session; no new claimed-but-unexecuted-edit event. First operational exercise of the forward convention post-adoption.

4. **Ninth close-rotation steady-state rotation**: per `read-contract.md` v4 §2c, at Session 037 close **Session 031 close rotates OUT of default-read** (moves to archive-surface-by-exclusion per §3); Session 037's own close enters the window. Top 6 session closes by NNN prefix at Session 037 close = Sessions 032, 033, 034, 035, 036, 037. Default-read holds at 19 files count unchanged. Physical paths unchanged. No retention-exception decisions recorded (WX-28-1 ninth data point at zero exceptions).

5. **Minor housekeeping**: `open-issues/index.md` OI-004 status unchanged (tally / voluntary:required / criterion-3 cumulative all carry Session 036 close values; Session 037 adds no new data points on OI-004 metrics). No other OI edits warranted.

**Rationale:** Pure housekeeping per long precedent chain. No multi-agent deliberation required (no substantive revision; no activation warrant fires on the housekeeping itself; minority activation-clock advancements and watchpoint data points are observational-mechanical). Bundling housekeeping into a single decision paired with Path A ratification + audit decision (D-117) follows Session 029/034 post-v-bump two-decision structure.

**Rejected alternatives:**
- Standalone housekeeping session: rejected; housekeeping per precedent is bundled into the post-v-bump audit session closure.
- Expanding housekeeping to include standalone WX-35-1 forward-convention audit (extra audit beyond §6.2): rejected per minimal-scope discipline; the forward-convention verification is part of §6.2 audit target (vi) at this close, not a separate audit decision.

---

## Session 037 validator state

Pre-session (Session 037 open): 865 pass / 0 fail / 3 warn PASS (aggregate 73,127 / 19 files).

Projected at close (per `00-assessment.md` §4): approximately 867–871 pass / 0 fail / 3 warn (close adds pass counts on checks 5/6/7/8/14/15/20; SESSION-LOG row + ninth close-rotation rotation). Three designed soft-warns persist unchanged (MAD 6,386 / reference-validation.md v3 7,160 / SESSION-LOG.md grows by Session 037 row under 8K hard ceiling). Aggregate adjusts per rotation delta (Session 031 close rotates out ~4,646 words; Session 037 close enters at its actual word count). No engine-v transition; no spec revision; no tool change.

## Summary

| D | Title | Triggers | Files changed | Engine-v? |
|---|-------|----------|---------------|-----------|
| D-117 | Path A ratified + §6.2 audit of Session 036 all-clean across 7 targets | [none] (Single-agent reason) | none | no-bump |
| D-118 | Housekeeping + minority activation-clock + watchpoint advancement + ninth close-rotation + WX-34-1 third-of-3 + WX-35-1 first-of-3 | [none] | SESSION-LOG.md, open-issues/OI-004.md | — |
