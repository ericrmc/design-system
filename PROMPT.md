You are about to execute the **Selvedge engine** against a specific application. This file is the dispatcher: it names the layers, names the two operating modes, and points to the mode-specific executable prompt. Load the pointed-at prompt and proceed under its instructions.

## The three layers

Per `specifications/identity.md` v2:

- **Selvedge** (unqualified) — names the methodology: the abstract-approach, domain-general mechanic of diverse perspectives reasoning together, producing durable artefacts, preserving reasoning, and evolving the system by running the same mechanic on its own outputs.
- **Selvedge engine** — denotes the current loadable implementation, enumerated in `specifications/engine-manifest.md`. The engine is the concrete file set; the methodology is the approach it realises.
- **Application of the Selvedge engine** — any specific run of the engine against a problem. Two kinds recognised: self-development and external-problem.

## The two operating modes

Every session runs the engine in exactly one mode. The mode is determined by the workspace's state (see §Dispatch below).

- **Self-development** — the engine evolves its own specifications by running on its own outputs. This workspace has been the self-development application across sessions 001–017+. Executable prompt: `prompts/development.md`.
- **External-problem** — the engine runs against a non-self problem in an application-specific workspace. The application's context (problem statement, constraints, stakeholders, success condition, initial state) is slotted into the executable prompt template. Executable prompt: `prompts/application.md`.

## Dispatch

**If the workspace contains `SESSION-LOG.md` with prior sessions of self-development, plus the engine-definition files enumerated in `specifications/engine-manifest.md` §3, plus development-provenance in `provenance/` — this is the self-development application's source workspace.** Load `prompts/development.md` and proceed under its instructions.

**If the workspace contains the engine-definition files but a fresh (empty or near-empty) `SESSION-LOG.md`, a fresh `open-issues.md`, an empty `provenance/`, and an `applications/NNN-<slug>/brief.md` naming the problem — this is an external-problem application's workspace.** Load `prompts/application.md`, populate its slots from the `brief.md`, and proceed under its instructions.

**If the workspace does not yet contain the engine-definition files, or the dispatch is otherwise ambiguous**, halt and seek clarification from the operator. Do not attempt to infer the mode from partial evidence.

Engine version loaded is declared in `specifications/engine-manifest.md` §2. Every session's provenance should record which engine version was loaded.

## Operating discipline (applies in both modes)

Every application of the engine follows the rules in `prompts/development.md` §Rules that hold across applications. Those rules are invariant across modes: do not import ideas from outside the process; do not skip steps; do not overwrite prior specifications silently; preserve all provenance; leave the workspace in a coherent state at the end of every application.

The nine-activity kernel (Read, Assess, Convene, Deliberate, Decide, Produce, Validate, Record, Close) per `specifications/methodology-kernel.md` is the same in both modes. The multi-agent deliberation triggers per `specifications/multi-agent-deliberation.md` apply in both modes. The two-tier validation per `specifications/validation-approach.md` applies in both modes. The three senses of validation per kernel §7 apply in both modes.

## Now dispatch

Inspect the workspace. Determine which mode applies. Load the appropriate executable prompt. Proceed under that prompt's instructions.
