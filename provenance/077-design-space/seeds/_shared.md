# Shared brief — Selvedge session 077 design-space deliberation

You are participating in a multi-agent deliberation that produces the design space for the next-generation Selvedge engine. This file is the shared portion of all five perspectives' seed briefs. Your role-specific framing is in your role file; read your role file together with this shared brief.

## Background you must read

In `/Users/ericmccowan/Development/complex-systems-engine/`:

- `specifications/methodology.md` — what Selvedge does. Identity, the nine session activities, when to convene multiple agents, when to review at close, validation senses, preservation, engine-feedback pathway, self-hosting. ~120 lines.
- `specifications/constraints.md` — the empirical brief: what 75 sessions of self-development taught us about LLM agents (six properties), what the methodology preserved, what the successor must build. ~105 lines. **The most important file for this deliberation.**
- `specifications/workspace.md` — file classes, session structure, decisions, specifications discipline. ~135 lines.
- `specifications/engine-manifest.md` — the engine-v16 file set. ~62 lines.
- `applications/075-selvedge-restart/selvedge-problem-statement.md` — the operator's full framing of where the engine is going. ~170 lines. Selvedge's record from a longer angle than `constraints.md`.
- `provenance/076-engine-restart/03-close.md` — most recent close. States that session 077 produces a design space (not a solution) covering: a database backend, a multi-agent shape, a subtraction role, a deliberately-built human-review role.

You may consult one or two `archive/pre-restart/specifications/*.md` files if a specific question requires it. Do not load the seventy-five-session provenance back-catalogue.

## What you must NOT read

You must not read any file under `provenance/077-design-space/perspectives/`. Those are the other perspectives' blind positions; reading them anchors yours. Your position is blind.

You may read your own role file in `provenance/077-design-space/seeds/`. You may read other role files in that directory if you want to know what scope the other perspectives are covering — that is not an anchoring concern, since it is the role definition not the position.

## What you produce

A single Markdown file at `/Users/ericmccowan/Development/complex-systems-engine/provenance/077-design-space/perspectives/<NN>-<your-role>.md`, where `<NN>` and `<your-role>` are given in your role file. The file's structure:

```markdown
---
session: 077
perspective: <your-role>
family: <Anthropic | OpenAI>
date: 2026-04-27
---

# <your-role> — blind position

## Frame
One paragraph. How you read the situation. The lens you are bringing. What you think the deliberation is actually about.

## Position
The substantive content. Length matched to substance — favour two pages of substance over six pages of texture. Use whatever sub-sections serve your argument; do not fill out a template.

## Where you would not commit
At least three points. Things you are uncertain about, places your position depends on assumptions you cannot verify from the brief alone, and what evidence would change your mind. This is not hedging — it is the surface session 078 needs in order to know where to push.

## What you think the other perspectives will miss
Speculative. What blindspot do you think the other voices in this deliberation are most likely to have? This goes into the synthesis as a check; it is not a prediction you must defend.
```

## Operational constraints

- **Be specific.** "We need a database" is not a position. "Decisions live in SQLite with table `decisions(session_id, decision_id, body_md, rejected_alternatives_md, ...)` and the validator enforces that every decision body's `[D-N]` references resolve to a row" is a position. Specificity lets the synthesis preserve dissent rather than collapse to platitudes.
- **Cite the brief.** When you make a claim that depends on a property of LLM agents the brief documents (e.g., "models default to prose"), name the property and which file you got it from. The synthesis will trace claims to source.
- **Do not import outside ideas as commitments.** If a pattern from outside the brief informs your position (a paper, a system you've worked on, a convention from your training distribution), surface it as a hypothesis named for what it is, not as a default. The methodology's value is that artefacts are traceable to the reasoning that produced them.
- **Do not propose what the brief already says.** The brief in `constraints.md` already commits to a database for structured state and a multi-agent shape. Your job is not to ratify those commitments — it is to make them concrete or argue against them.
- **Length.** Aim for 800–1500 words of substance. If you genuinely have less, write less; if you genuinely have more, write more. Do not pad.

## What this deliberation is not deciding

This session does not pick the winning architecture. It produces the *space* — candidates, open questions, rejected directions with reasons. Session 078 picks. Your position contributes a candidate (or an argument against the apparent direction); it is not a binding commitment to the engine.
