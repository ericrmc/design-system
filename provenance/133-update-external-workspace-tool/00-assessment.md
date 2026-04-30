---
session: 133
title: update-external-workspace-tool — assessment
engine_version_at_open: engine-v39
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S132 shipped methodology v7 and engine-manifest v39 lifting deliberation discipline to kernel; engine-v39 active. External workspace selvedge-disaster-recovery is at engine-v31 (8 versions behind).

## Agenda

1. Ship tools/update-external-workspace.sh: propagate engine-definition file set from source to target external workspace; apply new migrations; preserve application state.
2. Pre-flight refusals: target must exist with MODE.md and substrate, mode must be external-problem, no open session in target.
3. Default dry-run; explicit --apply required. SHIP_FILES per engine-manifest section 3; SUBTRACTED_FILES list cleans up files removed from prior versions.
4. Fix tools/bootstrap-external-workspace.sh: remove constraints.md from spec copy loop (subtracted at engine-v32 S109 DV-S109-1).
5. Coding review loop per T-30; reviewer subagent audits both scripts; iterate until clean.
6. Apply tool against disaster-recovery workspace: dry-run, then --apply; expect engine-v31 to engine-v39 via 8 new migrations.
