---
title: Multi-Agent Deliberation
version: 1
status: active
created: 2026-04-17
last-updated: 2026-04-17
supersedes: none
---

# Multi-Agent Deliberation

## Purpose

This specification defines how the methodology instantiates genuine multi-perspective deliberation. It describes when multi-agent deliberation is required, how perspectives are convened, how stance briefs are structured, how their outputs are synthesized, how the whole process is recorded, and what limitations remain. It serves the methodology's explicit injunction against single-perspective substantive work, and partially addresses Open Issue OI-004 (genuinely independent perspectives).

The term "multi-agent deliberation" describes a property, not a mechanism: that the perspectives reasoning about a question arrive at their positions without seeing each other's positions. The current implementation realises this property via parallel context-isolated subagents of the Claude model family. Future implementations may realise the same property via different-model agents, persistent personas, asynchronous cross-session deliberation, or human participants; the specification is written so those extensions are changes of mechanism, not of pattern.

## Specification

### When Multi-Agent Deliberation Is Required

A session must convene a multi-agent deliberation for any decision where at least one of the following is true:

1. The decision modifies `methodology-kernel.md`.
2. The decision creates or substantively revises any specification in `specifications/`.
3. The question is one on which reasonable practitioners could genuinely disagree — operationalised as: the session author can name at least two plausible positions before the deliberation begins.
4. The session author has marked the decision load-bearing for any other reason and records why.

For any decision that meets at least one of these triggers but is made by a single agent anyway, the decision record must state this explicitly, naming the reason (e.g., "Single-perspective; non-load-bearing: minor correction per D-014 precedent"). Unstated single-perspective decisions on triggered questions are a specification violation.

Decisions that meet none of the triggers — typos, reordering, routine execution of already-decided plans — may be made by a single agent without annotation.

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

### Mechanism

The required property is **independence-preservation during the independent phase**: no perspective's output can influence another perspective's reasoning while each is forming its position.

The current implementation realises this via parallel subagents launched through Claude Code's Agent tool, each in an isolated context. The specification does not mandate this mechanism. Alternative realisations that preserve the required property — different-model agents, persistent human reviewers briefed separately, asynchronous cross-session deliberations with explicit quarantine — are consistent with this specification.

### Synthesis

After all perspectives have returned their raw outputs, a synthesis step produces a single deliberation record.

- **Synthesizer identity.** The synthesizer must not have been one of the deliberation's perspectives. The synthesizer's identity (agent/model/date) is recorded in the synthesis file's frontmatter.
- **Citation requirement.** Claims attributing a position to a perspective must cite the source file and section/question: `[source-file, Q#]` or `[source-file, section]`.
- **Synthesizer-original claims.** Claims not directly sourced from any raw perspective are marked `[synth]`. This lets future readers compute the ratio of sourced to synthesised content and judge faithfulness.
- **Quote over paraphrase for load-bearing claims.** Where a perspective's argument turns on specific language, the synthesis quotes that language rather than paraphrasing.
- **Preserve dissent.** Disagreements are listed as disagreements. A minority position with a strong argument is preserved as-is, not diluted. Majority/minority structure is reported explicitly.
- **Convergence vs coverage.** The synthesis distinguishes *convergence* (all perspectives independently reached a similar conclusion) from *coverage* (only one perspective raised a point; others were silent). These are different epistemic states.
- **Synthesis order anchoring.** Perspectives are presented to the synthesis step in alphabetical order by role name, or in a fixed order documented in the synthesis file, to reduce ordering-induced synthesizer bias.

Synthesis maps; it does not decide. The Decide activity operates on the synthesis, not on raw outputs directly.

### Provenance Layout

Tiered by the number of deliberations in a session.

**Single-deliberation sessions** use flat numbered files at the session's provenance root, consistent with Sessions 001 and 002:

```
provenance/<NNN-title>/
  00-assessment.md
  01a-perspective-<role>.md
  01b-perspective-<role>.md
  ...
  01-deliberation.md          # synthesis
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
      synthesis.md
      manifest.json
  02-decisions.md
  03-close.md
```

`manifest.json` records model IDs, timestamps, and a commit hash at convening time. In the flat layout, this metadata goes in the synthesis file's frontmatter.

### Graceful Degradation

- **Minimum viable quorum.** If a perspective fails to return an output (error, refusal, malformed response), the deliberation may proceed with the remaining perspectives provided at least three returned valid outputs. The failure is recorded in the synthesis file's frontmatter or in `manifest.json`.
- **Stance refusal.** A perspective that refuses the assigned stance, or that substantively disagrees with the brief itself, has its refusal preserved as provenance. Refusal is signal, not an error to coerce around.
- **Fewer than three valid outputs.** The deliberation must be re-run or the question reformulated. A synthesis over one or two perspectives is not a multi-agent deliberation.

### Limitations

These statements are required content for every multi-agent deliberation's synthesis or decision record that relies on the current implementation:

- **All current perspectives share a model family.** The parallel-subagent implementation uses instances of the same Claude model family. Shared training produces shared blind spots: the same cultural priors, argumentative reflexes, refusal patterns, and aesthetic preferences.
- **Parallel isolation prevents conversational anchoring, not training-distribution anchoring.** Four instances of the same model, given briefs written in a shared vocabulary, will correlate in ways that look like agreement but are actually shared priors. Consensus across subagents is weak evidence, not strong.
- **Brief-writing has no adversary.** The convening agent's framing choices propagate into all perspectives identically. Adding multi-agent to brief-writing creates infinite regress; the methodology does not pretend otherwise.
- **The synthesis step is the pattern's highest-risk single-agent re-entry point.** Synthesis conventions (citation, dissent-preservation, `[synth]` marker, quote-over-paraphrase) reduce but do not eliminate this risk.
- **This mechanism does not close OI-004.** OI-004 is for truly independent perspectives — different models, human participants, or both. The current implementation is a meaningful floor, not a ceiling. Sessions with access to different models or human reviewers should use them.

The specification's tone on limitations is deliberately uncompromising. Softening the language in future revisions is not a minor correction.

### Interaction with Existing Decisions

- **D-005** (perspectives are work-specific, not fixed) — reaffirmed.
- **D-009** (acknowledgment of simulated disagreement) — remains in force. Its scope now includes the Claude-monoculture limitation of the current mechanism, not only the original same-context simulation case.
- **D-014** (minor-correction heuristic) — reaffirmed by D-020's treatment of the kernel pointer as a minor correction, because adding a pointer is *anticipated by* the kernel's mechanism-neutral Convene/Deliberate language.

### Open Extensions

These directions are noted as candidates for future revisions, not mandated:

- **Differentiated context per perspective** (the Futurist's position from Session 003) — each perspective receives only the workspace context its stance requires, declared by the brief.
- **Non-Claude or human participants** — direct path to narrowing OI-004. Requires infrastructure not available this session.
- **Disagreement-density metric** — count or rate disagreements across perspectives' outputs; flag suspiciously low values as likely training-induced correlation (the Skeptic's proposal from Session 003).
- **Pluggable synthesizer role** — different model, human reviewer, or panel synthesising. Requires designing synthesizer selection and accountability.
- **Automated citation-coverage check** — a validation tool check that flags synthesis text containing perspective-specific language not attributable to a cited raw output (the Archivist's linter idea).
- **Multi-agent synthesis** — when the synthesis itself is contested and load-bearing. Recursive application of this pattern to its own risky step.

## Validation

To validate this specification:

1. For every session with provenance, identify each Decision the session recorded. Each Decision that meets any trigger in "When Multi-Agent Deliberation Is Required" must be backed by either (a) multi-agent deliberation artifacts (raw perspective files plus a synthesis) or (b) an explicit single-agent annotation naming the reason.
2. For each multi-agent deliberation, verify that at least three raw perspective files exist in the session's provenance.
3. For each synthesis file, verify that the synthesizer's identity is recorded in the file's frontmatter (or in the deliberation's `manifest.json` in the subdirectory layout).
4. For each synthesis file, check that every claim attributing a position to a perspective cites a raw-output source. Unattributed perspective-specific language is a validation failure.
5. For each multi-agent deliberation, confirm the synthesis includes a Limitations note matching the required content above (either directly or by reference to this specification).
6. Confirm that briefs, if preserved as separate files, differ only in their role-specific sections (the shared sections are byte-identical).
7. Confirm that OI-004 is still open. If a future session claims to close OI-004, verify the closure is justified by demonstrated cross-model or human participation.

Checks 1 and 2 are candidates for automation in a future revision of `tools/validate.sh`. Checks 3–7 are candidates for the Tier 2 guided-assessment questions.
