---
session: 017
title: Shared Brief — OI-017 Engine-vs-Methodology Reframing Deliberation
date: 2026-04-22
status: committed (immutable from launch)
---

# Shared Brief — OI-017 Reframing Deliberation

The following sections are byte-identical across all four perspectives (Architect, Operationalist, Skeptic, Outsider). Only the role-specific stance — delivered separately to each perspective — varies.

---

## 1. Methodology context

You are a perspective in a deliberation run under a design methodology informally called **Selvedge**. Selvedge is self-hosting: it evolves its own specifications by running its own multi-perspective process on itself. Each session is one application of its bootstrap prompt (`PROMPT.md`); 16 sessions have been completed to date, with 6 active specifications, 13 active open issues, and 2 external artefacts.

### 1.1 — Active specifications (what exists today)

- **`PROMPT.md`** (9 KB). The bootstrap prompt. Frames the workspace as "building a design methodology." Uses the word "methodology" in two distinct senses: (a) abstract-approach ("The methodology itself — the mechanic of diverse perspectives reasoning together, producing durable artefacts, preserving their reasoning, and evolving the system by running the same mechanic on its own outputs — is domain-general"), and (b) concrete-implementation ("This workspace is building a design methodology"). The conflation is currently implicit.
- **`specifications/methodology-kernel.md`** v4. Defines the nine-activity execution semantics: Read, Assess, Convene, Deliberate, Decide, Produce, Validate, Record, Close. §7 Validate names three senses (Workspace, Domain, Reference).
- **`specifications/workspace-structure.md`** v2. Defines top-level directories (`PROMPT.md`, `SESSION-LOG.md`, `open-issues.md`, `specifications/`, `provenance/`, `tools/`, `applications/`). `applications/` holds external-intent artefacts; it was added in Session 009.
- **`specifications/multi-agent-deliberation.md`** v3. Defines when multi-perspective deliberation is required, non-Claude participation mechanism, per-participant manifest schema, synthesis discipline.
- **`specifications/validation-approach.md`** v3. Two-tier validation: `tools/validate.sh` (automated structural checks) + guided-assessment questions.
- **`specifications/identity.md`** v1. Names the methodology **Selvedge** (from the textile term for a self-finished edge). Created Session 012.
- **`specifications/reference-validation.md`** v1. Defines reference-validation as a third sense of validation. Created Session 014; un-exercised.

### 1.2 — External artefacts produced by the methodology to date

- `applications/008-morning-unfurl/morning-unfurl.md` — a movement sequence for a stiff lower back. Produced Session 008; Domain-validated by the user (Session 009).
- `applications/010-household-decision-protocol/house-decision-five-moves.md` v2 — a household decision protocol. Produced Session 010 (v1), revised Session 013 (v2) per user Validate feedback; v2 is not Domain-validated (user is unavailable for further validation; this triggered OI-016 and the reference-validation mechanism).

### 1.3 — The operator's Session 016 reframing proposal (verbatim, preserved)

> "The workspace has been developed as a methodology, but a reframing is offered for examination. The work produced across sessions may be better understood as an engine — a defined series of inputs, procedures, and outputs — rather than a methodology in the abstract. Under this framing, the workspace contains at least two applications of the engine. The first and foundational application is the engine's own development, which is what every session so far has produced. Subsequent applications apply the engine to external problems, using the same engine definition to generate domain-specific artefacts. Two structural consequences follow, offered as input rather than direction. First, the engine's current executable definition may benefit from being distinguishable from the provenance of its development, so that other applications can load the engine without loading its development history. Second, different applications likely require different execution prompts — the existing PROMPT.md drives the engine's self-development application, and applications against external problems may need a distinct prompt that loads the engine definition plus the relevant application's own context. Whether these observations are accurate, which to act on, in what order, and in what form are for the engine to determine. Any file in the workspace, including PROMPT.md, may be modified if the engine determines it appropriate."

### 1.4 — Session 016's surveying findings (summarised — full text at `provenance/016-operator-reframing-assessment/00-assessment.md` §3)

Session 016 surveyed the word "methodology" across all 6 active specifications and identified a latent two-sense usage (abstract-approach vs. concrete-implementation). Related framings from other traditions: specification-vs-reference-implementation; interpreter-vs-interpreted-program (closest fit); build-system-vs-built-artefact; meta-circular evaluator; framework-vs-application; method-vs-methodology-vs-methodological-framework; language-vs-specification-vs-implementation.

### 1.5 — Session 016's three hypotheses

Session 016 §4 produced three competing structural hypotheses. They are the preferred starting point for this deliberation, but additional hypotheses are permissible if argued.

- **H1 — No reframing.** Retain current framing; record the reframing observation as clarifying prose without specification changes. Minimal revision cost; latent ambiguity remains.
- **H2 — Full reframing.** Split `PROMPT.md` into engine-prompt + development-prompt (or single file with internal branches); add an engine-definition manifest naming the loadable engine; rename or retitle `methodology-kernel.md` as `engine-kernel.md`; update `workspace-structure.md` to distinguish engine-definition / development-provenance / application-scope file classes; update `identity.md` to say Selvedge names the engine; specify an application-initialisation pattern. High revision cost; full separation of concerns.
- **H3 — Partial reframing.** New `engine-manifest.md` specification naming the engine-definition files without renaming or moving them; minor updates to `identity.md` and `PROMPT.md` acknowledging the two application kinds; no split of `PROMPT.md`; no rename of existing files. Medium revision cost; addresses observation (1) but not fully observation (2); lets the first actual external application drive the rest of the restructure.

### 1.6 — Operator preference (Session 017 open steering)

The operator stated: "Continue with OI-017 as preference (full reframe)."

This expresses a preference for H2. Per the operator's Session 016 framing ("no stake in the specific shape of any resolution"; "for the engine to determine"), the preference is input, not a binding direction. **Your task is to reason independently for the hypothesis you are assigned to defend, regardless of operator preference.** If the operator's preference is wrong, say so; the methodology is designed to resist operator-preference anchoring.

### 1.7 — Relevant open issues

- **OI-004 (cross-model perspective participation).** Closure criteria 1, 2, 3 satisfied; criterion 4 unmet. This deliberation is D-023-triggering (kernel revision plausible); the Outsider participant's presence keeps OI-004 in active practice.
- **OI-015 (laundering enforcement gap).** Domain input must not be absorbed silently as given context. Operator preference is domain input; if your reasoning converges on H2, the synthesis will check whether convergence is reasoning-led or preference-primed.
- **OI-017 (this deliberation's subject).** Engine-vs-methodology reframing; three hypotheses enumerated above; additional hypotheses permissible.
- **`identity.md` Reopening condition 1 (external adoption threshold, unmet).** No named practitioner outside the operator has used the methodology for 3+ months on their own work. This is a live condition the Skeptic perspective in particular will emphasise. Pre-specifying external-application scaffolding before external adoption has occurred is one of the design risks this deliberation must weigh.

---

## 2. Problem statement

**Should the workspace adopt the engine-vs-methodology reframing, and if so, in what shape?**

The question is structural, not terminological. At stake:

- Whether the workspace's executable definition (the engine) is distinguishable from its development provenance as a loadable unit.
- Whether different kinds of application (self-development; external-problem) require different execution prompts, or whether one prompt with appropriate framing suffices.
- Whether a new specification (`engine-manifest.md` or equivalent) is needed to name what constitutes the engine at any version.
- Whether `identity.md` should treat Selvedge as the engine's name, the methodology's name, or both.
- Whether external-application initialisation is an engine-level concern worth pre-specifying now, or a concern that should wait until an actual external application is being launched.

**The workspace is being asked this question for the first time in Session 017.** Sessions 001–016 accumulated the structural ambiguity; Session 016 surfaced it; Session 017 decides what to do about it.

---

## 3. Design questions

Address each in your response.

- **Q1.** Should the workspace adopt a reframing? State your assigned hypothesis (or, for Outsider, your independently-reached position) and give your strongest reasoning for it, including the main cost of adopting it.
- **Q2.** If reframing is adopted, which existing specifications need to change, and in what shape? Identify specific files and specific changes; be concrete.
- **Q3.** How should `PROMPT.md` be reorganised under your position? (Split into multiple files / single PROMPT.md with internal branches / no change / other.) Give the reasoning.
- **Q4.** Should a new specification (`engine-manifest.md` or similarly-named) be created? If yes, what does it contain at minimum? If no, why not?
- **Q5.** How does the reframing interact with `identity.md`'s Selvedge naming and its four Reopening conditions? Does Selvedge name the engine, the methodology, both? Does adopting H2 or H3 trigger any Reopening condition?
- **Q6.** What is the activation path for external applications under your position? How does someone else initialise a fresh application workspace? (Be specific: what files, what structure, what initial state.)
- **Q7.** State the strongest argument AGAINST your assigned position. What evidence or observable condition, if it occurred, would cause you to abandon your position in favour of a competing one?

---

## 4. Response format

- **Length target:** 800–2,000 words total across all seven questions.
- **Structure:** One heading per question (`## Q1 — [your one-line summary]`); body prose under each.
- **Voice:** first-person reasoning ("I argue", "In my view"). No bullet-lists unless a list genuinely enumerates (e.g., Q2's file-by-file changes). Prose preferred over tabular output.
- **Dissent content:** Q7 is mandatory; state a real counter-argument with real operational conditions, not a rhetorical concession.
- **Concrete over abstract:** when naming files or changes, use the actual filenames (e.g., `methodology-kernel.md`, not "the kernel"). When proposing content, quote or specify the language you would adopt.
- **Uncertainty:** flag explicitly where you are uncertain. `[uncertain]` tags are welcome.

---

## 5. Constraint on external imports

You are reasoning from this brief and the workspace specifications it cites. If an insight arrives from your pretraining (e.g., a framework you know from outside this workspace), you must introduce it as an **explicit input** to your reasoning, not as given context. Flag pretrained inputs with `[pretraining: <brief summary>]` and then either use them as one option competing with others or discard them. Silent import of pretrained ideas — absorbed as "what I already know" — violates the methodology's anti-silent-import discipline (`PROMPT.md` §Rules that hold across applications) and the OI-015 laundering-enforcement concern.

Examples of legitimate use: "[pretraining: the interpreter/interpreted-program distinction from programming-language design] maps closely to H2's engine/application split; one difference worth weighing is…"

Examples of violations: "Obviously the right structure is a framework + application split" (pretraining smuggled as obvious).

---

## End of shared brief

Your role-specific stance follows in the separate message delivered to you. Respond per §4 format. Your response will be committed verbatim to the session's provenance as `01{letter}-perspective-{role}.md`.
