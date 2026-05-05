---
session: 206
title: test-infra-tmp-db-isolation-ship — decisions
generated_by: selvedge export
---

# Decisions

## D-1. S206 ships per-test ephemeral SELVEDGE_DB_PATH tmp-DB isolation closing OI-S205-1 by-mechanism via conftest refactor.

**Kind:** substantive.  **Outcome:** adopt process_rule `test-infra-tmp-db-isolation`.

**Why.**

- (engine_feedback) EF-S205-1 calibration retrospectively named the S204 pytest-touches-PRIMARY-DB failure mode and OI-S205-1 was opened as the MEDIUM remedy. [EF-S205-1]
- (prior_decision) DV-S081-1 substrate-loss-defense binds the L1a init-guard against carrying-sessions substrate; refactor narrows guard to per-test tmp DB scope. [DV-S081-1]
- (prior_decision) DV-S186-1 L2b subagent tempdir-clone established SELVEDGE_DB_PATH override + tmp_path isolated fixture as the proven precedent in test_clone_substrate. [DV-S186-1]
- (engine_feedback) AR-S205-3 named SELVEDGE_DB_PATH as the existing substrate-canonical lever already used by 6 test files; DV reuses that lever. [AR-S205-3]

**Effects.**

- modifies state/tests/conftest.py per-test autouse db_path + sha256 leakage guard
- modifies 18 test files migrated from PRIMARY_DB to db_path fixture
- modifies selvedge/monitor_external.py harvest-ef respects SELVEDGE_DB_PATH override
- modifies test_monitor_external _run_external_cli drops env for peer subprocess
- closes_issue OI-S205-1 — close OI-S205-1 pytest tmp-DB refactor

**Rejected alternatives.**

- **R-1.1.** Per-session shared tmp DB inited once with per-test reset; faster but couples test ordering and breaks trigger refusal probes that mutate substrate state.
  - (inferior_tradeoff) codex Q1 + arc invariants prefer correctness via per-test isolation; speed delta ~2 minutes; trigger probes invite share-DB order coupling.
- **R-1.2.** Keep PRIMARY_DB as a redirected name resolving from SELVEDGE_DB_PATH at access time so test files do not need editing; AR-S205-4 19-file scope avoided.
  - (preserves_legacy_path) PRIMARY_DB name encodes dangerous workspace-primary semantic; redirect would obscure intent and re-introduce S204 failure mode if env override breaks per codex Q2.
- **R-1.3.** Synthetic INSERT into objects table to seed non-assumption rows for T-42/T-43 trigger backstop tests; bypass the engine path.
  - (breaks_invariant) codex Q3 named (a) opening a meta session via clean_substrate as the right path: raw INSERT bypasses invariants the trigger tests trust.
- **R-1.4.** Ship a reusable selvedge.testing helper module exposing the isolated_db fixture for cross-application use at v1.
  - (too_large_for_session) codex Q5 + AR-S202-1 argue against premature cross-app abstraction at v1; ship in-tree and graduate when external apps demand.
- **R-1.5.** Defer to a future arc with a graduation watch-FR per DV-S190-2 substrate-receipt graduation-discipline pattern.
  - (violates_gate) EF-S196-2 bounded-scope precludes graduation-discipline as deferral basis for engine primitives evidenced by completed arcs; S204 IS the evidence.
