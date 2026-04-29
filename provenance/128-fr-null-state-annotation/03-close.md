---
session: 128
title: fr-null-state-annotation — close
engine_version_at_close: engine-v37
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S128 ships orient-time FR null-state annotation closing OI-S126-4 via two paths.py regex constants and orient.py render hook.

## Engine version

- engine-v37 unchanged; pure orient-rendering refinement, no spec or migration.
## What was done

- Added FR_ANY_ALIAS_RE and FR_NULL_STATE_RE to paths.py; orient.py emits null_state per FR item and renders [null-state] suffix.
- Five tests cover pure null-state, mixed-with-cite, no-phrase-actionable, cite-only-actionable, and markdown rendering.
- Disposed FR-S127-7, FR-S126-8, FR-S117-11; closed OI-S126-4 via DV-S128-1 closes_issue effect.
## State at close

- 203 pytest pass; orient queue against live substrate flags exactly one item (FR-S117-11) before disposition.
## Open issues

- DV-S128-2 defers P-2 schema-column enforcement direction until null-state recurrence after annotation lands.
## What the next session should address

- Pilot reference_harness against disaster-response stage 2 close per FR-S124-17, or address OI-S125-2 harness expire CLI.
## Validator at close

- tools/validate.sh 17 ok / 0 fail including 203-test pytest suite.
