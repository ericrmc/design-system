---
session: 093
title: orient-surfaces-engine-feedback — close
engine_version_at_close: engine-v25
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S093 ships orient surfacing of untriaged engine_feedback so triage signal is visible at session-open instead of waiting for subtract-eligibility aging.

## Engine version

- engine-v25 unchanged; orient extension is CLI-internal, no migration.
## What was done

- DV-S093-1 adopts an Untriaged engine feedback section in bin/selvedge orient; LEFT JOIN over engine_feedback x objects, filter disposition IS NULL, ordered DESC, capped at 20.
- _orient_sections returns untriaged_feedback / _total / _truncated; _orient_markdown renders a table with pipe-escaped heads.
- T-20 review converged in 2 iterations: 1 high fixed (dead test code), 1 medium fixed (blank-line head), 1 low fixed (NULL-alias fallback test).
- Six new pytest cases: empty-state shape, undisposed surfacing, disposed-filter, markdown rendering, blank-line head, NULL-alias fallback.
- EF-S092-1..4 triaged with disposition surfaced-via-orient-DV-S093-1; orient now shows 0 untriaged after the change.
## State at close

- engine-v25 active; orient shows untriaged_feedback section; 4 EFs disposed; 22 OIs open; no open review findings.
## Open issues

- Substrate friction list still includes: no submit engine-feedback handler (raw SQL still required); export --issues UX bugs (EF-S092-1/2 patterns) not yet fixed.
## What the next session should address

- Add submit engine-feedback handler so authoring follows substrate-only-writes; or fix export --issues to dry-run-by-default and reconcile open<->resolved transitions.
## Validator at close

- pytest 6/6 new orient cases pass; existing 18/18 migrate suite green; bin/selvedge orient end-to-end produced expected section.
