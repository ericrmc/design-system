---
session: 110
title: harvest-ef-substrate-direct — deliberation
generated_by: selvedge export
---

# Deliberation

## D-10 — Inter-workspace engine_feedback transport: substrate-direct read vs md-export round-trip

sealed_at: 2026-04-29T00:37:31.631Z

### P-1 (anthropic)

### P-2 (openai)

### Synthesis

Both perspectives independently chose Option 1 substrate-direct read. Convergence on: (1) Option 1 over md round-trip (engine-v20 substrate-only-writes principle binding); (2) narrow column contract over schema-version gating — both want feedback_id, session_id, flag, body_md, sessions.session_no, sessions.slug as the contract; (3) per-row idempotency keys over --since-session as dedup mechanism; (4) explicit structured error on locked peer DB, not silent empty result; (5) reuse existing file:?mode=ro pattern from monitor-external; (6) never write to peer. Divergence on lock handling: P-1 wants Python retry 3x with backoff before E_PEER_LOCKED; P-2 wants fail-fast with E_PEER_BUSY. Synthesis: use SQLite PRAGMA busy_timeout=1000 to handle transient WAL contention without explicit Python sleep loop; covers P-1 retry intent via SQLite native mechanism then falls through to P-2 structured error. Divergence on idempotency table: P-1 (peer_workspace_path_hash, peer_feedback_id) vs P-2 (source_workspace_id, source_kind, source_alias-or-feedback_id). P-2 wins: workspace_id is the metadata key (stable across path moves), source_kind allows generalising the import ledger beyond engine_feedback later. P-2 also caught precision error: peer feedback_id=7 alias is EF-S005-1 (per-session ordinal) not EF-S005-7 — design must key on object alias when present. Schema-drift handling synthesis: P-1 schema_migrations check vs P-2 capability-based detection. P-2 wins: capability-based is more robust to migration renumbering and matches the canonical engine pattern of resolving aliases not versions.

### Synthesis points

- **convergence C-1.** Both perspectives chose Option 1 substrate-direct read, citing engine-v20 substrate-only-writes principle.
- **convergence C-2.** Narrow column contract preferred over schema-version gating: feedback_id, session_id, flag, body_md, session_no, slug.
- **convergence C-3.** Per-row idempotency key with import ledger preferred over --since-session as dedup mechanism.
- **divergence D-1.** Lock handling: P-1 Python retry+backoff vs P-2 fail-fast. Synthesis: SQLite PRAGMA busy_timeout covers retry intent natively then E_PEER_BUSY.
- **minority M-1.** P-2 caught precision error: peer feedback_id=7 alias is EF-S005-1 not EF-S005-7. Design must key on object alias when present.
