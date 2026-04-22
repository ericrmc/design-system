ric ratios. Session 022’s honest note is enough evidence that this matters.
- **Versioning pressure.** If another engine bump is proposed quickly, require an explicit statement of why a minor-edit path is unavailable under the live rules.

I would **not** preserve a “budget-value changes are minor” minority as first-class. Under the present texts it is too weakly grounded; it is closer to a proposal to rewrite the rules than a plausible reading of them.

## Honest Limits

I did not read any current-session other-perspective output or any other §7 stance. The only current-session files I read were `provenance/023-session-assessment/00-assessment.md` and `provenance/023-session-assessment/01-brief-shared.md` for a mechanical word-count spot-check.

I read these workspace files directly: `specifications/read-contract.md`, `specifications/engine-manifest.md`, `specifications/validation-approach.md`, `open-issues/OI-002.md`, `provenance/022-workspace-scaling-trajectory/01-deliberation.md` (relevant §5.3-§5.4 sections), `provenance/022-workspace-scaling-trajectory/03-close.md`, `provenance/022-workspace-scaling-trajectory/archive/022-outsider/manifest.yaml`, and an excerpt from `[archive: provenance/022-workspace-scaling-trajectory/archive/022-outsider/#chunk-04]`. I also ran a mechanical word-count scan across active default-read files sufficient to estimate aggregate size; I did not rely on that scan for the main argument because some spot-check counts diverged from the brief’s stated file-size facts.

My largest unresolved uncertainty is that divergence: my spot-check suggested at least some active specs are longer than the brief reports (for example `specifications/multi-agent-deliberation.md` and `specifications/reference-validation.md` appeared above 5,000 words), while the brief says no default-read file exceeds 5,000 words. I did not resolve that discrepancy, so for Q1-Q3 I treated the brief’s numbers as the official deliberation baseline.

I did not inspect `tools/validate.sh` in full, only the constants/check references surfaced through search. My Q3 position also rests on an assumption rather than direct proof: that aggregate-burden remediation is currently awkward because the default-read enumeration and closed-session immutability make retroactive reduction structurally hard.

## Meta-note

My strongest likely cross-model divergence is this: I think the empirical falsification of the 15K rationale is by itself enough to justify tightening to 8K now, even though the Session 022 activation warrant did not literally fire. I expect some Claude positions may give more weight to warrant literalism, compromise at 10K, or cadence caution. I do not think those are stronger than correcting a budget whose own stated calibration has already failed.
tokens used
68,078
## Q1. Hard ceiling value

**8,000 words.**

The decisive issue is not whether the Session 022 Outsider activation warrant literally fired. It did not. The decisive issue is that the adopted calibration for `read-contract.md §2` has already been falsified. The current rationale says 15,000 words sits below a ~25,000-token single-read ceiling because it assumed ~1.3 tokens per word. Session 022’s close notes say the workspace’s prose-with-markdown files are empirically closer to ~3.0 tokens per word, making 15,000 words roughly 45,000 tokens and 10,000 words roughly 30,000 tokens (`provenance/022-workspace-scaling-trajectory/03-close.md`; brief §2-§3). On that calibration, 15K is not a ceiling relative to single-read effort; 12K and 10K are still above the stated single-read anchor.

`read-contract.md §2` was justified as a reader-contract, not just an anti-explosion number. If default-read means “read in full at every session open,” then a per-file ceiling that routinely requires paginated reading is misaligned with the rule’s own purpose. 8,000 words is the only surveyed value that still fits beneath the stated single-read ceiling at the empirical ratio (~24,000 tokens). It preserves the original shape of the argument while correcting the arithmetic.

It is also meaningfully binding without being immediately disruptive. On the brief’s own Session 023-open facts, the largest default-read file is ~4,800 words, so 8,000 words would bind at about 60% utilization rather than 32% under the current 15,000-word ceiling. That is what a real budget should look like: enough headroom for normal growth, not enough headroom to make restructuring optional forever. This matches the prior Outsider’s preserved warning that 15K risked becoming ceremonial rather than constraining [archive: provenance/022-workspace-scaling-trajectory/archive/022-outsider/#chunk-04, Q6]; `provenance/022-workspace-scaling-trajectory/01-deliberation.md §5.3`.

If the methodology wants to allow routine paginated reads inside the default-read surface, it can say that. But then the contract has changed in kind and should no longer be defended by appeal to single-read feasibility. I would not preserve that ambiguity.

## Q2. Soft warning value

**6,000 words, fixed.**

At the same ~3.0 tokens-per-word calibration, 6,000 words is roughly 18,000 tokens. That leaves real room below an 8,000-word hard ceiling while still giving early signal before a file becomes difficult to keep within one read. It keeps the warning meaningful as “approaching the ceiling,” not “already beyond the single-read anchor.”

I would not remove the warning. With an 8,000-word hard ceiling, a session needs advance signal to restructure before a file hard-fails at close. I also would not use 5,000 words. On the brief’s numbers, the current largest files are already in the high-4,000s. A 5K warning would be so close to normal large-file size that it risks becoming background noise rather than a useful early signal.

I also prefer a fixed value over a percentage formula in the live spec. The validator and `validation-approach.md` currently express these as explicit constants and thresholds, not derived formulas. A formula is elegant, but it adds interpretation overhead for little gain here. The reasoning can still be “approximately 75% of hard,” while the rule remains simply `6000`.

## Q3. Aggregate default-read surface budget

**Do not adopt an aggregate hard budget this session. Add it as a watchpoint, and preferably as a non-gating report.**

Using the working-set distinction named in brief §5 as a hypothesis rather than imported authority: per-file burden and aggregate working-set burden are different problems. The prior Outsider was right that per-file control alone does not stop aggregate drift by accretion [archive: provenance/022-workspace-scaling-trajectory/archive/022-outsider/#chunk-04, Q6]. I do think the aggregate surface should be measured every session and watched explicitly.

I do **not** think it should become a hard budget this session, because the remediation path is still underdesigned. Under `read-contract.md §1`, every closed session’s `03-close.md` remains default-read. That means total default-read words grow almost monotonically. Under the immutability rules carried through the current architecture, retroactive relief is limited. So a hard aggregate ceiling now would create a binding rule without a clear, already-legible repair path except a larger redesign of what counts as default-read.

My recommendation is:

- Record total default-read words at session open and close if convenient.
- Treat `>90,000 words` as an advisory watchpoint.
- Treat `>100,000 words` as the activation trigger where aggregate-budget design, or default-read-enumeration redesign, becomes the preferred revision direction.

That is consistent with the preserved Session 022 wording that used “e.g., 100K words total” as the operative scale for the aggregate concern (`provenance/022-workspace-scaling-trajectory/01-deliberation.md §5.3`; §7 WX-22-5). I would also trigger review if the aggregate grows by more than roughly 10% in a single session without a corresponding restructuring event. That catches sudden accretion, not just slow drift.

## Q4. Engine-version classification

**If Q1 changes the ceiling from 15,000, this is `engine-v4`. I do not see an honest narrow interpretation that avoids the bump under the current specs.**

`read-contract.md §10` explicitly says that changes to §2 budget values are substantive. `validation-approach.md`’s checks-20-22 gating section explicitly says revising the budget constants in `tools/validate.sh` is substantive and requires an engine-version bump. `engine-manifest.md §5` then says any substantive revision to an engine-definition file increments the engine version. This is mechanically overdetermined, not ambiguous.

On OI-002 merits, that classification is also correct. Budget values are not “minor elaborations within existing scope.” They change normative thresholds, failure/warning behavior, and session-close obligations. OI-002 consistently treats new rules, thresholds, triggers, severity decisions, and required artifacts as substantive (`open-issues/OI-002.md`). A 15K→8K change is exactly that sort of revision.

The only way to avoid `engine-v4` would be to first change the versioning discipline so that this sort of constant-tuning counts as minor. But that would itself be a substantive revision to the engine’s versioning rules. It is not a plausible “interpretation” of the current text. So if the ceiling changes, call the result `engine-v4`.

## Q5. Engine-version cadence (§5.4 minority response)

**Treat the activated warrant as a real informational signal, record it plainly, and proceed with `engine-v4` on the merits. Do not suppress the bump by reclassification.**

The Session 022 Skeptic minority gave a concrete warrant: if `engine-v3` is bumped to `engine-v4` within Sessions 023-025, the cadence concern is activated (`provenance/022-workspace-scaling-trajectory/01-deliberation.md §5.4`). If this session tightens the budget, that warrant fires. The deliberation should say so directly. Minority preservation only means something if triggered minorities are acknowledged when triggered.

But I would not let cadence pressure distort Q1 or Q4. Keeping a miscalibrated budget, or pretending a substantive threshold change is minor, would make the engine-version field less honest, not more. The cadence minority is warning about meaning-loss in the version number. Misclassification in order to avoid a bump would itself be meaning-loss.

I also would not revise `engine-manifest.md §5` in the same session purely to get relief from this case. That would read as goal-seeking rule change under immediate pressure. The cleaner response is:

- Admit the cadence warrant has activated.
- Still adopt `engine-v4` if the budget change is merited.
- Raise the burden for any near-term further engine bump.
- If `engine-v5` is proposed before Session 026, or if an external application shows real portability confusion between adjacent engine versions, then run a dedicated versioning-discipline deliberation.

That preserves both truths at once: the budget should be corrected, and the cadence pattern is now a live governance concern.

## Q6. Watchpoints and minorities

I would preserve these as first-class minorities:

- **10,000-word hard ceiling minority.** This is the strongest live counterposition on Q1. It accepts the calibration problem but permits routine paginated reading inside default-read. Activation trigger: if an 8,000-word ceiling forces two consecutive sessions into coherence-damaging splits, or produces repeated soft warnings/failures on files that remain operationally readable and well-structured, revisit upward.
- **Aggregate-budget-now minority.** If this session does not adopt an aggregate budget, preserve the contrary position that aggregate default-read burden should become normative, not merely observed. Activation trigger: aggregate default-read total exceeds 100,000 words; or exceeds 90,000 for two consecutive sessions; or grows by >10% in one session without compensating restructure.
- **Session 022 cadence minority (`§5.4`).** This should remain first-class and should now be marked activated if `engine-v4` is adopted. Escalation trigger after activation: `engine-v5` proposed before Session 026, or external-application portability confusion appears.

I would monitor these watchpoints in Session 024+:

- **Per-file drift under the new budget.** If any file sits above the soft warning for two consecutive sessions without restructure, the warning is not doing its job.
- **Near-ceiling clustering.** If several default-read files accumulate in the 7,000-8,000-word band at once, the problem may be document-shape drift rather than isolated file growth.
- **Aggregate growth.** Report the session-open and session-close totals. `>90K` is advisory; `>100K` should trigger design work.
- **Calibration discipline.** If future rationales convert tokens to words, they should use workspace-empirical calibration, not generic ratios. Session 022’s honest note is enough evidence that this matters.
- **Versioning pressure.** If another engine bump is proposed quickly, require an explicit statement of why a minor-edit path is unavailable under the live rules.

I would **not** preserve a “budget-value changes are minor” minority as first-class. Under the present texts it is too weakly grounded; it is closer to a proposal to rewrite the rules than a plausible reading of them.

## Honest Limits

I did not read any current-session other-perspective output or any other §7 stance. The only current-session files I read were `provenance/023-session-assessment/00-assessment.md` and `provenance/023-session-assessment/01-brief-shared.md` for a mechanical word-count spot-check.

I read these workspace files directly: `specifications/read-contract.md`, `specifications/engine-manifest.md`, `specifications/validation-approach.md`, `open-issues/OI-002.md`, `provenance/022-workspace-scaling-trajectory/01-deliberation.md` (relevant §5.3-§5.4 sections), `provenance/022-workspace-scaling-trajectory/03-close.md`, `provenance/022-workspace-scaling-trajectory/archive/022-outsider/manifest.yaml`, and an excerpt from `[archive: provenance/022-workspace-scaling-trajectory/archive/022-outsider/#chunk-04]`. I also ran a mechanical word-count scan across active default-read files sufficient to estimate aggregate size; I did not rely on that scan for the main argument because some spot-check counts diverged from the brief’s stated file-size facts.

My largest unresolved uncertainty is that divergence: my spot-check suggested at least some active specs are longer than the brief reports (for example `specifications/multi-agent-deliberation.md` and `specifications/reference-validation.md` appeared above 5,000 words), while the brief says no default-read file exceeds 5,000 words. I did not resolve that discrepancy, so for Q1-Q3 I treated the brief’s numbers as the official deliberation baseline.

I did not inspect `tools/validate.sh` in full, only the constants/check references surfaced through search. My Q3 position also rests on an assumption rather than direct proof: that aggregate-burden remediation is currently awkward because the default-read enumeration and closed-session immutability make retroactive reduction structurally hard.

## Meta-note

My strongest likely cross-model divergence is this: I think the empirical falsification of the 15K rationale is by itself enough to justify tightening to 8K now, even though the Session 022 activation warrant did not literally fire. I expect some Claude positions may give more weight to warrant literalism, compromise at 10K, or cadence caution. I do not think those are stronger than correcting a budget whose own stated calibration has already failed.
