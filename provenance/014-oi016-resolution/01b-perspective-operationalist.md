---
session: 014
title: Perspective — Operationalist
date: 2026-04-22
perspective: operationalist
participant_kind: claude-subagent
model_family: claude
model_id: claude-opus-4-7
provider: anthropic
status: verbatim
---

## Q1. Selection criteria for a reference case

I want to answer Q1 by starting from the tooling that sessions actually have and the effort budget per session, then pulling out criteria that make sourcing tractable. Session cadence in this workspace runs roughly one session every few days; from the commit log I can see Sessions 008 through 013 spanned weeks. A reference-validation exercise that requires 40 hours of domain reading to set up will not happen. A reference-validation exercise that can be set up in a session-opening Read step — 30 to 60 minutes of fetch, summarise, constraint-extract — is one a session-author will actually run.

Concrete criteria, weighted by operational viability:

**(C1) The reference solution is fetchable as a single primary document via WebFetch, a public repository, or a PDF accessible at a stable URL.** The session-opener needs a canonical artefact to anchor comparison against. A domain where "the reference" is folk-practice distributed across ten community forums is not operationally viable inside a session. Viable sources in descending accessibility order: open-source reference implementations (GitHub, GitLab) — canonical, diff-able, versioned; standards-body documents (IETF RFCs, ISO, W3C, ANSI) — stable, numbered, structurally legible; peer-reviewed papers with supplementary code or data (arXiv, journal OA) — structurally legible, often carry the constraint-set in §2-3 and the solution in §4-5; historical engineering documents that survived into digitised form (NASA technical reports on NTRS, US Patent and Trademark Office filings, old IEEE Transactions) — well-indexed, stable URLs; canonical textbooks that present worked examples with full derivation (chapter-exercises with full solutions, not just answers). Community best-practice documents (blog posts, Stack Overflow accepted answers) are sourceable but fail C2 and C3 below.

**(C2) The constraint set is separable from the solution.** Operationally, this means I can read the reference document, extract a constraint list, and hand that list to the Produce agents without handing them the paragraph containing the solution. RFCs are good here — §1-4 typically state requirements, §5+ present the protocol. Papers are often good because abstract/introduction name the problem, methods section gives the solution. Textbook worked examples are mixed: sometimes the problem statement is intertwined with the walkthrough. Bad cases: domain wisdom documents where constraint and solution are co-stated ("do X because Y" — Y is the constraint, X is the solution, separable only with difficulty).

**(C3) The domain is not a top-1000 LLM training target.** I'm naming this as pretrained input: I'm borrowing from the **model-contamination / training-data-leakage** discussions in the LLM evaluation literature (cf. the MMLU contamination audits, the HumanEval contamination audits, and the broader conversation around benchmark leakage). Operationally this means: I should avoid domains where a Claude model can reproduce canonical solutions from memory. Red flags: Python standard library algorithms, introductory CS textbook exercises, any problem in the Cracking the Coding Interview / LeetCode canon, top-100-starred GitHub repos, OpenAI cookbook canonical examples, well-known textbook case studies (the MIT lock-picking protocol, the Toyota Production System canon, the Agile Manifesto). Green flags: niche standards (obscure RFCs that did not make it into production widely), regional engineering practices, documents paywalled or OCR-damaged such that they are likely under-represented in training corpora, domain-specific protocols in fields with small professional communities.

**(C4) The constraint set can be staged — not all constraints are visible up-front.** This is the required criterion per the user steer. Operationally, I need references where the reference document itself reveals constraints progressively, OR I can split a fully-specified constraint set into tranches without distorting the problem. Good candidates: (a) RFC revision sequences (RFC N says X, RFC N+1 adds constraint Y that breaks X, RFC N+2 resolves) — the constraints genuinely arrived over time historically; (b) post-mortem documents for engineering failures (the pre-incident brief is tranche 1, the incident facts are tranche 2, the retrospective constraints are tranche 3); (c) design-review documents where reviewer comments add constraints to an initial draft — the draft is tranche 1, reviewer comments are tranches 2..N, final spec is the reference; (d) protocol suites where the problem statement genuinely evolved (e.g., TLS 1.0 → 1.1 → 1.2 adding constraints as attacks were discovered). Staging is operationally achievable by the session-author writing a brief that releases constraints on a schedule — this is effectively a **scripted brief that gates constraint visibility**. I'll name this as the **adversarial-Gatekeeper agent pattern**, which I'm importing from the red-team / role-play evaluation literature: an in-session agent that holds the full constraint set and releases tranches on methodology-defined triggers (e.g., "release tranche 2 when Produce emits a first draft", "release tranche 3 when Validate raises its first finding"). This is an operational commitment — it requires a second agent with state and a disclosure schedule.

**(C5) Bounded effort to source.** Operationally: one session-opener (30-60 min of agent-time) must be sufficient to locate the reference, fetch it, and extract the staged constraint tranches. A reference requiring inter-library loan, archival research, or translation fails this criterion. Pragmatically this means: first reference case must come from a domain where a web-accessible canonical document exists. Budget: ≤3 WebFetch calls to locate, ≤1 primary document to download, ≤90 minutes agent wall-clock to extract constraints and draft the Gatekeeper schedule.

**(C6) The reference solution is structurally comparable at coarser grain than lexical.** I want Q2's comparison procedure to work on structure, not wording. Operationally this favours references that have named components, sections, or decision points that the produced artefact can be mapped onto. A pseudocode algorithm is more comparable than a prose essay. A numbered protocol is more comparable than a philosophical argument. A decision tree is more comparable than a worldview.

**(C7) Representativeness of the methodology's external-artefact claim.** Both existing externals (Session 008 Unfurl; Session 010 House Decision) are short-form procedural artefacts — sequences and decision protocols. The methodology's external-artefact claim is not "we produce production software" — it's "we produce short, situated procedures for humans to enact." Reference cases must be proportionate. A 400-page database-internals reference is not representative; a 10-20-step documented protocol is.

**(C8) Pass/fail legibility is achievable without a domain-actor.** The reference comparison must be tractable by methodology agents (Claude subagents plus one cross-model agent via codex exec). If distinguishing "our artefact is equivalent to the reference" from "our artefact is subtly non-equivalent" would require a domain expert, this reference fails. Operationally: the reference should have explicit structural checkpoints (a numbered protocol; a typed interface; a list of invariants) that a methodology agent can verify presence/absence of.

**Operationalising C4 (the staging requirement) in practice.** I propose the session-author builds a `brief-gatekeeper.md` alongside the shared brief. The gatekeeper brief contains the full constraint set, tagged into tranches:

- `tranche-0`: constraints released at session open.
- `tranche-1`: released when Produce emits first draft (trigger: artefact file exists at known path).
- `tranche-2`: released when Validate raises its first finding (trigger: validate report file exists).
- `tranche-3`: released if an iteration is entered (trigger: session re-enters Deliberate).

The Gatekeeper is a separate agent with access to the gatekeeper brief; the Produce / Validate agents do not. Produce/Validate agents receive tranches via explicit message-passing. This is a concrete, runnable pattern rather than an abstraction.

## Q2. The comparison procedure

A concrete run of the comparison from the tooling perspective:

**Phase A — Isolation of Produce (reference held by Gatekeeper).** The Produce agents are spawned (via TeamCreate, or sequential dispatch — TeamCreate if multi-perspective Produce is desired, single dispatch if not) with access to: the tranche-0 constraints from the Gatekeeper brief, the methodology kernel, relevant prior-session precedent from `methodology/` and `provenance/`. They do NOT have: the reference document, any URL pointing to it, the reference's domain-specific terminology that would enable retrieval from pretraining. The session-author's discipline here is scripted by a pre-commit check: before Produce is dispatched, grep the Produce brief for reference-identifying terms (title, author, URL, distinctive phrasing from the reference) and fail if present. This is a **golden-input hygiene check**, which I am naming as pretrained input borrowed from the golden-test pattern in software testing: the reference is the golden output; the Produce brief must not leak it.

Cost of Phase A: one to three agent dispatches (depending on whether Produce is parallel-perspective), each 15-30k tokens of context, 20-60 minutes wall-clock. Total token budget for a single-perspective Produce: ~50k input + ~20k output. Multi-perspective Produce (e.g., four perspectives as Session 014 itself does): 4x dispatch, ~250k total tokens.

**Phase B — Comparison tooling.** Once the artefact exists at a path like `provenance/015-first-exercise/02-artefact-produced.md`, comparison runs as follows:

1. **Structural decomposition.** A comparison agent reads both reference and produced artefact, decomposes each into a structural list: named components, numbered steps, invariants, decision points. Output format: a table with columns `reference-component | produced-component | correspondence | notes`. This is a single agent dispatch, 30-50k tokens.

2. **Component-level equivalence check.** For each row of the table, the comparison agent rates correspondence as one of: `exact-match` (semantic equivalence at the component level), `equivalent-variant` (different wording/ordering, same function and invariants), `partial-match` (overlapping but not equivalent; one covers a case the other doesn't), `divergent` (the produced artefact has a component that does different work), `missing` (reference has a component the produced lacks), or `extra` (produced has a component the reference lacks). This is rule-based grading, single agent.

3. **Constraint-satisfaction check.** Independent of comparison-to-reference, the produced artefact is checked against the full released constraint set (all tranches released by end of the exercise). Each constraint is tagged satisfied / partially-satisfied / violated / unaddressed. This is the **design-evidence check**: a produced artefact can diverge from the reference and still satisfy all constraints — that's a positive finding, not a failure. This is critical operational nuance per the user's co-design steer.

4. **Cross-model sanity pass.** A codex-exec call to GPT-5 with only the produced artefact and the constraint set (not the reference) asks: does this artefact satisfy these constraints? A Claude-only comparison can be self-serving; the cross-model check is cheap insurance. Cost: one codex invocation, ~20k tokens, 5-10 minutes wall-clock.

**(c) What counts as match / partial / divergence.** I'll name the grading thresholds operationally rather than by fiat:

- **Match (artefact-pass candidate):** all reference components have `exact-match` or `equivalent-variant` correspondence, AND all constraints in the released set are `satisfied` or `partially-satisfied`, AND the cross-model sanity pass concurs that constraints are met.
- **Substantive divergence with design-evidence:** one or more reference components are `divergent` or `missing`, BUT all constraints are `satisfied`. This is not a failure — it is evidence the methodology derived a different-but-valid solution. This requires explicit justification: the produced artefact's divergent component must be traceable to a decision in the methodology's Deliberate/Decide step, not to a gap.
- **Substantive divergence without design-evidence:** reference components are `divergent` or `missing` AND constraints are partially or wholly unsatisfied. This is the failure case; the produced artefact does not hold up independently and is not the reference.
- **Partial match:** mixed picture. Some correspondence, some divergence, mixed constraint satisfaction. Triggers iteration.

**(d) Iteration structure.** If Phase B yields partial-match or substantive-divergence-without-design-evidence, iteration rules:

- Iteration releases the next constraint tranche if one is held (this is the case when the methodology missed a constraint that was still tranche-gated).
- If all tranches are released and divergence remains, the comparison agent produces a **gap-surface report** naming what went wrong: was it a Read-step miss? A Deliberate-step blind spot? A Produce-step execution failure? This mapping to methodology steps is the co-design output.
- Iteration dispatches a new Produce with expanded context (prior Produce's artefact, the gap-surface report, newly released tranche if any) — but still NOT the reference.

**(e) Number of iterations before pass/fail.** Operationally bounded at 2 iterations per session (3 Produce attempts total). A third failed iteration triggers hand-off to a subsequent session (see Q3) rather than a fourth in-session attempt. Rationale: session wall-clock. Each Produce is 20-60 min; each comparison is 15-30 min; 3 Produce + 3 comparison = 2-5 hours, which is within a 3-6 hour session but leaves little time for the gap-surface report and closing discipline. Beyond that, sunk-cost dynamics set in — the session-author starts reaching for "good enough" heuristics to close the exercise, which corrupts the signal. Better to hand off.

**Total operational cost of one full exercise (Q2 budget summary):**
- Reference sourcing: 30-60 min wall-clock, 1-3 WebFetch calls.
- Gatekeeper brief construction: 30-60 min wall-clock.
- Produce Phase A: 20-60 min per iteration, ~50-250k tokens per iteration (depending on perspective count).
- Comparison Phase B: 30-60 min per iteration, ~50-100k tokens.
- Cross-model sanity: ~5-10 min, ~20k tokens.
- Close / gap-surface report: 30-60 min, ~20-40k tokens.
- **Full single-iteration exercise: ~2-3 hours, ~200-400k tokens, 2-5 tool calls.**
- **Full three-iteration exercise: ~5-8 hours, ~600k-1.2M tokens, 6-15 tool calls.**

Three-iteration exercises do not fit a single session; they require hand-off (see Q3).

## Q3. Shape of the validation step

I'm picking **(iii) Hand-off to a subsequent session**, with a constrained form of **(ii) iteration within a session** nested inside it — so strictly a hybrid with hand-off as primary shape.

My reasoning is cost-structural. Here's how the candidate shapes price out:

**(i) Multi-agent judging** on a completed artefact is expensive and, per the user's co-design steer, structurally wrong for this problem. A jury reviewing a finished artefact can only say pass/fail/close — it cannot help the methodology absorb emergent constraints because absorbing emergent constraints means re-entering Deliberate, not re-judging Decide. Multi-agent judging is a fait-accompli mechanism; we need an iterative one. Cost: 4 judges × 30-50k tokens each = ~150-200k tokens, 1-2 hours. I'd pay this cost only if the shape fit, and it doesn't.

**(ii) Iteration within a single session.** This is appropriate for the actual iteration loop but cannot be the whole shape. A session cannot absorb three Produce/Compare cycles plus the opening Read and the closing discipline within a 3-6 hour budget. At two iterations the session is already stretched; at three iterations the session-author is making compromises. Iteration-within-session is necessary for tight loops but insufficient as the container.

**(iii) Hand-off to a subsequent session.** Session N produces; Session N+1 validates and possibly iterates; Session N+2 closes or further iterates. Cost: distributed across multiple sessions, which is how this workspace actually operates. The methodology already treats cross-session hand-off as first-class (Session 013 received a Session 010 revision; Session 014 engages OI-016 which was opened by Session 013). Cross-session coordination overhead is a known quantity here. This shape aligns.

**(iv) Single-agent validation.** Cheap but lossy. No internal dissent mechanism. Fails the Outsider's "procedural self-deception" test trivially because a single agent can rationalise whatever outcome the session-author wants.

**(v) Something else.** I briefly considered a **standing validation team** — a persistent multi-agent configuration reused across exercises. Operationally this is attractive (amortised setup cost, consistent calibration) but introduces a cross-exercise contamination risk: a standing team that sees reference A then is asked to validate exercise B may carry learned priors. I reject this for now; may revisit in Session 017+.

**My chosen hybrid: Exercise-scoped hand-off with in-session iteration budget.**

Concrete shape:

- **Session N (Produce session).** Opens with Gatekeeper brief construction; runs Phase A (Produce, up to 2 iterations within this session budget); emits produced artefact + iteration log + gap-surface report if iterated. Does NOT compare against reference in-session.
- **Session N+1 (Comparison session).** Opens with Gatekeeper full-constraint reveal + reference reveal; runs Phase B (structural decomposition, component equivalence, constraint satisfaction, cross-model sanity); emits comparison report with pass / substantive-divergence-with-design-evidence / partial-match / fail verdict. If partial-match, triggers Session N+2.
- **Session N+2 (iteration session, if triggered).** Receives gap-surface; re-enters Produce with expanded context (but still does not have the reference in its Produce brief — reference access is the Comparison-session's privilege, not Produce's); emits revised artefact.
- **Session N+3 (second comparison, if triggered).** Re-runs Phase B on revised artefact.

**Hard stop: 2 Produce cycles, 2 Comparison cycles, so 4 sessions maximum per exercise.** Beyond that, the exercise is declared unresolved and becomes a methodology-gap finding.

**Roles and participation:**
- Produce session: 1-4 agents (session-author decides based on problem type). If parallel-perspective Produce is used, perspectives should mirror the methodology's existing pattern (architect / operationalist / skeptic / outsider, or a subset).
- Comparison session: 3 agents minimum. One **reference-faithful reader** (agent given reference and produced artefact, asked to rate correspondence). One **constraint-satisfaction reader** (agent given constraints and produced artefact, asked whether constraints are met). One **cross-model sanity** (codex exec to GPT-5, given constraints and produced artefact only, no reference). If the first two disagree materially (e.g., reference-faithful says "divergent" and constraint-satisfaction says "all satisfied"), a fourth **adjudicator agent** reads both subreports and produces the session's verdict — with dissent preserved.

**Cross-model participation.** Required in Comparison session. GPT-5 via codex exec serves as the contamination tripwire (per Q4). Optional in Produce session; if used, it goes in as one of the perspective agents.

**Convergence / sign-off.** The Comparison session closes with one of four verdicts in a file named `comparison-verdict.md`:
1. `pass` — artefact matches reference or satisfies all constraints with design-evidence for divergences.
2. `partial-match-iterate` — defer to subsequent session.
3. `fail-methodology-gap` — the produced artefact fails AND the failure is attributable to a specific methodology gap; opens an OI.
4. `fail-mechanism-probe` — the comparison procedure itself could not produce a confident verdict; opens a meta-OI on the mechanism.

**Dissent preservation.** If the reference-faithful and constraint-satisfaction readers disagree, both sub-reports are preserved verbatim in the session record, and the adjudicator's verdict explicitly names the dissent it overruled.

**Emergent-constraint handling in this shape.** The Gatekeeper brief from Q1 operates within the Produce session. The Gatekeeper releases tranches on methodology-internal triggers — not on Comparison-session findings, which would collapse the isolation. The Gatekeeper is the operational mechanism for emergent constraints; the Comparison session only verifies after the fact that the methodology handled the staged release well.

## Q4. Defence against pretraining-contamination / circularity

The operational signals that tell us the mechanism is working or broken:

**Contamination signal 1: cross-model convergence on reference-specific wording.** If Claude and GPT-5, separately given only the constraints, produce artefacts with distinctive phrases that match the reference's wording beyond what the constraints would imply, that is contamination evidence. Operationally: the Comparison session runs a **lexical-overlap check** — tokenise produced artefact and reference, compute Jaccard or Dice coefficient over n-grams of length 5-10, flag if >0.15 for unique-phrase n-grams. This is a one-script check (~5 min).

**Contamination signal 2: artefact reproduces reference's accidental structure.** References have accidental features — section numbering quirks, specific variable names, idiosyncratic ordering. If the produced artefact reproduces those accidentals absent a constraint requiring them, that is contamination. Operationally: the comparison agent tags each correspondence as `substantive-match` vs `accidental-match` and flags if the ratio of accidental-matches exceeds 2.

**Contamination signal 3: suspiciously fast Produce convergence.** If Produce achieves a reference-matching artefact in tranche-0 (no emergent constraints needed), that itself is a signal — the methodology wasn't actually challenged, suggesting the Produce agent retrieved rather than derived. Operationally: track **Produce-iteration count**. Pass-on-iteration-0 with exact-match correspondence is treated as **presumptive contamination** and the exercise is re-run with a paraphrased / transformed reference.

**Defences in order of operational cost:**

**D1. Reference selection gate (per C3 above).** Operationally cheap; enforced at Q1's sourcing step. But Claude's training data includes enough of the engineering and scientific canon that "obscure" is not self-enforcing. We need automated checking — which brings us to D2.

**D2. Pre-Produce contamination probe.** Before the Gatekeeper constructs tranches, a prelude step asks the target Produce model (in an isolated dispatch with a neutral prompt like "given the problem domain X and constraint Y_1, Y_2, ..., what solution patterns exist?"). If the model returns anything resembling the reference text verbatim, selection fails and a new reference must be chosen. Cost: one agent dispatch, 10-20k tokens, 10 min.

**D3. Reference transformation / blinding.** If the domain is contamination-risky but otherwise strong, the session-author transforms the reference before comparison: rename entities, change units, shift a time period, translate if relevant, re-order sections. The transformed reference becomes the golden input for Phase B; the original is kept in a separate file for audit. This is operationally expensive — 45-60 min of careful transformation per reference — and risks breaking the reference's internal consistency. Use sparingly.

**D4. Cross-model divergence as a contamination signal (per Q4 option iii).** Implemented as two Produce runs in parallel: Claude + GPT-5 (via codex exec). If outputs converge lexically on reference-text, contamination. If they diverge but both satisfy constraints, design evidence. Cost: 2x Produce cost, ~100-200k tokens total. Budget-wise acceptable but effectively doubles the Produce phase. I recommend running this on **every first-of-domain exercise** and **every third exercise thereafter** as an audit sample.

**D5. Structural-level comparison (per Q4 option iv).** Phase B explicitly separates lexical and structural correspondence; the artefact-pass verdict weights structural more heavily than lexical. Already baked into Q2's grading rubric. Cost: none additional.

**Operational audit trail that makes contamination detectable.**

Each exercise maintains a file `contamination-audit.md` with:
- Pre-Produce contamination probe results (D2).
- Lexical-overlap Jaccard / Dice scores (from Comparison session).
- Accidental-match ratio.
- Produce-iteration count and whether tranche-0 was sufficient.
- Cross-model divergence / convergence characterisation (if D4 was run).

This file is committed with the exercise. A session-author reviewing the audit trail should be able to answer "did contamination occur?" from the trail alone.

**Operational-signal threshold for "contamination not controlled":** if on any single exercise (a) Jaccard-unique-phrase > 0.15, (b) accidental-match ratio > 2, and (c) tranche-0 sufficient for pass — all three — the exercise is voided and the mechanism's selection step is reviewed. If two consecutive exercises hit this combination, the mechanism itself is provisionally falsified and OI-016 re-opens.

## Q5. Kernel §7 revision

Operationally, I want §7 to read as a runnable checklist, not a definition. The current text ends with "Domain validation may complete out-of-session; when it does, the receiving session records the report and decides whether it triggers revision." That's a clear operational instruction. Reference-validation needs similar operational clarity.

I propose reference-validation as a **third named sense** (not an extension of Domain validation, because the absence of a domain-actor is structurally different). The current §7 should be renamed something like "Validation — three senses."

**Proposed replacement text for §7 (operational register):**

```
**Validation — three senses.** When a session produces or revises an artefact, validation is the session's check that the artefact holds up outside the session's own context. Validation has three senses; a session uses the sense appropriate to what the artefact is for.

**Workspace validation** applies to every artefact. The session establishes that the artefact satisfies the constraints that were stated to the session. This is checked by the session's own perspectives (see §6 Deliberate) and is the minimum bar for session-close.

**Domain validation** applies when an artefact is intended for use outside the workspace by an identifiable domain-actor — the person who will use the sequence, read the specification, or participate in the process. The session obtains evidence from that domain-actor that the artefact functioned for its intended use. Record who performed the validation, what was tried, what happened, and whether modifications were requested. Domain validation may complete out-of-session; when it does, the receiving session records the report and decides whether it triggers revision. If no domain-actor is available for a given artefact, domain validation cannot be substituted by other means; the artefact is either produced under reference validation (below) or held back.

**Reference validation** applies when an artefact is intended to demonstrate the methodology's capacity to produce external artefacts in domains where a live domain-actor is unavailable. The session designs an exercise against a documented proven solution from a tractable domain, isolates the Produce step from the reference, stages constraints so not all arrive up-front, compares the produced artefact to the reference and to the full released constraint set, and records the result with a contamination audit.

Reference validation is run across a bounded set of sessions (see the reference-validation specification). A single reference-validation exercise's pass or fail is a signal about the specific artefact; the methodology's external-artefact claim is considered validated at the methodology level only when the cross-exercise pass-fraction meets the specified threshold. A first-exercise that surfaces a specific methodology gap is a legitimate output and does not itself falsify the mechanism; consistent failure patterns across exercises may.

Reference validation does not substitute for domain validation when a domain-actor is available; it is the validation sense used when one is not.
```

Notes on the revision:
- The phrase "domain-actor who holds the problem the artefact addresses" is retained in Domain validation — the phrase was accurate there, the issue was that §7 previously implied it was the only validation sense.
- Reference validation is given a lightweight summary in §7 and then deferred to a separate specification file (`methodology/reference-validation-spec.md`) containing the Q1-Q6 operational detail. This keeps the kernel readable and allows the specification to evolve with exercises without kernel churn.
- The closing sentence ("Reference validation does not substitute for domain validation when a domain-actor is available") is the procedural-self-deception guardrail: it prevents reference validation becoming a cheaper replacement for domain validation in domains where domain-actors do exist.

## Q6. Iteration and pass criteria — the three-level question

**(a) Artefact pass.** An artefact passes reference-validation when the Comparison-session verdict is `pass` per the Q3 shape: all reference components correspond at exact-match or equivalent-variant level AND all released constraints are satisfied or partially-satisfied AND the cross-model sanity pass concurs. A verdict of `partial-match-iterate` is a continue-state, not a pass. A verdict of `fail-methodology-gap` is a fail AND opens an OI. A verdict of `fail-mechanism-probe` is a meta-failure and escalates to reviewing the mechanism.

An artefact may also pass with a **design-evidence divergence** — where the produced artefact differs from the reference but satisfies all constraints with methodology-traceable justification. This is a qualified pass and is recorded separately; it counts toward methodology-level pass-fraction but is flagged in reviews as a case where reference and methodology-output diverged legitimately.

**(b) Methodology pass.** This is the number-of-exercises question. Here's my operational reasoning.

Session cadence: let's assume one session per 3-5 days based on observed commit history. One exercise = 2-4 sessions per Q3 hand-off shape. That's 6-20 days per exercise. Across a year, with interruptions, maybe 10-15 exercises could run — but exercises will not be the only work; OIs, revisions, methodology updates continue in parallel. Realistic annual exercise throughput: **6-10 exercises**.

Methodology pass needs to be a proportion that (a) takes a meaningful number of exercises to accumulate, (b) can survive a few mixed results, (c) is not so stringent that one bad exercise dooms the claim.

Proposal: **N = 5 reference cases, with 3 passes required (3 of 5)**. Rationale:
- 5 is enough to average out domain / reference-quality variance.
- 3 of 5 = 60% bar. Lower than 4 of 5 (80%) because the methodology is co-designing — early exercises are expected to surface gaps. Higher than 2 of 5 (40%) because below half is not a defensible claim.
- Timeline: 5 exercises at 6-20 days each ≈ 1-3 months of focused exercise work. Feasible within a year, and completable before the methodology's claims become stale.

However, the 3-of-5 bar applies only once per **methodology version**. Kernel revisions reset the count — a new kernel is a different methodology and owes new evidence. Operationally: the reference-validation spec includes a `methodology-version` tag on each exercise; passes accumulate against the tagged version.

A **partial-credit** rule: if an exercise fails with `fail-methodology-gap` and the subsequent session(s) produce the methodology fix, the re-run exercise (against the same or structurally-equivalent reference case) counts as 0.5 toward the pass threshold, not 1.0. This prevents gaming (fail deliberately → fix → count as pass).

**(c) Mechanism-failure vs methodology-gap distinction — the operational test.**

A **methodology gap** looks like this in practice:
- The Comparison-session verdict is `fail-methodology-gap`.
- The gap-surface report names a specific step (Read, Deliberate, Decide, Produce, Validate) and a specific failure mode (e.g., "Deliberate did not consider constraint C7 because the perspective lineup lacked a reader with domain-expertise X").
- A targeted kernel revision or perspective-lineup revision is proposable.
- A re-run exercise against a similar reference case (same domain, same constraint structure) shows the gap closed.
- The contamination audit for the failing exercise was clean.

A **mechanism failure** looks like this:
- Two consecutive exercises produce `fail-mechanism-probe` verdicts — i.e., the comparison procedure itself cannot produce a confident pass/fail.
- OR the contamination audit consistently shows signals (Jaccard > 0.15, tranche-0 sufficiency) on exercises that otherwise verdict `pass`, suggesting pass verdicts are driven by pretraining not methodology.
- OR cross-model divergence reveals Claude-subagents and GPT-5-outsider systematically disagree on artefact-pass in ways the adjudicator cannot resolve (>50% adjudication rate, persistent across exercises).
- OR the mechanism's judgments are indistinguishable from judgments on shuffled-constraint exercises — an audit where the Gatekeeper randomises which tranche-tag each constraint gets shows the pass/fail distribution doesn't shift. This is a **noise-floor check** borrowed from **null-hypothesis testing**, named as pretrained input: if the mechanism's signal is not distinguishable from noise, the mechanism is not discriminating.

**Concrete threshold for declaring mechanism failure:**
- 2 consecutive `fail-mechanism-probe` verdicts OR
- 3 of 5 exercises show contamination-audit signals above threshold AND pass verdict — i.e., passes are largely contaminated OR
- Noise-floor audit shows pass-rate within 15 percentage points of shuffled-constraint pass-rate.

Hitting any of these reopens OI-016 with the mechanism itself as the issue, and the methodology returns to the state Session 013 Skeptic named: producing external artefacts is paused pending a different mechanism.

## Q7. Risks and dissent

**Strongest operational failure mode.** The Gatekeeper goes feral. The session-author constructs the Gatekeeper brief and cannot help smuggling knowledge of the solution into tranche tagging. Tranche-2 "happens to" release exactly the constraint Produce was missing; tranche-3 "happens to" arrive at exactly the iteration point where Produce was about to fail. This is **experimenter-demand-characteristics contamination**, naming as pretrained input from the psychology-methods literature. The session-author is not adversarial; they want the exercise to succeed; they unconsciously stage releases that help. The result: passes are real but compressed — the methodology looks better than it is.

Second failure mode, specific to this cost structure: **exercise-throughput collapse**. Each exercise is 2-4 sessions at 3-6 hours each = 12-24 hours of work. Across a year the methodology produces 6-10 exercises. If the pass bar requires 5-of-5 for defensibility, and the first exercise fails with a methodology gap, a productive year produces maybe 3-4 exercises toward a pass threshold that requires 5. The methodology's external-artefact claim remains in limbo for a year or more. Session-author fatigue sets in — the third exercise skips the Gatekeeper brief, the seventh exercise reuses an earlier reference "to save time," the mechanism drifts back toward ritual compliance.

Third failure mode: **audit-trail rot**. The `contamination-audit.md` file is produced diligently for exercises 1-3, hastily for exercises 4-5, then forgotten. Without the audit trail, contamination signals go unmonitored. This is a standard **model-drift / monitoring-fatigue** pattern (naming as pretrained input from ML-ops).

**Explicit falsifiability condition.** If Session 015 (the first exercise) exhibits any of:
- Tranche-0 sufficient for pass AND lexical-overlap > 0.15 — retrieval, not design.
- Produce-session wall-clock < 30 min AND Comparison-verdict `pass` — too easy, either contaminated or the reference was trivial.
- Comparison-session adjudicator required AND adjudicated in favour of the reference-faithful reader over the constraint-satisfaction reader without a substantive methodology argument — the mechanism favours reproducing the reference over demonstrating design capacity.
- Cross-model (GPT-5 outsider) disagrees with Claude-subagents by >50% on the pass verdict — the Comparison session cannot converge cross-model, which means the mechanism's judgments are model-dependent rather than methodology-dependent.

Any one of these in Session 015 warrants a Session 016 audit of the mechanism before continuing.

**The "procedural self-deception" concrete observable.** The observable is **Produce-session session-author edits of the Gatekeeper brief mid-exercise**. If the session-author, during Produce, modifies the tranche schedule (moves a constraint from tranche-3 to tranche-1 because Produce "obviously needed it"), the exercise is contaminated by experimenter effect. The git log of the exercise directory is the audit trail: commits that touch `brief-gatekeeper.md` after Produce-session open are red flags. This should be a pre-commit warning.

Second observable: **the absence of `fail-methodology-gap` verdicts.** If 5 of 5 exercises pass, that is suspicious — the methodology is either miraculously complete (improbable, given it is co-designing) or the mechanism is tuned to produce pass. A healthy mechanism produces a mix of pass, partial-match-iterate, and fail-methodology-gap. If fail-methodology-gap never appears, the mechanism is ritual.

**Circumstances under which to fall back to pause.** Two triggers:
1. Session 015 hits the falsifiability conditions above.
2. By Session 020 (approximately 5 exercises in), the cross-exercise pass-fraction is not distinguishable from what a no-methodology baseline would produce — an audit where an agent is given constraints-only and produces the artefact without invoking the methodology. If the methodology's pass-rate is within 15 percentage points of this baseline, the methodology is not adding detectable value, and reference-validation does not matter because there is nothing to validate. Fall back to pause; reopen OI-016 with a different framing.

**Engagement with Session 013 Skeptic's strong-pause position.** The Skeptic's carry-forward names the structural gap: without a domain-actor, workspace-only validation is insufficient for external artefacts. Reference validation is an attempt to fill that gap without a domain-actor. My operational answer: it can fill the gap partially — it provides a signal about artefact adequacy that is stronger than workspace-only and weaker than domain-actor — but only if the contamination audit and cross-model divergence checks are maintained. If audit rot sets in (failure mode three above), reference-validation collapses to workspace validation with ceremony, which is exactly the procedural self-deception the Outsider warned about. The Skeptic's position should be preserved as first-class minority within the adopted mechanism: the mechanism is provisional; its adequacy is itself under test; the audit-trail and noise-floor checks are the tests; pause remains on the table if any of those tests fail.

On the Skeptic's undemonstrable-falsifiability concern from Session 013 — that the Skeptic's falsifiability criterion depended on a future domain-actor that the methodology has just ruled out — reference validation does not resolve this; it provides a replacement falsifiability path (the noise-floor audit, the contamination thresholds, the cross-exercise pass-fraction) which is weaker than domain-actor feedback but still testable. The Skeptic should probe whether these replacement falsifiability paths are themselves falsifiable or merely internal to the mechanism. My honest operational view: the noise-floor audit (comparing pass-rate to constraint-only baseline) is the strongest of these — it asks whether the methodology adds value independent of the mechanism. If it fails, pause is the right fallback and the methodology has learned something true about itself.
