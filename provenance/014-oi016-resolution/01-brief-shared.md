---
session: 014
title: Shared Brief — OI-016 Resolution Deliberation
date: 2026-04-22
status: pre-anchor
anchor-commit: PENDING
agenda: OI-016 resolution — design a reference-validation mechanism
ratified-agenda: user-ratified Option A with explicit steering toward a fourth option (reference-validation)
perspectives: [architect, operationalist, skeptic, outsider]
required-trigger: true
d023-triggers-expected: [d023_1, d023_4, likely d023_2]
carry-forward-minority: Session 013 Skeptic strong-pause position
---

# Shared Brief — Session 014

This brief is the full context for the four-perspective parallel deliberation on how Session 014 resolves OI-016. All four perspectives receive this brief verbatim. Outsider receives this brief plus a standard D-024 framing appended.

## 1. What this deliberation must produce

Session 014's decision surface is: **how does the methodology obtain validation for external artefacts now that the user is no longer available as domain-actor for new artefacts?**

The Session 013 Outsider framing offered three options: (a) recruit alternate domain validators; (b) label outputs as unvalidated; (c) pause external-artefact production. The user has **ruled out all three** and proposed a **fourth option**: reference-validation — pick a use case with a documented proven solution; run the methodology on constraints that stage in (not fully handed over up front); compare the methodology's produced artefact to the reference; use tooling and data sources as needed; treat iteration as expected; choose a validation-step shape (multi-agent judging, in-session iteration, next-session hand-off, single-agent, or other) suited to the methodology.

Each perspective must converge on a **concrete mechanism specification** or argue substantively against it. A perspective is not permitted to argue for (a), (b), or (c) as the session's resolution — the user has ruled those out. A perspective may argue that Option (d) as specified is inadequate and that OI-016 should remain open pending further user guidance; that is the escape valve if the mechanism cannot be specified robustly within Session 014.

## 2. User steering (verbatim)

Received at Session 014 open:

> Option A (OI-016 resolution). No external human recruitment is possible. Artefacts will need validation to prove the methodology. You are encouraged to use additional tooling and data sources to complete the validation. For example, pick a use case that already has a proven solution documented, and see if your methodology would have produced the same artefacts knowing the same constraints, understanding this may be an iterative process, and more multi-agent use may be required in the validation step for this reason.

Received as a follow-up steer during brief drafting:

> For question 3, I would add that multi-agent validation was a suggestion that might not fit your methodology; it's possible a validation step might require revisiting previous steps, or rely on another session to deliberate further, it can be solved multiple ways, this is up to you. Ideally your use case simulations imply you do not have all the constraints up front, and your methodology should be able to adapt, follow the process, and continue designing the best system; at the same time you are designing the methodology itself.

Key constraints and steers:

- **No human recruitment.** The methodology cannot solve the validation problem by finding different humans.
- **Artefacts need validation.** The methodology cannot solve the validation problem by not validating.
- **Tooling and data sources** are permitted (web, files, search, whatever is available).
- **Iterative** — comparison may fail initially; iteration is expected.
- **Multi-agent in validation is a suggestion, not a prescription.** Alternative shapes include: iteration within a single session that revisits prior Read / Deliberate / Decide steps; hand-off to a subsequent session for further deliberation; single-agent validation under stated conditions; something else. The deliberation chooses the shape and justifies it. Multi-agent may be right, may be overkill, may be inadequate — argue the position.
- **Reference cases should imply constraints that do not arrive all at once.** The reference-validation exercise should test the methodology's capacity to *absorb emergent constraints while producing the artefact*, not just its ability to reproduce a solution from a fully-specified brief. This is a substantive design requirement on Q1 (selection criteria) and Q2 (comparison procedure). A reference case that hands over a complete constraint list up-front is a weaker test than one where some constraints surface only partway through.
- **Co-design, not just test.** The methodology is being designed at the same time it is designing. A reference-validation exercise that surfaces a gap in the methodology is a legitimate outcome; the methodology should be able to respond to that gap in a subsequent session rather than treat the gap as falsification of the mechanism. The mechanism's pass criteria (Q6) must reflect this: a failed first-exercise that surfaces a specific methodology gap is not the same as mechanism failure.

## 3. Background context you need

### 3.1 Kernel §7 (current text, v3)

```
**Domain validation** applies when a session produces or revises an artefact intended for use outside the workspace. Obtain evidence from the domain-actor who holds the problem the artefact addresses — the user of a sequence, the reader of a specification, the participant in a process, or an equivalent — that the artefact functioned for its intended use. Record who performed the validation, what was tried, what happened, and whether modifications were requested. Domain validation may complete out-of-session; when it does, the receiving session records the report and decides whether it triggers revision.
```

Current §7 does not contemplate reference-validation. The language "domain-actor who holds the problem the artefact addresses" presumes a live domain participant. The user's proposed fourth option is not a domain-actor; it is a reference-solution comparison.

### 3.2 Existing external artefacts (n=2)

- **Session 008 Morning Unfurl** — movement sequence; single-user self-report Validate; reported "fine as-is."
- **Session 010 House Decision in Five Moves** (revised Session 013) — household decision protocol; single-user self-report Validate with four specific corrections; v2 produced but **not domain-validated**.

Both validations used the same shape: user tries the artefact in their life; reports back at subsequent session open.

### 3.3 Session 013 OI-016 text (abbreviated)

OI-016 was opened with four-perspective position spread (Reviser mild; Householder cautious; Skeptic strong-pause; Outsider policy-choice-required). Skeptic's strong-pause minority was preserved as first-class. Activation trigger was "first Session 014+ that proposes producing a new external artefact." Session 014 engages OI-016 **voluntarily** — no new external artefact is being proposed in Session 014 itself; the session's work-product is the mechanism specification.

### 3.4 Session 013 Skeptic carry-forward (full quote)

From `provenance/013-artefact-revision/01c-perspective-skeptic.md` Q6:

> The methodology's Session 009 revision recognised domain-validation as a distinct activity from workspace-validation. The kernel now depends on receiving a domain-validation signal to close the loop on external artefacts. Without the user-actor providing that signal, any artefact the workspace produces terminates at workspace-validation only, which is exactly the insufficient state Session 009 named. Producing a third external artefact under those conditions would be knowingly operating against the kernel's own definition of adequate validation.

The Session 014 Skeptic inherits this position at full strength and may extend it with new attack lines specific to reference-validation.

### 3.5 Session 013 Outsider "procedural self-deception" flag

The Outsider's Session 013 framing named the concrete risk:

> continuing as though the old validation loop still existed

A viable Session 014 mechanism must explicitly address this. A mechanism that looks like validation but isn't — ritual compliance with a renamed but substantively-unchanged gate — would earn the "procedural self-deception" label and fail at the level the Outsider named.

## 4. Questions for each perspective

Each perspective addresses all seven questions. Respond with concrete proposed text where asked; don't speak only at the meta level.

### Q1. Selection criteria for a reference case

What makes a use case a good candidate for reference-validation? Propose 5–8 concrete criteria. Address at minimum: documented-solution existence and accessibility; constraint-legibility (can the constraints be stated to the methodology cleanly without smuggling the solution); domain not saturated with Claude-family / GPT-family training data (to reduce pretraining contamination); domain-legibility to validation judges (human or agent); bounded effort; representativeness of the methodology's external-artefact claim.

**Required criterion per user steering:** the reference case should *imply constraints that do not all arrive up front*. A candidate where the entire constraint set is documented alongside the reference solution is a weaker test than one where some constraints surface only partway through the methodology's run (e.g., during Deliberate, or triggered by a Validate step's findings). Specify how you operationalise this — how Session 015+ would stage constraint release to the Produce agents without tipping the reference.

### Q2. The comparison procedure

Given a reference case selected per Q1, what is the concrete procedure that compares the methodology's output to the reference? Address at minimum: (a) how the methodology's Produce step is isolated from the reference (the agents producing the artefact must not have the reference in context, else this is retrieval, not design); (b) how the comparison is performed; (c) what counts as a match, a partial match, a substantive divergence; (d) how iteration is structured if the first comparison fails; (e) how many iterations before the artefact is declared either passing or failing.

### Q3. Shape of the validation step

Per the user's follow-up steer: multi-agent validation is **a suggestion, not a prescription**. Your task is to choose and justify the validation-step shape that best fits the methodology. Candidate shapes to consider — evaluate each and pick one (or argue for a hybrid):

- **(i) Multi-agent judging.** N judges (possibly cross-model), role-differentiated (reference-faithful-reader, methodology-sympathetic-reader, adversarial-reader), with convergence thresholds and dissent-preservation.
- **(ii) Iteration within a single session.** The validation finding triggers a return to Read / Deliberate / Decide within the same session; the session closes only when validation resolves or explicitly declares an unresolved gap.
- **(iii) Hand-off to a subsequent session.** Session N produces the artefact; Session N+1 performs validation (possibly with a different perspective lineup) and either accepts, requests revision, or escalates.
- **(iv) Single-agent validation.** One agent (possibly non-Claude) performs the comparison under stated conditions; lower overhead but weaker cross-view triangulation.
- **(v) Something else.** Name it, describe it, justify it.

For your chosen shape address: how many agents or sessions involved; what roles / perspective-lineups; cross-model participation (if any); convergence or sign-off criteria; dissent-preservation; what happens when validators disagree substantively; how the emergent-constraint steer from §2 interacts with the chosen shape (a multi-agent jury reviewing a fait-accompli artefact may be worse at handling emergent constraints than an iterative-within-session loop; the Skeptic will probe this).

### Q4. Defence against pretraining-contamination / circularity

This is the Skeptic's primary attack line. Specific risk: if the reference solution is in the Produce agents' pretraining, they reproduce it by retrieval rather than derive it through methodology-driven design. The mechanism then claims validation evidence that does not exist. Propose defences. Options to consider and evaluate: (i) select references explicitly outside common training distributions; (ii) blind the Produce agents to the reference (mask / transform / paraphrase it); (iii) use cross-model divergence as a contamination signal (if Claude and GPT-5 converge on the reference text word-for-word, that is contamination evidence; if they diverge but both satisfy the constraints, that is design evidence); (iv) require the comparison to be at a structural rather than lexical level; (v) something else.

### Q5. Kernel §7 revision

The current kernel §7 names two senses (Workspace validation, Domain validation). What revision does reference-validation warrant? Address: (a) should reference-validation be a third named sense, an extension of Domain validation, or a mechanism that informs Workspace validation; (b) what normative text; (c) what specifically changes about when the receiving session records the report and decides whether it triggers revision; (d) does the "domain-actor who holds the problem" phrasing remain accurate or require replacement. Propose concrete replacement text for §7.

### Q6. Iteration and pass criteria — the three-level question

Three distinct "pass" questions. Each perspective addresses all three.

**(a) Artefact pass.** When does a specific artefact pass reference-validation? State the criterion in terms appropriate to your Q3-chosen shape (e.g., judge concurrence threshold if multi-agent; resolution-of-divergence if iteration-within-session; subsequent-session-acceptance if hand-off).

**(b) Methodology pass.** When has the methodology accumulated enough reference-validation evidence that its external-artefact claim is supported? Propose N (number of reference cases) and fraction thereof that must pass before the methodology's external-claim is considered validated at the methodology level — distinct from any single artefact's pass.

**(c) Mechanism-failure vs methodology-gap distinction.** Per the user's co-design steer, a first-exercise that fails *because it surfaces a specific gap in the methodology* is not the same as mechanism failure — the gap is a legitimate output to be addressed in a subsequent session. Specify the operational test that distinguishes the two. What pattern of first-exercise findings would falsify the reference-validation **mechanism itself** (as opposed to surface a fixable methodology gap)? Examples worth considering: the mechanism cannot produce a pass/fail signal at all; the mechanism consistently returns pass on contaminated runs and fail on clean runs; the mechanism's judgments are indistinguishable from noise. Name the threshold concretely.

### Q7. Risks and dissent — substantive engagement required

This is where the Skeptic carries forward the Session 013 strong-pause minority and where the other perspectives must engage it rather than work around it. Each perspective names:

- **Strongest failure mode** for reference-validation as specified in their Q1–Q6 answers.
- **Explicit falsifiability condition** — if this observed in first-exercise (Session 015), the mechanism's adequacy is falsified and the methodology should return to pause.
- **The "procedural self-deception" test** — how would the perspective know the mechanism is ritual rather than substantive validation? Name the concrete observable.
- **Circumstances under which to fall back to pause.**

The Skeptic additionally: makes the strongest case **against** Option (d) being adequate under any specification. That case either carries the session to "OI-016 remains open pending further user guidance" or is preserved as first-class minority within whatever mechanism is adopted. Both outcomes are permissible.

## 5. Perspective roles

**01a Architect** — proposes the mechanism. Your Q1–Q6 answers are the mechanism's content; your Q7 engages risk.

**01b Operationalist** — makes it runnable. Focus on: token / wall-clock / tool-call cost per session; reference sourcing (where proven solutions come from in practice — papers, open-source, historical records, technical canon); tooling integration (web fetch, file analysis, search); failure handling; sustainability across N sessions.

**01c Skeptic** (adversarial) — carry forward Session 013 strong-pause. Primary attack: circularity / pretraining-contamination. Secondary attacks: reference-gaming, selection bias, reference-solution-quality variance, undemonstrable-falsifiability concerns from the Session 013 audit (the Skeptic's own C4 falsifiability condition depends on a future domain-actor that the methodology has just ruled out). **Take positions; don't only object.** A Skeptic who concedes every question to the others is not serving the role.

**01d Outsider** — cross-model perspective via `codex exec` to OpenAI GPT-5. Your role is especially load-bearing on Q4 (the circularity question is itself a cross-model question — if you and the Claude subagents both reproduce a reference, that is contamination evidence; if you diverge, that is design evidence). Bring your own angle on candidate references and selection criteria; your different pretraining may surface reference-pools Claude perspectives miss.

## 6. Output format

Each perspective produces a file at `01{a|b|c|d}-perspective-{role}.md` with:

```
---
session: 014
title: Perspective — {Role}
date: 2026-04-22
perspective: {role}
participant_kind: claude-subagent | codex-exec
model_family: claude | openai
model_id: claude-opus-4-7 | gpt-5.X
provider: anthropic | openai
status: verbatim
---

## Q1. Selection criteria for a reference case
[your proposal]

## Q2. The comparison procedure
[your proposal]

## Q3. Shape of the validation step
[your chosen shape with justification]

## Q4. Defence against pretraining-contamination / circularity
[your proposal]

## Q5. Kernel §7 revision
[your proposal; include concrete replacement text]

## Q6. Iteration and pass criteria
[your proposal for both (a) artefact pass and (b) methodology pass]

## Q7. Risks and dissent
[per instructions in §4.Q7]
```

Target length 2,500–4,000 words per perspective. Favour concrete over meta. Use literal quotes from this brief when disagreeing with its framing.

## 7. Participation anti-drift discipline

- **State your position before hearing others** (the parallel-dispatch design enforces this mechanically).
- **Preserve dissent in your own output** — if you hold a view the others will likely reject, state it at full strength and explain why.
- **Avoid brief-priming** — do not merely echo this brief's vocabulary back in your answers. The synthesizer will check for lexical-echo patterns (see Sessions 005, 006, 007 for prior findings).
- **Do not silently import external knowledge.** Per PROMPT.md's anti-silent-import rule, if you introduce a concept from your pretraining (e.g., a named validation technique from engineering or statistics), name it explicitly as pretrained input.
- **Engage the circularity concern directly.** Q4 is the deliberation's highest-stakes question; glib defences ("just pick obscure references") will be flagged by the synthesizer.

## 8. Anchor commit

This brief is anchored at commit `PENDING` (to be filled after commit, before the `codex exec` invocation for the Outsider). The Outsider's brief will cite the anchor hash as the anti-tampering witness. Claude subagents are dispatched in parallel from the same message as the `codex exec` call to make the parallel-execution window auditable.

## 9. Scope boundaries

Session 014 **does not** produce:

- An external artefact in `applications/` (mechanism specification is self-infrastructure).
- An actual reference-validation run (deferred to Session 015+ first-exercise).
- An OI-004 closure deliberation (criterion-4 articulation is a separate agenda not chosen).
- An OI-015 laundering-gap deliberation (separate agenda not chosen).
- A broader OI-005 sub-activity deliberation for kernel §2–§6, §8, §9.

Session 014 **does** produce:

- Mechanism specification (either as a new specification file, or as a section within an existing spec, or as a revision to kernel §7 — the deliberation decides).
- Kernel §7 revision if warranted.
- Workspace-structure update if the mechanism introduces new file-location conventions.
- OI-016 state change.
- Session 013 Skeptic carry-forward engagement.
- WX-14-N watchpoints for first-exercise monitoring.

## 10. Closing note

The user's steering narrows the option space but leaves the design space open. Reference-validation is a reasonable frame; it is not self-executing. The deliberation's work is to specify the mechanism in enough detail that Session 015 could exercise it without further design work. If any perspective concludes the mechanism cannot be specified robustly within Session 014, say so — the escape valve (OI-016 remains open pending further user guidance) is permissible.
