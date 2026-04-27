---
session: 077
title: Design space for the next-generation engine
date: 2026-04-27
engine_version_at_open: engine-v16
mode: self-development
---

# Assessment

## State at session open

Engine-v16 is the active surface (eight files, ~350 lines): `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, `specifications/{methodology,constraints,workspace,engine-manifest}.md`, `tools/validate.sh`. The trim-and-restart at session 076 reset the spec set; the seventy-five-session pre-restart history is at `archive/pre-restart/` and in git log. Workspace-scope state (`provenance/`, `applications/`, `engine-feedback/`, `open-issues/`, `validation-debt/`, `records/`) is preserved in place; cross-references from that state into specs that have moved to archive are broken by design and are part of what sessions 077–078 will decide what to do about.

## What this session advances

Per session 076's close (`provenance/076-engine-restart/03-close.md` §"What session 077 should address"), session 077 produces the **design space** for the next-generation engine. The brief is `applications/075-selvedge-restart/selvedge-problem-statement.md`, distilled into `specifications/constraints.md`. The design space must include:

1. A database backend for structured state (identifiers, decisions, references, lifecycle records, counters in a queryable store with integrity guarantees).
2. Multiple new agents (rough shape: reader, specifier, decider, deliberator group, reviewer, validator, assembler) — each with bounded context, coordinating through the substrate.
3. A subtraction role with the authority to remove (a structural role, not another counter).
4. A deliberately-built human review role with defined scope and scheduled cadence.

This session does **not** commit to a solution. It produces the surface session 078 designs against: candidate architectures, open questions to resolve, directions rejected with reasons.

## How this session runs

Multi-agent deliberation per `specifications/methodology.md` §When to convene multiple agents. Five perspectives. Each writes its position blind — before seeing any other perspective's output — to prevent anchoring (operationally, all five seed prompts are launched in parallel and all write to disk before synthesis begins). Synthesis preserves dissent.

| # | Perspective | Family | Role |
|---|-------------|--------|------|
| 1 | Architect | Anthropic (Claude) | Proposes candidate architectures from the brief. |
| 2 | Adversary | Anthropic (Claude) | Challenges the emerging direction; surfaces unstated assumptions; argues for the proposition that the multi-agent + database direction is wrong. |
| 3 | Subtractor | Anthropic (Claude) | Argues for cutting more before adding. Treats every proposed addition as cost. |
| 4 | Cross-family generalist | OpenAI (codex) | Independent reading of the brief from outside the Claude pretraining distribution. Surfaces shape-of-question assumptions Claude may not see. |
| 5 | Cross-family DevOps / engineering | OpenAI (codex) | Engineering pragmatics: what does the data substrate actually look like at the schema level? What scales? What breaks? What ops burden does each candidate impose? |

Two cross-family voices is a deliberate choice this session. The brief in `constraints.md` calls out multi-family deliberation for foundation-touching decisions; it also calls out structural state as the substrate failure mode. Pairing a cross-family generalist with a cross-family engineering specialist tests both axes.

Codex perspectives are invoked via `codex exec --sandbox read-only --skip-git-repo-check` with the seed prompt written to a tmp file and piped as stdin. Outputs are captured to `perspectives/04-codex-generalist.md` and `perspectives/05-codex-devops.md`.

Claude perspectives are invoked via the Agent tool (general-purpose subagents). Each subagent is instructed to read only the four engine specs plus the operator brief plus its own role framing — not the other perspectives' outputs. Subagent outputs are written to `perspectives/01-architect.md`, `02-adversary.md`, `03-subtractor.md`.

## What this session reads

- The four engine-v16 specs (`methodology.md`, `constraints.md`, `workspace.md`, `engine-manifest.md`).
- `prompts/development.md` (executable prompt for self-development).
- `applications/075-selvedge-restart/selvedge-problem-statement.md` (operator's framing).
- `provenance/076-engine-restart/03-close.md` (most recent close).
- `open-issues/index.md` (active issues, mostly stale post-restart but read for awareness).

The session does not load the seventy-five-session pre-restart provenance.

## What this session does not do

- Does not commit to a database schema, an agent topology, or a coordination protocol.
- Does not retire or modify any active engine-v16 file.
- Does not delete or rearrange workspace-scope state preserved by session 076.
- Does not update `engine-manifest.md` (no engine version bump).
- Does not run a close-time reviewer audit (the prior reviewer mechanism is itself in redesign scope per 076's honest-limits note; whether 078 reviews this session retrospectively is 078's call).

## Agenda

1. Write blind seed prompts for the five perspectives.
2. Run all five perspectives in parallel; capture blind positions.
3. Synthesise to `01-deliberation.md`, preserving dissent.
4. Decide the design-space surface to `02-decisions.md`: candidate architectures, open questions for 078, rejected directions with reasons.
5. Validate (`tools/validate.sh`), close (`03-close.md`), commit, push.
