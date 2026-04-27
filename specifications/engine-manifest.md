---
title: Engine Manifest
version: 17
status: active
created: 2026-04-27
updated-by-session: 079
supersedes: engine-manifest v16 (engine-v16); per 078 D-7 + D-11
---

# Engine Manifest

This file enumerates the loadable Selvedge engine at the current commit. The engine is the file set listed below plus the substrate; loading the engine means having these files available, the substrate initialised, and the `selvedge` CLI on PATH.

## Current engine version

`engine-v17` (established Session 079 — the substrate vertical-slice landing).

`engine-v17` is the first engine version with a database-backed substrate (`state/selvedge.sqlite`, `state/migrations/001-initial.sql`, the `selvedge` CLI). The engine-v16 → engine-v17 transition applies the 078 D-7 cut to the active spec surface and adds the substrate; per 078 D-12, engine-v17 is smaller than engine-v16 by active-spec line count and adds enforcement (not ceremony) at the substrate layer.

`engine-v17` is **provisional** per 078 D-5: no methodology-expanding self-development sessions modify engine-v17 active spec content between 079 and the close of the first external-problem trial of 30 sessions. Bug-fix and validator-tightening sessions are admitted; new active-spec content is not.

## Engine-definition file set

Active spec (read at session open):

| File | Role |
|------|------|
| `PROMPT.md` | Dispatcher: determines mode and loads the executable prompt. |
| `prompts/development.md` | Executable prompt for self-development applications. |
| `prompts/application.md` | Executable prompt template for external-problem applications. |
| `specifications/methodology.md` | Kernel: what the engine does. The nine activities, when to convene multiple agents, validation senses, preservation, engine-feedback pathway, self-hosting. |
| `specifications/constraints.md` | What 75 sessions taught us about LLM agents. Brief for the successor design. |
| `specifications/workspace.md` | File classes, session structure, decisions, specifications discipline. |
| `specifications/engine-manifest.md` | This file. |
| `tools/validate.sh` | Wrapper that calls `selvedge validate --precommit`. |

Substrate (engine-definition; not read as prose):

| Path | Role |
|------|------|
| `state/migrations/001-initial.sql` | Schema for sessions, decisions, alternatives, refs, perspectives, deliberations, spec_versions, commitments, engine_feedback, work_items, role_write_capabilities, read_log, subtraction_log, schema_migrations, agent_runs (≤16 tables per 078 D-10). Encodes refusals T-01..T-16 (per 078 D-3). |
| `selvedge/` (Python package) | The CLI implementation. |
| `bin/selvedge` | Shell shim. |
| `state/selvedge.sqlite` | Per-workspace; not under VCS. Created by `selvedge init`. |

## What is not part of the engine

- `MODE.md` — workspace-identity (each workspace writes its own).
- `CLAUDE.md` — harness instructions (per-workspace).
- `provenance/` — session records.
- `applications/` — application briefs and artefacts.
- `engine-feedback/` — operator-mediated observations.
- `open-issues/` — workspace-scope issue tracker.
- `archive/` — superseded versions and retired files.
- `state/selvedge.sqlite` — workspace state, not engine-definition.

## Versioning

The engine version increments when any file in the active set above changes substantively, including a substrate migration. Typo corrections and formatting do not bump. Engine-version increments are recorded in the session's `02-decisions.md`. Per 078 D-5 release gate, engine-v17 → engine-v18 is not anticipated until after the first external-problem trial completes.

## Engine-version history

`engine-v1` through `engine-v15` ran for 75 self-development sessions and are preserved in git history. `engine-v16` (session 076) was the trim-restart that reduced the active surface to ~430 non-blank lines. `engine-v17` (session 079) applies the 078 D-7 cut, lands the SQLite substrate, and introduces the `selvedge` CLI as the only writer of structured state.
