---
session: 098
title: closes-issue-effect-wiring — close
engine_version_at_close: engine-v28
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

Engine-v28: closes_issue effects dispatch issue resolution via handler plus refusal trigger; identity carried by typed target_issue_id column.

## Engine version

- engine-v27 to engine-v28.
## What was done

- Added decision_effects.target_issue_id (mig 014); reissued T-17 to admit it; added T-27 (requires target_issue_id for closes_issue) and T-28 (target must be resolved/superseded).
- Wired _submit_decision_v2 to dispatch closes_issue effects through _submit_issue_disposition before INSERT, in the same write_tx, with descriptor bounds 8-120.
- Migration 015 extended decision_effects UNIQUE to include target_issue_id via calibrated table-recreation; triggers reissued outside the block.
- Updated _export_session_provenance to read target_issue_id and render closes_issue lines as kind alias dash descriptor.
## State at close

- All five smoke-test paths green (handler validation 3, T-27 bypass refusal, T-28 open-target refusal); review iteration 3 reports clean.
## Open issues

- OI-S090-5 substrate-spec authoring blocked two finding-fixes this session; OI-S090-2 pytest gap means smoke-tests are inline only.
## What the next session should address

- Either schedule a substrate-spec authoring pass on OI-S090-5 to land the engine-v28 manifest entry and prompts/development.md closes_issue contract.
- Or pick OI-016 (HIGH, deferred) now that the issue-lifecycle dispatch surface is structurally enforced; or run the queue-cleanup pass disposing 13 historical FRs.
- Or wire opens_issue when willing to grow decision_effects schema with title/priority fields, or define the policy that issues stay opened via explicit submit issue.
## Validator at close

- tools/validate.sh runs in the post-close commit step; smoke tests in-session covered handler bounds 7/8/120/121, T-17 fallthrough, T-27 bypass, T-28 open-target.
