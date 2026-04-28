---
session: 101
title: orient-fr-rot-flag — assessment
engine_version_at_open: engine-v29
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

Engine-v29 stable; queue clean; operator chose to build orient --fr-rot per FR-S100-6/EF-S100-1, with multi-agent deliberation.

## Agenda

1. Scope what FR-rot detects: cited-issue resolved/absent only, or broader (engine-version superseded, spec-version inactive, age threshold).
2. Decide detection mechanism: regex citation-extraction at orient time, structured cites_issue link at submit time, or hybrid.
3. Decide surface: --fr-rot CLI flag emitting a separate section, inline annotation on every FR, or new orient subcommand.
4. Convene perspectives across at least two model families before deciding.
5. Implement, exercise the reviewer subagent loop, export and close.
6. Record an open issue for renaming objects.citable_alias to alias (operator-surfaced mid-session, out-of-scope here).
