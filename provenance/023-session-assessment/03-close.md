---
session: 023
title: Close — Read-contract budget recalibration; engine-v3 → engine-v4
date: 2026-04-23
status: complete
---

# Close — Session 023

## Artefacts produced

### Provenance (`provenance/023-session-assessment/`)

- `00-assessment.md` — session-open assessment: Session 022 audit across five close-directed dimensions; validator-at-open 574 pass clean; six-path presentation; halt for operator direction.
- `01-brief-shared.md` — shared deliberation brief (§1 methodology context; §2 problem statement + calibration-error evidence; §3 current state facts + file-size table; §4 current spec text excerpts; §5 survey of adjacent traditions; §6 Q1–Q6 design questions; §7 four role-specific stances A–D; §8 response format; §9 anti-import constraint; §10 closure). Committed as deliberation anchor at commit `1c9f452`.
- `01a-perspective-calibrator.md` — Claude Opus 4.7 subagent output (verbatim). Position: 8K hard / 6K soft; aggregate as watchpoint; engine-v4; cadence informational.
- `01b-perspective-pacer.md` — Claude Opus 4.7 subagent output (verbatim). Position: 10K hard / 7.5K soft; aggregate as hard budget 90K/80K; engine-v4; cadence informational.
- `01c-perspective-skeptic.md` — Claude Opus 4.7 subagent output (verbatim; adversarial role). Position: no budget change (Rationale prose correction only); 10K soft retained; defer aggregate; engine-v3 retained if no value change; record §5.4 warrant; defer engine-manifest §5 revision to Session 024+.
- `01d-perspective-outsider.md` → **archive-packed at close per read-contract.md v2 §9** (20,142 words exceeded 8K hard ceiling). Archive-pack at `archive/023-outsider/` (4 chunks, 50KB each; byte-range boundaries; SHA-256 verified). Original file removed from provenance root; content preserved byte-identical in archive. Outsider position (OpenAI GPT-5.4 via codex exec, session id `019db6a2-ba9d-7b01-881a-75975c9c2700`, tokens_used 68,078, reasoning effort xhigh): 8K hard / 6K fixed soft; aggregate as watchpoint with advisory ≥90K + activation ≥100K or >10% single-session growth; engine-v4 mechanically required; record cadence warrant activated; raise burden for near-term further bumps. Outsider caught brief-factual-error: `multi-agent-deliberation.md` measured at 6,403 words, not the brief's estimated 4,800.
- `01-deliberation.md` — synthesis. Maps Q4/Q5 unanimous convergences (C1 engine-v4 if value change; C2 cadence informational); Q1 three-way split (8K / 10K / 15K) with 2-of-4 cross-family plurality for 8K (Calibrator Claude + Outsider non-Claude); Q2 same split pattern with 6K convergence; Q3 3-of-4 cross-family for watchpoint-only. Recommends R1–R10 for adoption; preserves five first-class minorities §5.1–§5.5 with operational activation warrants. Anti-laundering check (§7) passes all six tests. Brief-factual-error explicitly recorded in §2.5 and §8.
- `02-decisions.md` — two decisions. D-086 adopts R1–R10 with `triggers_met: [d016_2, d016_3]`. D-087 OI housekeeping with `triggers_met: [none]`.
- `03-close.md` — this file.
- `manifests/calibrator.manifest.yaml`, `pacer.manifest.yaml`, `skeptic.manifest.yaml`, `outsider.manifest.yaml` — per-participant D-024 manifests with v4 schema fields.
- `participants.yaml` — session-level index with `oi004_qualifying_participants: [outsider]` and `participants_family: cross-model`.
- `archive/023-outsider/` — archive-pack of Session 023 Outsider perspective file (20,142 words → 4 chunks; byte-range boundaries; SHA-256 source hash `fcc550628ef2cad6fa7ff2e9c44ebdf042e40d709cc060e200045de0a166a214` matches concatenation).

### Specifications revised substantively

- **`read-contract.md` v1 → v2** (D-086 R1–R4). §2 hard ceiling revised 15,000 → 8,000 words; §2 soft warning revised 10,000 → 6,000 words; §2 Rationale rewritten with empirically-correct 3.0× tokens-per-word ratio (v1 used incorrect 1.3×); §2 known-consequence note added (`multi-agent-deliberation.md` at 6,403 words fires new 6K soft on adoption); §2 minority-positions section added preserving §5.1 Pacer 10K/7.5K, §5.2 Skeptic no-change + warrant-literalism, §5.3 Pacer aggregate-hard-budget, §5.5 tokeniser-drift watch; §2a aggregate default-read surface report added with advisory threshold ≥90,000 and activation threshold ≥100,000 words OR >10% single-session growth; §10 Versioning updated with v2 history entry + WX-024 watchpoint against re-revision-within-3-sessions design-frame miscalibration. v1 preserved as `read-contract-v1.md` with `status: superseded`, `superseded-by: read-contract.md (v2)`, `superseded-at-session: 023`.

### Tooling updated substantively

- **`tools/validate.sh`** (D-086 R5). Constants `DEFAULT_READ_HARD_WORD_CEILING=8000` (was 15000) + `DEFAULT_READ_SOFT_WORD_CEILING=6000` (was 10000). New constants `DEFAULT_READ_AGGREGATE_ADVISORY=90000` and `DEFAULT_READ_AGGREGATE_ACTIVATION=100000`. Check 20 output extended with aggregate default-read surface report (informational; not pass/fail/warn) per read-contract.md v2 §2a. Session 023 engine-v4 bump is substantive per engine-manifest.md §5.

- **`engine-manifest.md`** (D-086 R4). §2 declares `engine-v4` (was `engine-v3`); §3 heading reflects engine-v4 (file set unchanged from engine-v3; no files added or removed); §7 history extended with engine-v4 entry citing D-086 and naming the substantive changes. Frontmatter `last-updated: 2026-04-23` + `updated-by-session: 023`. engine-manifest.md's own version unchanged at v1 per Session 021 sub-pattern (documentary updates to a tracking spec do not bump the tracking spec).

### Development-provenance files amended

- **`open-issues/OI-002.md`** — Session 023 10th data point appended. Heuristic continues to hold stable.
- **`open-issues/OI-018.md`** — new OI file (R7). "Revisit engine-manifest.md §5 bump-trigger criteria in light of §5.4 cadence minority activation." Open; deferred; activation-trigger-gated (engine-v5 before Session 026 OR external-application portability confusion).
- **`open-issues/index.md`** — OI-018 added; active count 12 → 13; OI-002 note updated; OI-004 voluntary:required 7:8 → 8:8; OI-015 positive-exercise count 4 → 5.

### No external artefact this session

Session 023 is a self-development deliberation session producing engine-definition revisions. No external artefact produced; no `applications/` directory changes.

### Engine-version transition — engine-v3 → engine-v4

This is the methodology's **third engine-version increment**. Notable: first engine-v-bump driven by budget-value recalibration on calibration-correctness grounds (prior bumps were new-spec-creation, v-bump-of-existing-specs, or schema-addition). Also the **second bump in adjacent sessions** (engine-v3 Session 022; engine-v4 Session 023) and the **third in four sessions** (engine-v2 Session 021; engine-v3 Session 022; engine-v4 Session 023). **Session 022 §5.4 Skeptic engine-version-cadence minority warrant activates.** Recorded in engine-manifest.md §7 history entry and tracked by new OI-018. Post-activation escalation trigger: any further engine-v-bump in Sessions 024/025/026 elevates §5.4 to substantive and forces a dedicated engine-manifest §5 revision in that session.

### SESSION-LOG.md

Session 023 entry added at close per R8a thin-index form.

## Decisions made

- **D-086** — Adopt R1–R10 read-contract budget recalibration; engine-v3 → engine-v4. Triggers: `[d016_2, d016_3]`. Voluntary non-Claude Outsider participation (d023_* not triggered; read-contract.md not in D-023 enumerated list). OI-004 criterion-3 gains 5 data points (cumulative 65).
- **D-087** — OI state housekeeping. OI-002 10th data point; OI-018 opened; OI-015 5th positive exercise; OI-004 tally unchanged at 7-of-3 required (voluntary:required rebalances 7:8 → 8:8). Triggers: `[none]`.

## Validation

`tools/validate.sh` at close: **PASS expected once SESSION-LOG update committed**. Pre-close run: 613 pass, 2 fail, 1 warn (1 fail for expected "Session 023 missing from SESSION-LOG.md" being addressed in this close; 1 warn is designed consequence per §1 below).

### Tier 1 Structural Checks

- Checks 1–19: pass per engine-v4 baseline (SESSION-LOG entry added at this close).
- Check 20 (default-read surface per-file budget): **1 soft warning** fires as designed. `specifications/multi-agent-deliberation.md` at 6,386 words exceeds new 6,000-word soft warning (within 8,000-word hard ceiling). Expected and explicitly recorded in D-086 R2 as designed soft-warning function. Session 024 responds per read-contract v2 §8 remediation options (reduce, split, or relocate to archive).
- Check 21 (archive-pack manifest integrity): 5 archive-packs pass — pre-R8a-SESSION-LOG, pre-R8b-open-issues, 014-oi016-outsider, 022-outsider, **and new 023-outsider** (source_hash_sha256 `fcc550628ef2cad6fa7ff2e9c44ebdf042e40d709cc060e200045de0a166a214` verified).
- Check 22 (archive-pack citation consistency): all `[archive: path]` references in default-read files resolve. New references in this session: archive/023-outsider/ cited from 01-deliberation.md and from the decision record; references to 022-outsider/ cited from read-contract.md §2a and 00-assessment.md.
- Aggregate default-read surface report (new in v4): current aggregate at engine-v4 adoption approximately 83K words; below 90K advisory; below 100K activation.

### Tier 2 Guided Assessment

1. **Provenance continuity (Q1).** Yes. Session 023 Read drew on Session 022 close (six-path presentation + audit dimensions); Session 021 close (engine-v2 bump precedent); Session 020 close (Outsider type-drift frame-replacement precedent); the Session 022 Outsider §5.3 minority preserved in read-contract.md §2. Path (C) operator ratification treated as path-selection not value-binding; synthesis produced three-way Q1 split including no-change (Skeptic) and middle-value (Pacer) not pre-determined by operator direction. No silent re-proposing of past rejections.

2. **Specification consistency (Q2).** Yes. read-contract.md v2's revised §2 is internally consistent (§2 values match §2 Rationale derivation; §2a aggregate thresholds are well-ordered 90K < 100K; §10 versioning updated with v2 pre-declaration still naming §2 budget values as substantive). validate.sh constants match read-contract.md v2 values. engine-manifest.md §2 + §7 consistent with declared engine-v4 and with §3 engine-definition file set unchanged. No cross-spec inconsistencies.

3. **Adversarial quality (Q3).** Yes. Skeptic was genuinely adversarial: argued for no-budget-change on warrant-literalism grounds against Calibrator + Pacer + Outsider; argued for engine-v3 retention contingent on Q1; argued the cadence concern should materialise as immediate-defer rather than proceed-and-record; proposed OI-018 as defer-to-Session-024 mechanism. Skeptic's positions preserved as §5.2 minority with specific vindication-warrant (no file above 7.5K by Session 027 without restructure); Skeptic's §5.4 cadence concern and OI-018 opening directly adopted by synthesis despite declining the no-change position. Adversarial role shaped outcomes.

4. **Meaningful progress (Q4).** Yes. Substantive budget recalibration grounded in empirical correction; new aggregate report adds observability against accretion failure mode; engine-v4 bump honestly declared with activated §5.4 minority; OI-018 opens an operational handle for future engine-manifest §5 deliberation. The brief-factual-error caught by Outsider became a teaching data point for future brief-authoring convention (§5.5 minority-watch).

5. **Specification-reality alignment (Q5).** Yes — strengthened. Pre-session: read-contract.md §2 Rationale cited an empirically-wrong 1.3× tokens-per-word ratio, making the 15K ceiling 1.8× the single-Read tool limit rather than the "headroom below single-read" the Rationale claimed. Post-session: §2 values (8K/6K) align with the Rationale's stated intent at the correct 3.0× ratio. Known consequence: multi-agent-deliberation.md fires soft warning on adoption — explicitly recorded rather than silently tolerated.

6. **Cross-model-honesty evidence (Q6).** Yes. Synthesis declares `cross_model: true`. Concrete evidence per 01-deliberation.md §9: codex exec CLI banner preserved in [archive: provenance/023-session-assessment/archive/023-outsider/] chunk 01; model gpt-5.4; provider openai; session id 019db6a2-ba9d-7b01-881a-75975c9c2700; 68,078 tokens first-marker. Outsider manifest declares `training_lineage_overlap_with_claude: independent-claim`, `participant_organisation: openai`, `independence_basis: organization-distinct`. Material contribution: the brief-factual-error catch (Outsider noted multi-agent-deliberation.md at >5K via direct workspace-read; no Claude perspective caught this; Synthesis §2.5 materially depended on the correction). Per multi-agent-deliberation v4 §Criterion-4 Articulation criterion 3, this is one new criterion-3 data point for OI-004.

7. **Trigger-coverage plausibility (Q7).**
   - **D-086 declares `[d016_2, d016_3]`.** Reading D-086's Decision text: R1–R5 substantively revise read-contract.md and tools/validate.sh (d016_2 ✓); R4 engine-manifest.md §2+§7 updates are documentary per Session 021 sub-pattern (no own version bump but part of engine-v4 declaration). Three-way Q1 split + 3-of-4 vs 1 Q3 split + non-unanimous Q2 all materially disagreed (d016_3 ✓). d016_1 not asserted: methodology-kernel.md unchanged. d016_4 not asserted per synthesis: the operator-ratification at session open selected the path, not the value; the value-decision is deliberation-driven. d023_* not asserted: read-contract.md not in D-023 enumerated list; Outsider participation voluntary per multi-agent-deliberation v4 clause-2 recommended-not-required.
   - **D-087 declares `[none]`.** Housekeeping per D-073/D-077/D-079/D-081/D-083/D-085 precedent. No kernel/spec/MAD/validation-approach revision in D-087 itself; no OI-004 state change asserted. `[none]` consistent per precedent.
   - No `**Non-Claude participation:** skipped` annotations; none required.

8. **OI-004 closure-retrospective substantive adequacy (Q8).** N/A this session — no `oi-004-retrospective.md` present.

9. **Read-contract adherence (Q9; in v5).**
   - (a) Default-read surface read at session open: all 33 enumerated files read per 00-assessment.md §4.
   - (b) Archive-surface records cited via `[archive: path]` convention in default-read files: read-contract.md v2 §2a cites archive/022-outsider/ chunk-04 for the Outsider §5.3(b) proposal; 01-deliberation.md §5.1 / §9 cite 023-outsider/ archive-pack; 00-assessment.md §3.1 WX-22-1 audit cited 022-outsider archive-pack. Check 22 resolves all.
   - (c) Honest-limits on non-reads declared in §8 of 01-deliberation.md and §4 of 00-assessment.md: Session 001 has no 03-close.md (structural note); I did not re-read full archive chunks of Session 022 Outsider beyond chunk 04 content-inspection.

## Honest notes from the session

- **Orchestrator brief-factual-error caught by Outsider.** My shared brief §3 file-size table estimated `multi-agent-deliberation.md` at 4,800 words; actual is 6,403 words. Two other specs in the brief table were also off (reference-validation.md at 5,183 not listed; validation-approach.md roughly correct at 4,664). The Outsider performed direct workspace-read during the independent phase and flagged the divergence in Honest Limits. The three Claude perspectives reasoned from the incorrect estimates; their Q2 soft-warning-firing analyses were based on "largest file at 4,800" when actual is 6,403. Synthesis §2.5 incorporated the corrected data. Preserved as §5.5 tokeniser-drift / brief-factual-error-watch minority with activation warrant: future briefs citing file-size claims should use validator-measured data, not estimated. This finding is the strongest single cross-model contribution of Session 023 — no Claude-only independence would have caught this.

- **Synthesis judgment on 2-of-4 cross-family plurality.** The Q1 8K adoption rests on 2-of-4 cross-family convergence (Calibrator Claude + Outsider non-Claude), not absolute majority. Pacer's 10K (1-of-4 Claude) and Skeptic's 15K no-change (1-of-4 Claude) are genuine dissents. The cross-family composition is the load-bearing adoption signal per multi-agent-deliberation v4 §Synthesis conventions; Session 020 and Session 014 precedents for 2-of-4-cross-family-vs-2-of-4-intra-family resolution support this. Both dissents preserved as first-class minorities with specific vindication-warrants.

- **Immediate soft-warning firing on adoption is the mechanism working.** `multi-agent-deliberation.md` at 6,386 words (measured by the new validator) exceeds the new 6,000-word soft warning. Session 024 responds per read-contract v2 §8. The Outsider's framing [01d Q1]: "meaningfully binding without being immediately disruptive" — a file at 80% of hard ceiling should fire soft warning; that is what soft warnings are for. The Pacer's 10K position would have avoided this immediate firing but at the cost of the calibration-fidelity the §2 Rationale articulates.

- **§5.4 Session 022 engine-version-cadence minority warrant activated.** First explicit activation of a Session 022 minority warrant. All four Session 023 perspectives recognised this and agreed (Q5 unanimity) that the honest response is record-and-proceed, not suppress-bump-via-reclassification. OI-018 opens the operational handle for Session 024+ if further cadence pressure materialises.

- **Three engine-v-bumps in four sessions is a pattern.** Session 021 engine-v2 (OI-004 criterion-4 articulation); Session 022 engine-v3 (new read-contract spec + three v-bumps); Session 023 engine-v4 (read-contract budget recalibration). Each is substantively warranted on content merits. The cadence pattern itself is now a watchpoint per W4 + OI-018.

- **Codex exec Outsider behavior stable at n=3 pre-response workspace exploration.** Session 021 was first; Session 022 second; Session 023 third. Pattern now stable: the Outsider routinely reads workspace files before producing its response, catching orchestrator-brief errors and grounding reasoning in actual spec text. This is a positive property but also a divergence from the multi-agent-deliberation v4 §Workspace context per perspective rule (Claude perspectives do not read; Outsider does). Worth Session 024+ attention: should the spec be updated to document this asymmetry explicitly, or should the Outsider-read behavior be constrained?

- **No brief-priming streak count maintained this session.** Session 022 close did not continue the Session 008-017 brief-priming-absent tally. The Outsider's concrete terminology ("calibration fidelity," "budget as commitment," "empirical falsification") entered the synthesis vocabulary. Session 023's brief borrowed Session 022 synthesis vocabulary ("default-read surface," "archive surface," "bounded-read-contract frame") consistent with the spec it was revising; this is spec-continuity rather than brief-priming. The §5.5 tokeniser-drift minority is the Session 023 observation worth Session 024+ audit of brief-authoring-discipline.

- **Session 023 did not advance OI-004 required-trigger tally.** D-086 declares no `d023_*` triggers (read-contract.md is not in D-023's enumerated list); Outsider participation is voluntary. Seventh consecutive non-advancing non-Claude session. Voluntary:required ratio rebalances to 8:8. Criterion-3 cumulative 65 data points. OI-004 criterion 4 remains articulated (state 3); no closure-retrospective attempted.

## Next session

Session 024 should:

1. Run `tools/validate.sh` at start. Expected baseline: **613 pass, 0 fail, 1 warn** (the warn is the designed 6K-soft-fire on `multi-agent-deliberation.md`; it persists until Session 024 responds per read-contract v2 §8).

2. **Respond to the multi-agent-deliberation.md soft-warning-firing.** This is the first operational test of the new 6K/8K budget. Options per read-contract v2 §8:
   - **Restructure in place.** Reduce the file to under 6K (soft clears) or under 5.2K (well-clear). Risk: content-coherence damage. Unlikely sufficient — the file has substantive content.
   - **Split into multiple default-read files.** E.g., §Criterion-4 Articulation could move to a new `multi-agent-deliberation-criterion4.md` while preserving cross-references. Risk: fragmentation; cross-reference maintenance cost.
   - **Relocate detail to archive surface.** E.g., §Heterogeneous-Participant Recording Schema's full field enumerations could move to a per-schema archive-pack while preserving the governance text at default-read. Risk: readers must follow references.
   - **Carry the warning through additional sessions with explicit decision-record.** Legitimate per read-contract §8 ("the next session should consider restructuring"); consider does not mean execute. If content does not grow, the warning becomes routine state.

   Session 024 deliberation should weigh these options. The §5.1 Pacer minority and §5.2 Skeptic minority both watch: if the adopted response is "restructure" driven by budget alone rather than by content-completion, the §5.1 activation trigger advances; if the adopted response is "carry the warning" for a session or two without degradation, the §5.2 vindication condition strengthens.

3. Audit Session 023 synthesis fidelity. Particular attention to:
   - **Whether the 2-of-4 cross-family plurality for 8K was genuinely load-bearing** or whether the synthesizer reached for cross-family composition when Pacer's 10K was the stronger Claude-weighted middle position. Examine [01b Q1] asymmetric-cost-of-binding argument against [01a Q1] + [archive: provenance/023-session-assessment/archive/023-outsider/#chunk-04] (Q1 position) calibration-fidelity arguments.
   - **Whether the brief-factual-error catch was faithfully incorporated** or post-hoc-rationalised. Examine §2.5 of 01-deliberation.md against the Outsider's actual Honest Limits text [archive: provenance/023-session-assessment/archive/023-outsider/#chunk-04].
   - **Whether multi-agent-deliberation.md's 6K-soft-fire at close is the mechanism working** or evidence of premature budget tightening. This is the test condition for §5.1 and §5.2 minorities.

4. Consider agenda options (no default pre-commitment; halt for operator direction):

   **(A) Session 024-specific: respond to multi-agent-deliberation.md soft-fire** per point 2 above. D-023-triggering (any substantive revision to multi-agent-deliberation.md fires d023_2; this would require non-Claude participation). This is the most session-specific option.

   **(B) OI-004 closure-retrospective draft.** State 3 → state 4 attempt. D-023-triggering.

   **(C) Cell 1 re-attempt of reference-validation.** Unexercised across Sessions 020–023.

   **(D) OI-015 laundering-gap deliberation.** Session 023 is 5th positive exercise; urgency soft.

   **(E) OI-018 engine-manifest §5 revision.** Activation-trigger-gated; not yet active.

   **(F) Operator-directed agenda.**

5. **Halt for operator ratification** before substantive execution on any path.

6. **Session 023 watchpoints active from Session 024:**
   - W1 per-file drift (primary: multi-agent-deliberation.md 6K-soft firing).
   - W2 near-ceiling clustering.
   - W3 aggregate growth (current ~83K; advisory 90K; activation 100K or >10% single-session).
   - W4 engine-v cadence (any further bump in 024/025/026 elevates §5.4).
   - W5 Rationale-text accuracy.
   - W6 read-contract-revision-frequency (no re-revision within 3 sessions per WX).

7. **§5.4 Session 022 cadence minority is now activated.** Any Session 024 proposal to bump engine-v5 must engage this minority directly in its deliberation and provide explicit cadence-justification per OI-018 scope.

8. **Engine-v4 portability check for Session 024+ onward.** An external-application workspace initialising from engine-v4 inherits the new 8K/6K per-file budget and aggregate report. If a Session 024+ external-application initialisation surfaces engine-v4-specific friction (e.g., the new budget fires on a fresh-clone template file; the aggregate report's thresholds are inappropriate for fresh workspaces), this is a portability bug worth recording as a new OI.
