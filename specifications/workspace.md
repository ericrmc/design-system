---
title: Workspace structure
version: 2
status: active
created: 2026-04-27
updated-by-session: 079
supersedes: workspace-v1 (engine-v16); per 078 D-7
---

# Workspace structure

This file defines where files live in a Selvedge workspace and what each holds. It replaces the prior `workspace-structure.md` plus the substrate-contract specifications (`read-contract.md`, `records-contract.md`, `retrieval-contract.md`), which were tied to a Markdown-only-state arrangement that the successor design will replace with a database substrate (per `specifications/constraints.md`).

## File classes

A Selvedge workspace contains four classes of file:

- **Engine-definition** — the loadable engine. Same across workspaces (modulo version). Enumerated in `specifications/engine-manifest.md`.
- **Workspace-identity** — `MODE.md` declares whether this workspace is `self-development` or `external-problem`. Each workspace writes its own.
- **Application** — `applications/NNN-<slug>/` carries the problem statement, constraints, success condition, and produced artefacts for one application of the engine. The first session of an external-problem workspace creates `applications/001-<slug>/brief.md` from the operator's framing.
- **Provenance** — `provenance/NNN-<slug>/` holds the record of one session's work. One directory per session. Immutable after close.

External workspaces inherit only the engine-definition files. They do not inherit the source workspace's provenance, applications, or workspace-identity.

## Top-level layout

The manifest defines engine-definition files; session records live under `provenance/`; structured state lives in `state/selvedge.sqlite` (per engine-v17); generated exports are not the source of truth once the substrate exists. (Per 078 D-7 step 5; the prior enumerated tree is archived at `archive/specifications/workspace-v1-removed-sections.md`.)

## Sessions

A **session** is one application of the engine. Each session's record lives at `provenance/NNN-<slug>/`, where `NNN` is the zero-padded session number and `<slug>` is a short kebab-case description of the session's focus.

Required files per session:

- `00-assessment.md` — the session's read of state and the agenda it commits to.
- `02-decisions.md` — what was decided, why, what was rejected, what remains open.
- `03-close.md` — what was produced, what state the workspace is in, what the next session should address.

Conditional files:

- `01-deliberation.md` — the synthesis of multi-agent deliberation when one was performed. Per-perspective records (one file per perspective) may sit alongside.
- `04-review.md` — the close-time reviewer's audit, when one was performed.

A session may add other files (raw perspective records, design-space surveys, draft artefacts) as the work warrants. The four files above are the load-bearing surface.

## Decisions

Each decision in `02-decisions.md` records:

- **What** — a single concrete commitment.
- **Why** — the key arguments that carried it. Cite source perspectives or workspace material.
- **Rejected alternatives** — the options considered and not chosen, each with the reason.
- **Open** — what remains uncertain or deferred.

Decisions are numbered within a session as `D-1`, `D-2`, etc. A workspace-wide decision counter is **not** maintained in Markdown; it will be derived from the database substrate when the successor design provides one. Until then, decisions are addressable as `<session-NNN>:D-N`.

## Specifications

Specifications are the durable design intent of the engine. They live in `specifications/` and carry YAML frontmatter:

```yaml
---
title: <title>
version: <integer>
status: active | superseded
---
```

When a spec is revised in substance, the prior version is preserved (in `archive/specifications/` or under a versioned filename like `<spec>-v<N>.md` with `status: superseded`) and the new version takes its place at the canonical filename.

A specification has three sections at minimum: a brief statement of what it specifies, the specification body, and (where applicable) how to validate it. Length and elaboration are matched to scope; brevity is preferred.

## Open issues

Items that warrant attention beyond a single session live in `open-issues/`:

- `OI-<id>-<slug>.md` per issue, where `<id>` is a numeric or short string identifier.
- `index.md` lists active issues with one-line summaries.

An open issue is closed when its disposition (resolved, deferred, withdrawn, superseded) is recorded in the issue file. Closed issues are preserved, not deleted.

## Engine-feedback

Operator-mediated observations about the methodology are recorded at `engine-feedback/EF-<session>-<slug>.md`. The directory is optional; it is created when the first feedback record is written.

Engine-feedback flows operator-mediated from external-problem workspaces back into the self-development source workspace's `engine-feedback/` for triage. The engine does not specify automated cross-workspace transport; the operator is the transport.

## Archive

Files no longer part of the active engine but preserved for historical reference live under `archive/`. Examples: superseded specification versions, retired tools, deliberation records that have outgrown context budgets.

Archive content is not loaded by the engine. It is read by humans or by future sessions on explicit reference.
