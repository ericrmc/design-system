---
session: 110
title: harvest-ef-substrate-direct — assessment
engine_version_at_open: engine-v32
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S110 opens to fix monitor-external harvest-ef which broke when external workspaces moved engine_feedback authoring to substrate-only per engine-v26.

## Agenda

1. Convene cross-family perspective on inter-workspace substrate read pattern (idempotency, schema-drift, RO-URI safety).
2. Decide between substrate-direct read (option 1) and md-export round-trip (option 2).
3. Implement chosen path in _me_harvest_ef; preserve existing write-target guards.
4. Reviewer loop until clean of medium+ findings; submit review-pass rows per T-30.
5. Run harvest-ef against disaster-recovery to land 8 rows including EF-S005-7.
6. Open OIs for S109 followups: superseded-spec discoverability gap, stale body_path bug, decision_effects/supports backfill.
7. Close-record with forward references: triage harvested EF-S005-7, gate on backfill OI before design work.
