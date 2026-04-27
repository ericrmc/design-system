---
session: 097
title: self-driving-dispatch-and-disposition-handlers — close
engine_version_at_close: engine-v27
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S097 ships engine-v27: forward_reference_dispositions table, engine-feedback-disposition + forward-reference-disposition handlers, prompt-development v3 with self-driving-dispatch and close-time-reflection sections.

## What was done

- Migration 013 ships forward_reference_dispositions table + T-26 facet gate + role capability.
- Two new submit handlers: engine-feedback-disposition (closes the substrate-only-writes loop EF-S096-2 surfaced) and forward-reference-disposition (closes EF-S096-1).
- _orient_sections forward-references: removed last-3-session window, filters NOT EXISTS in dispositions, renders FR-S<wno>-<seq> identifiers, capped at 30 with truncation flag.
- prompt-development v2 -> v3 adds 1.5 self-driving dispatch (propose from orient queue when prompt is open-ended) and 8.5 close-time reflection (mandatory engine_feedback row + dispose forward-references + dispose addressed engine_feedback).
- Disposed 7 EF rows (S092-1/2/4 by DV-S094-1; EF-S094-1, EF-S095-1, EF-S096-1/2 by DV-S097-1; EF-S092-3 deferred) and 6 forward-references (FR-S093-9, S094-9, S095-3/4, S096-3/4 by DV-S097-1).
## State at close

- Untriaged engine_feedback drops from 5 to 1 (only EF-S096-3 closes_issue trigger remains); undisposed forward-references drop from 19 to 13 (older S084-S091 next_should items remain — drainable in a cleanup pass).
- validate --precommit ok; pytest 24 of 26 pass (2 pre-existing contiguity tests broken per EF-S093-2).
## Open issues

- EF-S096-3 (closes_issue effect_kind is decorative-only) remains untriaged; the 13 historical forward-references are operationally stale but not yet disposed.
## What the next session should address

- Triage EF-S096-3 (closes_issue trigger or handler-side dispatch) so decision_effects.closes_issue actually flips issues.status; or run a queue-cleanup pass disposing the 13 historical FRs that are no longer load-bearing.
- Or pick OI-016 (HIGH, domain-validation under user unavailability) now that narrative-to-substrate friction is structurally lower.
## Engine version

- engine-v26 -> engine-v27.
## Validator at close

- validate --precommit ok; pytest 24 of 26 (2 broken pre-existing per EF-S093-2).
