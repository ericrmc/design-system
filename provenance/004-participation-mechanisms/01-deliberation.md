---
session: 004
title: Deliberation — Non-Claude Participation Mechanism (synthesized)
date: 2026-04-18
status: complete
synthesizer: session-004 orchestrating agent (Claude Opus 4.7, same model family as deliberators)
synthesizer-independence: did not play any of the three perspectives (Archivist, Integrator, Skeptic)
deliberation-anchor-commit: ab86605aaeea7b2bca88f89ecc2ab3b88dd2b378
perspective-order: alphabetical by role name
---

# Deliberation — Session 004: Non-Claude Participation Mechanism

## How This Deliberation Was Conducted

Three perspectives were convened as independent, parallel subagents via the Agent tool (`general-purpose` type, `model: opus`). Each subagent ran in an isolated context, received an identical shared brief plus a role-specific stance (see `01-brief-shared.md`, commit `ab86605`), answered six design questions, and returned a raw markdown response. None saw the others' outputs. Raw outputs are preserved verbatim at `01a-perspective-archivist.md`, `01b-perspective-integrator.md`, and `01c-perspective-skeptic.md` and are the ground truth; this synthesis is one synthesizer's reading of them and must be traceable back to sources. Perspectives are presented alphabetically throughout to reduce synthesizer-ordering bias (per D-018).

The three perspectives:

1. **The Archivist** — decades-later auditability, identity/version/reconstructibility (`01a-perspective-archivist.md`)
2. **The Integrator** — what runs today with available infrastructure (`01b-perspective-integrator.md`)
3. **The Skeptic** (required adversarial) — challenge whether any proposed mechanism narrows OI-004 at all (`01c-perspective-skeptic.md`)

All three subagents ran Claude Opus 4.7 — the same model family as the synthesizer. This is an acknowledged limitation preserved intentionally: this session's design work is itself subject to the critique it is designing a solution for, and the Skeptic's brief calls this out explicitly.

## Synthesis Conventions

Following D-018 and Session 003's precedent: claims attributing a position to a perspective cite the source file and question; claims not directly sourced are marked `[synth]`; load-bearing language is quoted rather than paraphrased; dissent is preserved as dissent; convergence (all perspectives independently reached a similar conclusion) is distinguished from coverage (only one perspective raised a point, others silent).

---

## Q1: Minimum viable non-Claude participation mechanism

**Convergence.** All three perspectives converge on a **human-reviewer mechanism** as the minimum viable path. None propose a non-Anthropic-model API call (all agree the workspace has no such keys configured and adding them is its own work).

**Divergence on where in the pipeline the human enters.**

- **Archivist** — a non-Claude participant (human or external model) joins as a **full perspective** via a committed brief-drop pattern: "the convener commits the same brief used for Claude perspectives to `provenance/NNN/briefs/<perspective>.md`, then delivers it to one non-Claude participant ... and commits the returned response verbatim as `provenance/NNN/raw/<perspective>.md`" [`01a-perspective-archivist.md`, Q1]. The convener is explicitly the transport layer; the workspace guarantees the *record*, not the *generation*.
- **Integrator** — a human enters as a full perspective, with an explicit **asynchronous halt** to force the deliberation to wait: "The session commits all briefs (including the empty-response human brief), then **halts**. A `provenance/NNN/STATUS.md` file is written with a single field: `awaiting: human-reviewer`" [`01b-perspective-integrator.md`, Q1]. Emphasises: "The asynchronous halt is load-bearing. Without it, the synthesizer proceeds before the human responds, and the human becomes a rubber-stamp rather than a perspective" [`01b`, Q1].
- **Skeptic** — the human enters not as a perspective but as a **reviewer with veto power over the synthesis**: "after raw perspective outputs are committed to `provenance/NNN/` but before the synthesizer runs, a named second human reads the raw outputs and writes `provenance/NNN/human-review.md`" [`01c-perspective-skeptic.md`, Q1]. Emphatic qualifier: "The mechanism narrows OI-004 *if and only if* the reviewer is non-consensual with the operator in an auditable way. Without that, it is ceremony. I would accept this mechanism as a **floor** — something better than nothing — and reject any claim that it is a ceiling or a closure" [`01c`, Q1].

**Coverage** (raised by only one perspective):

- Skeptic: a **pre-committed dissent log** — "after synthesis the operator writes what they expected the synthesis to conclude *before reading it*, committed as a separate file with a hash pinning the order. This does not add a non-Claude participant; it just exposes whether the operator's priors and the synthesis align suspiciously often. It is a measurement tool, not a participation mechanism, but it belongs in the same patch" [`01c`, Q1].
- Integrator: a **filesystem-and-git halt enforcement** — STATUS.md + `tools/check-human-slot.sh` guard [`01b`, Q1].

**[synth] Resolution direction.** The Archivist's brief-drop shape and the Integrator's halt-before-synthesis are complementary rather than competing — the former describes *what is committed*, the latter *when deliberation pauses*. The Skeptic's distinction between "perspective" and "reviewer" is a genuine design question: is the human a sixth voice arguing a stance, or a named auditor reading the Claude outputs? These are different roles and may both be legitimate. The synthesis direction is: adopt the brief-drop commit pattern (Archivist), adopt the halt-before-synthesis enforcement (Integrator), and permit both human-as-participant and human-as-reviewer as valid instances of the mechanism, each with distinct provenance markers. The pre-committed dissent log is an orthogonal measurement idea that can be adopted or deferred independently.

---

## Q2: Is Opus+Sonnet+Haiku meaningful cross-model?

**Total convergence.** All three perspectives answer the same question the same way: **training-distribution theatre, neither closure nor narrowing on the OI-004 scale**.

- Archivist: "**training-distribution theatre for the purpose of OI-004, but operationally useful for other reasons**. It falls at 'neither' on the OI-004 scale — not closure, not narrowing" [`01a`, Q2].
- Integrator: "**Training-distribution theatre, with a small caveat.** Place on the OI-004 scale: **neither closure nor narrowing**" [`01b`, Q2].
- Skeptic: "**Training-distribution theatre.** Not narrowing. Not closure. Not even on the OI-004 scale" [`01c`, Q2].

The Skeptic's sharpest formulation: "size-mixing is **worse than** running three Opus instances, because it creates the visual appearance of diversity (three different model names in the provenance!) while providing none of its substance. A future auditor reading the provenance and seeing 'Opus, Sonnet, Haiku deliberated' may credit the session with cross-model participation it did not perform. That is an honesty failure the methodology cannot afford" [`01c`, Q2].

**Convergence on a residual utility.** All three concede size-mixing may be useful for reasons unrelated to OI-004:
- Archivist: "capability stratification, cost-scaled deliberation, adversarial role assignment where the adversary is a different size" [`01a`, Q2].
- Integrator: "a **resolution** benefit, not an **independence** benefit" [`01b`, Q2].
- Skeptic concedes "size-mixing may surface capability-dependent errors ... a **validation** benefit, not an **independence** benefit. I concede the former; I reject the latter" [`01c`, Q2].

**Coverage.** Archivist uniquely proposes tracking intra-family size-mixing as its own open issue: "perhaps as a separate open issue OI-011 ('intra-family model mixing as a deliberation-quality lever, distinct from cross-model independence')" [`01a`, Q2].

**[synth] Resolution direction.** The convergence is strong enough to commit to a specification rule: **a deliberation using only Claude-family models must not record or claim any OI-004 progress**, regardless of the specific mix of Opus/Sonnet/Haiku. An `intra_family_variation` or `participants_family` field may record the mix for other purposes. Opening OI-011 to track size-mixing as a distinct deliberation-quality lever is worth adopting.

---

## Q3: Default — required, recommended, or optional?

**Convergence on structure.** All three propose a three-tier rule (required / recommended / optional) rather than a universal rule. All three place the recommendation floor for most D-016-triggered deliberations at "recommended with opt-out."

**Divergence on the required-trigger scope.**

- Archivist (broadest required): required for kernel changes; for changes to `multi-agent-deliberation.md`; for changes to `validation-approach.md` when validation involves semantic judgment [`01a`, Q3]. Recommended for new specifications and load-bearing D-016 decisions; optional otherwise.
- Integrator (narrowest required): required only when "the deliberation concerns the multi-agent deliberation mechanism itself, OI-004, or the non-Claude participation mechanism" [`01b`, Q3]. Recommended for any other D-016 trigger; optional otherwise. Justification for narrowness: "Making non-Claude participation required for all D-016 triggers would either (a) block routine deliberations on human availability, which is operationally fragile, or (b) pressure sessions to use a low-signal non-Claude channel just to check the box, which corrupts the mechanism" [`01b`, Q3].
- Skeptic (required with enforcement teeth): required when a decision is "**load-bearing claim about the methodology's own epistemic floor** — e.g., kernel changes that touch how truth is established, changes to `multi-agent-deliberation.md` itself, changes to `validation-approach.md`, and any decision that narrows or closes OI-004. A methodology cannot honestly assess its own monoculture limit using only its monoculture" [`01c`, Q3]. The Skeptic adds a sharp enforcement demand: "**'required' must mean the session does not proceed without it.** ... The opt-out must include a `retry_in_session` field naming the session where the missing participation will be added. ... 'We couldn't find a human in time' is an acceptable recorded reason; 'we didn't try' is not" [`01c`, Q3].

**[synth] Intersection.** Archivist and Skeptic propose nearly-identical required triggers (kernel + `multi-agent-deliberation.md` + `validation-approach.md` + OI-004). Integrator is narrower but his triggers are a *subset* of theirs. Adopting the broader Archivist/Skeptic scope does not reject the Integrator's rationale — it extends the required zone to include all meta-deliberations about the methodology's self-assessment mechanisms (validation, multi-agent, and OI-004 itself), but still excludes routine kernel-unrelated spec work (which becomes recommended).

**Preserved dissent — enforcement.** The Skeptic's "required must mean the session does not proceed without it; retry_in_session named on opt-out" is not contradicted by the other two, but the Integrator explicitly warns that a hard halt without opt-out is fragile. These resolve if we adopt Skeptic's retry_in_session field together with Integrator's opt-out mechanism — i.e., opt-out is permitted, must be named, must be reasoned, and must name the session where the missing participation will be secured.

---

## Q4: How to record heterogeneous-participant identity

**Convergence on required fields.** All three propose: participant kind/type, model identity, version, timestamps, an identity-known/unknown marker, and a rule that **unknown fields are recorded as the literal value `unknown`, never omitted**.

- Archivist: "the literal string `'unknown'` is required, never blank, never omitted. A missing field is a schema violation caught by `validate.sh`. `'unknown'` is a signal that says 'this session could not determine the value', which is itself auditable" [`01a`, Q4].
- Integrator: "`model`, `model_family`, `operator` must be either a specific string or the literal `unknown`. Empty strings are forbidden; `null` means 'not applicable to this kind'" [`01b`, Q4].
- Skeptic: "When fields are unknown, the literal value `unknown` is recorded — never omitted, never guessed. `training_lineage_overlap_with_claude: unknown` is a valid, auditable answer; a missing field is not" [`01c`, Q4].

**Divergence on where metadata lives.**

- Archivist: strong separation — minimal raw-output frontmatter (`perspective`, `committed_at` only); detailed per-perspective `manifest.yaml` file; `participants.yaml` session index; synthesis frontmatter cites manifest files, not model IDs directly [`01a`, Q4]. Justification: "This keeps the synthesis readable at the methodology layer and pushes all archival detail into the manifest, where a future auditor expects it."
- Integrator: flatter structure — YAML list of participants in the `session.md` (or equivalent) frontmatter, one `participants.md` human-readable index [`01b`, Q4]. Simpler; fewer files.
- Skeptic: participant identity fields live in each raw-output file's frontmatter directly; `participants.md` serves as index [`01c`, Q4]. Justification: the frontmatter should make structural violations of honest claims visible — "`tools/validate.sh` should fail a session that claims OI-004 narrowing in a decision record while recording all `participant_type: claude` in its provenance" [`01c`, Q4].

**Coverage** (uniquely raised):

- Archivist: **integrity hash** — `raw_response_sha256` in manifest, validated at every `validate.sh` run; raw files are **append-only** from commit forward; corrections live in a `.correction` sidecar, never overwrite [`01a`, Q4, Q6].
- Archivist: **convener attestation field** — "`convener_attestation: 'I confirm the raw_response_file is a verbatim copy of the received response, without edits beyond UTF-8 normalization.'` Signed with convener's git identity via commit signature where available" [`01a`, Q6].
- Skeptic: **validate.sh cross-check** that fails dishonest OI-004 narrowing claims against structurally Claude-only provenance [`01c`, Q4].
- Skeptic: **`training_lineage_overlap_with_claude`** field with values `known-overlap | unknown | independent-claim` — making the disputed claim about training overlap itself auditable [`01c`, Q4].
- Skeptic: **`participant_selection_method`** with values `self | solicited-from-graph | solicited-externally | pre-registered` — to let "a non-consensual human" claim be validated structurally [`01c`, Q4].
- Integrator: **tri-valued `identity_known`** (`true | false | partial`) with notes required on `partial` [`01b`, Q4].

**[synth] Resolution direction.** The Archivist's separation between raw-output frontmatter, per-participant manifest, and synthesis frontmatter is the cleanest boundary for auditability and should be adopted. The Skeptic's `participant_selection_method` and `training_lineage_overlap_with_claude` fields address honesty-under-structural-validation and should be incorporated into the manifest schema. The Integrator's tri-valued `identity_known` is subsumable as a manifest field. Integrity hashing, append-only raw files, and convener attestation (all Archivist coverage) are worth adopting but may be a future tooling enhancement rather than day-one requirements, since `validate.sh` would need extension to enforce them.

---

## Q5: Does this session close, narrow, or not-move OI-004?

**This is the deliberation's sharpest disagreement and the synthesis preserves it as-is.**

**Majority view (2 of 3): this session narrows OI-004, conditionally or unconditionally.**

- Archivist: "sufficient for narrowing OI-004, not for closure" — **conditional**: "If Session 004 actually includes a non-Claude participant using this mechanism, OI-004 narrows materially" [`01a`, Q5]. Since Session 004 did not include a non-Claude participant (see header — all three perspectives were Claude Opus 4.7 subagents), the Archivist's condition is technically unmet for this session's own work.
- Integrator: "**Verdict: narrowing, not closure.**" — **unconditional on the spec itself**: "OI-004 narrowed from 'no mechanism exists' to 'mechanism specified, awaiting sustained use.' Closure requires demonstrated use across at least N subsequent sessions" [`01b`, Q5]. Proposes threshold N=3 sessions with genuine non-Claude participation before closure review.

**Minority view (1 of 3, Skeptic): this session narrows nothing; writing a spec is a commitment to maybe narrow later.**

- Skeptic: "**This session's mechanism is sufficient for neither closure nor narrowing.** I state this plainly because my role requires it. ... Writing a spec that says 'future sessions should do X' does not narrow OI-004; it commits to maybe narrowing it later" [`01c`, Q5].

**[synth] The disagreement, stated precisely.** The question is whether "narrowing" is a property of the specification (Integrator: yes — the gap is smaller once a mechanism is specified) or a property of execution (Skeptic: no — only actually including a non-Claude participant narrows). The Archivist's position is a conditional middle: specification narrows *if and when* execution follows. Each position is internally coherent. The methodology's choice of which to adopt is itself a decision to be made.

**Convergence on closure requirements.** All three perspectives agree closure requires:

1. Participant independence (not downstream of Anthropic training) [Archivist, Integrator, Skeptic].
2. Sustained / structural practice, not a single demonstration [Archivist, Integrator, Skeptic].
3. Recording schema that makes heterogeneity auditable [Archivist, Integrator, Skeptic].

**Coverage — Skeptic's concrete audit metric.** Skeptic proposes a **cross-lineage-influence ratio**: "count the ratio of decisions per session where the non-Claude participant's position differs from the synthesized Claude consensus and the synthesis adopts the non-Claude position. ... If, across ten future deliberations tagged as load-bearing on OI-004, the ratio is zero — the non-Claude participation was ceremonial and OI-004 has not narrowed. A non-zero ratio, ideally above 10% over a rolling ten-session window, is a minimum floor for the claim 'non-Claude participation is affecting decisions.' Lower than that, the mechanism is theatre" [`01c`, Q5]. This is the deliberation's one concrete measurement proposal and deserves to be preserved whether or not it is adopted in full.

**Coverage — Integrator's session-threshold proposal.** Integrator proposes N=3 sessions with genuine non-Claude participation on required-trigger deliberations before OI-004 can be *reviewed* for closure (not automatically closed) [`01b`, Q5].

---

## Q6: Strongest objections and their answers

Each perspective was asked to object to its own Q1 proposal. All three retained the "this is a stopgap / floor / interim" framing in their responses.

**Archivist's objection to its own proposal**: "the manifest-based brief-drop pattern outsources reproducibility to human diligence. ... The mechanism trusts a single human in the loop — the convener — to be perfectly faithful with no tooling support" [`01a`, Q6]. Archivist's answer mixes concession (cannot automate away the trust dependency) with concrete mitigations (attestation field, integrity hash, role separation, naming the trust boundary in the spec itself).

**Integrator's objection to its own proposal**: "the asynchronous halt is a liveness failure disguised as rigor. ... sessions pile up in `awaiting:` state. In practice, the methodology quietly drops the required-trigger rule after the third stalled session, and the spec becomes a fiction" [`01b`, Q6]. Answer: narrow trigger scope, 14-day timeout with explicit provenance-recorded fallback, visible STATUS.md halt.

**Skeptic's objection to its own proposal**: "it launders a single human's priors through the same collapse point the Session 003 synthesis already had. One human, selected by the operator from the operator's social graph, correlated in worldview and profession and language and training, is not independence — it is a confederate" [`01c`, Q6]. Answer: "my proposal is a stopgap, not a solution. ... I am proposing the least-bad interim and I am documenting that it is interim" [`01c`, Q6]. Explicit condition on provenance recording: "If the session records my Q1 mechanism as narrowing OI-004 — it does not. If the session records it as a floor with a pre-committed upgrade path (OI-010 stays open, a sub-issue tracks 'secure external model endpoint' as explicit prerequisite for closure), I accept the record" [`01c`, Q6].

**[synth] Takeaway.** All three perspectives agree that their proposals are **interim floors**, not ceilings. The differences are only in what counts as "floor": the spec (Integrator), the spec-with-execution (Archivist, conditionally), or not-until-actually-used (Skeptic). Regardless of position, all three require the methodology to **not** record this session as closing OI-004, and to preserve the upgrade path in an open issue.

---

## Points of Agreement (across all three perspectives)

1. **Opus+Sonnet+Haiku mixing is not cross-model participation for OI-004 purposes.** Strong triple-convergence on language ("training-distribution theatre"). A Claude-only deliberation must not claim OI-004 movement regardless of intra-family size mix.
2. **The minimum viable path is a human participant, not a non-Anthropic model API.** All three note the workspace's lack of non-Anthropic API keys and the cost of adding them.
3. **Non-Claude participation should be required for a specific self-referential subset of deliberations, recommended for the main D-016 zone, and optional otherwise.** The three-tier structure is convergent.
4. **Heterogeneous identity must be recorded; unknown fields take the literal value `unknown`; a missing field is a schema violation.** Triple-convergent.
5. **OI-004 is not closed by this session.** All three agree closure requires sustained practice and independence from Anthropic training.
6. **The proposed mechanism is an interim floor, not a ceiling.** All three explicitly frame their proposals as stopgaps.

## Points of Disagreement (preserved, not resolved)

1. **Whether this session narrows OI-004.** Integrator: yes, unconditionally (the spec narrows). Archivist: yes, conditionally on execution. **Skeptic: no — only actual use by a future session would narrow.** The Skeptic's position is the minority and is preserved as-is; the Decide step must pick a posture on the record.
2. **Where the human enters the pipeline.** Archivist: as a full perspective (brief-drop). Integrator: as a full perspective (with halt). **Skeptic: as a reviewer at synthesis-time, not as a perspective.** The Skeptic's distinction between "perspective" and "reviewer" is a genuine structural disagreement and the specification must choose one primary shape or name both.
3. **The scope of the required-trigger rule.** Archivist and Skeptic: broader (kernel + multi-agent-deliberation + validation-approach-semantic + OI-004). Integrator: narrower (only the mechanism itself). Preserved; Decide must choose.
4. **Whether to mandate hard enforcement of the required trigger.** Skeptic demands "required must mean the session does not proceed without it"; Integrator warns that unconditional halt is fragile. Resolvable by combining opt-out with required `retry_in_session` field, but the decision explicitly picks the compromise.

## Open Threads Not Resolved

- **Cross-lineage-influence ratio** (Skeptic's proposal, `01c-perspective-skeptic.md`, Q5): concrete, implementable, but measurement requires future-session data. Candidate for a future validation-tool enhancement.
- **Integrity hashing, append-only raw files, convener attestation** (Archivist's proposals, `01a-perspective-archivist.md`, Q4/Q6): valuable but require extensions to `validate.sh`. Candidate for a future session.
- **Cross-provider model convergence risk** (Integrator's "What I cannot answer", `01b-perspective-integrator.md`): whether frontier-model training distributions are themselves converging across providers, degrading even cross-provider participation over time. Not addressable in this session.
- **Pre-committed dissent log** (Skeptic's secondary proposal, `01c`, Q1): measurement tool for operator-synthesis alignment. Candidate for a future tooling addition.
- **Opening OI-011 for intra-family size-mixing as a distinct concern** (Archivist, `01a`, Q2): not an OI-004 issue, but worth tracking separately.
