---
id: EF-079-001
title: T-12 trigger-form not implementable; downgraded to application-layer
session: 079
flag: blocker
status: open
triage-target: 080+ deliberation introducing first non-__cli__ writer
related-decisions: 079:D-3
---

# EF-079-001 — T-12 (role write capabilities) downgraded

## Observation

Refusal T-12 in 078 D-3 specifies: *"INSERT any row WHERE `agent_runs.role` not in `role_write_capabilities` for that table — Trigger lookup."* This is not implementable as a pure SQLite trigger.

A SQLite trigger has access to OLD/NEW row values and can read other tables, but it cannot read a connection-scoped session variable (no equivalent of PostgreSQL `SET LOCAL`). To enforce T-12 as a trigger, the substrate would need either:

1. A `current_role` table the writer stamps before each INSERT, with the trigger looking up the most recent stamp. This requires two writes per submit (set role; write row) and either application-level discipline that the stamp lifecycle is correct, or a follow-up sweeper that purges stale stamps.
2. A loadable SQLite extension exposing a `selvedge_current_role()` function bound to the connection. Adds a build-step requirement and a non-stdlib dependency.

Neither pays in 079, where the only writer is `__cli__` invoked by the human operator. The `role_write_capabilities` table ships seeded with `__cli__` rows; `selvedge submit` enforces the lookup in `_check_role_capability` (Python).

## Implication

Until a second writer-role exists, T-12 is application-layer. The moment a second writer (e.g., a `specifier` LLM agent process invoking `selvedge submit`) is introduced, application-layer enforcement is still load-bearing because the CLI is the choke point — but a hostile or buggy bypass (direct `sqlite3` connection by an agent process) would not be refused.

## Triage

080+ first session that introduces a non-`__cli__` writer must either:
- Adopt the `current_role` two-write pattern at the same time (small, mechanical — set the role, then write).
- Decide that all writes go through the `selvedge` CLI subprocess and direct DB connections from agents are forbidden by convention (the simpler position; relies on agent-process implementation discipline rather than substrate refusal).

Either choice closes this EF. The decision belongs in 080+.
