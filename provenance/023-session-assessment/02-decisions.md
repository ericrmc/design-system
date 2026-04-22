---
session: 023
title: Decisions — Read-contract budget recalibration; engine-v3 → engine-v4
date: 2026-04-23
status: complete
---

# Decisions — Session 023

Two decisions (D-086 and D-087) adopted per the Session 023 deliberation synthesized at `01-deliberation.md`.

## D-086: Adopt R1–R10 read-contract budget revision; engine-v3 → engine-v4

**Triggers met:** [d016_2, d016_3]

**Triggers rationale:** R1–R5 substantively revise `read-contract.md` v1 → v2 (d016_2 ✓ — §2 budget values + Rationale + minority section; §10 versioning; frontmatter). R5 additionally revises `tools/validate.sh` constants substantively (engine-definition per engine-manifest.md §3). R4 updates `engine-manifest.md` §2 + §7 (documentary update per Session 021 sub-pattern; does not bump engine-manifest's own version but is part of the engine-v4 declaration). Genuine cross-family disagreement materialised (d016_3 ✓): Calibrator + Outsider 8K vs Pacer 10K vs Skeptic 15K-no-change on Q1; 3-of-4 cross-family for watchpoint-only on Q3 vs Pacer hard-aggregate; Calibrator + Outsider 6K soft vs Pacer 7.5K soft vs Skeptic 10K-no-change on Q2. d016_1 not asserted: `methodology-kernel.md` unchanged. d016_4 not asserted: the operator-ratification at session open selected the path not the value; the value-decision is deliberation-driven not operator-marked.

**d023_* triggers not asserted:** Per v4 §When Non-Claude Participation Is Required, the four required triggers are kernel modification (d023_1), multi-agent-deliberation.md substantive revision (d023_2), validation-approach.md substantive revision touching semantic Tier 2 validation (d023_3), OI-004 state change (d023_4). None of these engine-definition specs are modified in this session's decisions. Revision to `read-contract.md` is not in the D-023 enumerated list. Non-Claude Outsider participation occurred voluntarily per v4 §When Non-Claude Participation Is Required clause 2 ("Non-Claude participation is recommended for other decisions that meet the multi-agent triggers above"). OI-004 tally-impact recorded in D-087: voluntary participation advances criterion-3 data but does not advance criterion-2 (required-trigger tally).

**Decision:**

Ten recommendations adopted per synthesis [01-deliberation.md §3]:

**R1.** `read-contract.md §2` hard ceiling revised **15,000 words → 8,000 words**. Adopted per Calibrator [01a Q1] + Outsider [01d Q1] cross-family convergence. Pacer's 10K position and Skeptic's no-change position preserved as first-class minorities §5.1 and §5.2 respectively.

**R2.** `read-contract.md §2` soft warning revised **10,000 words → 6,000 words**. Adopted per Calibrator [01a Q2] + Outsider [01d Q2] cross-family convergence. ~75% of hard-ceiling ratio articulated in spec text. Pacer's 7.5K position preserved as §5.1 paired minority. Known consequence recorded: `multi-agent-deliberation.md` at 6,403 words exceeds new 6K soft and fires on adoption. This is the designed function of the soft warning (prompt restructure before ceiling-breach); Session 024 responds per read-contract §8 remediation options.

**R3.** Aggregate default-read surface treated as **watchpoint only**, not hard budget. Validator reports aggregate word count in every Tier 1 run; advisory threshold ≥90,000 words; activation trigger ≥100,000 words OR >10% single-session growth without compensating restructure. Adopted per Calibrator [01a Q3] + Skeptic [01c Q3] + Outsider [01d Q3] 3-of-4 cross-family convergence. Pacer's hard-aggregate-budget position (90K hard / 80K soft) preserved as §5.3 minority.

**R4.** `engine-manifest.md` §2 declares **`engine-v4`** (was `engine-v3`); §7 history extended with engine-v4 entry naming D-086 as bump driver, citing the read-contract.md v1→v2 revision and validate.sh constants revision as the substantive changes. §3 engine-definition file set unchanged (no new files; no removed). Frontmatter `last-updated: 2026-04-23` + `updated-by-session: 023`. Per Q4 unanimous-conditional (C1 in synthesis): §10 pre-declaration classifies §2 budget-value changes as substantive; engine-manifest §5 mechanically requires v-bump. engine-manifest.md's own version unchanged at v1 per Session 021 sub-pattern (documentary updates to a tracking spec do not bump the tracking spec).

**R5.** `tools/validate.sh` updated: `DEFAULT_READ_HARD_WORD_CEILING=8000` (was 15000); `DEFAULT_READ_SOFT_WORD_CEILING=6000` (was 10000); `READ_CONTRACT_ADOPTION_SESSION` unchanged at 22 (the adoption-session pre-date of the original spec, not this revision). No check-logic changes. New aggregate-default-read-surface report added to check 20's output as informational (not pass/fail/warn).

**R6.** `read-contract.md` v1 preserved as `read-contract-v1.md` with frontmatter updated to `status: superseded`, `superseded-by: read-contract.md (v2)`, `superseded-at-session: 023`. Body byte-identical to the Session 022 adoption. Continuation of the Session 011/017/019/021/022 v1→v2-preservation pattern.

**R7.** **Open new OI-018**: "Revisit engine-manifest.md §5 bump-trigger criteria in light of §5.4 cadence minority activation." Adopted per Skeptic [01c Q5] + Outsider [01d Q5] shared recommendation. Activation trigger: engine-v5 proposed before Session 026 OR external-application portability confusion observed. Session 024+ may undertake the deliberation if the trigger fires.

**R8.** **OI-002 10th data point.** Substantive revision to `read-contract.md` v1 → v2 classified per heuristic; heuristic continues to hold stable; no formal update to OI-002's substantive-vs-minor text.

**R9.** **§5.4 Session 022 engine-version-cadence minority warrant activates.** Recorded in engine-manifest.md §7 engine-v4 history entry. Per Q5 unanimity (C2 in synthesis): activation is informational; record-and-proceed, not suppress-bump-via-reclassification. Post-activation escalation trigger: any further engine-v-bump in Sessions 024/025/026 elevates §5.4 to substantive and forces a dedicated engine-manifest §5 revision deliberation in that session. OI-018 (R7) tracks.

**R10.** **Preserve five first-class minorities** per synthesis §5 with concrete operational activation warrants: §5.1 Pacer 10K/7.5K minority; §5.2 Skeptic no-change + warrant-literalism minority; §5.3 Pacer aggregate-hard-budget minority; §5.4 Session 022 engine-version-cadence minority (now activated); §5.5 tokeniser-drift / brief-factual-error watch minority. Record six watchpoints per synthesis §6 for Session 024+ monitoring.

**Key arguments carried:**
1. Calibration-fidelity [01a Q1]: 15K hard ceiling was adopted on incorrect 1.3× tokens-per-word assumption; empirically 3.0×; 15K ≈ 45K tokens ≈ 1.8× single-Read ceiling, materially more permissive than §2 Rationale claimed.
2. Cross-family convergence [01a + 01d Q1 Q2]: Calibrator (Claude) + Outsider (non-Claude) independently converged on 8K hard / 6K soft. Plurality cross-family-composition is the load-bearing adoption signal.
3. §10 mechanical pre-declaration [01a Q4, 01b Q4, 01c Q4, 01d Q4]: unanimous-conditional on engine-v4 if values change; no narrow minor-classification pathway available that doesn't require re-reading §10 against plain text.
4. Cadence-transparency [01a Q5, 01b Q5, 01c Q5, 01d Q5]: unanimous that §5.4 warrant activation is informational not distorting; suppressing the bump via reclassification would be worse than adopting it and naming the activation.
5. Outsider's brief-factual-error catch [01d Honest Limits]: my brief §3 file-size table was inaccurate (stated max 4,800 words; actual multi-agent-deliberation.md at 6,403). The Outsider's direct workspace-read produced a contribution Claude-only reasoning could not. §2.5 of synthesis materially depended on the correction.

**Rejected alternatives:**
- **Pacer 10K/7.5K** [01b Q1, Q2] — Preserved as §5.1 minority with activation warrant (3 restructure-for-budget events in 5 sessions OR content-coherence damage from 8K-driven split).
- **Skeptic no-change + prose-correction-only** [01c Q1] — Preserved as §5.2 minority with activation warrant (if no file exceeds 7.5K by Session 027 without restructure, Skeptic position retroactively vindicated).
- **Pacer aggregate hard budget at 90K/80K** [01b Q3] — Preserved as §5.3 minority with activation warrant (aggregate exceeds 100K OR >10% single-session growth).
- **Same-session revision to engine-manifest §5 bump criteria** — Unanimously rejected; deferred to Session 024+ via OI-018.
- **Skeptic minor-correction-of-Rationale-only pathway** [01c Q4 Reading 2] — The value-change in R1-R2 forecloses this counterfactual; the argument remains preserved as part of §5.2 for its vindication condition.

**What remains open:**
- Session 024 response to the immediate 6K-soft-fire on `multi-agent-deliberation.md`: restructure, archive-migrate, or carry the warning through additional sessions with explicit decision-record.
- OI-018 engine-manifest §5 revision deliberation, if §5.4 escalation trigger fires.
- Empirical validity of the 3.0× tokens-per-word ratio across a broader sample of default-read files (WX-022-2 / §5.5 watch).
- Aggregate default-read surface growth trajectory (W3 watch).

## D-087: OI state housekeeping

**Triggers met:** [none]

**Triggers rationale:** Session-housekeeping per D-073/D-077/D-079/D-081/D-083/D-085 precedent. No kernel or specification modification in this decision (those are D-086's work). No d023_* trigger: no kernel/MAD/validation-approach/OI-004 state change asserted in D-087 itself. The OI-002 data-point tally update is bookkeeping; the OI-018 opening is bookkeeping of D-086's R7; the §5.4 cadence minority activation is bookkeeping of D-086's R9; OI-004 tally is unchanged (no required-trigger deliberation this session).

**Decision:**

1. **OI-002 10th data point** recorded. Session 023 executes one substantive revision (`read-contract.md` v1 → v2) and one new OI opening (OI-018). Both within the existing heuristic's scope. Heuristic continues to hold stable across 10 data points.

2. **OI-004 tally unchanged at 7-of-3 required-trigger threshold.** Session 023 is a voluntary non-Claude session per D-086's `d016_2` + `d016_3` triggers without any `d023_*` trigger firing (read-contract.md is not in the D-023 enumerated list). Seventh consecutive non-advancing non-Claude session after Sessions 007, 008, 010, 012, 013, 020, 022. Voluntary:required ratio extends to **8:8** (first session since Session 021 where voluntary-count matches required-count). Criterion-3 cumulative data points: **65** across Sessions 005–023 (+5 added Session 023 per synthesis §9 Outsider-unique contributions: (1) brief-factual-error catch via workspace-inspection; (2) 8K calibration convergence independent of Calibrator's reasoning route; (3) 6K fixed soft argument against percentage-formula framing; (4) "e.g., 100K words" activation-threshold refinement matching Session 022 preservation text; (5) 10%-growth-rate single-session trigger for aggregate watchpoint).

3. **OI-007 count advances 12 → 13.** OI-018 opened per D-086 R7. No OI resolved this session.

4. **OI-015 positive exercise (5th).** Session 023 Read activity surfaced the operator's Path (C) ratification as input to the deliberation, not as given context; the deliberation's Q1 positions include no-change (Skeptic) and middle-value (Pacer), not just the operator's 8K direction. The synthesis [§7 Anti-laundering check Test 5] explicitly addressed path-following-as-laundering risk with counter-evidence (cross-family composition, minority preservation, three-way Q1 split). 5th positive exercise of the OI-015 reconciliation discipline after Sessions 013, 016, 020, 022.

5. **New OI-018 opened.** File: `open-issues/OI-018.md`. Title: "Revisit engine-manifest.md §5 bump-trigger criteria in light of §5.4 cadence minority activation." Surfaced Session 023; status Open. Full text per D-086 R7 activation trigger: engine-v5 proposed before Session 026 OR external-application portability confusion observed.

6. **§5.4 Session 022 engine-version-cadence minority** status updated to **"activated this session"** in `provenance/022-workspace-scaling-trajectory/01-deliberation.md` reference from this session's close and in `engine-manifest.md` §7 history. Minority warrant text preserved verbatim per the first-class-minority-preservation discipline; no spec text of Session 022 is edited (D-017 immutability).

**Rejected alternatives:**
- **OI-004 tally advance claim on voluntary-non-Claude grounds.** Considered and rejected per Session 007 D-049 / Session 008 D-052 / Session 010 D-059 / Session 012 D-065 / Session 013 D-068 / Session 020 D-081 / Session 022 D-085 precedent: voluntary non-Claude participation without D-023 trigger firing contributes to criterion-3 data-points but does not advance criterion-2 required-trigger tally.
- **Close §5.4 minority as "resolved by adoption"** rather than activating it. Rejected per Q5 unanimity: activation is the honest state; the concern the minority raises (engine-version-meaning-loss via cadence) is live until resolved by either an elongated stability period or a dedicated deliberation.

**What remains open:**
- OI-018 engine-manifest §5 revision deliberation availability in Session 024+.
- OI-004 criterion-2 required-trigger tally (7-of-3; unchanged).
- OI-004 criterion-4 closure retrospective (state 3 "Articulated; awaiting closure-retrospective"; not advanced this session).
