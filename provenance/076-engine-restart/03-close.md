---
session: 076
title: Engine restart — close
date: 2026-04-27
engine_version_at_close: engine-v16
mode: self-development
---

# Close

## What was done

Per `00-brief-from-operator.md` (verbatim) and `02-decisions.md`:

1. **Spec set trimmed to four active files.** New: `methodology.md`, `constraints.md`, `workspace.md`, `engine-manifest.md`. Replaced or absorbed: `methodology-kernel.md`, `identity.md`, `multi-agent-deliberation.md`, `validation-approach.md`, `workspace-structure.md`, `reference-validation.md`. Deleted from active: `read-contract.md`, `records-contract.md`, `retrieval-contract.md`, `aliases.yaml`. All retired files moved to `archive/pre-restart/specifications/`.

2. **Prompts and dispatcher rewritten.** New: `PROMPT.md` (thin dispatcher), `prompts/development.md` (self-development), `prompts/application.md` (external-problem). Combined ~130 lines vs. the prior ~227.

3. **Validator replaced with minimal structural script.** New: `tools/validate.sh` checks presence of the active engine-definition file set, `MODE.md`, `provenance/`, and (for the latest session directory) `00-assessment.md` and `03-close.md`. Run at close: 14 ok / 2 warn / 0 fail. The two warnings flagged this session's `00-assessment.md` and `03-close.md` as missing; both exist now (this file is the latter).

4. **Substrate tools archived.** `tools/retrieval_server.py`, `tools/build_retrieval_index.py`, `tools/digest_emitter.py`, `tools/digest_reconstructor.py`, `tools/bootstrap-external-workspace.sh` moved to `archive/pre-restart/tools/`. The `.claude/settings.json` PostToolUse hook is emptied; a no-op stub remains at `tools/digest_emitter.py` so that this session's already-loaded hook configuration does not error during this session's remaining tool calls. The stub and the `settings.json` empty state can be removed in a later session.

5. **Engine version bumped to `engine-v16`.** Recorded in the new `engine-manifest.md`.

6. **Session 076 provenance written.** `00-brief-from-operator.md` (verbatim operator brief), `00-assessment.md` (state and agenda), `02-decisions.md` (eight decisions D-1 through D-8 covering the trim, archive moves, version bump, prompt rewrite, validator rewrite, hook disable, workspace-scope preservation, and the engine-feedback blanket rejection), `03-close.md` (this file). No `01-deliberation.md` — the trim was operator-directed under the established opt-out precedent.

7. **Workspace-scope state preserved with one disposition action.** Prior `provenance/001-` through `075-`, `applications/`, `open-issues/`, `validation-debt/`, `records/` are unchanged. **`engine-feedback/`** received a disposition action per operator direction at this session's close: the nine still-open records (three `new` plus six `triaged`/`triaged-partially-resolved`/`triaged-deferred-to-phase-3`) are marked **rejected by engine-v16 restart supersession**. Per-record rationale is recorded at `engine-feedback/triage/EF-076-engine-v16-restart-supersession.md`. `engine-feedback/INDEX.md` status summary now shows 0 new / 0 triaged / 10 resolved / 9 rejected. The inbox/triage records themselves are preserved as historical empirical record.

## State at close

The workspace's active engine surface is `engine-v16`:

```
PROMPT.md
prompts/development.md
prompts/application.md
specifications/methodology.md
specifications/constraints.md
specifications/workspace.md
specifications/engine-manifest.md
tools/validate.sh
```

Plus `MODE.md` (workspace-identity, unchanged from session 036's adoption) and `CLAUDE.md` (per-workspace harness instructions, unchanged).

Workspace-scope state preserved in place: `provenance/`, `applications/`, `engine-feedback/`, `open-issues/`, `validation-debt/`, `records/`. These directories will likely be partially migrated, archived, or rearranged by the successor design produced in sessions 077 and 078.

The workspace is in a coherent state at the level of the active engine. It is not in a coherent state at the level of cross-references between the active engine and workspace-scope state — prior decision IDs, retention windows, audit shapes, and counters in the preserved directories reference specifications that have moved to archive. This incoherence is the discontinuity the restart marks; it is not an error to fix.

## What session 077 should address

Session 077 produces the **design space** for the next-generation Selvedge engine. The brief is `applications/075-selvedge-restart/selvedge-problem-statement.md`, distilled into `specifications/constraints.md`. The design space must include:

1. **A database backend** for structured state. Identifiers, decisions, references, lifecycle records, counters in a queryable store with integrity guarantees.
2. **Multiple new agents** for executing the methodology in a scalable way. Rough shape from the brief: a reader, a specifier, a decider, a deliberator group, a reviewer, a validator, an assembler. Each agent's context bounded; coordination through the substrate.
3. **A subtraction role** with the authority to remove. Not another counter — a structural role.
4. **The deliberately-built human review role** with defined scope and scheduled cadence.

Session 077 runs as a multi-agent deliberation with at least one perspective from a model family different from the orchestrator's. The deliberation produces a design-space artefact at `provenance/077-<slug>/01-deliberation.md` (or equivalent) that surveys the candidate architectures, the questions to be resolved, and the rejected directions. Session 077 does not commit to a solution; it produces the surface session 078 designs against.

Session 078 designs the solution against the design space and starts implementation.

The trim leaves enough room that session 077's reading load is the active engine (~350 lines) plus the constraints document plus the operator's problem statement. The session can then load the perspectives' deliberations and their syntheses without saturating its working memory.

## Honest limits

- This session did not run a close-time reviewer audit. The trim is operator-directed and the prior reviewer mechanism (`validation-approach.md` v9 §Tier 2.5) is itself in the redesign scope. Session 077 may elect to run a reviewer over this trim retrospectively; the review's scope should be "did the trim correctly preserve the foundation while removing ceremony" rather than the prior sessions' "trajectory discipline" framing, which is itself in scope for redesign.
- The new spec set has not been exercised by a real session yet. Session 077 is the first exercise. Aspects that read coherently here may prove insufficient or wrong under the load of an actual multi-agent deliberation; session 077's close should report what was missing.
- The `.claude/settings.json` empty state and the no-op `tools/digest_emitter.py` stub are workarounds for the in-session-loaded hook configuration; they will be cleaned up in a later session.
- Workspace-scope cross-reference integrity is broken by design (per "State at close" above). Sessions 077–078 will decide what to do about the broken cross-references when they design the database substrate.
