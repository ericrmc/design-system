---
session: 003
title: Raw Perspective — Methodologist
date: 2026-04-17
status: complete
perspective: Methodologist
agent-type: general-purpose subagent (parallel, context-isolated)
---

*This file preserves the raw output from the Methodologist perspective verbatim, without editorial change. See `01-deliberation.md` for synthesis.*

---

# Methodologist Position

Multi-agent deliberation must be adopted as the default for substantive work because the methodology's own principles — self-hosting, honest acknowledgment of limitations, and the injunction against single-perspective substantive work — already require it; what remains is to specify it precisely enough that it is auditable, not to debate whether.

## Q1: When should multi-agent deliberation be used?

Selectively, by an explicit criterion tied to what the methodology already distinguishes. The kernel (per my reading) already separates routine mechanical acts (Read, Record, Close) from generative ones (Convene, Deliberate, Decide, Produce). Multi-agent deliberation should be **required** whenever the Deliberate activity produces a Decision that will be recorded in provenance — i.e., anything that becomes a D-### entry or modifies a specification. It should **not** be required for: fixing a typo, executing an already-decided plan, reading files, or writing synthesis prose once a decision is made. The criterion is provenance-binding: if the output will be immutable and future sessions will rely on it, the reasoning that produced it must not have been single-perspective. This respects D-009's acknowledgment without overreaching into activities where disagreement adds nothing. Doubt: the line between "substantive" and "mechanical" is itself a judgment call, and a lazy session could rationalize any decision as mechanical. The specification needs a default-on rule with an explicit, recorded justification required to opt out.

## Q2: How should perspectives be selected and briefed?

Three to five perspectives per deliberation. Fewer than three and you risk a tiebreaker-less binary; more than five and synthesis degrades into summarization. Stances must be written as **roles with stakes**, not viewpoints with labels — "the Methodologist who fears incoherence" rather than "pro-coherence view." Each brief should contain: (a) the problem statement verbatim, (b) the role's concern and what it is accountable for, (c) the decision questions, (d) the output format, and (e) an explicit instruction about what workspace context is and is not shared. Context should be **minimal and identical** across perspectives — the same problem brief, no workspace file access during reasoning. Asymmetric context creates spurious disagreement (agents disagreeing because they read different things) and masks genuine disagreement. This aligns with the self-hosting principle: the methodology's own specifications, if relevant, should be quoted into the brief rather than fetched by each agent.

## Q3: How should anchoring be prevented?

Parallel isolation handles temporal anchoring. Two further sources remain. First, **brief-anchoring**: the convener writes the briefs, and biased framing propagates into all perspectives identically. Mitigation: briefs should be drafted and then reviewed against a checklist (does it telegraph a preferred answer? does it omit a legitimate counter-position?). Second, **role-anchoring**: the set of roles chosen determines the space of possible disagreement. If you convene three variants of "careful pragmatist," they will agree. Mitigation: the convener must justify in provenance why the chosen role set spans the legitimate disagreement space, and a "Devil's Advocate" or "Skeptic" role should be mandatory when a decision feels consensual at convening time. No additional machinery beyond these.

## Q4: How should outputs be synthesized?

A separate synthesis step performed by a fresh agent (not one of the deliberators) whose job is explicitly *not* to decide but to map. The synthesis output should contain: (1) points of agreement across perspectives, (2) genuine disagreements with each side's strongest form, (3) unresolved questions no perspective addressed, and (4) a recommended decision **with explicit dissent preserved**. The Decide activity then operates on the synthesis, not the raw essays. Crucially: synthesis is not averaging. If four perspectives concur and one dissents with a strong argument, the synthesis must preserve the dissent as-is, not dilute it. This respects provenance-preservation (D-???; whichever decision establishes immutability).

## Q5: How should this be recorded in provenance?

All of it. Raw perspective outputs, briefs given, synthesis, and final decision — preserved verbatim, immutably, linked to the session. The briefs especially: they are where bias enters, and future sessions auditing a decision need to see them. Storage cost is negligible; epistemic cost of discarding is permanent. This is a direct implication of the existing provenance-immutability principle — if we discard raw reasoning, we cannot honestly claim provenance.

## Q6: What are residual limitations?

Substantial and worth stating plainly in the specification. All perspectives remain Claude — same training corpus, same RLHF shaping, correlated blind spots. Parallel isolation prevents visible convergence but not shared-prior convergence; agents may agree not because the answer is obvious but because they share a training distribution. The specification should say: "Multi-agent deliberation via parallel Claude subagents is stronger than single-agent simulation and weaker than genuine model/human diversity. Decisions made this way carry the residual bias of the shared model. Sessions with access to different models or human participants should use them; this mechanism is the floor, not the ceiling." Open Issue OI-004 should remain open, not close, with this characterization.

## Q7: Does methodology-kernel need substantive revision?

Elaboration, not revision. The kernel already contains the principles that require this (no single-perspective substantive work; honest limitation-acknowledgment; self-hosting). A new specification — call it `multi-agent-deliberation.md` — should define the mechanism, and D-009 should be updated with a cross-reference to it. A **minor** kernel update is warranted: a single sentence in Convene/Deliberate that says the default is multi-agent and points to the new spec. Anything more would be overreach and break the kernel's small-surface property. Flag: I am inferring the kernel is small-surface; if it is not, this answer needs revisiting.

## What I cannot answer from this perspective

- Whether the cost of running N subagents per deliberation is affordable in practice (Pragmatist question).
- Whether three, five, or some other number is empirically the sweet spot (Empiricist question).
- What synthesis *quality* looks like when the synthesizer is also Claude (meta-concern; I flag it but cannot evaluate it).
- Whether existing decisions D-001 through D-008 and D-010 through D-014 contain rules that contradict this proposal — I do not have their text in this brief and am reasoning from D-009 and OI-004 alone. If any of those decisions bind convener behavior or prohibit parallel reasoning, this position may need revision.
