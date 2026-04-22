---
session: 023
title: Calibrator Perspective — Raw Output
date: 2026-04-23
status: complete
perspective: calibrator
committed_at: 2026-04-23
---

## Q1. Hard ceiling value

I recommend **8,000 words** as the hard ceiling.

The calibration argument is direct. The §2 Rationale states its design intent: "leaves headroom below the single-read ceiling." The Rationale then executes that intent via an arithmetic step that turns out to be wrong by a factor of ~2.3×. The measured tokens-per-word ratio for workspace prose-with-markdown is ~3.0× (Session 022 Honest Notes, empirically derived from SESSION-LOG and open-issues word/token counts). The Rationale used 1.3×. At 1.3× the ceiling does leave headroom (15K words → 19.5K tokens, under the 25K single-Read limit). At 3.0× the ceiling overshoots (15K words → 45K tokens, 1.8× the single-Read limit). The ceiling as currently set does not accomplish what the Rationale said it accomplishes.

I want to be precise about what this means. The 15K value is not inherently wrong — a methodology could choose to set its per-file ceiling above single-Read and accept that files at the ceiling will require paginated reads. That would be a defensible design if it were the articulated choice. But that is not what §2 articulated. §2 articulated "headroom below the single-read ceiling," and the value it set does not deliver that property. This is a calibration error, not a policy disagreement. The honest correction is to bring the value into agreement with the articulated intent.

At 3.0× tokens-per-word, the ceiling that satisfies the Rationale's "headroom below single-Read" intent is approximately 8,000 words (24,000 tokens, narrowly within the 25K limit). This is the Outsider §5.3 value. It is not coincidence that the Outsider converged on this number — the Outsider was reasoning from the same concern (that the 15K value was set on arithmetic that would not survive empirical verification) and arrived at the calibrated answer.

Against 10K compromise: 10K words at 3.0× is 30K tokens, above single-Read. 10K does not satisfy the Rationale intent. It is a political midpoint rather than a calibrated value.

Against 12K modest tightening: Same objection, worse. 12K words at 3.0× is 36K tokens, well above single-Read. This would be tightening-for-appearance without tightening-to-purpose.

Against 15K retained + Rationale corrected: This is the option where we keep the value and rewrite the Rationale to say something like "ceiling set above single-Read limit; pagination expected at files near ceiling." This is internally consistent but represents a different methodology than the one Session 022 thought it was adopting. Session 022 thought it was adopting a ceiling with headroom under single-Read. Retaining 15K and rewriting the Rationale is adopting a different spec post-hoc. The honest move is to fix the value to match the original intent, not to fix the intent to match the accidental value.

Against Other: I considered 7,500 words (slightly under 8K, adds marginal safety against the ~3.0× ratio being off by a few percent) and 8,500 words (slightly over, gives marginal room for the largest current file at 4,800 to grow). I do not think the difference matters at this precision. The brief's §7 Calibrator stance names 8K as substantively preferred with 7.5K/8.5K refinements negotiable. I agree. 8,000 is a round number that sits within single-Read at 3.0× with ~1,000-token margin; that margin is adequate.

One caveat worth flagging: the 3.0× ratio is derived from two files (SESSION-LOG, open-issues). The ratio for other workspace files may differ. If we later measure a higher ratio for, say, specification files (which have denser markdown structure and may tokenise differently), then 8,000 words could itself exceed single-Read. I name this in Honest Limits. The response to that possibility is not to reject the calibration but to re-measure and re-calibrate if the empirical picture changes.

## Q2. Soft warning value

I recommend **6,000 words** as the soft warning.

The design function of a soft warning is to provide signal before the ceiling is breached — enough notice that the next session can restructure without emergency pressure. The ratio of soft-to-hard in the current spec is 10K:15K, which is 0.67. Preserving that ratio with an 8K ceiling gives 5,333 words, which rounds naturally to 5,000 or 6,000.

Against 6,000 (75% of 8K): Gives more headroom between soft and hard. Less likely to false-alarm; more likely to provide warning that is genuinely actionable (the session gets notice while still having room to maneuver). The largest current file at 4,800 words is 80% of 6,000 — close to trigger but not triggering. This means files approaching the new ceiling will fire the warning with meaningful advance notice.

Against 5,000 (63% of 8K): The largest current file at 4,800 words is 96% of 5,000 — essentially at the warning line. This would mean the warning fires immediately or near-immediately on adoption, which dilutes the warning's signal value. If everything is almost warning, nothing is warning. The watchpoint function of the soft warning is undermined.

Against removing the soft warning entirely: The soft warning was a Session 022 design element specifically to create a two-stage signal. Removing it because the hard ceiling is tighter treats the two-stage design as a luxury that only matters at large budgets. I disagree — the two-stage design matters more at tighter budgets because the distance from "fine" to "failure" is shorter. Retain soft warning; calibrate it sensibly.

Against percentage formula: I considered "soft = 0.67 × hard" or "soft = 0.75 × hard" as formula. The advantage is that the relationship between soft and hard survives future revisions automatically. The disadvantage is that formulas in validator constants are awkward (tools/validate.sh uses explicit integer constants). I think the right pattern is to state the ratio in the spec text as the design principle and set specific integer constants in the validator. 6,000 with 75% articulated ratio satisfies both.

Recommendation: 6,000 words soft warning, with §2 text explicitly stating "soft warning is set at 75% of hard ceiling" so that future revisions carry the ratio.

## Q3. Aggregate default-read surface budget

I support **adopting an aggregate budget** as a soft-warning-only mechanism. I decline to support an aggregate hard ceiling in this session.

The Outsider §5.3(b) concern is real: per-file control alone is insufficient if the default-read set grows by accretion. Thirty-three files at 4,000 words average each is 132,000 words aggregate — well beyond any single-Read, and growing. The per-file ceiling does nothing to limit this growth. The Outsider is right that per-file-only is a porous discipline.

However, I want to be careful about what an aggregate budget commits us to. At current 33 files, ~81,500 words, we are not in crisis. The aggregate has not yet demonstrated the failure mode the Outsider warns against. An aggregate hard ceiling set now would be guessing at the value — we do not have empirical data on what aggregate size breaks what property of the workspace.

What we do have is a reason to measure and watch. I recommend:

1. Add an aggregate **watchpoint** to validate.sh that reports the total word count across all default-read files at every validator run, with no pass/fail threshold but with a **soft warning threshold** at, say, 100,000 words (roughly 20% growth from current ~81.5K). The warning would be informational — "aggregate default-read surface at X words, approaching watch threshold" — not a failure.

2. Preserve the aggregate-hard-ceiling decision for Session 024 or later, with an explicit activation warrant: "if aggregate exceeds 120,000 words OR the soft warning has been active across 3 sessions without restructure, aggregate hard ceiling becomes a live decision."

3. The aggregate watchpoint text in §2 should explicitly name the Outsider §5.3(b) minority as the rationale for its existence.

Against adopting an aggregate hard ceiling now: we do not have data to set the value calibratively. Setting it would be picking a round number and declaring it correct, which is exactly the failure mode Session 022's 15K exhibits. Better to instrument, measure, and calibrate when empirical signal arrives.

Against rejecting entirely: the Outsider minority has a coherent concern; preserving it as a watchpoint with concrete activation triggers is how the methodology honours minority positions while waiting for empirical signal.

Recommendation: aggregate as watchpoint with soft warning at 100K words; aggregate hard ceiling deferred with concrete activation warrant.

## Q4. Engine-version classification

A budget-value change is **substantive**, and this revision is **engine-v4**.

I want to argue this on spec-revision merits as the brief directs, independent of cadence.

`read-contract.md` §10 is explicit: "Substantive: any change to the §1 enumeration, §2 budget values, §4 archive-pack structure, §5 manifest fields, §6 reference convention, or §7 integrity mechanism. Engine-version bump per `engine-manifest.md` §5."

This is a pre-declaration. Session 022 wrote this sentence knowing that budget values might later be revised. It chose to classify such revisions as substantive at the time of writing, not after the fact. The classification is not being freshly argued now — it was committed to by the spec's own terms.

Could we challenge the pre-declaration? Yes. The deliberation is allowed to challenge spec text. But the challenge would need to be: "the §10 pre-declaration is wrong and should be revised." That is itself a substantive revision to §10, which is itself a budget-adjacent metastructure. Revising §10 to say "budget value changes are minor" in the same session where we revise the budget values would be transparent: we would be rewriting the substantiveness test specifically to avoid triggering it.

The narrow-minor interpretation would have to argue that a value correction (fixing an arithmetic error) is different from a value change (adopting a different design). I do not find this interpretation persuasive. From the validator's perspective, DEFAULT_READ_HARD_WORD_CEILING changes from 15000 to 8000. From any user's perspective, the ceiling below which files must stay is now different. The behaviour the spec commits to is different. That is substantive regardless of whether we frame it as correction or change.

There is a more honest version of the minor-classification argument, which I will steelman: "This revision is correcting an arithmetic error in the Rationale, not changing the design intent. The intent — headroom below single-Read — was adopted in Session 022. We are not revising the intent; we are revising the value to match the intent. Therefore it is a typo-class correction." This argument is coherent but I still reject it. §10 does not distinguish "value change to match articulated intent" from "value change to adopt new intent." It classifies all budget value changes as substantive. The spec's commitment is mechanical, not purposive, and that is a feature — it prevents exactly this kind of post-hoc rationalisation from evading the classification.

Engine-v4 is the honest classification.

## Q5. Engine-version cadence

Record the cadence signal; do not let it defer the calibration.

The Session 022 §5.4 Skeptic minority warrant activates: "three engine-v-bumps in four adjacent sessions." That is a real signal. It is worth naming explicitly in Session 023 close and in engine-manifest.md §7.

But I do not support deferring the Q1-Q4 revision because of the cadence. Here is why.

The calibration error is demonstrable, small, and fixed by a specific value change. Deferring the fix to smooth the cadence signal would be trading methodology-fidelity for methodology-appearance. The methodology's honesty is its primary property. If the methodology has committed to a ceiling whose arithmetic is wrong, the right move is to fix it. Waiting a session or two so that the v-bump looks less frequent is optics, not discipline.

The §5.4 warrant was articulated in Session 022 for a reason — to surface a concern about engine-version inflation that could confuse external adopters. That concern is legitimate. The response to a warrant firing is not "take the warrant seriously by deferring the bump." It is "take the warrant seriously by examining whether each bump was substantively warranted." If we examine the three bumps — engine-v2 (OI-004 criterion-4 articulation), engine-v3 (new read-contract spec + three v-bumps of other specs), engine-v4 (read-contract §2 budget recalibration) — each is substantively warranted. The cadence is fast because the methodology is in a phase of intensive self-development; this is expected for a methodology that has been running 23 sessions, not 230.

What I support regarding §5.4:

1. Name the warrant firing in Session 023 close. Preserve the Skeptic minority concern.
2. Propose a change to engine-manifest.md §5 or §7 that adds an annotation discipline: when multiple v-bumps happen in a short window, the engine-manifest §7 history entry should explicitly name what was substantively different in each bump. This preserves the cadence signal for external adopters: they can read the history and see that the bumps were not trivial.
3. Do not revise engine-manifest §5 bump criteria to be stricter. The bump criteria are correctly calibrated. The issue is presentation, not criteria.
4. Set a concrete watchpoint for Session 024+: if three more engine-v-bumps happen in the next four sessions (six bumps in eight sessions), elevate the Skeptic warrant to a live deliberation item. This gives the warrant teeth beyond recording.

The Skeptic's concern is legitimate but does not bind the Calibrator's direction. Record, watch, and act if signal persists.

## Q6. Watchpoints and minorities

Minorities to preserve as first-class:

1. **Outsider §5.3(b) aggregate concern.** Per Q3, preserve as live watchpoint with specific activation: "if aggregate default-read surface exceeds 120,000 words OR soft warning (at 100K) has been active across 3 sessions without restructure, aggregate hard ceiling becomes a live Session N+1 decision." Name this in read-contract.md §2 text and in a section of the Session 023 close.

2. **Skeptic §5.4 engine-version-cadence concern.** Per Q5, preserve with activation: "if three more engine-v-bumps happen in Sessions 024–027 (six total in eight sessions), Skeptic warrant elevates to live deliberation item for that session." Name in engine-manifest.md §7 history entry for engine-v4.

3. **Tokeniser-drift concern** (my own, flagged here for first-class preservation). The 3.0× tokens-per-word ratio was measured on two files in Session 022. The ratio may differ for other file types, and it may drift as tokenisers evolve. Activation: "if any single-Read attempt on a default-read file fails due to token-budget-exceeded, even though the file is under 8K words, re-measure the ratio across a sample of default-read files and re-calibrate." Name this in read-contract.md §2 Rationale text.

4. **Revision-frequency for the revised spec itself.** The read-contract spec is being revised one session after adoption. There is honest-signal risk here: if we revise again in Session 024, that is a second-revision-in-two-sessions pattern for the same spec, which is a different warrant than the engine-version cadence one. Activation: "if read-contract.md §2 budget values are revised a second time within three sessions of the engine-v4 revision, examine whether the spec's design frame (per-file word count as the measurement primitive) is itself miscalibrated." Name this in read-contract.md §10 Versioning section.

5. **Largest-file growth watch.** The 4,800-word largest file is currently at 60% of the 8K ceiling. If it grows to 6,000 (75%, soft warning) in the next two sessions without restructure, that is signal the ceiling is binding closer than intended. Activation: "if the largest default-read file exceeds 6,000 words in Sessions 024 or 025, Session-024/025 deliberation should examine whether the growth is structurally necessary or an accretion failure." Name this in Session 023 close under "Session 024 watchpoints."

On what I would not preserve as first-class:

- The "15K should be retained with Rationale corrected" position. This is a defensible policy choice but it was not actually held by any brief-identified minority; it is a logical option. If it emerges from another perspective in this deliberation, it should be preserved; if not, I would not create it to preserve.

- The "engine-version classification should be challenged" position. My Q4 argument rejects this. If another perspective articulates a coherent challenge, preserve it; otherwise, the pre-declaration stands.

Session 024+ concrete watchpoints summary:
- Aggregate surface: watch at 100K; live-decide at 120K or 3-session soft-active.
- Engine-v cadence: elevate at six bumps in eight sessions.
- Tokeniser drift: re-measure on any single-Read token-exceed despite under-8K words.
- Read-contract revision frequency: examine design frame if re-revised within three sessions.
- Largest-file growth: examine at 6,000 words in Sessions 024–025.

## Honest Limits

**What I did not read.** I reasoned only from this brief per §1 instruction. I did not read:
- The full Session 022 synthesis, Honest Notes, or perspective outputs (only the excerpts in this brief).
- The full read-contract.md spec (only §2 and §10 excerpts).
- engine-manifest.md beyond the §5 and §7 excerpts.
- validation-approach.md or validate.sh beyond the constants named.
- The 33 default-read files themselves, except via the top-5 table.
- Any previous Calibrator or equivalent-role output from prior sessions.

**What I am uncertain about.**

The 3.0× tokens-per-word ratio is derived from a two-file sample in the Session 022 Honest Notes. I treat it as reliable for this reasoning but I have not verified it independently, and I do not know its variance across file types. If the true ratio for, say, spec files is 2.5×, then 8,000 words is 20,000 tokens — comfortably under single-Read. If the true ratio for archive files with heavy code blocks is 3.5×, then 8,000 words is 28,000 tokens — over single-Read. The calibration is only as good as the measured ratio.

The single-Read ceiling of ~25,000 tokens is stated in the brief as "unchanged since Session 022" but I do not have direct verification. If the ceiling has moved (either direction) my calibration math is off.

The aggregate-watchpoint threshold of 100K is a guess. I picked it as roughly 20% above current. I have no empirical basis for that specific value. A defensible alternative is 1.5× current (~122K) or 2× current (~163K). This watchpoint value should be treated as placeholder until we have signal.

The cadence-elevation threshold of "six bumps in eight sessions" is also a guess, scaled from the Session 022 Skeptic's "three in four" warrant. It is arithmetically consistent but I have no empirical basis for that specific scaling.

**Where my position rests on assumptions.**

My Q4 engine-v4 classification rests on the assumption that §10's pre-declaration should be honoured mechanically. This is a honest-reading-of-spec-text argument. If the methodology has an elsewhere-articulated principle that allows post-hoc re-classification (which I have not seen), my Q4 would need revision.

My Q1 calibration argument rests on the assumption that the §2 Rationale's "headroom below single-read ceiling" intent is the design intent that should govern the value. If the true design intent was different (e.g., "ceiling above single-read to force pagination as a discipline"), then 15K is closer to correct and 8K is wrong. I have argued that the Rationale text is the articulated intent, but I could be wrong about what Session 022 actually decided versus what it wrote down.

My Q3 decline-hard-ceiling-now position rests on the assumption that we have time to gather empirical data before the aggregate breaks something. If the aggregate surface is already degrading an unnamed property of the workspace, I am wrong to defer.

My Q5 cadence position rests on the assumption that external adopters of the methodology, if any, will read engine-manifest §7 history and understand substantive-vs-superficial distinctions. If external adopters treat v-bumps as opaque version changes, the cadence concern is stronger than I have credited and deferring the v-bump has more merit than I argued.

Finally: this is my first participation in Session 023 deliberation. I do not know what the other three perspectives will argue. My positions are independent per the §1 instruction; if the synthesis surfaces strong counter-arguments, my §8 format commitment is that the raw output stands as-written even if I would revise on reflection. That is the point of the method.
