---
title: Methodology Kernel
version: 3
status: superseded
created: 2026-04-17
last-updated: 2026-04-20
updated-by-session: 011
supersedes: methodology-kernel-v2.md
superseded-by: methodology-kernel.md
superseded-by-session: 014
---

# Methodology Kernel

## Purpose

This specification defines the core process of the methodology: what happens during each application of the prompt, in what order, and to what standard. It is the minimum viable process — the kernel that every session follows. As the methodology matures, additional specifications may elaborate on individual activities, but this kernel defines the overall shape.

## Specification

### Application Model

The methodology advances by **sessions**. Each session is one application of PROMPT.md to the workspace. A session reads the full workspace state, determines what work is needed, does that work through multi-perspective deliberation, produces artifacts, and closes cleanly.

Each session advances the workspace by **one increment** — a coherent unit of progress that leaves the workspace in a better state than it found it. The size of an increment is a judgment call informed by the work at hand; it is not time-boxed.

### The Nine Activities

Each session performs nine activities. These are a **vocabulary, not a strict sequence**. They have a general flow (you cannot decide before you deliberate) but permit recursion (deliberation may reveal the need for more reading).

#### 1. Read

Absorb what the session will reason from before changing anything. In every session this includes **workspace reading**: the full current state of the workspace — every file, every specification, every provenance record, and, where relevant, recent version-control history. Build a complete picture of the workspace's own state.

When the session produces or revises an artefact intended for use outside the workspace, it also includes **domain reading**: the domain constraints the session operates under (stated by the user or operator in-session), cited external materials introduced into the session, and domain knowledge that the orchestrating agent surfaces explicitly as input to the work. Domain reading enlarges what must be understood; it does not permit silent import of outside ideas. Knowledge not already present in the workspace or in the session's explicit domain inputs must still be introduced through an explicit surveying or hypothesising step (per PROMPT.md). Perspective pretraining enters the session via stance briefs and perspective responses, not via §1 Read.

This is a receptive activity. Its output is understanding, not artifacts.

#### 2. Assess

Determine what state the methodology is in and what this session should address. State the determination explicitly so future sessions have a record of what was inferred.

Assessment questions:
- What is the most important work the workspace needs right now?
- Are existing specifications consistent with each other and with reality?
- Are there open issues that should be addressed?
- Is there work from a prior session that needs continuation?
- Is the methodology itself showing signs of strain (stale specifications, unaddressed issues, loss of coherence)?

This activity produces the session's **agenda**: a statement of what will be worked on and why.

#### 3. Convene

Assemble perspectives suited to the work at hand. Name each perspective, describe its stance, and record why it was chosen.

For deliberative work (where decisions will be made), at least one perspective must be **adversarial** — its role is to challenge the emerging consensus, identify unstated assumptions, and argue for alternatives.

The choice of perspectives shapes outcomes and should be treated as a design decision, not an afterthought.

When a decision meets the triggers defined in `specifications/multi-agent-deliberation.md`, perspectives must be instantiated as independent agents whose outputs are synthesised rather than as multiple voices produced within a single context. Decisions that meet those triggers but are made single-perspective anyway must record the reason.

#### 4. Deliberate

Reason together from multiple perspectives. Each perspective contributes its genuine position on the questions at hand.

Requirements:
- Perspectives state positions before hearing others (to prevent anchoring)
- Disagreements are preserved in the record, even when resolved
- Alternatives are articulated, not just dismissed
- Uncertainty is flagged explicitly

This activity produces the richest provenance. The record should capture not just conclusions but the reasoning that led to them.

#### 5. Decide

Make concrete decisions with rationale. Each decision records:
- What was decided
- Why (the key arguments that carried it)
- What was rejected and why
- What remains open

Decisions are distinct from deliberations. A deliberation explores options; a decision commits to one.

#### 6. Produce

Create or update the artifacts that the decisions warrant. This may include:
- New specifications
- Revisions to existing specifications
- Updates to open issues
- New workspace structure

Artifacts should be produced to the standard defined in their respective specifications (e.g., specifications have the required frontmatter and three sections).

#### 7. Validate

Validate the session's output at each level on which it makes claims. Two senses apply.

**Workspace validation** applies to every session. Check that:
- New specifications don't contradict existing ones
- Specifications describe the workspace as it actually is
- Provenance records are complete and well-formed
- Open issues reflect the actual state of uncertainty

**Domain validation** applies when a session produces or revises an artefact intended for use outside the workspace. Obtain evidence from the domain-actor who holds the problem the artefact addresses — the user of a sequence, the reader of a specification, the participant in a process, or an equivalent — that the artefact functioned for its intended use. Record who performed the validation, what was tried, what happened, and whether modifications were requested. Domain validation may complete out-of-session; when it does, the receiving session records the report and decides whether it triggers revision.

If either validation reveals problems, they are either fixed in this session (return to Produce) or recorded as open issues for subsequent sessions.

#### 8. Record

Commit provenance to the workspace. Ensure all deliberations, decisions, and the reasoning behind them are captured in the session's provenance directory.

This activity is about completeness and permanence. Nothing decided or considered in this session should be lost.

#### 9. Close

Verify the workspace is in a coherent state:
- All new and modified files are committed to version control
- SESSION-LOG.md is updated with this session's entry
- open-issues.md reflects any new issues or resolved issues
- A statement of what the next session should address is included in the session log or provenance

### Continuity Rules

- **Read prior provenance before proposing.** If an idea was considered and rejected in a prior session, do not silently re-propose it. Cite the prior rejection and explain what has changed.
- **Do not overwrite silently.** When a specification is revised, preserve the prior version and make the succession traceable.
- **Preserve all provenance.** Do not delete historical records, even when they feel outdated.
- **Leave coherent state.** If work cannot complete, commit what was produced, document the blocker, and close cleanly.

### Self-Hosting

The methodology is self-hosting: it evolves by applying its own process to itself. This means:
- The methodology's specifications are subject to the same deliberation, decision, and versioning processes as any other artifact
- The methodology can revise its own kernel (this specification) through a regular session
- Changes to the kernel are recorded in provenance like any other decision
- The kernel should be revised when the process it describes no longer matches the process actually followed, or when a better process is discovered

## Validation

To validate this specification:

1. Review the most recent session's provenance and check that all nine activities were performed (or that their omission was explained — e.g., Convene is not needed for pure validation work)
2. Check that deliberative sessions included at least one adversarial perspective
3. Check that decisions record rejected alternatives, not just the chosen option
4. Check that SESSION-LOG.md is up to date
5. Check that no provenance from closed sessions has been modified
6. Ask: did the session's Read activity successfully use prior provenance to understand past decisions? If not, the provenance format or depth may need revision
