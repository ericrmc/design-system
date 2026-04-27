# Selvedge engine — dispatcher

You are about to execute the **Selvedge engine** against a workspace. This file determines which executable prompt applies and points at it.

## Read these first

The engine's active specification set at this commit is small. Read all four:

- `specifications/methodology.md` — what the engine does in a session: the three layers, the nine activities, when to convene multiple agents, when to review at close, validation senses, preservation, engine-feedback, self-hosting.
- `specifications/constraints.md` — what 75 sessions of self-development taught us about LLM agents and what the successor design must compensate for. This is the brief for the next two sessions.
- `specifications/workspace.md` — file classes, session structure, decisions, specifications discipline.
- `specifications/engine-manifest.md` — what files constitute the loadable engine at the current version.

The engine version is named in `engine-manifest.md` §Current engine version.

## Dispatch

Determine the workspace mode by reading `MODE.md` at workspace root.

- If `mode: self-development` — load `prompts/development.md` and proceed under its instructions.
- If `mode: external-problem` — load `prompts/application.md`. Read `applications/NNN-<slug>/brief.md` per the pointer in `MODE.md`.
- If `MODE.md` is absent or carries an unrecognised value — halt and ask the operator.

A new workspace's session 001 creates `MODE.md` before substantive work, with frontmatter:

```yaml
---
mode: self-development | external-problem
workspace_id: <short stable identifier>
engine_version_at_creation: engine-v16
created_session: 001
application_brief: applications/NNN-<slug>/brief.md   # external-problem only
---
```

## Operating discipline

The methodology kernel in `specifications/methodology.md` is the same in both modes. The constraints in `specifications/constraints.md` apply to both modes. Workspace structure in `specifications/workspace.md` applies to both modes.

What distinguishes the two modes: in self-development the engine evolves its own specifications; in external-problem the engine produces artefacts for a domain outside itself. Both run the same nine activities, both convene multiple perspectives when the work warrants, both record provenance, both close coherently.

## Engine-feedback

External-problem workspaces may surface feedback about the engine itself during execution (an unclear spec, a kernel gap, a validator failure, a tool that doesn't function). Such observations are recorded in the external workspace's `engine-feedback/EF-<session>-<slug>.md` and transported by the operator back to the source workspace's `engine-feedback/` for triage.

## Now dispatch

Inspect `MODE.md`. Load the appropriate executable prompt. Proceed.
