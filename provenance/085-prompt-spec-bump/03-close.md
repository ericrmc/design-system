---
session: 085
title: prompt-spec-bump — close
engine_version_at_close: engine-v20
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S085 register prompt-development v2 + prompt-application v2 to clear validator drift after S084 prompt edits.

## Engine version

- engine-v20 (no version bump in S085).
## What was done

- Two spec_version v2 rows registered with current file sha; v1 rows superseded.
## State at close

- Validator passes 17 ok / 0 fail. body_canonical_in_substrate=0 for v2 (markdown is canonical until re-decomposition).
## Open issues

- OI-085-001: re-decompose prompt-development v2 + prompt-application v2 into spec_clauses; flip body_canonical_in_substrate=1 when complete.
## What the next session should address

- Spawn spec-decomposition subagent for the two v2 prompts; OI-084-002 pytest coverage; OI-084-003 migrate runner harden.
