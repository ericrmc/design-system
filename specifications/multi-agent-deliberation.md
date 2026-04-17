---
title: Multi-Agent Deliberation
version: 2
status: active
created: 2026-04-17
last-updated: 2026-04-18
updated-by-session: 004
supersedes: multi-agent-deliberation-v1.md
---

# Multi-Agent Deliberation

## Purpose

This specification defines how the methodology instantiates genuine multi-perspective deliberation. It describes when multi-agent deliberation is required, how perspectives are convened, how stance briefs are structured, how their outputs are synthesized, how the whole process is recorded, and what limitations remain. It serves the methodology's explicit injunction against single-perspective substantive work, and partially addresses Open Issue OI-004 (genuinely independent perspectives).

The term "multi-agent deliberation" describes a property, not a mechanism: that the perspectives reasoning about a question arrive at their positions without seeing each other's positions. The current implementations realise this property via parallel context-isolated subagents of the Claude model family, optionally augmented by non-Claude participants (human reviewers or non-Anthropic models) following the Non-Claude Participation mechanism below. Future implementations may extend this further via different-model agents accessed through their own endpoints, persistent personas, or asynchronous cross-session deliberation; the specification is written so those extensions are changes of mechanism, not of pattern.

Version 2 adds the Non-Claude Participation mechanism, the three-layer heterogeneous-participant recording schema, and associated trigger rules. It supersedes v1 (`multi-agent-deliberation-v1.md`).

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

**Layer 3 — Session-level index.** `provenance/NNN/participants.yaml` (preferred) or `provenance/NNN/participants.md` listing each participant and their manifest path.

**Composition fields (synthesis frontmatter).** The synthesis file's frontmatter records:

```yaml
participants_family: claude-only | mixed-anthropic | cross-model
cross_model: true | false
non_claude_participants: <integer>
```

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
4. **Articulation.** A successor decision defines what "substantively different training provenance" means and enumerates acceptable participant kinds.

OI-004 is not automatically closed on meeting these criteria; a future session must deliberate and decide. "Closable" and "closed" are distinct states.

### Interaction with Existing Decisions

- **D-005** (perspectives are work-specific, not fixed) — reaffirmed.
- **D-009** (acknowledgment of simulated disagreement) — remains in force. Its scope now includes the Claude-monoculture limitation of the Claude-subagent mechanism, not only the original same-context simulation case, and it extends further to the trust-boundary limitation of human-mediated non-Claude participation transport.
- **D-014** (minor-correction heuristic) — reaffirmed.
- **D-016** (multi-agent triggers) — reaffirmed; this specification's "When Non-Claude Participation Is Required" extends, rather than replaces, D-016's triggers.
- **D-020** (treatment of v1 kernel pointer as minor) — reaffirmed.
- **D-022** (Claude-only is not cross-model) — integrated as the Claude-Only-Is-Not-Cross-Model rule above.
- **D-025** (this session does not narrow OI-004 operationally) — the specification records OI-004 as open awaiting first operational use of the mechanism.

### Open Extensions

These directions are noted as candidates for future revisions, not mandated:

- **Differentiated context per perspective** (from Session 003's Futurist position) — each perspective receives only the workspace context its stance requires, declared by the brief.
- **Cross-lineage-influence ratio** (from Session 004's Skeptic) — a measured ratio, across a rolling window of deliberations, of decisions where a non-Claude participant's position differed from the synthesized Claude consensus and the synthesis adopted the non-Claude position. Suggested floor: above 10% over a ten-deliberation window for non-Claude participation to be considered genuinely impactful. Not mandated; candidate for a validation-tool enhancement.
- **Pre-committed dissent log** (from Session 004's Skeptic) — after synthesis the operator writes what they expected the synthesis to conclude before reading it, committed as a separate hashed file. Measurement tool for operator-synthesis alignment.
- **Integrity hashing, append-only raw files, convener attestation** (from Session 004's Archivist) — `raw_response_sha256` per raw output, enforced by `validate.sh`; raw files append-only from commit; a `convener_attestation` field in manifests. All deferred to a future tooling session.
- **Structural validation cross-check for OI-004 honesty** (from Session 004's Skeptic) — `validate.sh` fails sessions that claim OI-004 narrowing in a decision record while recording all `participant_kind: claude-subagent` in their provenance. Requires extending the validator's parsing beyond structural checks.
- **Disagreement-density metric** (from Session 003) — count or rate disagreements across perspectives' outputs; flag suspiciously low values as likely training-induced correlation.
- **Pluggable synthesizer role** — different model, human reviewer, or panel synthesising. Requires designing synthesizer selection and accountability.
- **Non-Claude synthesizer** — when synthesis is itself load-bearing and contested, the synthesizer may be a non-Claude participant (reducing the single-model re-entry risk).
- **Multi-agent synthesis** — recursive application of this pattern to the synthesis step itself when contested.
- **Non-Anthropic model participation via API** — direct path to OI-004 closure that becomes available when the workspace's permissions and secrets allow an outbound non-Anthropic API call.

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

Checks 1–3, 8, 9 are candidates for automation in a future revision of `tools/validate.sh`. Checks 4–7, 10 are candidates for the Tier 2 guided-assessment questions.
