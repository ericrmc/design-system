---
session: 023
title: Synthesis — Read-contract budget calibration
date: 2026-04-23
status: synthesized
synthesizer: claude-opus-4-7-orchestrator
participants_family: cross-model
cross_model: true
non_claude_participants: 1
oi004_qualifying_participants: [outsider]
anchor_commit_cited: 1c9f452
---

# Synthesis — Session 023

## 1. Deliberation summary

Session 023 deliberated the read-contract.md §2 default-read budget one session after the spec's adoption at Session 022 (D-084). The operator ratified Path (C) at session open: "Tighten read-contract §2 budget to 8,000 words per Outsider §5.3 minority." The deliberation determined specific values, the engine-version consequence, and side-effects (aggregate budget, cadence-minority response, preserved minorities, watchpoints).

Four perspectives convened per engine-v3 convention: **Calibrator** (empirical-calibration advocate), **Pacer** (middle-value advocate), **Skeptic** (adversarial; defer/prose-correction advocate), **Outsider** (OpenAI GPT-5.4 via codex exec; voluntary non-Claude participation per multi-agent-deliberation v4 §When Non-Claude Participation Is Required clause 2 — substantive revision to read-contract.md is not in the D-023 enumerated list; Outsider's inclusion is voluntary per Sessions 007/008/010/012/013/020/022 precedent).

**Brief-factual error discovered mid-deliberation.** The shared brief §3 file-size table estimated `multi-agent-deliberation.md` at 4,800 words. The Outsider spot-checked directly during the independent phase and flagged the divergence [01d Honest Limits]. Post-synthesis verification: actual measurements are `multi-agent-deliberation.md` 6,403 words; `reference-validation.md` 5,183 words; `validation-approach.md` 4,664 words (the last matches the brief; the first two exceed the brief's "no file exceeds 5,000 words" claim). This error propagated into Calibrator and Pacer reasoning about whether proposed soft warnings would fire on adoption. The synthesis incorporates the corrected data below and notes the implications in §2.5.

## 2. Convergences and divergences

### 2.1 — Q4/Q5 unanimity

**C1. Engine-v4 if Q1 adopts any value change.** Calibrator [01a Q4], Pacer [01b Q4], Skeptic [01c Q4 Reading 1], Outsider [01d Q4] all agree: §10 pre-declaration classifies §2 budget-value changes as substantive; engine-manifest §5 mechanically requires v-bump. Unanimous conditional.

**C2. §5.4 cadence warrant activation is informational, not distorting.** All four perspectives [01a Q5, 01b Q5, 01c Q5, 01d Q5] agree: the §5.4 Skeptic minority warrant from Session 022 activates if engine-v4 adopted (three bumps in four sessions: 021/022/023). The honest response is record-and-proceed, not suppress-the-bump-via-reclassification. None of the four perspectives advocates revising engine-manifest §5 bump criteria in Session 023 itself; all four recommend deferring such a revision to Session 024+ if needed.

### 2.2 — Q1 hard-ceiling value: three-way split

| Perspective | Position | Rationale |
|-------------|----------|-----------|
| Calibrator (Claude) | 8K | Calibration fidelity: 15K was set on incorrect 1.3× ratio; correct 3.0× ratio makes 8K = 24K tokens = within single-Read |
| Pacer (Claude) | 10K | Preserve-headroom: largest file at 60% of 8K leaves no short-term growth runway; 10K gives ~5,200 words runway |
| Skeptic (Claude) | 15K (no change) | Activation-warrant-has-not-fired: Outsider §5.3 warrant requires 10K-soft breach within 5 sessions; one session in, no files above 5K |
| Outsider (non-Claude) | 8K | Empirical-falsification suffices: the 15K Rationale has already been falsified; warrant-literalism gives more weight to text than to the underlying concern |

**Cross-family weighting.** Plurality for 8K (Calibrator Claude + Outsider non-Claude, cross-family). 10K is 1-Claude-only. No-change is 1-Claude-only. No position attracts majority; Calibrator + Outsider 8K convergence is the strongest cross-family signal.

### 2.3 — Q2 soft warning value: same split

| Perspective | Position |
|-------------|----------|
| Calibrator (Claude) | 6K (75% of 8K hard) |
| Pacer (Claude) | 7.5K (75% of 10K hard) |
| Skeptic (Claude) | 10K (unchanged; contingent on Q1 unchanged) |
| Outsider (non-Claude) | 6K fixed; ~75% of 8K hard |

Calibrator + Outsider converge on 6K with 75% ratio articulation.

### 2.4 — Q3 aggregate budget: 3-of-4 cross-family for watchpoint-only

| Perspective | Position |
|-------------|----------|
| Calibrator (Claude) | Watchpoint only; soft at 100K; activation at 120K |
| Pacer (Claude) | Adopt hard budget: 90K hard / 80K soft |
| Skeptic (Claude) | Defer entirely; watchpoint in close only, not spec |
| Outsider (non-Claude) | Watchpoint with reporting; advisory ≥90K; activation ≥100K or >10% single-session growth |

3-of-4 cross-family (Calibrator Claude + Skeptic Claude + Outsider non-Claude) converge on watchpoint-only, against Pacer's hard-aggregate-now. The specific watchpoint values: Calibrator 100K/120K; Outsider 90K/100K; Skeptic defers even the watchpoint values to a future deliberation. Synthesis-judgment adopts Outsider's specific values because they match the Session 022 deliberation's "e.g., 100K words total" preservation language [01d Q3 reference to `provenance/022-workspace-scaling-trajectory/01-deliberation.md §5.3`; §7 WX-22-5] and provide a concrete near-term advisory band.

### 2.5 — The brief-factual-error recalibration

The Outsider's direct workspace read revealed `multi-agent-deliberation.md` at 6,403 words and `reference-validation.md` at 5,183 words — both above the brief's stated 5,000-word upper bound. Under the Calibrator/Outsider-adopted 8K hard / 6K soft:
- `multi-agent-deliberation.md` at 6,403 = 80% of 8K hard; **above 6K soft warning — fires on adoption.**
- `reference-validation.md` at 5,183 = 65% of 8K hard; 86% of 6K soft — close but not firing.
- `validation-approach.md` at 4,664 = 58% of 8K; 78% of 6K — close.

Under the Pacer-preferred 10K hard / 7.5K soft:
- `multi-agent-deliberation.md` at 6,403 = 64% hard; 85% soft — close but not firing.
- `reference-validation.md` at 5,183 = 69% soft — not firing.

Under the Skeptic-preferred no-change (15K hard / 10K soft):
- No file fires any warning. The budget does not bind any file.

This data is material for the synthesis-judgment on Q1. The Outsider position holds that immediate soft-warning firing is the mechanism working ("meaningfully binding without being immediately disruptive" [01d Q1]). The Calibrator reasoned from the brief's (incorrect) 4,800 max; their conclusion that 6K soft "provides meaningful advance notice" without immediate firing does not survive the corrected data. The Pacer reasoned from the same incorrect max; their "no immediate warnings" outcome holds at 10K/7.5K.

**Synthesis resolution.** Adopt 8K/6K per Calibrator + Outsider cross-family convergence. Acknowledge as a known consequence: the 6K soft will fire on `multi-agent-deliberation.md` on adoption. This is the designed function of the soft warning — to prompt restructure when a file approaches the ceiling. Session 024 may restructure `multi-agent-deliberation.md` (the spec has been stable at v4 since Session 021 and may warrant natural subsection-splits), or may elect to let the warning stand through additional sessions to see whether content genuinely requires that length.

## 3. Recommendations for adoption

**R1. Adopt 8,000 words hard ceiling per Calibrator [01a Q1] + Outsider [01d Q1] cross-family convergence.** Pacer's 10K position [01b Q1] preserved as §5.1 minority with activation warrant (see §5). Skeptic's no-change position [01c Q1] preserved as §5.2 minority with activation warrant. Cross-family weighting: Calibrator + Outsider 8K vs Pacer 10K vs Skeptic 15K — plurality on 8K carries the value-change; minorities preserved.

**R2. Adopt 6,000 words soft warning per Calibrator [01a Q2] + Outsider [01d Q2] cross-family convergence.** ~75% of hard-ceiling ratio articulated in spec text for future-revision guidance. Pacer's 7.5K position preserved as §5.1 paired minority. Known consequence: `multi-agent-deliberation.md` at 6,403 words fires the new soft warning on adoption; Session 024 responds per read-contract §8 remediation options (reduce, split, or relocate to archive).

**R3. Do not adopt aggregate hard budget this session** (3-of-4 cross-family against). Add aggregate-default-read-surface report to validator output per Outsider [01d Q3] (advisory threshold ≥90K; activation trigger ≥100K or >10% single-session growth). Pacer's hard-at-90K/80K position preserved as §5.3 minority with activation warrant. Report behaviour: validator prints the aggregate word count in each Tier 1 run; no pass/fail/warn based on aggregate in engine-v4; thresholds above inform Session 024+ deliberation if they fire.

**R4. Revise `read-contract.md` v1 → v2 (substantive).** §2 budget values updated; §2 Rationale rewritten with correct 3.0× empirical ratio and corrected arithmetic; §2 Outsider minority text updated to reflect that the 8K direction is now adopted and to preserve the new minorities (Pacer 10K; Skeptic no-change; aggregate-now); §10 Versioning updated to show v2 history. v1 preserved as `read-contract-v1.md` with `status: superseded` and `superseded-by: read-contract.md (v2)`.

**R5. Update `tools/validate.sh` constants.** `DEFAULT_READ_HARD_WORD_CEILING=8000`; `DEFAULT_READ_SOFT_WORD_CEILING=6000`. No other check logic changes. Add aggregate-default-read-surface report under check 20's scope (informational; not pass/fail/warn per R3).

**R6. Declare `engine-v4` in `engine-manifest.md` §2 + §7.** Per Q4 unanimous-conditional convergence (C1). §3 engine-definition file set unchanged (no new specs; no removed). §7 history entry names D-086 as bump driver, cites the read-contract.md v1 → v2 revision and validate.sh constants revision as the substantive changes; explicitly records §5.4 Skeptic minority warrant activation per Q5 unanimity (C2).

**R7. Open new OI-018** for engine-manifest §5 bump-trigger criteria revisit per Skeptic [01c Q5] + Outsider [01d Q5] shared recommendation. Session 024+ may undertake the deliberation if §5.4 warrant escalates (engine-v5 proposed before Session 026, or external-application portability confusion observed).

**R8. OI-002 10th data point.** Substantive revision to `read-contract.md` (v1 → v2) classified per heuristic; heuristic continues to hold stable.

**R9. Preserve five first-class minorities per §5 below.** Each with concrete operational activation warrants.

**R10. Record six watchpoints for Session 024+ per §6 below.**

## 4. Rejected alternatives

- **Pacer 10K hard ceiling [01b Q1].** Rejected in favour of Calibrator + Outsider 8K cross-family convergence. Pacer's asymmetric-cost-of-binding argument (specs may legitimately need to grow) is thoughtful but is outweighed by calibration-fidelity argument: a ceiling 30K tokens above single-Read does not accomplish "headroom below single-read" and is not the ceiling the §2 Rationale articulated. Preserved as §5.1 minority.

- **Skeptic no-change position [01c Q1].** Rejected on calibration-fidelity grounds. The Outsider §5.3 activation warrant has indeed not literally fired, but the warrant was written on the expectation that 15K ≈ 19,250 tokens — which is wrong by the very Session 022 Honest Notes that preserved the warrant. The spec's own empirical premise is already falsified; deferring correction until the warrant's precise textual trigger fires would be warrant-literalism over spec-fidelity. Preserved as §5.2 minority.

- **Pacer aggregate hard budget [01b Q3].** Rejected 3-of-4 cross-family. Pacer's "naming creates forcing function" argument is thoughtful but the remediation path is underdesigned (Outsider [01d Q3]: every closed session's 03-close.md is default-read and grows monotonically under immutability; a hard ceiling without a repair path binds without recourse). Preserved as §5.3 minority with numerical-value-specific activation warrant.

- **Calibrator specific watchpoint value of 120K aggregate activation [01a Q3].** Rejected in favour of Outsider's 100K activation + 10% growth-rate trigger. The 100K value matches Session 022 §5.3 preservation text; the 10% single-session growth trigger catches sudden accretion that a static threshold misses.

- **Skeptic "minor correction of Rationale prose only" pathway [01c Q4 Reading 2].** Rejected because Q1 adopts a value change. Under R1, the §10 pre-declaration binds the classification. Skeptic's argument that prose correction without value change is minor remains correct for the counterfactual no-value-change case; that counterfactual is preserved as part of §5.2.

- **Same-session revision to `engine-manifest.md` §5 bump criteria.** All four perspectives unanimously reject this (C2). Session 024+ may consider if §5.4 escalation warrants.

## 5. Preserved first-class minorities

Each minority includes specific operational activation warrants per multi-agent-deliberation v4 §minority-preservation discipline.

### §5.1 — Pacer 10K-hard / 7.5K-soft minority

**Position.** A 10,000-word hard ceiling preserves calibration-corrective discipline while leaving growth headroom consistent with observed Session 001–022 trajectory. A 7.5K soft warning provides advance signal without firing immediately on the largest current files.

**Source.** [01b-perspective-pacer.md Q1, Q2].

**Activation warrant.** If the adopted 8K/6K budget produces **three or more restructure-for-budget events in the next 5 sessions** — files restructured or archive-migrated because they crossed the ceiling rather than because their content completed — revisit upward toward 10K/7.5K. Restructure-for-budget is distinguished from restructure-for-content by an explicit field in the session close ("restructure prompted by budget: yes/no"). Alternatively, if 8K binds on `multi-agent-deliberation.md` or `reference-validation.md` in a way that forces artificial split (content-coherence damage as judged by the next deliberation's Architect-role perspective), Pacer position becomes preferred revision direction.

### §5.2 — Skeptic no-change + warrant-literalism minority

**Position.** The read-contract's own Outsider §5.3 activation warrant has not literally fired; revising values one session into a five-session grace window subverts the spec's own governance mechanism for self-revision. Factual correction to the §2 Rationale prose (wrong tokens-per-word ratio) is minor per OI-002; no budget-value change is warranted.

**Source.** [01c-perspective-skeptic.md Q1, Q4 Reading 2].

**Activation warrant.** If within 5 sessions of the Session 022 adoption (i.e., by Session 027) **no default-read file exceeds 7,500 words and no restructure-for-budget event occurs**, the Skeptic no-change position is vindicated retroactively: Session 023's revision was premature, and the record shows the warrant-literalism discipline would have produced a stable budget without the intervention. Vindication would inform Session 028+ consideration of whether future activation warrants should be held more strictly.

### §5.3 — Pacer aggregate-hard-budget minority

**Position.** An aggregate hard budget at 90K hard / 80K soft should be adopted now; naming a budget creates the forcing function that watchpoint-only reporting lacks.

**Source.** [01b-perspective-pacer.md Q3].

**Activation warrant.** If the aggregate default-read surface **exceeds 100,000 words OR grows >10% in a single session without compensating restructure** (the R3 advisory and activation thresholds), Pacer's hard-budget position becomes the preferred revision direction for Session 024+ read-contract.md §2 revision. This specific trigger is more crisp than "adopt aggregate budget now" because it names the data condition under which watchpoint-only becomes insufficient.

### §5.4 — Session 022 engine-version-cadence minority (activated)

**Position.** Three engine-v-bumps in four adjacent sessions (Session 021 engine-v2; Session 022 engine-v3; Session 023 engine-v4) is cadence-churn. Each bump increases external-application-portability risk.

**Source.** Session 022 [01c-perspective-skeptic.md §5.4] preserved in `provenance/022-workspace-scaling-trajectory/01-deliberation.md` §5 per D-084. **Warrant has activated this session per C2.**

**Post-activation escalation trigger.** If Session 024, 025, or 026 proposes **any further engine-v-bump**, that produces four bumps in five sessions (or three bumps in three sessions if the new bump is Session 024). Escalated trigger: the §5.4 minority elevates to substantive, and a dedicated engine-manifest.md §5 revision deliberation is warranted that session. OI-018 (R7) tracks this in open-issues.

**Alternative escalation trigger.** If an external-application workspace reports rule-drift confusion between engine-v2 / engine-v3 / engine-v4, §5.4 elevates immediately regardless of session-number pattern.

### §5.5 — Tokeniser-drift / brief-factual-error watch minority

**Position.** The 3.0× tokens-per-word ratio was measured on two files in Session 022 Honest Notes; applicability across file-types is not empirically verified. The brief's file-size estimates were inaccurate in a way that was caught only by direct workspace-inspection — this indicates a general discipline concern: session briefs citing file-size claims should use validator-measured data, not estimated.

**Source.** [01a-perspective-calibrator.md Honest Limits] + [archive: provenance/023-session-assessment/archive/023-outsider/#chunk-04, Honest Limits brief-factual-divergence observation] + synthesis §2.5.

**Activation warrant.** If any single-Read attempt on a default-read file fails due to token-budget-exceeded despite the file being under the adopted 8K word ceiling, re-measure the tokens-per-word ratio across a sample of default-read files and re-calibrate. If a future session's brief is found to have cited file-size estimates that diverge >10% from validator measurements, prompt revision to brief-authoring convention (e.g., require validator-measurement citation for file-size claims).

## 6. Watchpoints for Session 024+

**W1. Per-file drift under new budget.** If any default-read file sits above 6K soft for two consecutive sessions without restructure, the soft warning is not prompting action — revisit whether the adopted budget is enforceable at this soft-threshold. Per Outsider [01d Q6]. Specific initial trigger at Session 024: `multi-agent-deliberation.md` at 6,403 words fires the new 6K soft on adoption; Session 024 must either restructure, archive-migrate, or record an explicit decision to carry the warning through additional sessions.

**W2. Near-ceiling clustering.** If several default-read files accumulate in the 6,500–8,000-word band simultaneously, the problem is document-shape drift rather than isolated file growth; revise document-shape convention rather than tightening budget further. Per Outsider [01d Q6].

**W3. Aggregate growth.** Validator reports the aggregate default-read surface word count at every run (R3/R5). Informational at ≤90K; advisory at 90–100K; activation trigger at ≥100K or >10% single-session growth. Per Outsider [01d Q3] + Calibrator [01a Q3 alternative].

**W4. Engine-v cadence.** Any further engine-v-bump within three sessions of Session 023 elevates §5.4 to substantive per §5.4 post-activation escalation trigger. OI-018 tracks. Per Calibrator [01a Q5] + Outsider [01d Q5] + Skeptic [01c Q5].

**W5. Rationale-text accuracy.** Rationale prose making numeric claims must be validated against measured data at adoption and re-validated at each v-bump. If another spec is found with numerical factual errors in Rationale text, systematic review of Rationale prose across all specs warranted. Per Pacer [01b Q6 W4] + §5.5.

**W6. Read-contract-revision-frequency.** If `read-contract.md` §2 values are revised a second time within three sessions of the Session 023 v4 adoption, the spec's design frame (per-file word count as measurement primitive) may itself be miscalibrated — examine whether token-count or hybrid metrics would serve better. Per Calibrator [01a Q6 watchpoint 4].

## 7. Anti-laundering check

Per multi-agent-deliberation v4 §Synthesis and the Session 022 precedent, the synthesis is tested against known laundering patterns:

**Test 1 — lowering thresholds.** R1 and R2 tighten, not loosen, the per-file budget. R3 declines to relax any existing constraint; it adds a new watchpoint without removing any existing rule. No threshold lowered.

**Test 2 — dropping checks.** R5 validator changes add an aggregate report; no checks removed or weakened.

**Test 3 — widening labels.** No label widening. Per-file budget remains default-read-surface-scoped; archive-surface definition unchanged.

**Test 4 — softening mechanism-failure criteria.** No changes to the mechanism-failure criteria in any spec.

**Test 5 — specific to this session: does the value-tightening constitute "following the operator's path without actually binding"?** Potential concern: if the operator ratified "tighten to 8K" and the synthesis adopted exactly 8K without independent evaluation, this is path-following-as-laundering. Counter-evidence: the deliberation produced a three-way Q1 split (8K / 10K / 15K); the cross-family composition of the 8K position (Calibrator Claude + Outsider non-Claude) is the load-bearing adoption signal, not operator-ratification alone; 10K and no-change positions are preserved as first-class minorities; the Pacer 10K dissent is not dismissed. The operator's path-direction did not pre-determine the specific values.

**Test 6 — does engine-v4 declaration look like ceremony because the cadence warrant just fired?** Counter-evidence: Q4 unanimity is content-merits-driven (§10 pre-declaration + engine-manifest §5 mechanical trigger); engine-v-bump would be warranted even without §5.4 consideration. Q5 explicitly declines to suppress the bump for cadence reasons; the honest path is adopt-and-name-activation.

Synthesis passes tests 1-4 fully; tests 5-6 passed with explicit counter-evidence.

## 8. Honest limits

**Brief-factual-error.** The shared brief §3 file-size table I authored as orchestrator was inaccurate. The brief said "no file exceeds 5,000 words" but `multi-agent-deliberation.md` at 6,403 and `reference-validation.md` at 5,183 both exceed. I estimated rather than measuring; the estimate was wrong by ~33% on the largest file. The Outsider caught this via direct workspace-inspection; Calibrator and Pacer reasoned from the incorrect data (affecting their Q2 soft-warning-firing analyses). The synthesis above incorporates the corrected data. This is recorded as §5.5 minority-watch: brief-factual-error caught post-launch is signal the orchestrator's brief-authoring discipline needs validator-measurement citations.

**Synthesizer-original claims.** The 2.5 resolution (adopt 8K/6K acknowledging immediate soft-fire on `multi-agent-deliberation.md`) is synthesizer-original reasoning [synth]. The Calibrator and Pacer both reasoned from wrong data; the Outsider reasoned from correct data but did not explicitly compute the 6K-soft-firing consequence for `multi-agent-deliberation.md` (only noted the divergence in Honest Limits). The synthesizer's judgment to adopt 8K/6K *and explicitly acknowledge the immediate soft-fire as designed function rather than defect* is synthesizer-original.

**Single-synthesizer re-entry.** The synthesis is performed by a Claude Opus 4.7 orchestrator (same model family as Calibrator, Pacer, Skeptic). This is the pattern's highest-risk single-agent re-entry point per multi-agent-deliberation v4 §Limitations. Mitigations applied: explicit citations to perspective files; quote-over-paraphrase for load-bearing claims; majority/minority structure reported with cross-family weighting (§2); convergence vs coverage distinguished (§2.1 C1/C2 unanimous vs §2.2/§2.3 plurality-with-dissent); [synth] markers on synthesizer-original reasoning (§8 above).

**The 3.0× tokens-per-word ratio is from n=2 files.** The Calibrator [01a Honest Limits] and Pacer [01b Honest Limits] both flag this as an assumption. A future session may re-measure across a larger file sample; if the ratio diverges for spec files (say 2.5× or 3.5×), the 8K = 24K tokens calculation may need revision.

**Single-Read ceiling of ~25,000 tokens is asserted, not measured.** The brief states "unchanged since Session 022" but no perspective independently verified. If the ceiling has moved, the calibration derivation is off.

**Not all prior-session provenance was re-read for this synthesis.** I relied on default-read-surface material (specs, SESSION-LOG, 03-close.md files from all prior sessions, open-issues/index.md) + the current session's files. Archive-surface records consulted: read-contract.md §2 excerpt already in brief; Session 022 Outsider's §5.3 position preserved in read-contract.md §2 itself; Session 022 01-deliberation.md first 60 lines and §5.3/§5.4 references via citations in 03-close.md.

## 9. Cross-model evidence (paired with check 13)

Synthesis declares `cross_model: true`. Evidence distinguishing the Outsider from a Claude subagent with an edited manifest:

- **Invocation transcript.** Outsider's raw output [archive: provenance/023-session-assessment/archive/023-outsider/] (original moved to archive-pack at session close per read-contract.md v2 §9; 4 chunks; SHA-256 verified) contains the codex exec CLI banner including `OpenAI Codex v0.121.0 (research preview)`, `model: gpt-5.4`, `provider: openai`, `approval: never`, `sandbox: read-only`, `reasoning effort: xhigh`, OpenAI session id `019db6a2-ba9d-7b01-881a-75975c9c2700`. A Claude subagent would not emit this banner.
- **CLI command.** `codex exec -c model_reasoning_effort=xhigh < /tmp/023-outsider-prompt.txt > /tmp/023-outsider-response.txt 2>&1` (stdin-pipe invocation per Session 021 transport lesson). Background task id `bexunn7qx`. The `codex` binary is at `/opt/homebrew/bin/codex`, distinct from any Anthropic-routing Claude invocation.
- **Wall-clock and tool-use artefacts.** Outsider took ~6 minutes (three Claude subagents returned in ~2 minutes each). The Outsider's response contains multiple `codex` reasoning-trace markers and `exec` tool-call lines showing filesystem reads of `specifications/read-contract.md`, `specifications/engine-manifest.md`, `specifications/validation-approach.md`, `open-issues/OI-002.md`, `provenance/022-workspace-scaling-trajectory/01-deliberation.md`, and others. These are codex-specific runtime artefacts (Session 021/022 pattern; third session of this behavior). Token count: 68,078 (first codex marker).
- **Brief-factual-error detection.** Outsider's Honest Limits explicitly flagged the brief's file-size estimates as divergent from direct spot-check measurements. No Claude perspective caught this error; all three Claude perspectives reasoned from the brief's incorrect numbers. This is positive evidence that the Outsider's workspace-read (a behavior the brief's §7.D stance explicitly permits for the Outsider but not the Claude perspectives) produced a contribution Claude-only independence could not. Per multi-agent-deliberation v4 §Criterion-4 Articulation criterion 3 (recorded impact on outcomes), this counts as one criterion-3 data point for OI-004; §2.5 of this synthesis materially depended on the Outsider's correction.
- **Cross-perspective convergence pattern.** Outsider aligned with Calibrator on Q1 8K (against Pacer 10K and Skeptic 15K), with Calibrator on Q2 6K (against Pacer 7.5K and Skeptic 10K), with Calibrator + Skeptic on Q3 watchpoint-only (against Pacer's hard budget), with all three Claude on Q4 engine-v4-if-values-change, with all three Claude on Q5 treat-as-informational. Pattern is not Claude-vs-non-Claude axis; Outsider sides with different Claude perspectives on different questions. Genuine distinct-training participant signature.

Evidence passes Q6 bar. `cross_model: true` stands.
