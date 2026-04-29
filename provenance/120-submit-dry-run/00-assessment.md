---
session: 120
title: submit-dry-run — assessment
engine_version_at_open: engine-v34
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S119 modularised cli.py into selvedge/submit/* leaving the write-path surface scoped enough to add a dry-run.

## Agenda

1. Land FR-S119-10/FR-S118-10: implement --dry-run for bin/selvedge submit so handlers can be smoke-tested without polluting substrate provenance.
2. Design: use BEGIN IMMEDIATE then ROLLBACK in write_tx; surface dry_run flag through cmd_submit; suppress the only FS side-effect (_submit_spec_version body write) under dry-run.
3. Verify triggers and constraint refusals still propagate correctly when the transaction is rolled back at the end.
4. Run the coding review loop with a distinct reviewer subagent until clean.
