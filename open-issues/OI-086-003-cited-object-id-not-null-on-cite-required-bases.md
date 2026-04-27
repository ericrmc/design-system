---
id: OI-086-003
title: decision_supports / alternative_rejections allow NULL cited_object_id even on cite-requiring bases
surfaced-in-session: 086
priority: MEDIUM
status: open
---

# OI-086-003 — cited_object_id NOT NULL on cite-requiring bases

## What S086 found

`decision_supports.cited_object_id` and `alternative_rejections.cited_object_id` are nullable. Across the 13 supports + 5 alternatives + 6 rejections currently in the substrate, only 2 rows carry a non-NULL `cited_object_id`. Bases that semantically require a cite — `prior_decision`, `review_finding`, `deliberation`, `spec_clause`, `engine_feedback`, `operator_override` — are landing without one, defeating the traceability promise.

The S082 P-1 schema sketch (atom_id 59) names this exactly: `alternative_rejections.cited_object_id fk not null`. The substrate landed it nullable to admit `inferior_tradeoff` and `too_large_for_session` rejections, which can be argued from session-internal reasoning without a prior-object cite. That carve-out swallowed the constraint.

## What's needed

A lookup table of `(basis, applies_to)` → `cite_required` (boolean), checked by trigger on insert. Shape:

```sql
CREATE TABLE basis_cite_requirements (
  applies_to TEXT NOT NULL CHECK (applies_to IN ('decision_support','alternative_rejection')),
  basis TEXT NOT NULL,
  cite_required INTEGER NOT NULL CHECK (cite_required IN (0,1)),
  PRIMARY KEY (applies_to, basis)
) STRICT;
```

Seed with the cite-requiring set: `prior_decision`, `review_finding`, `deliberation`, `spec_clause`, `engine_feedback` for supports; `operator_override`, `preserves_legacy_path`, `redundant_with_existing`, `breaks_invariant` for rejections. Trigger refuses an insert with `cite_required=1 AND cited_object_id IS NULL`.

## Disposition path

Open. Land alongside OI-086-001 in a single migration session — both are decision-traceability fixes. May reveal that some currently-NULL rows need backfilled cites; cost is a few text_atoms per backfill.

## Cross-references

- F5 in `provenance/086-substrate-invariant-audit/04-review.md` (export pending close).
- DV-S086-1 — the disposition decision deferring this fix.
- atom_id 59 — original S082 P-1 schema-sketch with NOT NULL contract.
