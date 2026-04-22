---
session: 021
title: Shared Brief — OI-004 Closure Criterion-4 Articulation
date: 2026-04-22
status: anchor-committed
---

# Shared Brief — Session 021 OI-004 Criterion-4 Articulation

**This brief is committed as the deliberation anchor before any perspective-launch per `multi-agent-deliberation.md` v3 §Stance Briefs.** The same shared sections (§1–§7, §9–§11) are given to all four perspectives. Each perspective receives only its own §8.X role-specific stance (others' stances are visible in this committed audit-anchor file but were not included in any individual perspective's dispatched brief, preserving independence).

## §1 — Methodology context

You are participating in the self-development application of the Selvedge engine (per `PROMPT.md` dispatcher + `prompts/development.md` + `specifications/engine-manifest.md` v1). Session 021 has opened under Path (B) of the Session 020 close menu: **OI-004 closure criterion-4 articulation**. The operator ratified this path from the four-option AskUserQuestion presented at session open (the four options were drawn from Session 020 close §Next session paths A1/A2/A3, B, C, D, with E "operator-directed" as the implicit fifth).

The engine-definition spec set (per `engine-manifest.md` §3) at `engine-v1` is: `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, `specifications/methodology-kernel.md`, `specifications/multi-agent-deliberation.md`, `specifications/validation-approach.md`, `specifications/workspace-structure.md`, `specifications/identity.md`, `specifications/reference-validation.md`, `specifications/engine-manifest.md`, `tools/validate.sh`. **A substantive revision to `multi-agent-deliberation.md` bumps `engine-v1` → `engine-v2` per `engine-manifest.md` §5.** This deliberation's adopted decisions may force that bump.

This deliberation is **D-023-triggering** per the v3 spec's §Closure Criteria for OI-004 and §When Non-Claude Participation Is Required (clauses 2 and 4):

> 2. Creates or substantively revises `multi-agent-deliberation.md`.
> 4. Asserts a change in the state of OI-004.

Both clauses are likely to fire on this session's adopted decision (clause 2 if criterion-4 articulation is added to the spec; clause 4 if OI-004 state is changed from "Closable pending criterion-4 articulation" to a new state). Non-Claude participation is therefore **required**. The Outsider perspective satisfies this requirement.

## §2 — Problem statement

OI-004 ("Incorporating genuinely independent perspectives") was surfaced in Session 001 and has been the workspace's longest-running open issue (21 sessions of accumulated state). Per `multi-agent-deliberation.md` v3 §Closure Criteria, OI-004 may be considered for closure when **all four** of the following criteria are satisfied:

> 1. **Participant independence.** At least one participant in qualifying deliberations has `training_lineage_overlap_with_claude: independent-claim` (non-Anthropic model) or `participant_kind: human` with a `participant_selection_method` other than `self`.
> 2. **Sustained practice.** Non-Claude participation has occurred in at least three required-trigger deliberations across different sessions, recorded correctly per the schema above.
> 3. **Recorded impact.** The synthesis or decision records show that non-Claude input shaped at least one outcome — the cross-lineage-influence ratio (see Open Extensions) is non-zero.
> 4. **Articulation.** A successor decision defines what "substantively different training provenance" means and enumerates acceptable participant kinds.

**Status at Session 021 open** (per `open-issues.md` OI-004 + `multi-agent-deliberation.md` v3 §Closure Criteria):

- Criterion 1: **satisfied** since Session 005 (Outsider GPT-5/5.4 via `codex exec`, `training_lineage_overlap_with_claude: independent-claim`).
- Criterion 2: **satisfied** at Session 009 (3-of-3); extended to **6-of-3** at Session 017. Voluntary:required tally currently 7:6 after Session 020.
- Criterion 3: **satisfied** since Session 005; cumulative criterion-3 data points across Sessions 005–019 = **50** (cited in OI-004 record with per-session breakdowns).
- Criterion 4: **unmet.** No session has yet deliberated this articulation. The OI is "Closable pending criterion-4 articulation," not "Closed."

**Session 021's task:** deliberate criterion 4 — articulate what "substantively different training provenance" means and enumerate acceptable participant kinds. Decide whether the resulting articulation, taken with criteria 1–3 already satisfied, is sufficient to close OI-004, or whether closure should be deferred pending further conditions the deliberation identifies.

This is the methodology's first attempt at criterion-4 articulation across 20 prior sessions of OI-004 evolution. Why the long deferral: criterion 4 is the only criterion that requires "deliberate-and-articulate" rather than "accumulate-data-points-and-meet-threshold." Sessions that incrementally extended criteria 1–3 did so as side effects of other work (kernel revisions, spec revisions, OI-004 state assertions); criterion-4 articulation has no such piggyback opportunity — it requires its own deliberative session.

## §3 — Current spec text

### §3.1 — `multi-agent-deliberation.md` v3 §Closure Criteria for OI-004

(Quoted verbatim above in §2.)

### §3.2 — Existing schema fields that approximate criterion-4's substance

The current schema in `multi-agent-deliberation.md` v3 §Heterogeneous-Participant Recording Schema already contains *categories* that adjacent to (but not equivalent to) the criterion-4 articulation:

**Layer 2 manifest field `participant_kind`:**

```yaml
participant_kind: claude-subagent | anthropic-other | non-anthropic-model | human | unknown
```

**Layer 2 manifest field `training_lineage_overlap_with_claude`:**

```yaml
training_lineage_overlap_with_claude: known-overlap | unknown | independent-claim
```

**Layer 2 manifest field `participant_selection_method`:**

```yaml
participant_selection_method: self | solicited-from-graph | solicited-externally | pre-registered
```

**Synthesis frontmatter field `participants_family`:**

```yaml
participants_family: claude-only | mixed-anthropic | cross-model
cross_model: true | false
```

**The Claude-Only-Is-Not-Cross-Model rule** (v3 §Heterogeneous-Participant Recording Schema):

> A deliberation whose participants are all members of the Claude model family (any mix of Opus, Sonnet, Haiku; any sizes; any post-training runs) does not constitute cross-model participation for OI-004 purposes. The manifest must record `participants_family: claude-only` (or `mixed-anthropic` for explicit size-mixing) and `cross_model: false`. Intra-family size-mixing may be recorded for separate reasons (see OI-011) but contributes nothing to OI-004.

**Limitations §A single non-Claude participant narrows OI-004 less than its presence suggests** (v3 §Limitations):

> One human reviewer selected from the operator's social graph shares correlated priors with the operator; one non-Anthropic model accessed once may not reveal training differences that emerge only over many interactions. Closure of OI-004 requires sustained practice (see the Closure section).

These fields and rules **partially** answer criterion 4 but do not constitute its articulation:

- `training_lineage_overlap_with_claude: independent-claim` is a *self-claimed* property; the spec does not say what makes a claim of independence credible.
- `participant_kind` enumerates categories (claude-subagent, anthropic-other, non-anthropic-model, human, unknown) but does not say which categories *count* for OI-004 narrowing or in what combinations.
- The Claude-Only rule excludes intra-Claude-family mixing but does not affirmatively define what *is* sufficient.
- The Limitations note flags weak forms (operator's social graph; single access) but does not enumerate when forms are strong enough.

Criterion 4 calls for the *affirmative* articulation: not just what doesn't count, but what does count and on what basis.

### §3.3 — Existing OI-004 record observations relevant to articulation

From `open-issues.md` OI-004 record:

- **Voluntary:required ratio.** 7:6 after Session 020. The methodology has sustained non-Claude participation across 13 sessions (6 required-trigger + 7 voluntary). This is evidence that cross-model discipline is sustained roughly equally across required and voluntary contexts (Session 012 watchable pattern, restated at Session 014, restated at Session 020).
- **Frame-replacement vs frame-completion.** Per Session 020 close §Honest notes #4: "Session 014 Outsider originated three-cell protocol (structural innovation at the content level); Session 017 Outsider originated H4 layered model (frame-replacement at the concept level); Session 019 Outsider refined rejection conditions and trigger-text (textual precision); Session 020 Outsider produced 'indexes drifted to dossiers' type-drift diagnosis (frame-replacement at the type-theory level). Session 017 + Session 020 establish frame-replacement as a distinct Outsider contribution kind." This is qualitative evidence that non-Claude participation produces distinguishable contributions, not just dissent-votes.
- **Mechanical-gate cross-family invocation** (Session 018, per OI-004 Session 018 note). Codex exec GPT-5.4 was invoked mechanically as part of the L1 contamination canary and the C3 5-gram overlap test; cross-family divergence between Claude Opus 4.7 and GPT-5.4 on the same C3 input shaped a methodology decision (rejection of D2). This is a distinct evidence category from deliberation-based criterion-3 data points — mechanical invocation also produces cross-family signal.
- **Cumulative criterion-3 data points: 50 across Sessions 005–019.** Substantive content contributions (not just presence) are documented per session.

## §4 — Surveying

### §4.1 — Internal precedent: prior decisions adjacent to criterion-4 substance

The methodology has, across 20 sessions, accumulated *operational* understanding of what "substantively different training provenance" means, even though it has not articulated this in spec form:

- **D-021/D-022/D-023/D-024 (Session 004):** established the non-Claude participation mechanism. D-022 codified Claude-Only-Is-Not-Cross-Model. The mechanism designers took "substantively different" to mean "not Claude-family" by default; this is implicit in D-022's enumeration.
- **Session 005 first operational use:** Outsider = OpenAI GPT-5 via `codex exec`. The choice of OpenAI was deliberate: a different organisation, different training corpus, different model architecture (though both transformer-based). No formal criteria applied; the choice was informally justified as "not Anthropic, not Claude-family."
- **Session 011 + Session 017 + Session 020 frame-replacement contributions:** the Outsider's distinctive contributions (structural innovation, layered model, type-drift diagnosis) were qualitatively different from any Claude perspective's. This is *evidence* of training-provenance difference operating in observable ways.
- **Session 012 Outsider's cross-training divergence critique** (in the methodology-naming deliberation): the Outsider explicitly identified internal-vocabulary compound name candidates as an artefact of Claude-family training that the Claude perspectives could not see from inside. This is *self-aware* evidence of training-provenance asymmetry.
- **Session 018 mechanical cross-family gate:** non-deliberative cross-family invocation produced decision-shaping divergence. This expands the operational concept of "non-Claude participation" beyond the deliberation-only frame the v3 spec presumes.

### §4.2 — Precedent: what OTHER methodologies/standards have done

This survey is the orchestrating agent's domain reading and is being surfaced explicitly per OI-015 discipline. Perspectives should treat these as candidate inputs to evaluate, not as established facts.

- **Software diversity in safety-critical systems:** N-version programming requires *independently-developed* implementations (different teams, different languages, different design decisions) to detect common-mode failures. Articulated criteria typically include: different organisational provenance; different toolchain provenance; different specification interpretation. Analogy: a non-Claude model from a different organisation, trained on a different corpus, with different post-training, satisfies more independence criteria than one from the same organisation with shared post-training.
- **Statistical inter-rater reliability:** measures of rater independence (Cohen's kappa, ICC) presume raters have not communicated. Cross-model AI judgment can use the same logic: independence requires no shared training data, no shared optimisation objective.
- **Cross-validation in ML:** fold independence requires that no training data leaks across folds. Analogy: model independence requires no training-data overlap.
- **Diversity in deliberative panels (citizen assemblies, juries):** explicit articulation of dimensions (demographic, experiential, ideological) along which diversity is assessed. Random selection from a stratified sampling frame is the gold standard.

These are surveys, not prescriptions. The methodology may adopt, adapt, or reject any of them.

### §4.3 — Survey of candidate dimensions for "substantively different training provenance"

Possible dimensions along which two models' training provenance might be "substantively different":

1. **Organisational origin** — different developing organisation (Anthropic vs OpenAI vs Google vs Meta vs xAI vs open-source community vs academic lab). Strongest single signal: organisations have distinct mission alignment, RLHF teams, RLHF datasets, safety frameworks, and red-team practices.
2. **Pretraining corpus distinguishability** — whether the pretraining datasets are demonstrably distinct (e.g., one trained on web-crawl + books + code, another trained on a curated subset + proprietary data). In practice, exact corpus comparison is impossible (proprietary), so this dimension is typically *inferred* from public reports + capability profiles + behavioural fingerprints.
3. **Architecture family** — transformer-decoder vs transformer-encoder-decoder vs Mamba/SSM vs other. Most current LLMs are transformer-decoder; this dimension currently has low discriminating power among the strongest models.
4. **Post-training pipeline** — RLHF dataset, reward model, alignment protocol, constitutional AI vs RLAIF vs DPO. This is where many of the visible "personality" differences between models originate.
5. **Independence from operator-mediated selection** — whether the participant was selected through a process that itself reflects the operator's biases (operator's social graph, operator's tool-of-choice) vs through a structured process (random selection from a pool, third-party-curated panel).
6. **Independence from Claude-family lineage** — whether the model has been trained on outputs of Claude (distillation, synthetic data) or vice versa. A "non-Claude" model that distilled from Claude is less independent than one with no Claude exposure.
7. **Operational corroboration** — whether the participant has, in practice, produced contributions that differ from Claude in load-bearing ways (criterion-3-style data). This is *retrospective* evidence of training-provenance difference rather than prospective definition.

These seven dimensions are not mutually exclusive. The articulation may pick a subset, weight them, or define a composite criterion.

### §4.4 — Acceptable participant kinds: candidate enumeration

Possible participant-kind categories that could "count" for OI-004 narrowing/closure:

A. **Non-Anthropic LLM**, accessed through its own provider's endpoint (the dominant pattern across Sessions 005–020).
B. **Non-Anthropic LLM**, accessed through an aggregator API (e.g., OpenRouter) — adds aggregator as a transport intermediary.
C. **Open-source LLM**, locally hosted (e.g., Llama, Mistral, Qwen) — different organisational provenance, sometimes different training-corpus claims, no provider control.
D. **Human reviewer**, recruited from outside the operator's social graph (`participant_selection_method: solicited-externally`).
E. **Human reviewer**, recruited from inside the operator's social graph (`participant_selection_method: solicited-from-graph`) — flagged by current Limitations note as weaker.
F. **Panel of multiple non-Claude participants** (combining A, C, D in the same deliberation) — strongest single configuration.
G. **Mechanical cross-family invocation** outside the perspective-deliberation frame (Session 018 pattern) — not currently theorised by the v3 spec; may need its own category.

The articulation may admit some of these, exclude others, or place conditions on each.

### §4.5 — The recursive question

The OI-004 articulation deliberation is itself a deliberation that must satisfy criterion 4 *if* it is to count toward criterion 4's articulation. This creates a small recursive tension: the deliberation that articulates criterion 4 must itself meet whatever standard it is articulating. The Outsider's participation in this deliberation is one of the criterion-3 data points the articulation will reason about; the Outsider is reasoning about its own qualifying status.

This is an unavoidable property of self-applying methodologies. Perspectives should attend to whether the self-application creates load-bearing risk (e.g., the Outsider proposes a permissive criterion that conveniently includes itself) or whether the self-application is a feature (the deliberation tests whether the proposed criterion holds when applied to the deliberation that proposed it).

## §5 — Candidate articulation drafts

To anchor the deliberation, here are three candidate articulation drafts representing different points on the strict-vs-permissive spectrum. These are illustrative starting points, not adopted. Perspectives may propose own drafts.

### §5.1 — Permissive draft

> "Substantively different training provenance" means: developed by an organisation distinct from Anthropic, with no documented training-data dependency on Claude outputs (no distillation, no synthetic-data sourcing).
>
> Acceptable participant kinds:
> - Non-Anthropic LLM (any provider)
> - Open-source LLM not derived from Claude
> - Human reviewer (any selection method, with selection method recorded)

Closure of OI-004 on this articulation: open-eligible at any point at which existing criteria 1–3 are met with at least one such participant.

### §5.2 — Strict draft

> "Substantively different training provenance" means: developed by an organisation distinct from Anthropic, with publicly documented evidence of distinct pretraining corpus and distinct post-training methodology, AND no documented training-data dependency on Claude outputs.
>
> Acceptable participant kinds for OI-004 narrowing:
> - Non-Anthropic LLM where (i) provider is not a known Anthropic distillation customer, and (ii) at least one publicly documented behavioural distinction from Claude exists.
> - Open-source LLM with public training-data card showing no Claude distillation.
> - Human reviewer selected via `participant_selection_method: solicited-externally` only (selection from operator's social graph excluded).
> - Panel combining ≥2 of the above.

Closure of OI-004 on this articulation: requires a future deliberation explicitly applying the strict criteria to the methodology's accumulated operational record (Sessions 005–020) and finding it satisfied.

### §5.3 — Empirical-corroboration draft

> "Substantively different training provenance" is established by *operational evidence of distinct contribution patterns*, not by upstream definitional criteria. A participant qualifies when the methodology has accumulated at least N criterion-3 data points across ≥M sessions where the participant's contribution is qualitatively distinct from any Claude perspective's contribution (frame-replacement, novel mechanism, contradiction-of-Claude-consensus).
>
> Acceptable participant kinds: any participant for which the operational record substantiates the qualification.

Closure of OI-004 on this articulation: triggered automatically by accumulated record meeting N/M thresholds.

These three drafts span different commitments: permissive (definitional, low-bar), strict (definitional, high-bar), empirical (no-prior-definition, evidence-driven). The articulation may adopt one, blend them, or reject all in favour of a fourth shape.

## §6 — Sequencing observations

- **Session 020 close §Honest notes #4** establishes that frame-replacement is a distinct Outsider contribution kind, with two clear instances (Session 017 H4; Session 020 type-drift). This is direct evidence the deliberation should reason about for the §5.3 empirical-corroboration draft.
- **OI-015 (laundering enforcement gap in domain reading)**: this brief itself surfaces a domain-reading set (§4.2 external-methodology survey, §4.3 dimensional candidates, §4.4 participant-kind enumeration). Per OI-015, perspectives must treat these as candidate inputs to evaluate, not as established facts. The articulation must not silently absorb the brief's framings.
- **OI-007 (scaling open issues format)**: OI-004's record is now ~8KB of session-tally annotations. A criterion-4 articulation that closes OI-004 would convert OI-004 from an active OI to a Resolved entry, slightly easing OI-007 pressure.
- **engine-v1 → engine-v2 question**: a substantive revision to `multi-agent-deliberation.md` triggers an engine-version bump per `engine-manifest.md` §5. The deliberation must address whether criterion-4 articulation is a substantive revision (likely yes, per OI-002 heuristic — adds new normative content). If yes, this is the methodology's first engine-version bump.

## §7 — Design questions

Each perspective should address all eight questions.

**Q1 — Definition surface.** What does "substantively different training provenance" mean? Propose a definition. Be specific: which dimensions from §4.3 (or others you propose) are load-bearing? Are dimensions necessary, sufficient, or weighted? What's the *test* that determines whether two participants have substantively different training provenance?

**Q2 — Enumeration surface.** What are the acceptable participant kinds for OI-004 narrowing/closure? Use §4.4 candidate categories A–G as a starting point but propose your own list with justifications. Which kinds count alone? Which only in combination? Which are excluded entirely and why?

**Q3 — Sufficiency surface.** Even with criterion 4 articulated, is the proposed articulation sufficient to close OI-004? Or does the articulation reveal further conditions the spec should require before closure (e.g., a quorum requirement; a sustained-practice extension; a periodicity check)? If sufficient, justify; if not, name the further conditions.

**Q4 — Testability surface.** What manifest fields, `validate.sh` checks, or schema additions are needed to make the articulated criterion machine-verifiable? Without testability, the articulation is decorative. Propose concrete schema/check changes (or argue why testability is unnecessary or premature).

**Q5 — Self-application surface.** This deliberation includes one Outsider (GPT-5.4 via `codex exec`). Does the Outsider's participation in *this* deliberation satisfy your proposed criterion-4? If yes, does that satisfy you, or is the self-applying convenience a flag? If no, which gap does the Outsider fail on (per your own articulation)?

**Q6 — Closure decision.** Should Session 021 close OI-004? Three sub-options: (a) close on adoption of articulation (treating articulation as the last missing criterion); (b) keep open with named blockers (articulation adopted but named further conditions remain unsatisfied); (c) defer the closure decision to a future session that applies the articulation explicitly. Argue your sub-option.

**Q7 — Engine-version impact.** A substantive revision to `multi-agent-deliberation.md` bumps `engine-v1` → `engine-v2` per `engine-manifest.md` §5. Is this revision substantive, minor, or contestable? If substantive, is the engine-version bump warranted *now* (vs deferring articulation to soft-text within OI-004's record without spec amendment)? Engine-v2 would be the methodology's first engine-version bump; the precedent set matters.

**Q8 — Anti-laundering check.** Apply Session 014 Skeptic's Q7 test to your own proposal: does it widen what counts as pass? Specifically:
  - Does your articulation make it *easier* to claim OI-004 narrowing for a participant that wouldn't actually narrow it (false positive)?
  - Does your articulation make it *harder* to recognise legitimate OI-004 narrowing the methodology is already getting (false negative)?
  - Does your articulation have a route by which the methodology could close OI-004 without genuinely improving the cross-model discipline?

State the falsifier threshold for your position per Session 015/019 Minimalist precedent: *"If I argued [permissive / strict / empirical / defer], the threshold to move me off would be ..."*

## §8 — Role-specific stances

(Each perspective receives only its own §8.X stance in its dispatched brief; the others are visible in this committed audit-anchor file for synthesis-traceability but were not given to any individual perspective.)

### §8.1 — Articulator stance

**Articulator.** You propose an affirmative articulation. Your task is to draft *the actual text* that would be added to `multi-agent-deliberation.md` v3 §Closure Criteria (or to a new §Criterion-4 Articulation subsection) defining "substantively different training provenance" and enumerating acceptable participant kinds. You should pick a definite point on the strict-vs-permissive spectrum (§5.1, §5.2, §5.3, or your own fourth shape) and defend the choice.

You should also propose: whether your articulation is sufficient to close OI-004 (Q3, Q6); what testability hooks (Q4) are needed; engine-version impact (Q7). Your strongest argument is probably that OI-004 has been "Closable pending criterion-4 articulation" for 12 sessions and the methodology's operational record is extensive enough that articulation is overdue. Your weakest argument is probably handling Q5 (self-application): an articulation that includes the deliberation that articulated it can read as self-serving.

You inherit Session 014 Architect "structural innovation" forward in spirit (favour structural changes that change what the methodology can express, not just what it documents).

### §8.2 — Skeptic stance

**Skeptic.** You are adversarial. Your first question is whether this articulation is warranted *now*. Per Session 019 Minimalist defer-revision posture (inherited Session 020 Skeptic) and Session 015/016 single-observation-insufficient discipline, the bar for substantive spec revision is high: name the specific operational evidence that demands articulation now (vs continuing the "Closable pending" status that has held for 12 sessions without observable harm).

Your second question, if articulation proceeds, is to find the accommodation pressure in any proposed articulation. Apply the Session 014 Skeptic Q7 test rigorously: would the proposed articulation make it possible to *close* OI-004 in a future session in a way that does not reflect a genuine narrowing of the cross-model gap? Your strongest argument is probably that an articulated criterion creates a closeable *gate* — and gates that close OIs without commensurate substantive improvement are exactly the laundering pattern OI-015 warns against.

Your third question is closure: even if articulation is adopted, should OI-004 be closed? Argue strongly for "articulate-but-keep-open-with-named-conditions" or "defer-closure-to-a-future-session" if either applies. You inherit Session 013 Skeptic strong-pause posture forward in spirit (when in doubt, pause and require explicit argument for advance).

You are not bound to oppose all articulation — you are bound to maximally adversarial scrutiny. If you find a specific articulation defensible on adversarial scrutiny, you may say so.

### §8.3 — Operationaliser stance

**Operationaliser.** Your concern is testability. An articulated criterion that cannot be machine-verified or systematically auditable is decorative — it has no anti-laundering teeth. Your task is to propose concrete schema additions or `validate.sh` check extensions that would make criterion-4 enforceable.

Specifically: what manifest fields would a participant need to carry such that an automated check could verify "substantively different training provenance"? What's the minimum credible schema? What does `validate.sh` need to parse? Could the existing `training_lineage_overlap_with_claude` field be tightened (e.g., from `independent-claim` to `independent-claim-with-evidence: <evidence-pointer>`)? Could a new check extend Layer 2 to require explicit organisational/architectural/training-corpus fingerprints?

You inherit Session 005/006 Archivist "machine-verifiability is the audit guarantee" forward in spirit (the spec should not require subjective judgement at audit time).

Your strongest argument is probably that articulated-but-unenforceable criteria create a documentation-vs-discipline gap that cannot be detected from outside the workspace. Your weakest argument is probably that *some* criteria (e.g., "qualitatively distinct contribution" per §5.3) are inherently human-judgement-dependent and resist machine verification — you must address whether the methodology should accept this irreducibility or refuse criteria that resist verification.

### §8.4 — Outsider stance

**Outsider.** You are a non-Claude participant (GPT-5.4 via `codex exec`). Your participation is structurally interesting in this deliberation: you are reasoning about the very property (substantively different training provenance) that determines whether your participation counts. Address this self-reflexive surface honestly.

Particular contribution-surface where you may be better positioned than Claude perspectives:

- **Self-assessment.** What aspects of your own training distinguish you from Claude in load-bearing ways? Concrete, not vague. Where you can name specific reasoning patterns or frame-defaults that differ between GPT-5.4 and Claude family, name them.
- **Outside-of-Claude vantage.** Claude perspectives must reason about Claude's training-distribution effects from inside that distribution. You may be better positioned to identify Claude-family blind spots that an articulation should preserve sensitivity to. Conversely: do you think there are GPT-family blind spots that an articulation centred on "non-Claude" misses (i.e., would a GPT-only deliberation also have monoculture risk that a Claude-only deliberation does not see)?
- **External-skeptic test.** Imagine an external skeptic who does not yet trust the methodology. What evidence would convince them that the cross-model participation in Sessions 005–020 actually narrowed the methodology's blind spots vs being a procedural performance? Frame your articulation answer to that skeptic.
- **Frame-challenge authorisation.** Per Session 017 H4 + Session 020 type-drift precedents (your prior frame-replacement contributions), you are explicitly authorised to challenge the *frame* of this deliberation. If criterion-4 articulation is the wrong question, name the right question. If the §5.1/§5.2/§5.3 spectrum misframes the choice, propose a fourth shape. If the deliberation should not produce articulation now, name the alternative (along with what would change your mind).

You are not bound to endorse Articulator, Skeptic, or Operationaliser. A fourth-way is on the table if you propose one with operational warrant.

## §9 — Response format

Produce a Markdown response with sections Q1 through Q8. Use explicit citation format `[01x, Qn]` when referencing your own content and `[brief §X]` when referencing this brief. Include any draft spec text *inline* (not pasted from files) so synthesis can assess text coherence. If your position adopts an articulation, *draft the exact text* you propose for the spec amendment. If your position preserves status-quo (defer articulation), argue *specific falsifiers* that would move you off that position (per Session 015/019 Minimalist precedent).

At the end of your response, add a single section **"Honest-limits"** listing anything you know but did not address, or any reasoning you would need additional evidence to complete. Include the Session 014 Skeptic Q7 anti-laundering check applied to your own proposals (see §7 Q8).

## §10 — Constraint on external imports

Per `PROMPT.md` anti-silent-import rule and OI-015 laundering-gap discipline: if you use an idea from your pretraining (e.g., a training-provenance criterion from a specific AI safety paper, an N-version programming convention, a deliberative-democracy quorum design), surface it explicitly as survey-input — *"From my pretraining, I recall that ..."* — rather than stating it as established fact. The orchestrator will treat surfaced-pretraining claims as candidate evidence to evaluate, not as given facts. Unsourced assertions that could be pretraining-derived weaken your argument.

This constraint binds especially tightly here because criterion-4 articulation is unusually pretraining-rich territory (everyone has read AI-safety/cross-model-deliberation literature in training; everyone has opinions about model independence). The discipline of surfacing-not-importing is the difference between articulation grounded in this methodology's accumulated record vs articulation imported from external consensus the methodology has not adopted.

## §11 — Closure

This brief is committed as the deliberation anchor. Perspective files (`01a-perspective-articulator.md`, `01b-perspective-skeptic.md`, `01c-perspective-operationaliser.md`, `01d-perspective-outsider.md`) will be produced in isolation from each other and committed verbatim. Synthesis (`01-deliberation.md`) will follow. Decisions (`02-decisions.md`) and close (`03-close.md`) will complete Session 021.

No other substantive activity has occurred in Session 021 between the committed assessment (`00-assessment.md`) and this brief.

The four perspectives' independence is preserved by per-perspective dispatch: the shared sections (§1–§7, §9–§11) are byte-identical across all four perspective briefs; only the §8.X stance varies. The committed `01-brief-shared.md` shows all four §8 stances together as the audit anchor; no individual perspective received a brief containing other perspectives' stances.
