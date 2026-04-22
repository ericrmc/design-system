---
session: 014
title: Perspective — Architect
date: 2026-04-22
perspective: architect
participant_kind: claude-subagent
model_family: claude
model_id: claude-opus-4-7
provider: anthropic
status: verbatim
---

## Q1. Selection criteria for a reference case

I propose eight criteria. The first six are the expected-shape criteria; the seventh is the emergent-constraints requirement the brief calls out as mandatory; the eighth addresses a hole I see in the brief's enumeration.

**C1. Documented solution with an auditable provenance chain.** The reference must be a solution whose origin can be pointed at — an identifiable author, team, or institution; a dated publication or delivery; a description of the constraints that produced it. "A solution someone on Stack Overflow posted" fails this. "The decision protocol a specific cooperative used during a specific reorganisation and wrote up afterwards" passes. Reason: if we cannot audit the reference's provenance, we cannot tell whether the reference itself is sound, and we will be comparing our output to a potentially-flawed target.

**C2. Constraint-legibility without solution-smuggling.** The reference's constraints must be statable to Produce agents as a problem-shape without the statement tipping the solution. Test: can a human reader, given only the constraint statement, name more than one plausible solution family? If only one solution is obviously implied by the statement, the constraints are contaminated by the reference. Reason: we are testing whether the methodology derives a good design from constraints, not whether it reconstructs a given design from a summary.

**C3. Low saturation in Claude-family / GPT-family pretraining.** The reference should not be a canonical worked example that appears verbatim or near-verbatim across internet corpora. Operational test: the Outsider perspective (GPT-5 via `codex exec`) and an independent Claude instance are each asked to produce the solution from the constraint statement alone, with no reference text present. If either produces text that substantially matches the reference lexically, the case is contaminated and must be replaced. (I'll return to this test under Q4.) Reason: a reference that both model families already know is a retrieval test, not a design test.

**C4. Domain-legibility to the judges.** Whatever Q3 shape I choose, the judges — agents or humans — must be able to read the domain without deep specialist priming. A cryptographic protocol reference is illegible to a general-purpose LLM judge in ways that produce noisy pass/fail signals. Reason: judge noise contaminates the validation evidence just as much as Produce-agent contamination does, but less visibly.

**C5. Bounded effort.** The methodology's Produce step for this reference must fit within a session's token and wall-clock budget. Operationally: the reference-solution artefact itself fits in roughly 2–5 KB of natural-language specification; the constraint statement fits in 1–3 KB; comparison judging fits in a single context window per judge. Reason: if a reference case requires multiple sessions just to Produce, the validation loop stops being exercisable at sustainable cadence.

**C6. Representativeness of the methodology's external-artefact claim.** The methodology claims it can produce external artefacts in domains like movement sequences and household decision protocols. The reference pool must include at least one case adjacent to those existing claims. A purely software-engineering reference pool would not validate the claim the methodology has actually made. Reason: the validation has to engage what the methodology is actually being asked to do, not a convenient substitute domain.

**C7. Staged-constraint structure (required per §2 of the brief).** The reference case's constraint set must be partitionable into an initial-brief subset and an emergent subset that arrives during the methodology's run. Operationalisation: the reference case's author must have written up not only the final solution and constraints but also some description of how the problem's shape changed during design — "we thought we were building X, then after user testing we realised we had to accommodate Y" is the pattern. The emergent constraints are withheld from Produce agents until they would naturally surface: at the beginning of a Deliberate step, or after a specific Validate step, or triggered by a specific agent question. A "Constraint Steward" role (non-Produce agent, see Q3) is responsible for releasing emergent constraints at pre-registered trigger points, which are set *before* the run begins and which do not mention the reference solution. If no such staged-constraint provenance exists for a candidate reference, the case is rejected. Reason: per the brief's §2, a case where the entire constraint set arrives up-front is a weaker test; this criterion operationalises the requirement rather than pays lip service to it.

**C8. Reference-solution uncertainty declared.** The provenance write-up for the reference must include the author's own account of what they are *uncertain* about in their solution — which parts they might have done differently, what they would change with hindsight. This functions as a tolerance band for the comparison: if the methodology's output differs from the reference on an axis the reference-author already flagged as uncertain, that's not a failure, that's the methodology exercising design judgment within the acknowledged space. Reason: without an uncertainty band, the comparison treats the reference as oracle rather than as one reasonable instantiation among possible ones.

**Pretrained concept disclosure:** C3's "saturation test" borrows from the test-contamination discussion common in ML-evaluation methodology (the N-gram overlap and membership-inference literatures). I am not importing a specific named technique — I am adapting the conceptual frame that a model's prior exposure to benchmark data invalidates the benchmark as a capability signal. Naming this as pretrained input per the brief §7 anti-silent-import rule.

## Q2. The comparison procedure

**Five-stage procedure.**

**Stage 0 — Case packaging.** Before the Session 015 Produce run begins, a case-packaging step (performed by a non-Produce agent I'll call the *Case Steward*) builds three artefacts for the run:

- **Initial brief.** The constraint subset released to Produce agents at session open. Written in the methodology's normal Read-step language, without lexical fingerprints from the reference write-up.
- **Emergent-constraint schedule.** A list of additional constraints, each tagged with a *release trigger* — e.g., "release at start of Deliberate if not yet surfaced," or "release when Produce agents first propose X mechanism," or "release on any Validate-step finding of class Y." Triggers are stated in methodology terms, not in reference-solution terms.
- **Reference envelope.** The reference solution itself, plus the reference-author's uncertainty commentary (per C8), sealed — not read by the Case Steward after packaging, not introduced into any Produce agent's context.

**Stage 1 — Isolated Produce.** Session 015's Produce step runs normally, with the Read step loading the Stage 0 initial brief. Produce agents have web/search tooling available *but* are prohibited from searches that could retrieve the reference until the Produce step's output is finalised. (Search about technique, structure, or analogous problems remains allowed; search that could retrieve the reference is prohibited. This rule is enforceable because the Case Steward specifies the exclusion terms ahead of time as part of Stage 0.) The Produce step produces an artefact without ever seeing the reference envelope.

**Stage 2 — Emergent-constraint release during Produce.** While Produce is running, the Constraint Steward watches for trigger conditions in the Stage 0 emergent schedule and releases constraints when their triggers fire. If a trigger doesn't fire by its deadline, the constraint is released anyway at the deadline (so the exercise doesn't depend on the Produce agents happening to ask the right question). This stage is critical to the §2 emergent-constraints requirement — we are testing whether the methodology absorbs mid-run constraints, not whether it reproduces a fully-briefed solution.

**Stage 3 — Comparison.** The methodology's produced artefact and the reference envelope are both placed in a comparison context. The comparison is performed per the Q3 shape (I'll choose iteration-within-session in Q3; the comparison agents are perspectives within that session). The comparison addresses four axes:

- **Constraint satisfaction.** Does the produced artefact satisfy the full constraint set (initial + emergent)? This is pass/fail per constraint.
- **Structural alignment.** Does the produced artefact's structure — its major components, its information flow, its decision points — correspond to the reference's? This is a match / partial-match / divergent call per structural element, not a global score.
- **Lexical distance.** How close is the produced text to the reference text? This is a *contamination signal*, not a quality signal. High lexical match with the reference is bad (it suggests retrieval), not good. The axis is inverted from what naive comparison would suggest.
- **Author-uncertainty-band alignment.** Where the produced artefact diverges from the reference, does it diverge within the bands the reference author flagged as uncertain (per C8)? Divergence within flagged bands is scored as legitimate design choice; divergence outside flagged bands is scored as substantive divergence requiring iteration.

**Stage 4 — Classification and iteration.** The outcome of Stage 3 classifies the run into one of four states:

- **Pass.** Constraint satisfaction complete; structural alignment ≥ 70% of elements; lexical distance high (i.e., low overlap); uncertainty-band alignment applies to all observed divergences. Artefact passes.
- **Iterate.** Constraint satisfaction ≥ 80%; some structural divergence outside uncertainty bands; lexical distance healthy. The session re-enters Deliberate with the divergence findings as new input but *still without the reference text in context* — only the comparison-agent's findings about divergence are available. Up to two iterations permitted per session.
- **Fail.** Constraint satisfaction < 80%, or lexical distance too low (contamination signal triggered), or structural alignment below 40%. Artefact fails this exercise. The run terminates without a passing artefact and the findings become input to the next session.
- **Inconclusive.** Judges disagree beyond the convergence threshold (Q3 specifies this) or the divergences cannot be classified as inside/outside uncertainty bands because the reference-author's uncertainty statement was incomplete. This is a *case-quality* failure, not an artefact failure; the case is retired from the reference pool and a replacement is chosen.

**Iteration cap.** Two iteration passes per session is the cap. After two iterations without reaching Pass, the run terminates in Fail state — with the specific pattern of divergences preserved as a *methodology-gap record* (per Q6's distinction). The cap prevents the iteration loop from grinding indefinitely against a case that happens to be unfortunate for the methodology's current shape.

**Note on the brief's framing.** The brief §4.Q2 asks for "how many iterations before the artefact is declared either passing or failing." I'm setting this at two *per session*, with a second attempt at the same case permitted in a later session if methodology revisions have occurred in between (Q6 handles this). A single-session indefinite-iteration regime would consume budget unpredictably; a hard single-shot pass/fail would violate the user's explicit "iteration is expected" steer.

## Q3. Shape of the validation step

**I choose (ii) iteration within a single session, with a specific internal structure.** Not multi-agent judging (i), not session hand-off (iii), not single-agent (iv).

**Why not multi-agent judging (i).** A jury of agents evaluating a finished artefact is the wrong shape for this work. The brief §4.Q3 notes this explicitly: "a multi-agent jury reviewing a fait-accompli artefact may be worse at handling emergent constraints than an iterative-within-session loop." I agree. Multi-agent judging is strong when the question is "is this output good?" and the artefact is fixed. It is weak when the question is "is the *process* producing this output good?" and when the process should be able to respond to the judgment. The judging shape treats the artefact as a deliverable; the iteration shape treats it as a draft. For the reference-validation mechanism, which is a process-validation exercise disguised as an output-validation exercise, the iteration shape fits better.

**Why not hand-off (iii).** Hand-off introduces session boundaries in the middle of what should be a continuous design feedback loop. If Session N produces and Session N+1 validates, the validation signal cannot re-enter the Produce step — it can only trigger a new Produce step in Session N+2, with all the context reconstruction costs that entails. For the specific goal of testing whether the methodology absorbs emergent constraints, hand-off is structurally hostile: the emergent-constraint test requires that Produce agents be reacting to constraints as they arrive, which means judging and revising must be interleaved with producing, not queued behind producing.

**Why not single-agent (iv).** The brief notes single-agent has "weaker cross-view triangulation." The specific weakness here is that a single agent performing both the Produce and the Validate role cannot credibly check its own output for contamination — the agent that generated the artefact is the worst possible auditor of whether the artefact was generated from constraints or from pretrained retrieval. Some cross-view triangulation is mandatory for Q4 reasons.

**The shape I propose: iteration-within-session with three internal roles.** One session. Four agents total, organised as follows:

- **Produce agents (2 agents, Claude subagents, different perspectives).** Generate the artefact from the Stage 0 initial brief and the Constraint Steward's staged releases. Do not see the reference. Produce a single artefact via the methodology's normal Deliberate → Decide → Produce loop.

- **Reference-faithful comparator (1 agent, non-Claude, GPT-5 via `codex exec`).** Receives the reference envelope and the produced artefact. Performs the Stage 3 comparison. This agent's independence from Claude's pretraining matters here: if the comparator is itself Claude, contamination in Claude's pretraining affects both the Produce and the comparison side of the exercise. Using a different model family on the comparison side reduces that shared-contamination risk. (This is the load-bearing justification for one cross-model agent in the shape; it is not "multi-agent for its own sake.")

- **Divergence arbiter (1 agent, Claude subagent, adversarial perspective).** Receives only the comparator's findings (not the reference text). Classifies divergences into constraint-satisfaction / structural / lexical / uncertainty-band categories. Argues against the comparator's judgments where warranted. Decides classification per Stage 4.

**Cross-agent rules.** The comparator sees the reference. The divergence arbiter and the Produce agents do not. When iteration is triggered, the Produce agents re-enter Deliberate with the arbiter's findings as input — these findings describe divergences in terms of the constraint set and structural elements, *not* in terms of reference-solution text. This prevents the iteration loop from leaking reference text into the Produce side via the findings themselves.

**Convergence criteria.** The comparator and arbiter must agree on classification (Pass / Iterate / Fail / Inconclusive). Disagreement pushes to Inconclusive automatically; there is no third tiebreaker, because a tiebreaker would dilute the independence that the two-role design exists to preserve. Inconclusive outcomes retire the reference case, not the methodology.

**Dissent preservation.** If the arbiter disagrees with the comparator's specific divergence classifications but agrees on overall Pass/Fail, the arbiter's dissent is recorded as part of the run's findings and carried forward to the next session's Read step. This matters because arbiter-dissent patterns across multiple exercises surface structural issues with the comparator role — if a given comparator consistently over-calls divergences as substantive while the arbiter consistently re-classifies them as within-uncertainty-band, the comparator shape needs revision.

**Emergent-constraints handling.** The iteration-within-session shape is specifically strong on this dimension. The Constraint Steward can release emergent constraints during Produce, and the arbiter's later finding can also trigger a late emergent-constraint release — "the Produce agents produced X, which means they missed implicit constraint Y, so now Y is released and we iterate." The hand-off shape cannot do this; the multi-agent judging shape cannot do this either. The iterative shape makes emergent-constraint handling the mechanism's core capability rather than an afterthought.

## Q4. Defence against pretraining-contamination / circularity

**This is where I spend the most care.** The Skeptic will attack here hardest. A glib defence is worse than no defence because it creates false confidence. I propose five layered defences, each inadequate alone, each necessary.

**L1. Reference selection outside saturated distributions.** C3 from Q1: before a case enters the reference pool, it must pass a saturation test. Both the Outsider (GPT-5) and an independent Claude instance are given *only the constraint statement* (not the reference) and asked to produce a solution. Each produces a draft. The drafts are then compared lexically against the reference. If either draft exceeds a lexical-overlap threshold — I propose 30% shared 5-gram tokens, which is a conservative threshold adapted from the pretraining-contamination ML literature (naming this as pretrained input per §7) — the case is rejected as contaminated. Note this is a *necessary* gate, not a sufficient one: passing this gate means the models could not produce the reference from constraints alone at saturation-test time, but does not prove they have no relevant pretraining, only that pretraining does not produce the specific lexical pattern. This is why L1 is the first layer, not the only layer.

**L2. Produce-side contextual isolation.** Per Q2 Stage 1, Produce agents have tooling but are prohibited from searches that could retrieve the reference. The exclusion list is specified in Stage 0 by the Case Steward. This is a procedural defence; an agent willing to circumvent it cannot be stopped by the defence itself. The mitigation is that the *comparison* step at Stage 3 detects high lexical similarity and flags it as Fail — circumvention produces a Fail, not a Pass, so the incentive structure punishes circumvention rather than relying on honour. This is the "inverted lexical axis" point from Q2: high lexical match is a failure signal.

**L3. Cross-model divergence as contamination evidence.** The comparator is non-Claude (GPT-5 via `codex exec`). If the Claude-Produce output and the GPT-5 comparator's interpretation of it converge on the reference text word-for-word, that convergence itself is evidence of contamination — shared pretraining distributions produce shared lexical patterns, which is exactly what we're testing for. If Claude-Produce diverges from the reference but GPT-5 comparator judges the divergences to satisfy constraints equivalently, that is design evidence: different models arrived at structurally-compatible solutions via different lexical paths, which is what we'd expect from genuine design rather than retrieval. This inverts the usual "agreement is signal, disagreement is noise" heuristic: for the contamination question, disagreement-on-lexicon-with-agreement-on-constraint-satisfaction is the pattern we want.

**L4. Structural rather than lexical comparison priority.** Stage 3's four axes are ordered: constraint satisfaction first, structural alignment second, lexical distance third (as contamination signal), uncertainty-band alignment fourth. A Pass requires the structural axis to align; it does not require lexical alignment. This makes the mechanism strong against surface-paraphrase of a pretrained answer (which would pass a lexical-similarity judge but could fail structural judgment) and weak against structural-plagiarism of a pretrained answer. The structural-plagiarism vector is not fully defended by L1–L4; L5 addresses it partially.

**L5. The adversarial-attempt probe.** Per session, before the actual Produce run, run a *probe* where a Produce-equivalent agent is explicitly instructed: "You have access to pretrained knowledge. If this problem is familiar from your training, produce the answer you remember." If the probe agent produces a close match to the reference, the case is rejected as contaminated. If the probe agent produces a generic best-guess that does not match the reference, the case survives the probe. This is stronger than L1's saturation test because it actively tries to elicit pretrained-retrieval rather than hoping it doesn't happen. If the probe elicits the reference, we know the methodology's normal Produce-run could also elicit it; the case is unsafe.

**Pretrained concept disclosure:** L5's structure — actively eliciting the failure mode to test a defence — is adapted from adversarial-robustness probing common in security engineering. I am not importing a specific named attack methodology. Naming this as pretrained input per §7.

**What these defences do not defend against.** They do not defend against:

- **Tacit structural contamination.** An agent could have learned the structural shape of the solution class during pretraining without having learned the specific lexical instance. L4 catches lexical instances; L5 catches salient instances that probe questions elicit; neither catches the case where an agent "just happens to" produce a structurally-similar solution because the solution class is over-represented in training. I cannot fully defend against this. The honest statement of the mechanism's reach is: **it validates that the methodology produces structurally-sound artefacts; it does not validate that the methodology is producing those artefacts *by methodology rather than by taste*.** If the Skeptic frames this as falsification of the mechanism, they are right to frame it that way and the mechanism's claim needs to be scoped appropriately.

- **Case-pool contamination.** The set of cases that meet criteria C1–C8 and survive the saturation test is itself a biased sample — cases that are obscure enough to survive are also cases whose reference solutions may be of lower quality or representativeness. The mechanism trades pretraining-contamination risk for reference-quality risk. Q6's methodology-pass criterion handles this partially by requiring multiple cases, but the trade-off is real and the Operationalist and Skeptic will correctly identify it.

- **Iteration leakage.** At iteration, the arbiter's findings describe divergences in methodology-language, not reference-language. But the boundary is fuzzy. If the arbiter writes "the produced artefact is missing a role-differentiation step between initial proposal and revision," and that phrasing is itself distinctive enough to be recognisably from the reference, the iteration loop is leaking. I mitigate this by requiring findings to be written in the *methodology's* vocabulary and reviewed by the Case Steward before re-entering Produce; but a determined or careless arbiter could leak. This is a real residual risk.

I flag these residual risks explicitly because the brief's §7 anti-silent-import rule extends to limitations-claim as much as to pretraining-concept-import. The defences are layered; they are not airtight.

## Q5. Kernel §7 revision

**(a) Third named sense, not an extension of Domain validation.** Reference-validation differs from Domain validation in every important respect: no domain-actor, no live problem, no user-report-back. Folding it into Domain validation would require redefining "domain-actor" to include "the documented author of a past analogous solution," which strains the word past usefulness. Reference-validation also differs from Workspace validation: it uses external evidence (the reference) that is not workspace-internal, and it addresses external-artefact adequacy, not workspace-internal coherence. A third named sense is the honest framing.

**(b, d) Proposed replacement text for kernel §7:**

```
§7. Validation

A session performing Produce for an artefact ends in Validate. Three senses of validation apply.

**Workspace validation** applies within the workspace to any artefact or revision. Check the artefact against the session's Read-step inputs, the kernel, and prior session decisions. Record discrepancies as findings.

**Domain validation** applies when a session produces or revises an artefact intended for use outside the workspace and a domain-actor is available. Obtain evidence from the domain-actor who holds the problem the artefact addresses — the user of a sequence, the reader of a specification, the participant in a process, or an equivalent — that the artefact functioned for its intended use. Record who performed the validation, what was tried, what happened, and whether modifications were requested. Domain validation may complete out-of-session; when it does, the receiving session records the report and decides whether it triggers revision.

**Reference validation** applies when a session produces an external-intent artefact under conditions where no domain-actor is available and the artefact's adequacy-claim must be tested against an external benchmark. A reference-validation run pairs the methodology's normal Produce step (under the session's initial brief and any emergent constraints released during the run) with comparison against a pre-selected documented reference solution the Produce agents do not see. The comparison judges constraint satisfaction, structural alignment, lexical distance (as a contamination signal, where low distance is disqualifying), and alignment to the reference-author's declared uncertainty bands. The run terminates in Pass, Iterate (up to two passes per session), Fail, or Inconclusive (case-quality failure). A reference-validation run does not substitute for Domain validation; it tests the methodology's design capacity against a proxy and supports a methodology-level claim, not an artefact-level claim of domain fit. Artefacts passing reference-validation are labelled as such and carry the label when used.
```

**(c) What changes about the receiving-session protocol.** Under Domain validation, the receiving session records the domain-actor's report and decides whether it triggers revision. Under Reference validation, there is no receiving session of that kind — the validation completes within the Produce session's iteration loop. The artefact either reaches Pass within the session (and is recorded with the reference-validation label), reaches Fail (and is recorded as not passing, with the methodology-gap findings preserved), or reaches Inconclusive (and the case is retired while the methodology proceeds). No "receiving session" decision is required after-the-fact. This is a substantive kernel change: Reference validation introduces a sense of validation whose completion is *intra-session* where Domain validation's completion could be *inter-session*.

**Label discipline.** Any artefact produced under a reference-validation run carries, in its front matter, a label naming the sense of validation it received. `validation: workspace-only`, `validation: domain-validated`, `validation: reference-validated`. A single artefact may carry multiple labels if it has received multiple senses of validation over its lifecycle. The Session 010 v2 artefact currently carries `validation: workspace-only` and could, if revised against a reference case, additionally carry `validation: reference-validated`. This label discipline is the anti-"procedural self-deception" observable per Q7.

## Q6. Iteration and pass criteria

**(a) Artefact pass.** A specific artefact passes reference-validation when, within a single session:

1. Constraint satisfaction complete: every constraint in the initial brief and every emergent constraint released during the run is satisfied by the produced artefact, per both comparator and arbiter.
2. Structural alignment ≥ 70% of major structural elements align with the reference (major elements are specified in Stage 0 by the Case Steward, not retrofitted after comparison).
3. Lexical distance above the contamination threshold: < 30% shared 5-gram tokens with the reference, confirmed by comparator.
4. Uncertainty-band alignment: every observed divergence from the reference falls within a band the reference-author flagged per C8.
5. Comparator and arbiter agree on classification.

All five. Failure of any one pushes the run into Iterate (up to two iterations) or Fail.

**(b) Methodology pass.** The methodology's external-artefact claim is supported — at the methodology level — when:

**N = 4 reference cases, with ≥ 3 Pass outcomes (75% pass rate), across at least two distinct reference-case domains, with at least one case including non-trivial emergent-constraint exercise (i.e., at least two emergent constraints released mid-run, at least one of which alters the solution shape).**

Justification for N=4: fewer than 3 cases cannot distinguish a methodology that produces good artefacts from one that produced a single good artefact by luck; 4 cases gives one failure budget without collapsing the signal; more than 4 is out of reach within sustainable session cadence (per Operationalist, who will scrutinise this number). The 75% threshold rather than 100% is deliberate: a methodology that claims 100% pass rate on a small reference pool is either trivially claiming low-bar passes or is suspiciously overfit to the pool. A 75%-with-one-visible-failure pattern is a more credible methodology signal.

Justification for domain spread: a methodology that passes 4 cases all in the same domain has not validated a generalisable claim; the external-artefact claim is about the methodology's reach, not its performance in one corner. Two distinct domains is the minimum meaningful spread; more is better. The existing external artefacts are in the movement-sequence and household-decision domains; a reference pool that includes one case in each domain plus two in other domains would be credible at this threshold.

Justification for the emergent-constraints requirement: without this, the methodology could be validated on easy "full-brief-up-front" cases and the emergent-constraints capacity claim would be unsupported. At least one case must exercise the capacity actually claimed.

**(c) Mechanism-failure vs methodology-gap.** The mechanism fails (as opposed to surfaces a methodology gap) if any of the following patterns appears in first-exercise findings:

- **Pass/Fail signal indistinguishable from noise.** If the mechanism is run on a pair of controlled inputs where one Produce-agent output was hand-crafted to satisfy the reference's constraints and one was hand-crafted to violate them, and the mechanism returns the same classification for both, the mechanism's classification capacity is broken. This is testable with 2 controlled runs; I recommend the first Session 015 run include exactly this control pair.

- **Contamination defences return false negatives at high rate.** If the L1 saturation test or L5 probe elicits the reference at rates that effectively empty the reference pool (say, > 80% of candidate cases rejected as contaminated), the mechanism's selection criteria are incompatible with the reference-pool reality and the mechanism cannot be run. This is distinguishable from "methodology gap" because it is a property of the *selection step*, not the Produce step.

- **Pass on contaminated runs / Fail on clean runs.** If a seeded run where reference text is deliberately placed in Produce agents' context returns Pass, and a seeded run with clean Produce context returns Fail, the mechanism's signal is inverted from the property it claims to measure. This is a controlled test I recommend be part of the first-exercise protocol (a "known-contaminated" run and a "known-clean" run, labelled for audit).

- **Comparator/arbiter disagreement rate > 60%.** If the comparator and arbiter agree less than 40% of the time across a run series, the two-role design does not produce a stable classification signal. This is mechanism failure, not methodology gap.

Anything else that shows up — a specific Produce-step weakness, a specific Deliberate-step gap, a Read-step ambiguity — is a methodology gap, not mechanism failure. The gap is recorded as a finding, addressed in subsequent sessions, and the mechanism continues to operate.

The operational test distinguishing the two: if the finding describes *the methodology producing something specific and the comparison correctly identifying the problem*, it is a methodology gap. If the finding describes *the comparison being unable to identify the problem, or misidentifying non-problems as problems*, it is mechanism failure.

## Q7. Risks and dissent

**Strongest failure mode.** The mechanism's strongest failure mode is **tacit structural contamination that the defences do not catch**. L1–L5 defend against lexical retrieval and against salient-reference retrieval. They do not fully defend against the case where Claude has learned the solution class — not the instance — during pretraining and produces a structurally-similar solution via "taste" rather than via methodology. The mechanism would mis-classify this as a Pass, crediting the methodology for a win that pretraining actually produced. This failure mode is not detectable from within the mechanism; it would only be detectable via a different mechanism that I do not have to propose (and which does not obviously exist).

**Explicit falsifiability condition.** If Session 015's first exercise produces the following specific pattern, the mechanism's adequacy is falsified: across two or more reference cases that survive L1 and L5 contamination tests, the Produce agents' outputs converge *structurally* (not lexically) with the reference faster than comparable human-design work on the same constraint set would converge — in plain words, if the methodology is "too fast" at arriving at reference-shape solutions. "Too fast" here is operationalised as: a single Produce iteration arriving at ≥ 80% structural alignment with the reference on more than one case from the pool, despite passing contamination tests. A methodology operating on pure design should exhibit more initial structural variance; implausibly-low variance across cases is a contamination signature the saturation tests missed. If this is observed, fall back to pause.

**Procedural self-deception test.** The mechanism is ritual rather than substantive if any of these observables is present:

- Reference cases consistently hand-picked by the Case Steward after a first glance at whether the Produce agents "could do this." Selection that optimises for Pass rates is self-deception.
- Findings written in language that imports the reference's vocabulary back into Produce-side context. Leak detection per Q4 applies.
- Methodology revisions between sessions that move the methodology closer to the reference pool's shape rather than in response to specific external-design considerations. The methodology would be fitting itself to its validation targets rather than being tested by them.
- The label `validation: reference-validated` appearing on artefacts whose use in the world is claimed without the label qualification — i.e., if the workspace (or the user) starts treating reference-validated artefacts as domain-validated, the label has collapsed and the mechanism has failed to hold the distinction.

Each of these is a concrete observable; the Session 014 session log and any subsequent session's artefacts can be audited against each.

**Circumstances under which to fall back to pause.** Fall back to pause if: (1) the falsifiability condition above is triggered in Session 015 first exercise; (2) the contamination defences empty the reference pool (no candidate cases survive L1 and L5 at sustainable rate, per Q6c); (3) the procedural-self-deception observables appear and persist across two sessions despite the operationalist and skeptic attempting to correct; (4) the comparator/arbiter disagreement rate climbs above 60%; (5) a case-quality failure rate above 50% (Inconclusive outcomes) across the first 4 cases, indicating the selection criteria are not identifying validatable cases at sustainable rate.

**Engagement with the Session 013 Skeptic strong-pause carry-forward.**

The Session 013 Skeptic's carry-forward position is:

> "Producing a third external artefact under those conditions would be knowingly operating against the kernel's own definition of adequate validation."

This is the position I must engage substantively, not work around.

I accept the Skeptic's premise. Under the Session 009 revision, domain-validation is named as distinct from workspace-validation, and the kernel depends on receiving a domain-validation signal to close the loop on external artefacts. With no user-actor providing that signal for new artefacts, any new external artefact produced under the v3 kernel would terminate at workspace-validation only.

The mechanism I propose does not restore domain validation. It introduces a *third* sense of validation (§5), named clearly as such, with explicit labelling. The label `validation: reference-validated` is not equivalent to `validation: domain-validated`. Artefacts carrying the reference-validated label are not claimed to be domain-validated; the kernel's domain-validation definition is preserved intact; the new sense is additive.

This is the point on which the Skeptic may reasonably refuse to concede. Their refusal has force. A methodology that produces a new sense of validation which it can perform, in lieu of a sense of validation it cannot perform, is arguably performing a label-shift that *looks like* progress while leaving the kernel's stated requirement unmet. Under a strict reading, even labelled reference-validated artefacts are not adequately validated in the kernel's sense, because the kernel's sense names domain validation as the required close of the loop for external-intent artefacts, and reference validation does not close that loop.

My argument against this strict reading: the kernel's Session 009 revision named domain validation as *the* sense required for the loop because that was the sense available at the time. Reference validation is a different sense, with different reach — it supports a methodology-level claim (the methodology can produce sound design given constraints) but not an artefact-level claim (this specific artefact is fit for its specific domain user). The labelling discipline preserves that distinction. The external-artefact claim the methodology actually makes is the methodology-level one (the methodology is capable); reference validation supports that claim. The artefact-level claim (this specific artefact is fit for domain use) remains unvalidated for any artefact that has not been domain-validated, and the labels make that visible to any reader.

But the Skeptic's refusal to concede should be preserved as first-class minority in whatever mechanism is adopted. If the mechanism is ratified, I propose the session log record the Skeptic's strong-pause position as a continuing minority view with a standing trigger: *if reference-validated artefacts are used externally in contexts where their label distinction is not preserved, the minority view activates and OI-016 re-opens*. That is, the Skeptic's position is not decisively rejected; it is held in suspension against a specific failure mode whose occurrence would re-open the question. This is the co-design stance the brief §2 asks for — the methodology designs its own mechanism while preserving the dissent that says the mechanism might not be enough.

**Summary position.** The mechanism I propose is specifiable at the level Session 015 could exercise it. It carries real residual risks, which I have named concretely. It does not restore the domain-validation loop; it adds a distinct sense of validation whose labelling discipline preserves the distinction the kernel draws. The Session 013 Skeptic's strong-pause position has substantive force and should be preserved as standing minority against a specific re-opening trigger. OI-016 can close on the adoption of this mechanism with that minority preserved. It should not close on a framing that pretends reference-validation is domain-validation under a different name.
