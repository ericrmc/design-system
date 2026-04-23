---
session: 044
perspective: Outsider
perspective_index: 3
lineage: gpt
---

# Perspective 3: Outsider

## Reading performed

- `provenance/044-session-assessment/01-brief-shared.md` §§1-4, §5c, §§6-9 only. I did not read §§5a/5b/5d.
- `provenance/044-session-assessment/00-assessment.md` §§2-3.
- `provenance/043-session-assessment/00-assessment.md` §§5-6.
- `provenance/043-session-assessment/01-deliberation.md` §§1-7.
- `provenance/043-session-assessment/participants.yaml`.
- `provenance/043-session-assessment/manifests/outsider.manifest.yaml`.
- `provenance/043-session-assessment/manifests/non-claude.manifest.yaml`.
- `specifications/multi-agent-deliberation.md` §§When Multi-Agent Deliberation Is Required, When Non-Claude Participation Is Required, Perspectives, Stance Briefs, Non-Claude Participation Mechanism, Heterogeneous-Participant Recording Schema, Synthesis, Limitations.
- `specifications/methodology-kernel.md` §Convene.
- `open-issues/OI-019.md`.

## Q1 through Q7 (Q5 skipped per operator R3)

### Q1

The S043 split happened because the engine treated "Outsider" as a stance label and "non-Claude" as a participant-presence property, while the historical practice had made them the same operational object.

Candidate (1), no MAD v4 normative requirement, is load-bearing. S044 assessment §3c verifies that MAD v4 requires non-Claude participation for certain decision categories but does not constrain which role that participant fills. MAD v4 §Perspectives likewise governs number, disagreement, adversarial stance, and naming, not lineage.

Candidate (2), no Convene lineage check, is also load-bearing. Methodology Kernel §Convene says to assemble perspectives, name each stance, and record why chosen, but says nothing about recording provider/model family against role-function. That makes the S043 shape formally legible while functionally hiding the break.

Candidate (3), S043 assessment §5 splitting the historically fused roles without naming the split, is the proximate cause. S043 §5a item 4 called Outsider a Claude subagent "per the engine's established Outsider pattern"; item 5 separately assigned Gemini the non-Claude lineage. S044 §3d correctly identifies the problem: it cited the role pattern while omitting the 21-for-21 lineage component.

Candidate (4), default-token ratification, is contributory but not root. The operator ratified a shape whose implication was not surfaced. That is an interface failure in convening records, not a substantive operator endorsement of the split.

Candidate (5), §5.6 literal discharge on participant-presence grounds, is partly load-bearing and partly symptomatic. Strictly, S043 §5.6 asked whether non-GPT non-Claude participation occurred, and Gemini satisfied that. But S044 §3e is right that the warrant operated at participant-presence level while the latent concern presumed role/lineage continuity.

Additional cause: MAD v4 Shape A says a non-Claude participant may be a perspective "indistinguishable in role from the Claude perspectives." That phrasing is useful generally, but here it encouraged role fungibility. It made "add a non-Claude perspective" look equivalent to "preserve the Outsider function." It was not.

### Q2

The operator's position is correctly scoped to every deliberation where the engine uses the role name "Outsider." It need not imply that every multi-perspective deliberation must include an Outsider, or that every low-stakes deliberation must become cross-family. But once the engine invokes "Outsider" as a role, non-Claude lineage is part of the role's function, not an optional transport detail.

The narrow trigger-based scope - "Outsider must be non-Claude only when MAD v4 independently requires non-Claude participation" - is too weak. It would still allow a Claude Outsider in optional non-Claude cases, preserving the same false role signal.

The broader but cleaner scope is: in a Claude-hosted workspace, a perspective named Outsider cannot be Claude-family. If no non-Claude participant is available, the engine may convene an "Internal Frame Challenger" or "Adversarial Reviewer," but should not call it Outsider. For required non-Claude-trigger decisions, the Outsider seat should normally satisfy the non-Claude requirement unless the convening record explicitly justifies assigning the non-Claude participant to another lineage-sensitive function.

### Q3

Mitigation 1, increased default-read surface, helps but is insufficient. Mechanism: session-open assessment should include a small role/lineage precedent note whenever it cites an "established pattern"; for Outsider, it should surface the 21-for-21 prior non-Claude assignment verified in S044 §3b. Risk: precedent can be laundered into rule without deliberation. Codification should start as convention with a verification window, not immediate spec text. OI-019 interaction: positive but narrow; it increases visible warrant surface without deciding OI-019.

Mitigation 2, Convene checklist, is the strongest immediate control. Mechanism: add a convene-time role/participant matrix to the assessment shape: perspective, role function, participant kind, provider/model family, which MAD v4 trigger it satisfies, and any lineage constraint. It should halt if Outsider = Claude unless an explicit operator override states that the role is degraded and not counted as a true Outsider. This can begin as convention; if successful, it belongs in Methodology Kernel §Convene or MAD v4. Spec-level adoption is an engine-v bump candidate.

Mitigation 3, MAD v4 normative addition, is warranted. The rule should not only say "when non-Claude participation is required"; it should say that Outsider is a lineage-constrained role. Risk: overfitting to one label while leaving other role/lineage dependencies invisible. Pair it with the matrix.

Mitigation 4, multi-family panel as default, should be rejected for now as an operational default. The brief §7 separates the Outsider question from the three-family-panel question, and §9 records that this session's GPT-only non-Claude availability is an operator-informed tradeoff. Multi-family panels are valuable data points for OI-019 and §5.6, not a present standing requirement.

Claude-family perspectives are likely to miss: that stance-brief independence does not equal lineage independence; that "spec silent" is not "function preserved"; that operator ratification is weak when the implication is unmarked; and that bundling this with OI-019 is neat but may dilute both problems.

### Q4

Candidate (a), "Outsider MUST be non-Claude when non-Claude participation is required," is a good floor but wrongly scoped. It fixes the exact S043 required-trigger case but leaves the role name available for Claude in optional cases.

Candidate (b), "Outsider MUST be non-Claude in all multi-perspective deliberations," is closer, provided it means "whenever an Outsider role is used," not "every deliberation must include non-Claude." If non-Claude is unavailable, do not use the role name.

Candidate (c), "Convene MUST enumerate lineage per perspective and halt if Outsider = Claude without explicit override," is necessary but not sufficient. It prevents invisible recurrence, but an override can become boilerplate unless it requires a reasoned statement that the Outsider function is not being fully instantiated.

Preferred formulation: MAD v4 should define Outsider as a lineage-constrained role in Claude-hosted deliberations: a perspective named Outsider must be non-Claude; if unavailable, the convening record must either defer, rename the role to an internal challenger, or record an explicit operator override. Separately, Convene should require the role/lineage matrix for all MAD deliberations.

### Q6

OI-019 and the S044 issue should be linked but not bundled into one closure path.

The overlap is real: both concern what the engine sees at convene/session-open time, and both involve a hidden mismatch between formal compliance and functional discipline. OI-019 asks whether path-selection work channels and warrant surfaces are too narrow; this session asks whether perspective roles with lineage-dependent functions are being preserved.

Bundled spec revision would be a mistake. OI-019 explicitly requires operational evidence, cross-family convergence on a specific mechanism, and engagement with the §5.12 Path-Selection Defender minority. Its Honest note warns against rapid closure with spec change. This issue has enough evidence now for a targeted MAD/Convene fix; forcing it through OI-019 would either slow a direct safety correction or launder OI-019 forward prematurely.

Operational recommendation: create a cross-link and shared checklist surface, not a joint OI closure. The Convene role/lineage matrix can serve both: here it blocks Outsider-role misuse; for OI-019 it may later expose whether path-selection alternatives and warrant inputs were genuinely considered.

### Q7

Partial rejection is warranted only against the narrow "one-time error" framing. Under the operator's declared position, S043 was an error. But the more accurate formulation is: S043 exposed a spec/convention asymmetry in which a functionally lineage-dependent role was preserved by name while its lineage basis was silently severed.

Several candidate causes should be narrowed. Default-token ratification did not cause the split; it failed to catch an unmarked implication. §5.6 discharge did not directly require the Outsider role to be non-Claude; it revealed the participant-presence vs role-assignment confusion. Mitigation 1 alone addresses visibility but not enforceability. Mitigation 4 addresses cross-family concentration but not the specific Outsider-role failure.

The residual gap after adopting a default-read note, Convene checklist, and MAD v4 Outsider rule is broader role/lineage discipline. The engine still needs to ask, for each named perspective: does this role depend on structural position, training lineage, operator relation, or synthesis timing? MAD v4 §Limitations already says Claude subagents share family blind spots and that brief-writing has no adversary. A non-Claude Outsider helps, but it does not fix Claude-authored framing, Claude synthesis re-entry, or future cases where a different role has an unstated lineage dependency.

## Independent claim

The missing concept is not simply "non-Claude participation"; it is role-function integrity. A role whose purpose is to stand outside the Claude workspace cannot be instantiated by a Claude subagent, even with a perfect stance brief, because the structural relation is part of the role.

## Confidence and limits

High confidence: S043 formally split Outsider role from non-Claude lineage; MAD v4 did not prohibit it; Convene lacks a lineage check; a targeted Outsider-lineage clause plus convene-time matrix is warranted.

Lower confidence: exact spec wording and engine-v classification should be decided after synthesis across all four perspectives. The requested root path `manifests/non-claude.manifest.yaml` was not present; I read the S043 `provenance/.../manifests/non-claude.manifest.yaml` instead.
tokens used
