# Shared brief — Selvedge session 078 design-commitments deliberation

You are participating in a multi-agent deliberation that produces **design commitments** for the next-generation Selvedge engine. Session 077 produced the design space (candidates and open questions); 078 picks. Session 079 implements against 078's commitments.

This file is the shared portion of all five perspectives' seed briefs. Read it together with your role-specific brief.

## Background you must read

In `/Users/ericmccowan/Development/complex-systems-engine/`:

- `specifications/methodology.md` — what Selvedge does. ~120 lines.
- `specifications/constraints.md` — the empirical brief: what 75 sessions taught us about LLM agents. **The most important file.** ~105 lines.
- `specifications/workspace.md` — file classes, sessions, decisions, specifications discipline. ~135 lines.
- `specifications/engine-manifest.md` — engine-v16 file set. ~62 lines.
- `applications/075-selvedge-restart/selvedge-problem-statement.md` — the operator's full framing. ~170 lines.

Session 077's full record (read all of it):

- `provenance/077-design-space/00-assessment.md` — how 077 ran.
- `provenance/077-design-space/01-deliberation.md` — synthesis with seven convergence points and seven divergences. The divergences are 078's surface to commit against.
- `provenance/077-design-space/02-decisions.md` — the five 077 decisions (D-1 refusal contract; D-2 agent set candidates A-min/A-mid; D-3 substrate-shape candidates S1/S2/S3; D-4 minority positions D-4.a/b/c; D-5 design-then-implement split).
- `provenance/077-design-space/03-close.md` — what 078 must produce.
- `provenance/077-design-space/perspectives/01-architect.md` through `05-codex-devops.md` — the five blind positions 077 produced. Read your counterpart from 077 first, then the others as your role requires.

You may consult `archive/pre-restart/specifications/*.md` if a specific question requires it. Do not load the seventy-five-session provenance back-catalogue.

## What you must NOT read

You must not read any file under `provenance/078-design-commitments/perspectives/`. Those are the other 078 perspectives' blind positions; reading them anchors yours. Your position is blind.

You may read your own role file in `provenance/078-design-commitments/seeds/`. You may read other role files there if you want to know what scope the other perspectives are covering.

## What you must NOT do

**Do not run `git`.** No `git add`, no `git commit`, no `git push`, no `git status`. Staging and commit are the orchestrator's responsibility. (This instruction exists because in 077 a subagent committed and pushed unilaterally before the orchestrator was ready; that was a mechanism failure recorded in 077's close.)

Do not modify any active engine-v16 file (`PROMPT.md`, `prompts/*`, `specifications/*`, `tools/*`). Your output is your perspective file only.

Do not invoke other Agent tools or spawn subagents.

## What you produce

A single Markdown file at `/Users/ericmccowan/Development/complex-systems-engine/provenance/078-design-commitments/perspectives/<NN>-<your-role>.md`, where `<NN>` and `<your-role>` are given in your role file. Structure:

```markdown
---
session: 078
perspective: <your-role>
family: <Anthropic | OpenAI>
date: 2026-04-27
---

# <your-role> — blind position

## Frame
One paragraph. How you read the situation. The lens you bring. What you think the deliberation is actually about, given that 077 produced the design space and 078 is committing against it.

## Position
The substantive content. Your role brief lists specific deliverables you primarily own and divergences you must engage. Address all of them. Length matched to substance — favour two pages of substance over six pages of texture. Use whatever sub-sections serve your argument; do not fill out a template.

## Where you would not commit
At least three points. Things you are uncertain about, places your position depends on assumptions you cannot verify, what evidence would change your mind. This is the surface 079 needs to know where the commitments are weakest.

## What you think the other perspectives will miss
Speculative. The blindspot you think the other voices in this deliberation are most likely to have. This goes into the synthesis as a check; not a prediction you must defend.
```

## Operational constraints

- **Be specific.** "Pick S1" is not a position. "Pick S1 with `body_md TEXT NOT NULL`, refusal contract `T1` through `T8` enumerated, worked example showing how a decision with `[D-3]` reference gets rejected on insert" is a position.
- **Cite the brief.** When a claim depends on a property of LLM agents the brief documents (e.g., "models default to prose"), name the property and which file it came from. Synthesis will trace claims to source.
- **Cite 077.** When you adopt or reject a 077 position, cite it: `[077-arch]`, `[077-adv]`, `[077-sub]`, `[077-gen]`, `[077-dev]`, or `[077-D-N]` for a 077 decision. The continuity-of-reasoning check requires this.
- **Do not import outside ideas as commitments.** If a pattern from outside the brief informs your position, surface it as a hypothesis named for what it is, not as a default.
- **Do not propose what the brief or 077 already commits to.** 077-D-1 commits to substrate-as-refusal-contract; 077-D-2 commits to ≤5 LLM agents with reader/validator/assembler as deterministic. Your job is to *operationalise* those commitments at a level 079 can build against, or to argue against them with cause.
- **Length.** Aim for 1000–1800 words of substance. Substrate-architect and cross-family engineer may run longer if the schema specificity warrants it; adversary may run shorter if its critique is sharp.

## What this deliberation is committing to

This session picks. The seven deliverables (per 077-D-5 and 077-`03-close.md`):

1. Refusal-contract specification for the chosen substrate-shape.
2. Agent-set commitment (A-min vs A-mid) with reviewer disposition.
3. Worked example: chosen substrate-shape produces methodology's existing artefacts (decision with rejected alternatives; specification with supersession edge; deliberation synthesis with preserved dissent).
4. Explicit dispositions on D-4.a (diagnosis-partial), D-4.b (subtractor=human?), D-4.c (further-cut engine-v16).
5. Schema-evolution protocol.
6. Substrate technology commitment (SQLite is hypothesis; concurrency answer required).
7. Handoff to 079 with implementation surface specified.

Your role brief tells you which deliverables you primarily own and which divergences you must engage substantively even when they are not your primary deliverable.
