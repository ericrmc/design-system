---
session: 111
title: fix-stale-constraints-body-path — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Fix stale body_path on superseded constraints v1 via one-time calibrated backfill mirroring migration 008 pattern.

**Kind:** schema_migration.  **Outcome:** adopt migration `020-fix-stale-constraints-body-path`.

**Why.**

- (engine_feedback) OI-S110-2 names a real broken pointer; sha256 b6325... matches archive/specifications/constraints-v1.md so only the path is stale.
- (prior_decision) Migration 008 established the drop-trigger / surgical UPDATE / recreate-trigger pattern for closed-session row corrections, identical structure applies here.
- (constraint) T-06 refuses direct UPDATE on closed-session spec_versions rows so calibrated backfill is the only substrate-blessed correction path.

**Effects.**

- adds_migration state/migrations/020-fix-stale-constraints-body-path.sql
- modifies spec_versions row spec_id=constraints version=1 body_path -> archive/specifications/constraints-v1.md
- closes_issue OI-S110-2 — OI-S110-2 stale body_path resolved by corrected pointer

**Rejected alternatives.**

- **R-1.1.** Widen T-06 generally to admit body_path mutation on already-superseded rows so future stale-pointer cases need no migration.
  - (too_large_for_session) Expands mutation surface for one stale pointer; per-incident calibrated backfill keeps the audit trail explicit and matches the 008 precedent.
- **R-1.2.** Leave body_path stale and document in workspace.md that subtracted specs body_path may not resolve.
  - (inferior_tradeoff) Leaves orient consumers and future readers with a broken pointer indefinitely; the sha-matched archive file already exists so correction is cheap.
- **R-1.3.** NULL the body_path on the superseded row.
  - (breaks_invariant) spec_versions.body_path is NOT NULL by schema; would require schema change for marginal value over pointing at the archive file.
