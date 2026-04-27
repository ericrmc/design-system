---
title: Engine Manifest
version: 16
status: active
created: 2026-04-27
updated-by-session: 076
supersedes: engine-manifest.md (engine-v15)
---

# Engine Manifest

This file enumerates the loadable Selvedge engine at the current commit. The engine is the file set listed below; loading the engine means having these files available and treating them as a closed unit for executing a session.

## Current engine version

`engine-v16` (established Session 076 — the trim-and-restart of Selvedge).

The seventy-five-session run that produced engine-v1 through engine-v15 is preserved at `archive/pre-restart/` and in git history. `engine-v16` is the minimal viable engine from which session 077 deliberates the next-generation design (multi-agent + database-backed substrate per `specifications/constraints.md`).

## Engine-definition file set

| File | Role |
|------|------|
| `PROMPT.md` | Dispatcher: determines mode and loads the executable prompt. |
| `prompts/development.md` | Executable prompt for self-development applications. |
| `prompts/application.md` | Executable prompt template for external-problem applications. |
| `specifications/methodology.md` | Kernel: what the engine does. Identity, the nine activities, when to convene multiple agents, when to review at close, validation senses, preservation, engine-feedback pathway, self-hosting. |
| `specifications/constraints.md` | What 75 sessions taught us about LLM agents. Brief for the successor design. |
| `specifications/workspace.md` | File classes, session structure, decisions, specifications discipline. |
| `specifications/engine-manifest.md` | This file. |
| `tools/validate.sh` | Minimal structural validator. |

## What is not part of the engine

- `MODE.md` — workspace-identity (each workspace writes its own).
- `CLAUDE.md` — harness instructions (per-workspace).
- `provenance/` — session records.
- `applications/` — application briefs and artefacts.
- `engine-feedback/` — operator-mediated observations.
- `open-issues/` — workspace-scope issue tracker.
- `archive/` — superseded versions and retired files.
- `tools/archive/` — substrate tools retired in the trim (retrieval, digest), kept for reference until the successor design lands.

## Versioning

The engine version (`engine-v16`, `engine-v17`, ...) increments when any file in the active set above changes substantively. Typo corrections and formatting do not bump the version. Engine-version increments are recorded in the session's `02-decisions.md`.

## Loading the engine in a fresh workspace

To initialise a new external-problem workspace:

1. Copy the engine-definition files above into a fresh directory, preserving paths.
2. Create `MODE.md` declaring `mode: external-problem`, with a short `workspace_id` and `engine_version_at_creation: engine-v16`.
3. Create `applications/001-<slug>/brief.md` with the problem statement, constraints, stakeholders, success condition, and initial state. The brief is the primary input to every session's Read.
4. Create `provenance/`, `engine-feedback/`, and `open-issues/` as empty directories (they are populated as the application runs).
5. Run session 001 against the loaded engine. The dispatcher (`PROMPT.md`) selects `prompts/application.md` based on `MODE.md`.

The successor design (sessions 077–078) is expected to introduce a database substrate that changes initialisation. The recipe above is the recipe for `engine-v16`.

## Engine-version history

The seventy-five-session history of `engine-v1` through `engine-v15` is preserved at `archive/pre-restart/engine-history.md` (created at the same close as this manifest) and in git log. The trim-and-restart at session 076 is a discontinuity by design: the prior engine accumulated to ~3000 lines of active specification that no longer fit a single agent's working memory at session-open, which `specifications/constraints.md` documents as the structural failure mode of the prior arrangement. `engine-v16` resets the surface; sessions 077 and 078 will design what the next-generation engine looks like.
