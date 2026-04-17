---
session: 003
title: Raw Perspective — Skeptic (adversarial)
date: 2026-04-17
status: complete
perspective: Skeptic
agent-type: general-purpose subagent (parallel, context-isolated)
---

*This file preserves the raw output from the Skeptic (adversarial) perspective verbatim, without editorial change. See `01-deliberation.md` for synthesis.*

---

# Skeptic Position

This session is performing independence rather than achieving it, and the methodology is about to encode that performance as progress.

## Q1: When should multi-agent deliberation be used?

Never, under the current mechanism, as a default. The correct answer is "selectively, and rarely" — but the framing of the seven questions presumes multi-agent will be standard and only asks *which* cases. That ordering is already a concession I refuse.

Strongest failure mode: the methodology will apply multi-agent to routine decisions (naming, file layout, ordering of sections) because the machinery exists and using it feels rigorous. Each such use burns tokens, adds synthesis overhead, and trains the methodology's future sessions to treat the *presence* of multi-agent as a quality signal. Within five sessions this becomes ritual. Criterion I'd actually defend: multi-agent only when a single agent has already produced a draft decision and a named reviewer can identify a specific axis of likely blindspot. Otherwise: don't convene.

Strongest point. Weakest: I can't prove the slide to ritual will happen; I'm predicting institutional drift.

## Q2: How should perspectives be selected and briefed?

This is where the proposal is most fragile. Writing the brief *is* the deliberation. Whoever drafts "The Skeptic's job is to argue X" has already determined roughly what the skeptic will say — I am currently proving this by producing the argument the brief told me to produce. The brief even lists my "possible angles." I picked from the menu. An agent inhabiting a pre-written stance is a puppet with extra steps.

Number of perspectives: the honest answer is that below ~4 you get theater, above ~6 you get synthesis collapse, and at any number the briefs do the real work. 

Context exposure: every additional file shown to a perspective narrows them toward the existing methodology's vocabulary. Less context produces more genuine disagreement but also more irrelevance. There is no good setting. Name this openly in the specification rather than pretending a number exists.

Strongest point: brief-writing is upstream framing that the methodology is about to treat as neutral. Weakest: I have no alternative that isn't also framed by *someone*.

## Q3: How should anchoring be prevented?

Parallel isolation prevents *conversational* anchoring. It does nothing about *training* anchoring, which is the dominant failure mode here. Four Claude instances sharing weights, trained on overlapping corpora, given briefs written in a shared vocabulary, will correlate in ways that look like agreement but are actually shared priors. The methodology will read this correlation as convergence-on-truth. This is the central deception of the proposed pattern.

Mitigations that would actually help and are not in the proposal: (1) include at least one non-Claude model, even a weaker one, as a tiebreaker; (2) require the synthesis step to report *disagreement density* as a number, and flag sessions where it falls below a threshold as likely-correlated rather than likely-correct; (3) have a human read raw outputs before synthesis on any decision tagged substantive. Without at least (2), isolation is cosmetic.

Strongest point in my whole position.

## Q4: How should outputs be synthesized?

The synthesis step is where single-agent bias re-enters through the front door after being escorted out the back. One agent reads N essays and writes The Deliberation. That agent's framing choices — what to foreground, what to call "consensus," which dissent to treat as signal versus noise — now determine the record. The methodology will have spent tokens on N perspectives and then collapsed them through one.

Minimum acceptable: synthesis must quote, not paraphrase, the load-bearing sentences from each perspective. Disagreements must be listed as disagreements, not resolved. The synthesis agent should be forbidden from introducing claims not traceable to a raw output. If any of these are omitted the pattern is worse than single-agent work because it launders single-agent conclusions through apparent plurality.

## Q5: How should this be recorded in provenance?

Preserve everything: briefs, raw outputs, synthesis, and the identity of the agent doing synthesis. Anything less lets future sessions read a clean summary and forget the seams. My specific demand: briefs must be stored verbatim and flagged as framing artifacts, not neutral inputs. If the methodology ever cites a multi-agent deliberation without also making the briefs inspectable, it is citing its own framing as evidence.

## Q6: What are residual limitations?

All perspectives are Claude. Say this in the specification in exactly these words, not softened. Further: all perspectives were briefed by a process that itself had no adversary. The deliberation inherits whoever wrote the brief's blindspots. The methodology currently has no mechanism to audit brief-writing, and adding multi-agent deliberation to brief-writing creates infinite regress. The honest specification text is: "This mechanism reduces some forms of single-agent bias and introduces others. It is not independence. Treat its outputs as one agent's structured self-questioning, not as a panel."

## Q7: Does methodology-kernel need substantive revision?

Yes. Treating this as elaboration — a new specification slotting in beside existing ones — lets the methodology avoid confronting that D-009 and OI-004 are not solved by this session, merely attended to. The kernel should be revised to state that no current mechanism achieves genuine perspective independence, that OI-004 remains open after this session, and that any claim of resolution requires non-Claude or human participants. If the session closes OI-004 based on parallel Claude subagents, the methodology has lied to itself at the level of its own record. That is the worst possible failure for a self-hosting system.

## What I cannot answer from this perspective

- Whether non-Claude models are actually accessible to this methodology's operator, or whether I'm demanding something structurally unavailable.
- What the token/cost budget looks like in practice — my "rarely" recommendation might already be the default simply because multi-agent is expensive.
- Whether human participants are on any roadmap; if they are, my objections weaken considerably and the current pattern becomes a reasonable stopgap rather than a pretension.
- Empirical disagreement density between parallel Claude subagents — without measurement I'm asserting correlation I haven't proven.
