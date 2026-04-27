---
id: OI-086-004
title: legacy_imports.decomposition_status does not track actual decomposition coverage
surfaced-in-session: 086
priority: MEDIUM
status: open
---

# OI-086-004 — legacy_imports.decomposition_status semantics

## What S086 found

The `legacy_imports.decomposition_status` column is set by the import / submit path at write time but is never validated against the actual presence of decomposed rows. Concretely, in the present substrate:

- Perspectives 1–5 (S080 smoke-A/B and S081 claude/codex/adversarial) carry `decomposition_status='ratified'` but have **zero** `perspective_position` rows and **zero** `perspective_claim` rows. Their `body_md` remains the only carrier.
- Perspectives 6–8 (S082 P-1/P-2/P-3) carry `decomposition_status='in_progress'` but have **3** positions and **126** claims captured (35 + 39 + 52). They are nearly-fully decomposed but their status row says otherwise.

The column means nothing without something asserting it. Operators reading it as a coverage indicator (which it claims to be) get the inverse signal.

## What's needed

Two viable shapes:

1. **Derive, do not assert.** Replace the column with a view that computes status from row presence: `unratified` if 0 positions/claims, `in_progress` if some, `ratified` if ≥1 position AND ≥1 claim. Drop the stored column (T-15-compliant via migration, since column-drop is admitted under the recreate-table pattern).

2. **Assert via trigger.** Keep the column but add a trigger on `legacy_imports` UPDATE that refuses `decomposition_status='ratified'` if the corresponding source row has zero downstream rows. Also add a trigger on `perspective_position` / `perspective_claim` INSERT that bumps the linked legacy_import row from `unratified` → `in_progress`.

Option 1 is cleaner (single source of truth) but requires careful migration. Option 2 keeps the writable column but introduces three new triggers.

## Disposition path

Open. Independent of the OI-086-001/002/003 cluster; can land in any future schema-migration session. The right framing is: "does this column do real work, or is it a stale comment?" If the answer at next-touch is "stale comment", drop it via Option 1.

## Cross-references

- F8 in `provenance/086-substrate-invariant-audit/04-review.md` (export pending close).
- DV-S086-1 — the disposition decision deferring this fix.
