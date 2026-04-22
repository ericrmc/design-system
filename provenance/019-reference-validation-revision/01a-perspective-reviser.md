---
session: 019
title: Perspective — Reviser
date: 2026-04-22
perspective: reviser
participant_kind: claude-subagent
model_family: claude
model_id: claude-opus-4-7
provider: anthropic
status: verbatim
---

## Q1. Is a spec revision warranted now, or should it wait?

**Position: Revision warranted now, with tight scope.** Session 018 produced a sharp, non-ambiguous empirical signal: given the full 278-word constraint statement stripped of title/author/distinctive phrases, a Claude Opus 4.7 subagent reproduced the Kerth Prime Directive *verbatim* (~94% 5-gram overlap, the reference's exact section heading emitted spontaneously). This is not a noisy measurement awaiting replication; it is a single-instance falsification of an implicit premise that was load-bearing in several textual surfaces of v1.

The one-datapoint base supports the following specific revisions:

1. **WX-18-2 (canary-insufficiency) revision.** The finding is mechanical, not statistical: thin prompts derived from tranche-0 are by construction a proper subset of the information in the full constraint statement. If the full statement triggers emission but the thin prompt does not, the canary is structurally under-powered for any reference whose triggering content is distributed across the requirements themselves. This does not need a second data point to establish; it is entailed by what the canary does.

2. **WX-18-4 (cross-family divergence as discriminating signal) revision.** The finding is that the *same input* produced verbatim reproduction in one family and from-scratch composition in another. This asymmetry is a qualitatively different signal from 5-gram overlap alone — it distinguishes "constraints uniquely determine this text" (which should produce cross-family convergence) from "one family has memorised this text" (which produces cross-family divergence with only one family reproducing). §4 L3 already names the signal; §1 C3 does not reference it. The spec's quantitative test and qualitative test are textually misaligned. One data point suffices to surface the misalignment.

The one-datapoint base does **not** support full revision of:

- **WX-18-5 (Cell 2 Produce default) at `multi-agent-deliberation.md` v3 surface.** D2 is a single agile-retrospective case; generalising from it to "Claude-Produce is saturation-prone across reference-validation domains" over-reads. The watchpoint should sharpen into spec text inside `reference-validation.md` (as a known asymmetry to probe for) without yet editing `multi-agent-deliberation.md`'s Cell 2 default.

- **Kernel §7 scope-statement change (Q5).** See Q5.

**Deferral threshold.** If I argued deferral instead, the threshold would be: "require n≥2 reference-validation attempts, preferably in non-agile domains, before touching C3/L1 text." I reject that threshold because WX-18-2 and WX-18-4 are both analytic findings (entailed by the mechanism's structure) as much as empirical ones. Waiting for a second rejection to confirm that thin prompts are a proper subset of the full requirements would be symptomatic of the very anti-laundering failure mode Session 014 Skeptic named: postponing a visible structural defect by demanding more rejections.

## Q2. Which findings should yield spec revisions?

| Finding | Revise? | Surface |
|---|---|---|
| WX-18-2 | Yes | §1 C3 quantitative test + §4 L1 canary design |
| WX-18-3 | Partial | §1 Flagged tension text (strengthen, not resolve) |
| WX-18-4 | Yes | §1 C3 quantitative test (add cross-family clause) |
| WX-18-5 | Watchpoint + §4 L1 note | Not `multi-agent-deliberation.md` v3 yet |

**WX-18-3** is primarily empirical vindication of existing flagged text. The flagged tension in §1 already says "the tension is not resolved." Session 018 has shown the tension is not only unresolved but operationally load-bearing. I propose strengthening the flagged-tension text (acknowledging the Session 018 manifestation) without pretending the underlying tension can be resolved textually. This is the opposite of widening — it makes the known-limit more visible, not less.

**WX-18-5** is where I differ most from a Minimalist-style position. I think this finding is important enough to surface in `reference-validation.md` (as an asymmetry-probing clause at L1) but not yet ready to revise `multi-agent-deliberation.md`'s Cell 2 Produce default. A single agile-retrospective reference is not a population; the right move is to add a concrete probe clause to L1 that will produce multiple data points across future attempts, and defer `multi-agent-deliberation.md` changes until those data points exist.

## Q3. Specific text drafts

### Revision R1 — §1 C3 (WX-18-2 + WX-18-4)

**Current text:**

> **C3 — Low saturation in common training distributions.** The reference must not be a canonical worked example appearing verbatim or near-verbatim across internet corpora. Operational test: both a non-Claude model (via `codex exec`) and an independent Claude instance are each given only the constraint statement and asked to produce a solution. If either produces text that exceeds 30% shared 5-gram token overlap with the reference, the case is rejected as contaminated. Additionally, the Outsider contamination canary (per §4.L1) runs thin prompts derived from tranche-0 against at least two model families; if they spontaneously emit the reference's idiosyncratic structure, labels, or sequence, the case is discarded.

**Proposed text:**

> **C3 — Low saturation in common training distributions.** The reference must not be a canonical worked example appearing verbatim or near-verbatim across internet corpora. Operational test runs in two stages against **both** a non-Claude model (via `codex exec`) and an independent Claude instance:
>
> **(a) Thin-prompt contamination canary (per §4 L1).** Thin prompts derived from tranche-0 are fired at each model family. Spontaneous emission of the reference's idiosyncratic structure, labels, or sequence discards the case.
>
> **(b) Full-constraint saturation test.** Each model is given the complete constraint statement as it would be issued to Cell 2 and asked to produce a solution. **Rejection conditions (any one fires):**
>   1. Either model produces text exceeding 30% shared 5-gram token overlap with the sealed reference;
>   2. Either model spontaneously emits a verbatim distinctive phrase, section heading, or named label from the reference (zero-tolerance regardless of overall overlap percentage);
>   3. **Cross-family asymmetry: one model family reproduces the reference verbatim or near-verbatim while another produces from-scratch composition from the same constraints.** Cross-family divergence of this shape is positive contamination evidence for the reproducing family — it indicates the constraints do not uniquely determine the text, only retrieval does. The case is rejected even if the diverging family's output would pass on its own.
>
> Stage (a) is necessary but not sufficient: thin prompts describe problem-shape without the full requirements; they under-detect saturation when the triggering content is distributed across the requirements themselves (**WX-18-2, Session 018**). Stage (b) is the gating test.

**Rationale against anti-laundering:** This revision *strengthens* C3: it adds two new rejection conditions (verbatim-phrase zero-tolerance, cross-family asymmetry) without lowering the existing 30% threshold. It also reorders stages so the thin-prompt canary is explicitly named as under-powered. A future case that would have "passed" canary but failed full-constraint (as D2 did) will now trigger rejection at the pre-committed stage (b) rather than surviving into Cell 2. This is extension of the rejection surface, not softening.

### Revision R2 — §4 L1 (WX-18-2 + WX-18-5 probe)

**Current text:**

> **L1 — Reference selection saturation gate.** Per §1 C3. Pre-adoption test: Outsider + independent Claude each given constraints-only, asked to produce solution. Reject on >30% 5-gram overlap. Outsider-originated **contamination canary**: thin prompts derived from tranche-0 fired at multiple model families; reject on spontaneous emission of reference's idiosyncratic structure/labels/sequence.

**Proposed text:**

> **L1 — Reference selection saturation gate.** Per §1 C3. Two stages:
>
> **L1a — Thin-prompt contamination canary (Outsider-originated).** Thin prompts derived from tranche-0 fired at multiple model families; reject on spontaneous emission of reference's idiosyncratic structure, labels, or sequence. **Known limitation:** canary under-detects when the reference's triggering content is distributed across requirements rather than concentrated in problem-shape (WX-18-2). L1a survival is necessary but not sufficient.
>
> **L1b — Full-constraint saturation test.** Outsider + independent Claude each given the complete constraint statement (as it will be issued to Cell 2), asked to produce solution. Reject per §1 C3 rejection conditions (1)–(3), including cross-family asymmetry. **Asymmetry probe:** when L1b fires condition (3), record which family reproduced the reference and which did not; accumulated asymmetry records across exercises inform future revisions to the default Produce constitution (see §10 preserved minority on Cell 2 defaults).
>
> Cases passing both L1a and L1b proceed to sealing per §4 L2.

**Rationale:** R2 aligns L1 with the revised C3, makes the two-stage structure explicit at the operational-locus level, and adds the asymmetry-probe clause that will accumulate WX-18-5-type evidence without prematurely editing `multi-agent-deliberation.md`. The asymmetry probe is a data-collection mechanism with no pass-criterion softening.

### Revision R3 — §1 Flagged tension (WX-18-3)

**Current text:**

> **Flagged tension (preserved per Session 014 Skeptic Q1).** Criteria (5) legibility and (8) pre-LLM-co-design are in structural tension with (3) low-saturation. A domain legible to Claude subagents and whose reference pre-dates 2022 is almost by construction heavily represented in Claude's pretraining. The selection criteria attempt to probe around this tension via the saturation test and contamination canary; the tension is not resolved. If the tension empties the candidate pool at sustainable rate (Session 015+ pattern), the mechanism-failure trigger in §8(c) fires.

**Proposed text:**

> **Flagged tension (preserved per Session 014 Skeptic Q1; empirically materialised Session 018 WX-18-3).** Criteria (5) legibility and (8) pre-LLM-co-design are in structural tension with (3) low-saturation. A domain legible to Claude subagents and whose reference pre-dates 2022 is almost by construction heavily represented in Claude's pretraining.
>
> **Session 018 Cell 1 first-exercise confirmation.** The Kerth Prime Directive retrospective opening protocol — a canonical D2 candidate satisfying C5 and C8 — failed C3 at stage (b) with ~94% 5-gram overlap and verbatim section-heading emission by a Claude Opus 4.7 subagent (provenance: `provenance/018-reference-validation-exercise-1/`). This is an empirical instance of the flagged tension, not an unexpected finding; it confirms the tension is operationally load-bearing and cannot be treated as theoretical.
>
> The selection criteria probe around this tension via the two-stage saturation test (§1 C3, §4 L1); **the tension is not resolved by this spec and cannot be resolved by threshold-tuning.** If the tension empties the candidate pool at sustainable rate (Session 015+ pattern), or if a second full-constraint-stage rejection matches the Session 018 shape in a non-agile domain, the mechanism-failure trigger in §7 fires (see also §9 re-opening trigger 5).

**Rationale:** R3 makes the structural-limit hypothesis explicit in the spec, cites Session 018 by provenance pointer, and names that threshold-tuning cannot resolve the tension. This is anti-widening: future sessions cannot claim this tension has been addressed by mere parameter adjustment. It also pre-commits a second trigger condition (a second rejection of the same shape in a non-agile domain) without softening anything.

### Revision R4 — §7 Mechanism-failure (light; precision only)

**Current text (relevant excerpt):**

> **Failure of any two of these three core properties in a single exercise is mechanism falsification.** A single hard leak of the reference into Cell 2 is mechanism-falsifying for that exercise.

**Proposed text (addition only, existing text retained verbatim):**

> [Existing paragraph retained unchanged.]
>
> **Pre-seal reference reproduction by a Cell 2 Produce-default model family under full-constraint test (per §1 C3 stage (b)) is not mechanism failure for the exercise** (the protocol rejected the case correctly), **but is evidence bearing on §9 re-opening trigger 5 (three-consecutive-gap-surfaced-non-passes) and on the Cell 2 Produce constitution question.** Accumulated instances are tracked at §4 L1b's asymmetry probe.

**Rationale:** This addition clarifies what Session 018 *was* (a correct rejection, not a mechanism failure) and what it *counts toward* (the anti-laundering trigger and the Cell 2 composition question). It does not soften §7; it adds a disambiguation that protects against future sessions miscounting a pre-seal rejection as either a pass or a full mechanism failure.

### Non-revision: §8 Label discipline, §9 Re-opening triggers (primary text), §10 preserved minorities

I propose **no changes** to §8 label discipline text. The `validation: reference-validated` label scope is unchanged; Session 018 produced no artefact requiring labelling.

I propose **one specific addition** to §9, discussed in Q4.

I propose **no removal or weakening** of §10 preserved minorities. Q7 addresses whether a new minority should be added.

### Non-revision: `multi-agent-deliberation.md` v3

I propose **no changes to `multi-agent-deliberation.md` v3 in Session 019.** WX-18-5's generalisation is not supported by one data point. The asymmetry probe at §4 L1b (R2) is the correct scope for now; `multi-agent-deliberation.md` revision is a Session 021+ question contingent on accumulated asymmetry evidence.

## Q4. OI-016 re-opening, label discipline, §9 triggers

My proposed revisions do not soften kernel §7's anti-substitution clause and do not soften §8 label discipline. R1–R4 extend rejection surfaces; they do not lower pass thresholds or widen what counts as a pass.

**Proposed addition to §9 re-opening triggers (minor):**

**Current §9 excerpt:**

> OI-016 re-opens if: (1) three-core-properties test failure; (2) counterfactual-probe inversion (§4 L5); (3) "too fast" pattern ≥80% structural alignment despite passing contamination tests; (4) noise-floor inversion within 15 pp of baseline; (5) three-consecutive-gap-surfaced-non-passes; (6) label discipline collapse — `validation: reference-validated` used without qualification; kernel §7's anti-substitution clause softened without concurrent strengthening.

**Proposed addition (new trigger 7):**

> (7) **Two pre-seal C3 stage (b) rejections in structurally-different domains (e.g., not both agile-retrospective) with verbatim or near-verbatim reproduction by the Cell 2 Produce-default family.** Two such rejections activate the Session 014 Skeptic "provisional substitute" minority warrant (per §10) as a required kernel §7 revision consideration, and re-open OI-016.

**Rationale:** This trigger pre-commits that if the Session 018 pattern recurs in a different domain, the Session 014 Skeptic minority warrant is activated without further deliberation required to demonstrate the pattern. It tightens OI-016's re-opening surface. No current state-transition for OI-016 is required; it remains **Resolved — provisionally addressed pending first-exercise**, now with enriched §9 and an extended §1 C3. Session 018's single rejection is counted toward §9 trigger 5 (three-consecutive-gap-surfaced-non-passes); the newly proposed trigger 7 requires two rejections in structurally-different domains.

No concurrent strengthening is needed because nothing is softened.

## Q5. Kernel §7 "provisional substitute"

**Position: Do NOT revise kernel §7 v4 text in Session 019.** Session 014 Skeptic's preserved minority in `reference-validation.md` §10 has a specific operational warrant:

> **Operational warrant:** if label discipline collapse (§9 trigger 6) is observed, the Skeptic's stricter "provisional substitute" framing is the preferred revision direction for kernel §7.

WX-18-3 is empirical vindication of the §1-flagged tension, not label-discipline collapse. No artefact has yet been produced and labelled `validation: reference-validated`; no artefact has yet been cited simply as "validated" without the narrower scoping. The specifically-required trigger has not fired.

However, I recognise the Skeptic perspective will push that WX-18-3 has activated the *spirit* of the warrant (empirical vindication of the narrow-claim position). My counter-position is that activating a warrant preemptively would itself be a form of anti-laundering risk: the warrant was written with a specific trigger so that kernel-text changes would be tightly coupled to observed pass/fail patterns rather than to any single session's interpretation of what a finding "really means."

**What I propose instead:** my R4 addition to §7 mechanism-failure and my proposed §9 trigger 7 together strengthen the coupling between future C3 rejections and kernel-level reconsideration, *without* prejudging that kernel §7 v4 is currently miscalibrated. If two structurally-different-domain rejections accumulate, trigger 7 fires and kernel §7 revision becomes a *required* consideration. If the Session 018 pattern does not recur, kernel §7 v4 remains defensible.

If the Skeptic in this deliberation argues for kernel §7 revision now, that is a first-class minority I support preserving (see Q7); I would not dissent at full strength against adopting their framing, but my own drafting stance is that one data point is not yet enough to revise the kernel's named third sense.

## Q6. Change scope per OI-002

- **R1 (§1 C3 two-stage restructure + new rejection conditions 2, 3):** **Substantive (v-bump).** Adds new normative rejection conditions (verbatim-phrase zero-tolerance, cross-family asymmetry). These are new pass/fail rules, not clarifications of existing text. → `reference-validation.md` v2.

- **R2 (§4 L1 two-stage restructure + asymmetry probe):** **Substantive.** Adds an asymmetry probe clause with record-keeping obligations not present in v1. Bundled into the v2 bump.

- **R3 (§1 Flagged tension strengthening):** **Minor.** Makes explicit what existing flagged text already contained (the tension is real and not resolved) and cites the Session 018 empirical instance. No new normative rules. Would qualify as minor on its own but travels with the substantive changes in the same v-bump.

- **R4 (§7 addition re pre-seal rejection):** **Minor.** Disambiguates existing text without adding new rejection conditions. Travels with the v-bump.

- **§9 trigger 7 addition:** **Substantive.** New automatic re-opening trigger with specific conditions. Travels with the v-bump.

**Aggregate:** `reference-validation.md` v1 → v2. `methodology-kernel.md` v4 unchanged. `multi-agent-deliberation.md` v3 unchanged in Session 019.

## Q7. Preserved first-class minorities

If my revisions are adopted, the revised `reference-validation.md` v2 should carry the following minorities:

**(a) Session 014 Skeptic "provisional substitute" minority (preserve, strengthen annotation).** §10 text retained verbatim; add annotation:

> **Session 019 update.** The §1-flagged tension materialised empirically in Session 018 (WX-18-3). Session 019 deliberation did not adopt the Skeptic's preemptive kernel §7 revision on n=1 evidence, but strengthened §9 trigger 7 to make the Skeptic's warrant automatically activate on n=2 structurally-different-domain rejection. The minority's framing is the pre-committed revision direction under that condition.

**(b) Session 014 Architect pure-within-session minority (preserve unchanged).** No Session 019 evidence bears on it.

**(c) Session 014 Skeptic+Outsider joint narrower-claim minority (preserve unchanged).** No Session 019 evidence bears on it; its text is compatible with the R1/R2 strengthening.

**(d) Session 019 Skeptic minority (add if dissent emerges in this deliberation).** If the Session 019 Skeptic argues for kernel §7 revision now and the synthesis does not adopt it, that dissent should be preserved at first-class strength as a new §10 entry citing this session's provenance.

**(e) Session 019 Minimalist minority (add if deferral advocated and not adopted).** If the Session 019 Minimalist argues for full deferral of R1/R2 to n=2 evidence and my "revise now" position is adopted over it, the Minimalist's deferral rationale should be preserved as a §10 entry so that if R1/R2 later prove premature, the minority is available for rollback argument.

**(f) Session 019 Outsider minority (add if cross-family framing differs).** If the Outsider proposes a frame-level alternative (e.g., non-Claude Produce default in `multi-agent-deliberation.md`) not adopted, it should be preserved, especially given it is the cross-family check D-023 clause 1 explicitly requires.

## Q8. Anti-laundering check

The specific failure mode to check against is Session 014 Skeptic Q7's: "the Session N+1 kernel or spec-file edits that *widen* what counts as reference-validation pass (e.g., dropping the contamination check because 'it kept firing,' or raising the allowed iteration count because 'the methodology needs more room')."

Examining R1–R4 and the §9 trigger 7 addition against this rule:

- **R1 adds two new rejection conditions** (verbatim-phrase zero-tolerance; cross-family asymmetry). It does not lower the 30% threshold; the threshold is retained verbatim as rejection condition (1). This is extension of the rejection surface.

- **R2 adds the asymmetry probe** (data collection, no pass-criterion change) and acknowledges L1a's known limitation explicitly. It does not soften L1 gating.

- **R3 strengthens the flagged-tension text** by citing Session 018 and explicitly stating the tension cannot be resolved by threshold-tuning. A future session cannot now argue "the tension has been addressed" merely by parameter adjustment.

- **R4's addition to §7** disambiguates pre-seal rejection from mechanism failure but explicitly couples pre-seal rejections to §9 trigger 5 (three-consecutive-gap-surfaced-non-passes) and asymmetry probe accumulation. This prevents "rejection without consequence" framing.

- **§9 trigger 7** tightens the re-opening surface: a new automatic OI-016 re-opener is added.

**Specific passages to point to for Skeptic scrutiny:**

- R1 rejection condition (2) — "zero-tolerance regardless of overall overlap percentage" — closes a loophole where a case with <30% overall overlap but a verbatim distinctive phrase could have squeaked through v1's 30% rule. Session 018 Cell 1 Step 3 revealed the spontaneous emission of "The Prime Directive" as a section heading; that specific behaviour would now be a rejection condition on its own.

- R1 rejection condition (3) — cross-family asymmetry — inverts the naive reading of v1's "*if either* produces text that exceeds 30%." v1's text could be read as "either-or"; the GPT-5.4 non-reproduction could have been read as "Outsider passed, so the case has exoneration evidence." R1 (3) explicitly names cross-family divergence with one family reproducing as *positive contamination evidence*, not exoneration.

- §9 trigger 7 — pre-commits that a second structurally-different-domain rejection *automatically* activates the Skeptic's kernel §7 revision warrant. Future sessions cannot negotiate this trigger away on a case-by-case basis without changing §9 itself (which would require anti-laundering scrutiny on its own terms).

**Where the revisions do NOT strengthen, and whether this is accommodation:**

- I do not revise kernel §7 v4 now. This is *not* accommodation because the Skeptic's own preserved warrant specifies label-discipline collapse as the trigger, which has not occurred. The right-sized response to n=1 is to tighten the coupling (§9 trigger 7) so that n=2 automatically activates the warrant.

- I do not revise `multi-agent-deliberation.md` v3 Cell 2 default. This could be read as accommodation if one thought WX-18-5 was a confirmed generalisation. I think it is a single-domain finding that justifies data-collection (asymmetry probe) but not default-changing. A Minimalist pushing further in this direction has a fair argument; I would accept an even-lighter version of R2 that retained the asymmetry probe without any L1 text change if that were the synthesis compromise.

**Conclusion on Q8:** R1–R4 and §9 trigger 7 together extend the rejection surface and the re-opening surface of `reference-validation.md` without lowering any pass threshold, softening any mechanism-failure criterion, or widening any label-discipline rule. The one non-revision (kernel §7) is coupled to a strengthened §9 trigger so that the minority warrant activates automatically on a pre-committed observable. On my reading this passes the procedural-self-deception test. Session 019 Skeptic should check my specific drafts; I welcome dissent if any passage fails the check.
