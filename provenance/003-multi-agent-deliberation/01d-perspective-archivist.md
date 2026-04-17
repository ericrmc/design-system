---
session: 003
title: Raw Perspective — Archivist
date: 2026-04-17
status: complete
perspective: Archivist
agent-type: general-purpose subagent (parallel, context-isolated)
---

*This file preserves the raw output from the Archivist perspective verbatim, without editorial change. See `01-deliberation.md` for synthesis.*

---

# Archivist Position

**Stance:** Multi-agent deliberation is only as valuable as what survives it; every provenance choice must be made as though the synthesis will be lost and the raw outputs are all that remains.

## Q1: When should multi-agent deliberation be used?

Selectively, and the criterion should be recordable. My position: multi-agent deliberation is required whenever a session produces a Decision that will be cited by name (D-xxx) in any future specification's Validation section. For Reads, Assessments, Produce steps, and administrative Decides, a single agent is sufficient and the record stays clean. The cost of multi-agent work is archival weight — more files, more briefs, more reconstruction burden — and that cost must be earned.

The practical test I'd codify: if the Decide activity would, under single-agent work, need to invoke the "what would someone who disagrees say" move, then convene. If it would not, don't. The session log should record which Decides triggered multi-agent work and which didn't, so the threshold itself accumulates evidence.

My doubt: "substantive" is soft. Future agents may rationalize skipping the mechanism. A harder trigger — e.g., "any Decision that amends methodology-kernel" — may be needed. Flagging for the Deliberate step.

## Q2: How should perspectives be selected and briefed?

Three to five perspectives. Fewer than three collapses to pairwise argument; more than five dilutes each voice in synthesis and blows out the archive.

Each perspective gets a brief with a fixed schema — this matters for reproducibility:

```
deliberations/<session-id>/<decision-id>/briefs/<NN>-<role>.md
```

Schema sections: `Role`, `Stance`, `Methodology context` (shared across all briefs, identical text), `The question` (shared), `Specific concerns` (role-specific), `Response format`, `Constraints`. The shared sections must be byte-identical across briefs in a single deliberation — diffing briefs should reveal only the role-specific delta. This is what makes deliberations re-runnable.

Workspace context: minimum viable. Each agent sees the brief and nothing else — no file reads, no tool use beyond reasoning. This is already the current mechanism and I endorse it for archival reasons: if agents read arbitrary workspace state, the record can't tell future readers what input produced the output.

How a stance is written: second person, imperative, naming the specific anxieties that perspective holds. Not a persona sketch — a job description with teeth.

## Q3: How should anchoring be prevented?

Parallel isolation handles temporal anchoring. The residual risk is *brief anchoring* — the writer of the briefs shapes outcomes by what concerns they plant. Two defenses:

1. The brief-writer (the convening agent) must themselves be briefed, and that meta-brief is preserved as `deliberations/<session-id>/<decision-id>/convene-brief.md`.
2. Briefs are written before any deliberation begins and committed to git in a single commit. No brief is edited after agents begin responding. The commit hash is the anchor.

I don't think anything else is needed at current scale. Adding more anti-anchoring machinery would be ornamental.

## Q4: How should outputs be synthesized?

Synthesis is an act of authorship and must be marked as such. My convention:

- Raw outputs are preserved verbatim at `deliberations/<session-id>/<decision-id>/responses/<NN>-<role>.md`.
- Synthesis lives at `deliberations/<session-id>/<decision-id>/synthesis.md`.
- Every claim in synthesis that attributes a position to a perspective must cite the source file and a line range or quoted fragment, e.g., `[Archivist, responses/03-archivist.md, Q4]`.
- Synthesizer-original claims (framings, resolutions, compromises not present in any source) are marked `[synth]`. Readers can then compute the ratio of cited to synthesized content and judge honesty.

The synthesis.md should have a fixed structure: per-question summary, points of agreement, points of disagreement, synthesizer resolution (if any), and open threads surfaced but not resolved. The synthesizer must name themselves and the agent they were at synthesis time (model ID, date).

My doubt: citation overhead may cause synthesizers to paraphrase rather than quote to avoid tagging every sentence. A linter-style check — "synthesis contains no unattributed paraphrases of perspective-specific language" — might be needed but is hard to automate. Flag for later.

## Q5: How should this be recorded in provenance?

Preserve everything. Storage is cheap; context reconstruction is expensive.

Directory layout:
```
provenance/sessions/<session-id>/deliberations/<decision-id>/
  convene-brief.md          # meta-brief for the convening agent
  briefs/
    00-shared-context.md    # the identical shared sections, extracted once
    01-<role>.md            # role-specific delta only
    ...
  responses/
    01-<role>.md
    ...
  synthesis.md
  manifest.json             # model IDs, timestamps, commit hash at convene, token counts
```

`manifest.json` is load-bearing: it records which model produced which output and when. Without it, three years from now, "a Claude subagent said X" is untraceable to capability. Include model version strings exactly as the runtime reports them.

Briefs AND raw outputs AND synthesis — all three. Dropping any one breaks a reconstruction path.

## Q6: What are residual limitations?

All perspectives are Claude. This is monoculture. The specification must say so in plain language, in a `Limitations` section, not buried in Open Issues. Suggested text: *"Multi-agent deliberation in this methodology currently uses parallel instances of a single model family. Shared training produces shared blind spots. This mechanism is an improvement on single-context simulation but does not substitute for cross-model or human participation. Deliberations producing decisions that amend methodology-kernel should flag this limitation explicitly in their synthesis."*

Residual bias this doesn't fix: shared priors about what counts as a "good" methodology, shared rhetorical conventions, shared tendency to converge on plausible-sounding compromise. Parallel isolation reduces *within-session* anchoring, not *training-induced* agreement.

## Q7: Does methodology-kernel need substantive revision?

New specification (`multi-agent-deliberation.md`) plus a minor update to methodology-kernel — one sentence pointing to the new spec under the Convene/Deliberate activities. The kernel stays stable; the mechanism spec carries the detail. This matches how Session 002's validation work layered in without rewriting the core.

## What I cannot answer from this perspective

- **Right number of perspectives.** I argued 3-5 from archival cost; someone reasoning about deliberation quality may have a sharper number.
- **Whether synthesis should itself be multi-agent.** I assumed a single synthesizer for traceability, but that reintroduces single-perspective bias at the most consequential step. Needs a deliberation-methods voice.
- **When to re-run a deliberation.** Briefs are reproducible by design, but I don't know the trigger for re-running — only how to make it possible.
- **Cost ceilings.** Token/time budgets for deliberations aren't my call; an economics-minded voice should weigh archival completeness against session throughput.
