---
session: 087
title: redecompose-v2-specs — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Land migration 008 widening T-06 to admit body_canonical_in_substrate flips on closed-session spec_version rows; bump engine v20 to v21.

**Kind:** schema_migration.  **Outcome:** adopt migration `008-widen-t06-for-canonical-flag`.

**Why.**

- (prior_decision) S086 substrate-invariant audit registered the three v2 rows as having body_canonical_in_substrate=0 and zero clauses, tracking via OI-085-001. [DV-S086-1]
- (review_finding) OI-085-001 mandated flipping the flag after re-decomposition; the existing T-06 trigger refused because rows belong to closed sessions S084 and S085.
- (operator_directive) Operator selected direct-SQL flip path; when T-06 blocked, escalated to a substrate migration widening the trigger; deferred open_issues table to a focused future session.

**Effects.**

- adds_migration 008-widen-t06-for-canonical-flag.sql
- modifies T-06 trigger widened to admit body_canonical_in_substrate transitions
- bumps_engine engine-v20 to engine-v21
- supersedes SPEC-engine-manifest-v21
- closes_issue OI-085-001 redecomposition + flag-flip complete

**Rejected alternatives.**

- **R-1.1.** Add a submit spec-canonicalize CLI kind that performs the flag flip via the substrate write path.
  - (redundant_with_existing) The flag has no read-side consumer in code; adding a CLI kind for a marker that nothing reads is ceremony.
- **R-1.2.** Defer the flag flip to a follow-up open-issue, ship redecomposition only this session.
  - (preserves_legacy_path) OI-085-001 explicitly scopes the flag flip into its own resolution; deferring would leave the OI partial.
- **R-1.3.** Bundle an open_issues substrate table + submit open-issue kind into this session.
  - (too_large_for_session) open_issues schema deserves its own deliberation; bundling would inflate review surface and risk a half-baked schema.
