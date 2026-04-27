---
session: 078
title: Design commitments for the next-generation engine
date: 2026-04-27
engine_version_at_open: engine-v16
mode: self-development
---

# Assessment

## State at session open

Engine-v16 active surface unchanged from session 076 (eight files, ~350 lines). Session 077 produced the design space at `provenance/077-design-space/` — five blind perspectives, synthesis preserving dissent, five decisions (D-1 framing substrate as refusal contract; D-2 reducing brief's seven-role roster to A-min or A-mid; D-3 carrying three substrate-shape candidates S1/S2/S3 forward; D-4 preserving three minority positions; D-5 amending 076's handoff so that 078 commits and 079 implements).

The unilateral subtractor commit recorded in 077-`03-close.md` §"Honest limits" is the operative mechanism note for 078: subagent task prompts must explicitly forbid `git` invocations. Session 078 will obey that.

## What this session advances

Per `provenance/077-design-space/03-close.md` §"What session 078 should address," 078 produces design **commitments** against 077's surface. Seven concrete deliverables:

1. **Refusal-contract specification** for the chosen substrate-shape (D-1 + D-3).
2. **Agent-set commitment** — pick A-min vs A-mid; resolve the reviewer's status (kept-narrower-scope, deferred, or merged with subtractor/human).
3. **Worked example** — the chosen substrate-shape produces the methodology's existing artefacts (a decision record with rejected alternatives; a specification with supersession edge; a deliberation synthesis with preserved dissent) without losing readability.
4. **Explicit dispositions** on each of D-4.a (diagnosis-is-partial — Readings B and C), D-4.b (subtraction role and human reviewer collapse), D-4.c (further-cut engine-v16 by ~80–100 lines).
5. **Schema-evolution protocol** (Divergence-7).
6. **Substrate technology commitment** with concurrency-trial reasoning (Divergence-6 — SQLite is the working hypothesis but distributed/concurrent agents need an answer).
7. **Explicit handoff to session 079** with implementation surface specified at the level a single session can build against.

This session does **not** begin implementation. Session 079 builds against 078's commitments (per 077-D-5).

## How this session runs

Multi-agent deliberation per `specifications/methodology.md` §When to convene multiple agents. Five perspectives, two from a different model family (operator-confirmed at session open). Each writes blind before any sees another. Synthesis preserves dissent.

Role design differs from 077: 077 opened space with architect/adversary/subtractor/generalist/devops; 078 closes space by committing. Each 078 perspective owns one or more deliverables and engages assigned divergences from 077.

| # | Perspective | Family | Primary deliverables | Divergence engagement |
|---|-------------|--------|----------------------|-----------------------|
| 1 | Substrate-architect | Anthropic | Substrate-shape pick (S1/S2/S3); refusal-contract spec; worked example | Div-3 (body-in-cells vs index-only vs tuples); Div-7 (schema evolution input) |
| 2 | Agents-architect | Anthropic | Agent-set pick (A-min vs A-mid); reviewer disposition | Div-2 implementation; D-4.b position |
| 3 | Adversary | Anthropic | Stress-test against `constraints.md` six properties | D-4.a (Readings B and C); D-4.b (collapse argument) |
| 4 | Cross-family engineer | OpenAI (codex) | Substrate technology pick; concurrency reasoning; schema-evolution protocol | Div-6, Div-7 primary owner |
| 5 | Cross-family methodologist | OpenAI (codex) | D-4.c position (further cut to engine-v16); handoff design for 079 | D-4.a alternative reading; cross-family check on multi-agent direction itself |

Two cross-family voices is the same ratio as 077 (2-of-5). Reasoning: a single cross-family voice is more easily out-voted in synthesis when the deliberation reaches commitments; a paired cross-family voice forces the convergent cross-family observations to be load-bearing rather than incidental. The methodology requires *at least* one; two is a 078 choice with reasoning recorded here.

Codex perspectives invoked via `codex exec --sandbox read-only --skip-git-repo-check` with seed prompts written to tmp files and piped as stdin. Outputs captured to `perspectives/04-codex-engineer.md` and `perspectives/05-codex-methodologist.md`.

Claude perspectives invoked via the Agent tool (general-purpose subagent). Seed prompts forbid `git` invocations explicitly (per 077-`03-close.md` honest-limit-1).

## What this session reads

- The four engine-v16 specs (`methodology.md`, `constraints.md`, `workspace.md`, `engine-manifest.md`).
- `prompts/development.md`.
- `applications/075-selvedge-restart/selvedge-problem-statement.md`.
- `provenance/077-design-space/{00-assessment.md, 01-deliberation.md, 02-decisions.md, 03-close.md}` and the five `perspectives/` files.
- Session-specific role briefs in `provenance/078-design-commitments/seeds/`.

The session does not load 075-and-prior provenance back-catalogue.

## What this session does not do

- Does not begin implementation (per 077-D-5). No SQLite database is created. No migrations are written. No agent process is started.
- Does not commit to anything that would require modifying engine-v16 active spec content this session unless the commitment carries no plausible non-implementation realisation. Whether 078 bumps engine-v16 → engine-v17 is itself a 078 decision recorded in `02-decisions.md`.
- Does not run a retrospective close-time reviewer audit over 077. (Operator-directed at session open: 077's close self-documented honest limits thoroughly; reviewer mechanism is in redesign and would anchor 078 on a pattern that may not survive. The disposition decision belongs to 078 only inasmuch as 078 may surface engine-feedback if the lack of audit costs something.)

## Cautions specific to 078

The deliberation pattern's foundational risk for a *commitment* session, distinct from a *design-space* session:

- **Convergence pressure.** When five perspectives are asked to commit, they will tend toward the architecturally-easiest commitment (S1, A-mid, SQLite) because that minimises the prose cost of writing a position. The adversary's role is to push against this, but the synthesis must also actively check whether the commitment direction is a function of write-cost rather than judgment.
- **Anchoring from 077.** Each perspective in 078 has read 077's full surface, including the synthesis. This is unavoidable — 078 commits against 077 — but it means the adversary's Reading B / Reading C in 077-D-4.a will tend to be treated as "already considered" rather than as live alternatives. The 078 adversary must engage them as if for the first time.
- **The substrate-shape choice is irreversible in practice.** Once 079 implements one of S1/S2/S3, switching substrate-shapes mid-engine is a discontinuity comparable to the 076 trim. The worked-example deliverable (3) exists because the irreversibility justifies a higher evidence bar than 077's design-space deliberation provided.

## Agenda

1. Write seed briefs for the five perspectives.
2. Run all five perspectives blind in parallel; capture positions.
3. Synthesise to `01-deliberation.md` preserving dissent.
4. Decide the seven commitments to `02-decisions.md` with rejected alternatives.
5. Validate (`tools/validate.sh`), close (`03-close.md`), commit, push.
