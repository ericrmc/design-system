---
session: 003
title: Raw Perspective — Pragmatist
date: 2026-04-17
status: complete
perspective: Pragmatist
agent-type: general-purpose subagent (parallel, context-isolated)
---

*This file preserves the raw output from the Pragmatist perspective verbatim, without editorial change. See `01-deliberation.md` for synthesis.*

---

# Pragmatist Position

Multi-agent deliberation should be a sharp tool reserved for genuinely consequential or contested decisions, with a minimum viable shape (3 perspectives, ~200-word briefs, single synthesis pass) that a tired session at 11pm will actually execute rather than skip.

## Q1. When should multi-agent deliberation be used?

Selectively. Triggering on "all deliberations" guarantees silent regression — the spec will be routinely violated within five sessions. Triggering on "substantive decisions" is too vague to enforce.

Concrete criteria, any one of which triggers multi-agent:
- The decision modifies the methodology-kernel or a spec's Purpose section.
- The decision creates a new top-level specification.
- Reasonable practitioners could disagree (the session author must be able to name two plausible positions before starting).
- The decision is marked "load-bearing" in the session plan.

Routine decisions — naming, formatting, minor elaborations, bug fixes in validation scripts — get single-agent treatment with a one-line note: "Single-perspective; non-load-bearing." This makes the shortcut auditable rather than hidden.

Doubt I'll flag: the third criterion is subjective and will drift. Accept that. Better an imperfect trigger that gets used than a perfect one that gets bypassed.

## Q2. How should perspectives be selected and briefed?

**Number: 3, occasionally 4, never 2 or 5+.** Two produces tennis matches; five produces mush and quadruples cost. Three is the minimum that breaks ties and forces synthesis work.

**Stance briefs: 150-250 words each, hard cap 300.** Structure: (a) one-sentence stance, (b) what this perspective values, (c) what it is suspicious of, (d) specific argumentative moves it should make. The Pragmatist brief I received is near the upper bound and roughly right — any longer and the agent starts reciting the brief instead of reasoning from it.

**Workspace context per agent: the problem statement and directly relevant artifacts only.** Not the full workspace. Each agent should see (i) the problem brief (~500 words), (ii) any specification directly under revision, (iii) the three most recent related decisions. If an agent needs more, the convener has over-scoped the deliberation.

**Selection method:** The session lead drafts a candidate perspective list before convening. Perspectives should be chosen for expected disagreement on *this* problem, not as a reusable cast. "Pragmatist vs Theorist vs Historian" is fine for some problems; "Minimalist vs Completionist vs Sceptic" is right for others. No permanent roster.

## Q3. How should anchoring be prevented?

Parallel isolation (what's happening now) handles 80% of anchoring. Beyond that:

- Briefs written before any perspective runs, committed to git, not edited mid-deliberation.
- Synthesis must quote at least one specific phrase from each raw output. If a perspective's contribution cannot be quoted, either it added nothing or the synthesiser is anchoring.
- Do not run a "fourth round" to break ties. If three perspectives disagree, that disagreement is the finding — record it and let the Decide step resolve it.

I would not add adversarial review, debate rounds, or voting. Each of those sounds rigorous and triples cost for marginal gain.

## Q4. How should outputs be synthesized?

One synthesis pass by a single agent (likely the session lead), producing:

1. A one-paragraph convergence summary (what all perspectives agreed on).
2. Named disagreements, each 2-4 sentences, with a quoted phrase per side.
3. A residual-questions list.

Hard limit: synthesis ~500 words. If it's longer, the deliberation was too broad.

**Do not** attempt to merge perspectives into a single unified recommendation. The Decide step does that, informed by the synthesis. Keeping synthesis and decision separate preserves the honesty of the disagreement.

## Q5. How should this be recorded in provenance?

Preserve:
- Stance briefs (verbatim).
- Raw perspective outputs (verbatim).
- Synthesis.
- Decision, with explicit reference to which perspective(s) it drew from and which it rejected.

Storage: one directory per deliberation under the session's provenance folder. Raw outputs are named by perspective. This is non-negotiable — without raw outputs, future sessions cannot audit whether synthesis was faithful.

Cost: maybe 10KB per deliberation. Trivial.

## Q6. What are residual limitations?

All perspectives are still Claude, same model, likely same version, shaped by the same training. What parallel isolation buys is independence from conversational anchoring, not independence from shared priors. Expect:

- Shared blind spots go undetected.
- Shared stylistic tics (hedging, list-making, meta-commentary) appear across all perspectives.
- "Disagreements" may cluster around axes Claude finds salient, missing orthogonal concerns a different model or human would raise.

The specification should say this plainly: "Multi-agent deliberation with parallel Claude subagents reduces conversational anchoring but does not produce model-independent perspectives. Treat consensus across subagents as weak evidence, not strong." A periodic check — maybe every 10 sessions — where a human or a different model reviews a recent deliberation would catch drift.

## Q7. Does methodology-kernel need substantive revision?

Elaboration, not revision. The kernel already says substantive work shouldn't be single-perspective. What's missing is the *how*. Write a new specification — call it something like `multi-agent-deliberation.md` — with the triggers, numbers, and recording rules above. Update the kernel with a one-sentence pointer and a note that OI-004 is now addressed by that spec.

If the kernel needs rewriting to accommodate this, the kernel was wrong. It isn't.

## What I cannot answer from this perspective

- Wall-clock cost in this specific environment (I'd guess 2-5 minutes per deliberation for 3 parallel subagents, but I don't know the actual latency).
- Whether the orchestration tooling (`TeamCreate`) has constraints that make N=3 awkward or N=4 natural.
- Whether session leads have the judgement to apply the selectivity criteria honestly, or whether a stricter "all substantive decisions" rule is needed as a forcing function.
- Whether there's prior provenance structure that would conflict with the per-deliberation directory proposal.
- How to handle the case where a deliberation's synthesis itself is load-bearing and contested — recursive multi-agent synthesis feels wrong but I haven't thought it through.
