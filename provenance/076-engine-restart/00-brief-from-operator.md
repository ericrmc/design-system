---
session: 076
title: Engine Restart Brief
date: 2026-04-27
captured-by: orchestrator
captured-from: operator-direct prompt
verbatim: true
---

# Engine restart brief (operator, verbatim)

The operator's prompt to session 076, captured verbatim. Effort level was set to `high` and then `max` immediately before the substantive prompt.

> read `/Users/ericmccowan/Development/complex-systems-engine/applications/075-selvedge-restart/selvedge-problem-statement.md` then scan the current project. Do not read full files; this has millions of words of content that is not relevant to you. read `/Users/ericmccowan/Development/complex-systems-engine/specifications/engine-manifest.md` for a good view of what the system is doing and what other files you need to read. Your goal is to restart this engine so it can be applied to itself and external applications, with only minimal human operator or human reviewer intervention. You can use extra Agents for research, reading, or even Agent Teams. You can read and act on PROMPT.md if you wish, but note the recent sessions are extremely heavy for ceremony and will break your context. You should not even read the previous 6 sessions like it says. Ideally, the specifications need to be trimmed right back in this session, and the next session should produce a design space using multi-agent deliberation that includes a database backend and multiple new agents for executing the methodology in a scalable way, and the session following that should design the solution. You should create a new session 076 to store this verbatim but you are welcome to ignore other instructions. You should not use tools in the substrate; they will be replaced by the new database backend. We are at a point where the validator will likely fail; you may treat errors as warnings.

## Operative directives extracted from the brief

- **Trim the specifications right back this session.** The active spec set has accumulated to ~3000 lines across 9 files plus ~3200 lines of superseded versions. Trim to a minimal viable set.
- **Don't read previous 6 sessions** despite the existing read-contract requiring it. Ceremony in those closes will overwhelm context.
- **Don't use the substrate tools** (retrieval, digest emitter/reconstructor). They will be replaced by a database backend designed in the next two sessions.
- **Treat validator failures as warnings** — the existing validate.sh references many things being deleted; expect breakage.
- **Next session (077) — design space via multi-agent deliberation** that includes (a) a database backend, (b) multiple new agents for executing the methodology in a scalable way.
- **Following session (078) — design the solution** based on the design space.
- **Goal — restart the engine so it can be applied to itself and external applications with only minimal human operator/reviewer intervention.**

## Frame

Application 075 (`applications/075-selvedge-restart/selvedge-problem-statement.md`) is the operator's framing of where Selvedge's seventy-five sessions of self-development have landed. Six properties of LLM agents surfaced over those sessions, the methodology's foundation survived contact with reality, and the path forward is a multi-agent system with a database substrate replacing the single-agent-with-Markdown-state arrangement that hit its ceiling around session fifty-eight.

The problem statement is the brief for sessions 077 and 078. It is preserved verbatim at `applications/075-selvedge-restart/selvedge-problem-statement.md`. The trimmed specifications produced this session are the minimum viable surface from which session 077 can run multi-agent deliberation on the design space.
