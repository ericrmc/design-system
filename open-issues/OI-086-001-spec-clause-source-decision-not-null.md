---
id: OI-086-001
title: spec_clause source_decision_v2_id traceability is unenforced (and unused)
surfaced-in-session: 086
priority: MEDIUM
status: open
---

# OI-086-001 — spec_clause source_decision_v2_id traceability

## What S086 found

All 272 rows in `spec_clauses` have `source_decision_v2_id IS NULL`. The traceability column was named in the S082 P-1 schema sketch (atom_id 59) as `source_decision_id fk not null`, but the substrate landed it nullable to admit legacy-imported clauses. No clause — including those that pass through the post-restart write path — populates the column. The column is documentation, not a constraint.

This breaks the substrate-only-state contract at its load-bearing point: if specs are canonical in the substrate (S084 D-2), and clauses must trace to decisions to be auditable, then a NULL source_decision_v2_id on a non-legacy clause is a silent provenance loss.

## What's needed

Two-part fix:

1. **Backfill the legacy origin.** Every clause currently sitting at NULL came from a legacy markdown import. Either (a) wire each existing spec_version to a legacy_import row that points at the markdown source, so the NULL is interpretable as "imported from <body_path> at sha <body_sha256>", or (b) introduce a sentinel decision_v2 row per import that legacy clauses cite. Option (a) is cleaner because legacy_imports already carries the shape; option (b) inflates decisions_v2 with non-deliberation rows.

2. **Enforce going forward.** A trigger or partial CHECK that refuses `INSERT INTO spec_clauses` when `source_decision_v2_id IS NULL` AND the parent `spec_version` is post-restart (e.g. session_id ≥ 1, or a new column `is_legacy_import` on spec_versions). The legacy carve-out must be explicit, not the default.

## Disposition path

Open. Block on:
1. Re-decomposition of prompt-development v2, prompt-application v2, engine-manifest v20 (OI-085-001) — those clauses must be authored against decision_v2 rows, so the constraint can be tested against real post-restart writes.
2. Migration 008 (or whichever next migration lands) introduces the sentinel-or-trigger mechanism in a single calibrated pass.

## Cross-references

- F2, F3 in `provenance/086-substrate-invariant-audit/04-review.md` (export pending close).
- DV-S086-1 — the disposition decision deferring this fix.
- atom_id 59 — the original S082 P-1 schema sketch with the NOT NULL contract.
