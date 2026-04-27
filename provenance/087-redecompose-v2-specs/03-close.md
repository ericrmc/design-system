---
session: 087
title: redecompose-v2-specs — close
engine_version_at_close: engine-v21
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S087 closes OI-085-001: redecomposed three v2 spec_versions, landed migration 008 widening T-06 for body_canonical_in_substrate flips, bumped engine v20 to v21.

## Engine version

- engine-v20 to engine-v21 via migration 008.
## What was done

- Decomposed engine-manifest v20, prompt-application v2, prompt-development v2 into spec_sections+spec_clauses (24 sections, 200 clauses across the three).
- Wrote migration 008-widen-t06-for-canonical-flag.sql with one-time backfill UPDATE and widened T-06 WHEN clause; reviewer subagent ran iteration 1, two findings adjudicated.
- Updated specifications/engine-manifest.md to v21 (engine-v21 paragraph, migrations 005-008 enumerated, history line). Submitted spec-version v21 superseding v20; decomposed v21 (6 sections, 80 clauses).
- Direct UPDATE workspace_metadata.current_engine_version=engine-v21 and direct INSERT into refs to record v20 to v21 supersedes (handler bug worked around).
## State at close

- All six active specs now have body_canonical_in_substrate=1; engine-manifest v21 active; migration 008 applied; no open review findings.
## Open issues

- OI-085-001 closes; OI-086-001..004, OI-085-002, and the legacy 17 active OIs remain. Per dispatcher queue: OI-086-001 next.
- New observation: _submit_spec_version handler in selvedge/cli.py has two bugs surfaced by this session: INSERT-active-before-flip-prev order trips T-03 partial unique index; no-op UPDATE on already-superseded prev trips widened T-06.
- New observation: open_issues substrate table not yet schemaed; current OIs are markdown files. Operator flagged migration off MD as needed soon; deferred to dedicated session.
## What the next session should address

- Either fix _submit_spec_version handler order (insert as superseded then flip if needed; or flip prev first then insert) or schema open_issues substrate table; both are unblocked.
## Validator at close

- Pending bash tools/validate.sh post-export; expected pass.
