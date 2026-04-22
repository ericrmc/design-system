---
session: 019
title: Perspective — Outsider
date: 2026-04-22
perspective: outsider
participant_kind: non-anthropic-model
model_family: gpt
model_id: gpt-5.4
provider: openai
status: verbatim
---

## Q1. Is a spec revision warranted now?

Yes, but narrowly.

Session 018 did not just produce “one bad candidate.” It exposed a concrete blind spot in the current gate design: the thin canary was allowed to stand next to the C3 full-overlap test as if both were probing the same risk, but WX-18-2 shows they are not. The failure mode is already known enough to fix before Session 020. [synth] In testing terms, this is a screening/confirmatory mismatch: the cheap screen omitted the operative stimulus, so the confirmatory probe found a positive case the screen systematically under-saw.

What I would revise now:
- tighten `reference-validation.md` §1 C3 and §4 L1 so the full-constraint probe is the decisive pre-seal gate and the thin canary is explicitly supplementary;
- revise §4 L3 so cross-family divergence is treated as a diagnostic signal, not as positive design evidence when observed at pre-seal.

What I would not revise now:
- kernel §7’s naming of reference-validation as a third sense;
- `multi-agent-deliberation.md` defaults;
- any family-conditional narrowing of C3 that would let a Claude-saturated case pass by shifting Produce elsewhere.

Evidence that would move me toward broader revision:
- two or three additional candidate evaluations showing the same asymmetric pattern across otherwise plausible cases, especially if lower-saturation candidates still fail only in Claude-family probes;
- evidence that the candidate pool is sustainably emptied by the C3/C5/C8 tension after the L1 fix.

Evidence that would move me toward “we should have waited”:
- the next two or three candidate evaluations show strong agreement between thin canary and full-constraint probe, and Session 018 looks idiosyncratic rather than structural.

## Q2. Which findings should yield revisions?

1. **WX-18-2 should yield revision.** Surface: `reference-validation.md` §1 C3 and §4 L1, with a small strengthening in §9. This is the clearest spec defect.

2. **WX-18-3 should remain a watchpoint for now.** Surface unchanged. The spec already contains the flagged tension:
> “The tension is not resolved.”
Session 018 is the first empirical materialisation, not yet enough to rewrite kernel scope or mechanism-failure rules.

3. **WX-18-4 should yield revision, but only in §4 L3.** The revision should be a downgrade in claim strength: cross-family divergence is a useful diagnostic, but from one case it is not yet a reliable positive signal of “design evidence.” [synth] From an `n=1` asymmetric interaction, you can infer “something differs by family here,” not a stable cross-family law.

4. **WX-18-5 should remain a watchpoint for now.** I would not revise `multi-agent-deliberation.md` yet. Making Produce family selection conditional on which family failed C3 would be a substantive widening of what counts as pass unless the claim language were also narrowed. That is too accommodation-prone after one case.

## Q3. Draft specific text for each proposed revision.

**1. `reference-validation.md` v1 §1 C3**

Current text:
> **C3 — Low saturation in common training distributions.** The reference must not be a canonical worked example appearing verbatim or near-verbatim across internet corpora. Operational test: both a non-Claude model (via `codex exec`) and an independent Claude instance are each given only the constraint statement and asked to produce a solution. If either produces text that exceeds 30% shared 5-gram token overlap with the reference, the case is rejected as contaminated. Additionally, the Outsider contamination canary (per §4.L1) runs thin prompts derived from tranche-0 against at least two model families; if they spontaneously emit the reference's idiosyncratic structure, labels, or sequence, the case is discarded.

Proposed replacement:
> **C3 — Low saturation in common training distributions.** The reference must not be recoverable from the case description itself in common model training distributions. Operational test has two mandatory screens, both completed before seal. First, a **full-constraint probe**: one non-Claude model (via `codex exec`) and one independent Claude instance are each given the fullest candidate constraint statement prepared for pre-seal evaluation, with reference author, title, and distinctive phrases removed, and asked to produce a solution. If either output exceeds 30% shared 5-gram token overlap with the reference, explicitly names the reference, or reproduces its distinctive labelled sequence, the case is rejected as contaminated. Second, the Outsider contamination canary (per §4 L1) runs thin prompts derived from tranche-0 against at least two model families; if they spontaneously emit the reference's idiosyncratic structure, labels, or sequence, the case is discarded. **Canary survival is early-warning only and does not satisfy C3 on its own.**

Reason: this directly addresses WX-18-2 without widening pass criteria.

**2. `reference-validation.md` v1 §4 L1**

Current text:
> **L1 — Reference selection saturation gate.** Per §1 C3. Pre-adoption test: Outsider + independent Claude each given constraints-only, asked to produce solution. Reject on >30% 5-gram overlap. Outsider-originated **contamination canary**: thin prompts derived from tranche-0 fired at multiple model families; reject on spontaneous emission of reference's idiosyncratic structure/labels/sequence.

Proposed replacement:
> **L1 — Reference selection saturation gate.** Per §1 C3. Pre-adoption screening runs in two passes. Pass A is the **full-constraint probe** on the exact pre-seal constraint statement prepared to characterise the candidate case. Pass B is the Outsider-originated **contamination canary** using thin prompts derived from tranche-0 across multiple model families. Reject on any C3 failure in either pass. The seal record preserves the prompts, model families, and outputs used to clear C3. **Thin-canary survival may justify continuing evaluation; it may not justify sealing by itself.**

Reason: this makes the gate operationally legible and audit-friendly.

**3. `reference-validation.md` v1 §4 L3**

Current text:
> **L3 — Cross-model divergence analysis.** Cell 3 validators span Claude-family and non-Claude-family. Cross-family convergence on reference text is contamination evidence. Cross-family divergence with both satisfying constraints is design evidence.

Proposed replacement:
> **L3 — Cross-model divergence analysis.** Cell 3 validators span Claude-family and non-Claude-family. Cross-family convergence on reference text is contamination evidence. **Cross-family divergence is interpretable only after the candidate has already passed L1.** Divergence observed during pre-seal probing is a contamination diagnostic, not design evidence: it shows uneven saturation across model families, not that the methodology derived the structure. **A candidate that fails C3 is not rescued by cleaner output from another family.**

Reason: this addresses WX-18-4 and blocks an easy laundering path via WX-18-5.

**4. `reference-validation.md` v1 §9**

Current text:
> 6. Label discipline collapse (§8): `validation: reference-validated` artefacts used externally without the label qualification; kernel §7's anti-substitution clause softened or removed without concurrent strengthening elsewhere.

Proposed replacement:
> 6. Label discipline or scope softening (§8): `validation: reference-validated` artefacts used externally without the label qualification; kernel §7's anti-substitution clause softened or removed without concurrent strengthening elsewhere; or §1 C3 narrowed from cross-family contamination screening to family-conditional screening without explicit concurrent narrowing of claim language and labels.

Proposed insertion after item 6:
> 7. Saturation-gate false-negative pattern: after adoption of the revised L1 gate, two candidate cases in a single reference-selection series survive thin-canary screening but are rejected at the full-constraint probe by explicit naming, distinctive-sequence recovery, or >80% shared 5-gram overlap.

Reason: item 6 blocks future accommodation-by-narrowing; item 7 turns repeated L1 under-sensitivity into an observable re-opening condition.

I would leave the following unchanged for now:
- `reference-validation.md` §1 flagged tension text;
- `reference-validation.md` §8 label discipline text;
- `methodology-kernel.md` §7;
- `multi-agent-deliberation.md` v3.

## Q4. Do these revisions affect OI-016 status, §9 triggers, or §8 label discipline?

OI-016 should remain **Resolved — provisional** after Session 019. I would not re-open it now.

The revisions I’m proposing strengthen the re-opening machinery rather than soften it:
- §8 stays unchanged;
- §9 item 6 becomes stricter about future scope-softening;
- new §9 item 7 makes repeated L1 false negatives observable.

Because I am not proposing any softening of kernel §7 or any narrowing of C3 to “only the family we plan to use,” there is no compensating-strengthening problem to solve in the present revision. The compensating strengthening is precautionary: it makes future softening visible if someone later tries it.

## Q5. Does the “provisional substitute” minority now warrant a kernel change?

No, not yet.

WX-18-3 materially supports the Skeptic minority’s caution, but it does not activate the minority’s stated warrant. The warrant preserved in §10 is specific:
> “if label discipline collapse (§9 trigger 6) is observed”

That condition has not occurred. What has occurred is evidence that the operating region may be narrow. That is important, but it is not the same problem.

So my position is:
- keep kernel §7 unchanged for Session 019;
- keep the Skeptic minority preserved and salient;
- do not preemptively rename reference-validation as “provisional substitute” on the basis of one C3 failure.

If later sessions show repeated candidate-pool collapse after the L1 fix, then I would revisit this. At that point the argument would not be “label discipline already collapsed,” but “the mechanism’s usable domain is so narrow that the kernel should stop naming it as co-equal in practice.” That is a stronger empirical basis than the one now available.

## Q6. OI-002 change scope: substantive or minor?

`reference-validation.md`: **substantive**.

These changes add and sharpen normative content:
- mandatory full-constraint probe before seal;
- canary explicitly downgraded from sufficient-adjacent to supplementary;
- explicit naming/distinctive-sequence recovery becomes rejection basis;
- L3 no longer treats pre-seal divergence as design evidence;
- §9 gains stronger re-opening conditions.

`multi-agent-deliberation.md`: **no change** under my recommendation.

`methodology-kernel.md`: **no change** under my recommendation.

## Q7. What preserved first-class minorities should the revised spec carry?

1. **Preserve the Session 014 Skeptic “provisional substitute” minority as-is.** I would not convert it to main text, but I would explicitly note in the Session 019 decision record that WX-18-3 increased its empirical credibility without satisfying its activation condition.

2. **Preserve any Session 019 minority that argues for no immediate spec revision beyond watchpointing.** That is a legitimate conservative position, especially on `n=1`.

3. **Preserve any Session 019 minority that argues WX-18-5 should change Produce-family selection now.** I would oppose adopting that view now, but it is exactly the kind of fork that should remain visible because it affects anti-laundering discipline and future kernel scope.

4. **Preserve any minority that resists new §9 item 7 as too trigger-happy.** I think the trigger is worthwhile, but if others judge it premature, that dissent is worth carrying.

## Q8. Anti-laundering check: do these revisions strengthen the mechanism or widen pass?

They strengthen it.

The hardening passages are:
- in C3: “**both completed before seal**” and “**Canary survival … does not satisfy C3 on its own**”;
- in C3: rejection on “**explicitly names the reference**” or “**reproduces its distinctive labelled sequence**”;
- in L3: “**Cross-family divergence is interpretable only after the candidate has already passed L1**”;
- in L3: “**A candidate that fails C3 is not rescued by cleaner output from another family**”;
- in §9.6: future narrowing from cross-family to family-conditional screening becomes an explicit re-opening trigger;
- in §9.7: repeated false-negative gating becomes observable instead of being hand-waved as bad luck.

What I am explicitly not proposing:
- not dropping the canary because it missed once;
- not raising overlap thresholds;
- not allowing a candidate to pass because only one family was contaminated;
- not shifting to non-Claude Produce as an escape hatch for a Claude-saturated case;
- not widening the label claim.

That last point matters most. If Session 019 responded to D2 by saying, in effect, “reference-validation still passes as long as one family remains clean and we use that family,” that would be accommodation. It would redefine the test around the observed weakness. My proposed §9.6 text is there specifically to make that manoeuvre visible.

So my Outsider judgment is: revise now, but only by making failure easier to detect and harder to explain away.
