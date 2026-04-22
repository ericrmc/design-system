---
session: 027
title: Deliberation — Folder-naming discipline
date: 2026-04-23
status: complete
synthesizer: session-027-orchestrating-agent (Claude Opus 4.7 1M; not a deliberating perspective)
participants_family: claude-only
cross_model: false
non_claude_participants: 0
oi004_qualifying_participants: []
---

# Deliberation — Folder-Naming Discipline (Session 027)

## §1 Summary and perspectives convened

Three perspectives were convened as independent Claude subagents via the Agent tool. Each received a byte-identical shared brief (`01-brief-shared.md` §§1-3, 5-6) and a role-specific §4 stance. Independence-preservation was realised by parallel Agent launches in isolated contexts; no perspective saw any sibling's output before committing its response.

- **Archivist** [01a-perspective-archivist.md]: load-bearing concern is D-017 immutability and OI-007 scaling pressure. Argues against formalisation and against retroactive rename. Advisory note in prompts/development.md acceptable as lightest option.
- **Discoverer** [01b-perspective-discoverer.md]: load-bearing concern is discoverability as a compounding property. Argues for formalised close-step rename in workspace-structure.md (substantive; engine-v5) plus scoped retroactive dispensation for Sessions 023-026.
- **Minimalist** [01c-perspective-minimalist.md]: load-bearing concern is cumulative surface accretion (OI-007). Argues against formalisation and against retroactive rename, but proposes changing the opening default from `NNN-session-assessment` to `NNN-session` as a minor revision to workspace-structure.md §provenance.

Presentation order in this synthesis is alphabetical by role name per `multi-agent-deliberation.md` v4 §Synthesis (Synthesis order anchoring).

## §2 Question-by-question synthesis

### Q1 — Should the engine formalise a folder-naming discipline?

**2-of-3 against formalisation** (Archivist, Minimalist). **1-of-3 for** (Discoverer).

- **Archivist** [01a-perspective-archivist.md, Q1]: "Do not formalise. If something must be done, make it a single sentence in prompts/development.md under 'How to operate' — and make it advisory, not a spec clause." Argues that "what failed is a cosmetic labelling convention that was never specified in the first place. Calling this a 'drift' elevates it to spec status."
- **Minimalist** [01c-perspective-minimalist.md, Q1]: "Standardise on the opening-default form as the permanent name. Specify in workspace-structure.md that provenance folders are `NNN-session` (or `NNN-session-NNN` if we want redundant stability)." Reframes the observation as "evidence that a convention which was already fraying before Session 023 ... stopped being performed once the SESSION-LOG thin-index absorbed the function the folder name was serving."
- **Discoverer** [01b-perspective-discoverer.md, Q1]: "Formalise the discipline... At session close, if the session produced any substantive output... then the folder MUST be renamed from the `NNN-session-assessment` default to a descriptive slug reflecting the session's load-bearing content." Argues folder names are load-bearing for discoverability.

**Convergence**: all three perspectives agree that the pre-Session-023 practice was informal, not specified. They disagree on whether informality is a repair target (Discoverer) or the correct state given SESSION-LOG's authoritative role (Archivist, Minimalist).

**Coverage-only**: Minimalist raises the specific argument that SESSION-LOG.md's R8a thin-index adoption at Session 022 (the pre-R8a SESSION-LOG content is preserved as an archive-pack at `provenance/022-workspace-scaling-trajectory/archive/pre-R8a-SESSION-LOG/` and cited in the Session 022 close) superseded the folder-name-as-thin-index function. Archivist does not directly address this; Discoverer does not directly address this. [synth: the Minimalist framing is the cleanest explanation for why the rename practice drifted — it was serving a function that SESSION-LOG now serves, so attention leaked off it.]

### Q2 — When and who for folder-name choice/revision?

All three perspectives converge on: **current session only; never after close**. Divergence is on whether a rename should happen at close at all.

- **Archivist** [01a, Q2]: "The only safe answer is: at open or during-session, never after close... Current-session authority only."
- **Discoverer** [01b, Q2]: "At session close, as part of the Close activity... The current session, as the final step of Close... Specifically: after the close-log is drafted and decision records are written, before the commit... The rename is part of the same commit that records the close."
- **Minimalist** [01c, Q2]: "The folder name is chosen at open, matches a deterministic template... and is never revised... If forced to pick [a formalised rule variant]: current-session-at-close, with explicit written permission in workspace-structure.md, and no retroactive-rename authority ever granted to subsequent sessions."

**3-of-3 convergence on D-017 interpretation for post-close state**: no perspective supports post-close mutation under any framing. Discoverer's argument that "D-017 is about content, not address" is an argument for a specific dispensation being narrow, not an argument for blanket authority; Discoverer still confines rename authority to the session that flags the drift (Session 027 for the retroactive proposal).

### Q3 — Retroactive rename for Sessions 023/024/025/026?

**2-of-3 against retroactive rename** (Archivist, Minimalist). **1-of-3 for** (Discoverer, with conditions).

- **Archivist** [01a, Q3]: "Do not rename. And I want to be specific about why each of the three options the brief enumerates is worse than inaction." Dissects all three options (leave stale; edit references; narrow dispensation) and argues the "path-string only" boundary is "a lexical distinction, not a semantic one. Semantically, any edit inside a closed-session file is a post-hoc edit."
- **Minimalist** [01c, Q3]: "No retroactive rename... The four folders are historical witnesses to the drift. That is not a cost — that is a feature." Adds: "Retroactive renaming produces a workspace where the file tree says one thing, the commit messages say another, and the closed-session files either say the old thing (option a) or were illegally edited (option b/c)."
- **Discoverer** [01b, Q3]: "Yes for 023 and 024. Yes, probably, for 025 and 026 — for symmetry and clarity." Proposes a specific, scoped dispensation (verbatim at [01b-perspective-discoverer.md, Q3 block]):
  - Permitted edits: (1) `git mv` of folder; (2) path-string updates in four enumerated categories *inside the renamed folder*; (3) path-string updates in SESSION-LOG.md and active specs.
  - Forbidden edits: any mutation of decision-record content; deliberation content; commit messages; files outside the enumeration.
  - Auditable via `grep -r "023-session-assessment"` returning zero matches except this decision record and git log.

**Key substantive disagreement** — whether "path-string only" is a safe boundary:

- **Archivist position** [01a, Q3]: the boundary is lexical not semantic; "a path-string inside a narrative sentence is content. 'We executed Path A at `provenance/025-session-assessment/...`' contains a path-string; the sentence is a narrative claim about the session's trajectory; editing the path-string edits the sentence."
- **Discoverer position** [01b, Q3]: the enumeration closes the door; "path strings inside content that are self-references are tracking metadata, not reasoning or conclusions; updating them to match the new address is a coherence repair, not a content mutation."

Neither perspective's argument fully reduces the other's. [synth: the operator's call on whether the boundary is safe is the adjudicating move; this synthesis cannot resolve it on argument alone.]

### Q4 — Should the opening default name change?

**Split 1-1-1** (not a majority direction):

- **Archivist** [01a, Q4]: No strong opinion, leaning no. "`session-assessment` is not meaningless — it literally describes activity 2 of the 9 (Assess), and every session does open with an assessment phase. The placeholder is semantically grounded in the methodology."
- **Discoverer** [01b, Q4]: Leans keep current default, but **conditional**: "The current default is a useful placeholder *conditional on a reliable rename mechanism*. Without the mechanism, it is a design bug." If the rename mechanism is not adopted, Discoverer's position flips to wanting a more-obvious-placeholder (e.g., `NNN-pending-title`).
- **Minimalist** [01c, Q4]: Change default to `NNN-session` (no tail). "The bug: `session-assessment` is a session-shape classification. It implies every session is an 'assessment' session, which is false." Rejects editorial-judgment options because they "require per-session authorship, which is exactly the close-step obligation I am trying to remove."

**Asymmetric positions**: Archivist is "no change" regardless; Minimalist is "change to NNN-session" regardless; Discoverer's position is contingent on Q1. If the Q1 deliberation lands against formalisation (as 2-of-3 does), Discoverer's contingent position effectively migrates toward Minimalist's "change the default to be less misleading" — both agree the placeholder becomes a misnomer without a rename mechanism.

[synth: if the Decide step adopts the 2-of-3 no-formalisation position, the downstream implication is either Archivist's "keep default" (because the placeholder is semantically grounded in Assess) or Minimalist's "change to NNN-session" (because the placeholder misleads once no rename is coming). The operator's call.]

### Q5 — Where should the rule live?

**Conditional on Q1 outcome.**

If no rule is adopted (majority position): no location question arises, or at most a single advisory sentence in `prompts/development.md` (Archivist) or a minor revision to `workspace-structure.md` §provenance (Minimalist, for the default-permanent rule).

If Discoverer's rule is adopted: "Primary location: `workspace-structure.md` §provenance... Secondary location: `prompts/development.md` §How to operate" [01b, Q5]. Substantive per OI-002 heuristic; engine-v5 bump.

All three perspectives **converge on avoiding a new OI, a new spec file, and a new validator check** for folder-naming. The convergence is explicit in Archivist [01a, Q5]: "A 'does this name reflect the content' check is aesthetic — it cannot be mechanised without either (a) a heuristic that will produce false positives and negatives, or (b) a human judgement call dressed in a checklist." Minimalist [01c, Q5]: "Adding a spec file for a folder-naming rule is the most expensive possible placement for the smallest possible rule." Discoverer [01b, Q5] scopes the rule to workspace-structure.md + prompts/development.md only; does not propose validator or OI.

### Q6 — Is this class of drift governable by the proposed mechanism?

**3-of-3 convergence**: single-session self-audits cannot catch this class of cross-sectional drift. The operator's external observation is the mechanism that detected the drift.

- **Archivist** [01a, Q6]: "The remedy — and I offer this tentatively — is a periodic audit whose prompt is not 'does X hold?' but 'what has drifted?' That is an open-ended audit, an audit without a target. It is what the operator just performed at Session 027 open."
- **Discoverer** [01b, Q6]: "The engine needs a distinct audit altitude: an **index audit** that periodically examines the workspace as a listing, without opening individual files."
- **Minimalist** [01c, Q6]: "The operator is the correct mechanism for this class of drift. External observation by someone who sees the workspace as a whole, not through the lens of a single session's scope, is the detection mechanism that actually worked here."

**This is the strongest convergence of the deliberation.** All three perspectives, reasoning independently, arrive at the same methodology-level observation: audits scoped to content cannot see drift in the index that contains the content. The detection mechanism that worked was operator attention applied to the workspace as a whole.

**Divergence within the convergence**:
- Archivist and Minimalist frame the finding as "do not replace the external-attention mechanism with a narrower mechanism" — i.e., accept that operator observation is the layer.
- Discoverer frames it as "a new audit altitude could supplement external attention" — i.e., propose index-audit as a future session's agenda, not as Session 027's output.

All three agree Session 027 should not propose the index-audit mechanism as a concrete spec. Discoverer explicitly defers: "I do not want to propose the full audit mechanism in this session. The immediate task is to fix the folder-name drift and specify the discipline. The audit mechanism is a follow-on" [01b, Q6].

## §3 Convergences

1. **Q6 — cross-sectional drift is not governable by single-session self-audit.** 3-of-3. Operator observation (or an equivalent external mechanism) is load-bearing for this class of drift. Recording this as the deliberation's load-bearing methodology finding is appropriate; the specific folder-name question is downstream of it.
2. **Q2 — post-close rename authority should be current-session or never.** 3-of-3. Any retroactive mechanism requires explicit dispensation; no perspective supports ad-hoc post-close editing.
3. **Q5 — no validator check, no new OI, no new spec file.** 3-of-3. Whatever rule (if any) is adopted lives in an existing spec or prompt file.
4. **OI-007 scaling pressure is load-bearing for the decision.** Archivist [01a, Q1, Q5, Q6] and Minimalist [01c, Q1, Q5] cite it explicitly; Discoverer [01b, Q1] scopes his proposal to avoid OI-controllable surface (no new OI, no validator check). All three are paying the same discipline.

## §4 Divergences preserved

### Majority: against formalisation and against retroactive rename

2-of-3 (Archivist, Minimalist) on both Q1 (do not formalise) and Q3 (do not rename retroactively). The two perspectives have different downstream recommendations: Archivist prefers a single advisory sentence in prompts/development.md; Minimalist prefers a minor revision to workspace-structure.md §provenance standardising on `NNN-session` as the permanent default. These are compatible — both can be adopted — though neither insists on both.

### Minority §A: Discoverer — close-step rename plus scoped retroactive dispensation

Full position preserved at [01b-perspective-discoverer.md, Q1-Q5]. Key elements:

- **Close-step rename rule** in `workspace-structure.md` §provenance, cross-referenced from `prompts/development.md`. Substantive per OI-002 → engine-v5 bump.
- **Retroactive dispensation** for Sessions 023/024 (+ 025/026 for symmetry) with closed enumerations of permitted and forbidden edits.
- **Activation warrant** (for preservation as minority, per multi-agent-deliberation.md §Minorities): if future workspace reorganisation (e.g., a new workspace-structure spec revision) requires path-string updates inside closed-session folders and the adopted rule does not authorise it, the Discoverer dispensation shape is the preferred template for that future dispensation. The scoped-enumeration approach is preserved as the recommended form for any future D-017 narrow dispensation, whether or not Session 027 adopts one.

### Minority §B: Minimalist — change opening default to `NNN-session`

Full position preserved at [01c-perspective-minimalist.md, Q4]. Key claim: `session-assessment` is a session-shape classification ("assessment" is one of the nine activities), which implies every session is an assessment, which is false for many session shapes (Path A execution; planned deliberation; domain artefact production).

- **Activation warrant**: if a future session observes confusion caused by the `session-assessment` default name (a future Claude or operator misinterpreting the folder name as a claim about session content), the Minimalist position becomes the preferred revision direction: `NNN-session` (semantically empty) or `NNN-session-NNN` (redundant but stable).

### Minority §C: Archivist — advisory-only placement

Full position preserved at [01a-perspective-archivist.md, Q5]. Key claim: if *any* rule is adopted, it belongs only in `prompts/development.md` as advisory guidance, not in `workspace-structure.md` as normative specification. Rationale: "workspace-structure.md is load-bearing for the engine's correctness... A folder-naming convention is not structural in this sense."

- **Activation warrant**: if a future session proposes moving folder-naming guidance from workspace-structure.md to prompts/development.md (or adopting a rule and placing it in workspace-structure.md in a way that causes the spec-prompt divergence Archivist predicts), the Archivist advisory-placement position is the preferred alternative.

## §5 Convergence-vs-coverage flags

Per `multi-agent-deliberation.md` v4 §Synthesis (Convergence vs coverage):

- **Convergence (multiple perspectives independently reached similar conclusions)**: Q6 finding; Q2 authority rule; Q5 no-validator-no-new-OI constraint; OI-007 scaling pressure as the backstop.
- **Coverage (only one perspective raised the point; others silent)**:
  - Minimalist's SESSION-LOG-supersession argument [01c, Framing note] — that the folder-name-as-thin-index function was absorbed by SESSION-LOG at Session 022 R8a. Archivist and Discoverer did not address this. The argument is load-bearing for the 2-of-3 Q1 position but the support is 1-of-3.
  - Discoverer's "index audit altitude" proposal [01b, Q6] — specifically the future-session agenda item. Archivist's "periodic open-ended attention" [01a, Q6] is related but not identical; Archivist does not propose a new session-type, Discoverer does (gestured, not specified).
  - Discoverer's closed-enumeration dispensation shape [01b, Q3] — the specific form of the dispensation is a single-perspective construction; Archivist and Minimalist reject the shape but do not propose alternative dispensation shapes (they reject all dispensations).

## §6 Limitations note (required per multi-agent-deliberation.md §Synthesis)

Required content for every multi-agent deliberation synthesis:

- **All three perspectives are Claude subagents from the same model family.** Shared training produces shared blind spots: cultural priors, argumentative reflexes, refusal patterns, aesthetic preferences. The 3-of-3 convergence on Q6 may reflect a genuine insight OR a shared Claude-family preference for framing narrowly; this synthesis cannot distinguish.
- **Intra-Claude-family size-mixing is not cross-model participation.** The three perspectives run through the Agent tool with unknown model-id / model-version per manifests; they may be the same underlying model. No OI-004 narrowing claim is made for this deliberation.
- **Parallel isolation prevents conversational anchoring, not training-distribution anchoring.** Consensus across subagents is weak evidence, not strong.
- **Brief-writing has no adversary.** The framing of the six design questions (e.g., Q1 framing "Should the engine formalise...") shaped responses. A different framing (e.g., "What is the minimum intervention that addresses the operator observation?") might have produced different convergences.
- **The synthesis step is the pattern's highest-risk single-agent re-entry point.** This synthesis is written by the session orchestrator (same agent-identity as the assessment author), who holds prior views on the folder-naming question formed during the pre-session exchange with the operator. Citation discipline (every perspective claim carries `[<file>, <section>]` reference) and dissent-preservation (Minorities §A/§B/§C) are applied but do not eliminate synthesizer bias.
- **No non-Claude participant convened.** Per §5c assessment trigger analysis, d023_* does not fire for this deliberation. Non-Claude participation is optional/recommended, not required. The operator's pre-session observation functioned as the external-pattern-detection input that a non-Claude Outsider might otherwise have provided. Voluntary:required ratio remains 9:8 unchanged; Session 027 does not contribute to OI-004 narrowing.

## §7 Decision shape for Decide step

This synthesis maps; it does not decide. The Decide activity (§Decide in `02-decisions.md`) adjudicates.

Three decision-shapes are available for the Decide step:

**Shape α (majority-aligned, lightest)**:
1. Acknowledge the Q6 finding as the session's load-bearing methodology output.
2. No new spec clause for folder-naming. Optionally add single advisory sentence to prompts/development.md (Archivist-aligned) OR minor revision to workspace-structure.md §provenance changing default to `NNN-session` (Minimalist-aligned).
3. No retroactive rename of Sessions 023/024/025/026.
4. Preserve Discoverer close-step rule as Minority §A with activation warrant.
5. Preserve Minimalist default-change as Minority §B (if Archivist path chosen) or as adopted position (if Minimalist path chosen).
6. Preserve Archivist advisory-placement as Minority §C (if Minimalist path chosen) or as adopted position (if Archivist path chosen).
7. Engine-v4 preserved; no engine-v bump.

**Shape β (Discoverer minority adopted)**:
1. Adopt close-step rename rule in workspace-structure.md §provenance.
2. Cross-reference in prompts/development.md.
3. Issue retroactive dispensation per Discoverer's scoped-enumeration form.
4. Substantive revision → engine-v4 → engine-v5 bump.
5. Preserve Archivist and Minimalist positions as Minorities with activation warrants.

**Shape γ (hybrid)**:
1. Acknowledge Q6 finding as methodology output.
2. Adopt Minimalist default change (`NNN-session-assessment` → `NNN-session` or keep `NNN-session-assessment` but specify "stable, not revised") in workspace-structure.md §provenance as minor revision.
3. No retroactive rename.
4. Add single advisory sentence to prompts/development.md noting that sessions producing substantive output *may* (not must) be renamed informally at close, but the folder name is not load-bearing — SESSION-LOG is the authoritative thin-index.
5. Preserve Discoverer close-step rule as Minority §A with activation warrant.
6. Engine-v4 preserved.

[synth: Shape α or γ is the 2-of-3-majority-honouring disposition; Shape β adopts the 1-of-3 minority. The operator ratified "optionally authorise a retroactive rename" at pre-session, which signals openness to either direction; the 2-of-3 deliberation outcome points toward α or γ as the deliberation's weight.]

## §8 Flagged for next session

Per Discoverer [01b, Q6] and Archivist [01a, Q6] shared direction: a future session may consider an "index audit" session-shape — periodic examination of the workspace as a listing, distinct from content audits, at the altitude that caught the folder-name drift. This synthesis does not propose the mechanism; it records the shared perspective convergence as a forward item.

## §9 End of synthesis

Three perspective files committed verbatim. Three manifests committed (Layer 2). One session-level participants.yaml committed (Layer 3). Independence-preservation verified via parallel Agent launches with no cross-perspective access during independent phase. Synthesis passes citation discipline: every perspective claim cites `[<file>, <question>]`.
