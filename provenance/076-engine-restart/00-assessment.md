---
session: 076
title: Engine restart — assessment
date: 2026-04-27
engine_version_at_open: engine-v15
mode: self-development
---

# Assessment

## State at session-open

The Selvedge engine had completed seventy-five sessions of self-development. The active spec set carried ~3000 lines across nine specifications (`methodology-kernel.md`, `multi-agent-deliberation.md`, `validation-approach.md`, `identity.md`, `workspace-structure.md`, `reference-validation.md`, `read-contract.md`, `records-contract.md`, `retrieval-contract.md`) plus ~3200 lines of superseded `*-vN.md` versions, plus six tools (validator, retrieval substrate, harness-telemetry digest emitter and reconstructor, bootstrap script). The most recent session close (`provenance/075-session/03-close.md`) ran on the order of tens of thousands of words and the engine was operating well above its original ~90K-word soft aggregate ceiling.

The operator created `applications/075-selvedge-restart/selvedge-problem-statement.md` — a synthesis of what seventy-five sessions surfaced about LLM-agent properties and what the successor design must compensate for. The operator's brief to this session (preserved verbatim at `00-brief-from-operator.md`) directs:

- Trim the specifications right back this session.
- Skip reading the previous six sessions' provenance; ceremony there is heavy and would consume context.
- Do not use the substrate tools (retrieval, digest); they will be replaced by a database backend.
- Treat validator failures as warnings; the existing validator references many things that are about to be deleted.
- Next session (077) — design space via multi-agent deliberation including database backend and multiple new agents.
- Following session (078) — design the solution.
- Goal — restart the engine so it can be applied to itself and external applications with only minimal human intervention.

The brief is operator-directed and binding. No multi-agent deliberation precedes its execution; per the existing `multi-agent-deliberation.md` v4 §Opt-out, operator-directive on policy authority is a recognised opt-out from MAD requirement (the precedent applied at session 074 for the Gemini reviewer-family removal). The same opt-out applies here at the larger scope of trim-and-restart.

## Agenda

This session executes the trim. Concretely:

1. Save the operator's brief verbatim at `provenance/076-engine-restart/00-brief-from-operator.md` (done before this assessment).
2. Replace the active spec set with a minimal four-file surface: `methodology.md`, `constraints.md`, `workspace.md`, `engine-manifest.md`. Fold the prior identity, kernel, deliberation, validation, workspace-structure content into the methodology and workspace files. Drop the substrate-contract specs entirely (read-contract, records-contract, retrieval-contract) since the database successor design will replace them.
3. Replace the executable prompts (`PROMPT.md`, `prompts/development.md`, `prompts/application.md`) with thin versions that point at the minimal spec set.
4. Replace `tools/validate.sh` with a minimal structural validator. Move the substrate tools (retrieval, digest) and the bootstrap script to `archive/pre-restart/tools/`.
5. Move all superseded specifications and the now-deprecated active specs to `archive/pre-restart/specifications/`.
6. Bump the engine version to `engine-v16` in the new manifest.
7. Record session 076's decisions and close.

What this session does not do:

- It does not deliberate the successor design. Sessions 077 and 078 do that.
- It does not migrate any provenance, applications, engine-feedback, open-issues, or other workspace-scope material. Those remain in place; the successor design will decide their disposition.
- It does not design the database substrate. The next two sessions design it.
- It does not run a close-time reviewer audit. The trim is operator-directed and the prior reviewer mechanism is itself in the scope of the redesign.

## Honest limits

- This session reads only the active specs at small skim depth, the operator's brief, the engine manifest, and `PROMPT.md` and `MODE.md`. It does not read the seventy-five prior session closes, the open-issues directory, the engine-feedback inbox, or the validation-debt ledger. The operator's directive is explicit on this.
- The trimmed kernel deliberately omits a retrieval substrate, a default-read enumeration, an audit shape for the reviewer beyond three reporting axes, and a multi-agent orchestration pattern beyond the cross-family deliberation pattern. Sessions 077 and 078 are expected to fill these in.
- The surviving workspace state (provenance, applications, engine-feedback, open-issues, validation-debt, records) will appear inconsistent with the new minimal spec set: prior decisions reference `D-NNN` IDs, retention windows, audit shapes, and counters that the new specs do not name. This inconsistency is by design; it is the discontinuity that the restart marks.
