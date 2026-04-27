---
id: OI-085-002
title: Structural restriction of markdown authoring (no more honest tool use)
surfaced-in-session: 085
priority: HIGH
status: open
---

# OI-085-002 — Structural restriction of markdown authoring

## Why

Path A (S084 D-2) says agents do not author markdown for session state, specifications, or prompts; the substrate is canonical and `bin/selvedge export` materialises markdown views. Today this discipline is honour-bound — nothing structurally prevents the agent from editing `provenance/<NNN>-<slug>/*.md`, `specifications/*.md`, or `prompts/*.md` directly. The S084 → S085 cycle exhibited the failure mode: the orchestrator edited prompts as markdown and broke the spec_versions sha invariant; a follow-up session was required to register v2 rows and clear the drift.

Constraints §2 names this exact pattern: "Failure has no consequence the model can perceive. Tools that don't impose friction are not used." Honest tool use does not survive context pressure across sessions.

## What's needed

A structural block at the harness layer (Claude Code settings.json `PreToolUse` hook) that refuses `Write` and `Edit` against:

- `provenance/<NNN>-<slug>/*.md` (always — these are pure substrate exports)
- `specifications/*.md` where the corresponding `spec_versions.body_canonical_in_substrate = 1`
- `prompts/development.md`, `prompts/application.md` once their v2 rows have `body_canonical_in_substrate = 1`
- `PROMPT.md` once a `dispatcher` spec_id ships

The hook mirrors the substrate's refusal at the file boundary: file-level `Write`/`Edit` on substrate-canonical paths is refused; the agent must `bin/selvedge submit ...` and then `bin/selvedge export`.

Ratification path:
- Hook implemented as a small Python or shell program checking the path against `body_canonical_in_substrate`.
- `selvedge export specs --to specifications/` must ship first; otherwise spec edits have no path forward.
- Migration 008 introduces a `path_canonical_in_substrate(path TEXT, canonical INTEGER)` lookup table the hook reads, with rows for the always-canonical paths (provenance/) and the conditionally-canonical ones (specs, prompts) tracked via `body_canonical_in_substrate`.

## Disposition path

Open. Block on:
1. `selvedge export specs --to specifications/` shipping (so spec edits have a non-markdown path).
2. The `submit open-issue` and `submit engine-feedback` substrate kinds shipping (so all session-state writes have a CLI path).

Once both ship, a single session lands the harness hook + migration 008 + flips `body_canonical_in_substrate=1` on spec/prompt rows that currently sit at 0.
