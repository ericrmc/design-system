---
session: 109
title: subtract-constraints-from-manifest — close
engine_version_at_close: engine-v32
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

Subtracts constraints.md from the engine-definition file set; archives it; engine bumps to v32.

## Engine version

- engine-v31 to engine-v32.
## What was done

- Removed constraints.md from engine-definition file set: spec_version superseded, file archived to archive/specifications/constraints-v1.md, manifest updated to v32, PROMPT.md and validate.sh cleaned of dangling references.
- Backfilled substrate table in engine-manifest through migration 018, closing FR-S107-11 and FR-S108-10.
- Corrected frontmatter version drift in engine-manifest (was saying v30, now correctly v32).
## State at close

- Engine-definition file set is 7 markdown files (down from 8). constraints spec_version row is superseded. Validator passes 16/16.
## Open issues

- 26 open issues unchanged. workspace.md line 12 retains a historical citation to constraints.md (adjudicated low, no engine-coherence impact).
## What the next session should address

- Proceed with external workspace bootstrap (FR-S108-8, FR-S108-9) or address highest-priority open issues per orient queue.
## Validator at close

- bash tools/validate.sh: 16 ok / 0 fail. selvedge validate --precommit: ok.
