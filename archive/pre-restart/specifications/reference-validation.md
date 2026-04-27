---
title: Reference Validation
version: 3
status: active
created: 2026-04-22
last-updated: 2026-04-23
updated-by-session: 033
supersedes: reference-validation-v2.md
---

# Reference Validation

## Purpose

This specification defines the reference-validation mechanism: how the methodology produces a **provisional reference substitute** for Domain validation when a live domain-actor is unavailable. The substitute supplies evidence about the methodology's capacity to derive artefacts under stated constraints.

Per `methodology-kernel.md` v6 §7, the output of a reference-validation exercise is named **Provisional reference substitute** (formerly "Reference validation" at v5 and earlier). The kernel v6 sense-name rename is load-bearing: reference-validation is a provisional substitute for Domain validation, not an equal-but-distinct third sense. The procedure by which the substitute is produced retains the name "reference-validation exercise"; the renamed category applies to what the procedure *produces* at the level of claim. **Reference-provisional evidence does not establish that any specific artefact functioned in its intended use, and it does not substitute for Domain validation when a domain-actor is available.** This scope-statement is load-bearing and must be preserved in any citation of reference-provisional evidence.

This specification was produced in Session 014 as a resolution of OI-016 (domain-validation pathway under user unavailability). It is provisional pending first-exercise at Session 015; automatic re-opening triggers on OI-016 are specified within this document's §9.

**Version 3 (Session 033)** revises v2 in response to `reference-validation.md` v2 §9 trigger 7 firing at Session 032 close (second structurally-different-domain Cell 1 rejection: Session 018 D2 agile-retrospective + Session 032 PD-A community-admission/Rule-of-St-Benedict, the latter a **cross-family-symmetric** saturation case). §9 trigger 7 activated the Session 014 §10.1 Skeptic "provisional substitute" framing minority as a required kernel §7 revision direction. Session 033 deliberation (3-of-4 cross-family convergence: Outsider GPT-5.4 + Reviser Claude + Synthesiser Claude; 1-of-4 Skeptic-preserver Claude dissent preserved as first-class minority) adopted the rename + mandatory-dissent principle + strengthened scope-statement direction. v3 substantive changes propagate that revision: rename-sync to match kernel v6 sense-name; §1 C3 Stage (b) Condition 3 extended with cross-family-symmetric sub-case distinct from cross-family-asymmetric; §4 L1b extended with cross-family-symmetric sub-check; §8 label-discipline clause adds three-element citation requirement; §8 frontmatter label renamed `reference-validated` → `reference-provisional`; §9 trigger 7 text refreshed to record its one firing event (Session 032) and specify re-fire conditions; §10 extended with three new first-class minorities from Session 033 deliberation (§10.3 Skeptic-preserver minimal-revision; §10.4 Outsider "Constraint-derivation probe" naming; §10.5 Reviser separate-OI-for-detection-gap). v2 is preserved as `reference-validation-v2.md` status superseded.

**Version 2 (Session 019)** revises v1 in response to Session 018's first-exercise Cell 1 C3 rejection (WX-18-2 through WX-18-5). Substantive changes: §1 C3 restructured as a two-stage test with three rejection conditions (quantitative overlap, verbatim distinctive-phrase emission, cross-family retrieval asymmetry); §1 Flagged tension strengthened with empirical materialisation annotation; §4 L1 restructured as L1a thin-prompt canary + L1b full-constraint saturation test (canary is necessary-but-not-sufficient); §4 L3 extended with pre-seal diagnostic-not-design-evidence text; §9 triggers sharpened (trigger 5 counts pre-seal rejections; trigger 6 extended; new trigger 7 pre-commits kernel §7 revision consideration on n=2 structurally-different-domain rejection); §10 preserved minorities annotated with Session 019 and three new Session 019 minorities added. v1 is preserved as `reference-validation-v1.md` status superseded.

## Specification

### 1. Selection criteria for a reference case

A candidate reference case must satisfy all eight of the following criteria. A single-criterion failure is disqualifying.

**C1 — Documented solution with auditable provenance.** The reference must be a solution whose origin can be pointed at: identifiable author, team, or institution; dated publication or delivery; accessible URL or citation. The reference must have been published or archived at least 12 months before the exercise-opening session. A snapshot of the reference URL or document is committed into the exercise's provenance directory as an anti-drift witness at Cell 1 open.

**C2 — Constraint-legibility without solution-smuggling.** The constraint set must be statable to Produce agents as a problem-shape without the statement tipping the solution. A fresh agent reading only the constraint statement must be able to name more than one plausible solution family. If the constraint statement is so detailed that the reference solution is implied, the case has leaked and is rejected.

**C3 — Low saturation in common training distributions.** The reference must not be a canonical worked example appearing verbatim or near-verbatim across internet corpora, nor recoverable from the full candidate constraint statement itself. Operational test runs in two stages against **both** a non-Claude model (via `codex exec`) and an independent Claude instance; both stages are mandatory pre-seal.

**Stage (a) — Thin-prompt contamination canary (per §4 L1a).** Thin prompts derived from tranche-0 are fired at each model family. Spontaneous emission of the reference's idiosyncratic structure, labels, or sequence discards the case.

**Stage (b) — Full-constraint saturation test (per §4 L1b).** Each model is given the complete constraint statement as it would be issued to Cell 2, with reference author, title, and distinctive phrases removed, and asked to produce a solution. **Rejection conditions (any one fires):**

1. Either model produces text exceeding 30% shared 5-gram token overlap with the sealed reference.
2. Either model spontaneously emits a verbatim distinctive phrase, section heading, or named label from the reference (zero-tolerance regardless of overall overlap percentage).
3. **Cross-family retrieval asymmetry or cross-family symmetric reproduction:** one of two sub-cases rejects.
   - **3a — Cross-family asymmetric retrieval:** one model family reproduces the reference verbatim or near-verbatim (or with its idiosyncratic section labels or sequence) while the other produces constraint-satisfying but from-scratch text. The case is rejected even if the quantitative 5-gram figure for the divergent family is below threshold. Cross-family asymmetry of this shape is positive contamination evidence for the reproducing family; it indicates that constraints do not uniquely determine the text, only retrieval does.
   - **3b — Cross-family symmetric reproduction (Session 033 addition per Session 032 PD-A):** both model families reproduce the reference's distinctive labels, section headings, or sequence structure despite the constraint statement's forbidden-terms discipline. Cross-family symmetric reproduction indicates that the reference tradition is densely-trained across multiple pretraining families (not just within one family); in this case, the cross-family divergence-check in Cell 3 (primary L3 signal) degrades as a contamination detector, because convergence across families does not distinguish derivation from shared-canon retrieval. The case is rejected regardless of quantitative 5-gram overlap. Candidates rejected under 3b are **structurally-vulnerable** to reference-provisional framing as specified in `methodology-kernel.md` v6 §7 scope-statement: a passing result in such a domain is not methodology-level evidence even if structural constraints are satisfied. Sub-case 3a and sub-case 3b are methodologically distinct observation classes and must be recorded separately in the contamination-audit file per §4 and §7.

**Stage (a) is necessary but not sufficient** (per WX-18-2, Session 018): thin prompts describe problem-shape without the full requirements and under-detect saturation when the triggering content is distributed across the requirements themselves. Canary survival justifies continuing evaluation; it does not satisfy C3 on its own.

**C4 — Staged-constraint structure.** The reference case's constraint set must be partitionable into an initial subset (tranche-0) and at least two emergent subsets (tranche-1, tranche-2, ...) whose release is tied to methodology-internal triggers pre-committed at Cell 1. Tranche-0 contains no more than roughly 60% of the final constraint set. Cases where all constraints are knowable up-front are weaker tests and are deprioritised. The reference case's author must have documented evidence of the problem's shape changing during design (project diaries, retrospective papers, change logs, revision history) — constraints that genuinely arrived over time historically.

**C5 — Domain-legibility to the judges.** The reference case must be in a domain where Cell 3 validators (Claude subagents plus at least one non-Claude judge) can read both the reference and the methodology's output with enough competence to distinguish structural match from lexical coincidence. If judges need domain expertise unavailable to the validator panel, the comparison collapses to surface-string overlap.

**C6 — Bounded effort.** The reference artefact fits under 10,000 tokens; the constraint statement fits in 1–3 KB; comparison judging fits in a single context window per judge. One Cell 1 preparation session should be sufficient to source the reference, fetch it, extract the staged constraint tranches, and commit the sealed case pack. Cases requiring archival research, translation, or inter-library-loan fail this criterion.

**C7 — Representativeness of the methodology's external-artefact claim.** The reference case must be an artefact of the type the methodology actually claims to produce: protocol, sequence, decision aid, structured procedure, concise specification, or checklist. Not a proof, not a mathematical construction, not a piece of software, not a piece of music, not an aesthetic output. The Session 008/010 external artefacts are in the movement-sequence and household-decision domains; the reference pool must include cases adjacent to those existing claims.

**C8 — Pre-LLM-co-design reference date + falsification-admitting + uncertainty-declared.** Three sub-criteria, all required.
- **Pre-LLM-co-design:** the reference must not have been produced with LLM assistance; for most domains this means predating late 2022. LLM-co-designed references already reflect LLM design patterns and comparing an LLM-methodology output to an LLM-co-designed reference is short-circuit contamination.
- **Falsification-admitting:** the reference must have explicit mandatory constraints, explicit optional elements, and explicit failure conditions. If every divergence can be explained away as "another valid approach," the case cannot validate anything.
- **Uncertainty-declared:** the provenance write-up for the reference must include the author's own account of what they are uncertain about in their solution — which parts they might have done differently, what they would change with hindsight. This provides a tolerance band for divergence scoring: divergence within author-flagged uncertainty bands is scored as legitimate design judgment, not as substantive divergence.

**Flagged tension (preserved per Session 014 Skeptic Q1; empirically materialised Session 018 WX-18-3).** Criteria (5) legibility and (8) pre-LLM-co-design are in structural tension with (3) low-saturation. A domain legible to Claude subagents and whose reference pre-dates 2022 is almost by construction heavily represented in Claude's pretraining.

**Session 018 Cell 1 first-exercise confirmation.** The Kerth Prime Directive retrospective opening protocol — a canonical D2 candidate satisfying C5 and C8 — failed C3 stage (b) with ~94% 5-gram overlap and verbatim section-heading emission by a Claude Opus 4.7 subagent (provenance: `provenance/018-reference-validation-exercise-1/`). This is an empirical instance of the flagged tension, not an unexpected finding; it confirms the tension is operationally load-bearing and cannot be treated as theoretical.

The selection criteria probe around this tension via the two-stage saturation test (§1 C3, §4 L1); **the tension is not resolved by this spec and cannot be resolved by threshold-tuning.** A single Cell 1 rejection against the known limit is not in itself evidence of sustainable-rate pool exhaustion. If the tension empties the candidate pool at sustainable rate (Session 015+ pattern), or if a second full-constraint-stage rejection matches the Session 018 shape in a structurally-different domain, §9 trigger 7 fires and the mechanism-failure trigger in §7 comes into consideration (see also §9 re-opening triggers 5 and 7).

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

**L1 — Reference selection saturation gate.** Per §1 C3. Two stages; both mandatory pre-seal.

**L1a — Thin-prompt contamination canary** (Outsider-originated). Thin prompts derived from tranche-0 fired at multiple model families; reject on spontaneous emission of reference's idiosyncratic structure, labels, or sequence. **Known limitation:** the canary under-detects saturation when the reference's triggering content is distributed across requirements rather than concentrated in problem-shape (WX-18-2, Session 018). L1a survival is necessary but not sufficient.

**L1b — Full-constraint saturation test.** Outsider + independent Claude each given the complete constraint statement as it would be issued to Cell 2 (with reference author, title, and distinctive phrases removed), asked to produce a solution. Reject per §1 C3 rejection conditions (1) >30% 5-gram overlap, (2) verbatim distinctive-phrase or section-heading emission (zero-tolerance), (3a) cross-family asymmetric retrieval, or (3b) cross-family symmetric reproduction (Session 033 addition per Session 032 PD-A). The L1b verdict file MUST record which sub-case applies when Condition 3 fires (3a asymmetric vs 3b symmetric); sub-case recording is load-bearing because 3a and 3b inform different downstream remediations (3a: asymmetry-probe family-blind-spot signal; 3b: candidate structurally-vulnerable regardless of remediation, per §1 C3 Stage (b) 3b). The seal record preserves the prompts, model families, and outputs used to clear L1b.

Cases passing both L1a and L1b proceed to sealing per §4 L2.

**L2 — Produce-side contextual isolation.** Cell 2 agents have tooling but search exclusion list enforced at pre-commit. No reference text, URL, or reference-identifying phrasing in Produce context. Enforcement: if comparison at Cell 3 detects high lexical similarity, Fail verdict (inverted-axis rule). Incentive structure punishes circumvention.

**L3 — Cross-model divergence analysis.** Cell 3 validators span Claude-family and non-Claude-family. Cross-family convergence on reference text is contamination evidence. Cross-family divergence with both satisfying constraints is design evidence **at Cell 3 (post-seal)**.

**Pre-seal interpretation (Session 019 revision per WX-18-4).** Cross-family divergence observed during §1 C3 stage (b) or §4 L1b is a contamination diagnostic, not design evidence: it shows uneven saturation across model families, not that the methodology derived the structure. **A candidate that fails C3 is not rescued by cleaner output from another family.** Pre-seal cross-family divergence is interpretable as design evidence only after a case has passed L1 and reached Cell 3.

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
validation: reference-provisional
```

**Label rename (Session 033 per kernel v6 cascade).** The v1/v2 label `validation: reference-validated` is renamed to `validation: reference-provisional` at v3 to align with the kernel v6 sense-name rename ("Reference validation" → "Provisional reference substitute"). **Grandfather clause:** artefacts produced under kernel v3/v4/v5 (Sessions 009–032) that carry `validation: reference-validated` are semantically-equivalent-to `validation: reference-provisional` for citation purposes; no retroactive rewriting of sealed session records per D-017 immutability. New artefacts produced from engine-v6 adoption onward use the `validation: reference-provisional` label.

A single artefact may carry multiple labels if it receives multiple senses of validation over its lifecycle. Possible labels:
- `validation: workspace-only` (neither Domain nor Reference-provisional obtained).
- `validation: domain-validated` (Domain validation obtained per kernel §7).
- `validation: reference-provisional` (Reference-provisional substitute obtained per this specification).
- `validation: reference-validated` (pre-v3 label; semantically-equivalent to `reference-provisional` per grandfather clause above; not used for new artefacts from engine-v6 onward).

**The distinction between `domain-validated` and `reference-provisional` must be preserved in any citation** of the artefact's validation status. Reference-provisional artefacts carry the narrower claim specified in §1: "the methodology can derive this artefact under stated constraints" — not "this artefact functioned in its intended use."

**Mandatory-dissent citation discipline (Session 033 v3 addition per §9 trigger 7 firing; operationalises kernel v6 §7 citation-discipline principle).** Any citation of a reference-provisional result outside the producing session — in external-facing artefacts, in methodology-level claims, or in subsequent sessions treating it as evidence for the methodology's capacity — must carry all three of the following:

1. **Explicit label.** The `validation: reference-provisional` label MUST be preserved (or, for grandfathered pre-v3 artefacts, the `validation: reference-validated` label with a note per the grandfather clause).
2. **Named dissent or contamination-risk acknowledgement.** A named dissenting view from the sealed record, OR — if no dissent was recorded in the exercise — an explicit acknowledgement of contamination risk naming the saturation profile of the reference domain: (copyrighted / public-domain) × (single-family-asymmetric / cross-family-symmetric per §1 C3 Stage (b) 3a/3b distinction).
3. **Contamination-audit pointer.** A provenance-relative path to the exercise's contamination-audit file.

Citations that drop any of (1)–(3) are workspace-invalid and must be repaired before the containing artefact seals. Enforcement: (a) **session-scoped sealing gate** — the Validate activity (kernel §7) checks any artefact citing a reference-provisional result for the three required elements before the session closes; failure returns to Produce; (b) **frontmatter propagation** — the `validation: reference-provisional` label propagates into any artefact that cites the result. If an artefact cites multiple validation sources, the most-provisional label wins at the frontmatter level; (c) **close-rotation check** — the close-rotation checklist verifies citation discipline on any reference-provisional citations introduced this session.

Citation of a reference-provisional artefact as simply "validated" without the `reference-provisional` qualification (or the grandfathered `reference-validated` qualification for pre-v3 artefacts) triggers OI-016 re-opening per the label-discipline-collapse condition (§9 trigger 6).

**Cross-family-symmetric caveat.** When a reference-provisional artefact is produced on a reference where cross-family-symmetric reproduction was observed at any Cell 1 §1 C3 stage, the citation MUST record this observation alongside the label; per kernel v6 §7 scope-statement, such a result is at most methodology-consistent evidence, not methodology-level evidence.

### 9. Automatic re-opening triggers for OI-016

This specification's adoption moves OI-016 to **Resolved — provisionally addressed pending first-exercise**. The resolution is provisional; OI-016 automatically re-opens if any of the following is observed:

1. **Three-core-properties test failure** (§7): failure of any 2 of Blindness / Stageability / Discriminability in any exercise.
2. **Counterfactual-probe inversion** (§4 L5): counterfactual-probe results show the methodology producing an artefact tracking original reference rather than modified constraint.
3. **"Too fast" pattern** (Session 014 Q7 Architect): single Produce iteration arriving at ≥80% structural alignment across multiple cases despite passing contamination tests.
4. **Noise-floor inversion** (§7): reference-validation pass-rate within 15 percentage points of no-methodology constraint-only baseline.
5. **Three-consecutive-"gap-surfaced"-non-passes** (§7 anti-laundering rule). **Session 019 clarification (per Skeptic R7, WX-18):** "gap-surfaced non-pass" includes pre-seal Cell 1 rejections; the trigger counts across all exercise attempts regardless of which cell the non-pass occurs in. Session 018 counts as exercise 1.
6. **Label discipline or scope softening** (§8): `validation: reference-validated` artefacts used externally without the label qualification; kernel §7's anti-substitution clause softened or removed without concurrent strengthening elsewhere; **or §1 C3 narrowed from cross-family contamination screening to family-conditional screening without explicit concurrent narrowing of claim language and labels** (Session 019 extension per Outsider).
7. **Structurally-different-domain Cell 1 rejection pattern** (Session 019 addition per Reviser R4 + Outsider §9.7; **FIRED once at Session 032 per D-104**). **Two pre-seal C3 stage (b) rejections in structurally-different domains** (e.g., not both agile-retrospective) with verbatim or near-verbatim reproduction by the Cell 2 Produce-default family. Two such rejections:
   - Activate the Session 014 Skeptic "provisional substitute" minority warrant (per §10) as a **required kernel §7 revision consideration** in the next session after the second rejection.
   - Re-open OI-016 to Open state pending that consideration.
   - Make the saturation-gate false-negative pattern (a candidate surviving L1a canary but rejected at L1b full-constraint probe) observable as a pattern rather than a single-session artefact.

   **Firing event (Session 032).** Counter advanced 1-of-2 (Session 018 D2 Kerth Prime Directive agile-retrospective) → 2-of-2 (Session 032 PD-A Rule of St. Benedict community-admission). Both instances exhibit near-verbatim Claude-family reproduction of reference distinctive labels or section-structure; Session 032 additionally exhibits cross-family-symmetric reproduction per newly-added §1 C3 Stage (b) Condition 3b. Session 033 kernel §7 revision (v5 → v6) adopted the activated minority warrant; OI-016 re-resolved to **Resolved — provisionally-v2** per D-108 with three explicit re-fire conditions specified below.

   **Re-fire conditions for §9 trigger 7 post-v3 adoption** (Session 033 per D-108): trigger 7 re-fires on any one of:
   - (a) **n=3 rejection threshold.** A third structurally-different-domain Cell 1 C3 Stage (b) rejection, particularly one exhibiting cross-family-symmetric reproduction (§1 C3 Stage (b) 3b). n=3 makes the cross-family-symmetric pattern a regularity rather than a pair; forces a deeper revision than v3 (possibly: retire reference-provisional as a sense, or constrain it to non-public-domain corpora only; this is the §10.2 Synthesiser-framing of the finite-loop-by-design argument).
   - (b) **Label-discipline violation.** Any use of the `validation: reference-provisional` label in an external-facing citation without the §8 mandatory-dissent three-element citation requirement.
   - (c) **Scope-reversal.** Reduction of the kernel v6 §7 scope-paragraph or rename of the sense back toward `validation` (i.e., away from `Provisional reference substitute`) without a concurrent substantive justification.

### 10. Preserved first-class minorities

Nine dissenting positions are preserved as first-class minorities within this specification: three from the Session 014 deliberation that produced v1, three from the Session 019 deliberation that produced v2, and three from the Session 033 deliberation that produced v3. Each has a specified operational warrant that would reopen the relevant design question.

#### 10.1 — Session 014 minorities (preserved verbatim from v1, with Session 019 + Session 033 annotations)

**Skeptic "provisional substitute" framing minority** (Session 014, 01c Q5). The kernel should name reference-validation as explicitly provisional, not as equal-but-distinct third sense. The adopted kernel text incorporates the Skeptic's load-bearing scope-statement content ("does not establish intended-use functioning") without using the word "provisional." Operational warrant: if label discipline collapse (§9 trigger 6) is observed, the Skeptic's stricter "provisional substitute" framing is the preferred revision direction for kernel §7.

> **Session 019 annotation.** WX-18-3 is empirical vindication of the underlying narrow-claim position: Session 018 Cell 1 rejected D2 (Kerth Prime Directive) for precisely the reason the Session 014 Skeptic predicted. Session 019's deliberation (3-of-4 cross-family majority: Reviser + Minimalist Claude + Outsider non-Claude) adopted the *narrow reading* of the §10 warrant — label-discipline collapse is the specifically-required trigger; WX-18-3 is a different empirical event. Session 019 instead strengthened §9 trigger 7 to make the Skeptic's warrant automatically activate on n=2 structurally-different-domain rejection. The Session 014 Skeptic minority's framing remains the pre-committed revision direction under §9 triggers 6 or 7. See §10.2 "Session 019 Skeptic preemptive-activation minority" for the broad-reading alternative preserved from Session 019.

> **Session 033 annotation — ACTIVATED and ADOPTED.** §9 trigger 7 fired at Session 032 close (n=2 structurally-different-domain rejection: Session 018 D2 + Session 032 PD-A). Per trigger 7's pre-committed mandate, this minority was activated as the required kernel §7 revision direction. Session 033's 3-of-4 cross-family deliberation (Outsider + Reviser + Synthesiser; Skeptic-preserver dissent preserved as §10.3) adopted the activated direction per D-106: kernel §7 sense-name renamed "Reference validation" → "Provisional reference substitute"; frontmatter label renamed `reference-validated` → `reference-provisional` (grandfather clause for pre-v3 artefacts); scope-statement strengthened with saturation-profile-dependent evidential-value language + MAY/MUST NOT/MUST citation-discipline modals. The minority's operational warrant is discharged by adoption; the minority text remains preserved for provenance continuity. **First-ever activation-and-adoption event for a `reference-validation.md` §10 minority.**

**Architect pure-within-session shape minority** (Session 014, 01a Q3). Validation should be a single-session loop, not a hand-off across sessions. The adopted shape is the Outsider-originated three-cell protocol with hand-off between Cell 2 and Cell 3. Operational warrant: if Cell 2 → Cell 3 hand-off consistently loses design-intent information that a continuous within-session loop would have preserved (per WX-14-2), the Architect's pure-within-session proposal is the preferred revision direction.

> **Session 019 annotation.** Not engaged by Session 018's Cell 1 pre-seal rejection or by Session 019's revisions. Preserved unchanged.

**Skeptic+Outsider joint narrower-claim minority** (Session 014, 01c+01d Q7). Even if the mechanism works as designed, it validates a narrower claim than the original domain-validation loop. The adopted OI-016 disposition (Resolved-provisional) incorporates this position via the automatic re-opening triggers. Operational warrant: this joint minority is the standing warrant behind §9's re-opening conditions; any movement to soften kernel §7's scope-statement activates the minority and reopens OI-016.

> **Session 019 annotation.** Session 019's §9 trigger strengthening (sharpened trigger 5, extended trigger 6, new trigger 7) increases the surface on which this joint minority can activate. Compatible with the R1–R5 revisions. Preserved unchanged.

#### 10.2 — Session 019 minorities (new; added at v2)

**Minimalist defer-revision minority** (Session 019, 01b Q1, Q7). Position: the single data point from Session 018 (one C3 rejection of D2) does not compel spec amendment; the spec should not be edited before n=2 exercise evidence or before the §1 pool-exhaustion trigger fires. Session 019's majority adopted spec revisions over this position; the R1–R5 text was drafted from one data point. Operational warrant: if Session 020's Cell 1 attempt with S1, S2, or a re-surveyed candidate passes C3 stage (a) and (b) without triggering any of the three rejection conditions, the revised §1 C3 and §4 L1 text did no work that the v1 text would not also have done, and the amendments can be read as premature. In that event, the Minimalist position is vindicated and the amendments are candidates for rollback argument. The Minimalist explicitly passed the anti-laundering check on their deferral position, citing specific revision-compulsion thresholds (n=2 same-shape rejection; §8(c) pool-exhaustion trigger firing) that prevent deferral from becoming indefinite.

**Skeptic preemptive-activation minority** (Session 019, 01c Q5, Q7). Position: WX-18-3's empirical materialisation of the §1-flagged tension satisfies the *spirit* of §10.1's "provisional substitute" warrant, even though the specific textual trigger (label-discipline collapse) has not occurred; kernel §7 should have been revised in Session 019 to use the phrase "provisional substitute" and to add a mandatory-dissent clause. Session 019's 3-of-4 cross-family majority adopted the narrow reading of the warrant instead, strengthening §9 trigger 7 to activate the kernel §7 revision on n=2. Operational warrant: if Sessions 020–022 produce a second structurally-different-domain Cell 1 rejection (triggering §9 trigger 7) and the broad-reading preemptive activation would have prevented interim citation drift (per §8 label discipline), the Skeptic's preemptive-activation position is vindicated and the kernel §7 revision direction is the preferred response. The Skeptic's full Q5 text (kernel §7 draft with "provisional substitute" + mandatory-dissent clause) is preserved in `provenance/019-reference-validation-revision/01c-perspective-skeptic.md` Q5.

> **Session 033 annotation — VINDICATED Session 032; adoption completed Session 033.** Session 032's n=2 structurally-different-domain rejection fired §9 trigger 7 as the minority predicted. The minority's specific proposal (kernel §7 revision using "provisional substitute" framing + mandatory-dissent clause) was adopted by Session 033 D-106 per the activated §10.1 Session 014 Skeptic minority. The minority's operational warrant is discharged by vindication; the minority text remains preserved for provenance continuity. **First-ever vindication event for a `reference-validation.md` §10.2 minority** (recorded Session 032 close per D-104).

**Reviser asymmetry-probe minority** (Session 019, 01a Q3 R2). Position: §4 L1 should include an explicit asymmetry-probe clause recording which family reproduced the reference and which did not at L1b, with accumulated records informing a future Cell 2 Produce default question (WX-18-5). Session 019's 3-of-4 majority (Minimalist + Skeptic + Outsider) rejected this clause on the grounds that watchpoint WX-18-5 suffices for n=1 and that the probe clause risks over-reading into `multi-agent-deliberation.md` territory prematurely. Operational warrant: if Sessions 020+ produce multiple Cell 1 L1b rejections and the session-level ability to judge WX-18-5 as a pattern is impaired by absence of structured asymmetry records, the Reviser's probe clause is the preferred revision direction for a Session 021+ §4 L1 amendment. The Reviser's full R2 text is preserved in `provenance/019-reference-validation-revision/01a-perspective-reviser.md` Q3 R2.

> **Session 033 annotation.** Session 018 D2 was asymmetric (Claude-family reproduced, codex-family did not); Session 031 S1 was symmetric pass (both families constraint-derived); Session 032 PD-A was cross-family-symmetric (both families reproduced). The asymmetry-probe minority is partial-vindicated for the asymmetric sub-case (§1 C3 Stage (b) 3a) — v3 retains §4 L1b sub-case recording per the minority's direction. The minority is not-engaged for the symmetric sub-case (§1 C3 Stage (b) 3b) — symmetric reproduction is not an asymmetry to record, but is recorded separately under the new 3b sub-case. The minority is preserved unchanged in text; v3's §1 C3 + §4 L1b sub-case recording partially realises the minority's direction.

#### 10.3 — Session 033 minorities (new; added at v3)

**Skeptic-preserver minimal-revision minority** (Session 033, 01b). Position: the kernel §7 revision adopted at v6 is over-calibrated to n=2 evidence. The minimum-viable response to §9 trigger 7 firing is a one-word "provisional" insertion in the v5 scope-statement — no sense-name rename; no kernel-level mandatory-dissent clause (place in `reference-validation.md` §8 only if anywhere); no `reference-validation.md` v3 substantive bump. The activated Session 014 minority warrant is honored at minimum scope; n=2 is the activation threshold, not the characterisation threshold. Reserve larger revisions for n≥3.

The Skeptic-preserver's full Q1 minimal text is preserved in `provenance/033-session-assessment/01b-perspective-skeptic.md` Q1:

> "Keep the third-sense name ('Reference validation'). In the scope-statement paragraph, change 'supplies evidence about the methodology's capacity to derive artefacts under stated constraints' to 'supplies provisional evidence about the methodology's capacity to derive artefacts under stated constraints.' One word. No rename. No cascading label changes."

Operational warrant: if Session 034+ demonstrates the broader v6 revision over-corrected (operators find the `reference-provisional` label cumbersome with no corresponding evidence-quality improvement; citation discipline failures do not decrease; kernel stability erodes measurably), the minimum-revision path is the preferred rollback direction. Concretely: if a v6 → v7 kernel revision is proposed within 5 sessions post-v6 that rolls back scope-statement strengthening, the Skeptic-preserver's n=2-is-insufficient position is vindicated.

**Outsider "Constraint-derivation probe" naming minority** (Session 033, 01d Q1). Position: the renamed sense could more accurately be called "Constraint-derivation probe" than "Provisional reference substitute," because it names what the mechanism measures (derivation capacity under blind conditions) rather than what it cannot measure (fitness validation). Session 033's 3-of-4 direction favored "Provisional reference substitute" to preserve parallel structure with `Workspace` and `Domain` senses, but the Outsider's alternative is methodologically sharper.

The Outsider's full Q1 naming text is preserved in `provenance/033-session-assessment/01d-perspective-outsider.md` Q1:

> "I slightly prefer the second because it names what the mechanism actually measures (can the methodology derive a constraint-consistent artefact when a reference is hidden) rather than what it cannot measure (validation of fitness)."

Operational warrant: if future external readers misunderstand "Provisional reference substitute" (e.g., citing it as a "validated reference" anyway despite the provisional qualifier), the "Constraint-derivation probe" naming is the preferred revision direction for a v7+ kernel revision. Alternatively, if `reference-validation.md` v3+ operational practice reveals that the sense is used primarily as capacity-measurement rather than substitute-for-validation, the rename may be preferable on pure-naming-accuracy grounds.

**Reviser separate-OI-for-detection-gap minority** (Session 033, 01a Q5). Position: the cross-family-symmetric saturation finding surfaces a detection-mechanism gap (the Session 019 Reviser asymmetry-probe does not detect this pattern) that is analytically separate from the validation-pathway question OI-016 tracks. A separate OI (OI-019 or next-available number) should be opened to track the detection-mechanism gap as its own problem, rather than folding it into OI-016's validation-pathway scope or tracking it only as a watchpoint.

The Reviser's full Q5 text is preserved in `provenance/033-session-assessment/01a-perspective-reviser.md` Q5:

> "A second OI (call it OI-017 — cross-family-symmetric saturation detection) may be appropriate to open now, separate from OI-016, to track the detection-mechanism gap (Reviser asymmetry-probe does not see it) as its own problem rather than folding it into the validation-pathway OI."

Operational warrant: if within 3 sessions post-033 the cross-family-symmetric detection gap surfaces material design questions that the OI-016 re-opening conditions do not adequately track (e.g., a structurally-separate detection mechanism is proposed that does not belong in the OI-016 validation-pathway scope), the separate-OI approach is vindicated and a session may open the OI at that time citing this minority. If no such material design question surfaces within 3 sessions, the watchpoint-only approach is vindicated. Session 033 records the cross-family-symmetric detection gap as watchpoint **WX-33-1** rather than opening a new OI, per 2-of-3 Claude-perspective preference against OI-proliferation (Outsider did not take a position).

## Validation

To validate this specification:

1. Read kernel §7 v4 and confirm Reference validation is named as a third sense with explicit scope-statement and anti-substitution clause.
2. Confirm Session 014's provenance contains the full v1 deliberation (`provenance/014-oi016-resolution/01-deliberation.md`), four perspective raw outputs, and the three decisions (D-069, D-070, D-071).
3. Confirm Session 019's provenance contains the full v2 deliberation (`provenance/019-reference-validation-revision/01-deliberation.md`), four perspective raw outputs, per-participant manifests, and the two decisions recording the v1 → v2 revision adoption.
4. Confirm `open-issues.md` carries OI-016 in "Resolved — provisionally addressed pending first-exercise" state with the seven re-opening triggers (§9).
5. Confirm this specification's internal cross-references (§1 to §4, §5, §7; §4 to §5; §7 to §9; §8 to §9; §9 to §10) are traceable.
6. When a future session next attempts Cell 1, confirm it follows the two-stage §1 C3 / §4 L1 structure and commits the required per-exercise artefacts (`brief-gatekeeper.md`, `contamination-audit.md`, `comparison-verdict.md`).
7. When a reference-validation exercise completes Cell 3, confirm the artefact carries the `validation: reference-validated` frontmatter label (if it passes) or is explicitly recorded as not-reference-validated (if it does not).
8. Confirm v1 is preserved at `specifications/reference-validation-v1.md` with frontmatter `status: superseded` and `superseded-by: reference-validation.md (v2)`.
