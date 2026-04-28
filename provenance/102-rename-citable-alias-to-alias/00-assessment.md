---
session: 102
title: rename-citable-alias-to-alias — assessment
engine_version_at_open: engine-v29
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S102 opens to address OI-S101-1: rename objects.citable_alias and issues.citable_alias to alias for query ergonomics; backup taken pre-session.

## Agenda

1. Confirm scope: 2 tables, ~50 cli.py callsites, T-22 trigger, ~5 test callsites, payload field rename in 4 issue handlers.
2. Author migration 016: rebuild objects with alias column; rebuild issues with alias column and T-22 trigger updated.
3. Refactor cli.py: replace citable_alias with alias in all SQL, payload field reads, error messages.
4. Refactor state/tests/test_existing_kinds.py to use alias.
5. Update prompts/development.md and specifications references where citable_alias appears in active surfaces.
6. Bump engine version to v30 reflecting the schema rename.
7. Run validate.sh and tests; ensure orient still emits the alias column.
8. Record decision DV-S102-1 (rename adopted) closing OI-S101-1.
