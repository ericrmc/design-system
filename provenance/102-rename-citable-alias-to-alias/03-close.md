---
session: 102
title: rename-citable-alias-to-alias — close
engine_version_at_close: engine-v30
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S102 ships engine-v30: rename objects.citable_alias and issues.citable_alias to alias via ALTER TABLE RENAME COLUMN, closing OI-S101-1.

## Engine version

- engine-v29 to engine-v30.
## What was done

- Migration 016 renames objects.citable_alias and issues.citable_alias to alias; T-22 trigger reissued with updated RAISE message naming alias.
- cli.py: ~50 callsites refactored hard-cut, payload field renamed, return shape now keys alias not citable_alias.
- tests refactored; prompt-development v5 + engine-manifest v30 submitted via spec-version body_md handler.
## State at close

- Substrate at engine-v30; orient packet validated; 31/33 pytest green (two pre-existing failures from session-offset assertions, unrelated).
## Open issues

- 24 open issues remain; OI-016 still the only HIGH; OI-S090-2 and OI-S090-1 still queued.
## What the next session should address

- Take OI-016 (domain-validation pathway HIGH) or OI-S090-2 (pytest coverage Path A handlers + export round-trip).
## Validator at close

- validate.sh 17 ok / 0 fail; pytest 31 passed / 2 pre-existing failures unrelated to S102.
