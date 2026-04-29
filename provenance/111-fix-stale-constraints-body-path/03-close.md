---
session: 111
title: fix-stale-constraints-body-path — close
engine_version_at_close: engine-v33
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S111 closes OI-S110-2 by calibrated backfill migration 020 correcting stale body_path on superseded constraints v1 to its archive location.

## Engine version

- engine-v33 (no version bump; surgical data-correction migration only).
## What was done

- Migration 020 drops T-06 UPDATE trigger, scopes UPDATE to spec_id=constraints version=1 status=superseded, recreates trigger unchanged.
- DV-S111-1 records adopt of one-time backfill pattern with three rejected alternatives (widen T-06, leave stale, NULL the path).
- Reviewer Explore subagent ran ten-point adversarial checklist against migration 020 and reported clean on iteration 1.
## State at close

- spec_versions row 3 now points at archive/specifications/constraints-v1.md with sha b632567... matching the archived file.
## Open issues

- OI-S110-1 (orient discoverability of superseded specs) and OI-S110-3 (alias backfill) remain for subsequent sessions per FR-S110-11.
## What the next session should address

- Address OI-S110-1 next (orient discoverability of superseded specs) per FR-S110-11 sequencing.
- Consider documenting subtraction-supersession convention in workspace.md so future spec removals update body_path at supersede time without needing a calibrated migration.
## Validator at close

- Migration applied cleanly; review-pass outcome=clean iteration=1; T-15 compliant (no DROP TABLE/COLUMN, no CHECK relaxation).
