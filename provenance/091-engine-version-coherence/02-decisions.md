---
session: 091
title: engine-version-coherence — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Engine v24 to v25: workspace_metadata.current_engine_version coherence (atomic propagation in _submit_spec_version)

**Kind:** substantive.  **Outcome:** adopt engine_version `engine-v25`.

**Why.**

- (constraint) Two sources of truth for engine version (spec_versions + workspace_metadata) drifted across S087-S090; S091 opened at engine-v23 from the stale metadata while substrate truth was v24.
- (constraint) Migration 007 seeded the metadata at engine-v20; bumps were operator-policed and silently fell off in four consecutive sessions. [SPEC-engine-manifest-v24]
- (engine_feedback) Handler change validated end-to-end by this v24 to v25 bump itself: spec_versions row is v25 active, workspace_metadata says engine-v25, propagation was atomic. [SPEC-engine-manifest-v25]
- (engine_feedback) OI-S090-4 reorder fix exercised again on this bump; T-03 not tripped, no direct SQL workaround needed.

**Effects.**

- bumps_engine engine-v24 to engine-v25
- adds_migration 011-engine-version-coherence.sql
- closes_issue OI-086-002
- supersedes engine-manifest v24 to v25

**Rejected alternatives.**

- **R-01.** Make workspace_metadata.current_engine_version a derived view of spec_versions instead of a stored row
  - (inferior_tradeoff) Requires DROP+RECREATE of workspace_metadata or a substantial rewrite; the stored-row model is read everywhere; structural propagation in the writer is a much smaller surface change.
- **R-02.** Add a substrate trigger refusing engine-manifest spec_version inserts that do not also UPDATE workspace_metadata in the same transaction
  - (inferior_tradeoff) Triggers cannot inspect handler-level transaction grouping; would need to be a multi-statement assertion that is awkward in SQLite. Application-layer enforcement in the single writer is sufficient.
- **R-03.** Continue operator-policed metadata updates per session
  - (no_feedback_loop) Already failed across S087-S090; four consecutive operator-policed bumps drifted. Discipline does not survive context pressure.
