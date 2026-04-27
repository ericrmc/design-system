---
session: 087
title: redecompose-v2-specs — assessment
engine_version_at_open: engine-v20
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

Three v2 spec rows (engine-manifest v20, prompt-application v2, prompt-development v2) are active with body_canonical_in_substrate=0 and zero sections/clauses; OI-085-001 mandates re-decomposition.

## Agenda

1. Spawn spec-decomposition subagent to read each markdown body and submit spec-section + spec-clause rows against the existing v2 spec_version_ids.
2. Verify clause counts post-decomposition vs v1 baselines (engine-manifest 40, prompt-application 30, prompt-development 38).
3. Flip body_canonical_in_substrate=1 on the three v2 rows via direct SQL UPDATE; record rationale in decision-record (no CLI kind exists; flag has no read-side consumer).
4. Submit decision-record adopting the redecomposition outcome with supports citing OI-085-001 and DV-S086-1; close session.
