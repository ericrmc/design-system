---
id: OI-086-002
title: spec_versions has no constraint preventing two simultaneously-active versions per spec_id
surfaced-in-session: 086
priority: MEDIUM
status: open
---

# OI-086-002 — single-active spec_version per spec_id

## What S086 found

`spec_versions` declares `UNIQUE (spec_id, version)` and `status IN ('active','superseded')`, but nothing prevents two rows with the same `spec_id` from carrying `status='active'` simultaneously. Today the data is clean (each `spec_id` has exactly one active version), but the constraint is held by orchestrator discipline at submit time, not by the schema.

If a future submit kind that does not flip `status='superseded'` on the prior version slips through, the dispatcher's active-spec query (`PROMPT.md` §Read the active engine spec) silently returns clauses from both versions. The failure mode is the same as the prose-in-rows issue named in OI-085-002: honest tool use does not survive context pressure.

## What's needed

A SQLite partial unique index:

```sql
CREATE UNIQUE INDEX uq_spec_versions_one_active
  ON spec_versions(spec_id) WHERE status = 'active';
```

This refuses a second active row at write time. Migration is small (~5 lines effective DDL), additive (T-15 compliant), and the failure mode is loud (E_UNIQUE).

## Disposition path

Open. Land in the next schema-migration session. No prerequisite work; the data is already clean so the index applies cleanly.

## Cross-references

- F4 in `provenance/086-substrate-invariant-audit/04-review.md` (export pending close).
- DV-S086-1 — the disposition decision deferring this fix.
- OI-085-002 — same failure-mode pattern (honest tool use under context pressure).
