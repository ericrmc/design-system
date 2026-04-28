---
session: 108
title: monitor-external — assessment
engine_version_at_open: engine-v31
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S107 shipped engine-v31 bootstrap rebuild and archived v7 disaster-response. monitor-external CLI is the last piece needed before S109 bootstrap execution.

## Agenda

1. Implement bin/selvedge monitor-external subcommand group (status, next-input, harvest-ef) per DV-S106-3 / OI-S106-2.
2. Generic across external workspaces; do not specialise for disaster-response arc.
3. status reads target external SQLite read-only and prints metadata, sessions tail, OI counts, EF outbox files, derived arc-phase heuristic.
4. next-input reads arc-plan + latest close-record next_session_should + optional assumption-ledger artefact and emits JSON draft for operator review.
5. harvest-ef reads external engine-feedback/EF-*.md, copies into self-dev engine_feedback rows via existing _submit_engine_feedback handler.
6. Add pytest coverage for the three subcommands and refusal paths.
7. Run T-30 review loop against the diff before close.
8. Dispose FR-S106-11 and FR-S107-9 on session close.
