---
title: Methodology
version: 2
status: active
created: 2026-04-27
updated-by-session: 079
supersedes: methodology-v1 (engine-v16); per 078 D-7
---

# Methodology

This file defines what Selvedge does. It is the entire kernel: what the engine is, what a session does, when to convene multiple agents, when to review at close, and how preservation works. It replaces the prior split across `methodology-kernel.md`, `identity.md`, `multi-agent-deliberation.md`, and `validation-approach.md`.

## What Selvedge is

Three layers:

- **Selvedge** — the methodology. Diverse perspectives reasoning together, producing durable artefacts, preserving reasoning, and evolving the system by running the same mechanic on its own outputs.
- **Selvedge engine** — the current loadable implementation. The set of files enumerated in `specifications/engine-manifest.md` at a given commit.
- **Application of the engine** — a specific run against a problem. Two kinds: **self-development** (the engine evolves its own specifications) and **external-problem** (the engine runs against a non-self problem).

The methodology is domain-general. The engine is a concrete realisation. An application is a particular run.

The name *selvedge* — the self-finished edge of woven cloth — names three properties: self-hosting (the methodology evolves by running its own process on itself), multi-strand preservation (disagreement preserved as first-class, not melted into consensus), and durability by construction (versioned specs, recorded supersession, provenance as a first-class output).

## How a session works

A **session** is one application of the engine. Each session reads what it needs from the workspace, decides what to advance, does the work, and closes coherently.

A session may include any subset of the following activities. They are a vocabulary, not a strict sequence. They have a general flow (you cannot decide before you deliberate) but recursion is permitted.

1. **Read** — load only what the session's work requires. Record what was loaded.
2. **Assess** — state what this session will address and why. The agenda is explicit so the next session can read it.
3. **Convene** — name the perspectives the work needs. For deliberative work, at least one perspective is adversarial.
4. **Deliberate** — perspectives state positions independently before seeing one another, then synthesise. Disagreements are preserved.
5. **Decide** — record what was decided, the reasoning that carried it, what was rejected and why, what remains open.
6. **Produce** — create or revise the artefacts the decisions warrant.
7. **Validate** — check that what was produced is consistent with the workspace and meets its stated purpose. Three senses: workspace, domain, and provisional reference substitute (when no domain-actor is available).
8. **Record** — commit the session's provenance to `provenance/NNN-<slug>/`.
9. **Close** — leave the workspace coherent. Commit at git. State what the next session should address.

A session that does only validation may skip Convene and Deliberate. A session that proposes a kernel revision should perform all nine.

## When to convene multiple agents

Use multi-agent deliberation when:

- The decision changes how the methodology works (a kernel revision, a deliberation-pattern change, a validation-mechanism change, a workspace-structure change).
- The question has two or more genuinely plausible positions that the author can name before deliberation.
- The author marks the work load-bearing for reasons stated in the record.

Each perspective:

- States its position before seeing other perspectives' positions, to prevent anchoring.
- Cites the workspace material it relied on for load-bearing claims.
- Is willing to say "I don't know" rather than fabricate.

At least one perspective is adversarial (challenges the emerging consensus, identifies unstated assumptions, argues for alternatives).

When the decision touches the methodology itself, **at least one perspective should come from a different model family** (different organisation; e.g., not Anthropic). The cross-family perspective surfaces assumptions a single training-distribution shares. This was Selvedge's earliest substantive finding (session 4) and the property that protected the methodology's foundation against single-family bias.

The synthesis of perspectives **is not itself a decision**. It feeds Decide. Synthesis preserves dissent: a minority position is recorded as a minority, not erased.

If a multi-agent deliberation would otherwise be triggered but is not performed (because the workspace lacks a non-Claude provider, because the decision is operator-directed, because the cost is unwarranted for this scope), the reason is recorded in the session's decision record.

## When to review at close

Close-time review is superseded until the substrate distinguishes prevention from audit; D-2 conditional re-introduction governs (per 078 D-7 step 1; prior text archived at `archive/specifications/methodology-v1-removed-sections.md`).

## Validation senses

A session's Validate activity may operate at two senses:

- **Workspace validation** — the session's artefacts are internally consistent, do not contradict active specifications, and accurately describe the workspace as it is. Workspace validation applies to every session.
- **Domain validation** — when a session produces an artefact intended for use outside the workspace, and a domain-actor is available, the domain-actor reports whether the artefact functioned for its intended use. The session records the report.

## Preservation

- **Decisions record rejected alternatives**, not just chosen options. The reasoning that led to a rejection is the input to a future decision that may reconsider it.
- **Specifications evolve through new versions, not silent edits.** When a spec is revised, the prior version is preserved (in archive or under a versioned filename) and the new version takes its place at the canonical filename.
- **Provenance is immutable after close.** Closed-session records are not edited; if a closed session contained an error, a subsequent session corrects it explicitly with a record of the correction.
- **All session work is committed to git** at close. Git history is the workspace's tamper-evident substrate.

## Engine-feedback pathway

**Engine-feedback** is the channel for surfacing concerns about the methodology itself during the execution of an application. An operator (human) or an application-agent records observations as files at `engine-feedback/EF-<session>-<slug>.md`. A future session may triage feedback and act on it as a methodology revision.

The engine-feedback pathway is what allowed the operator's interventions across Selvedge's seventy-five self-development sessions to become structural rather than ephemeral. A successor system should not rely on a self-correcting agent (no LLM agent has shown sustained self-correction under load); it should expect that some of its limitations will be surfaced by humans and design the surfacing path deliberately.

## Self-hosting

The methodology evolves by applying its own process to itself. Changes to this kernel pass through the same Read → Assess → Convene → Deliberate → Decide → Produce → Validate → Record → Close as any other artefact. The kernel is revised when the process it describes no longer matches the process actually followed, or when a better process is discovered.

The self-hosting property has limits. A self-applied methodology with no problem outside itself loses the falsification signal that keeps work substantive. The methodology that survives contact with a real complex-systems-design problem will be different from the one that has only been applied to itself, and only the former is the methodology Selvedge originally set out to build. Self-development is the bootstrap, not the destination.
