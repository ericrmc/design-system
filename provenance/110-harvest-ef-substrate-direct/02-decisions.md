---
session: 110
title: harvest-ef-substrate-direct — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Adopt substrate-direct read for monitor-external harvest-ef with per-row import ledger

**Kind:** substantive.  **Outcome:** adopt engine_version `harvest-ef-substrate-direct-engine-v33`.

**Why.**

- (deliberation) Both P-1 and P-2 independently chose Option 1 substrate-direct read citing engine-v20 substrate-only-writes principle. [P-10-P-1]
- (deliberation) P-2 cross-family perspective converged on narrow column contract over schema-version gating and per-row idempotency keys. [P-10-P-2]
- (spec_clause) Engine-v20 made substrate the only writable surface; round-tripping through markdown reverses that. [SPEC-engine-manifest-v32]
- (engine_feedback) Disaster-recovery peer adopted substrate authoring; harvest-ef returned no engine-feedback dir, blocking EF-S005-1 transport.

**Effects.**

- modifies _me_harvest_ef reads peer engine_feedback via file:?mode=ro&immutable=0 with busy_timeout+query_only
- adds_migration migration 019: harvested_engine_feedback ledger table, UNIQUE (peer_workspace_id, peer_feedback_id)
- modifies harvest-ef contract: capability-based peer schema detection over migration-version gating
- bumps_engine engine-v32 to engine-v33

**Rejected alternatives.**

- **R-1.1.** Option 2: add export --engine-feedback flag materialising EF-*.md files for existing harvest-ef
  - (violates_gate) Re-introduces prose-as-transport that engine-v20 substrate-only-writes principle eliminated.
  - (inferior_tradeoff) Two-command operator workflow plus stale-file cleanup debt in peer workspace.
- **R-1.2.** Option 1 with --since-session as the dedup mechanism (no import ledger)
  - (inferior_tradeoff) Coarse-grained; partial-harvest re-run loses precision; per-row keys admit surgical re-harvest.
- **R-1.3.** Option 1 with body_md provenance marker for migration-free dedup
  - (inferior_tradeoff) Parse-prose-as-state for control plane is the pattern engine-v20 eliminated for data plane; ledger is cheap and structurally honest.
- **R-1.4.** Schema-version gating against peer schema_migrations table
  - (inferior_tradeoff) Brittle to migration renumbering; capability detection matches canonical alias-not-version pattern.
- **R-1.5.** Python retry-with-backoff loop for locked peer DB
  - (inferior_tradeoff) PRAGMA busy_timeout covers transient contention natively; no Python sleep loop needed.
