---
session: 099
title: substrate-driven-spec-authoring — close
engine_version_at_close: engine-v29
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

Engine-v29: substrate-driven spec body authoring via inline body_md on submit spec-version closes OI-S090-5.

## Engine version

- engine-v28 to engine-v29.
## What was done

- Extended _submit_spec_version to accept inline body_md; handler validates path-traversal, computes sha, writes file in-process after INSERT.
- Hoisted the path-traversal guard above the if/else so both authoring branches refuse body_path escapes from workspace_root.
- Added five pytest tests covering hash-match, sha-mismatch, empty body, whitespace-only body, and path-traversal on both branches plus orphan-file-on-rollback.
- Used the new path to land engine-manifest v28 (S098 catch-up), engine-manifest v29 (this session), and prompt-development v4.
## State at close

- selvedge.sqlite at engine-v29; spec_versions and on-disk hashes coherent; review_findings 55-61 disposed (fixed/adjudicated).
## Open issues

- OI-S090-5 resolved via DV-S099-1 closes_issue effect. 24 open issues remain; OI-016 (HIGH, deferred) is top of queue.
## What the next session should address

- Either pick OI-016 now that domain-validation gating is the only HIGH still open and substrate-authoring friction is gone.
- Or queue-cleanup pass: dispose the 14 still-undisposed historical forward-references (FR-S084-x through FR-S091-x) that reference resolved or stale items.
- Or pick OI-S090-2 (pytest coverage for Path A handlers + export round-trip) as a small follow-on.
## Validator at close

- tools/validate.sh: 17 ok / 0 fail. pytest spec_version coverage: 11/11 pass. Two pre-existing test_session_open failures predate S099.
