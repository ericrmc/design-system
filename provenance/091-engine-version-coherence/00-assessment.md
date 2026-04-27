---
session: 091
title: engine-version-coherence — assessment
engine_version_at_open: engine-v23
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S091 at engine-v23 (stale metadata; substrate truth is v24 via engine-manifest v24 active). Substrate hygiene: fix metadata coherence, resolve OI-086-002.

## Agenda

1. Fix _submit_spec_version: when spec_id=engine-manifest, UPDATE workspace_metadata.current_engine_version
2. Backfill workspace_metadata.current_engine_version to engine-v24
3. Resolve OI-086-002: T-03 is the partial UNIQUE index the OI asks for
4. T-20 review on the handler change
5. Engine bump v24 to v25 (handler structurally enforces coherence)
6. Close + export + validate + commit
