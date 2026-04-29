---
session: 113
title: backfill-decision-targets-supports — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Migration 021 backfills decision_effects target FKs (17 rows) and decision_supports.cited_object_id (1 row); closes OI-S110-3.

**Kind:** schema_migration.  **Outcome:** adopt migration `021-backfill-decision-targets-supports.sql`.

**Why.**

- (operator_directive) Operator prescribed proceed with OI-S110-3 per FR-S112-8 sequencing.
- (prior_decision) DV-S111-1 set the calibrated UPDATE-only migration pattern this one mirrors. [DV-S111-1]
- (engine_feedback) EF-S110-7 names the cross-session referent graph as the next direction; backfill is the prerequisite. [EF-S110-7]
- (review_finding) Reviewer iter-1 high finding adjudicated as diagnostic misread; medium finding adjudicated as out-of-scope. [RF-S113-1-111]

**Effects.**

- adds_migration 021-backfill-decision-targets-supports.sql
- modifies decision_effects target FKs backfilled on 17 historical rows (4 supersedes, 13 issue-linked)
- modifies EF-S092-3 — decision_supports.cited_object_id backfilled on 1 row (EF-S092-3)
- closes_issue OI-S110-3 — Backfill landed; residual non-resolvable rows documented in migration header.

**Rejected alternatives.**

- **R-1.1.** Add a CLI subcommand selvedge backfill-decision-targets that runs the resolver dynamically each call.
  - (inferior_tradeoff) One-shot data backfill is what migrations are for; a runtime CLI invites repeated re-resolution and adds a surface only to fix history.
- **R-1.2.** Defer until a CHECK constraint can refuse NULL target on opens_issue/supersedes effects.
  - (too_large_for_session) Tightening write-side invariants is a separate decision; OI-S110-3 is the historical backfill specifically and gates EF-S110-7 work.
