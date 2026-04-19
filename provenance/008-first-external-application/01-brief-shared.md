---
session: 008
title: Shared Brief — First External Application Target Selection (Branch B)
date: 2026-04-19
status: finalised-before-launch
deliberation-anchor-commit: ddeb5172da8d79ff7c0cc9acaa9a9f2c4d3c2d4a
perspectives:
  - explorer (Claude Opus 4.7, subagent)
  - pragmatist (Claude Opus 4.7, subagent)
  - skeptic (Claude Opus 4.7, subagent, adversarial)
  - outsider (OpenAI GPT-5 via Codex CLI, non-Claude participant per D-021 Shape A)
note: |
  This brief's sections 1–6 are byte-identical across all four perspectives.
  The frontmatter above was added to the committed file for validate.sh
  check 8 compliance; it was NOT part of what perspectives saw during the
  independent phase (perspectives received section headings starting at
  "# Shared Brief — Session 008" through the role-specific stance section).
  Frontmatter is file-level metadata for provenance tracking, not content.
---

# Shared Brief — Session 008

**Notice to all perspectives.** This brief's non-role-specific sections (1–6) are **byte-identical** across all four perspectives (Explorer, Pragmatist, Skeptic, Outsider). Only the Role-Specific Stance section at the end differs. All perspectives answer the same design questions from the same stated context. Do not coordinate; do not seek external context beyond this brief; do not read workspace files during your reasoning.

---

## 1. Methodology Context

This workspace is building a design methodology in which diverse perspectives deliberate, produce durable specifications, and preserve the reasoning behind decisions (provenance) so future readers — human or agent — can reconstruct what was decided and what was considered. The methodology is self-hosting: it evolves by running its own process on itself.

The methodology proceeds in **sessions**. Each session performs a set of nine activities (Read, Assess, Convene, Deliberate, Decide, Produce, Validate, Record, Close). Each session produces one increment of progress.

The methodology has been exercised for seven sessions, all on its own infrastructure: bootstrap, validation tooling, multi-agent deliberation pattern, non-Claude participation mechanism, schema enforcement, triggers-met annotation, and external-application preparation. Session 007 concluded that the methodology has not yet been applied to any non-self problem and produced selection criteria, a selection mechanism, and a binding commitment for Session 008 to execute the first non-self application.

**The current session is Session 008. Its work-product is the first non-self application.**

## 2. Problem Statement — Target Selection under D-045 Branch B

Session 007 asked the user whether to name a specific target, delegate selection to the orchestrating agent, or rule out any domains. The user's response:

- No specific target in mind.
- **Delegates selection to the orchestrating agent** — Branch B of D-045.3 (user-ratified agent proposal).
- No domains ruled out beyond what D-046 already excludes.

Under Branch B, this deliberation must produce a shortlist of up to three candidate targets that meet D-046's selection criteria, plus one recommended pick with reasoning. The user will then ratify or reject before execution. The target — the domain and problem — will be the material on which the methodology is exercised for the first time outside its own infrastructure.

### D-046 — Selection Criteria (verbatim from Session 007's decision record)

A candidate target must satisfy all eight criteria to be selectable by the agent-selection path (Branch B). Criteria 1 and 8 are overridable only by user-direction (not applicable here — the user has delegated, not directed); criteria 2–7 are hard requirements.

1. **Bounded scope.** The target admits a first-session executable increment — Session 008 produces a concrete external artefact (specification, decision, deliberation-record, or design fragment) in one session without closing the entire problem. Open-ended first targets are disqualified. Multi-session continuation is expected; un-bounded scope is not.

2. **Reversibility / low stakes.** The first external artefact is advisory or sandboxed — failure of the methodology on the target cannot produce real-world harm. Commit-now irreversible targets (legal documents, safety-critical design, clinical decisions) are disqualified.

3. **Validate analogue required.** The target must admit a non-trivial Validate activity within the methodology's terms — a test, a peer-review pass, a pilot exercise, a reviewer panel, a reproducibility check, or a comparable domain-native mechanism. Targets where "validation" reduces to "does the spec read coherently" are disqualified.

4. **Mid vocabulary distance.** The target's vocabulary must differ from the methodology's native self-description (activities, specifications, provenance, deliberations, triggers, manifests) but overlap enough to translate.

5. **Externally legible.** The target's outcome must be readable and judgeable by someone outside this workspace who has not internalised the methodology's provenance. If the first external artefact is only interpretable by readers who have read the methodology's internal specs, no external evidence has been produced.

6. **Not pre-shaped by orchestrating agent.** If the target is selected by the orchestrating agent, the selection must visibly resist the agent's expected-to-succeed bias. Operationalised as: the recommended pick's selection record must name one target property the agent expected would be challenging, and the reason the agent proceeded nonetheless.

7. **Domain-accessible from available materials.** Session 008's work must be executable from a bounded brief plus materials the user can provide. It must not require fieldwork, proprietary data, gated external APIs, or physical artefacts the workspace cannot handle. Accessibility is a floor (work must be *possible*), not a ceiling (targets should not be chosen *because* they are easy); criterion 6 is the counter-weight.

8. **Software-adjacency ruled out of agent-selection default.** Domains whose vocabulary is software-design, tool-building, specification-management, or workspace-engineering are disqualified as agent-selection defaults. The methodology was built in a software-shaped workspace; success on software-adjacent targets is confounded with confirmation bias. (User-direction can override this, but the user has chosen to delegate rather than direct, so criterion 8 binds in full.)

### User context available to the selection

The user is the session operator (the methodology's author across Sessions 001–007) and works in a personal-knowledge environment that mixes development work, a personal-assistant project, and a vault-style note system. The "materials the user can provide" are therefore plausibly: notes, documents, personal project plans, articulated goals, reading or study interests, or artefacts from non-work domains the user pursues. What the user cannot provide: third-party-confidential data, credentialed external API access, physical samples, or time-bounded expert reviewers beyond the user themselves as first reader.

The user has not indicated their domain preference; the delegation is genuine. The candidates this deliberation produces should be framed at a level where the user can ratify a **domain-and-problem pair** (e.g., "a curriculum for topic X" rather than just "curriculum"), with one or two illustrative problem-shapes per candidate so ratification can be substantive.

## 3. Design Questions

Answer each question. Be concrete. Name and argue against plausible alternatives. Do not only state your preferred answer.

**Q1. Candidate targets.** Propose up to three candidate targets that meet D-046's eight criteria. For each candidate, specify:

- The **domain** (the kind of thing being designed) and the **problem** (the specific design task — concrete enough that the user could ratify or propose a variant).
- One or two illustrative example problem-shapes within the domain, so the candidate is not abstract.
- Which of D-046's criteria the candidate most clearly satisfies, and which is the weakest fit.

Do not pick three candidates from adjacent sub-domains of the same space (e.g., three kinds of curricula). If your candidates span three genuinely different domains, they form a usefully different shortlist for the user.

**Q2. Your recommended pick.** From your own three candidates (Q1), which would you recommend as the single pick for ratification, and why? Name the criteria the recommended pick handles best. Name one property of the recommended pick the selecting agent would expect to be challenging — a risk that the test may fail, a way the methodology's vocabulary may not translate, a place where Validate may strain — and argue why proceeding with this candidate despite that property is the right call for a first external target.

Be adversarial to your own recommendation in this question. If the challenging property is too load-bearing to proceed, say so and either demote the recommendation to a shortlist candidate or recommend a different candidate you hold less strongly but that clears the risk.

**Q3. Failure-modes on the recommended pick.** If Session 008 executes on your recommended pick and fails — the methodology produces an artefact that reads like methodology-talk wrapped around the domain rather than genuine domain work — what property of the target (not of the methodology) would you expect is the cause? Name at least two failure modes specific to this target, and what evidence would distinguish them from methodology failures.

This question serves two purposes: it forces honest thought about target-quality before commitment, and it gives Session 008's Validate activity a set of failure-hypotheses to probe.

**Q4. External legibility.** For your recommended pick, describe what the first external artefact will look like from the perspective of a reader who has never read this methodology's specifications. How will they judge whether the output is real work in that domain? What would make the artefact read as "this is a real design package for X" rather than "this is the methodology's internal processes narrated in the vocabulary of X"? Criterion 5 is the filter.

**Q5. What the agent might be pre-shaping.** The selecting agent has biases. Three are explicit and guarded against by criterion 8 (software-adjacency) and criterion 6 (expected-to-succeed). Others are not named. Identify one non-obvious agent bias that might shape which targets seem obvious — a prior that makes certain domains feel "natural" for methodology work in ways that do not survive scrutiny. Propose a candidate target (or rule out one that seems obvious) based on this scrutiny. You do not need to add this candidate to your Q1 shortlist; the purpose is adversarial space on agent-selection itself.

## 4. Response format

Produce a single Markdown response. Use H2 headings matching `## Q1` through `## Q5`. Under each heading, provide your answer with the arguments considered and the rejected alternatives. Target length: 300–600 words per question. Be concrete; use names and examples.

At the end of your response, include a short section `## Meta-note` of up to 150 words noting: (a) any position you hold that you expect to differ from what other perspectives will say, and why it is salient; (b) any assumption in this brief you flag as suspect; (c) any concern about the deliberation's framing.

## 5. Constraint on external imports

Reason primarily from this brief. Do not open workspace files. If an idea you want to use arrived through your pretraining, a real-world example, or an analogue from outside the methodology, flag it explicitly (e.g., "[external analogue: ...]") and argue why the analogue applies; do not silently commit external ideas as if generated from within the brief.

## 6. Closing note

Your response will be committed verbatim as provenance. It will be read by synthesis in conjunction with three other perspective responses. Your positions — including positions you hold reluctantly or conditionally — are recorded at their strongest. Do not soften them to anticipate synthesis. If you hold a position in tension with your role-specific stance, record the tension explicitly; the synthesis prefers honest tension to performed alignment.
