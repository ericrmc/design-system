---
session: 206
title: test-infra-tmp-db-isolation-ship — forward-reference-dispositions
generated_by: selvedge export --session
---

# Forward-reference dispositions

## FR-S205-9

- **Originating session.** S205 (`next_session_should` state-item seq 9).
- **Original ask.** Open coding session shipping OI-S205-1 refactor: convert clean_substrate + 19 test files to SELVEDGE_DB_PATH per-session tmp DB; mirror test_clone_substrate isolated fixture; seed trigger-backstop objects.
- **Resolved.** addressed by DV-S206-1 (per-test ephemeral SELVEDGE_DB_PATH refactor of conftest + 18 test files)
- **Resolved-at.** 2026-05-05T12:10:29.645Z

## FR-S205-12

- **Originating session.** S205 (`next_session_should` state-item seq 12).
- **Original ask.** Per DV-S081-1 substrate-loss-defense binding: any OI-S205-1 ship MUST preserve the L1a init-guard refusal of init --force against carrying-sessions substrate; refactor narrows guard to tmp-DB scope not weakens it.
- **Resolved.** addressed by DV-S206-1 (refactor narrows L1a init-guard to per-test tmp DB scope; primary-substrate sha256 unchanged across 465 pytest run)
- **Resolved-at.** 2026-05-05T12:10:31.893Z
