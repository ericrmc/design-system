---
session: 090
title: lost-ois-and-md-hook — close
engine_version_at_close: engine-v24
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S090 ships engine-v24 PreToolUse hook (resolves OI-085-002 after 4 deferrals), reorders _submit_spec_version (resolves OI-S090-4, fixes 3-session regression), files 5 lost OIs (OI-S090-1..5).

## Engine version

- engine-v23 to engine-v24 via .claude/settings.json hook wiring (no migration; harness configuration)
## What was done

- tools/hooks/refuse-substrate-md.py created; .claude/settings.json wires it on Edit, Write, MultiEdit, NotebookEdit
- selvedge/cli.py _submit_spec_version reordered: prev to superseded BEFORE insert; T-03 satisfied
- Added 2 pytest cases (supersession happy-path + T-03 structural-guarantee); both pass
- T-20 ran twice: loop 1 (handler reorder) converged in 2 iterations; loop 2 (hook) converged in 2 iterations; 4 medium findings recorded and fixed
## State at close

- OI-085-002 + OI-S090-4 resolved; OI-S090-1..3 + OI-S090-5 filed; engine-manifest v24 active; 25 OIs open
## Validator at close

- Hook live-verified by probe Write to specifications/__hook_verify.md (refused exit 2); spec-version v23 to v24 submitted without T-03 trip
## What the next session should address

- OI-016 (HIGH, domain-validation under user unavailability) is now top of queue; OI-S090-5 (substrate-driven spec authoring) is the felt-friction follow-up; OI-S090-1..3 are mediums available
