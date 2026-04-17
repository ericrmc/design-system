---
session: 003
title: Deliberation — Multi-Agent Deliberation Pattern (synthesized)
date: 2026-04-17
status: complete
synthesizer: session-003 orchestrating agent (Claude Opus 4.7, same model family as deliberators)
---

# Deliberation — Session 003: Multi-Agent Deliberation Pattern

## How This Deliberation Was Conducted

This is the methodology's first non-simulated deliberation. Five perspectives were convened as independent, parallel subagents via the Agent tool (`general-purpose` type). Each subagent ran in an isolated context, received an identical methodology brief plus a role-specific stance, answered seven design questions, and returned a raw markdown response. None saw the others' outputs. Raw outputs are preserved verbatim at `01a-` through `01e-` and are the ground truth; this synthesis is one synthesizer's reading of them and must be traceable back to sources.

The five perspectives:

1. **The Methodologist** — coherence with existing methodology principles (`01a-perspective-methodologist.md`)
2. **The Pragmatist** — what actually works under real session conditions (`01b-perspective-pragmatist.md`)
3. **The Skeptic** (required adversarial) — challenge the premise itself (`01c-perspective-skeptic.md`)
4. **The Archivist** — provenance, reproducibility, recordkeeping (`01d-perspective-archivist.md`)
5. **The Futurist** — evolvability beyond current mechanism (`01e-perspective-futurist.md`)

All perspectives were run by Claude Opus 4.7 subagents — the same model family as the synthesizer. This is a known and preserved limitation.

## Synthesis Conventions

Following the Archivist's proposal [`01d-perspective-archivist.md`, Q4]: claims attributing a position to a perspective cite the source file; claims not directly sourced from any perspective are marked `[synth]`. This lets future readers compute the ratio of cited to synthesized content and judge whether the synthesizer was faithful.

---

## Q1: When should multi-agent deliberation be used?

**Convergence.** All five perspectives reject "every deliberation" as the default — all call for selective use. None proposes a pure time-cost threshold; all propose criteria tied to decision consequentiality.

**Divergence on stringency.** Criteria span a spectrum:
- Methodologist: required "whenever the Deliberate activity produces a Decision that will be recorded in provenance — i.e., anything that becomes a D-### entry or modifies a specification" [`01a`, Q1]. This is the broadest selective rule.
- Archivist: required "whenever a session produces a Decision that will be cited by name (D-xxx) in any future specification's Validation section" [`01d`, Q1]. Narrower than Methodologist.
- Pragmatist: four concrete triggers — kernel/Purpose-section changes, new top-level specifications, "reasonable practitioners could disagree" (requires author to name two plausible positions), or explicit "load-bearing" tag [`01b`, Q1].
- Futurist: "decision properties, not session phases ... when a decision's consequences propagate" [`01e`, Q1].
- Skeptic: "never, under the current mechanism, as a default" — and more strongly, "only when a single agent has already produced a draft decision and a named reviewer can identify a specific axis of likely blindspot" [`01c`, Q1].

**Preserved dissent.** The Skeptic rejects even selective-default framing: "the framing of the seven questions presumes multi-agent will be standard and only asks *which* cases. That ordering is already a concession I refuse" [`01c`, Q1]. The Skeptic predicts the mechanism will drift to ritual within five sessions.

**[synth] Resolution.** All non-Skeptic perspectives agree on *selective*. They differ on stringency. The Methodologist's criterion (any decision recorded as a D-###) is broadest; the Skeptic's (only when a named blindspot axis is identified) is narrowest. The Pragmatist's and Archivist's criteria cluster around "decisions that affect specifications." A workable criterion set should combine: (a) Pragmatist's forcing functions (kernel changes, new specs — these are non-negotiable triggers), (b) a contested-design-space test (Pragmatist's "can you name two positions?"), and (c) opt-out with a one-line recorded justification for decisions that cross these thresholds but are judged non-load-bearing by the session author. The Skeptic's drift-to-ritual concern remains open and is tracked.

**Points on which all perspectives agree:**
- "Every deliberation uses multi-agent" is wrong.
- The trigger must be specific enough to prevent both over-use and silent regression.
- The criterion should be recorded alongside the decision so thresholds accumulate evidence.

---

## Q2: How should perspectives be selected and briefed?

**Convergence on range.** All numerical proposals cluster in 3–7:
- Methodologist: 3–5 [`01a`, Q2]
- Pragmatist: "3, occasionally 4, never 2 or 5+" [`01b`, Q2]
- Archivist: 3–5 [`01d`, Q2]
- Futurist: 3–7 [`01e`, Q2]
- Skeptic: "below ~4 you get theater, above ~6 you get synthesis collapse, and at any number the briefs do the real work" [`01c`, Q2]

**[synth] The overlap is 3–5 perspectives.** The Pragmatist's hard ceiling at 4 and the Futurist's ceiling at 7 are the extremes. A reasonable rule: default 3, up to 5, with 5 requiring written justification.

**Divergence on stance-brief construction.**
- Methodologist: "roles with stakes, not viewpoints with labels" — briefs contain problem verbatim, role's accountability, decision questions, format, context instructions [`01a`, Q2].
- Pragmatist: "150-250 words each, hard cap 300. Structure: (a) one-sentence stance, (b) what this perspective values, (c) what it is suspicious of, (d) specific argumentative moves" [`01b`, Q2].
- Archivist: fixed schema for reproducibility — shared sections byte-identical across briefs [`01d`, Q2].
- Futurist: abstract the terminology — "stance specification" rather than "brief," "participant" rather than "subagent" [`01e`, Q2].
- Skeptic: "writing the brief *is* the deliberation ... an agent inhabiting a pre-written stance is a puppet with extra steps" [`01c`, Q2]. The Skeptic has no alternative but names the problem as fundamental.

**Divergence on workspace context.**
- Methodologist and Pragmatist and Archivist: minimal, identical context per agent — "asymmetric context creates spurious disagreement" [`01a`, Q2].
- Futurist: *differentiated* context per perspective — "each participant gets the problem brief and only the files their stance requires" [`01e`, Q2]. Uniform distribution "undermines the value of differentiated perspectives."

**Preserved disagreement.** The Methodologist-Pragmatist-Archivist view favors uniform context for archival and auditability reasons. The Futurist view favors differentiated context for diversity. These are genuinely different design philosophies, not reconcilable by averaging.

**[synth] Provisional position.** For the first pattern version, default to *uniform minimal* context (the current session's approach). The Futurist's differentiated-context case is real but riskier — it requires the convener to correctly anticipate what each perspective needs, which itself leaks framing. Archive the Futurist's case as an OPEN direction for future revisions once the uniform case has accumulated evidence.

**Skeptic's escalation, preserved.** "An agent inhabiting a pre-written stance is a puppet with extra steps" [`01c`, Q2]. The Skeptic is correct that brief-writing is upstream framing the methodology has no mechanism to audit. This is not resolved; it is a permanent property of the pattern and must be named explicitly in the specification.

---

## Q3: How should anchoring be prevented?

**Convergence.** All five perspectives agree that parallel isolation handles *conversational* anchoring. All five perspectives agree that it does not handle other forms.

**Brief-anchoring** — raised by Methodologist, Skeptic, Archivist:
- Methodologist: checklist-review of brief before launching [`01a`, Q3].
- Archivist: briefs committed to git before deliberation begins; commit hash is the anchor; convener themselves must be briefed with a `convene-brief.md` [`01d`, Q3].
- Skeptic: unaudited brief-writing "creates infinite regress" if you try to fix it with more multi-agent [`01c`, Q6].

**Training-anchoring** — raised most sharply by the Skeptic, acknowledged by others:
- Skeptic: "Four Claude instances sharing weights ... will correlate in ways that look like agreement but are actually shared priors. The methodology will read this correlation as convergence-on-truth. This is the central deception of the proposed pattern" [`01c`, Q3].
- Pragmatist: "Treat consensus across subagents as weak evidence, not strong" [`01b`, Q6].
- Archivist: "shared training produces shared blind spots" [`01d`, Q6].
- Futurist: "parallel isolation prevents *conversational* anchoring but not *training-distribution* anchoring" [`01e`, Q6].

**Synthesis-anchoring** — raised by Skeptic, Futurist, Archivist:
- Futurist: "order in which perspectives are presented to the synthesis step ... randomize or alphabetize" [`01e`, Q3].
- Skeptic: synthesis is "where single-agent bias re-enters through the front door" [`01c`, Q4].
- Archivist: synthesis must cite raw outputs with file+position references [`01d`, Q4].

**[synth] Resolution.** Adopt all three classes of mitigation:
1. **Conversational anchoring** — parallel-isolated contexts (already the mechanism).
2. **Brief-anchoring** — briefs committed before deliberation; convening rationale preserved; no edits mid-deliberation.
3. **Training-anchoring** — explicit, unsoftened acknowledgment in the specification that this mechanism does not address it, and a standing recommendation to include non-Claude or human participants when available. OI-004 stays open precisely because this is unaddressed.
4. **Synthesis-anchoring** — synthesis must cite sources per the Archivist's convention; `[synth]` marker for synthesizer-original claims; alphabetize source presentation to synthesizer.

---

## Q4: How should outputs be synthesized?

**Convergence on structure.** All perspectives agree synthesis must:
- Preserve raw outputs verbatim as separate artifacts.
- Distinguish agreement from disagreement from coverage (Futurist introduces the useful distinction between *convergence* — all perspectives independently reached a conclusion — and *coverage* — only one perspective raised a point, rest were silent) [`01e`, Q4].
- Keep synthesis and the Decide step separate — synthesis maps, does not decide.

**Divergence on who synthesizes.**
- Methodologist: "a separate synthesis step performed by a fresh agent (not one of the deliberators)" [`01a`, Q4].
- Pragmatist: "one synthesis pass by a single agent (likely the session lead)" [`01b`, Q4].
- Archivist: single synthesizer, who names themselves [`01d`, Q4].
- Futurist: "pluggable — a different model, a human, or a panel. Don't bake in 'the orchestrator synthesizes'" [`01e`, Q4].
- Skeptic: any single synthesizer "launders single-agent conclusions through apparent plurality" [`01c`, Q4]; synthesis must quote not paraphrase.

**[synth] Provisional position.** The Methodologist's "fresh agent, not one of the deliberators" is the strictest principled position. The Pragmatist's "session lead" is practical but reintroduces the role's framing. The Futurist's "pluggable" is the right long-term shape.

For this pattern's first version: the synthesizer must not have been one of the deliberation's perspectives. In the current session, that is satisfied — the orchestrating (synthesizing) agent did not play any of the five perspectives. The synthesis specification should require this separation and record the synthesizer's identity.

**Skeptic's demand, adopted:** "Synthesis must quote, not paraphrase, the load-bearing sentences from each perspective. Disagreements must be listed as disagreements, not resolved. The synthesis agent should be forbidden from introducing claims not traceable to a raw output" [`01c`, Q4]. This synthesis attempts to comply. Where `[synth]` appears, the synthesizer is taking a position not present in raw outputs; every other claim cites a source.

---

## Q5: How should this be recorded in provenance?

**Total convergence.** All five perspectives agree: preserve briefs, raw outputs, synthesis, and synthesizer identity. No perspective argues for less. The Archivist proposes the most detailed schema.

**Divergence on directory layout.**
- Archivist proposes: `provenance/sessions/<session-id>/deliberations/<decision-id>/` with subdirectories for briefs, responses, synthesis, manifest.json [`01d`, Q5].
- Pragmatist: "one directory per deliberation under the session's provenance folder" [`01b`, Q5]. Simpler.
- Others: preservation yes, layout not specified.

**[synth] Provisional position.** The Archivist's layout is more rigorous but heavier. For this session (one deliberation, manageable at five numbered files at the session root), the existing flat numbered-files convention (`01a-...md`, `01b-...md`) is sufficient and consistent with Sessions 001 and 002. When a session contains multiple deliberations, adopt the Archivist's subdirectory layout. Make this tiered convention explicit in the specification.

**[synth] manifest.json.** The Archivist's `manifest.json` recording model IDs, timestamps, and token counts is worth adopting in principle but introduces a new file type. For now, store this metadata in the synthesis file's frontmatter. Upgrade to a dedicated `manifest.json` if the metadata outgrows frontmatter.

---

## Q6: What are residual limitations?

**Unanimous agreement.** All five perspectives state that parallel Claude agents share training and therefore share blind spots. None softens this. The specification language should be uncompromising, per the Skeptic: "Treat its outputs as one agent's structured self-questioning, not as a panel" [`01c`, Q6]. The Archivist's suggested text [`01d`, Q6] and the Methodologist's "this mechanism is the floor, not the ceiling" [`01a`, Q6] are both adoptable.

**Graceful degradation** (raised by Futurist): what happens when a participant fails? The Futurist proposes minimum-viable-quorum and a protocol for recording absence [`01e`, Q6]. **[synth]** Adopt: if a participant fails to respond (error, refusal, malformed output), the deliberation may proceed with remaining participants if at least three remain, but the failure is recorded as part of the deliberation's manifest. Participants refusing the assigned stance should have the refusal preserved as signal.

**Brief-writing has no adversary.** Raised by Skeptic and implicitly by Methodologist. The specification must acknowledge this as a permanent property.

---

## Q7: Does methodology-kernel need substantive revision?

**Majority position (4 of 5): elaboration, not revision.** Methodologist, Pragmatist, Archivist, and Futurist (conditionally) all argue for a new specification plus a minor kernel update.

**Minority position (Skeptic): substantive revision.** "Treating this as elaboration ... lets the methodology avoid confronting that D-009 and OI-004 are not solved by this session, merely attended to. The kernel should be revised to state that no current mechanism achieves genuine perspective independence" [`01c`, Q7].

**[synth] Resolution.** Preserve both positions via this approach:
- Create a new specification, `multi-agent-deliberation.md`, carrying the mechanism detail (this follows the 4-of-5 majority and matches the precedent of how `validation-approach.md` was added in Session 002).
- Update `methodology-kernel.md` with a small addition under Convene/Deliberate pointing to the new spec.
- **Honor the Skeptic's core demand explicitly:** do not close OI-004. The new specification states in plain terms that this mechanism does not achieve genuine perspective independence, that OI-004 remains open, and that closure requires non-Claude and/or human participants.

This is the compromise: the Skeptic's substantive complaint is encoded in the specification's Limitations section and in OI-004's continued openness, not in a kernel revision. If the Skeptic's critique proves correct — if the methodology drifts to treating multi-agent as a proxy for quality — a future session must revise the kernel to force honesty.

The Futurist's conditional (whether the kernel currently smuggles in single-agent assumptions) has been checked by the synthesizer: `methodology-kernel.md` sections 3 (Convene) and 4 (Deliberate) are mechanism-neutral — they say "perspectives" without specifying how they are instantiated. The kernel already hosts this pattern; a minor pointer is sufficient.

---

## Points of Agreement (across all five perspectives)

1. Multi-agent deliberation should be selective, not default-on.
2. Perspectives must be chosen for the specific work (no permanent roster) — this reaffirms D-005.
3. Raw outputs, briefs, and synthesis must all be preserved as provenance.
4. All perspectives share Claude's training; this is a real limitation the specification must name honestly.
5. Synthesis must not resolve disagreement into compromise — it must preserve dissent.
6. A new specification (`multi-agent-deliberation.md`) should be created; the kernel needs at most a pointer (with the Skeptic's caveat noted).

## Points of Disagreement (preserved, not resolved)

1. **Whether multi-agent deliberation is progress.** Four perspectives say yes-with-limits; the Skeptic says the pattern will become ritual within five sessions and the synthesis step launders single-agent bias. The Skeptic's dissent is preserved and reflected in the Limitations section of the new specification and in OI-004's continued openness.
2. **Uniform vs. differentiated context per perspective.** Methodologist/Pragmatist/Archivist favor uniform minimal context. Futurist favors differentiated context. For v1, uniform wins on simplicity and audit-traceability. Recorded as a future revision direction.
3. **Required stringency of the trigger.** Methodologist's broadest rule (any D-### decision) vs. Skeptic's narrowest (only when a named blindspot exists) vs. Pragmatist's concrete set. Adopted set leans toward Pragmatist's concrete triggers; stringency may tighten or loosen with evidence.
4. **Whether the kernel needs revision.** Skeptic says yes; others say no. Adopted: no revision, but OI-004 remains open and the Skeptic's argument is archived explicitly in the new specification.

## Open Threads Not Resolved

- **Recursive synthesis.** If a deliberation's synthesis is itself load-bearing and contested (Pragmatist flagged this), does the synthesis step itself need multi-agent treatment? Unresolved — deferred as an open question.
- **Disagreement-density measurement.** The Skeptic proposed measuring disagreement density and flagging sessions where it is low as likely-correlated-rather-than-correct [`01c`, Q3]. Concrete and implementable; deferred as a candidate enhancement for a future session.
- **Non-Claude or human participants.** The mechanism to actually achieve non-monoculture participation is not designed in this session. OI-004 remains open for this reason.
- **Linter for synthesis citation coverage.** Archivist's idea [`01d`, Q4] — an automated check that synthesis contains no unattributed perspective-specific language — is feasible but not in this session's scope.
