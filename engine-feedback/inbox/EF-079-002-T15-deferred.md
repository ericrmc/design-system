---
id: EF-079-002
title: T-15 (no DROP COLUMN/DROP TABLE) deferred until selvedge migrate exists
session: 079
flag: blocker
status: open
triage-target: 080+ first additive migration
related-decisions: 079:D-5
---

# EF-079-002 — T-15 enforcement deferred

## Observation

T-15 (per 078 D-3) refuses `DROP COLUMN` and `DROP TABLE` operations in migrations, admitting only `ADD` operations. The mechanism is "Pre-migration check in `selvedge migrate`."

079 does not implement `selvedge migrate`. Migration 001 is run by `selvedge init` directly via `executescript()`. There is no migration-runner code path in which a T-15 pre-check would fire, because migration 001 itself is purely additive and there is no migration 002 to check.

## Implication

T-15 is currently enforced by **review of the source SQL** (a future migration's `.sql` file is human-readable; a destructive operation is grep-able). The substrate does not refuse a destructive migration applied via the same `executescript()` path that would land an additive one.

This is a strictly weaker position than 078 D-3 specifies, but the threat model is bounded: the only path to a destructive migration in 079's regime is a human-authored SQL file checked into the repo and then run by hand. There is no automated migration runner to bypass.

## Triage

080+'s first additive migration (e.g., adding a column for the first LLM-writer role) triggers building `selvedge migrate`:
- Subcommand `selvedge migrate --dry-run`: parse the migration SQL; refuse on `DROP COLUMN`, `DROP TABLE`, `ALTER TABLE ... DROP`, etc.
- `selvedge migrate --apply`: same pre-check, then runs in-transaction.
- D-8's two-tier rollback: pre-close failure → SQLite rollback + restore from `.backup`; post-close failure → forward-only corrective migration.

T-15 becomes active enforcement at the moment the runner ships, which is the same moment the runner has work to do. Cost is paid when value is paid.
