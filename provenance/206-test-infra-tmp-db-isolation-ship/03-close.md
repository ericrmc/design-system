---
session: 206
title: test-infra-tmp-db-isolation-ship — close
engine_version_at_close: engine-v59
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S206 ships per-test ephemeral SELVEDGE_DB_PATH tmp-DB isolation closing OI-S205-1 by-mechanism; conftest rewrite + 18 test files + monitor_external.py db_path() change.

## Engine version

- engine-v59 unchanged (no migration; pure refactor).
## What was done

- conftest.py rewritten: per-test autouse db_path fixture sets SELVEDGE_DB_PATH and SELVEDGE_SNAPSHOTS_DIR; clean_substrate now uses tmp DB.
- Session-scoped sha256 leakage guard replaces _snapshot_primary copy/restore; primary substrate sha256 unchanged across pytest run is the receipt-pattern proof.
- 18 test files migrated from PRIMARY_DB to db_path fixture via AST-based bulk transform plus manual fixups for keyword-only and multi-line signatures.
- selvedge/monitor_external.py harvest-ef now resolves self_db via paths.db_path() respecting SELVEDGE_DB_PATH override; production behaviour preserved when env unset.
- test_monitor_external _run_external_cli drops SELVEDGE_DB_PATH when extra_env names non-self workspace; preserves peer-vs-self DB isolation.
- T-42 + T-43 trigger-backstop tests now seed text_atoms with atom_type=claim in fresh tmp DB rather than relying on inherited PRIMARY rows.
## State at close

- engine-v59; pytest 465 ok unchanged; primary substrate sha256 verified unchanged across run; reviewer iter-1 clean head_sha=25f2c956.
## Open issues

- Zero open issues. OI-S205-1 closed-by-mechanism via DV-S206-1 effect.
## What the next session should address

- Pick OI-S196-7 spec-only amendment (last S196 OI per FR-S204-10) OR untriaged EF triage; FR-S205-11 watch remains open as continuing recurrence monitor.
- If next session opens substantive coding work, run codex shape-consult per §1.5 + cite AR-S206-2 codex-substitute-for-deliberation precedent.
- Watch FR-S206-1: if calibration EFs surface clean_substrate name-confusion across N>=3 sessions per AR-S206-1 v2 trigger, open gate-promotion OI for isolated_substrate rename.
## Validator at close

- validate.sh expected 18 ok / 0 fail unchanged; pytest 465 ok unchanged; manifest-reconcile expected clean post-export.
