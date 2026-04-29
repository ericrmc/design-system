---
session: 120
title: submit-dry-run — close
engine_version_at_close: engine-v34
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S120 ships bin/selvedge submit --dry-run on engine-v34 with iter-1 clean review, closing FR-S118-10 / FR-S119-10 / EF-S118-1 friction.

## Engine version

- engine-v34 (no bump; runtime addition only, no spec/manifest change).
## What was done

- Conn.write_tx accepts dry_run kwarg and ROLLBACKs after a successful handler when set.
- cmd_submit threads --dry-run via _dry_run_var contextvar and emits dry_run:true in the JSON envelope.
- _submit_spec_version suppresses its body-file write when is_dry_run() to keep the workspace clean under rollback.
- Smoke-verified valid path (decision-record returns alias DV-S120-1 with row count unchanged) and refusal path (T-31 / E_VALIDATION still propagates with dry_run:true).
## State at close

- Substrate clean; validate.sh 16/0; review-pass iter-1 outcome=clean; one LOW finding adjudicated (ROWID reuse note).
## Open issues

- No new issues opened; FR-S118-10 / FR-S119-10 disposed; EF-S118-1 disposed.
## What the next session should address

- Address next highest-priority forward-reference or open issue from orient queue; OI-S104-2 (decision_effects.effect_kind deletes) and OI-S105-1 (third validation sense) remain low-friction candidates.
## Validator at close

- tools/validate.sh 16 ok / 0 fail; selvedge validate --precommit ok.
