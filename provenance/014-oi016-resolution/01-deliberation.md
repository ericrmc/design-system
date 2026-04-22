---
session: 014
title: Deliberation — Synthesis
date: 2026-04-22
status: complete
perspectives-synthesised: [architect, operationalist, skeptic, outsider]
synthesis-type: quote-over-paraphrase-for-load-bearing-claims
---

# Deliberation Synthesis — Session 014

Four perspectives independently addressed Q1–Q7 on how to resolve OI-016 by designing a reference-validation mechanism per the user's ratified Option (d). Raw outputs preserved verbatim at `01a-perspective-architect.md`, `01b-perspective-operationalist.md`, `01c-perspective-skeptic.md`, `01d-perspective-outsider.md`. Citations use `[01a]`, `[01b]`, `[01c]`, `[01d]` with question references.

## Vote tally across questions

| Question | Architect [01a] | Operationalist [01b] | Skeptic [01c] | Outsider [01d] |
|---|---|---|---|---|
| Q1 core criteria count | 8 | 8 | 8 | 8 |
| Q2 iteration cap | 2/session | 2/session, 4 sessions max | 1 | 3 total rounds |
| Q3 validation shape | **(ii) within-session** | **hybrid (iii)+(ii)** | **hybrid (ii)+(iii)** | **sealed three-cell, cross-session** |
| Q4 defence layers | 5 | 5 with cost tiers | rejects structural-primary; adds counterfactual probe | 8 defences; contamination canary + distinctive-marker audit |
| Q5 §7 framing | **third named sense** (equal) | **third sense, anti-substitution** | **provisional substitute, not pillar** | **third named sense, anti-substitution** |
| Q6 methodology pass | N=4, 75%, 2 domains | N=5, 60%, version-reset | N=5, 80%, 3 domains | N=5, 80%, 3 types, ≥2 low-saturation |
| Q7 strongest failure | tacit structural contamination | Gatekeeper goes feral | retrieval-masquerading-as-design | benchmark theater |
| Q7 close OI-016? | yes, Skeptic as standing minority | yes, Skeptic as first-class minority | **no — provisionally addressed, remain open** | mechanism provisional; flatten-claims test |

**Shape split (Q3):** 3-of-4 for hand-off-containing hybrid; Architect is the sole within-session advocate. The majority includes the non-Claude Outsider.

**Framing split (Q5):** 3-of-4 for "third named sense" with explicit anti-substitution clauses; Skeptic alone holds "provisional substitute." The Skeptic's position is substantively closer to the others than the framing suggests — all four require anti-substitution language — but the Skeptic argues the framing itself is load-bearing against procedural self-deception.

**Pass-threshold split (Q6):** Outsider+Skeptic converge on stricter bars (N=5, 80%, 3 domains). Operationalist middle (N=5, 60%). Architect loosest (N=4, 75%, 2 domains). The majority of four, 2-of-4 at 80%, 1-of-4 at 60%, 1-of-4 at 75%. Cross-model (Outsider) aligns with adversarial (Skeptic) on the stricter bar.

## Q1 — Selection criteria for a reference case

**Four-way convergence on eight-criterion frame.** All four perspectives proposed eight criteria; the cores converge substantially. Shared elements across all four:

- **Documented provenance of reference solution** [01a C1, 01b C1, 01c 1, 01d first bullet]. The reference must be fetchable as a single primary document, have verifiable authorship, and be committed as an anti-drift witness before the exercise runs.
- **Constraint-separable-from-solution** [01a C2, 01b C2, 01c 2, 01d third bullet]. The constraint statement must not smuggle the solution; reading constraints alone, a fresh agent should be able to name >1 plausible solution family.
- **Low-saturation in training distributions** [01a C3, 01b C3, 01c 3, 01d fourth bullet]. Reference must not be a canonical worked example in common LLM training data. Operational test: Outsider+independent-Claude, given only constraints, must not reproduce the reference lexically.
- **Staged-constraint structure** [01a C7, 01b C4, 01c 4, 01d second bullet]. **Required per user steering.** Constraint set partitionable into initial brief + emergent tranches released at pre-committed methodology-internal triggers.
- **Domain-legibility to judges** [01a C4, 01b C8, 01c 5, 01d fifth bullet]. Judges must be able to distinguish structural match from lexical coincidence.
- **Bounded effort** [01a C5, 01b C5, 01c 6, 01d sixth bullet]. Reference + produce + comparison fit a sustainable session budget (≤10k tokens reference; ≤2–5 iterations total).
- **Representativeness of external-artefact claim** [01a C6, 01b C7, 01c 7, 01d seventh bullet]. Reference must be an artefact type the methodology actually claims to produce (protocol, sequence, decision aid, spec) — not a proof, a piece of software, a physical design.

**Perspective-unique additions adopted:**

- **C8 Architect: Reference-author-uncertainty declared.** The provenance writeup must include the author's own account of what they're uncertain about in their solution. This provides a tolerance band for divergence scoring. *Adopted* — this is the anti-oracle-treatment criterion.
- **C8 Skeptic: Pre-2022 reference date.** Reject references co-designed with LLMs. *Adopted* — this cuts a distinct contamination source.
- **C8 Outsider: Falsification-admitting.** The reference must have explicit mandatory constraints, optional elements, and failure conditions. *Adopted* — this blocks the "every divergence can be explained away" failure mode.

**Skeptic's flagged tension** [01c Q1 close-paragraph]: "Criteria (4), (5), and (8) are in tension with (3). A domain legible to Claude subagents, whose reference pre-dates 2022 and whose constraint structure is staged, is almost by construction a domain heavily represented in Claude's pretraining. This tension is not mine to resolve; it is a property of the design space the user has narrowed to." **Preserved as load-bearing dissent inside the selection criteria.** The synthesis does not claim the tension is resolved; it claims the tension is named and the mechanism attempts to probe around it (per Q4 defences). If the tension empties the candidate pool at sustainable rate, the mechanism fails per Q6(c) operationalist's noise-floor audit.

**Synthesis Q1 position:** Adopt the eight-criterion frame with all three perspective-unique additions (Architect C8 uncertainty, Skeptic C8 pre-2022, Outsider C8 falsification-admitting) consolidated into a single criterion list. Skeptic's tension preserved explicitly within the specification.

## Q2 — The comparison procedure

**Convergence on five-phase-ish structure; divergence on iteration count.** All four perspectives propose procedures with the same skeleton: (a) pre-run case packaging by a non-Produce agent; (b) Produce runs blind with staged release; (c) comparison at structural level with lexical distance as contamination signal; (d) classification into match/partial/divergence/contaminated; (e) iteration under specified rules.

**Convergence on 4-state classification taxonomy** [01a Stage 4, 01b (c), 01c match-taxonomy, 01d outcome-classes]:
- Pass / Match
- Partial match (iterate)
- Substantive divergence (potentially failure; or design-evidence-divergence per Operationalist/Architect)
- Contaminated / no-signal (exercise voided, case retired)

**Convergence on inverted lexical axis** [01a Q2 axis-list, 01b contamination-signals, 01c comparison-phase, 01d contamination-indicators]: high lexical match with reference is a failure signal (contamination), not a pass signal.

**Convergence on Produce-side isolation discipline**: Produce agents do not see the reference; search tooling constrained to exclude reference-retrieval; high lexical similarity at comparison time is detected and flagged.

**Divergence on iteration count:**
- Architect: 2 per session
- Operationalist: 2 per session, 4 sessions max per exercise
- Skeptic: 1 cap (hard)
- Outsider: 3 rounds total (initial + 2 revisions)

**Synthesis Q2 position — adopt the 5-stage procedure with a cap compromise:**

1. **Case packaging** (separate agent; seals reference; builds initial brief + staged constraint tranches + release triggers; commits anti-drift witness) — adopt Architect+Operationalist detail.
2. **Isolated Produce** (blind to reference; search constrained; staged release per tranche triggers) — adopt Skeptic+Outsider isolation rules.
3. **Emergent-constraint release during Produce** — adopt Architect Stage 2 + Operationalist Gatekeeper pattern.
4. **Structural comparison + constraint-satisfaction check + cross-model sanity** — adopt Operationalist Phase B; add Outsider's distinctive-marker audit as contamination-indicator check.
5. **Classification + iteration (cap: 2 iterations per case, distributed across sessions per Q3)** — compromise between Architect's 2/session and Skeptic's 1-cap. Rationale: 1-cap is too aggressive for a co-design mechanism explicitly designed to handle iteration; 3+ risks the training-loop failure Skeptic names. 2 total iterations across the exercise (not per-session) gives the methodology room to respond to a first-round miss without becoming an answer-key-chasing loop.

**Adopted operational elements:**
- **Gatekeeper brief** (Operationalist): separate `brief-gatekeeper.md` with tranche-tagged constraints and trigger rules; Gatekeeper agent holds the brief and releases on triggers.
- **Constraint-to-decision trace** (Outsider): Produce cell emits two artefacts each round — the artefact itself AND a short trace explaining why each major feature exists, referenced to released packets. This is the **process-trace requirement**.
- **Contamination-audit file** (Operationalist): each exercise commits `contamination-audit.md` recording the audits performed (lexical overlap, accidental-match ratio, tranche-0 sufficiency, cross-model divergence, distinctive-marker findings).

## Q3 — Shape of the validation step

**3-of-4 cross-model convergence on hand-off-containing hybrid over pure within-session.** Operationalist, Skeptic, and Outsider all propose shapes that distribute the exercise across multiple sessions. Only Architect argues for pure within-session.

- [Operationalist, Q3]: *"Exercise-scoped hand-off with in-session iteration budget. Session N (Produce session) opens with Gatekeeper brief construction... Session N+1 (Comparison session) opens with Gatekeeper full-constraint reveal + reference reveal..."*
- [Skeptic, Q3]: *"Within Session 015 (Produce + iterate)... At Session 016 (hand-off, reference-comparison)..."*
- [Outsider, Q3]: *"A sealed three-cell protocol combining hand-off across sessions with multi-agent judging. Cell 1: Curation. Cell 2: Produce. Cell 3: Validation."*

**Architect's minority** [01a Q3]: pure within-session with 4 internal roles (2 Produce agents, 1 cross-model comparator, 1 Claude arbiter). Argument: hand-off "introduces session boundaries in the middle of what should be a continuous design feedback loop… the emergent-constraint test requires that Produce agents be reacting to constraints as they arrive."

**Outsider-originated structural contribution — sealed three-cell protocol** [01d Q3]: the decisive structural framing. Separation of duties between **Curation Cell** (selects reference, builds packet schedule, seals reference), **Produce Cell** (runs methodology blind), **Validation Cell** (multi-agent judging with cross-model participation). This separation is a cross-model-originated structure; no Claude perspective produced the three-cell framing at this level. It operationalises the isolation discipline Q4 demands while accommodating the emergent-constraint steer.

**Synthesis Q3 position: adopt the Outsider-originated three-cell protocol, with internal iteration budget per Operationalist and Skeptic.**

Concrete shape:

- **Cell 1 — Curation (Session N-1 or session-opening sub-step of Session N).** One or two agents (non-Produce) perform reference selection per Q1 criteria; build the sealed case pack containing reference, staged constraint tranches, release triggers, and contamination-audit plan. Anti-tampering: the case pack is committed at a named commit hash before Produce Cell runs.
- **Cell 2 — Produce (Session N).** Produce agents run blind against tranche-0, with staged emergent-constraint release per the Gatekeeper. Up to 2 internal iterations within the Produce Cell triggered by in-session Validate findings. Emits artefact + constraint-to-decision trace.
- **Cell 3 — Validation (Session N+1).** Three judges minimum: (1) reference-faithful reader (sees reference; maps to rubric); (2) methodology-sympathetic reader (sees constraints and artefact; evaluates design response); (3) contamination auditor (looks for retrieval signals, leakage, distinctive-marker reproduction). **Cross-model mandatory in Cell 3** — at least one judge from a non-Claude family (Outsider via `codex exec`). If reference-faithful and methodology-sympathetic disagree materially, a 4th adjudicator agent reads both subreports and issues the verdict with dissent preserved.

**Convergence criteria:** Pass requires ≥2/3 structural agreement AND no unresolved contamination dissent. Any judge may file a blocking contamination dissent if they point to reference-specific features not derivable from released constraints. Contamination dissent dominates structural finding (per Outsider Q3 + Skeptic Q3): ambiguity on contamination is not resolved optimistically.

**Hand-off discipline for iteration:** If Cell 3 returns partial-match, iteration is permitted *once more*: Session N+2 re-runs Produce Cell with the Validation-cell's constraint-delta memo (not reference-informed brief per Skeptic). Maximum 2 Produce rounds × 2 Validation rounds = 4 sessions per exercise. Beyond that, case closes as unresolved and becomes a methodology-gap finding.

**Emergent-constraint handling in the adopted shape:** The Gatekeeper releases tranches during the Produce Cell on methodology-internal triggers (first draft emission, first Validate finding, explicit Produce question). Cell 3's Validation receives the full released tranche set + the artefact + the reference. The three-cell separation does NOT weaken emergent-constraint handling — the emergence happens inside the Produce Cell's iteration loop, and the Validation Cell verifies after-the-fact that the methodology handled the staged release well (which is itself load-bearing, per Skeptic [01c Q3]: *"the validation is of the methodology's process as much as the artefact's content"*).

**Why the 3-cell adoption over Architect's within-session:** the emergent-constraint requirement is preserved inside Cell 2's iteration budget (2 rounds). The hand-off between Cell 2 and Cell 3 establishes the separation of duties Skeptic [01c Q3 correlated-errors], Outsider [01d Q3 role-separation], and Operationalist [01b Q3 cost-structure] all independently identify as load-bearing. Architect's concern (session boundaries in the middle of the loop) is real but is mitigated by the within-Cell-2 iteration budget and the constraint-delta-memo discipline for Cell 2-to-Cell 2 re-runs.

**Architect's minority preserved as first-class dissent** with a specific reopening condition: if the first exercise (Session 015) shows Cell 2-to-Cell 3 hand-off consistently losing design-intent information that in-session iteration would have preserved — i.e., if the Validation Cell's findings repeatedly require Produce Cell to reconstruct context a continuous loop would have retained — the Architect's within-session proposal is the operational warrant for revising Q3 toward pure-within-session.

## Q4 — Defence against pretraining-contamination / circularity

**Four-way convergence: no single defence is airtight; layered defences are necessary.** All four perspectives adopt this frame explicitly.

- [Architect, Q4 close]: *"The defences are layered; they are not airtight."*
- [Operationalist, Q4]: layered defences D1–D5 with cost tiers; audit-trail requirement.
- [Skeptic, Q4]: *"Survives adversarial pressure only for genuinely novel problem formulations, which are scarce."* — but evaluates each defence and adopts counterfactual probing as strongest.
- [Outsider, Q4]: *"'Just pick obscure references' is not a defence. It only lowers prior probability."* — 8 defence requirements with contamination canary + distinctive-marker audit as new elements.

**Synthesis Q4 position: adopt a composite 7-layer defence stack, each named with source.**

**L1. Reference selection saturation gate** [Architect C3 + L1, Operationalist C3 + D1, Skeptic Q1-3, Outsider contamination-canary]: before case adoption, Outsider (GPT-5) AND independent Claude given constraints-only, asked to produce solution. If either produces lexical match >30% 5-gram overlap with reference, case rejected. *Outsider-originated refinement: "contamination canary runs"* — thin prompts derived from tranche-0 fired at both model families; if they spontaneously emit reference's idiosyncratic structure/labels/sequence, discard the case.

**L2. Produce-side contextual isolation** [Architect L2, Operationalist Phase-A, Skeptic isolation-discipline, Outsider strict-blinding]: Produce cell has tooling but search exclusion list enforced at pre-commit; no reference text, URL, or reference-identifying phrasing in Produce context.

**L3. Cross-model divergence analysis** [Architect L3, Operationalist D4, Skeptic Q4(iii), Outsider convergence-interpretation]: Cell 3 validators span Claude-family AND non-Claude-family. **Cross-family convergence on reference-text is contamination evidence, not pass evidence.** Cross-family divergence with both satisfying constraints is design evidence.

**L4. Structural + lexical-inverted comparison** [Architect L4, Operationalist Phase-B, Outsider distinctive-marker audit]: Cell 3's rubric weights structural correspondence primarily, lexical distance as contamination signal (inverted axis). **Skeptic's warning adopted** [01c Q4(iv)]: "structural match suggests the much harder-to-catch case of copying the shape of a solution while varying the words. This defence makes contamination easier to miss, not harder." Mitigation: L4 is never adopted alone; it always runs with L5 + L6 + L7.

**L5. Counterfactual probing** [Skeptic Q4(v), adopted as load-bearing]: after Produce completes, modify one or more constraints off-distribution for the reference. Ask the methodology to re-produce. If the methodology tracks the new constraint genuinely, design evidence. If it produces a near-copy of the original, retrieval evidence. *This is the only defence that actively probes design vs retrieval rather than passively measuring output overlap.* **Adopted per Skeptic's argument that all other defences are passive.**

**L6. Process-trace requirement** [Outsider Q4 + Q2]: Produce cell emits the constraint-to-decision trace with the artefact. Cell 3 validators check: does each major artefact element trace to a released constraint plus methodology decision? Elements lacking constraint-grounded rationale do not count as validation evidence even if they match the reference.

**L7. Unexpected-detail rule + distinctive-marker audit** [Outsider Q4, adopted]: Cell 3 validators explicitly list rare markers in the reference (branded labels, unusual ordering, arbitrary counts, signature metaphors). If the produced artefact reproduces those markers absent constraint-grounded rationale, contamination evidence. This is the specific defence against "structural-plagiarism of a pretrained answer" that Architect [01a Q4 close] names as the L1–L4 gap.

**Contamination-audit file** [Operationalist D-audit]: each exercise commits `contamination-audit.md` recording L1 saturation-test results, L5 counterfactual-probe results, L3 cross-model divergence characterisation, L7 distinctive-marker findings, lexical-overlap scores, accidental-match ratio, tranche-0 sufficiency, iteration count. The file is the audit trail that makes contamination detectable rather than hidden.

**Synthesis-honest-scope statement** [adopted from Architect Q4 close]: **the 7-layer defence validates that the methodology produces structurally-sound artefacts; it does not fully validate that the methodology is producing those artefacts by methodology rather than by taste.** Tacit structural contamination (agent having learned solution class during pretraining without learned specific instance) is residual risk not closed by any defence. This is a known limitation of the mechanism, preserved in the specification.

**Skeptic's regime-statement** [01c Q4 close]: *"For classical engineering problems with canonical solutions, widely-taught design patterns, textbook-standard protocols, and heavily-documented technical canon, reference-validation is not evidence of methodology capability regardless of mechanism."* **Adopted in full as a scope boundary.** The Q1 criterion list (C3 low-saturation, C8 pre-2022, C8 falsification-admitting) is designed to exclude this regime; the Skeptic's warning is that the exclusion is imperfect and the sweet-spot domain-pool may be narrower than the brief implies.

## Q5 — Kernel §7 revision

**3-of-4 cross-model convergence on third-named-sense framing; Skeptic alone holds provisional-substitute.** Architect, Operationalist, and Outsider all propose "Reference validation" as a third named validation sense alongside Workspace and Domain. Skeptic proposes a paragraph explicitly framed as "provisional substitute, not pillar" with mandatory dissent clause.

- [Architect, Q5(a)]: *"Third named sense, not an extension of Domain validation."*
- [Operationalist, Q5]: three senses: Workspace, Domain, Reference. Explicit anti-substitution clause: *"Reference validation does not substitute for domain validation when a domain-actor is available."*
- [Outsider, Q5]: three senses with anti-substitution: *"Reference validation supplies evidence about the methodology's capacity to derive an artefact under comparable constraints; it does not by itself count as domain validation for live use."*
- [Skeptic, Q5]: *"Reference validation is a provisional substitute for domain validation, usable only when no domain-actor is available and the alternative is producing an artefact without any external check… Reference validation does not establish that the artefact functioned in its intended use."*

**Underlying four-way convergence:** all four insist on explicit **anti-substitution language** in the kernel text. All four state that reference-validation does not establish intended-use functioning. The divergence is whether the framing itself names reference-validation as "provisional" (Skeptic) or as equal-but-distinct third sense (others).

**Synthesis Q5 position: adopt the three-named-sense framing (majority) AND adopt the load-bearing elements of Skeptic's dissent into the kernel text.**

Specifically:

- The kernel §7 introduces three senses: Workspace validation, Domain validation, Reference validation.
- Reference validation carries **explicit scope-statement** in the kernel text matching Skeptic's "does not establish intended-use functioning" requirement.
- Reference validation carries **anti-substitution clause** (all four converge): cannot substitute for domain validation when a domain-actor is available.
- Reference validation carries **label discipline** [Architect Q5]: artefacts carry `validation: workspace-only | domain-validated | reference-validated` frontmatter tag; multiple labels permitted; labels are additive.
- Kernel text summarises mechanism and defers detail to a separate specification file.

**Candidate kernel §7 text for synthesis** (drawing Operationalist's operational-register + Outsider's clear anti-substitution wording + Skeptic's scope-statement + Architect's label discipline):

```markdown
#### 7. Validate

Validate the session's output at each level on which it makes claims. Three senses apply.

**Workspace validation** applies to every session. Check that:
- New specifications don't contradict existing ones
- Specifications describe the workspace as it actually is
- Provenance records are complete and well-formed
- Open issues reflect the actual state of uncertainty

**Domain validation** applies when a session produces or revises an artefact intended for use outside the workspace and a domain-actor is available. Obtain evidence from the domain-actor who holds the problem the artefact addresses — the user of a sequence, the reader of a specification, the participant in a process, or an equivalent — that the artefact functioned for its intended use. Record who performed the validation, what was tried, what happened, and whether modifications were requested. Domain validation may complete out-of-session; when it does, the receiving session records the report and decides whether it triggers revision.

**Reference validation** applies when a session produces an external-intent artefact and no domain-actor is available. A reference-validation exercise pairs the methodology's Produce step (run blind against a staged constraint tranche set whose emergent constraints surface during the run) with comparison against a pre-selected documented proven solution the Produce agents do not see. The exercise runs across a small number of sessions in a sealed three-cell protocol (Curation, Produce, Validation) specified in `specifications/reference-validation.md`. The exercise records constraint-satisfaction, structural correspondence, cross-model divergence, and a contamination audit.

**Reference validation supplies evidence about the methodology's capacity to derive artefacts under stated constraints. It does not establish that the artefact functioned in its intended use. It does not substitute for Domain validation when a domain-actor is available.** Artefacts passing reference-validation carry the label `validation: reference-validated` in frontmatter and retain that scoping in any later citation.

If any validation reveals problems, they are either fixed in this session (return to Produce) or recorded as open issues for subsequent sessions.
```

The bolded sentence near the end is the load-bearing Skeptic-dissent-into-kernel. It matches the core of Skeptic's Q5 position ("does not establish that the artefact functioned in its intended use") without using the word "provisional" — which would have fought the majority's equal-third-sense framing. The wording is Outsider-adjacent but tightened per Skeptic.

**Separate specification file for mechanism detail:** create `specifications/reference-validation.md` as a new v1 spec (`supersedes: none`) containing the Q1 selection criteria, Q2 comparison procedure, Q3 three-cell shape, Q4 seven-layer defence stack, Q6 pass criteria, Q7 failure modes. This keeps the kernel light and lets the mechanism spec evolve with exercises without kernel churn [Operationalist Q5 rationale adopted].

**What changes about the receiving-session protocol:** Reference validation has no out-of-session completion pathway equivalent to Domain validation. The validation completes across the three-cell protocol's 2–4 sessions. No receiving-session decision is required after-the-fact; Cell 3 is the validation record.

**Skeptic's framing dissent preserved as first-class minority inside the kernel revision decision (not inside the kernel text itself):** the Skeptic's "provisional substitute" framing is recorded verbatim in the session decision record and in OI-016's disposition. If the label discipline fails in use (artefacts referenced without the reference-validated qualification; reference-validation treated as equivalent to domain-validation in external communication), the Skeptic's minority is the explicit warrant for re-opening OI-016 and revising kernel §7 toward Skeptic's stricter framing.

## Q6 — Iteration and pass criteria

### (a) Artefact pass

**Convergence on multi-condition pass requirement.** All four perspectives require all of:
- Constraint satisfaction complete
- Structural match / equivalence
- No unresolved contamination dissent
- Judge concurrence

**Synthesis adopts the strictest Outsider+Skeptic formulation** (the cross-model+adversarial convergence carries weight on the Q6 adversarial surface):

An artefact passes reference-validation when **all five** of the following hold in Cell 3:

1. All mandatory constraints from tranche-0 and all emergent tranches released during the run are satisfied (per methodology-sympathetic reader + cross-model sanity).
2. Structural correspondence score ≥ 80/100 (adopting Outsider's 80-threshold over Architect's 70; per adversarial+cross-model convergence).
3. Lexical distance above contamination threshold (< 30% shared 5-gram tokens with reference).
4. No unresolved contamination dissent from the contamination-auditor judge (per Outsider "ambiguity on contamination should not be resolved optimistically" + Skeptic "contamination dominates structural finding").
5. L5 counterfactual probe demonstrates genuine differentiation (per Skeptic's positive-design-evidence requirement).

**Partial match triggers one additional Produce round** (per Q2 iteration cap). After the second Produce round, result is final (pass / fail / unresolved-methodology-gap).

### (b) Methodology pass

**Outsider+Skeptic strict bar adopted over Architect's loose and Operationalist's middle:**

The methodology's external-artefact claim is considered validated at the methodology level when:

- **N = 5 reference cases completed** (not 4; Architect's N=4 is too few to distinguish methodology success from case-selection luck).
- **≥ 4 of 5 pass** (80% threshold; Outsider+Skeptic convergence). Neither 100% (suspicious) nor 60% (below defensibility).
- **Cases span ≥ 3 distinct artefact types or domains** (Outsider+Skeptic convergence over Architect's 2).
- **≥ 1 case selected from the difficult-to-contaminate tail** (Skeptic Q6 close; Outsider ≥2 low-saturation; adopt Skeptic's 1-minimum as binding, Outsider's 2-minimum as aspirational).
- **No counted pass may carry unresolved contamination dissent** (Outsider + Skeptic).
- **Methodology-version reset** [Operationalist Q6]: kernel revisions reset the count; a new kernel is a different methodology and owes new evidence. Each exercise carries a `methodology-version` tag; passes accumulate against the tagged version.

**Partial-credit rule** [Operationalist-originated; adopted]: an exercise that fails with `fail-methodology-gap`, produces a fix in subsequent session(s), and re-runs against a similar reference case, counts as 0.5 toward the pass threshold (not 1.0). This blocks the fail-deliberately-then-fix gaming path.

### (c) Mechanism-failure vs methodology-gap distinction

**Outsider-originated three-core-properties test adopted as primary:** the mechanism is falsified if any two of three core properties fail.

- **Blindness**: producers are isolated from the reference (no context access, no retrieval tooling access).
- **Stageability**: constraints can be packetized without solution-bearing language; releases are at pre-committed triggers; no adaptive staging.
- **Discriminability**: validators can distinguish structural adequacy from retrieval or vibe-similarity; pass/fail signal is reproducible across re-runs of the same inputs.

**Thresholds:**
- If Session 015 shows failure of **any two of these three core properties**, mechanism is falsified; methodology returns to pause.
- A **single hard leak of the reference into Produce** is mechanism-falsifying for that run (per Outsider).
- A **single methodology gap with the three core properties intact** is not mechanism failure; gap is recorded, addressed in subsequent sessions.

**Additional mechanism-failure patterns** [Architect+Operationalist]:
- Comparator/arbiter disagreement rate > 60% across a run series — two-role design does not produce stable classification.
- Noise-floor audit [Operationalist Q6c] within 15pp of shuffled-constraint baseline — mechanism's signal indistinguishable from noise.
- Pass on seeded-contaminated runs + Fail on seeded-clean runs [Architect Q6c] — signal inverted.

**Methodology-gap looks like:** the Cell 3 verdict is `fail-methodology-gap`; the gap-surface report names a specific step (Read, Deliberate, Decide, Produce) and specific failure mode; a targeted fix is proposable; re-run against a similar case shows the gap closed; the contamination audit was clean for the failing exercise.

**Skeptic's anti-laundering rule** [01c Q7 three-consecutive-"gap-surfaced" clause; adopted]: if three consecutive exercises each "surface a gap" each "addressed in subsequent session" with none producing a passing result, the pattern is not gap-surfacing; it is methodology-failure being serially relabelled. Methodology returns to pause.

## Q7 — Risks and dissent

**Four-way convergence on layered strongest-failure-modes.** Each perspective names a concrete failure mode that survives their own Q1–Q6 defences:

- [Architect, Q7]: *"Tacit structural contamination that the defences do not catch."* — agent learned solution class during pretraining; produces structurally-similar solution via "taste" rather than methodology.
- [Operationalist, Q7]: *"The Gatekeeper goes feral."* — experimenter-demand-characteristics contamination where the session-author unconsciously stages releases to help the methodology succeed.
- [Skeptic, Q7]: *"Retrieval-masquerading-as-design on reference cases drawn from the canonical-solution regime."* — structural matches read as validation evidence that measure only training-distribution overlap with reference-distribution.
- [Outsider, Q7]: *"Benchmark theater."* — the workspace starts choosing references legible to models, packetising them in solution-shaped language, scoring surface resemblance as evidence.

Each of these names a real failure mode. They are substantially convergent at the level "the mechanism is vulnerable to adversarial-selection-and-packaging that produces passes without methodology-capability evidence." The mechanism's defences attempt to block each; none close them completely.

**Falsifiability conditions — synthesis adopts union:** the mechanism's adequacy is falsified, and methodology returns to pause, if any of these are observed in first-exercise or accumulate across exercises:

1. **Outsider's three-core-properties test** [01d]: failure of any 2 of Blindness / Stageability / Discriminability in Session 015.
2. **Skeptic's counterfactual-probe inversion** [01c Q7]: counterfactual-probe results show methodology produces artefact tracking original reference rather than modified constraint.
3. **Architect's "too fast" pattern** [01a Q7]: single Produce iteration arriving at ≥80% structural alignment across multiple cases despite passing contamination tests.
4. **Operationalist's noise-floor inversion** [01b Q6c + Q7]: pass-rate within 15pp of no-methodology constraint-only baseline.
5. **Three-consecutive-"gap-surfaced"-non-passes** [01c Q7]: serial relabelling of failure.
6. **Label discipline collapse** [01a Q7 + 01d Q7]: `validation: reference-validated` artefacts used externally without the label qualification; reference-validation referred to as "validated" simpliciter.

**Procedural-self-deception observables — synthesis adopts union:**
- Reference cases consistently hand-picked after "could the methodology do this?" first-glance (Architect).
- Findings written in reference-vocabulary that leaks back into Produce-side context (Architect).
- Between-session methodology revisions moving the methodology closer to the reference pool's shape rather than addressing external-design considerations (Architect).
- Gatekeeper-brief edits mid-exercise (Operationalist — git log of `brief-gatekeeper.md` commits after Produce Cell open).
- Absence of `fail-methodology-gap` verdicts across exercises — 5/5 pass is suspicious (Operationalist).
- Validators' "close enough to reference" pass based on names/slogans/formatting rather than functionally-necessary structure (Outsider).
- Iterations that move artefact closer to reference's wording after validators have seen reference — answer-key chasing (Outsider).

### Session 013 Skeptic carry-forward — substantive engagement

All four perspectives explicitly engage the Session 013 Skeptic strong-pause minority. Positions:

- **Architect** [01a Q7]: *"I accept the Skeptic's premise… The mechanism I propose does not restore domain validation. It introduces a third sense of validation, named clearly as such, with explicit labelling."* Proposes closing OI-016 on mechanism adoption with Skeptic's position preserved as standing minority against a specific re-opening trigger (label discipline collapse).

- **Operationalist** [01b Q7]: *"The Skeptic's position should be preserved as first-class minority within the adopted mechanism: the mechanism is provisional; its adequacy is itself under test."* Proposes OI-016 closes but with preserved minority.

- **Skeptic** [01c Q7]: *"Option (d) is therefore inadequate in principle to the problem OI-016 names… It can be adopted as a less-bad-than-nothing substitute… But adopting it does not close OI-016 at the level Session 009's insight set. OI-016 should remain open, flagged as 'provisionally addressed by reference-validation mechanism, with the prior structural concern preserved.'"* Proposes OI-016 does NOT close.

- **Outsider** [01d Q7]: *"My preserved dissent, stated strongly: even if this mechanism works, it validates a narrower claim than the old loop did. It can support 'the methodology can derive artefacts that resemble proven solutions under blinded staged constraints.' It cannot honestly mean 'the methodology's new external artefacts work in live domains.'"* Does not directly specify OI-016 disposition but the narrower-claim framing aligns substantively with Skeptic.

**Split on OI-016 disposition: 2-2.** Architect + Operationalist for close-with-minority. Skeptic + Outsider for the stronger position that the mechanism doesn't close the issue Session 009's insight named. *This is 2-2 including the cross-model perspective aligning with the adversarial perspective.*

**Synthesis Q7 OI-016 position — adopt the Skeptic+Outsider framing with a compromise:** **OI-016 moves from Open to "Resolved — provisionally addressed pending first-exercise".** The OI's text is updated to record the adopted mechanism, the Skeptic+Outsider joint position that the mechanism validates a narrower claim than the original domain-validation loop, and the six falsifiability conditions above. OI-016 re-opens automatically if any falsifiability condition fires.

This is not the Skeptic's preferred disposition (the Skeptic wants OI-016 to remain Open). It is stronger than the Architect+Operationalist's close-with-minority. It captures what the cross-model+adversarial convergence requires: the mechanism is adopted, but it does not settle the question Session 009 opened. The question returns to the open list the moment the mechanism shows strain.

The word "Resolved" is used reluctantly because the workspace's OI format uses Open/Resolved as the status field. The qualifier "provisionally addressed pending first-exercise" is load-bearing and must appear wherever the OI-016 status is cited.

**Fallback-to-pause triggers — adopted:** any of the six falsifiability conditions above; plus Skeptic's specific additions (inability to find low-contamination cases at sustainable rate per Q6c noise-floor; repeated contamination dissents not conservatively resolvable; two consecutive cases where packetization itself smuggles solution per Outsider).

## Cross-model contributions to adopted content — count for OI-004 criterion 3

Outsider-originated contributions that materially shape adopted Session 014 content:

1. **Sealed three-cell protocol (Curation + Produce + Validation) as the Q3 adopted shape.** No Claude perspective produced the three-cell separation-of-duties framing at this level. Architect proposed pure within-session with 4 internal roles; Operationalist proposed session-sequenced hand-off; Skeptic proposed hybrid within-session-then-hand-off. None produced the curation/produce/validation trinity as a primary structural distinction. Outsider's Q3 formulation carries the majority adoption.

2. **Contamination canary (pre-case-adoption thin-prompt probe) as L1 refinement.** Architect's L1 is the saturation test with lexical-overlap threshold; Operationalist's D2 is a pre-Produce probe on the target Produce model. The Outsider's refinement — thin prompts derived from P0 fired at multiple model families, looking for spontaneous emission of reference's idiosyncratic structure — is a distinct operational test that strengthens L1 against Claude-specific contamination detection gaps.

3. **Distinctive-marker audit (L7) with rare-marker enumeration.** Architect L4 is lexical-threshold-based; Operationalist Phase-B's accidental-match ratio is related but coarser. Outsider's explicit list-rare-markers-then-check-reproduction framing is a distinctive mechanism no Claude perspective produced at this operational granularity.

4. **Three core properties (Blindness + Stageability + Discriminability) as mechanism-failure test.** No Claude perspective produced this three-property formulation. Architect's four mechanism-failure patterns, Operationalist's four patterns, Skeptic's two criteria — all enumerate thresholds but none distil the mechanism's integrity into three inter-dependent core properties. The Outsider's articulation is adopted as the primary mechanism-failure test in Q6(c).

5. **"Benchmark theater" framing for strongest failure mode.** Architect ("tacit structural contamination"), Operationalist ("Gatekeeper goes feral"), Skeptic ("retrieval-masquerading-as-design") each name a real failure. Outsider's *"benchmark theater"* is a distinct characterisation — the failure as a genre of performance rather than as a local mechanism-violation. The framing shapes the synthesis's union of falsifiability conditions.

6. **Narrower-claim preservation in Q7 OI-016 disposition.** The Skeptic+Outsider 2-2 convergence on the stronger "narrower claim" framing (vs Architect+Operationalist's close-with-minority) shapes the adopted disposition (Resolved — provisionally addressed pending first-exercise; re-opens on falsifiability). Without the Outsider's Q7 narrower-claim framing, the Skeptic would be a 1-of-4 minority and the adopted disposition might have been closer to Architect+Operationalist's close-with-minority rather than the stronger state-change that preserves the OI's structural weight.

**Six concrete Outsider-sourced contributions**, continuing the Sessions 011/012/013 five-per-session pattern at +1. Cumulative OI-004 criterion-3 data points across Sessions 005–014: **forty**.

## Recommendations for the Decide activity

1. **Adopt the reference-validation mechanism** as synthesised. Kernel §7 v3 → v4 substantive revision per Q5 candidate text. Create `specifications/reference-validation.md` v1 as a new specification containing Q1–Q7 mechanism detail. Preserve kernel v3 as `methodology-kernel-v3.md`.

2. **Revise `workspace-structure.md`** if the mechanism introduces new canonical paths. The three-cell protocol introduces `brief-gatekeeper.md`, `contamination-audit.md`, and `comparison-verdict.md` as per-exercise artefacts; these need a canonical path structure. Proposed: `applications/NNN-[slug]/exercise-materials/` for the sealed case pack and `provenance/NNN-[slug]/` for session-level records. Decide whether this needs a workspace-structure v2 → v3 substantive revision or a minor annotation.

3. **Preserve Skeptic's "provisional substitute" framing dissent** as first-class minority within the kernel §7 v4 revision decision record AND within OI-016's disposition text. The minority is operationalised as re-opening trigger: if label discipline collapses in use, the minority is the warrant for revising §7 toward Skeptic's stricter framing.

4. **Preserve Architect's within-session shape** as first-class minority within the Q3 shape decision. Re-opening trigger: if hand-off Cell 2-to-Cell 3 consistently loses design-intent information, the within-session proposal is the warrant for revising Q3.

5. **Move OI-016 to "Resolved — provisionally addressed pending first-exercise"** with the six falsifiability conditions as automatic re-opening triggers. Preserve the Session 013 Skeptic+Session 014 Skeptic+Outsider joint dissent that the mechanism validates a narrower claim than the original domain-validation loop.

6. **Record Session 014 watchpoints** for Session 015+ first-exercise monitoring:
   - WX-14-1: Contamination canary efficacy (does L1 meaningfully reduce candidate pool?).
   - WX-14-2: Three-cell hand-off information loss (Architect's minority-reopening trigger).
   - WX-14-3: Label discipline preservation (Skeptic's minority-reopening trigger).
   - WX-14-4: Gatekeeper-brief edit frequency (Operationalist's procedural-self-deception observable).
   - WX-14-5: Pass-rate distribution across exercises — presence/absence of `fail-methodology-gap` verdicts.
   - WX-14-6: Cross-model convergence pattern in Cell 3 (is cross-model divergence yielding useful contamination signal?).

7. **OI state housekeeping.** OI-016 → Resolved-provisional (new state language). OI-004 criterion-3 +6 data points (cumulative 40); tally advances from 4-of-3 to **5-of-3** (fifth required-trigger deliberation with non-Claude participation; D-023_1 fires on kernel revision). OI-002 observation (creation of `specifications/reference-validation.md` extends the creation-pattern from Session 012's identity.md; no formal heuristic update). OI-007 count: depends on closure — likely 13→12 if OI-016 resolves. OI-005 not touched. OI-008 could be revisited since reference-validation mechanism uses audit-file artefacts — consider as follow-up.

## End of synthesis

The synthesis recommends three decisions:

- **D-069:** Adopt the reference-validation mechanism; revise kernel §7 (v3 → v4, substantive); create `specifications/reference-validation.md` v1.
- **D-070:** Resolve OI-016 to "Resolved — provisionally addressed pending first-exercise" with six automatic re-opening triggers; preserve Skeptic+Outsider joint narrower-claim dissent; preserve Architect within-session minority.
- **D-071:** OI state housekeeping; Session 014 watchpoints WX-14-1 through WX-14-6; OI-004 tally advance to 5-of-3.
