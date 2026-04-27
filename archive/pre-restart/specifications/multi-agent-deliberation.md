---
title: Multi-Agent Deliberation
version: 4
status: active
created: 2026-04-17
last-updated: 2026-04-22
updated-by-session: 021
supersedes: multi-agent-deliberation-v3.md
---

# Multi-Agent Deliberation

## Purpose

This specification defines how the methodology instantiates genuine multi-perspective deliberation. It describes when multi-agent deliberation is required, how perspectives are convened, how stance briefs are structured, how their outputs are synthesized, how the whole process is recorded, and what limitations remain. It serves the methodology's explicit injunction against single-perspective substantive work, and partially addresses Open Issue OI-004 (genuinely independent perspectives).

This specification applies equally to the self-development application and to external-problem applications of the Selvedge engine. Triggers, shapes, schemas, and conventions defined here are engine-level and do not vary by application kind (per D-074, Session 017).

The term "multi-agent deliberation" describes a property, not a mechanism: that the perspectives reasoning about a question arrive at their positions without seeing each other's positions. The current implementations realise this property via parallel context-isolated subagents of the Claude model family, optionally augmented by non-Claude participants (human reviewers or non-Anthropic models) following the Non-Claude Participation mechanism below. Future implementations may extend this further via different-model agents accessed through their own endpoints, persistent personas, or asynchronous cross-session deliberation; the specification is written so those extensions are changes of mechanism, not of pattern.

Version 4 adds the OI-004 criterion-4 articulation (`### Criterion-4 Articulation for OI-004`), the acceptable-participant-kinds enumeration (`### Acceptable Participant Kinds for OI-004`), six new Layer 2 manifest fields (`participant_organisation`, `claude_output_in_training`, `training_lineage_evidence_pointer`, `aggregator_intermediary`, `selection_relationship_to_operator`, `independence_basis`), one new synthesis frontmatter field (`oi004_qualifying_participants`), one new session-level participants.yaml block (`mechanical_cross_family_invocation:`), the four-state OI-004 lifecycle, and the closure procedure (operationalised by `validate.sh` checks 16-19 and `validation-approach.md` v4 Tier 2 Q8). It supersedes v3 (`multi-agent-deliberation-v3.md`). Adopted Session 021 per D-082; engine-v1 → engine-v2 bump declared in `engine-manifest.md` §2 + §7.

Version 3 added the Trigger-Coverage Annotation Schema (`triggers_met:` + `triggers_rationale:` per-decision) and the associated session-number gating rule, operationalising v2 Validation items 1 and 2 as `validate.sh` checks 14 and 15. It superseded v2 (`multi-agent-deliberation-v2.md`).

Version 2 added the Non-Claude Participation mechanism, the three-layer heterogeneous-participant recording schema, and associated trigger rules. It superseded v1 (`multi-agent-deliberation-v1.md`).

## Specification

### When Multi-Agent Deliberation Is Required

A session must convene a multi-agent deliberation for any decision where at least one of the following is true:

1. The decision modifies `methodology-kernel.md`.
2. The decision creates or substantively revises any specification in `specifications/`.
3. The question is one on which reasonable practitioners could genuinely disagree — operationalised as: the session author can name at least two plausible positions before the deliberation begins.
4. The session author has marked the decision load-bearing for any other reason and records why.

For any decision that meets at least one of these triggers but is made by a single agent anyway, the decision record must state this explicitly, naming the reason (e.g., "Single-perspective; non-load-bearing: minor correction per D-014 precedent"). Unstated single-perspective decisions on triggered questions are a specification violation.

Decisions that meet none of the triggers — typos, reordering, routine execution of already-decided plans — may be made by a single agent without annotation.

### When Non-Claude Participation Is Required

Distinct from the requirement to convene multi-agent deliberation at all, this specification governs when at least one participant must come from outside the Claude model family (human reviewer, non-Anthropic model, or both).

Non-Claude participation is **required** for any deliberation whose decision falls in one of the following categories:

1. Modifies `methodology-kernel.md`.
2. Creates or substantively revises `multi-agent-deliberation.md`.
3. Creates or substantively revises `validation-approach.md` in ways that touch semantic (Tier 2) validation.
4. Asserts a change in the state of OI-004.

Non-Claude participation is **recommended** for other decisions that meet the multi-agent triggers above.

Non-Claude participation is **optional** for all other decisions.

**Opt-out.** A session may make a required-trigger decision without a non-Claude participant, but must record in the decision:

- `non_claude_participation: skipped`
- A reason. Acceptable reasons: "no non-Claude participant available within session timebox"; "mechanism designer exempt" (the first-use bootstrap exemption, see below); "subject matter does not plausibly expose Claude-family blind spots" (must be argued in the decision record, not asserted).
- `retry_in_session: NNN` — the session number where the missing non-Claude participation will be added.

Unstated skips on required-trigger decisions are a specification violation.

**Bootstrap exemption (one-time).** Session 004, which established these rules, was exempt because the rules did not exist when it began. Future sessions revising this mechanism do not share the exemption.

### Trigger-Coverage Annotation Schema

Added in v3 (Session 006) to make trigger coverage machine-verifiable by `tools/validate.sh` checks 14 and 15. The schema is prospective-only from Session 006; pre-adoption decisions (D-001 through D-036) are out-of-scope.

**Field: `triggers_met:`.** A flat list of trigger identifiers that the decision meets.

- Identifier format: lowercase-underscore, `d016_N` or `d023_N` where `N` is the clause number within the current D-016 or D-023 ruleset.
- Current allowed values (as of v3): `d016_1`, `d016_2`, `d016_3`, `d016_4`, `d023_1`, `d023_2`, `d023_3`, `d023_4`.
- Empty-state token: `triggers_met: [none]`. YAML-standard `triggers_met: []` is explicitly **not** valid — `[none]` is required as a positive author assertion. The convention is chosen to make it harder to silence the field accidentally.
- Absence semantics: in a post-adoption session (≥006), absence of `triggers_met:` is a validation failure. In a pre-adoption session (<006), absence is expected and out-of-scope for checks 14 and 15.

**Field: `triggers_rationale:`.** A required prose sibling providing a one-to-two-sentence explanation of why each listed trigger applies (or why none apply for `[none]`).

- Purpose: adversarial visibility. A decades-later reviewer can audit whether the `triggers_met:` list aligns with the decision's content.
- The checks do not parse `triggers_rationale:`; it is archival and adversarial content, not structural.
- It is nevertheless a required field — a decision record with `triggers_met:` but no `triggers_rationale:` is malformed.

**Placement.** Per-decision inline, directly under the decision's `## D-NNN:` heading, using the bolded-key format that matches existing decision-record idiom:

```markdown
## D-NNN: [Title]

**Triggers met:** [d016_2, d016_3]

**Triggers rationale:** One-to-two-sentence explanation of why each listed trigger applies.

**Decision:** ...
```

The validator parses `**Triggers met:**` lines with a line-anchored regex; the bracketed list is extracted with a simple sed/awk expression. Multi-document YAML is not used.

**Future rule additions.** The identifier namespace is append-only. A new D-NNN that introduces a trigger reserves fresh identifiers (e.g., `d040_1`). Existing records are not rewritten — their `triggers_met:` stays accurate as of their authoring. The validator's recognized-identifier set must be updated in the same session that introduces new identifiers.

**Retroactivity.** No backfill of D-001 through D-036. The immutability rule (D-017; workspace-structure §provenance) is honored. `tools/validate.sh` gates checks 14 and 15 on session number ≥6 via an explicit `TRIGGERS_MET_ADOPTION_SESSION=6` constant (see `validation-approach.md` v3 Gating Conventions). If a future session needs historical trigger classification, that is a distinct session's job producing a new artefact (e.g., `reclassification.md`) that references pre-adoption decisions without editing them.

**Complementary annotations.** Two additional decision-level annotations support the rules:

- `**Single-agent reason:**` — a bolded-key line on any decision that declares a `d016_*` trigger but was made single-agent anyway. Required for check 14 to pass in that case.
- `**Non-Claude participation:**` — a bolded-key line on any decision that declares a `d023_*` trigger but was made without non-Claude participation. Must include a `reason:` sub-field and a `retry_in_session:` sub-field. Required for check 15 to pass in that case.

Both annotations are prose-plus-structured-fields; see `validation-approach.md` v3 for parse details.

### Perspectives

- **Number.** Default three. Up to five when the problem spans clearly different concern-domains. More than five requires a written justification recorded at convening time.
- **Selection.** Perspectives are chosen for expected disagreement on *this* problem. There is no permanent roster. Reaffirms D-005.
- **Adversarial requirement.** At least one perspective must be adversarial — its job is to challenge the emerging consensus and argue against the proposal. Reaffirms the methodology-kernel rule.
- **Naming.** Each perspective has a short name (e.g., "The Pragmatist," "The Archivist") used consistently throughout briefs, raw outputs, synthesis, and decision records.

### Stance Briefs

Each perspective receives a stance brief before the independent phase begins. Every brief in a single deliberation has the same structure, in this order:

1. **Methodology context** — shared, byte-identical across all briefs in the deliberation. A concise description of what the methodology is and its current state.
2. **Problem statement** — shared, byte-identical. What question the deliberation is answering.
3. **Design questions** — shared, byte-identical. The specific questions each perspective is asked to address.
4. **Role-specific stance** — the only section that varies between briefs. Second person, imperative, naming the specific concerns the perspective holds. Target length 150–300 words.
5. **Response format** — shared. What structure the response should take, length target, constraints on output.
6. **Constraint on external imports** — shared. A reminder to reason primarily from the brief and to flag pretrained ideas as external inputs rather than committing them directly (per the PROMPT.md rule).

Diffing two briefs from the same deliberation should reveal only the role-specific stance. This makes deliberations reproducible.

**Workspace context per perspective.** Minimal and identical. Perspectives reason from the brief; they do not read workspace files or use other tools during the independent phase. This keeps the deliberation reproducible and prevents spurious disagreement from divergent reading. A future version may specify differentiated context per perspective (see Open Extensions below); until then, uniform minimal context is the rule.

**Brief immutability.** Briefs are committed to the workspace (or otherwise preserved) before any perspective is launched. Briefs are not edited during the deliberation. The commit hash or equivalent timestamp at brief-finalisation is the deliberation's anchor.

### Non-Claude Participation Mechanism

A non-Claude participant joins a multi-agent deliberation in one of two shapes:

**Shape A — Participant as perspective.** The non-Claude participant is treated as a perspective indistinguishable in role from the Claude perspectives:

1. A brief is written following the Stance Briefs section above and committed before the participant sees it.
2. The brief is delivered to the participant by whatever channel is available: for a human, a text editor; for a non-Anthropic model, a web UI paste or a CLI invocation from the workspace.
3. The returned response is committed **verbatim** as a raw-output file at the session's provenance root (flat layout) or under `deliberations/<decision-id>/responses/` (subdirectory layout) with the same naming convention as Claude raw outputs.
4. If the participant cannot respond synchronously, the session writes `provenance/NNN/STATUS.md` naming the awaited participant and **halts**. Synthesis does not proceed until the awaited response is committed.

**Shape B — Participant as reviewer.** The non-Claude participant is a named auditor at synthesis-time:

1. Claude raw outputs are committed as normal.
2. Before the synthesizer runs, a named human reviewer (not the session operator) reads the raw outputs and writes `provenance/NNN/human-review.md` containing: the review's frontmatter (identity, relationship-to-operator, time-spent), a prose record of what was flagged, and the explicit field `reviewer_changed_synthesis: true | false`.
3. The synthesizer reads `human-review.md` as an input alongside the raw perspective outputs.
4. A reviewer is not a deliberator: they see the Claude outputs in raw form and their job is to flag what a Claude-only synthesis would likely miss.

Shapes A and B may be used separately or in combination in the same deliberation, provided the manifest declares each participant's shape.

**Transport guarantee.** The workspace guarantees the **record** (committed brief, verbatim response, attributable participant), not the **generation** (which depends on channels the workspace cannot automate). Convener fidelity to verbatim reproduction is a required property; attempts to automate faithfulness are a future direction, not a day-one requirement.

### Heterogeneous-Participant Recording Schema

Heterogeneous-participant deliberations record identity across three layers.

**Layer 1 — Raw-output file frontmatter (minimal).** Required fields: `session`, `title`, `date`, `status`, `perspective`, `committed_at`. The response body is the payload; no identity, version, or transport fields appear here.

**Layer 2 — Per-participant manifest.** One YAML file per participant at `provenance/NNN/manifests/<perspective>.manifest.yaml`. Required fields:

```yaml
perspective: <role name>
participant_kind: claude-subagent | anthropic-other | non-anthropic-model | human | unknown
participant_identity: <free text, canonicalized>
model_family: <string or "unknown">
model_id: <string or "n/a" for human or "unknown">
model_version: <string or "unknown">
provider: <anthropic | openai | google | local | human | unknown>
endpoint: <string or "web-ui" | "in-person" | "unknown">
invocation_method: <agent-tool | cli-wrapper | copy-paste | written-by-hand | unknown>
sampling:
  temperature: <value or "unknown">
  top_p: <value or "unknown">
  max_tokens: <value or "unknown">
training_lineage_overlap_with_claude: known-overlap | unknown | independent-claim
participant_selected_by: <operator identity>
participant_selection_method: self | solicited-from-graph | solicited-externally | pre-registered
identity_known: true | false | partial
context_source: <path to brief, or "verbal" for humans>
delivered_at: <ISO-8601 or "unknown">
received_at: <ISO-8601 or "unknown">
raw_response_file: <path>
transport_notes: <free text>
output_edited_after_submission: true | false
participation_shape: perspective | reviewer
```

**Layer 2 fields added in v4 (D-082, Session 021)** — for OI-004 criterion-4 enforcement; see §Criterion-4 Articulation for OI-004 below for normative use:

```yaml
participant_organisation: <organisation-name from closed set>  # required when participant_kind: non-anthropic-model. Closed set enumerated in tools/validate.sh PARTICIPANT_ORGANISATION_CLOSED_SET; extensible by named decision per validation-approach.md v4 §Closed-set extension discipline. Operationalised by check 19.
claude_output_in_training: known-yes | known-no | unknown | n/a  # required when participant_kind in {non-anthropic-model, human}; n/a permitted for human. Out-of-scope for {claude-subagent, anthropic-other}. Operationalised by check 17. The `unknown` value is signal per the Unknown-field rule and surfaces to Tier 2 Q8 review.
training_lineage_evidence_pointer: <provenance-relative path | URL | "unknown-but-asserted">  # required when training_lineage_overlap_with_claude: independent-claim. Operationalised by check 16. The pointer must resolve to: a model card or training-data card published by the provider (URL); a provider-public statement on Claude-distillation policy (URL); a workspace-internal note explaining what evidence the operator inspected (provenance-relative path); or the literal string "unknown-but-asserted" with mandatory transport_notes explanation.
aggregator_intermediary: <string or "n/a">  # required when access via aggregator (e.g., OpenRouter); names the aggregator. "n/a" for direct provider access.
selection_relationship_to_operator: <free-text or "n/a">  # required when participant_kind: human. Records relationship-to-operator and selection method context per the OI-004 criterion-4 articulation human-branch requirement.
independence_basis: organization-distinct | local-open-weights | human-selection-distinct | mixed-panel | unknown  # required for participants claimed for OI-004 narrowing. Records the basis on which the participant claims criterion-4 eligibility.
```

The v4 fields are required from session 021 onward for participants claimed for OI-004 narrowing; pre-adoption sessions (001-020) are out-of-scope per the immutability rule (D-017) and per the session-number gating in `validation-approach.md` v4.

**Layer 3 — Session-level index.** `provenance/NNN/participants.yaml` (preferred) or `provenance/NNN/participants.md` listing each participant and their manifest path.

**Composition fields (synthesis frontmatter).** The synthesis file's frontmatter records:

```yaml
participants_family: claude-only | mixed-anthropic | cross-model
cross_model: true | false
non_claude_participants: <integer>
oi004_qualifying_participants: [<list-of-perspective-names>]  # added v4: explicit declaration of which perspectives' manifests satisfy criterion-4 articulation; empty list permitted for sessions making no OI-004-narrowing claim
```

**Session-level participants index extension (added v4, D-082, Session 021).** When mechanical cross-family invocation occurs outside the perspective-deliberation frame (e.g., the Session 018 contamination-canary pattern), it is recorded as a separate top-level block in `provenance/NNN/participants.yaml`:

```yaml
mechanical_cross_family_invocation:
  - purpose: <free text, e.g. "C3 5-gram overlap test", "L1 contamination canary">
    invoked_model: <model id>
    provider: <provider id>
    invocation_method: <cli-wrapper | api | other>
    decision_shaped: <D-NNN id or "none">
    evidence_pointer: <provenance-relative path>
```

This block records mechanical cross-family invocation as corroborating evidence for criterion 3 of OI-004 (recorded impact on outcomes); it is **not** a participant kind for criterion 4 (per §Acceptable Participant Kinds for OI-004 below). The block is optional; absence is permitted (most sessions will not record mechanical invocation).

`participants_family: mixed-anthropic` is the value for intra-Claude-family size-mixing (Opus + Sonnet + Haiku, any combination) — this **is not** cross-model participation (see the Claude-Only-Is-Not-Cross-Model rule below). `cross_model: true` requires at least one participant with `training_lineage_overlap_with_claude` other than `known-overlap`.

**Unknown-field rule.** Unknown values are recorded as the literal string `unknown`. Empty strings are forbidden. Missing required fields are a schema violation. `identity_known: partial` requires a `transport_notes` entry explaining what is and is not recorded. The literal `unknown` is signal — it says "this session could not determine the value" and is itself auditable.

**Claude-Only-Is-Not-Cross-Model.** A deliberation whose participants are all members of the Claude model family (any mix of Opus, Sonnet, Haiku; any sizes; any post-training runs) does not constitute cross-model participation for OI-004 purposes. The manifest must record `participants_family: claude-only` (or `mixed-anthropic` for explicit size-mixing) and `cross_model: false`. Intra-family size-mixing may be recorded for separate reasons (see OI-011) but contributes nothing to OI-004.

### Mechanism

The required property is **independence-preservation during the independent phase**: no perspective's output can influence another perspective's reasoning while each is forming its position.

The Claude-subagent implementation realises this via parallel subagents launched through Claude Code's Agent tool, each in an isolated context. Non-Claude participation realises it through the brief-drop pattern and halt-before-synthesis described above — the non-Claude participant reasons from the committed brief without access to Claude perspectives' outputs during the independent phase.

The specification does not mandate any single mechanism. Alternative realisations that preserve the required property — different-model agents accessed via their own endpoints, persistent human reviewers briefed separately, asynchronous cross-session deliberations with explicit quarantine — are consistent with this specification.

### Synthesis

After all perspectives (Claude and non-Claude) have returned their raw outputs, a synthesis step produces a single deliberation record.

- **Synthesizer identity.** The synthesizer must not have been one of the deliberation's perspectives. The synthesizer's identity (agent/model/date) is recorded in the synthesis file's frontmatter.
- **Reviewer input.** If the deliberation includes a reviewer-shape non-Claude participant, the synthesizer reads `human-review.md` alongside the raw perspective outputs.
- **Citation requirement.** Claims attributing a position to a perspective must cite the source file and section/question: `[source-file, Q#]` or `[source-file, section]`.
- **Synthesizer-original claims.** Claims not directly sourced from any raw perspective are marked `[synth]`. This lets future readers compute the ratio of sourced to synthesised content and judge faithfulness.
- **Quote over paraphrase for load-bearing claims.** Where a perspective's argument turns on specific language, the synthesis quotes that language rather than paraphrasing.
- **Preserve dissent.** Disagreements are listed as disagreements. A minority position with a strong argument is preserved as-is, not diluted. Majority/minority structure is reported explicitly.
- **Convergence vs coverage.** The synthesis distinguishes *convergence* (all perspectives independently reached a similar conclusion) from *coverage* (only one perspective raised a point; others were silent). These are different epistemic states.
- **Synthesis order anchoring.** Perspectives are presented to the synthesis step in alphabetical order by role name, or in a fixed order documented in the synthesis file, to reduce ordering-induced synthesizer bias.

Synthesis maps; it does not decide. The Decide activity operates on the synthesis, not on raw outputs directly.

### Provenance Layout

Tiered by the number of deliberations in a session.

**Single-deliberation sessions** use flat numbered files at the session's provenance root, consistent with Sessions 001, 002, 003, and 004:

```
provenance/<NNN-title>/
  00-assessment.md
  01-brief-shared.md            # optional: shared brief preserved for auditability
  01a-perspective-<role>.md
  01b-perspective-<role>.md
  ...
  01-deliberation.md            # synthesis
  manifests/
    <role>.manifest.yaml        # one per participant
  participants.yaml             # session-level index
  human-review.md               # if a reviewer-shape participant was included
  STATUS.md                     # if the session halted awaiting a non-Claude response
  02-decisions.md
  03-close.md
```

When all briefs in the deliberation share byte-identical non-role sections (the default), briefs need not be preserved as separate files — each raw-output file already contains the role-specific stance, and the shared sections are derivable from any brief. If briefs in a deliberation depart from this shape (e.g., differentiated context), the briefs must be preserved as separate files named `01*-brief-<role>.md`.

**Multi-deliberation sessions** use a subdirectory layout:

```
provenance/<NNN-title>/
  00-assessment.md
  deliberations/
    <decision-id>/
      briefs/
        00-shared-context.md
        01-<role>.md
      responses/
        01-<role>.md
        ...
      manifests/
        <role>.manifest.yaml
      participants.yaml
      human-review.md             # if a reviewer-shape participant was included
      synthesis.md
      manifest.json               # session-level metadata (model IDs, timestamps, commit)
  02-decisions.md
  03-close.md
```

`manifest.json` records deliberation-level metadata (commit hash at convening time, deliberation decision-id, start/end timestamps). Per-participant detail lives in the `manifests/` directory.

### Graceful Degradation

- **Minimum viable quorum.** If a perspective fails to return an output (error, refusal, malformed response), the deliberation may proceed with the remaining perspectives provided at least three returned valid outputs. The failure is recorded in the synthesis file's frontmatter or in `manifest.json`.
- **Stance refusal.** A perspective that refuses the assigned stance, or that substantively disagrees with the brief itself, has its refusal preserved as provenance. Refusal is signal, not an error to coerce around.
- **Fewer than three valid outputs.** The deliberation must be re-run or the question reformulated. A synthesis over one or two perspectives is not a multi-agent deliberation.
- **Non-Claude participant non-response.** Per the halt-before-synthesis rule, synthesis does not proceed when a Shape-A non-Claude participant has not responded. Timeout policy (whether a session may eventually proceed after N days with a recorded opt-out) is not mandated by v2; the halt is in place until the awaited response is committed or the session formally records opt-out.

### Limitations

These statements are required content for every multi-agent deliberation's synthesis or decision record that relies on a Claude-only mechanism:

- **All Claude-subagent perspectives share a model family.** The parallel-subagent implementation uses instances of the same Claude model family. Shared training produces shared blind spots: the same cultural priors, argumentative reflexes, refusal patterns, and aesthetic preferences.
- **Intra-Claude-family size-mixing is not cross-model participation.** Mixing Opus, Sonnet, and Haiku does not narrow OI-004; it may surface capability-band differences but does not introduce independent training lineages. See OI-011 for separate tracking of intra-family mixing.
- **Parallel isolation prevents conversational anchoring, not training-distribution anchoring.** Four instances of the same model, given briefs written in a shared vocabulary, will correlate in ways that look like agreement but are actually shared priors. Consensus across subagents is weak evidence, not strong.
- **Brief-writing has no adversary.** The convening agent's framing choices propagate into all perspectives identically. Adding multi-agent to brief-writing creates infinite regress; the methodology does not pretend otherwise.
- **The synthesis step is the pattern's highest-risk single-agent re-entry point.** Synthesis conventions (citation, dissent-preservation, `[synth]` marker, quote-over-paraphrase) reduce but do not eliminate this risk.
- **Non-Claude participation depends on convener fidelity.** The transport guarantee is over the record, not the generation. The convener must commit the participant's response verbatim; there is no automated verification of faithfulness at v2. See Open Extensions below for future enforcement directions.
- **A single non-Claude participant narrows OI-004 less than its presence suggests.** One human reviewer selected from the operator's social graph shares correlated priors with the operator; one non-Anthropic model accessed once may not reveal training differences that emerge only over many interactions. Closure of OI-004 requires sustained practice (see the Closure section).

The specification's tone on limitations is deliberately uncompromising. Softening the language in future revisions is not a minor correction.

### Closure Criteria for OI-004

OI-004 may be considered for closure when all of the following hold:

1. **Participant independence.** At least one participant in qualifying deliberations has `training_lineage_overlap_with_claude: independent-claim` (non-Anthropic model) or `participant_kind: human` with a `participant_selection_method` other than `self`.
2. **Sustained practice.** Non-Claude participation has occurred in at least three required-trigger deliberations across different sessions, recorded correctly per the schema above.
3. **Recorded impact.** The synthesis or decision records show that non-Claude input shaped at least one outcome — the cross-lineage-influence ratio (see Open Extensions) is non-zero.
4. **Articulation.** A successor decision defines what "substantively different training provenance" means and enumerates acceptable participant kinds. Articulated Session 021 per D-082; see §Criterion-4 Articulation for OI-004 below.

OI-004 is not automatically closed on meeting these criteria; a future session must deliberate and decide. "Closable" and "closed" are distinct states. The OI now has a four-state lifecycle (added v4); see §Closure Procedure for OI-004 below. **OI-004 reached state 4 (Closed) at Session 041 per D-125** via the closure procedure below; see `open-issues/resolved/OI-004.md` for the closure record and `provenance/041-session-assessment/oi-004-retrospective.md` for the closure-retrospective artefact. Forward semantics of `d023_4` + clause 4 in the closed state are specified at the end of §Closure Procedure for OI-004 below.

### Criterion-4 Articulation for OI-004

(Added v4 per D-082, Session 021.)

Criterion 4 requires an **independence warrant** with two branches: model-provenance independence (for LLM participants) and selection independence (for human participants). The two-branch structure follows the Outsider's frame-completion contribution at Session 021 [01d, Q1] — "training provenance" is the right question for model participants but the wrong question for humans, where selection-process independence is the load-bearing dimension.

**For model participants**, "substantively different training provenance" is established by ALL of the following:

1. **Organisational origin distinct from Anthropic.** Recorded as `participant_organisation: <name>` in the Layer 2 manifest; the organisation MUST NOT be Anthropic, MUST NOT be a known Anthropic-derived entity, and MUST be a value in the closed set enumerated in `tools/validate.sh` PARTICIPANT_ORGANISATION_CLOSED_SET (initial set: openai, google, meta, xai, mistral, deepseek, cohere, local, other-named; extensible by named decision per `validation-approach.md` v4 §Closed-set extension discipline).

2. **No documented Claude-derived training dependency.** No public documentation that the LLM was trained on Claude outputs (distillation, synthetic-data sourcing, or RLAIF using a Claude reward model). Recorded as `claude_output_in_training: known-no | known-yes | unknown` in the Layer 2 manifest. Where `known-yes`, the participant fails this prong. Where `unknown`, the participant is recorded as such; `unknown` is itself signal per the unknown-field rule and surfaces to Tier 2 Q8 review (see `validation-approach.md` v4).

3. **Stable attributable identity at provider / model-family / model-id granularity.** Sufficient for audit: a future auditor must be able to identify *which specific model* participated. Recorded across the existing `provider`, `model_family`, `model_id`, `model_version` fields. A participant lacking any of these is `unknown` at that level and fails this prong.

**For human participants**, the analogous requirement is **selection independence from the operator**:

1. `participant_selection_method` MUST NOT be `self`.
2. Selection method MUST be one of `solicited-externally`, `pre-registered`, or `solicited-from-graph` (the last conditionally; see §Acceptable Participant Kinds for OI-004 below).
3. Selection-method context MUST be recorded in `selection_relationship_to_operator` (free-text or `n/a`).

**Operational corroboration** (criterion 3, the existing acceptance test) is required to convert eligibility-under-this-articulation into actual narrowing. Criterion-4 articulation defines *who can count*; criterion 3 verifies *whether they did*. This bifurcation follows the 2-of-4 cross-family Session 021 split with cross-family weighting (Skeptic + Outsider) on placing operational corroboration in criterion 3 rather than in criterion-4 definition. The Articulator's [01a, Q1] D-Min ∩ O-Corr position and the Operationaliser's [01c, Q1] P4 position (operational corroboration as definitional prong) are preserved as joint first-class minority §5.5 in `provenance/021-oi004-criterion4-articulation/01-deliberation.md` with operational activation triggers.

**Audit-time test.** For any deliberation `S` claiming OI-004-narrowing participation by `P`:

1. Verify `P`'s manifest declares the v4 fields `participant_organisation` (if `non-anthropic-model`), `claude_output_in_training`, `training_lineage_evidence_pointer` (if `independent-claim`), `selection_relationship_to_operator` (if `human`), and `independence_basis`. Missing fields are validation failures (checks 16, 17, 19).
2. Verify the model-branch or human-branch prongs above hold per declared values. If any prong fails, the criterion-4-narrowing claim for `P` is rejected.
3. Verify criterion-3 evidence (recorded impact) for `P` exists in the deliberation's synthesis or decision record. If absent, the participant is eligible-on-trust for an introductory window of three required-trigger deliberations; thereafter, criterion-3 evidence is required.

### Acceptable Participant Kinds for OI-004

(Added v4 per D-082, Session 021.)

The following participant categories are **acceptable** when their per-participant manifest satisfies the criterion-4 articulation prongs above.

**Qualifying alone** (count toward OI-004 narrowing without combination):

- **Non-Anthropic LLM via own provider's endpoint.** `participant_kind: non-anthropic-model`; `provider` in closed set; `aggregator_intermediary: n/a`. Examples: GPT-family via `codex exec`; Gemini via Google API; Llama via Meta endpoint.
- **Non-Anthropic LLM via aggregator API.** Same as above but with the underlying provider/model/version recorded; `aggregator_intermediary: <name>` field required and non-empty. Operator MUST disclose if the aggregator is known to apply system-prompt modifications that could mask training-provenance signal.
- **Locally hosted open-weight model.** `participant_kind: non-anthropic-model`; `provider: local`; weights lineage recorded in `transport_notes`; `claude_output_in_training: known-no` (open-weight models with public training-data cards typically support this) or `unknown` with explicit acknowledgement.
- **Human reviewer recruited externally.** `participant_kind: human`; `participant_selection_method: solicited-externally`. Recruitment channel MUST be recorded in `selection_relationship_to_operator`; compensation, if any, MUST be disclosed in `transport_notes`.
- **Human reviewer pre-registered.** `participant_kind: human`; `participant_selection_method: pre-registered`. Pre-registration date and basis MUST be recorded.

**Qualifying only in combination** with another qualifying participant:

- **Human reviewer from operator's social graph.** `participant_kind: human`; `participant_selection_method: solicited-from-graph`; `selection_relationship_to_operator:` annotation required and substantive. Per the existing Limitations note, this category alone does not substantiate cross-provenance independence; combination with at least one Qualifying-Alone participant is required.

**Qualifying shapes**: both `participation_shape: perspective` and `participation_shape: reviewer` qualify if the independence-preserving procedure is documented per the existing Non-Claude Participation Mechanism section.

**Recommended for high-stakes deliberations** (D-023-triggering; engine-version bumps; OI closures): panel of multiple non-Claude participants. Not required for criterion 4; recorded as a synthesis-frontmatter signal for future analyses.

**Excluded**:

- `participant_kind: claude-subagent` (per existing Claude-Only-Is-Not-Cross-Model rule).
- `participant_kind: anthropic-other` — the affirmative complement to Claude-Only-Is-Not-Cross-Model: intra-Anthropic mixing does not satisfy OI-004 even with model-branding distinctions. (Per Operationaliser [01c, Q2] and Outsider [01d, Q2] convergence.)
- `participant_kind: unknown`.
- Any participant with `training_lineage_overlap_with_claude: known-overlap`.
- `participant_kind: human` with `participant_selection_method: self`.

**Mechanical cross-family invocation outside the perspective-deliberation frame** (the Session 018 pattern) is **NOT** a participant kind for OI-004 narrowing. It MAY be recorded as corroborating evidence for criterion 3 in the session-level participants index via the `mechanical_cross_family_invocation:` block (schema above). Mechanical invocation supplements but does not substitute for participant-perspective contribution. (4-of-4 cross-family convergence at Session 021.)

The Skeptic's [01b, Q2] strict-enumeration position — enumerate only kinds the methodology has operationally exercised — is preserved as first-class minority §5.1 in `provenance/021-oi004-criterion4-articulation/01-deliberation.md` with operational activation triggers including unexercised-enumeration-cited-as-narrowing-basis.

### Closure Procedure for OI-004

(Added v4 per D-082, Session 021.)

OI-004 has four ordered states:

1. **Open.** Default until criteria 1–3 are satisfied.
2. **Closable pending criterion-4 articulation.** Criteria 1–3 satisfied; criterion 4 not yet articulated. (Sessions 009–020 held this state.)
3. **Articulated; awaiting closure-retrospective.** All four criteria articulated as auditable predicates per §Criterion-4 Articulation above. Closure requires a one-time `oi-004-retrospective.md` artefact applying the criteria to the cumulative record. (Sessions 021+ hold this state.)
4. **Closed.** The retrospective artefact is committed, `validate.sh` check 18 passes for the artefact, Tier 2 Q8 has been answered substantively, and a successor session has decided on OI-004 closure with explicit citation to the retrospective.

States are advanced by named decisions, not asserted by prose annotation. A state advance from Articulated (state 3) to Closed (state 4) requires ALL of the following:

(i) **Closure-retrospective artefact** committed at `provenance/<NNN-closure-session>/oi-004-retrospective.md` containing the three required sections (`## Qualifying Deliberations Table`, `## Summary Tally`, `## P4 Assertion`) per check 18; plus `validate.sh` check 18 PASS; plus Tier 2 Q8 substantively answered.

The retrospective's Qualifying Deliberations Table contains one row per Sessions-005-onwards qualifying deliberation with columns: session number; decision id(s); participant kinds; per-prong satisfaction (boolean per row) of criterion-4 articulation prongs; criterion-3 data points contributed; frame-replacement-or-novel-mechanism flag (boolean).

The Summary Tally totals: total qualifying deliberations; total non-Claude participants; total criterion-3 data points; total frame-replacement-or-novel-mechanism instances.

The P4 Assertion explicitly cites at least one cross-lineage divergence-from-Claude-consensus with `[provenance/<NNN>/<file>, §X]` citation. (Per Skeptic [01b, Q3] condition (i): a documented case where the non-Claude participant's position contradicted Claude-perspective consensus AND the synthesis adopted the non-Claude position.)

(ii) **Successor-session adjudication.** The closure decision must be made by a session distinct from the session that articulated criterion 4 (Session 021 for the initial articulation). The successor session must be a multi-agent deliberation with non-Claude participation per §When Non-Claude Participation Is Required clause 4 (asserts a change in OI-004 state). The successor session's Outsider should not be the same instance as the articulating session's Outsider where feasible.

(iii) **Cross-model contradiction-prevailing data point** identified in the retrospective per the P4 Assertion above. If absent in the existing record, OI-004 remains in state 3 until such a case occurs in a future deliberation.

(iv) **Sustained-practice forward commitment**: voluntary:required ratio (counted across non-Claude participation history) remains ≥1.0 at successor-session adjudication time. Drift below would be evidence the discipline weakened post-articulation.

The Articulator's [01a, Q6] and Outsider's [01d, Q6] sub-option-(a) "close-on-articulation" positions are preserved as first-class minorities §5.2 and §5.3 in `provenance/021-oi004-criterion4-articulation/01-deliberation.md` with operational activation triggers including the Outsider's "indefinitely movable finish line" warrant. **Both §5.2 and §5.3 were discharged at Session 041 closure (D-125): §5.3 strongly vindicated; §5.2 partially vindicated.** See `open-issues/resolved/OI-004.md` Session 041 closure entry for disposition detail. **Session 041 closure preserved §5.6 (Skeptic + Outsider GPT-family-concentration joint minority)** as the new live minority with reopen warrants (i) external-review-cites-narrow-record and (ii) six-session-window-without-non-GPT-non-Claude-participation; see `provenance/041-session-assessment/01-deliberation.md §5.6` for detail.

**Forward semantics of `d023_4` and `§When Non-Claude Participation Is Required` clause 4 after state 4 (Closed).** Per Session 041 D-125/D-126 and 4-of-4 cross-family convergence on the substantive reading (synthesis §2.6 + §3.4):

- `d023_4` ("Asserts a change in the state of OI-004") in closed-state fires only on proposed state-changes to OI-004 — reopen, revise articulation, weaken or strengthen closure conditions. It does not fire on ongoing workspace monitoring, cross-model participation records, or tally observations after closure.
- `§When Non-Claude Participation Is Required` clause 4 continues to apply in its narrowed closed-state form: non-Claude participation remains required for future attempts to reopen or materially revise the OI-004 settlement.
- The criterion-4 articulation, acceptable-participant-kinds enumeration, and manifest schema additions remain active specification for all deliberations — not only for OI-004 tally advancement.
- The §Limitations note remains load-bearing; specifically the clauses about shared Claude training distribution and single-non-Claude-participant narrowing.

### Interaction with Existing Decisions

- **D-005** (perspectives are work-specific, not fixed) — reaffirmed.
- **D-009** (acknowledgment of simulated disagreement) — remains in force. Its scope now includes the Claude-monoculture limitation of the Claude-subagent mechanism, not only the original same-context simulation case, and it extends further to the trust-boundary limitation of human-mediated non-Claude participation transport.
- **D-014** (minor-correction heuristic) — reaffirmed.
- **D-016** (multi-agent triggers) — reaffirmed; this specification's "When Non-Claude Participation Is Required" extends, rather than replaces, D-016's triggers.
- **D-020** (treatment of v1 kernel pointer as minor) — reaffirmed.
- **D-022** (Claude-only is not cross-model) — integrated as the Claude-Only-Is-Not-Cross-Model rule above; v4 extends this to anthropic-other per §Acceptable Participant Kinds for OI-004.
- **D-025** (this session does not narrow OI-004 operationally) — the specification records OI-004 as state 3 ("Articulated; awaiting closure-retrospective") per v4 four-state lifecycle.
- **D-082** (Session 021 — OI-004 criterion-4 articulation; engine-v1 → engine-v2 bump) — adopts the criterion-4 articulation, acceptable-participant-kinds enumeration, schema additions, and four-state lifecycle in v4.

### Open Extensions

These directions are noted as candidates for future revisions, not mandated. Each entry records its **activation precondition**: the concrete event or schema change that would make the extension worth revisiting (per D-035, Session 005; the pattern is "keep rule-history inside the artifact that enforces the rule" per the Archivist's Session 005 Q6 proposal).

- **Differentiated context per perspective** (from Session 003's Futurist position) — each perspective receives only the workspace context its stance requires, declared by the brief. *Activation precondition: a session surfaces evidence that shared-brief uniform context distorted outputs (e.g., a brief-priming failure beyond the level observed in Session 004's "training-distribution theatre" phrase).*
- **Cross-lineage-influence ratio** (from Session 004's Skeptic) — a measured ratio, across a rolling window of deliberations, of decisions where a non-Claude participant's position differed from the synthesized Claude consensus and the synthesis adopted the non-Claude position. Suggested floor: above 10% over a ten-deliberation window for non-Claude participation to be considered genuinely impactful. Not mandated; candidate for a validation-tool enhancement. *Activation precondition: OI-004 approaches closure (closure criterion 3 explicitly requires this metric or equivalent evidence-of-impact).*
- **Pre-committed dissent log** (from Session 004's Skeptic) — after synthesis the operator writes what they expected the synthesis to conclude before reading it, committed as a separate hashed file. Measurement tool for operator-synthesis alignment. *Activation precondition: a session surfaces evidence of suspected operator-synthesis alignment (e.g., a synthesis that reads as confirmation of the operator's stated priors rather than of the raw outputs).*
- **Integrity hashing, append-only raw files, convener attestation** (from Session 004's Archivist) — `raw_response_sha256` per raw output, enforced by `validate.sh`; raw files append-only from commit; a `convener_attestation` field in manifests. All deferred to a future tooling session. *Activation precondition: one instance of suspected post-hoc editing of a raw output, OR a future session decides check 13's gaming surface needs narrowing. These three items are paired; adopt together or not at all, since each alone is partial.*
- **Structural validation cross-check for OI-004 honesty** (from Session 004's Skeptic) — `validate.sh` fails sessions that claim OI-004 narrowing in a decision record while recording all `participant_kind: claude-subagent` in their provenance. Requires extending the validator's parsing beyond structural checks. *Activation precondition (revised Session 006, D-042): `triggers_met:` is adopted prospectively (done Session 006 via D-037 through D-040) AND at least one post-adoption decision asserting an OI-004 state change exists, OR a separate non-mutating retrospective index has been produced for earlier cases per the D-039 retrospective-artefact pattern. Rationale for revision: Session 005's D-033 narrowing (the original first test case) predates `triggers_met:` adoption under D-039's session-number gating; a derivative check would have no in-scope test case until a post-adoption OI-004-state-change decision is made. Additionally, Session 006's D-043 is itself an OI-004 state change and implementing the check in Session 006 would have required grading Session 006's own claim (Skeptic, Session 006 Q6) — a conflict of interest on first firing.*
- **Disagreement-density metric** (from Session 003) — count or rate disagreements across perspectives' outputs; flag suspiciously low values as likely training-induced correlation. *Activation precondition: a reporter-tool scope is defined distinct from `validate.sh` (which is scoped to structural checks, not measurements).*
- **Pluggable synthesizer role** — different model, human reviewer, or panel synthesising. Requires designing synthesizer selection and accountability. *Activation precondition: a session surfaces a load-bearing synthesizer-framing failure that single-synthesizer conventions cannot correct.*
- **Non-Claude synthesizer** — when synthesis is itself load-bearing and contested, the synthesizer may be a non-Claude participant (reducing the single-model re-entry risk). *Activation precondition: check 13 gaming becomes a live concern (recorded in provenance) AND a non-Claude synthesizer channel is available.*
- **Multi-agent synthesis** — recursive application of this pattern to the synthesis step itself when contested. *Activation precondition: a session surfaces a synthesis quality gap unaddressed by single-synthesizer conventions (citation, dissent-preservation, `[synth]` markers, quote-over-paraphrase).*
- **Non-Anthropic model participation via API** — direct path to OI-004 closure that becomes available when the workspace's permissions and secrets allow an outbound non-Anthropic API call. *Activation precondition: a concrete need for API-based transport that CLI wrappers (demonstrated usable in Session 005 via `codex exec`) cannot serve.*

## Validation

To validate this specification:

1. For every session with provenance, identify each Decision the session recorded. Each Decision that meets any trigger in "When Multi-Agent Deliberation Is Required" must be backed by either (a) multi-agent deliberation artifacts (raw perspective files plus a synthesis) or (b) an explicit single-agent annotation naming the reason.
2. For every Decision that meets any trigger in "When Non-Claude Participation Is Required", there must be either (a) at least one participant in the deliberation with `participant_kind` other than `claude-subagent` (and `anthropic-other`), with matching manifest entries, or (b) an explicit `non_claude_participation: skipped` annotation with a recorded reason and `retry_in_session` field.
3. For each multi-agent deliberation, verify that at least three raw perspective files exist in the session's provenance.
4. For each synthesis file, verify that the synthesizer's identity is recorded in the file's frontmatter (or in the deliberation's `manifest.json` in the subdirectory layout).
5. For each synthesis file, check that every claim attributing a position to a perspective cites a raw-output source. Unattributed perspective-specific language is a validation failure.
6. For each multi-agent deliberation, confirm the synthesis includes a Limitations note matching the required content above (either directly or by reference to this specification).
7. Confirm that briefs, if preserved as separate files, differ only in their role-specific sections (the shared sections are byte-identical).
8. For each heterogeneous-participant deliberation, confirm the per-participant manifests exist, the session-level participants index exists, and every required manifest field is present (with `unknown` recorded as a literal string where applicable).
9. For any session that records `cross_model: true`, verify that at least one participant's manifest has `training_lineage_overlap_with_claude` other than `known-overlap` (i.e., `unknown` or `independent-claim`) or `participant_kind: human`. A session recording `cross_model: true` with all-Claude manifests is a validation failure.
10. Confirm that OI-004 is still open. If a future session claims to close OI-004, verify the closure is justified by the criteria listed in the Closure section and decided explicitly, not asserted.

Status of automation (as of v3, Session 006):

- Checks 3, 8, 9 are automated as `validate.sh` checks 11, 12, 13 respectively (Session 005, D-028).
- Checks 1 and 2 are automated as `validate.sh` checks 14 and 15 respectively (Session 006, D-040), gated on session ≥ 006 per D-039 and dependent on the `triggers_met:` schema (D-037, D-038).
- Checks 4–7, 10 remain candidates for the Tier 2 guided-assessment questions.
