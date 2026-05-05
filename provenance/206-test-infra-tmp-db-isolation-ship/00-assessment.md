---
session: 206
title: test-infra-tmp-db-isolation-ship — assessment
engine_version_at_open: engine-v59
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S206 ships OI-S205-1 refactor: per-test ephemeral tmp DB via SELVEDGE_DB_PATH eliminating pytest mutation of primary substrate that surfaced at S204.

## Agenda

1. Refactor conftest.py: add per-test isolated_substrate fixture (db_path + env + run + conn), preserve clean_substrate as compat alias pointing at tmp DB.
2. Add SELVEDGE_DB_PATH primary-substrate leakage guard per codex shape-consult Q6.
3. Update 19 test files to use db_path fixture instead of importing PRIMARY_DB and connecting directly.
4. Seed trigger-backstop objects via meta session-open (path A per codex Q3) so T-42 and T-43 find non-assumption objects.
5. Submit DV-S206-1 substantive decision-record with precheck closing OI-S205-1 by-mechanism.
6. Run pytest until 465+ ok; verify primary substrate sha256 unchanged across run.
7. Invoke reviewer subagent against substrate clone per T-30 coding-session gate.
8. Close-time §8.5 reflection (EF + FR-S205-9/12 disposition + audit-step + scoping-pass) and close-record.
