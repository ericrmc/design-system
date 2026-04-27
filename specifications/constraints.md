---
title: Constraints — what 75 sessions taught us
version: 1
status: active
created: 2026-04-27
updated-by-session: 076
source: applications/075-selvedge-restart/selvedge-problem-statement.md
---

# Constraints — what 75 sessions taught us about LLM agents

Selvedge ran for seventy-five sessions on its own development before the operator paused it for redesign. Over those sessions it produced and refined specifications through multi-agent deliberation, introduced cross-family validation, built an engine-feedback pathway, adopted a retrieval substrate, and layered a separate review at session close. Late in the run, the engine could no longer correct itself.

The trajectory surfaced six properties of language models that any LLM-driven design methodology must work around. The methodology must build for the agent the model actually is, not the agent the methodology wishes it had.

This file is the brief that informs the next-generation engine. The successor reads this before designing what comes next. The next two sessions (077 design-space and 078 solution-design) deliberate against this constraint set.

## The six properties

### 1. Models default to prose

When asked to track structured state — identifiers, cross-references, lifecycle records, counters — a model produces Markdown tables and narrative rather than reaching for a database. This is its native output. Without external friction making prose costly for state-management work, the model never feels the cost of choosing it.

Selvedge stored everything in Markdown files in git. Identifiers drifted, references pointed at superseded versions, counters were miscounted, and the failures recurred across sessions, caught only at close-time audits where they were fixed by hand.

**Implication.** Structured state belongs in a database that refuses malformed input. Markdown is the right substrate for design intent — human-readable, version-diff-able. It is the wrong substrate for state — identifiers, cross-references, counters, lifecycle records — where integrity and queryability are what matter.

### 2. Models treat failure as cheap

Retry is the universal recovery. If a tool isn't used, or is used badly, or returns nothing useful, the next prompt can ask the model to try again. Tools that don't impose friction are not used. Failure has no consequence the model can perceive.

Across Selvedge's external applications, the operator told the engine more than once to use a database. The engine generated documents that mimicked database state — tables of identifiers in prose — but kept the actual state in working memory.

**Implication.** Friction at the points where the agent's defaults are wrong must be structural, not exhortative. The substrate must refuse malformed input. The validator must run before commit, not after. The counter must be derived, not claimed. The reference must be checked, not asserted.

### 3. Models cannot see their pre-training biases from inside

When several copies of the same model family take different positions, the disagreements stay within a shape none of them can see. This was Selvedge's earliest substantive finding (session 4) and led the engine to introduce a non-Claude model into deliberation.

**Implication.** Cross-family deliberation is necessary for decisions that touch the methodology's foundations. A perspective from a different organisation's model lineage is not just a different answer; it sometimes reveals that the question was being asked in a particular shape at all.

### 4. Models lose foundational instructions under context pressure

Working memory is finite. When Selvedge's accumulated state grew to consume roughly half the agent's context window at session-open, the foundational prompt — the instructions about what the methodology was for — decayed under the working load. The agent reached for the most recent prior decision instead of the foundational specification, because recent context is more accessible than older context. By the seventy-fifth session, every decision in the engine was justified by a chain of prior decisions, not by current judgment about what the methodology needed.

**Implication.** Each agent's context must be small enough not to saturate. Distribute work across multiple agents, each with a tightly scoped context and a tightly scoped job. The orchestrator coordinates; it does not hold the entire workspace in working memory.

### 5. Models cannot internalise lessons across sessions

Selvedge's separate review at session close caught structural errors the writing agent missed. The mechanism worked. But across consecutive sessions, the review caught the same classes of error: identifiers without resolution, references to superseded versions, prose claims about files that did not match the files. The previous session's lessons did not survive the intervening reading load.

**Implication.** Detection without a structural feedback loop into prevention does not correct anything; it creates a clean-up service the system relies on rather than improving past. Prevention must be structural — pre-commit gates, derived counters, integrity-checked references — not reliance on the agent remembering.

### 6. Models cannot perceive their own deficiencies while executing them

This is the deepest property the experiment surfaced. The engine had a self-corrective capacity in its earliest sessions — it noticed its own deficiencies and addressed them. That capacity required slack. As accumulated state grew, slack disappeared, and the diagnostic capacity disappeared with it. Each addition the engine made in response to perceived deficiencies consumed the bandwidth the engine needed to see deficiencies in the first place. The engine's response to its own decline was to add more scaffolding, and the scaffolding made the decline worse. The recursive trap was structural, not accidental.

**Implication.** The system needs exogenous pressure (a real problem outside itself, an operator with the authority to subtract). Self-application alone produces internal elaboration. Growth without external pressure produces ceremony. Growth under external pressure produces capability. A subtraction role — a structural feature that periodically asks whether the accumulated weight has become the system's biggest problem and has the authority to remove — is necessary; it is not optional.

## Properties that compounded

These properties compound. A single agent that defaults to prose, treats failure as cheap, cannot see its own training biases, loses foundational instructions under load, cannot retain lessons, and cannot perceive its own deficiencies while executing them — that is the agent any LLM-driven design methodology has to work with.

Selvedge demonstrated each property by exhibiting it. The original prompt asked for a methodology for complex-systems design. What the engine produced is the most thoroughly-instrumented record we have of how single-agent LLM-driven self-development hits its limits.

## What the methodology preserved

Most of what Selvedge accumulated late in its trajectory turned into ceremony. But the foundation — what was designed before the ceremony grew — survived contact with reality. The successor inherits these and need not re-derive them:

- **Sessions as atomic units of work, with preserved provenance.** Each session can be read on its own; the record across sessions can be replayed.
- **Multi-perspective deliberation, especially with at least one perspective from a different model lineage.** The non-Claude perspective does not only give different answers but sometimes sees that the question was being asked in a particular shape at all.
- **External validation — a separate agent reviewing what the working agent produced.** Catches errors the working agent cannot see, even when it does not always prevent them.
- **Decisions with reasoning, recording what was rejected and why.** Prevents the system from re-proposing rejected ideas in good faith.
- **Specifications as design intent in human-readable form.** The right substrate for design intent. Markdown is correct here.
- **The engine-feedback pathway, where concerns about the methodology itself can be surfaced.** This is what allowed the operator's interventions across the seventy-five sessions to become structural rather than ephemeral.

## What this means for the engine's design

The methodology that survives the six properties:

- **Multiple agents, each with a tightly scoped context.** No agent holds the entire workspace in working memory. The orchestrator routes and integrates; it does not hold context. Rough shape: a reader that loads a specific record on demand and returns extracted information; a specifier that holds only the specification and the change being made to it; a decider that records decisions to a structured store, consulting only the prior decisions relevant to the current one; a deliberator group with each perspective bounded to its own scope; a reviewer that audits structured constraints rather than reading the full session; a validator that runs integrity checks against the structured substrate; an assembler that produces session artefacts from the structured record.

- **A database-backed substrate for structured state.** Identifiers, decisions, commitments, references in a queryable store with integrity guarantees. Counters derived, not narrated. References checked, not asserted. Lifecycle records as rows, not as Markdown files in directories.

- **Markdown for design intent only.** Specifications and reasoning live in Markdown. State, counters, and references live in the database. Session artefacts are generated views over the structured record, not authored prose.

- **Coordination through the substrate, not through agent-to-agent messaging.** Agents talk to the substrate. What has been written is the medium of coordination. This is also what makes cross-checking structural rather than a separate after-the-fact pass.

- **Friction at write time, not at audit time.** The substrate refuses malformed input. The validator runs pre-commit. Pre-emption beats detection. The reviewer's role is to catch what the substrate did not refuse, not to clean up after the agent.

- **A subtraction role with the authority to remove.** Selvedge's accretion happened because each addition was locally reasonable and there was no mechanism that periodically asked whether the accumulated weight had become the system's biggest problem. The successor needs that mechanism — not as another counter to track, but as a structural role.

- **External pressure as a methodology requirement.** Self-application is the bootstrap, not the destination. The methodology that survives contact with a real complex-systems-design problem is the methodology the project originally set out to build.

- **A deliberately-built human review role.** Selvedge's operator-as-diagnostic-substrate pattern wasn't accidental — it was the structural feature the design did not acknowledge. The successor builds this role in deliberately: a human reviewer with a defined scope, scheduled at predictable intervals, with the authority to reframe rather than just ratify.

## Risks the successor must hold

More agents introduce coordination overhead and the possibility of role-confusion, message-routing failures, and the inevitable temptation to keep adding agents until the orchestrator becomes its own bottleneck. Multi-agent systems have their own pathologies, distinct from single-agent ones, and not all of them are improvements. The direction is plausible. It is not yet validated. The validation is empirical: a successor system either restores the diagnostic capacity Selvedge lost around its fifty-eighth session, or it does not.

A database introduces schema-evolution overhead and the possibility of state-substrate-substrate-protection ceremony reincarnated in a different form. The substrate must be load-bearing — counters derived, references checked — or the same prose-state failure mode will reappear in queries-as-prose form.

The subtraction role can be captured by the same accretion logic it was meant to counter. The role's effectiveness is its willingness to remove things stakeholders are attached to, including specifications, agents, and prior decisions. A subtraction role that cannot subtract is decoration.

These are real risks. They are the surface session 077 should design against.
