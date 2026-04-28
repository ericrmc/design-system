You are about to execute the **Selvedge engine** against a specific application. This file is the dispatcher: it names the layers, names the two operating modes, and points to the mode-specific executable prompt. Load the pointed-at prompt and proceed under its instructions.

## The three layers

Per `specifications/identity.md` v2:

- **Selvedge** (unqualified) — names the methodology: the abstract-approach, domain-general mechanic of diverse perspectives reasoning together, producing durable artefacts, preserving reasoning, and evolving the system by running the same mechanic on its own outputs.
- **Selvedge engine** — denotes the current loadable implementation, enumerated in `specifications/engine-manifest.md`. The engine is the concrete file set; the methodology is the approach it realises.
- **Application of the Selvedge engine** — any specific run of the engine against a problem. Two kinds recognised: self-development and external-problem.

## The two operating modes

Every session runs the engine in exactly one mode. The mode is determined by the workspace's `MODE.md` file (authoritative when present) with a structural-signature fallback (see §Dispatch below).

- **Self-development** — the engine evolves its own specifications by running on its own outputs. This workspace has been the self-development application across sessions 001–035+ and is the source workspace where the engine is developed. Executable prompt: `prompts/development.md`.
- **External-problem** — the engine runs against a non-self problem in an application-specific workspace. The application's context (problem statement, constraints, stakeholders, success condition, initial state) is slotted into the executable prompt template. Executable prompt: `prompts/application.md`.

## Dispatch

At load, determine the workspace mode by the following ordered checks.

**1. `MODE.md` at workspace root (authoritative if present).** Read its frontmatter.

- If `mode: self-development` — this is the self-development application's source workspace. Load `prompts/development.md` and proceed under its instructions.
- If `mode: external-problem` — this is an external-problem application's workspace. Load `prompts/application.md`, populate its slots from the `application_brief:` pointer (typically `applications/NNN-<slug>/brief.md`), and proceed under its instructions.
- If `MODE.md` exists but carries an unrecognised `mode:` value, halt and seek clarification from the operator. Do not attempt to infer the mode.

**2. Structural signature (fallback when `MODE.md` is absent).**

- If the workspace contains the engine-definition files enumerated in `specifications/engine-manifest.md` §3 AND contains at least one `applications/NNN-<slug>/brief.md` file, this is an external-problem application's workspace. Load `prompts/application.md`. The loading session should create `MODE.md` at its close if not already present (one-time post-hoc creation per `specifications/workspace-structure.md` §MODE.md adoption clause).
- If the workspace contains the engine-definition files AND contains `provenance/001-genesis/` AND contains **no** `applications/NNN-<slug>/brief.md`, this is the self-development application's source workspace. Load `prompts/development.md`. The loading session should create `MODE.md` at its close if not already present.

**3. Ambiguous or uninitialised (halt).** If the workspace does not yet contain the engine-definition files, OR if both the external-problem and self-development structural signatures fire (e.g., a workspace containing both `provenance/001-genesis/` and an `applications/NNN-<slug>/brief.md`), OR if neither structural signature fires, halt and seek clarification from the operator. Do not attempt to infer the mode from partial evidence.

Engine version loaded is declared in `specifications/engine-manifest.md` §2. Every session's provenance should record which engine version was loaded.

## Session-001 obligation for new workspaces

Session 001 of any new workspace (self-development or external-problem) **MUST** create `MODE.md` at workspace root before substantive work. The file carries YAML frontmatter:

```yaml
---
mode: self-development | external-problem
workspace_id: <short stable identifier>
created_session: 001
engine_version_at_creation: <e.g., engine-v7>
---
```

For external-problem workspaces, `MODE.md` additionally carries `application_brief: applications/NNN-<slug>/brief.md`.

For pre-existing workspaces that adopt `MODE.md` after Session 001 (e.g., the self-development source workspace's one-time Session 036 adoption), the frontmatter additionally carries `marker_adopted_session: NNN` and `engine_version_at_marker_adoption: engine-vM`, recording the retroactive-adoption event distinct from at-init creation. Retroactive adoption is permitted only once per workspace.

## Operating discipline (applies in both modes)

Every application of the engine follows the rules in `prompts/development.md` §Rules that hold across applications. Those rules are invariant across modes: do not import ideas from outside the process; do not skip steps; do not overwrite prior specifications silently; preserve all provenance; leave the workspace in a coherent state at the end of every application.

The nine-activity kernel (Read, Assess, Convene, Deliberate, Decide, Produce, Validate, Record, Close) per `specifications/methodology-kernel.md` is the same in both modes. The multi-agent deliberation triggers per `specifications/multi-agent-deliberation.md` apply in both modes. The two-tier validation per `specifications/validation-approach.md` applies in both modes. The three senses of validation per kernel §7 apply in both modes.

## Engine-feedback pathway

External-problem workspaces may surface feedback about the engine or methodology itself during their execution (e.g., an unclear spec, a kernel §7 gap, a dispatcher ambiguity, a reference-validation exercise gap). Such feedback is recorded in the external workspace's `engine-feedback/` directory and is **operator-mediated** back into the self-development source workspace's `engine-feedback/inbox/`. The pathway's normative specification is in `specifications/workspace-structure.md` §engine-feedback. The self-development workspace's `prompts/development.md` reads `engine-feedback/INDEX.md` at session open when the file exists.

## Now dispatch

Inspect the workspace. Determine which mode applies via the ordered checks above. Load the appropriate executable prompt. Proceed under that prompt's instructions.
