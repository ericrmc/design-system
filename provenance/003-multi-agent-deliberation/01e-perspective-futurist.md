---
session: 003
title: Raw Perspective — Futurist
date: 2026-04-17
status: complete
perspective: Futurist
agent-type: general-purpose subagent (parallel, context-isolated)
---

*This file preserves the raw output from the Futurist perspective verbatim, without editorial change. See `01-deliberation.md` for synthesis.*

---

# Futurist Position

The mechanism of the day — parallel Claude subagents — is a transient implementation; the specification must name the abstract pattern (independent perspectives deliberating in isolation, then synthesized) so that swapping in heterogeneous models, humans, tool-using agents, or persistent personas is a configuration change, not a revision to the kernel.

## Q1. When should multi-agent deliberation be used?

Selectively, by a capacity-and-consequence test: invoke multi-perspective deliberation when a decision's consequences propagate (changes kernel terminology, constrains future sessions, or encodes a norm) OR when the question is genuinely contested within the design space. Trivial housekeeping decisions should not pay the cost. The criterion should be written in terms of decision properties, not session phases, because future mechanisms may make convening cheap enough that the threshold shifts. Lock in the *criterion language*, not the *current cost curve*.

My doubt: "substantive" is fuzzy. A specification must give operational tests (e.g., "does this decision modify a living specification's Specification section?") rather than relying on judgment.

## Q2. How should perspectives be selected and briefed?

Three to seven perspectives. Fewer than three is two-sided debate; more than seven produces synthesis fatigue and token cost without marginal diversity gain. Each perspective is defined by a **stance brief** — a small structured artifact with: name, one-sentence stance, concerns/priorities, what it is authorized to dismiss, and explicit acknowledgement of its blind spots.

Terminology to abstract out now:
- Don't say "subagent" in the specification. Say **participant** or **perspective-holder**. A future participant may be a human, a different model, or a persistent persona.
- Don't say "context-isolated" as the mechanism. Say **independence-preserved**, with a note that the current implementation achieves this via parallel isolated contexts. Tomorrow's may achieve it via different-model instantiation, or by convening humans who haven't seen prior replies.
- Don't say "brief." Say **stance specification** or keep "brief" but define it as the artifact, so it can carry tool grants, persona continuity pointers, or human-reviewer instructions later.

Workspace context: each participant gets the *problem brief* and *only the files their stance requires*. Uniform full-context distribution undermines the value of differentiated perspectives. The mechanism should let a brief declare its reading requirements.

## Q3. How should anchoring be prevented?

Parallel isolation is sufficient for the current mechanism but will not be sufficient for all future ones. Specify the **property** ("no participant's output can influence another participant's reasoning during the independent phase") rather than the mechanism. Future asynchronous deliberations spanning sessions will need explicit quarantine rules. Future human participants will need written instructions not to read peers' drafts.

Additionally: order of synthesis can anchor the synthesizer. Randomize or alphabetize the order in which perspectives are presented to the synthesis step. This is cheap insurance.

## Q4. How should outputs be synthesized?

The synthesis step is the riskiest single point in the whole pattern — it is where N perspectives collapse to one record and where a single agent's bias re-enters. Treat the synthesizer as a **named role** with its own specification, not as a side-effect of the orchestrating session.

Required properties of synthesis:
- Must cite each perspective by name for every claim of agreement or disagreement.
- Must preserve dissent explicitly — a minority position is a first-class output, not a footnote.
- Must distinguish *convergence* (all perspectives reached similar conclusion independently) from *coverage* (only one perspective raised a point, others were silent). These are different epistemic states and future readers need both.

Future-proofing: the synthesizer should eventually be pluggable — a different model, a human, or a panel. Don't bake in "the orchestrator synthesizes."

## Q5. How should this be recorded in provenance?

Preserve: (a) every stance brief as written, (b) every raw participant output verbatim, (c) the synthesis, (d) the synthesizer's identity and instructions. Raw outputs are not redundant — they are the only way a future session can audit whether the synthesizer distorted, and the only way a future mechanism (different model, human reviewer) can re-synthesize from the same sources.

Store them as separate addressable artifacts, not concatenated blobs. Addressability matters when provenance is queried later.

## Q6. What are residual limitations?

All participants here are Claude instances. Shared training data produces shared blind spots: the same cultural priors, the same argumentative reflexes, the same refusal patterns, the same aesthetic preferences baked into RLHF. Parallel isolation prevents *conversational* anchoring but not *training-distribution* anchoring. The specification must say this plainly: "Current mechanism achieves perspective-independence at the reasoning-thread level, not at the epistemic level. Residual homogeneity is expected and unmeasured."

Graceful degradation to name now:
- One participant failing (timeout, refusal, malformed output) must not block the deliberation. Specification should define a minimum-viable-quorum (e.g., three of five) and a protocol for recording the absence.
- Participants disagreeing with the brief itself — refusing the stance — should be recorded, not coerced. That is signal.

## Q7. Does the kernel need substantive revision?

Elaboration, not revision — provided the kernel already contains language general enough to host this pattern. If the kernel currently says "deliberation" without specifying single-agent vs multi-agent, a new specification (`multi-perspective-deliberation.md` or similar) plus a minor kernel clarification suffices. If the kernel assumes single-perspective flow, the kernel needs one targeted revision to neutralize that assumption, and everything else goes in a child specification.

My doubt: I haven't read the kernel, so this is conditional. The Decider should check.

## What I cannot answer from this perspective

- Whether the current kernel's language is already mechanism-neutral, or smuggles in single-agent assumptions I'd need to see to diagnose.
- The token and latency budget that makes the "three to seven perspectives" recommendation practical or impractical for this project's session cadence.
- Whether human participants are plausible for this methodology's roadmap or purely hypothetical — the answer changes how hard we push on heterogeneity-now vs. heterogeneity-later.
- Concrete synthesis quality metrics; I can name properties but not validate them empirically from here.
- Whether OI-004 tracks other concerns beyond what this brief names.
