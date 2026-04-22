---
session: 021
title: Synthesis — OI-004 Criterion-4 Articulation Deliberation
date: 2026-04-22
status: complete
synthesizer: claude-opus-4-7-orchestrator
synthesizer_kind: claude-orchestrator-not-perspective
participants_family: cross-model
cross_model: true
non_claude_participants: 1
deliberation_anchor_commit: 31951bd
---

# Synthesis — Session 021 OI-004 Criterion-4 Articulation Deliberation

## §1 Position summary

Four perspectives committed verbatim in this directory: Articulator [01a], Skeptic [01b], Operationaliser [01c], Outsider [01d]. Per `multi-agent-deliberation.md` v3 §Synthesis, this synthesis maps positions; the Decide activity (in `02-decisions.md`) operates on this synthesis, not on the raw outputs directly.

**One-sentence position summary per perspective:**

- **Articulator [01a]**: D-Min ∩ O-Corr two-clause hybrid (definitional minimum + operational-corroboration backstop); close OI-004 on adoption with one-time retrospective audit as verification follow-on; engine-v1 → engine-v2 bump warranted now.
- **Skeptic [01b]**: minimal definition (organisational origin + no Claude-distillation, necessary-not-sufficient); enumerate only kinds methodology has operationally exercised (A only; G watchable); articulation NOT sufficient for closure — three additional conditions; engine-v2 for articulation only, closure not in same bump.
- **Operationaliser [01c]**: four-predicate definitional-with-empirical-floor (P1 closed-set provider + P2 claude_output_in_training + P3 closed-set selection method + P4 cumulative operational corroboration via closure-retrospective); broader enumeration with mandatory disclosure annotations; new OI-004 state "Articulated; awaiting closure-retrospective"; engine-v2 includes articulation + schema deltas + new validate.sh checks 16/17/18 + new Tier 2 Q8.
- **Outsider [01d]**: bifurcation of training-provenance (models) vs selection-independence (humans) as criterion-4 frame; for models necessary triplet is organisational origin + no Claude-derived dependency + stable attributable identity at provider/model-family/model-id granularity; broad family-agnostic enumeration; close OI-004 on adoption (refusal to close risks "indefinitely movable finish line").

## §2 Convergences (with citations)

### §2.1 Articulation now is warranted (4-of-4 cross-family)

All four perspectives agree articulation should occur in this session, though on different grounds.

- Articulator [01a, position summary]: "I argue this is sufficient to close OI-004 at Session 021 ... engine-v1 → engine-v2 bump is warranted now and should not be deferred."
- Skeptic [01b, preamble]: "Provisionally yes — but only because the cost of *continued non-articulation* has begun to accumulate (12 sessions of 'Closable pending' ...). My yes is a *housekeeping* yes, not a *driven-by-need* yes."
- Operationaliser [01c, Q6]: "Sub-option (c) preserves the 12-session 'Closable pending' status that is itself a quiet form of laundering — the OI is described as nearly-closed without ever being made adversarially closeable."
- Outsider [01d, Q3]: "Adding another sustainment or quorum bar here would effectively create a hidden criterion 5 after twenty sessions."

### §2.2 engine-v1 → engine-v2 bump warranted for articulation (4-of-4 cross-family)

- Articulator [01a, Q7]: "The revision is substantive. The engine-v1 → engine-v2 bump is warranted now and should not be deferred."
- Skeptic [01b, Q7]: "This revision IS substantive; engine-v1 → engine-v2 bump IS warranted; the precedent set should be that engine-version bumps require both substantive normative change AND deliberation that adopted the change with full per-perspective independence."
- Operationaliser [01c, Q7]: "The Q1 articulation, Q2 enumeration, Q3 closure-procedure, and Q4 schema additions are collectively a **substantive revision** to `multi-agent-deliberation.md` and would bump `engine-v1` → `engine-v2`."
- Outsider [01d, Q7]: "This is a **substantive** revision, and `engine-v2` is warranted if the articulation is written into `multi-agent-deliberation.md`."

### §2.3 Soft-text alternative rejected (4-of-4 cross-family)

All four explicitly reject the alternative of placing the articulation in OI-004's open-issues record without amending `multi-agent-deliberation.md`.

- Articulator [01a, Q7]: "Soft-text in an OI record is not normatively binding on future deliberations or on external workspaces loading engine-vN."
- Skeptic [01b, Q7]: "Soft-text articulation is itself a laundering route: it allows the methodology to claim criterion-4-articulated without subjecting the articulation to engine-version-bump scrutiny."
- Operationaliser [01c, Q7]: "Deferring articulation to 'soft text within OI-004's record without spec amendment' creates exactly the gap the Operationaliser exists to close."
- Outsider [01d, Q7]: "If the articulation lives only in OI-004 commentary, then closure depends on provenance prose rather than engine rule. That is the wrong precedent for an issue this old and this central."

### §2.4 Definition core: organisational origin + no Claude-derived dependency (4-of-4 cross-family)

All four perspectives include both prongs as necessary in their proposed definitions.

- Articulator [01a, Q1 D-Min prongs 1+2]: "Developed by an organisation distinct from Anthropic ... No public documentation that the LLM was trained on Claude outputs."
- Skeptic [01b, Q1 minimal definition]: "(a) Developed by an organisation distinct from Anthropic, AND (b) No documented training-data dependency on Claude outputs."
- Operationaliser [01c, Q1 P1+P2]: "Provider field is a value in a closed set distinct from `anthropic` ... `claude_output_in_training: known-yes | known-no | unknown`."
- Outsider [01d, Q1 model branch prongs 1+2]: "The participant is developed outside the Anthropic / Claude family. The record contains no known Claude-derived training dependency."

### §2.5 Selection independence matters for humans (4-of-4 cross-family, with strength variations)

All four perspectives include selection-method discipline; three (Articulator + Outsider + Operationaliser) treat it as load-bearing for human participants specifically.

- Articulator [01a, Q1 D-Min prong 3]: "Selection method MUST be one of: (a) `solicited-externally` for human participants, (b) `pre-registered` for any kind, or (c) for LLM participants, *any* method. Method (c)'s asymmetry with (a) is deliberate."
- Skeptic [01b, Q1 implicit + Q2 explicit]: refuses to enumerate human kinds the methodology hasn't exercised, but Q4 schema accepts the existing `participant_selection_method` field with no proposal to remove `self` or `solicited-from-graph`.
- Operationaliser [01c, Q1 P3]: "`participant_selection_method` is in a closed set distinct from `self`. ... criterion-4 articulation closes the set against `self` for OI-004-narrowing purposes."
- Outsider [01d, Q1 human branch]: "Necessary: selection independence from the operator; `self` does not count. Strength ranking: `solicited-externally` and `pre-registered` are strong; `solicited-from-graph` is weak."

### §2.6 Excluded categories (4-of-4 cross-family)

All four perspectives exclude (a) Claude-only configurations and (b) the Session 018-pattern mechanical cross-family invocation as a *participant kind* satisfying criterion 4 alone.

- Excluded Claude-only: Articulator [01a, Q2 Excluded]; Skeptic [01b, by minimal-enumeration logic]; Operationaliser [01c, Q2 Excluded — extends to anthropic-other affirmatively]; Outsider [01d, Q2 Excluded].
- Mechanical cross-family invocation NOT alone-qualifying: Articulator [01a, Kind G "supplementary evidence"]; Skeptic [01b, Q2 "single-observation; ... watchable pattern, not yet an enumerated kind"]; Operationaliser [01c, Q4 "first-class recorded category, distinct from deliberation participation"]; Outsider [01d, Q2 "Counts as evidence, not as a separate kind"].

### §2.7 Schema additions warranted (4-of-4 cross-family)

All four propose new manifest fields and validate.sh extensions, varying in scope.

- Articulator [01a, Q4]: 3 new Layer 2 fields + 1 synthesis frontmatter field + 4 new validate.sh checks.
- Skeptic [01b, Q4]: 1 new field (`participant_organisation`) + 1 sub-field (`independence_basis`) + 2 new validate.sh checks. **Refuses** machine-verification of judgement-dependent properties.
- Operationaliser [01c, Q4]: 4 schema additions + 3 new validate.sh checks (16/17/18) + new Tier 2 Q8.
- Outsider [01d, Q4]: 5 new manifest fields + several validate.sh extensions + 1 synthesis frontmatter field.

### §2.8 Self-application risk acknowledged (4-of-4 cross-family)

All four engage Q5 (self-application) honestly. None paper over the recursive structure.

- Articulator [01a, Q5]: "Yes, the Outsider's participation in this deliberation satisfies my proposed criterion-4. This is the most adversarial-defensibility-vulnerable surface of my position, and I take it seriously." Defends via four arguments.
- Skeptic [01b, Q5]: "The Outsider's participation in this deliberation is a LOAD-BEARING RISK, not a feature." Names two specific risks (permissive-articulation; synthesis-bias).
- Operationaliser [01c, Q5]: "I should be honest: the articulation *does* include the participant kind that argued for it. ... Proposing an articulation that includes the participant arguing for it is a soft flag the synthesis should weight."
- Outsider [01d, Q5]: "The self-application convenience is only a flag if the articulation is shaped so narrowly that it effectively means 'GPT counts because GPT is what we already used.' My proposal avoids that. It is family-agnostic."

### §2.9 Operational corroboration acceptance test must remain (4-of-4 cross-family)

Whether placed in definition (Articulator's O-Corr; Operationaliser's P4) or in criterion 3 (Skeptic, Outsider), all four perspectives agree some form of operational evidence is required to convert eligibility into actual narrowing.

## §3 Divergences (with citations)

### §3.1 Closure decision — 2-of-4 cross-family on each side (deepest split)

The split is exactly 2-of-4 on each side, with cross-family balance:

- **Close-now (sub-option a)**: Articulator [01a, Q6] + Outsider [01d, Q6]. Cross-family: 1 Claude + 1 non-Claude.
- **Keep-open with named conditions (sub-option b)**: Skeptic [01b, Q6] + Operationaliser [01c, Q6]. Cross-family: 2 Claude.

**Articulator's argument for close-now** [01a, Q6]: "Keeping OI-004 open with the audit as a named blocker conflates 'verification pending' with 'criterion unmet.' ... adding a sequel-session step is moving the goalposts."

**Outsider's argument for close-now** [01d, Q6]: "If the methodology refuses to close now, criterion-4 risks becoming an indefinitely movable finish line. ... For an external skeptic, the convincing bundle is not the manifest alone. It is: Counterfactual decision evidence; Frame-replacement evidence; Discipline evidence."

**Skeptic's argument for keep-open** [01b, Q6]: "The asymmetry is decisive: (b) preserves correction-paths; (a) closes them. ... Let Session 021 produce the articulation. Let Session 022 (or later) apply the articulation to the record and decide closure."

**Operationaliser's argument for keep-open** [01c, Q6]: "Sub-option (a) would close OI-004 in the same session that articulates the criterion that allows closure. This is the laundering pattern Q8 below names — a closeable gate that the articulation itself opens. The retrospective requirement (Q3) is the structural defence."

This is **2-of-4 cross-family on each side**, not the 3-of-4 cross-family threshold the workspace has typically required for substantive moves (Sessions 011, 014, 017, 019 precedent). The non-Claude vote is on the close-now side; the same-family convergence is on the keep-open side.

### §3.2 Operational corroboration as definition-prong vs criterion-3 acceptance (2-of-4 cross-family on each side)

- **In definition**: Articulator [01a, Q1 O-Corr] + Operationaliser [01c, Q1 P4]. Cross-family: 2 Claude.
- **As criterion 3 acceptance, not definition**: Skeptic [01b, Q1] + Outsider [01d, Q1]. Cross-family: 1 Claude + 1 non-Claude.

Skeptic [01b, Q1]: "These two conditions are *necessary*. They are not, by themselves, *sufficient* — a participant satisfying (a) and (b) is a *candidate* for OI-004 narrowing; whether the participant in fact narrows OI-004 in any given deliberation is determined by criterion-3 evidence (recorded impact), not by criterion-4 alone."

Outsider [01d, Q1]: "Retrospective corroboration, not definition: operational divergence [brief §4.3.7]. That is already what criterion 3 measures."

### §3.3 Enumeration breadth (3-of-4 cross-family for broad; 1-of-4 same-family for strict)

- **Broader enumeration** (admits A, B, C, D, E with conditions, F, G with disclosure): Articulator [01a, Q2] + Operationaliser [01c, Q2] + Outsider [01d, Q2]. Cross-family: 2 Claude + 1 non-Claude.
- **Strict enumeration** (only A; G watchable; B-F not enumerated until operationally exercised): Skeptic [01b, Q2]. 1 Claude.

The 3-of-4 cross-family majority for broader enumeration includes the non-Claude perspective. Skeptic's narrow position has principled basis (operational-record-only discipline; "the methodology does not enumerate participant kinds it has not used") but is a 1-of-4 minority position.

Outsider's distinct contribution to this divergence [01d, Q2]: "I would not let criterion-4 collapse into 'Claude plus GPT is enough forever.'" — explicitly arguing *against* the Skeptic's narrow enumeration on the grounds it would dyad-lock the methodology.

### §3.4 Schema delta scope

Spectrum from minimal to richest:

- **Minimal** (Skeptic [01b, Q4]): tighten existing fields only; refuse machine-verification of judgement-dependent properties.
- **Moderate** (Articulator [01a, Q4]): 3 new fields + 4 new checks.
- **Moderate** (Outsider [01d, Q4]): 5 new fields + several new checks.
- **Richest** (Operationaliser [01c, Q4]): 4 schema additions + 3 new checks + 1 new Tier 2 question.

3-of-4 cross-family converge in the moderate-to-richest range; Skeptic dissents toward minimal.

### §3.5 Frame contributions unique to Outsider (cross-family-distinctive)

The following Outsider contributions have no Claude analogue in the deliberation:

1. **Bifurcation of "training provenance" (models) vs "selection independence" (humans)** as the criterion-4 text-structure [01d, Q1]. None of the three Claude perspectives proposed two-branch text. Articulator handles humans inside the same definitional framework; Operationaliser likewise; Skeptic doesn't enumerate humans.

2. **"Stable attributable identity at provider/model-family/model-id granularity"** as a third necessary prong [01d, Q1]. Operationaliser's P1 closed-set is at provider level only; Articulator's D-Min is at organisation level only.

3. **Behavioural fingerprint self-disclosure** [01d, Q1]: "I more readily reject the offered frame, police type/boundary drift, and convert vague distinctions into operational gates." This is concrete cross-family self-assessment no Claude perspective could produce structurally.

4. **GPT-family blind spots** named [01d, Q2]: "procedural flattening, over-trust in explicit tests and checklists, premature closure once an operational rule exists, treating GPT as the default proxy for all externality." No Claude perspective produced this content. Frame-completion contribution.

5. **"Indefinitely movable finish line"** framing [01d, Q3+Q6] for closure decision. Outsider unique.

These extend the Session 020 close §Honest notes #4 frame-replacement pattern (Session 014 three-cell protocol; Session 017 H4 layered model; Session 020 type-drift diagnosis; Session 021 bifurcation of model-vs-human criterion-4 text-structure). Session 021's Outsider contribution is closer to "frame-completion at the structural level" than full frame-replacement (the brief's question is preserved; only the answer-shape is novel). This is the fourth distinct kind of Outsider contribution recorded across Sessions 005-020 (third-way split-resolution; structural innovation; layered-model frame-replacement; type-drift frame-replacement; structural bifurcation).

## §4 Recommended adoption (R1-R6)

The synthesis recommends the following adoption-set. The Decide activity in `02-decisions.md` will adjudicate whether to adopt R1-R6 as proposed, modify, or reject.

### R1 — Adopt criterion-4 articulation in `multi-agent-deliberation.md` (cross-family 4-of-4)

Add a new subsection `### Criterion-4 Articulation for OI-004` immediately after the four-criterion enumeration in §Closure Criteria. Adopt the **two-branch independence-warrant structure from Outsider [01d, Q1]** as the spec text frame, with the necessary prongs converged on across all four perspectives:

> ### Criterion-4 Articulation for OI-004
>
> Criterion 4 requires an **independence warrant** with two branches: model-provenance independence (for LLM participants) and selection independence (for human participants).
>
> **For model participants**, "substantively different training provenance" is established by ALL of the following:
>
> 1. **Organisational origin distinct from Anthropic.** Recorded as `participant_organisation: <name>` in the Layer 2 manifest; the organisation MUST NOT be Anthropic, MUST NOT be a known Anthropic-derived entity, and MUST be a value in the closed set enumerated by the spec (openai, google, meta, xai, mistral, deepseek, cohere, local, other-named — extensible by named decision).
>
> 2. **No documented Claude-derived training dependency.** No public documentation that the LLM was trained on Claude outputs (distillation, synthetic-data sourcing, or RLAIF using a Claude reward model). Recorded as `claude_output_in_training: known-no | known-yes | unknown` in the Layer 2 manifest. Where `known-yes`, the participant fails this prong. Where `unknown`, the participant is recorded as such; `unknown` is itself signal per the unknown-field rule and surfaces to Tier 2 review.
>
> 3. **Stable attributable identity at provider / model-family / model-id granularity.** Sufficient for audit: a future auditor must be able to identify *which specific model* participated. Recorded across the existing `provider`, `model_family`, `model_id`, `model_version` fields.
>
> **For human participants**, the analogous requirement is **selection independence from the operator**:
>
> 1. `participant_selection_method` MUST NOT be `self`.
> 2. Selection method MUST be one of `solicited-externally`, `pre-registered`, or `solicited-from-graph` (the last conditionally; see §Acceptable Participant Kinds below).
> 3. Selection-method context MUST be recorded in `selection_relationship_to_operator` (free-text or `n/a`).
>
> **Operational corroboration** (criterion 3, the existing acceptance test) is required to convert eligibility-under-this-articulation into actual narrowing. Criterion-4 articulation defines *who can count*; criterion 3 verifies *whether they did*.

**Rationale.** This adopts the 4-of-4 cross-family-convergent core (organisational origin + no Claude-dependency + stable attributable identity for models; selection independence for humans). The bifurcation honours the Outsider's frame-completion contribution. The "operational corroboration is criterion 3, not part of definition" framing follows the 2-of-4 split with cross-family weighting (Skeptic + Outsider), preserving the Articulator's and Operationaliser's "operational corroboration in definition" position as first-class minority. Operational corroboration *itself* is preserved as load-bearing — only its *placement* differs from Articulator/Operationaliser proposal.

### R2 — Adopt acceptable-participant-kinds enumeration with broader-scope (cross-family 3-of-4)

Add a new subsection `### Acceptable Participant Kinds for OI-004` immediately after R1's articulation. Adopt the 3-of-4 cross-family broader enumeration (Articulator + Operationaliser + Outsider; Skeptic dissents). Skeptic's narrow position preserved as first-class minority §5.1.

> ### Acceptable Participant Kinds for OI-004
>
> The following participant categories are **acceptable** when their per-participant manifest satisfies the criterion-4 articulation prongs above.
>
> **Qualifying alone** (count toward OI-004 narrowing without combination):
>
> - Non-Anthropic LLM via own provider's endpoint (`provider` ∈ closed-set; `participant_kind: non-anthropic-model`).
> - Non-Anthropic LLM via aggregator API, with the underlying provider/model/version recorded (`aggregator_intermediary: <name>` field required; `participant_kind: non-anthropic-model`).
> - Locally hosted open-weight model (`provider: local`; `participant_kind: non-anthropic-model`; weights lineage recorded; no known Claude-derived dependency).
> - Human reviewer recruited externally (`participant_kind: human`; `participant_selection_method: solicited-externally`).
> - Human reviewer pre-registered (`participant_kind: human`; `participant_selection_method: pre-registered`).
>
> **Qualifying only in combination** with another qualifying participant:
>
> - Human reviewer from operator's social graph (`participant_kind: human`; `participant_selection_method: solicited-from-graph`; `selection_relationship_to_operator:` annotation required).
>
> **Qualifying shapes**: both `participation_shape: perspective` and `participation_shape: reviewer` qualify if the independence-preserving procedure is documented.
>
> **Recommended for high-stakes deliberations**: panel of multiple non-Claude participants (combining LLM and human-selection independence). Not required for criterion 4; recordable signal for future analysis.
>
> **Excluded**:
>
> - `participant_kind: claude-subagent` (per existing Claude-Only-Is-Not-Cross-Model rule).
> - `participant_kind: anthropic-other` (the affirmative complement to Claude-Only-Is-Not-Cross-Model: intra-Anthropic mixing does not satisfy OI-004 even with model-branding distinctions).
> - Any participant with `training_lineage_overlap_with_claude: known-overlap`.
> - `participant_kind: human` with `participant_selection_method: self`.
>
> **Mechanical cross-family invocation outside the perspective-deliberation frame** (Session 018 pattern) is NOT a participant kind for OI-004 narrowing. It MAY be recorded as corroborating evidence for criterion 3 in the session-level participants index via the `mechanical_cross_family_invocation:` block (schema in R3). Mechanical invocation supplements but does not substitute for participant-perspective contribution.

**Rationale.** Adopts the 3-of-4 cross-family broader enumeration. Outsider's frame-agnosticism argument [01d, Q2] is decisive against Skeptic's narrow operational-record-only discipline: criterion 4 must not collapse into "Claude+GPT-dyad-as-final-state." Operationaliser's mandatory-disclosure-for-weakened-cases honours both the broader admission and the testability discipline. Skeptic's strict-enumeration position preserved as §5.1 first-class minority with operational warrant.

### R3 — Adopt schema deltas (cross-family 4-of-4 on additions; range adopted at moderate-richer)

Adopt the following schema additions to `multi-agent-deliberation.md` v3 §Heterogeneous-Participant Recording Schema. Position is closer to Operationaliser's [01c, Q4] richest-coherent-set with a few Outsider additions, blunted by Skeptic's machine-verification-irreducibility caveats.

**Layer 2 manifest additions**:

```yaml
participant_organisation: <organisation-name from closed set>  # required when participant_kind: non-anthropic-model
claude_output_in_training: known-yes | known-no | unknown | n/a  # required when participant_kind ∈ {non-anthropic-model, human}; n/a for human; out-of-scope for {claude-subagent, anthropic-other}
training_lineage_evidence_pointer: <provenance-relative path | URL | "unknown-but-asserted">  # required when training_lineage_overlap_with_claude: independent-claim
aggregator_intermediary: <string or "n/a">  # required when access via aggregator
selection_relationship_to_operator: <free-text or "n/a">  # required when participant_kind: human
independence_basis: organization-distinct | local-open-weights | human-selection-distinct | mixed-panel | unknown  # required for participants claimed for OI-004 narrowing (Outsider [01d, Q4])
```

**Synthesis frontmatter additions**:

```yaml
oi004_qualifying_participants: [<list-of-perspective-names>]  # the participants whose manifests satisfy criterion-4 articulation; explicit claim for audit
```

**Session-level `participants.yaml` extension** (per Operationaliser [01c, Q4 Schema-addition-4]):

```yaml
mechanical_cross_family_invocation:
  - purpose: <free text, e.g. "C3 5-gram overlap test", "L1 contamination canary">
    invoked_model: <model id>
    provider: <provider id>
    invocation_method: <cli-wrapper | api | other>
    decision_shaped: <D-NNN id or "none">
    evidence_pointer: <provenance-relative path>
```

**`tools/validate.sh` additions** (substantive validator changes; included in the engine-v2 bump):

- **Check 16** (per Operationaliser [01c, Q4]): independent-claim has training_lineage_evidence_pointer.
- **Check 17** (per Operationaliser [01c, Q4]): claude_output_in_training disclosure presence.
- **Check 18** (per Operationaliser [01c, Q4]): closure-retrospective well-formedness when present.
- **Check 19** (Articulator+Operationaliser convergence): non-anthropic-model participants have non-empty participant_organisation in the closed set.

**Validation-approach.md addition** (Tier 2 Q8 per Operationaliser [01c, Q4]):

> **Q8. OI-004 closure-retrospective substantive adequacy** (paired with check 18). If this session contains an `oi-004-retrospective.md`, read its Qualifying Deliberations Table and P4 Assertion. For each row marked frame-replacement-or-novel-mechanism, verify the cited synthesis section actually contains a non-Claude-originated reframing. For the P4 assertion, verify the cited divergence shows the synthesis adopted a position that contradicts (or substantively augments) the Claude consensus, not merely supplemented it. Flag rows where the substantive claim is weaker than the structural claim suggests.

**Rationale.** Adopts the cross-family-convergent additions (4-of-4 on at least some additions) at moderate-rich scope. Operationaliser's Tier 2 Q8 pairing addresses the human-judgement-irreducibility honestly per Skeptic's discipline. Skeptic's "minimal-additions only" position preserved as §5.4 first-class minority.

### R4 — Adopt new OI-004 state "Articulated; awaiting closure-retrospective" — DEFER closure decision (cross-family balanced)

The closure decision is the deepest split: 2-of-4 cross-family on each side, with the non-Claude vote on close-now and same-family Claude convergence on keep-open.

**Adopt sub-option (b) keep-open with named conditions** per Skeptic [01b, Q6] + Operationaliser [01c, Q6]. Specifically, transition OI-004 from "Closable pending criterion-4 articulation" to a new state **"Articulated; awaiting closure-retrospective"** per Operationaliser's four-state lifecycle [01c, Q6 spec text]:

> ### Closure Criteria for OI-004 (revised)
>
> OI-004 has four ordered states:
>
> 1. **Open.** Default until criteria 1–3 are satisfied.
> 2. **Closable pending criterion-4 articulation.** Criteria 1–3 satisfied; criterion 4 not yet articulated. (Sessions 009–020 held this state.)
> 3. **Articulated; awaiting closure-retrospective.** All four criteria articulated as auditable predicates. Closure requires a one-time `oi-004-retrospective.md` artefact applying the criteria to the cumulative record. (Sessions 021+ hold this state.)
> 4. **Closed.** The retrospective artefact is committed, check 18 passes, Tier 2 Q8 has been answered substantively, and a successor session has decided on OI-004 closure with explicit citation to the retrospective.

**Named conditions for advancing from state 3 to state 4** (combining Skeptic's three additional conditions [01b, Q3] with Operationaliser's retrospective-artefact requirement [01c, Q3]):

> Closure of OI-004 (advancing state 3 → state 4) requires ALL of:
>
> (i) **Closure-retrospective artefact** committed at `provenance/<NNN-closure-session>/oi-004-retrospective.md` containing:
>    - Qualifying-deliberations table (one row per Sessions 005–onwards qualifying deliberation; columns per Operationaliser [01c, Q3]).
>    - Summary tally (totals).
>    - P4 assertion: at least one cross-lineage divergence-from-Claude-consensus cited with provenance pointer.
>    - `validate.sh` check 18 PASS.
>    - Tier 2 Q8 substantively answered.
>
> (ii) **Successor-session adjudication.** The closure decision must be made by a session distinct from Session 021 (the articulating session). The successor session must be a multi-agent deliberation with non-Claude participation per `multi-agent-deliberation.md` §When Non-Claude Participation Is Required clause 4 (asserts a change in OI-004 state). The successor session's Outsider should not be the same instance as Session 021's Outsider where feasible.
>
> (iii) **Cross-model contradiction-prevailing data point** identified in the retrospective. Per Skeptic [01b, Q3 condition (i)]: at least one documented case where the non-Claude participant's position contradicted Claude-perspective consensus AND the synthesis adopted the non-Claude position. This may be present in the existing 50 criterion-3 data points; the retrospective must identify it explicitly. (If absent, OI-004 remains in state 3 until such a case occurs.)
>
> (iv) **Sustained-practice forward commitment**: voluntary:required ratio remains ≥1.0 (currently 7:6) at successor-session adjudication time. Drift below would be evidence the discipline weakened post-articulation.

**Rationale.** This is the synthesis's most difficult adjudication. Both close-now and keep-open positions have substantive cross-perspective warrant. The synthesis adopts keep-open on three grounds:

(1) **Cross-family threshold**: 2-of-4 cross-family does not meet the 3-of-4 cross-family majority threshold the workspace has typically required for substantive moves. Sessions 011, 014, 017, 019 all required 3-of-4 cross-family for substantive adoption. Both options are at 2-of-4; neither satisfies the threshold. In ambiguous cases, the workspace's discipline favors the more reversible option. Keep-open is reversible (a successor session can close); close-now is not.

(2) **Convergence-by-mechanism**: Skeptic and Operationaliser independently arrived at the structural defence of successor-verification (Skeptic via condition iii; Operationaliser via the four-state lifecycle and check 18 + Tier 2 Q8). This is convergence-by-mechanism even if both perspectives are Claude — the same structural insight arrived via different reasoning routes (Skeptic via adversarial-defence-of-spec-discipline; Operationaliser via testability-of-closure-claim).

(3) **The asymmetry argument is decisive** (Skeptic [01b, Q6]): "(b) preserves correction-paths; (a) closes them." If keep-open turns out to be over-cautious, OI-004 closes in Session 022 or 023 with little harm. If close-now turns out to be premature, OI-004 cannot easily be re-opened against the closeable-gate-already-flipped record.

**Articulator's [01a, Q6] and Outsider's [01d, Q6] close-now positions are preserved as first-class minorities** (§5.2 and §5.3 below) with operational activation warrants. The Outsider's "indefinitely movable finish line" warrant is the strongest single argument for close-now and is recorded in §5.3 as the primary trigger for revisiting R4.

### R5 — Adopt engine-v1 → engine-v2 bump (cross-family 4-of-4)

Update `engine-manifest.md` §2 (current version) and §7 (history):

- §2 declares `engine-v2` as current.
- §7 adds an engine-v2 history entry naming the Session 021 D-082 (or equivalent decision number) as the bump driver. Names the spec changes: `multi-agent-deliberation.md` v3 → v4 (substantive: criterion-4 articulation + acceptable-participant-kinds enumeration + schema additions); `tools/validate.sh` substantive update (new checks 16, 17, 18, 19); `validation-approach.md` v3 → v4 (substantive: new Tier 2 Q8).

**Per-spec version handling**:
- `multi-agent-deliberation.md` v3 → v4 (substantive per OI-002 heuristic): new normative content, new required fields, new closure procedure. v3 preserved as `multi-agent-deliberation-v3.md`; v4 takes canonical filename.
- `validation-approach.md` v3 → v4 (substantive per OI-002 heuristic): new Tier 2 question. v3 preserved as `validation-approach-v3.md`; v4 takes canonical filename.
- `tools/validate.sh` updated in place (no version-suffix preservation per OI-002 minor-vs-substantive heuristic — but the substantive validator changes are part of engine-v2 bump per `engine-manifest.md` §5).

**Rationale.** 4-of-4 cross-family agreement on engine-v2 bump for the articulation. The synthesis explicitly limits the bump scope to the articulation + schema + Tier 2 Q8 (the R4 closure decision is procedurally separate and does NOT itself require a further engine bump — the four-state lifecycle text is part of multi-agent-deliberation.md v4, but advancing OI-004 from state 3 to state 4 in a future session is an OI-record update, not a spec revision). This honours Skeptic's [01b, Q7] precedent-setting argument: engine-bumps require substantive normative change adopted with multi-perspective independence; the same precedent argues *against* bundling closure into the same bump.

### R6 — OI housekeeping

**OI-004 status update** (in `open-issues.md`):
- Status changes from "Closable pending criterion-4 articulation" to "Articulated; awaiting closure-retrospective."
- Per-OI annotation extended with Session 021 record:
  - Criterion-4 articulation adopted per D-082 R1.
  - Acceptable participant kinds enumerated per D-082 R2.
  - Schema deltas adopted per D-082 R3 + validate.sh checks 16-19.
  - New OI-004 state "Articulated; awaiting closure-retrospective" per D-082 R4.
  - Engine-v2 declared per D-082 R5.
  - Closure conditions named: closure-retrospective + successor-session adjudication + cross-model contradiction-prevailing data point + sustained-practice ≥1.0 voluntary:required ratio.
- Tally: criterion-2 advances from 6-of-3 to 7-of-3 (Session 021 is the seventh required-trigger deliberation with non-Claude participation: D-082 modifies multi-agent-deliberation.md — d023_2 fires; D-082 asserts OI-004 state change — d023_4 fires). Voluntary:required rebalances from 7:6 to 7:7.
- Criterion-3 cumulative data points: 50 (Sessions 005-019) + 5 from Session 021 (Outsider's bifurcation; stable-identity prong; behavioural fingerprint; GPT-family blind spots; "indefinitely movable finish line" framing) = **55**.

**OI-002 ninth data point**: `multi-agent-deliberation.md` v3 → v4 is **substantive** (new normative content: criterion-4 articulation, acceptable-participant-kinds enumeration, schema additions, four-state OI-004 lifecycle). Heuristic continues to hold stable.

**OI-007 count**: unchanged at 12 active OIs (no OI opened or resolved this session — OI-004 transitions states but remains open).

**No OI closed this session.** OI-004 closure is explicitly deferred per R4.

## §5 Preserved first-class minorities

Per Session 015/019/020 precedent, preserved minorities have explicit operational activation triggers, not vague "future deliberation may revisit" language.

### §5.1 — Skeptic strict-enumeration minority

**Position** [01b, Q2]: "The methodology does not enumerate participant kinds it has not used. ... If we obviously want to allow them, run a deliberation with one and then enumerate."

**Operational warrant**: this minority is the preferred revision direction for §Acceptable Participant Kinds if any of the following observable conditions occurs:

(i) A future session enumerates a participant kind into the spec but the kind is never operationally exercised within 5 subsequent sessions, AND
(ii) The unexercised enumeration is then cited as basis for OI-004 narrowing or any related claim (i.e., the methodology claims credit for cross-model discipline based on unexercised categories).

OR:

(iii) An external workspace loading engine-v2 attempts to use a kind in §Acceptable Participant Kinds that turns out to be operationally non-functional (e.g., aggregator B in a region without aggregator availability), and the spec's enumeration misled the external workspace.

If either (i)+(ii) or (iii) occurs, R2's broader enumeration is candidate for narrowing back toward Skeptic's exercised-only position.

### §5.2 — Articulator close-on-adoption minority

**Position** [01a, Q6]: "Close on adoption of the articulation. Not (b) keep-open-with-named-blockers, not (c) defer-to-future-session. ... Keeping OI-004 open with the audit as a named blocker conflates 'verification pending' with 'criterion unmet.'"

**Operational warrant**: this minority is the preferred revision direction for R4 (close OI-004 immediately rather than via state-3 → state-4 transition) if any of the following observable conditions occurs:

(i) The closure-retrospective in a future session passes check 18 AND substantively passes Tier 2 Q8 with citation evidence the orchestrator and at least one non-Claude perspective agree is genuine. At that moment, the keep-open-with-conditions framing has incurred its full cost (one extra deferral session) without producing distinct value the close-on-adoption framing would not have produced. Articulator's position is vindicated retrospectively.

OR:

(ii) Three sessions pass without any session attempting the closure-retrospective; OI-004 remains in state 3 indefinitely. This activates the Outsider's "indefinitely movable finish line" risk (§5.3) and converts to Articulator's "procedural avoidance" diagnosis. R4's keep-open is then vindicated as Skeptic's worry materialised; rollback to close-now is candidate.

### §5.3 — Outsider close-now-with-bifurcation minority

**Position** [01d, Q3+Q6]: "I would treat the articulation above as sufficient to close OI-004 now ... Adding another sustainment or quorum bar here would effectively create a hidden criterion 5 after twenty sessions ... If the methodology refuses to close now, criterion-4 risks becoming an indefinitely movable finish line."

**Operational warrant**: this minority is the preferred response if any of the following observable conditions occurs:

(i) **Indefinitely-movable-finish-line activation**: three or more successor sessions pass without OI-004 advancing from state 3 to state 4, AND no operationally-named blocker is preventing the advance. At three sessions, the keep-open framing is itself the indefinitely-movable-finish-line the Outsider warned against; close-on-adoption (this minority) becomes the preferred revision direction.

OR:

(ii) **Hidden-criterion-5 emergence**: the closure-retrospective is attempted, passes check 18 + Tier 2 Q8, AND a successor session adds a new closure condition not present in R4's named-conditions list (effectively creating a fifth criterion). The Outsider's "hidden criterion 5" warning is then materialised; rollback to close-on-adoption + revisit R4's named-conditions for laundering risk.

OR:

(iii) **External-skeptic-test passage**: a future external review of the workspace finds the cumulative Sessions 005–021 record clearly meets "the convincing bundle" Outsider [01d, Q6] names (counterfactual decision evidence + frame-replacement evidence + discipline evidence) AND criticises OI-004 for being open in state 3. External pressure justifies advancing closure.

### §5.4 — Skeptic minimal-schema minority

**Position** [01b, Q4]: "Schema additions in the engine-definition spec set are themselves OI-015-style laundering surfaces — they create the *appearance* of audit discipline without changing the substantive judgement load. ... The discipline is in the human/synthesis judgement, not in the schema field that records it."

**Operational warrant**: this minority is the preferred revision direction for R3 (revert toward minimal-schema-additions) if any of the following observable conditions occurs:

(i) **`unknown`-as-default drift**: across 5 successor sessions using engine-v2, the new fields `claude_output_in_training` and `independence_basis` are populated with `unknown` in ≥80% of qualifying participant manifests. This indicates the new fields are not actually surfacing operator-knowledge; they are creating mechanical compliance theatre.

OR:

(ii) **Schema-is-not-discipline failure**: a closure-retrospective passes check 18 + check 19 mechanically but a Tier 2 Q8 review (or external review) finds the cited evidence is weak. The schema additions added compliance-cost without preventing weak-citation closure. R3's testability adoption is reverted toward minimal.

### §5.5 — Articulator + Operationaliser O-Corr-in-definition minority (joint)

**Position** [01a, Q1 D-Min ∩ O-Corr]; [01c, Q1 P4]: operational corroboration should be part of criterion-4 definition, not deferred to criterion-3 acceptance.

**Operational warrant**: this joint minority is the preferred revision direction if:

(i) **Criterion-3 enforcement gap**: a future session-23+ deliberation finds that criterion 3 is not consistently applied to OI-004-narrowing claims (i.e., the workspace cites criterion-3 as the acceptance test but doesn't actually verify it for each claim). At that point, embedding O-Corr/P4 in criterion-4 definition itself becomes the preferred enforcement structure.

OR:

(ii) **Closure-retrospective produces ambiguous P4 verification**: the future closure-retrospective per R4 finds that some Sessions 005-020 narrowing claims are clearly operationally corroborated and others are ambiguous. The ambiguity is itself evidence that operational-corroboration-as-criterion-3-only is too easy to claim without verification; embedding O-Corr in criterion-4 definition (per Articulator's D-Min ∩ O-Corr or Operationaliser's P4) raises the per-deliberation bar.

## §6 Anti-laundering check applied to this synthesis

Per Session 014 Skeptic Q7 test applied to the synthesis (R1-R6 aggregate):

**Does this synthesis make it easier to claim OI-004 narrowing for participants that wouldn't actually narrow it (false positive)?**

R1 narrows the per-participant test by adding "stable attributable identity" and "no Claude-derived dependency" as necessary prongs. R2 enumerates kinds the methodology hasn't operationally exercised (Skeptic's concern). R3 schema additions create new compliance surfaces but the `unknown` value remains visible (Skeptic's residual risk). Net: the threshold is **raised** at the per-participant level (more required fields, more explicit independence basis); the gate-pass is **broader** at the enumeration level (more kinds admitted). The two move in opposite directions; net is approximately neutral with explicit visibility increases.

Mitigation: the broader enumeration is paired with mandatory disclosure annotations (R2 "with mandatory disclosure annotation" categories) so weakened kinds are visible in audit. Skeptic's narrow position preserved as §5.1 with operational triggers.

**Does this synthesis make it harder to recognise legitimate OI-004 narrowing the methodology is already getting (false negative)?**

R4 defers closure to a successor session — adding one mandatory deferral. This is a procedural cost. Articulator and Outsider argue this cost is unwarranted (their close-now positions). The synthesis weighs this against the structural defence value of successor-verification.

R3's mechanical-cross-family-invocation block recognises Session 018 evidence that v3 schema currently underspecifies — this is a structural recognition of legitimate narrowing the methodology was already getting but couldn't formally record. Net: synthesis slightly improves recognition of mechanical-gate evidence; slightly delays recognition of cumulative deliberation-perspective evidence.

**Does this synthesis have a route by which the methodology could close OI-004 without genuinely improving the cross-model discipline?**

The R4 closure-conditions chain (retrospective + successor + contradiction-prevailing + sustained-practice) is designed to prevent this. The residual risks per perspective:

- Operationaliser [01c, Q8 residual]: "A future session whose orchestrator wants to close OI-004 has every procedural opportunity to do so with my proposal. The procedural defences ... require operator integrity at exactly the same surface as check 13's honest limit."
- Skeptic [01b, Q8 residual]: "The successor audit itself could be conducted without rigour, finding the criterion satisfied because the orchestrating agent wants OI-004 closed. ... a stopping point but it is a stopping point."

The synthesis acknowledges these residual risks without claiming to eliminate them. They are in the operator-integrity floor that no methodology spec can fully defend against. Mitigation: transparency (§5 minorities preserved with activation triggers; closure-retrospective deliberated and Tier-2-reviewed; voluntary:required ratio remains observable).

**Three candidate laundering patterns specifically tested and blocked:**

1. **"Articulate-and-close-in-same-session" laundering** (the deepest risk — articulation that mechanically opens its own gate). **Blocked by R4's deferral to successor session and four-state lifecycle.**

2. **"Soft-text articulation in OI-record without spec amendment" laundering** (hides the substantive change from external-application visibility). **Blocked by 4-of-4 rejection; R5 makes engine-v2 official.**

3. **"Broad enumeration becomes silent permission" laundering** (enumerated-but-unexercised kinds become precedent without operational test). **Blocked at the enumeration level by R2's mandatory-disclosure-for-weakened-cases; preserved as §5.1 minority with operational rollback triggers.**

**One weakest-bonded mitigation surface**: R4's condition (iii) cross-model contradiction-prevailing data point requires the closure-retrospective to identify ≥1 such case in the existing record. **The synthesis has not verified this case exists.** Skeptic [01b, honest-limits 1] explicitly acknowledges this: "I have asserted that none of the 50 criterion-3 data points have been characterised at this strength. I have not read the per-session breakdowns to verify this." The synthesis inherits this uncertainty — the closure-retrospective in a future session may find no contradiction-prevailing case in the cumulative record, blocking closure indefinitely. This is **WX-21-2** (recorded in Decisions §03-close as monitoring): if the closure-retrospective fails to identify a contradiction-prevailing case, R4 condition (iii) is the binding constraint and the methodology must either (a) wait for one to occur, or (b) revise condition (iii) downward. (b) would itself be a substantive revision triggering re-deliberation.

## §7 Honest notes from synthesis

**Brief-priming-absence assessment.** Inspection of all four perspective files shows perspectives used their own vocabulary for framing. Articulator used "D-Min ∩ O-Corr", "definitional minimum", "introductory window", "three-deliberation onboarding"; Skeptic used "necessary not sufficient", "operational-record-only discipline", "successor-session audit", "convergence-by-mechanism"; Operationaliser used "four-predicate definitional-with-empirical-floor", "P1/P2/P3/P4", "closure-retrospective", "well-formedness check"; Outsider used "independence warrant", "two branches", "stable attributable identity", "behavioural fingerprint", "indefinitely movable finish line". Brief's vocabulary ("strict draft", "permissive draft", "empirical-corroboration draft" per §5) was cited not echoed; perspectives produced independent framings. Brief-priming-absent for eleventh consecutive session.

**Outsider's pre-response workspace exploration** is a novel pattern for Session 021. The Outsider invoked four `exec` tool calls (sed/ls on specifications/engine-manifest.md, multi-agent-deliberation.md, open-issues.md, provenance/017/, provenance/020/) before producing its response body. This grounded the Outsider's response in the actual spec text rather than the brief's quoted excerpts. Per the Outsider's own honest-limits acknowledgement, this did not violate §10 anti-import (workspace read is not pretraining import). The pattern is recorded in the Outsider's manifest `transport_notes` and is potentially relevant to future OI-015 deliberations on the boundary between "brief content" and "workspace context" for Outsider perspectives.

**Cross-family closure split is the deepest ratification challenge.** Both R4-keep-open (adopted) and the close-now alternative (preserved as §5.2 + §5.3) have substantive cross-perspective warrant. The synthesis's adoption of keep-open is on three grounds (cross-family threshold, convergence-by-mechanism, asymmetry argument). A future audit of Session 021's synthesis fidelity may legitimately ask whether the cross-family-threshold reasoning is defensible (2-of-4 cross-family for close-now does include the non-Claude vote, which is qualitatively distinct from 2-of-4 same-family). The convergence-by-mechanism argument is the strongest defence of keep-open against this audit pressure: Skeptic and Operationaliser arrived at successor-verification via distinct reasoning routes, which is structural support beyond mere headcount. **WX-21-3** (recorded in close): Session 022 audit should specifically test whether the "convergence-by-mechanism" reasoning holds up on re-inspection, or whether the synthesis privileged Claude-Claude convergence over cross-family vote unduly.

**Outsider's frame-completion contribution is weaker than Session 020's frame-replacement** but stronger than Sessions 005-013's third-way split-resolutions. Session 021's Outsider bifurcation of model-vs-human criterion-4 text is structural innovation at the spec-text level (frame-completion). The 5 cross-family contributions enumerated in §3.5 are concrete and material, but none is a frame-replacement on the order of Session 017 H4 or Session 020 type-drift. The criterion-3 cumulative count advances by 5 (50 → 55).

**This synthesis is single-synthesizer** (Claude Opus 4.7, the orchestrator). The synthesis step is the pattern's highest-risk single-agent re-entry point per `multi-agent-deliberation.md` v3 §Limitations. Mitigations applied: explicit citations to perspective files for all attributed positions; quote-over-paraphrase for load-bearing claims; majority/minority structure reported explicitly with cross-family weighting; convergence vs coverage distinguished. The synthesis adopts R4 (keep-open) on 3 stated grounds, all of which can be challenged on Session 022's audit of synthesis fidelity. The synthesizer is Claude (orchestrator); the reasoning that adopted keep-open over close-now privileges a Claude-Claude convergence that the non-Claude perspective explicitly opposed. This is the most synthesis-risky surface of the deliberation. WX-21-3 is the operational test for whether the synthesis discipline held.

**Anti-import discipline applied to synthesis**: the synthesis has not introduced concepts not present in the perspective files. The "convergence-by-mechanism" framing in §4 R4 rationale is a synthesizer-original framing label `[synth]` for what Skeptic and Operationaliser independently reasoned. The "asymmetry argument" framing is a `[synth]` label for Skeptic's [01b, Q6] explicit reasoning. The "indefinitely-movable-finish-line" framing in §5.3 is a direct quote from Outsider [01d, Q6]. Other section-labels (R1-R6 numbering; convergence-then-divergence-then-recommendation structure) are organisational, not novel content.
