---
session: 206
title: test-infra-tmp-db-isolation-ship — engine-feedback
generated_by: selvedge export --session
---

# Engine feedback

## EF-S206-1

- **flag.** observation
- **disposition.** (none)

_Harvested from peer substrate `selvedge-self-development` (peer feedback_id 1, alias `EF-S181-1`, external session S181)._

**peer-import-1** harvest-ef import coverage atom one.

## EF-S206-2

- **flag.** blocker
- **disposition.** (none)

_Harvested from peer substrate `selvedge-self-development` (peer feedback_id 2, alias `EF-S181-2`, external session S181)._

**peer-import-2** harvest-ef import coverage atom two.

## EF-S206-3

- **flag.** observation
- **disposition.** (none)

**codex-shape-consult: S206 OI-S205-1 ship (FR-S205-9 substantive coding session)** — non-Anthropic-family read on shape pre-session-open: (Q1) per-test tmp DB at v1 correctness over speed; (Q2) explicit isolated_substrate API recommended (deferred to v2 per AR-S206-1); (Q3) seed via meta session-open path A; (Q4) staged commits within one DV; (Q5) keep in-tree no selvedge.testing module; (Q6) hard guard against SELVEDGE_DB_PATH resolving to primary. All 6 stances integrated into DV-S206-1 (R-1.1 Q1, R-1.2 Q2, R-1.3 Q3, R-1.4 Q5).

## EF-S206-4

- **flag.** observation
- **disposition.** (none)

**success-signal:** S206 ships OI-S205-1 closure by-mechanism via DV-S206-1 + conftest rewrite + 18 test files migrated + selvedge/monitor_external.py db_path() change + per-test ephemeral SELVEDGE_DB_PATH isolation; pytest 465 ok unchanged; primary substrate sha256 unchanged across run (session-scoped leakage guard satisfied); reviewer iter-1 clean; substantive coding session 7-chain-walks emitted; engine-v59 unchanged (no migration).

## EF-S206-5

- **flag.** observation
- **disposition.** (none)

**audit-step:** 5 load-bearing interpretive choices.

1. clean_substrate fixture name retained as compat alias rather than renamed to isolated_substrate per codex Q2: lifted-to AR-S206-1 (api-rename-deferral; reversible in v2 if calibration EFs surface caller-confusion).

2. Skip 3-perspective formal deliberation under bare-prompt auto-proceed; codex shape-consult substituted as cross-family input per §1.5: lifted-to AR-S206-2 (codex 6-question consult ratified all design choices with named edits before session-open).

3. Per-test vs per-session tmp DB at v1 (correctness over speed): accepted-implicit covered by sealed DV-S206-1 R-1.1 alternative + codex Q1 consult EF-S206-3.

4. selvedge/monitor_external.py production-code change in test-isolation refactor: accepted-implicit covered by sealed DV-S206-1 effect (uniform respect-SELVEDGE_DB_PATH invariant rather than test-only override).

5. _run_external_cli drops SELVEDGE_DB_PATH only when peer workspace != self workspace: accepted-implicit micro-decision per exclusion list (preserves harvest-ef writes-to-self semantics; alternative would leak peer subprocess to self tmp DB).

## EF-S206-6

- **flag.** observation
- **disposition.** (none)

**scoping-pass: 2** — patterns considered: schema-adjacency, caller-implications, migration-implications. Lifts: AR-S206-1 (api-rename-deferral) + AR-S206-2 (codex-substitute-for-deliberation). schema-adjacency: no schema migration this session; existing text_atoms + objects + sessions tables sufficient for tmp-DB seed. caller-implications: future code calling selvedge.paths.db_path() will inherit SELVEDGE_DB_PATH override behaviour now that monitor_external.py joined the convention; remaining hardcoded workspace-primary callers (none surveyed remain in production code per reviewer iter-1) would be calibration-EF candidates. migration-implications: no migration; conftest rewrite is per-test fixture replacement only.
