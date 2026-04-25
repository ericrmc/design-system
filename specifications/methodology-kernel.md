---
title: Methodology Kernel
version: 6
status: active
created: 2026-04-17
last-updated: 2026-04-26
updated-by-session: 063
supersedes: methodology-kernel-v5.md
---

# Methodology Kernel

## Purpose

This specification defines the core process of the methodology: what happens during each application of the prompt, in what order, and to what standard. It is the minimum viable process — the kernel that every session follows. As the methodology matures, additional specifications may elaborate on individual activities, but this kernel defines the overall shape.

This specification defines the Selvedge methodology kernel: the abstract execution semantics that a conforming engine must realise. `specifications/engine-manifest.md` enumerates the files that constitute the current engine; `specifications/identity.md` establishes the denotation layering (Selvedge names the methodology; "Selvedge engine" denotes the current executable implementation; each session is an application of that engine). The kernel applies equally to the self-development application and to external-problem applications.

## Specification

### Application Model

The methodology advances by **sessions**. Each session is one application of PROMPT.md to the workspace. A session reads the full workspace state, determines what work is needed, does that work through multi-perspective deliberation, produces artifacts, and closes cleanly.

Each session advances the workspace by **one increment** — a coherent unit of progress that leaves the workspace in a better state than it found it. The size of an increment is a judgment call informed by the work at hand; it is not time-boxed.

### The Nine Activities

Each session performs nine activities. These are a **vocabulary, not a strict sequence**. They have a general flow (you cannot decide before you deliberate) but permit recursion (deliberation may reveal the need for more reading).

#### 1. Read

Absorb what the session will reason from before changing anything. In every session this includes **workspace reading** of the default-read surface: the active specifications (per `specifications/engine-manifest.md` §3), the dispatcher and executable prompts (`PROMPT.md`, `prompts/development.md`, `prompts/application.md`), the `SESSION-LOG.md` index, `open-issues/index.md`, every prior session's `03-close.md`, and every file in the current session's provenance directory. The enumeration is specified in `specifications/read-contract.md` §1 and is closed — a file not on the default-read enumeration is archive surface.

The **archive surface** (raw perspective records from closed sessions, superseded specification versions, over-budget annotations preserved as archive-packs per `read-contract.md` §4) is read by explicit reference as the session's work requires; it is not default-read. A session relying on an archive-surface record for a load-bearing claim cites it via the `[archive: path]` convention (`read-contract.md` §6), and either reads the cited chunk(s) in full or declares in the session's honest-limits section why the chunk was not read and what gap that leaves. Silent non-reads of relevant archive records are a validation concern per `validation-approach.md` v5 Tier 2 Q9.

Build a complete picture of the workspace's default-read surface and of any archive-surface material the session depends on.

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

Validate the session's output at each level on which it makes claims. Three senses apply: two primary (Workspace, Domain) and one provisional substitute (Provisional reference substitute).

**Workspace validation** applies to every session. Check that:
- New specifications don't contradict existing ones
- Specifications describe the workspace as it actually is
- Provenance records are complete and well-formed
- Open issues reflect the actual state of uncertainty

**Domain validation** applies when a session produces or revises an artefact intended for use outside the workspace and a domain-actor is available. Obtain evidence from the domain-actor who holds the problem the artefact addresses — the user of a sequence, the reader of a specification, the participant in a process, or an equivalent — that the artefact functioned for its intended use. Record who performed the validation, what was tried, what happened, and whether modifications were requested. Domain validation may complete out-of-session; when it does, the receiving session records the report and decides whether it triggers revision.

**Provisional reference substitute** (formerly "Reference validation" at v5 and earlier) applies when a session produces an external-intent artefact and no domain-actor is available. It is a *provisional substitute* for Domain validation, not an equal-but-distinct third sense of validation. A reference-validation exercise — the procedure by which the substitute is produced — pairs the methodology's Produce step (run blind against a staged constraint tranche set whose emergent constraints surface during the run) with comparison against a pre-selected documented proven solution the Produce agents do not see. The exercise runs across a small number of sessions in a sealed three-cell protocol (Curation, Produce, Validation) specified in `specifications/reference-validation.md`. The exercise records constraint-satisfaction, structural correspondence, cross-model divergence, and a contamination audit. Any citation of reference-provisional evidence as support for a methodology-level claim must accompany the citation with at least one named contamination or scope-limitation risk (per `reference-validation.md` §8 label discipline).

**Scope and citation discipline for Provisional reference substitute.** Reference-provisional evidence is qualified by the candidate's saturation profile. It supplies evidence about the methodology's capacity to derive an artefact under stated constraints **only to the extent that the reference is not recoverable from shared pretraining corpora across the Produce and judging families.** It does not establish that the artefact functioned in its intended use. It does not substitute for Domain validation when a domain-actor is available. A passing reference-provisional result in a domain where cross-family-symmetric reproduction was observed at any stage of `reference-validation.md` §1 C3 is not methodology-level evidence; it is at most methodology-consistent evidence. A reference-provisional artefact MAY be cited as methodology-capacity evidence. It MUST NOT be cited as evidence of domain function. It MUST carry the `validation: reference-provisional` label; label transition to `validation: domain-validated` occurs only upon subsequent Domain validation. When a domain-actor later becomes available, Domain validation supersedes and the artefact's label transitions.

**Label grandfathering.** Artefacts produced under kernel v3/v4/v5 (Sessions 009–032) that carry `validation: reference-validated` in frontmatter are semantically-equivalent-to `validation: reference-provisional` for citation purposes; no retroactive rewriting of sealed session records. New artefacts produced from engine-v6 adoption onward use the `validation: reference-provisional` label.

**Distinct-reviewer mechanism for triggered surfaces (added engine-v11 Session 063 per D-228).** At session close, when any of the Layer 2 trigger conditions in `validation-approach.md` v6 §Tier 2.5 fires (engine-definition-touching session, substantive-arc-class session, Layer 1 (α) WARN/FAIL, (z5) lifecycle event, or operator-discretionary), the workspace produces a cross-family reviewer audit at `provenance/<NNN-session>/04-tier-2-audit.md`. The reviewer is non-Claude family per `multi-agent-deliberation.md` v4 §Heterogeneous-Participant Recording Schema; the audit shape and discipline are specified in `validation-approach.md` v6 §Tier 2.5. This mechanism supplements Tier 2 self-assessment by the orchestrator agent for claims about unresolved validation debt, substantive progress, engine-definition change, and repeated warnings — the surfaces where self-assessment was empirically insufficient per the S051-S058 honest-limit chain pattern that EF-058-tier-2-validation surfaced. Routine workspace claims (Tier 2 Q1-Q9) may remain self-assessed per the principled-asymmetry articulation in `validation-approach.md` v6 §Principled Asymmetry.

If any validation reveals problems, they are either fixed in this session (return to Produce) or recorded as open issues for subsequent sessions.

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
