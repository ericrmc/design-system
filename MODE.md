---
mode: self-development
workspace_id: selvedge-self-development
created_session: 001
marker_adopted_session: 036
engine_version_at_creation: engine-v1
engine_version_at_marker_adoption: engine-v7
---

# Workspace mode marker

This workspace is the **self-development application** of the Selvedge engine. It has been self-development from Session 001 (2026-04-17, genesis session) through the current session. It is the source workspace where the engine is developed.

The marker file `MODE.md` was adopted at engine-v7 (Session 036 per D-113). For Session 001 of any *new* workspace (either self-development or external-problem), this file is created at Session 001 before substantive work. For this pre-existing workspace, the marker is adopted retroactively at the engine-v7 adoption session (Session 036), carrying `marker_adopted_session: 036` to record the one-time post-hoc creation distinct from at-init creation.

See `PROMPT.md` §Dispatch for how this file is consumed at session load.

See `specifications/workspace-structure.md` §MODE.md for the normative specification.

See `specifications/engine-manifest.md` §Workspace identity files for the classification of this file as workspace-identity (distinct from engine-definition).
