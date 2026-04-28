---
session: 101
title: orient-fr-rot-flag — close
engine_version_at_close: engine-v29
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

Always-on inline rot annotation lands in orient: FRs whose cited issue aliases are resolved/superseded/absent get a [rot: ...] suffix at render time, no schema change, no flag.

## Engine version

- engine-v29 (no bump; CLI/code-only change to orient packet rendering).
## What was done

- Three-perspective deliberation (Plan/codex/adversarial); decision DV-S101-1; FR_ISSUE_CITE_RE constant and rot-extraction block in _compute_orient_packet; rot suffix in _orient_markdown; reviewer two-iteration loop converged clean.
- Always-on inline annotation appears only when an FR cites at least one issue alias whose status is resolved/superseded or whose row is absent.
## State at close

- Orient FR section now shows rot annotations; current 4 undisposed FRs all cite live issues, so output is byte-identical to pre-patch baseline today.
## Open issues

- OI-S101-1 opened: rename objects.citable_alias to objects.alias for query ergonomics (LOW).
## What the next session should address

- Pick OI-016 or OI-S090-2 (the two outstanding asks from S099/S100 that remain undisposed).
- Or take OI-S101-1 (citable_alias rename) as a small substrate-ergonomics follow-on.
## Validator at close

- tools/validate.sh: 17 ok / 0 fail. Reviewer iteration-2 CLEAN.
