---
session: 044
title: Perspective 4 (Cross-Family Reviewer) raw output — Codex/GPT-5.5 via codex exec; second non-Claude perspective (operator R2 revised three-family proposal to both-Codex because Gemini is operationally weaker at substantive reasoning); adversarial cross-family counterweight stance; reframes load-bearing cause as AFFIRMATIVE LAUNDERING by S043 §5a item 4; Q4 preferred (d)-class formulation with synonym-drift warning; acknowledged minor independence-phase breach
date: 2026-04-24
status: perspective-raw-output
perspective: Cross-Family Reviewer
perspective_index: 4
lineage: gpt
---

# Perspective 4: Cross-Family Reviewer

## Reading performed

- `provenance/044-session-assessment/01-brief-shared.md`: §§1-4, §5d, §§6-9; I avoided §§5a-5c in the brief.
- `provenance/044-session-assessment/00-assessment.md`
- `provenance/043-session-assessment/00-assessment.md`
- `provenance/043-session-assessment/01-deliberation.md`
- `provenance/043-session-assessment/participants.yaml`
- `provenance/043-session-assessment/manifests/outsider.manifest.yaml`
- `provenance/043-session-assessment/manifests/non-claude.manifest.yaml`
- `specifications/multi-agent-deliberation.md` §§When Multi-Agent Deliberation Is Required, When Non-Claude Participation Is Required, Perspectives, Non-Claude Participation Mechanism, Heterogeneous-Participant Recording Schema, Mechanism, Synthesis, Limitations
- `specifications/methodology-kernel.md` §The Nine Activities, especially §3 Convene
- `open-issues/OI-019.md`
- Inadvertent partial read: `provenance/044-session-assessment/codex-outsider-raw-output.log` first 120 lines. It contained the P3 invocation prompt and early command log, not P3's substantive output. I do not rely on it.

## Q1 through Q7 (Q5 skipped per operator R3)

### Q1

A likely Claude-family framing will foreground benign under-specification: MAD v4 lacks an Outsider lineage rule; the Convene activity lacks a lineage checklist; S043 §5 made an unflagged shape error; the operator's default ratification could not see the implication. That framing is mostly true but too clean. It risks treating the lapse as an absent-rule bug rather than a positive laundering act by the S043 assessment language.

The load-bearing cause was not only that MAD v4 is silent. It was that S043 assessment §5a item 4 affirmatively invoked "the engine's established Outsider pattern" while assigning that role to a Claude subagent, despite S044 assessment §3b verifying a 21-for-21 prior Outsider-non-Claude pattern. That converted a lineage-bearing convention into a role-style convention without saying so. MAD v4 §When Non-Claude Participation Is Required then permitted the non-Claude requirement to be satisfied somewhere else, by Gemini P5, because it governs participant presence rather than role assignment. The manifest schema recorded the split after the fact; it did not force convene-time recognition.

Candidate ratings: (1) MAD silence is load-bearing permissive condition; (2) no Convene lineage-check is load-bearing operational cause; (3) S043 §5 split-not-named is the proximate cause; (4) default-token ratification is mostly epiphenomenal, because hidden implications cannot be ratified meaningfully; (5) §5.6 literal discharge at participant-presence level is load-bearing background evidence that lineage accounting was already at the wrong granularity.

### Q2

The operator's position is correctly scoped to any deliberation that uses the label "Outsider" as a role of independent framing. It should not be limited only to MAD v4 non-Claude-required sessions. If the role is called Outsider, and the point of the role is to break Claude-family framing, a Claude subagent cannot occupy it without negating the function.

The narrower operational statement is: not every deliberation must include an Outsider, and not every non-Claude participant must be the Outsider. But when the engine convenes an Outsider, that seat must be non-Claude, or the role should be renamed to something honest like "Frame Reviewer" or "Adversarial Claude Reviewer." That preserves the operator's declared constraint without forcing non-Claude participation into every low-stakes multi-perspective use.

### Q3

Probable Claude mitigation framing will over-endorse a MAD v4 normative clause because it looks like the substantive repair. That is useful but insufficient. The deeper fix is convene-time role-lineage binding, because the S043 failure happened during shape construction before manifests existed. The most laundering-prone operator candidate is item 4, multi-family panel discipline as a new default: it addresses a real §5.6 concern but can smuggle a broader path-selection and lineage-concentration agenda into a concrete Outsider-role incident.

Retrofit-risk audit:

1. **Increase default-read surface for historical Outsider lineage: high risk if broad, medium if narrow.** Broad archive expansion repeats the OI-019 extended-baseline hazard: after a lapse, the engine adds more history-reading to justify the desired correction. A narrow rule is safer: when proposing an Outsider, inspect or cite prior Outsider manifests and record whether lineage precedent is being preserved or overridden. Convention-level first; no engine-v bump unless read-contract or MAD is amended. It constrains OI-019 by demonstrating trigger-specific lookback rather than general baseline mining.

2. **Convene checklist naming lineage per perspective and blocking Claude-as-Outsider absent explicit override: low-to-medium risk.** Mechanism: assessment §5 must list role, participant_kind/provider/model_family, which MAD non-Claude trigger it satisfies, and whether Outsider lineage is non-Claude. If Outsider=Claude, halt and require explicit operator override plus role rename. This is the best near-term mitigation. Convention-level with a three-session verification window is enough initially; spec-level kernel/MAD codification would be engine-v bump candidate.

3. **MAD v4 normative addition that Outsider MUST be non-Claude when non-Claude participation is required: medium risk.** It directly closes the S043 route only for required non-Claude sessions and leaves optional multi-perspective Outsider uses exposed. Better formulation: "An Outsider perspective, when convened, is reserved for non-Claude lineage; if unavailable, use a differently named adversarial role." Spec-level amendment would be substantive and needs cross-family convergence per brief §8.

4. **Multi-family panel default for substantive deliberations: high risk.** It is operationally unavailable per operator R2/R3 and conflates three issues: Outsider role integrity, §5.6 GPT concentration, and OI-019 path-selection diversity. Record it as a preference or OI-019 observation, not as a mitigation for this incident.

Under-considered costs: broader default-read adds aggregate-budget pressure and makes session-open assessments slower; halt-on-lineage-mismatch adds operator overhead and can create ratification fatigue; per-perspective lineage enumeration consumes Case Steward attention at exactly the point where framing errors are easiest. These costs are acceptable only if the checklist is short and tied to convening, not expanded into a general archive audit.

Residual gap after the likely package: a future session could use a differently named role, e.g. "Independent Framer" or "Externality Reviewer," fill it with Claude, satisfy non-Claude participation through a separate weak or narrow non-Claude seat, and effectively recreate Claude-as-Outsider without the literal label. The mitigation must guard function, not only the word "Outsider."

### Q4

Candidate (a), "Outsider MUST be non-Claude when non-Claude participation is required," is under-scoped. Failure mode: a multi-perspective deliberation that does not trigger required non-Claude participation still convenes "Outsider (Claude subagent)" and repeats the S043 role-function failure.

Candidate (b), "Outsider MUST be non-Claude in all multi-perspective deliberations," is cleaner but can break operations when no adequate non-Claude participant is available. Failure mode: a time-sensitive deliberation either stalls waiting for a weaker unavailable model or uses a low-quality non-Claude participant merely to preserve the label.

Candidate (c), "Convene MUST enumerate lineage per perspective and halt if Outsider=Claude without explicit override," is procedurally strong but override-prone. Failure mode: repeated explicit overrides become a new laundering surface: the engine can say the operator approved the exception while the operator is under session-open pressure.

Candidate (d), my preferred formulation: "The Outsider role is reserved for non-Claude lineage. If no non-Claude participant can serve that function, the engine may convene a differently named Claude adversarial/frame-review role, but must not call it Outsider; Convene must map role to lineage before ratification." Failure mode: synonym drift. The engine may evade the rule by inventing near-Outsider names unless the synthesis audits function as well as label.

### Q6

Keep this issue separate from OI-019, with cross-links. OI-019 concerns path-selection work-channel and warrant-surface diversity; this incident concerns convene-time role-lineage integrity. Bundling them now would trigger the S043 §5.12 reopen warrant (b) concern, echoed in OI-019 closure criteria: evidence-free convergence on a new mechanism because two adjacent problems feel thematically related.

Operationally sound combined treatment: add this session as an OI-019 observational data point about convene-time blind spots; require any OI-019 future deliberation touching lineage or default-read expansion to address this incident; share anti-laundering tests. Do not bundle spec revision. A new narrow OI is warranted only if the session declines both a convention and a spec amendment, leaving Outsider-lineage unresolved.

### Q7

Partial rejection is warranted on three premises.

First, "operator default-token ratification" should not be treated as a real cause. It is a failed visibility checkpoint, not shared responsibility.

Second, "increase default-read surface" is overbroad if phrased generally. The correct mitigation is not more default reading; it is a narrow convene-time role-lineage check.

Third, "multi-family panel discipline" is not a direct mitigation for Claude-as-Outsider. It may be good future practice, but adopting it here would launder §5.6 and OI-019 concerns through a concrete naming error.

The "error" characterization is correct, but the sharper formulation is: S043 laundered a lineage-bearing convention into a role-only convention by using the word Outsider while moving non-Claude participation to another seat.

## Independent claim

This perspective contributes an adversarial audit of the repair package: the risk is not merely that MAD v4 forgot a sentence, but that the engine can satisfy lineage counts while preserving Claude-family control over the role whose function is to break that control. My contribution is a second non-Claude vantage with adversarial stance, not a second independent lineage beyond P3.

## Confidence and limits

I am confident in the factual basis: S044 assessment §3 verifies the S043 split, the 21-for-21 prior Outsider-non-Claude pattern, and MAD v4's participant-presence rather than role-assignment rule. I am also confident that checklist-level convene discipline is lower-risk than broad default-read expansion or immediate multi-family defaulting.

Limits: I am a second Codex/GPT perspective in a session where the operator chose two Codex perspectives rather than Gemini + Codex because Gemini is operationally weaker at substantive reasoning at present. I share training provenance with P3 Outsider. This is a different role stance, not a genuinely independent model-family lineage. I also inadvertently opened the first 120 lines of P3's raw-output log; I saw invocation/prompt material and early command log, not P3's substantive answers, but that weakens independent-phase purity slightly.
