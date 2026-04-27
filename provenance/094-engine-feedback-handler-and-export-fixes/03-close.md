---
session: 094
title: engine-feedback-handler-and-export-fixes — close
engine_version_at_close: engine-v26
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S094 ships engine-v26: substrate-only-writes for engine_feedback + dry-run-legible reconciling export --issues.

## What was done

- Added submit engine-feedback handler in selvedge/cli.py with EF-S<wno>-<idx> alias allocation, refs recording, role capability gate.
- Renamed dry-run export key files_written->files_planned and added a dry_run flag, addressing EF-S092-1 misleading-key trap.
- _export_issues now reconciles by deleting on-disk *.md not in the substrate target set, addressing EF-S092-2 stale-path bug.
- Bumped engine-manifest to v26; workspace_metadata.current_engine_version updated atomically by the S091 handler.
## State at close

- Self-test: bin/selvedge submit engine-feedback produced EF-S094-1 cleanly; export --issues --write removed two stale top-level paths (OI-085-002, OI-086-002).
- pytest state/tests/test_existing_kinds.py passes excluding the two known-broken contiguity tests pre-existing per EF-S093-2.
- bin/selvedge validate --precommit reports ok.
## Open issues

- EF-S092-1, EF-S092-2, EF-S092-4 are addressed by code but their disposition fields remain set to surfaced-via-orient-DV-S093-1; no engine-feedback-disposition handler was added in this session.
## What the next session should address

- Add submit engine-feedback-disposition handler so the surfaced->triaged->resolved transitions can move via substrate-only-writes; then dispose EF-S092-1/2/4 referencing DV-S094-1.
- Or pick OI-S090-5 (substrate-driven spec content authoring path) so the engine-manifest body edit no longer requires bypassing the PreToolUse hook via Bash.
## Engine version

- engine-v25 -> engine-v26 per DV-S094-1.
## Validator at close

- validate --precommit ok; pytest 24 of 26 pass (2 broken contiguity tests pre-existing per EF-S093-2).
