pt reference-validation only as a blinded, staged-constraint, structurally scored, cross-model audited protocol. If Session 015 cannot distinguish design from retrieval, this mechanism is not a substitute for the lost loop; pause should return.

## Q1. Selection criteria for a reference case

I do not accept a literal reading of “produce the same artefacts” if “same” means textual sameness. For outsider purposes, exact wording overlap is often a warning, not a success condition. A good reference case is one where structural adequacy can be tested without smuggling the answer.

Criteria:

- The case must have a documented final artefact and independent evidence that it was actually used or accepted. A blog post praising a solution is not enough; there must be a primary artefact plus evidence of uptake, outcome, or revision history.
- The case must support staged constraint release. Before Produce begins, a curator must be able to divide the case into at least three packets: `P0` initial brief, `P1` mid-course constraint surfacing, `P2` late constraint or exception. `P0` should contain no more than roughly 60 percent of the final constraint set.
- Each packet must be solution-blind restatable. If a constraint can only be expressed by borrowing the reference’s order, labels, or phrasing, the case is disqualified because the constraint is already carrying the answer.
- The case must be low-saturation in common model training distributions. Avoid famous frameworks, benchmark-like tasks, widely taught checklists, canonical case studies, viral blog posts, and heavily repeated prompt fodder. Prefer long-tail operational documents, local or domain-specific process artefacts, revision-tracked institutional materials, or recent low-circulation sources.
- The case must be judge-legible. A validator who did not produce the artefact must be able to say what counts as success, what the mandatory elements are, and where equivalence is plausible. If only insiders can tell, the comparison becomes taste-based.
- The case must be bounded. One preparation session should be enough to build the packet set, reference seal, and rubric; one produce session plus up to two revision cycles should be enough to close the case. If the case needs a week of archival research, it is too large for mechanism testing.
- The artefact type must be representative of the methodology’s actual external claim. Good candidates are procedures, protocols, decision aids, structured sequences, checklists, or concise specifications. Bad candidates are trivia-like puzzles, purely aesthetic outputs, or tasks where “correctness” is just answer-key matching.
- The case must admit falsification. There must be explicit mandatory constraints, explicit optional elements, and explicit failure conditions. If every divergence can be explained away as “another valid approach,” the case cannot validate anything.

Operationalising staged release:

- `P0` contains problem statement, actor/context, and initial constraints only.
- `P1` is released either after the first complete draft or when producers explicitly request missing operational information.
- `P2` is released only after the first validation finding or when the draft encounters a known exception class.
- The packet schedule is sealed before Produce. It cannot be improvised later to rescue the artefact.

Candidate pools I would actively prefer: low-salience operational redesigns with revision history, migration or incident-response procedures with issue chronology, and institutional process artefacts that show late-emerging exceptions. I would actively reject famous productivity systems, canonical design methods, or any reference I can plausibly reconstruct from prior training alone.

## Q2. The comparison procedure

I am explicitly importing four pretrained concepts here: `holdout set` and `contamination canary` from ML evaluation, `separation of duties` from assurance practice, and `process tracing` from causal/process analysis. Those concepts fit this problem directly.

Procedure:

1. A curation cell selects the case and creates a sealed case pack.
2. The sealed pack contains the source artefact, evidence it worked, a packetized constraint chronology, a structural rubric, and a contamination-risk note.
3. The Produce cell receives only `P0` plus the standing methodology rules. It does not receive the reference, the full chronology, or the rubric.
4. Producers must emit two things each round: the artefact and a short constraint-to-decision trace explaining why each major feature exists.
5. `P1` and `P2` are released only by precommitted triggers. A validator who has seen the reference may not directly brief producers; any relay must be rewritten into constraint language, not solution language.
6. Once a produce round is frozen, the validation cell opens the reference and scores at the structural level.

Isolation rules:

- No agent may both read the reference and participate in Produce for that case.
- No comparison rubric is shown to producers.
- No validation memo may mention reference ordering, wording, labels, or distinctive motifs; it may only state missed constraints, unsupported assumptions, or unmet functional requirements.

Comparison method:

- Score mandatory constraint satisfaction.
- Score structure: sequence, decision points, branching, exception handling, and closure conditions.
- Score operational fit: whether the artefact can plausibly be enacted under the stated constraints.
- Score trace adequacy: whether the produced rationale is explainable from the released packets.
- Check contamination indicators separately: lexical overlap, rare-label overlap, unexplained specificity, and inclusion of details not present in released constraints.

Outcome classes:

- `Match`: all mandatory constraints satisfied, no fatal contradiction, structural score at or above 80/100, and no unresolved contamination signal.
- `Partial match`: all safety-critical or core mandatory constraints satisfied, structural score 60-79/100, and divergences are repairable without changing the problem framing.
- `Substantive divergence`: any mandatory miss that breaks function, structural score below 60, incompatible problem framing, or contamination indicators strong enough that similarity cannot count as design evidence.

Iteration:

- Maximum three produce rounds total: initial attempt plus two revisions.
- A failed round produces only a constraint-delta memo, not a reference-informed rewrite brief.
- If round one fails because `P1` or `P2` surfaced a genuine methodology gap, that is a legitimate output, not automatic mechanism failure.
- After round three, close the case as `pass`, `fail`, or `unresolved methodology gap`.

## Q3. Shape of the validation step

I choose a hybrid that is not identical to any one candidate: a `sealed three-cell protocol` combining hand-off across sessions with multi-agent judging.

Why not single-session iteration? Because once the same deliberative unit has seen the reference, contamination and anchoring pressure are hard to reverse. Why not single-agent validation? Because the whole point of Q4 is triangulation across model families and roles. Why not pure multi-agent judging in one room? Because role separation matters more than headcount.

Shape:

- Cell 1: `Curation`. One or two agents prepare the sealed case pack and packet schedule.
- Cell 2: `Produce`. One methodology-following agent or small team designs blind against staged constraints.
- Cell 3: `Validation`. Three judges compare output to the sealed reference.

Validator roles:

- `Reference-faithful reader`: maps the actual reference into the rubric.
- `Methodology-sympathetic reader`: asks whether the artefact is a defensible design response to the released constraints.
- `Contamination auditor`: looks specifically for retrieval signals, leakage, and solution-shaped packet wording.

Cross-model participation is mandatory in Cell 3. At least one Claude-family and one OpenAI-family participant must be present in validation. On this question, same-family agreement is weaker evidence than cross-family agreement.

Sign-off criteria:

- Pass requires at least 2/3 structural agreement and no unresolved contamination dissent.
- Any judge may file a blocking contamination dissent if they can point to reference-specific features not derivable from released constraints.
- All dissents are preserved verbatim.

When validators disagree:

- If the disagreement is about structural equivalence, the case may proceed to another produce round with a constraint-delta memo.
- If the disagreement is about contamination, the default is no pass. Ambiguity on contamination should not be resolved optimistically.

Session shape:

- Session N prepares the case and may run the first blind Produce.
- Session N+1 validates.
- If revision is warranted, Session N+2 re-runs Produce blind against the next packet or delta memo.

This fits the emergent-constraint requirement better than a one-shot benchmark. It lets late constraints arrive without allowing the reference itself to leak backward into design.

## Q4. Defence against pretraining-contamination / circularity

This is the load-bearing part. My view is blunt: “just pick obscure references” is not a defence. It only lowers prior probability.

Defences I would require:

- Low-saturation case selection. Necessary but insufficient.
- Strict blinding of Produce. Mandatory.
- Structural rather than lexical comparison. Mandatory.
- Cross-model divergence analysis. Important, but only as a signal, not proof.
- Contamination canary runs. Before adopting a candidate case, give thin prompts derived from `P0` to at least two model families. If they spontaneously emit the reference’s idiosyncratic structure, labels, or sequence, discard the case.
- Unexpected-detail rule. If a produced artefact includes a specific feature present in the reference but absent from all released constraints, count that as contamination evidence unless producers can justify it from generic domain logic.
- Process-trace requirement. Producers must explain why each major element exists. If an element matches the reference but lacks a constraint-grounded rationale, similarity does not count as validation evidence.
- Distinctive-marker audit. Validators should explicitly list rare markers in the reference: branded labels, unusual ordering, arbitrary counts, non-obvious wording, signature metaphors. Reproduction of those markers is more probative of contamination than broad structural resemblance.

How to interpret convergence and divergence:

- If Claude and GPT independently reproduce reference wording or rare structure from `P0`, that is contamination evidence, not a triumph.
- If they diverge lexically and structurally but both satisfy the released constraints and map cleanly onto the reference at the rubric level, that is the strongest design evidence available in this setting.
- If one family converges suspiciously and the other does not, treat the case as contaminated for that family and do not count it as a clean validation pass.

What I will not accept is a pass based on “close enough to the reference” when the closeness lives in names, slogans, or quirky formatting rather than functionally necessary structure.

## Q5. Kernel §7 revision (include concrete replacement text)

Reference-validation should be a third named sense, not a rename of Domain validation. The current phrase “domain-actor who holds the problem” is accurate for live use but inaccurate for reference comparison. Keeping them separate prevents category error.

Proposed replacement text for §7:

```text
**Validation** records evidence about whether an artefact is adequate for its claimed use and what revision, if any, follows from that evidence.

**Workspace validation** applies to the session's internal product. Record whether the artefact is coherent with the read set, the stated constraints, and the session's own decisions, and whether the session judges it ready for external testing or further revision.

**Reference validation** applies when a live domain-actor is not available but a documented solved case exists. Sequester the reference before Produce. Provide the producing session only with a staged constraint dossier that does not disclose the solution. Compare the produced artefact against the sealed reference at a structural level rather than by surface wording alone. Record the case source, evidence that the reference solved the problem, the constraint-release schedule, the isolation measures, the judges, contamination checks, substantive divergences, any dissent, and whether the finding bears on the artefact, the methodology, or the case-selection procedure. Reference validation supplies evidence about the methodology's capacity to derive an artefact under comparable constraints; it does not by itself count as domain validation for live use.

**Domain validation** applies when an artefact is intended for actual use outside the workspace. Obtain evidence from the domain source that bears the problem in use: the user of a sequence, the reader of a specification, the participant in a process, the operating record of a deployed system, or an equivalent. Record who or what supplied the evidence, what was tried, what happened, and whether modification was requested.

A receiving session records any validation report when the report becomes available and decides whether it closes the artefact, triggers artefact revision, triggers methodology revision, or shows that the validation mechanism itself was inadequate.
```

What changes in practice:

- The receiving session now records reference-validation reports as first-class evidence, not as stretched workspace notes.
- It must classify the consequence explicitly: artefact revision, methodology revision, case rejection, or mechanism failure.
- Domain validation remains separate and is not silently backfilled by reference success.

## Q6. Iteration and pass criteria (all three sub-parts)

### (a) Artefact pass

A specific artefact passes reference-validation when all four conditions hold:

- All mandatory constraints across all released packets are satisfied.
- The validation cell assigns a structural score of at least 80/100.
- At least 2/3 validators judge the artefact functionally equivalent or superior on the rubric.
- No unresolved contamination dissent remains.

A `partial match` is not a pass. It authorises another blind produce round.

### (b) Methodology pass

The methodology’s external-artefact claim becomes supported, not proven once and for all, after `5` reference cases with at least `4` passes.

Additional conditions:

- The 5 cases must span at least 3 artefact types or domains.
- At least 2 cases must be explicitly low-saturation cases selected for contamination resistance.
- No counted pass may carry unresolved contamination dissent.
- One non-pass may be classified as a methodology gap without resetting the whole program.

I am deliberately not setting the bar at 3/3. Small-sample success is too easy to fake through case selection.

### (c) Mechanism-failure vs methodology-gap distinction

Operational test:

- `Methodology gap` if the failure localises to a missing or weak design rule inside the methodology, while blindness, staged release, and structural comparison all remained intact.
- `Mechanism failure` if the protocol cannot produce discriminating evidence even when the methodology is followed.

Three core properties must all hold:

- `Blindness`: producers are isolated from the reference.
- `Stageability`: constraints can be packetized without solution-bearing language.
- `Discriminability`: validators can distinguish structural adequacy from retrieval or vibe-similarity.

Concrete threshold:

- If Session 015 shows failure of any two of those three core properties, the mechanism is falsified and the methodology should return to pause.
- A single hard leak of the reference into Produce is also mechanism-falsifying for that run.
- A single methodology gap with the three core properties intact is not mechanism failure.

## Q7. Risks and dissent (all four bullets)

- Strongest failure mode: benchmark theater. The workspace starts choosing references that are legible to models, packetizing them in solution-shaped language, and scoring surface resemblance as if it were evidence. The mechanism then restores the comfort of “validation” without restoring the lost loop.
- Explicit falsifiability condition: if Session 015 cannot satisfy blindness, stageability, and discriminability at the same time, or if the contamination canary shows cross-family spontaneous reproduction of the reference’s distinctive structure from the initial packet, the mechanism’s adequacy is falsified and pause should return.
- The “procedural self-deception” test: the validation report is ritual if it cannot name the concrete ways the artefact might have failed and the concrete reasons it did not. Another observable is worse: every iteration moves the artefact closer to the reference’s wording or idiosyncratic labels after validators have seen the reference. That is not validation; it is answer-key chasing.
- Circumstances under which to fall back to pause: inability to find low-contamination cases; repeated contamination dissents that cannot be resolved conservatively; two consecutive cases where packetization itself smuggles the solution; or any attempt to treat reference-validation as interchangeable with domain validation for live deployment claims.

My preserved dissent, stated strongly: even if this mechanism works, it validates a narrower claim than the old loop did. It can support “the methodology can derive artefacts that resemble proven solutions under blinded staged constraints.” It cannot honestly mean “the methodology’s new external artefacts work in live domains.” If other perspectives flatten those claims together, that is exactly the procedural self-deception Session 013 warned about.
