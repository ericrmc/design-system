---
title: Engine Manifest
version: 19
status: active
created: 2026-04-27
updated-by-session: 083
supersedes: engine-manifest v18 (engine-v18); per 083 D-2 (operator-directed coding review loop in methodology v3, with no-deliberation exception at 083 D-1); v18 per 082 D-1 (substrate migration 002 + selvedge migrate runner); enumeration correction at v17 per 081 D-1; v17 itself per 078 D-7 + D-11
---

# Engine Manifest

This file enumerates the loadable Selvedge engine at the current commit. The engine is the file set listed below plus the substrate; loading the engine means having these files available, the substrate initialised, and the `selvedge` CLI on PATH.

## Current engine version

`engine-v19` (established Session 083 — methodology v3 introduces the coding review loop per operator direction).

`engine-v19` adds a structural reviewer mechanism for code-producing sessions: a reviewer subagent, distinct from the implementer, audits any change to executable code (Python under `selvedge/`, SQL under `state/migrations/`, shell under `bin/` or `tools/`), and the loop continues until the reviewer reports no medium-or-higher findings remain. The pre-existing engine-definition close review is retained as a single-pass mechanism. Both are documented in `specifications/methodology.md` §When to review and wired into `prompts/development.md` and `prompts/application.md`.

The change is operator-directed and is recorded as a deliberate exception to the 078 D-5 release gate. Specifically, the gate's clause forbidding methodology-expanding self-development sessions from modifying active spec content between Session 079 and the close of the first external-problem trial of 30 sessions is overridden for this revision by operator directive (recorded in S083 D-2 / substrate D-S004-2 R-1.3, with the reason). Per `specifications/methodology.md` §When to convene multiple agents (when multi-agent deliberation is otherwise triggered but not performed because the decision is operator-directed, the reason is recorded), no cross-family deliberation was convened on the loop's design details; the procedural exception itself is recorded at S083 D-1 / substrate D-S004-1, and a future cross-family review of the loop's design details is deferred until the mechanism has been exercised against real code-producing sessions.

`engine-v19` remains **provisional** in the same sense `engine-v18` was: no further methodology-expanding self-development sessions modify active spec content between 083 and the close of the first external-problem trial of 30 sessions, except where operator-directed. Bug-fix and validator-tightening sessions remain admitted.

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
| `state/migrations/001-initial.sql` | Schema for sessions, objects, decisions, decision_alternatives, spec_versions, perspectives, deliberations, synthesis_points, refs, commitments, engine_feedback, work_items, role_write_capabilities, read_log, subtraction_log, schema_migrations, agent_runs (17 tables; 16 per 078 D-10 + synthesis_points calibrated breach per 081 D-1 with cause: T-14 enforcement has no other structural home; `objects` is the citable_alias indirection table powering T-01). Encodes refusals T-01..T-16 (per 078 D-3). |
| `state/migrations/002-tighten-deliberation-immutability.sql` | Closes OI-080-001 (per 082 D-1 + D-2): adds T-06 trigger pair on `deliberations` UPDATE/DELETE for closed sessions; tightens T-13 to refuse any change-in-place to a non-NULL `sealed_at`. Activated by the `selvedge migrate` runner shipped in the same session. |
| `selvedge/` (Python package) | The CLI implementation. Includes the `migrate` subcommand (engine-v18+) with `--status`, `--dry-run`, `--apply`; T-15 pre-check; sha256 drift detection; 078 D-8 tier-1 rollback via `.pre-migrate-backup`. |
| `bin/selvedge` | Shell shim. |
| `state/selvedge.sqlite` | Per-workspace; not under VCS. Created by `selvedge init`, which now chains `selvedge migrate` so a fresh init applies all known migrations (engine-v18+). |

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

The engine version increments when any file in the active set above changes substantively, including a substrate migration. Typo corrections and formatting do not bump. Engine-version increments are recorded in the session's `02-decisions.md`. The 078 D-5 release gate constrains *what kind* of change can ship; it does not exempt qualifying changes from the bump rule. Bug-fix and validator-tightening sessions admitted under the gate (which add migrations like 002) bump the engine version normally.

## Engine-version history

`engine-v1` through `engine-v15` ran for 75 self-development sessions and are preserved in git history. `engine-v16` (session 076) was the trim-restart that reduced the active surface to ~430 non-blank lines. `engine-v17` (session 079) applies the 078 D-7 cut, lands the SQLite substrate, and introduces the `selvedge` CLI as the only writer of structured state. `engine-v18` (session 082) adds migration 002 (closes OI-080-001 by adding T-06 trigger pair on `deliberations` UPDATE/DELETE and tightening T-13 to refuse any change-in-place to a non-NULL `sealed_at`) and ships the `selvedge migrate` runner that activates T-15 enforcement (the runner deferral was named at S079 close per `engine-feedback/inbox/EF-079-002-T15-deferred.md`). `engine-v19` (session 083) introduces the coding review loop in methodology v3 and updates both prompts to invoke it.
