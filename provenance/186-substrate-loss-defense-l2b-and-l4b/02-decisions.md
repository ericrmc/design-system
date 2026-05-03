---
session: 186
title: substrate-loss-defense-l2b-and-l4b — decisions
generated_by: selvedge export
---

# Decisions

## D-1. S186 ships L2b subagent tempdir-clone via bin/selvedge clone-substrate plus prompt-development v2 §4 clause; closes OI-S081-2 per FR-S081-12.

**Kind:** substantive.  **Outcome:** adopt process_rule `l2b-subagent-tempdir-clone`.

**Why.**

- (prior_decision) DV-S081-1 sealed substrate-loss-defense-v1 with L2b subagent tempdir-clone via SQLite backup API as a load-bearing layer; this ship slices that layer. [DV-S081-1]
- (engine_feedback) EF-S186-1 records gpt-5.5 codex-shape-consult endorsing single-arc L2b-then-L4B with prompt-level env-var discipline acceptable plus tests proving clone writes do not reach primary. [EF-S186-1]
- (spec_clause) SPEC-prompt-development-v2 documents the clone-substrate workflow alongside the existing do-not-mutate-substrate boilerplate as a substrate-dispatch upgrade. [SPEC-prompt-development-v2]

**Effects.**

- creates selvedge/clone_cmd.py + test_clone_substrate.py
- creates SPEC-prompt-development-v2 — SPEC-prompt-development-v2 §4 L2b clause
- supersedes SPEC-prompt-development-v1 — SPEC-prompt-development-v1 -> v2
- closes_issue OI-S081-2 — OI-S081-2 closed by-mechanism

**Rejected alternatives.**

- **R-1.1.** Ship the L2b workflow as prompt-only discipline without a CLI command, requiring the orchestrator to manually invoke sqlite3.Connection.backup() before each subagent dispatch.
  - (inferior_tradeoff) Prose-only reproduces the DV-S176-1 failure mode: when discipline depends on the agent reaching for a tool the substrate could dispatch, ship the substrate dispatch.
- **R-1.2.** Substrate-side enforcement of SELVEDGE_DB_PATH=<clone> at subagent-dispatch time via harness shell-shim or prompt linter.
  - (too_large_for_session) Harness-side enforcement is the engine-v52 graduation path per the existing prompt-development clause; ship orchestrator-side surface first per phased-rollout.
- **R-1.3.** Make SELVEDGE_READONLY env-var a hard substrate refusal so subagent writes are blocked at the connection layer regardless of clone path.
  - (violates_gate) DV-S081-1 explicitly preserved SELVEDGE_READONLY as advisory-only; promoting to hard refusal would break orchestrator writes that share the code path.

## D-2. S186 ships L4B extractor at tools/extract-legacy-substrate.py producing provenance/legacy-substrate-summary.md inventory; closes OI-S081-5 per FR-S081-12.

**Kind:** substantive.  **Outcome:** adopt process_rule `l4b-legacy-substrate-extractor`.

**Why.**

- (prior_decision) DV-S081-1 sealed L4B as the inventory-only (not rebuild) layer of substrate-loss-defense-v1 against pre-S180 backup files. [DV-S081-1]
- (engine_feedback) EF-S186-1 records gpt-5.5 endorsement of provenance/legacy-substrate-summary.md as the right home for the inventory output (derived provenance evidence, not transient tool output). [EF-S186-1]

**Effects.**

- creates tools/extract-legacy-substrate.py one-shot inventory tool
- creates provenance/legacy-substrate-summary.md output artefact
- closes_issue OI-S081-5 — OI-S081-5 closed by-mechanism

**Rejected alternatives.**

- **R-1.1.** Skip the extractor entirely since no pre-S180 binary backups survive; rely on git history + grep over provenance/ when future readers need legacy data.
  - (no_feedback_loop) Without a static summary the recovery posture stays implicit and a future reader has to rediscover the no-backup-files fact each time; the inventory makes the loss explicit.
- **R-1.2.** Implement the L4B extractor as a rebuild tool that re-parses markdown back into typed substrate rows (the original FR-S080-9 framing).
  - (too_large_for_session) Rebuild requires foreign-key reconstruction across decisions/specs/issues/EFs; that is OI-S180-1 work and would not fit this single-arc session per codex-shape-consult Q1.
- **R-1.3.** Land the inventory output under tools/output/ or a fresh archive/ subtree rather than under provenance/.
  - (inferior_tradeoff) provenance/ is the workspace canonical home for derived per-session evidence; codex Q3 confirms tools/output/ would treat the summary as transient when it is durable inventory.
