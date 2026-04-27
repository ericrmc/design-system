---
session: 091
title: engine-version-coherence — close
engine_version_at_close: engine-v25
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S091 ships engine-v25 + migration 011: structural coherence between workspace_metadata.current_engine_version and active engine-manifest spec_version; resolves OI-086-002 (already-satisfied by T-03).

## Engine version

- engine-v24 to engine-v25 via migration 011 + _submit_spec_version handler change
## What was done

- Migration 011 seeds workspace_metadata:update capability and backfills current_engine_version from engine-v23 to engine-v24
- _submit_spec_version: when spec_id=engine-manifest, atomically UPDATE workspace_metadata.current_engine_version inside the same write_tx; rowcount==1 invariant asserted
- Added test_engine_manifest_bump_updates_workspace_metadata covering positive (engine-manifest propagates) and negative (other spec_id does not touch metadata) paths
- OI-086-002 resolved as already-satisfied: T-03 in migration 001 is the partial UNIQUE index the OI requested
- T-20 review converged in 2 iterations: 1 medium fixed (rowcount check), 1 medium adjudicated (snapshot encoding tracked under OI-S091-1)
## State at close

- engine-manifest v25 active; workspace_metadata=engine-v25 (validated end-to-end by the v24 to v25 bump itself); 27 OIs open
## Validator at close

- tools/validate.sh expected ok; pytest 5/5 spec_version tests pass
## What the next session should address

- OI-016 (HIGH, domain-validation under user unavailability) is top of queue; OI-S089-1 (issue-work-item handler) closes the M:N CLI surface; OI-S090-5 substrate-driven spec authoring remains open
