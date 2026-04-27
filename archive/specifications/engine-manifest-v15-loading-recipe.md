---
title: engine-manifest §"Loading the engine in a fresh workspace" (v16 recipe)
status: superseded
superseded-by: engine-manifest v17 (engine-v17, session 079)
superseded-on: 2026-04-27
provenance: provenance/079-substrate-vertical-slice/
---

# Removed: §"Loading the engine in a fresh workspace" (engine-v16 recipe)

To initialise a new external-problem workspace:

1. Copy the engine-definition files above into a fresh directory, preserving paths.
2. Create `MODE.md` declaring `mode: external-problem`, with a short `workspace_id` and `engine_version_at_creation: engine-v16`.
3. Create `applications/001-<slug>/brief.md` with the problem statement, constraints, stakeholders, success condition, and initial state. The brief is the primary input to every session's Read.
4. Create `provenance/`, `engine-feedback/`, and `open-issues/` as empty directories (they are populated as the application runs).
5. Run session 001 against the loaded engine. The dispatcher (`PROMPT.md`) selects `prompts/application.md` based on `MODE.md`.

The successor design (sessions 077–078) is expected to introduce a database substrate that changes initialisation. The recipe above is the recipe for `engine-v16`.

**Why removed.** 078 D-7 step 6: invalidated by 079's substrate. Engine-v17's loading recipe is `selvedge init` plus the operator filling `MODE.md` and `applications/001-<slug>/brief.md`; the recipe is documented in `selvedge init --help` (substrate-side) rather than in the manifest.
