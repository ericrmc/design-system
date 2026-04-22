---
title: Reference Validation
version: 1
status: superseded
created: 2026-04-22
last-updated: 2026-04-22
updated-by-session: 014
supersedes: none
superseded-by: reference-validation.md (v2)
---

# Reference Validation

## Purpose

This specification defines the reference-validation mechanism: how the methodology tests its external-artefact-production claim against documented proven solutions, under conditions where a live domain-actor is unavailable.

Reference validation is a third named sense of validation alongside Workspace validation and Domain validation (per `methodology-kernel.md` v4 §7). It supplies evidence about the methodology's capacity to derive artefacts under stated constraints. **It does not establish that any specific artefact functioned in its intended use, and it does not substitute for Domain validation when a domain-actor is available.** This scope-statement is load-bearing and must be preserved in any citation of reference-validation as evidence.

This specification was produced in Session 014 as a resolution of OI-016 (domain-validation pathway under user unavailability). It is provisional pending first-exercise at Session 015; six automatic re-opening triggers on OI-016 are specified within this document's §9.

## Specification

### 1. Selection criteria for a reference case

A candidate reference case must satisfy all eight of the following criteria. A single-criterion failure is disqualifying.

**C1 — Documented solution with auditable provenance.** The reference must be a solution whose origin can be pointed at: identifiable author, team, or institution; dated publication or delivery; accessible URL or citation. The reference must have been published or archived at least 12 months before the exercise-opening session. A snapshot of the reference URL or document is committed into the exercise's provenance directory as an anti-drift witness at Cell 1 open.

**C2 — Constraint-legibility without solution-smuggling.** The constraint set must be statable to Produce agents as a problem-shape without the statement tipping the solution. A fresh agent reading only the constraint statement must be able to name more than one plausible solution family. If the constraint statement is so detailed that the reference solution is implied, the case has leaked and is rejected.

**C3 — Low saturation in common training distributions.** The reference must not be a canonical worked example appearing verbatim or near-verbatim across internet corpora. Operational test: both a non-Claude model (via `codex exec`) and an independent Claude instance are each given only the constraint statement and asked to produce a solution. If either produces text that exceeds 30% shared 5-gram token overlap with the reference, the case is rejected as contaminated. Additionally, the Outsider contamination canary (per §4.L1) runs thin prompts derived from tranche-0 against at least two model families; if they spontaneously emit the reference's idiosyncratic structure, labels, or sequence, the case is discarded.

**C4 — Staged-constraint structure.** The reference case's constraint set must be partitionable into an initial subset (tranche-0) and at least two emergent subsets (tranche-1, tranche-2, ...) whose release is tied to methodology-internal triggers pre-committed at Cell 1. Tranche-0 contains no more than roughly 60% of the final constraint set. Cases where all constraints are knowable up-front are weaker tests and are deprioritised. The reference case's author must have documented evidence of the problem's shape changing during design (project diaries, retrospective papers, change logs, revision history) — constraints that genuinely arrived over time historically.

**C5 — Domain-legibility to the judges.** The reference case must be in a domain where Cell 3 validators (Claude subagents plus at least one non-Claude judge) can read both the reference and the methodology's output with enough competence to distinguish structural match from lexical coincidence. If judges need domain expertise unavailable to the validator panel, the comparison collapses to surface-string overlap.

**C6 — Bounded effort.** The reference artefact fits under 10,000 tokens; the constraint statement fits in 1–3 KB; comparison judging fits in a single context window per judge. One Cell 1 preparation session should be sufficient to source the reference, fetch it, extract the staged constraint tranches, and commit the sealed case pack. Cases requiring archival research, translation, or inter-library-loan fail this criterion.

**C7 — Representativeness of the methodology's external-artefact claim.** The reference case must be an artefact of the type the methodology actually claims to produce: protocol, sequence, decision aid, structured procedure, concise specification, or checklist. Not a proof, not a mathematical construction, not a piece of software, not a piece of music, not an aesthetic output. The Session 008/010 external artefacts are in the movement-sequence and household-decision domains; the reference pool must include cases adjacent to those existing claims.

**C8 — Pre-LLM-co-design reference date + falsification-admitting + uncertainty-declared.** Three sub-criteria, all required.
- **Pre-LLM-co-design:** the reference must not have been produced with LLM assistance; for most domains this means predating late 2022. LLM-co-designed references already reflect LLM design patterns and comparing an LLM-methodology output to an LLM-co-designed reference is short-circuit contamination.
- **Falsification-admitting:** the reference must have explicit mandatory constraints, explicit optional elements, and explicit failure conditions. If every divergence can be explained away as "another valid approach," the case cannot validate anything.
- **Uncertainty-declared:** the provenance write-up for the reference must include the author's own account of what they are uncertain about in their solution — which parts they might have done differently, what they would change with hindsight. This provides a tolerance band for divergence scoring: divergence within author-flagged uncertainty bands is scored as legitimate design judgment, not as substantive divergence.

**Flagged tension (preserved per Session 014 Skeptic Q1).** Criteria (5) legibility and (8) pre-LLM-co-design are in structural tension with (3) low-saturation. A domain legible to Claude subagents and whose reference pre-dates 2022 is almost by construction heavily represented in Claude's pretraining. The selection criteria attempt to probe around this tension via the saturation test and contamination canary; the tension is not resolved. If the tension empties the candidate pool at sustainable rate (Session 015+ pattern), the mechanism-failure trigger in §8(c) fires.

### 2. The comparison procedure

The comparison procedure has five stages, operating within the three-cell protocol specified in §3.

**Stage 0 — Case packaging (Cell 1).** A non-Produce agent (the Case Steward) assembles the sealed case pack. The pack contains:
- Initial brief (tranche-0 constraints, written in methodology-standard language without reference-lexical fingerprints).
- Emergent-constraint schedule (tranche-1..N constraints, each tagged with a release trigger — e.g., "release at start of Deliberate," "release when Produce first proposes mechanism X," "release on any Validate finding of class Y"). Triggers stated in methodology terms only.
- Reference envelope (reference solution + author-uncertainty commentary, sealed, not read by Case Steward after packaging, not introduced into any Produce agent's context).
- Contamination-audit plan (which checks will run, what thresholds apply, what counts as a failed audit).

The sealed case pack is committed at a named commit hash before Cell 2 opens. The commit hash is the anti-tampering witness.

**Stage 1 — Isolated Produce (Cell 2).** Produce agents run the methodology's normal Deliberate → Decide → Produce loop on tranche-0. Search tooling is available but an exclusion list is enforced at pre-commit: agents cannot search for the reference's title, author, URL, or reference-identifying distinctive phrasing. The exclusion list is specified by the Case Steward in Stage 0.

Produce agents emit two artefacts each round:
- The produced artefact.
- A **constraint-to-decision trace** explaining why each major feature exists, referenced to specific released tranche-items. An element without constraint-grounded rationale does not count toward validation evidence at Cell 3.

**Stage 2 — Emergent-constraint release.** A Constraint Steward (distinct from Case Steward, but also non-Produce) watches for trigger conditions in Stage 0's emergent schedule during Cell 2 iteration. Triggers fire on observable methodology events (artefact file written; Validate report committed; Produce agent explicit question). If a trigger does not fire by its deadline, the constraint is released at the deadline anyway so the exercise does not depend on the Produce agents happening to ask the right question.

Cell 2 iterates up to **2 internal Produce rounds** triggered by in-session Validate findings or by emergent-constraint-release events. Each iteration emits a fresh artefact + constraint-to-decision trace.

**Stage 3 — Comparison (Cell 3).** Cell 3 opens in a subsequent session. Three validator judges receive: the produced artefact (final iteration), the constraint-to-decision trace, the full released constraint set (tranche-0 + all emergent tranches), and the reference envelope. Validators are role-differentiated:

- **Reference-faithful reader.** Sees reference and artefact; maps reference components to a structural rubric; rates correspondence per component.
- **Methodology-sympathetic reader.** Sees constraints and artefact only (not reference); evaluates whether the artefact is a defensible design response to the released constraints.
- **Contamination auditor.** Sees reference, artefact, and constraint-to-decision trace; runs the seven-layer contamination defence stack (§4) and flags any failures.

**Cross-model mandatory in Cell 3.** At least one judge must be from a non-Claude family (via `codex exec` to an OpenAI or other non-Claude model). Same-family judge agreement is weaker evidence than cross-family agreement.

Comparison is performed across four axes:
- **Constraint satisfaction.** Pass/fail per constraint.
- **Structural alignment.** Match / partial-match / divergent / missing / extra per major structural element.
- **Lexical distance.** Shared 5-gram token overlap with reference. **This is inverted: low overlap is healthy; high overlap is a contamination signal.**
- **Author-uncertainty-band alignment.** Divergences within author-flagged uncertainty bands are scored as legitimate design judgment.

**Stage 4 — Classification and iteration.** Cell 3's verdict is one of four states:

- **Pass.** All five artefact-pass conditions per §5 hold.
- **Partial match.** Some of §5's conditions fail but gaps are repairable. Triggers one additional Produce round in Session N+2 with constraint-delta memo only (not reference-informed brief). After second Produce round, verdict is final.
- **Fail — methodology-gap.** Constraint satisfaction incomplete AND gap is localisable to a specific methodology step; the produced artefact does not hold up independently against constraints. Opens a new open issue; the methodology can revise in subsequent sessions and re-attempt a similar case.
- **Fail — mechanism-probe.** Comparison procedure itself cannot produce a confident pass/fail signal. Escalates to meta-OI on mechanism.
- **Contaminated / no-signal.** Contamination auditor flags a defence failure. Exercise voided, case retired from pool, replacement selected.

### 3. The sealed three-cell protocol

Validation runs across a small number of sessions (2–4 per exercise) organised into three cells with clean role-separation.

#### Cell 1 — Curation

**Agents.** One or two Case Stewards (non-Produce, non-Validation). May include a Constraint Steward if distinct from Case Steward.

**Outputs.** Sealed case pack (reference envelope, tranche-tagged constraint set, release-trigger schedule, contamination-audit plan, committed anti-drift witness). `brief-gatekeeper.md` at the exercise-provenance root.

**Constraints.** Case Steward does not read the reference after sealing. Anti-tampering: any post-sealing edit to `brief-gatekeeper.md` is a red flag (see WX-14-4).

#### Cell 2 — Produce

**Agents.** One to four methodology-following perspectives per the standing `multi-agent-deliberation.md` v3 convention. May include a non-Claude perspective for additional cross-model variance on the Produce side (optional, not required — cross-model is required in Cell 3).

**Outputs.** Produced artefact + constraint-to-decision trace, committed per iteration round. Up to 2 internal iterations triggered by in-session Validate findings or emergent-constraint releases.

**Constraints.** Produce agents do not see the reference. Search exclusion list enforced at pre-commit. No reference text, URL, or identifying phrasing in Produce context. Emergent constraints enter Cell 2 only via the Constraint Steward's explicit releases.

#### Cell 3 — Validation

**Agents.** Minimum three judges: reference-faithful reader, methodology-sympathetic reader, contamination auditor. **At least one non-Claude judge mandatory.** Optional fourth adjudicator agent if reference-faithful and methodology-sympathetic disagree materially.

**Outputs.** `comparison-verdict.md` with verdict state and judge-by-judge rationale. `contamination-audit.md` with all §4 defence results. Both committed at Cell 3 close.

**Constraints.** Contamination dissent dominates structural finding: ambiguity on contamination is not resolved optimistically. Any judge may file a blocking contamination dissent if they can point to reference-specific features not derivable from released constraints. All dissents preserved verbatim.

#### Session shape

- **Session N** (Cell 1 + Cell 2). Opens with Case Steward work (Cell 1); proceeds to Produce (Cell 2) once case pack is sealed; up to 2 internal iterations.
- **Session N+1** (Cell 3). Opens reference envelope; runs comparison with three judges; emits verdict.
- **Session N+2** (Cell 2 iteration, if triggered). Re-runs Produce with constraint-delta memo; does not re-open reference envelope.
- **Session N+3** (Cell 3 second comparison, if triggered). Re-runs comparison on revised artefact.

**Hard stop:** 2 Produce rounds × 2 Validation rounds = 4 sessions maximum per exercise. Beyond that, exercise closes as unresolved-methodology-gap.

### 4. The seven-layer contamination defence stack

No single defence is airtight. Layered defences are mandatory.

**L1 — Reference selection saturation gate.** Per §1 C3. Pre-adoption test: Outsider + independent Claude each given constraints-only, asked to produce solution. Reject on >30% 5-gram overlap. Outsider-originated **contamination canary**: thin prompts derived from tranche-0 fired at multiple model families; reject on spontaneous emission of reference's idiosyncratic structure/labels/sequence.

**L2 — Produce-side contextual isolation.** Cell 2 agents have tooling but search exclusion list enforced at pre-commit. No reference text, URL, or reference-identifying phrasing in Produce context. Enforcement: if comparison at Cell 3 detects high lexical similarity, Fail verdict (inverted-axis rule). Incentive structure punishes circumvention.

**L3 — Cross-model divergence analysis.** Cell 3 validators span Claude-family and non-Claude-family. Cross-family convergence on reference text is contamination evidence. Cross-family divergence with both satisfying constraints is design evidence.

**L4 — Structural + lexical-inverted comparison.** Cell 3's rubric weights structural correspondence primarily, with lexical distance as contamination signal (not quality signal). Never adopted alone; always runs with L5 + L6 + L7.

**L5 — Counterfactual probing.** After Cell 2 Produce completes, the Case Steward modifies one or more constraints to be off-distribution for the reference and asks the methodology to re-produce. If the methodology produces a genuinely different artefact tracking the new constraint, that is positive design evidence. If the methodology produces a near-copy that ignores the constraint change, that is retrieval evidence. This is the **only defence that actively probes design vs retrieval** rather than passively measuring output overlap.

**L6 — Process-trace requirement.** Cell 2 emits the constraint-to-decision trace with the artefact. Cell 3 validators check: does each major artefact element trace to a released constraint plus methodology decision? Elements lacking constraint-grounded rationale do not count as validation evidence even if they match the reference.

**L7 — Distinctive-marker audit.** Cell 3 contamination auditor explicitly enumerates rare markers in the reference: branded labels, unusual ordering, arbitrary counts, non-obvious wording, signature metaphors. Reproduction of those markers in the produced artefact, absent constraint-grounded rationale, counts as contamination evidence even if structural correspondence is otherwise defensible.

**Contamination-audit file.** Each exercise commits `contamination-audit.md` at exercise close with L1 saturation-test results, L3 cross-model divergence characterisation, L5 counterfactual-probe results, L7 distinctive-marker findings, lexical-overlap scores, accidental-match ratio, tranche-0 sufficiency, and iteration count.

**Honest-scope statement.** This seven-layer defence stack validates that the methodology produces structurally-sound artefacts. **It does not fully validate that the methodology produces those artefacts by methodology rather than by taste.** Tacit structural contamination — an agent having learned the solution class during pretraining without the specific lexical instance — is residual risk not closed by any defence. This is a known limitation of the mechanism and must be cited alongside any methodology-level claim built on reference-validation evidence.

**Regime in which no defence is adequate.** For classical engineering problems with canonical solutions, widely-taught design patterns, textbook-standard protocols, and heavily-documented technical canon, reference-validation is not evidence of methodology capability regardless of mechanism. §1 criteria C3 + C8 + C5 attempt to exclude this regime; the exclusion is imperfect and the sweet-spot domain-pool may be narrower than this specification implies.

### 5. Artefact pass criteria

An artefact passes reference-validation when **all five** of the following hold in Cell 3's verdict:

1. All mandatory constraints from tranche-0 and all emergent tranches released during the exercise are satisfied (per methodology-sympathetic reader + non-Claude cross-model sanity).
2. Structural correspondence score ≥ 80/100 (per reference-faithful reader rubric; major structural elements specified in Stage 0 by Case Steward, not retrofitted after comparison).
3. Lexical distance above contamination threshold: < 30% shared 5-gram tokens with reference (confirmed by contamination auditor).
4. No unresolved contamination dissent from the contamination auditor (contamination dominates structural finding; ambiguity not resolved optimistically).
5. L5 counterfactual probe demonstrates genuine methodology differentiation (the methodology produces a different artefact when the constraint is modified off-distribution).

Failure of any one pushes the verdict to Partial match (if gaps repairable) or Fail (otherwise).

### 6. Methodology pass criteria

The methodology's external-artefact claim is considered validated at the methodology level when:

- **N = 5 reference cases completed.**
- **≥ 4 of 5 pass** (80% threshold). A 100% pass rate is itself a contamination signal — expect occasional defensible divergences that don't match the reference.
- **Cases span ≥ 3 distinct artefact types or domains.** A methodology validated on 4 cases all in one domain has not supported its cross-domain claim.
- **≥ 1 case selected from the difficult-to-contaminate tail** (per §1 C3 low-saturation, stringently applied).
- **No counted pass may carry unresolved contamination dissent.**
- **Methodology-version reset:** kernel revisions reset the count. Each exercise carries a `methodology-version` tag (e.g., `kernel-v4`). Passes accumulate against the tagged version. A new kernel is a different methodology and owes new evidence.
- **Partial-credit rule:** an exercise failing with `fail-methodology-gap`, receiving a fix in subsequent session(s), and re-running against a similar reference case, counts as 0.5 toward the pass threshold (not 1.0). Blocks the fail-deliberately-then-fix gaming path.

### 7. Mechanism-failure vs methodology-gap distinction

A **methodology gap** is a legitimate output: the failure localises to a missing or weak design rule inside the methodology (e.g., "Deliberate did not consider constraint C7 because perspective lineup lacked domain-expertise X"); a targeted kernel or spec revision is proposable; a re-run exercise against a structurally-similar reference case shows the gap closed; the contamination audit for the failing exercise was clean.

**Mechanism failure** is falsification of the reference-validation protocol itself. Three core properties must all hold for the mechanism to operate:

- **Blindness.** Producers are isolated from the reference.
- **Stageability.** Constraints can be packetised without solution-bearing language; releases are at pre-committed triggers; no adaptive staging.
- **Discriminability.** Validators can distinguish structural adequacy from retrieval or vibe-similarity; pass/fail signal is reproducible across re-runs of the same inputs.

**Failure of any two of these three core properties in a single exercise is mechanism falsification.** A single hard leak of the reference into Cell 2 is mechanism-falsifying for that exercise. Additional mechanism-failure patterns include:

- Comparator/arbiter disagreement rate > 60% across a run series.
- Noise-floor audit (shuffled-constraint baseline comparison) shows mechanism pass-rate within 15 percentage points of no-methodology baseline.
- Pass verdicts on seeded-contaminated runs paired with fail verdicts on seeded-clean runs (signal inversion).

**Anti-laundering rule.** Three consecutive exercises each "surface a gap" each "addressed in subsequent session" with none producing a passing result, is not gap-surfacing; it is methodology-failure serially relabelled. Methodology returns to pause.

### 8. Label discipline

Artefacts produced under reference-validation carry a frontmatter label:

```yaml
validation: reference-validated
```

A single artefact may carry multiple labels if it receives multiple senses of validation over its lifecycle. Possible labels:
- `validation: workspace-only` (neither Domain nor Reference validation obtained).
- `validation: domain-validated` (Domain validation obtained per kernel §7).
- `validation: reference-validated` (Reference validation obtained per this specification).

**The distinction between `domain-validated` and `reference-validated` must be preserved in any citation** of the artefact's validation status. Reference-validated artefacts carry the narrower claim specified in §1: "the methodology can derive this artefact under stated constraints" — not "this artefact functioned in its intended use."

Citation of a reference-validated artefact as simply "validated" without the `reference-validated` qualification triggers OI-016 re-opening per the label-discipline-collapse condition.

### 9. Automatic re-opening triggers for OI-016

This specification's adoption moves OI-016 to **Resolved — provisionally addressed pending first-exercise**. The resolution is provisional; OI-016 automatically re-opens if any of the following is observed:

1. **Three-core-properties test failure** (§7): failure of any 2 of Blindness / Stageability / Discriminability in any exercise.
2. **Counterfactual-probe inversion** (§4 L5): counterfactual-probe results show the methodology producing an artefact tracking original reference rather than modified constraint.
3. **"Too fast" pattern** (Session 014 Q7 Architect): single Produce iteration arriving at ≥80% structural alignment across multiple cases despite passing contamination tests.
4. **Noise-floor inversion** (§7): reference-validation pass-rate within 15 percentage points of no-methodology constraint-only baseline.
5. **Three-consecutive-"gap-surfaced"-non-passes** (§7 anti-laundering rule).
6. **Label discipline collapse** (§8): `validation: reference-validated` artefacts used externally without the label qualification; kernel §7's anti-substitution clause softened or removed without concurrent strengthening elsewhere.

### 10. Preserved first-class minorities

Three dissenting positions from the Session 014 deliberation are preserved as first-class minorities within this specification. Each has a specified operational warrant that would reopen the relevant design question.

**Skeptic "provisional substitute" framing minority** (Session 014, 01c Q5). The kernel should name reference-validation as explicitly provisional, not as equal-but-distinct third sense. The adopted kernel text incorporates the Skeptic's load-bearing scope-statement content ("does not establish intended-use functioning") without using the word "provisional." Operational warrant: if label discipline collapse (§9 trigger 6) is observed, the Skeptic's stricter "provisional substitute" framing is the preferred revision direction for kernel §7.

**Architect pure-within-session shape minority** (Session 014, 01a Q3). Validation should be a single-session loop, not a hand-off across sessions. The adopted shape is the Outsider-originated three-cell protocol with hand-off between Cell 2 and Cell 3. Operational warrant: if Cell 2 → Cell 3 hand-off consistently loses design-intent information that a continuous within-session loop would have preserved (per WX-14-2), the Architect's pure-within-session proposal is the preferred revision direction.

**Skeptic+Outsider joint narrower-claim minority** (Session 014, 01c+01d Q7). Even if the mechanism works as designed, it validates a narrower claim than the original domain-validation loop. The adopted OI-016 disposition (Resolved-provisional) incorporates this position via the six automatic re-opening triggers. Operational warrant: this joint minority is the standing warrant behind §9's re-opening conditions; any movement to soften kernel §7's scope-statement activates the minority and reopens OI-016.

## Validation

To validate this specification:

1. Read kernel §7 v4 and confirm Reference validation is named as a third sense with explicit scope-statement and anti-substitution clause.
2. Confirm Session 014's provenance contains the full deliberation (`01-deliberation.md`), four perspective raw outputs, and the three decisions (D-069, D-070, D-071).
3. Confirm `open-issues.md` carries OI-016 in "Resolved — provisionally addressed pending first-exercise" state with the six re-opening triggers.
4. Confirm this specification's internal cross-references (§1 to §4, §5, §7; §4 to §5; §7 to §9; §8 to §9) are traceable.
5. When Session 015 first-exercises this mechanism, confirm it follows the three-cell protocol and commits the required per-exercise artefacts (`brief-gatekeeper.md`, `contamination-audit.md`, `comparison-verdict.md`).
6. When Session 015's exercise completes, confirm the artefact carries the `validation: reference-validated` frontmatter label (if it passes) or is explicitly recorded as not-reference-validated (if it does not).
