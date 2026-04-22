---
session: 013
title: Decisions — Artefact Revision (House Decision in Five Moves)
date: 2026-04-22
status: complete
---

# Decisions — Session 013

**Notice.** Per D-037/D-038/D-039 (adopted Session 006), every decision in a post-adoption session (≥006) carries `**Triggers met:**` and `**Triggers rationale:**` inline. Session 013 is a post-adoption session; decisions below follow the schema.

Decisions recorded in this session: **D-066 through D-068** (three decisions).

---

## D-066: Adopt the revision design and produce the revised external artefact

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** Reasonable practitioners genuinely disagreed (d016_3) — 3-1 cross-model split on move count (Reviser, Skeptic, Outsider for five moves with restructured-in-place Move 5; Householder for six moves with new Move 6); 3-1 split on disposal-handling placement (Reviser, Householder, Outsider for conditional-note-in-close-move; Skeptic for single-sentence-in-after-note); variance across four Move 5 title proposals; variance across Move 1 example-opening count (two vs three) and specific openers. Operator-marked load-bearing (d016_4) because this is the methodology's **first Validate-driven revision of an external artefact** — the user's report for Session 010's artefact is the first domain-actor-requested-revision the methodology has processed, distinct from Session 008's "no modifications requested" receipt that informed Session 009's *spec* revision without requiring *artefact* revision. d016_1 not triggered (no kernel revision); d016_2 not triggered (the artefact is not a specification per `workspace-structure.md` v2's applications vs specifications distinction; OI-002 heuristic does not apply to non-specification artefacts). d023_1/2/3/4 not triggered: no kernel modification; no multi-agent-deliberation or validation-approach revision; no OI-004 state change asserted in this decision. Non-Claude participation was voluntary, continuing the Sessions 005–012 conservative-inclusion pattern; five concrete Outsider-sourced contributions materially shaped adopted content (see Key Arguments Carried).

**Decision.**

1. **Adopt the five-move shape** with restructured-in-place Move 5, per the 3-of-4 cross-model convergence (Reviser + Skeptic + Outsider). Move count stays at five; the artefact title ("A House Decision in Five Moves") is preserved unchanged.

2. **Replace Move 1 with question-opener framing**, per the four-way convergence. Adopted text (synthesised from the three-example proposals with example openings drawn from Reviser, Outsider, and a new garden-corner variant):

   ```markdown
   ## 1. Name the decision

   One of you opens the conversation — usually with a question, not an answer. One line is enough.

   > *"Should we talk about the lounge?"*
   >
   > *"What should we do about that empty corner of the garden?"*
   >
   > *"Do we want to sort the shelving out, or leave it for now?"*

   You don't need to know the budget, the timing, or exactly what you're buying yet. Some of that only surfaces later, once you've both said what you care about.

   If you're not sure it's even worth a real conversation, say that too. Sometimes the answer is "let's just do it." Sometimes naming the decision out loud is the only move you need.
   ```

3. **Restructure Move 5 in place** with the Outsider-originated title "Close it, and name the follow-through" (per Outsider's flag that "owner" is project-management language; "follow-through" is plainer and domestic). Adopted text:

   ```markdown
   ## 5. Close it, and name the follow-through

   Someone says it out loud:

   > *"Alright — bookshelves, up to $500, let's order them this weekend."*

   The other confirms. That's the decision closed.

   Then say who's handling what comes next — ordering, scheduling, being home for delivery, whatever the thing needs. It's a real bit of work; you both own the decision, but one of you is carrying the next steps. If it splits naturally, say how.

   > *"I'll place the order tonight."*
   >
   > *"I can be home Saturday for the delivery."*

   Not a full plan — just enough that you both know what's been taken on.

   If something is being replaced, the old one is part of the follow-through too. Reuse it somewhere else, offer it to someone, donate it, or arrange disposal. This is often more work than people expect.

   > *"We'll offer the old shelf first, then donate it if no one takes it."*

   If you're not ready to close, say that too, and name when you'll come back to it — a specific day, not "soon."
   ```

4. **Do not modify Moves 2, 3, 4**, the "Not this" section, or the opening framing. All four perspectives converged on this scope discipline.

5. **Preserve the original artefact as v1.** File `applications/010-household-decision-protocol/house-decision-five-moves-v1.md` is created as a copy of the current v1 with `status: superseded` and `superseded-by: house-decision-five-moves.md` added to frontmatter. The canonical path `applications/010-household-decision-protocol/house-decision-five-moves.md` becomes v2, with `version: 2`, `last-revised-session: 013`, and `supersedes: house-decision-five-moves-v1.md` in frontmatter.

6. **Apply the register-drift watchlist as a Produce-check.** Per the Outsider's Q1/Q5 flags, grep the revised artefact body for each of "surface the decision," "surface tensions," "check in on," "align on," "check in with," "align on what matters," "hold space," "space to share." Zero hits required for commit. The watchlist is recorded in the session provenance (this decision) as ad-hoc check; a future session may decide whether to codify it into `validate.sh` or a brief-authoring convention (see WX-13-2).

7. **Preserve dissent.** Per the synthesis's §Recommendations 3:

   - **Householder's Move 6 / six-move dissent** [01b, Q2]: preserved as first-class minority. If the revised artefact's next use surfaces the failure mode the Householder named (close inherits caring-more-equals-owning-execution default from Move 4; both people believe closed, neither commits; weeks pass), Householder's position is the explicit warrant for reopening the Move 5/Move 6 structure question. Recorded as WX-13-1.

   - **Skeptic's single-sentence-acknowledgment / no-body-text-for-C4 dissent** [01c, Q3, Q6]: preserved as first-class minority with falsifiability condition. If a future domain-actor reports (should future domain validation become available) that the conditional disposal note reads as domain-specific scaffold rather than useful prompt, or implies that non-furniture domains should expect similar conditionals, the Skeptic's alternative text (*"Some decisions carry extra bits that vary by kind — clearing out what's being replaced, coordinating with a tradesperson, timing around seasons. Handle those where they fit; the five moves above are the shape of the conversation, not the whole job."*) is the explicit warrant for relocation. Recorded as WX-13-3.

   - **Session 010's preserved "no protocol at all" dissent** (per D-057.9): unchanged and still preserved. Session 013's work does not weaken it. The Skeptic's Session 013 Q6 observation that two positive Validate data points do not establish generalisable pattern is recorded as continuing warrant for the Session 010 dissent.

   - **Session 010's Drafter "we"-throughout dissent** (per D-057.9): also unchanged. Session 013 does not revisit voice; the adopted Outsider hybrid voice from Session 010 remains.

**Substantive-versus-minor classification per OI-002 heuristic.** Not applicable — no specification is being revised. This decision revises an external artefact. OI-002's heuristic scope is specification revisions (v1/v2/v3 with explicit supersedes pointer in `specifications/`). External-artefact revisions in `applications/` are governed by a distinct pattern that Session 013 uses operationally and does not formalise: preserve prior version with a `-v1` suffix in place, add `status: superseded` to the preserved file, and update canonical path's frontmatter with `version: 2`, `supersedes: [v1-filename]`, and `last-revised-session:`. Whether this pattern should be formalised into `workspace-structure.md` §applications is recorded in **WX-13-6** for future deliberation.

**Key arguments carried.**

1. **Four-way convergence on question-opener framing for Move 1** [01a, 01b, 01c, 01d, all at Q1]. All four perspectives independently arrived at the same core diagnosis. No perspective proposed retaining the imperative-declarative frame; no perspective proposed an alternative beyond the question form. This is the session's strongest four-way convergence and the load-bearing warrant for overturning the Session 010 Move 1 imperative-declarative frame.

2. **Three-of-four cross-model convergence on restructured-in-place Move 5** [01a, 01c, 01d at Q2]. Reviser, Skeptic, and Outsider converged (including across the model-family axis via the Outsider) on "close and owner are two beats of one conversational act; a separate Move 6 would create false ceremony." The Outsider's verbatim framing: *"In real use, couples do not experience 'we've decided' and 'who's actually doing the next bit' as two separate phases. They happen in one breath."*

3. **Outsider-originated "follow-through" terminology** [01d, Q2]: *"I would not use the word 'owner' in the artefact, even if the design discussion uses it. 'Owner' is project-management language."* Adopted as Move 5 title's load-bearing noun.

4. **Outsider-originated split-follow-through example structure** [01d, Q2]. Demonstrates splittable burden without enumeration-as-checklist. Adopted as Move 5's example-line pair.

5. **Three-of-four convergence on disposal-conditional-within-close-move** [01a, 01b, 01d at Q3]. Reviser and Outsider place in Move 5; Householder places in Move 6; synthesis locates in Move 5 consistent with the Q2 shape decision.

6. **Outsider-originated social-permission observation for question form** [01d, Q1, Q6]: *"'Should we talk about the lounge?' is not only a topic label. It is also a light request for attention and timing. It gives the other person room to say 'not right now.' Claude-family models often flatten that into a neat naming device and miss the social permission built into the question form."* Shapes the Move 1 example-opener selection — openers that leave room for "not right now."

7. **Reviser's C2 diagnostic refinement** [01a, Q6]: the flagged example's failure is the listing gesture, not corporate vocabulary. Shapes the Move 1 revision to remove the listing entirely rather than casualising its vocabulary.

8. **Outsider-originated register-drift watchlist** [01d, Q1, Q5]: five specific Claude-family corporate-adjacent phrases to avoid ("surface the decision," "check in on the lounge," "align on what matters," "surface tensions," "check in on each person's priorities"). Adopted as explicit Produce-check; no Claude perspective produced this specific list.

9. **Four-way convergence on not touching Moves 2, 3, 4, "Not this" section, or opening framing.** Hard constraint on scope.

10. **Skeptic's brief-framing meta-observation** [01c, Q6]: Labelling C1–C4 symmetrically as "corrections" produces symmetric-treatment pressure; C4 is better understood as a scope-boundary observation. Recorded as WX-13-5 for future brief-authoring conventions to consider.

**Rejected alternatives (preserved as dissent).**

- **Householder: new Move 6 / six-move shape** [01b, Q2, Q4]: *"Close-the-decision and name-the-owner are two different moments, not one, and the artefact has to treat them that way."* Rejected on three-of-four cross-model convergence but preserved as first-class dissent with operational warrant (WX-13-1). The Householder's argument that separating the moves breaks the caring-more-equals-owning-execution inheritance from Move 4 is the specific concern the synthesis's "you both own the decision, but one of you is carrying the next steps" clarification tries to address without the structural separation. If in use the clarification is insufficient to dissolve the inheritance, the Householder's separation is the preferred fix.

- **Skeptic: single-sentence-in-after-note for C4 / no-body-text-for-replaced-items** [01c, Q3, Q6]: *"The user isn't asking for the artefact to cover disposal; the user is asking for the artefact to acknowledge that stuff like disposal exists outside its frame."* Rejected on three-of-four convergence but preserved with explicit falsifiability condition per WX-13-3. The Skeptic's verbatim alternative text is preserved for future relocation should the falsifiability condition activate.

- **Reviser: two example openings for Move 1** [01a, Q1]: rejected on majority convergence (three of four proposed three examples). The Reviser's argument that "three would start to feel like a menu" is preserved; if use reports (via future domain validation if available, or via the Skeptic's attention to synthesis quality) the three-example form reads as menu-like, the Reviser's two-example form is the preferred contraction.

- **Householder: five-example Move 5 sub-task enumeration** [01b, Q2]: considered and rejected by the Householder themselves on register grounds; recorded here because the Householder's Q2 explicitly flagged it as a path the synthesis should resist. Corporate drift via explicit enumeration is already covered by d016_3 scope-discipline convergence.

- **Reviser: "Close it, and name who's following up" as Move 5 title** [01a, Q2]: slightly longer and uses "following up" (more project-management adjacent per the Outsider's flag) than the adopted Outsider title. Preserved as secondary candidate if the Outsider's title reads awkwardly in use.

- **Skeptic: "Close it, and say who picks it up" as Move 5 title** [01c, Q2]: preserved as tertiary candidate. The Skeptic's "picks it up" is slightly more idiomatic than "follow-through" but less generalisable across decision kinds (a garden-strip decision is less naturally "picked up" than "followed through").

**Non-Claude participation:** Included (Outsider = OpenAI GPT-5 via `codex exec`). Not required per D-023 (no kernel change, no spec change in D-023 categories, no OI-004 state change asserted). Conservative voluntary inclusion continues the Sessions 005–012 pattern. The Outsider's contributions materially shaped five adopted elements of the revision:

1. Move 5 title's "follow-through" noun (over "owner"/"following up"/"picks it up");
2. Social-permission framing of the question form (shaping Move 1 example-opener selection);
3. Split-follow-through example structure (shaping Move 5 two-example pair);
4. Register-drift watchlist (adopted as explicit Produce-check);
5. Three-policy-choice structure for the user-unavailability OI (shaping D-067's preferred-starting-point framing — see D-067 below).

This is **five concrete Outsider-sourced contributions** extending OI-004 closure criterion 3's cumulative data-point count.

---

## D-067: Open new OI-016 for domain-validation pathway under user unavailability

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** Reasonable practitioners genuinely disagreed (d016_3) — four distinct positions recorded on what the session should do about the user-unavailability constraint: Reviser mild/artefact-sprawl-concern, Householder cautious/not-routine, Skeptic strong-pause-by-default, Outsider policy-choice-required with tripartite options. No two-of-four converge on the same stance. Operator-marked load-bearing (d016_4) — this is the first explicit methodological constraint recorded in response to a domain-validation pathway narrowing, and affects the decision surface for every Session 014+ that proposes producing an external artefact. d016_1 not triggered (no kernel revision in this decision — OI-016's activation may later warrant kernel §7 elaboration, but that deliberation is for the activating session, not Session 013). d016_2 not triggered (no spec creation/revision in this decision). d023_1/2/3/4 not triggered: no kernel modification; no D-023 spec-family revision; **opening a new OI is not an OI-004 state change (D-023.4 covers only OI-004 specifically).**

**Decision.** Open new **OI-016: Domain-validation pathway under user unavailability**.

**Text (as entered in `open-issues.md`):**

> ### OI-016: Domain-validation pathway under user unavailability
> **Surfaced:** Session 013 (per D-067; sourced from user's standing constraint in the Session 010 Validate receipt, per `00-validate-user-report.md`)
> **Status:** Open — activation trigger specified
>
> Session 013's user Validate receipt for the Session 010 external artefact included a standing constraint: *"I'm no longer available to manually validate any artefacts you produce due to availability constraints."* Sessions 008 and 010 both obtained Domain validation per `methodology-kernel.md` v3 §7 via single-user self-report after live use. Session 013 itself does not require new Domain validation (it revises an artefact whose Validate receipt is already in hand); but **Session 014+ producing any new external artefact loses the default domain-validation pathway the methodology has relied on for its two existing external artefacts**.
>
> **Four-perspective position spread recorded in Session 013 deliberation:**
>
> - Reviser [01a, Q6]: mild concern — the methodology may compensate for lost feedback by producing more artefact-sprawl, when it should produce less and more precise.
> - Householder [01b, Q6]: cautious — methodology should not refuse external-artefact production but should not treat it as routine; n=2 is narrow evidence base.
> - Skeptic [01c, Q6]: strong — Session 014+ should not produce new external artefacts until the validation-source question is resolved; pause by default, unpause only via explicit argument.
> - Outsider [01d, Q6]: policy-choice-required — before the next external-artefact session, methodology needs a choice between (a) recruit alternate domain validators; (b) label outputs as unvalidated; (c) pause external-artefact production. The main risk is *procedural self-deception* — continuing as though the old validation loop still existed.
>
> **Activation trigger:** first Session 014+ that proposes producing a new external artefact. That session must engage with OI-016 as prerequisite deliberation; the OI is load-bearing but not a hard pause. A session proposing new external-artefact production without addressing OI-016 is a specification violation under the methodology's "leave coherent state" continuity rule.
>
> **Preferred starting point for the activating session's deliberation:** the Outsider-originated three-policy-choice frame — (a) recruit alternate domain validators; (b) label outputs as unvalidated; (c) pause external-artefact production. The activating session is not bound to choose one of these three; a fourth option (proxy validation, panel review, observational pilot, self-validation with explicit limitations) is permissible if argued. The three-policy-choice frame is the starting point because it gives the deliberation a clean decision surface and names the procedural-self-deception failure mode that any chosen option must address.
>
> **Skeptic's strong-pause position preserved as first-class minority within this OI.** If the activating session elects option (a) "recruit alternate validators" or option (b) "label as unvalidated," the Skeptic's minority is the explicit warrant that the methodology is operating below the Session 009 kernel §7 bar and should not claim Domain validation has been performed unless the chosen alternative is substantive enough to match the kernel's domain-actor criteria.
>
> **Scope boundary:** OI-016 addresses the *pathway* question. It does not address revision of existing Validate receipts for Session 008 and Session 010 artefacts (both in hand, both complete). It does not require kernel §7 revision — that question is downstream of the pathway decision.
>
> **Interaction with OI-014 (domain-actor receipt shape variance).** OI-014's activation trigger was "the first external application whose domain-validation receipt shape materially differs from Session 008's single-user-self-report pattern." Session 013's receipt for the Session 010 artefact is a *shape continuation* of Session 008 (single-user-self-report), not a material variance — it's the same user reporting on a different artefact. So OI-014's activation trigger has not fired in Session 013. However, any option-(a) resolution of OI-016 (recruit alternate validators) would *automatically* activate OI-014 in the activating session — the alternate validator's receipt would by construction materially differ from the Session 008 shape. The two OIs are interdependent: OI-016's resolution may force OI-014's activation.

**Substantive-versus-minor classification per OI-002 heuristic.** Not applicable — no specification is being revised in this decision. Opening a new OI is an `open-issues.md` update; the OI-002 heuristic scope is specification revisions, not OI list updates.

**Key arguments carried.**

1. **Outsider-originated three-policy-choice frame** [01d, Q6]: the tripartite structure (recruit / label-as-unvalidated / pause) gives the activating session a clean decision surface. No Claude perspective produced this tripartite structure; the Claude perspectives had four distinct positions that did not cleanly partition. Adopted as preferred starting point.

2. **Outsider-originated "procedural self-deception" framing** [01d, Q6]: *"The main risk is not quality in the abstract; it is procedural self-deception. If the system keeps producing external artefacts as though the old validation loop still exists, it will be pretending to have a safeguard that has already been withdrawn."* Shapes the OI's severity posture.

3. **Skeptic's load-bearing minority position preserved** [01c, Q6]: the strong-pause-by-default framing is preserved inside the OI, not softened to majority position. The Skeptic's argument that options (a) and (b) may operate below the Session 009 kernel §7 bar is specific and falsifiable — the activating session must engage with it substantively if it chooses those options.

4. **Householder's "scope the OI precisely, leave the design question open" framing** [01b, Q6]: the OI names the constraint without pre-empting the mechanism. Adopted as the OI's structural discipline.

5. **Reviser's language-level concern** [01a, Q6]: artefact-sprawl pressure under lost validation feedback. Recorded inside the OI as a secondary watchpoint (procedural self-deception is the primary risk; artefact-sprawl is a specific manifestation the Reviser's register-sensitivity surfaced).

6. **Interaction with OI-014** is recorded explicitly. This is a synthesis-originated observation drawing on all four perspectives' implicit references to alternate-validator shapes, but no single perspective named the OI-014 interaction. Not a cross-model contribution; a synthesis-originated structural observation.

**Rejected alternatives (preserved as dissent).**

- **Do not open an OI at all.** Rejected because the constraint is load-bearing for future external-artefact work. Opting not to record it would be the exact procedural self-deception the Outsider named.

- **Open the OI with a hard-pause default.** Rejected in favour of the soft-activation-trigger form. Skeptic's strong-pause position is preserved inside the OI. A hard pause at the Session 013 level would be Session 013 committing to the Skeptic's minority over the other three perspectives' varied positions, which is not what synthesis should do on a 1-1-1-1 split.

- **Open the OI with a specific preferred option (e.g., "recruit alternate validators").** Rejected on the Householder's framing: the OI should name the constraint precisely and leave the design question open. Pre-empting the activating session's choice would reduce its deliberation to ratification.

- **Pair the OI with a commitment mechanism analogous to D-048.4 (the methodology-claim-downgrade provision).** Considered in Session 013's assessment (open question deferred to close) and rejected here. Reasoning: D-048.4 was a commitment mechanism for a specific conditional failure case (Session 008 fails to produce external application → downgrade the domain-general claim in Session 009). Session 013's situation is different: the constraint is *already* present, known, user-stated. A commitment mechanism would add machinery without corresponding uncertainty. The activating session's prerequisite-deliberation requirement is sufficient commitment by itself.

**Non-Claude participation:** Included (Outsider). Not required per D-023. The Outsider's tripartite policy-choice frame and "procedural self-deception" framing both shape the adopted OI — two concrete Outsider-sourced contributions materially shaping this decision.

---

## D-068: OI state housekeeping — Session 013 updates

**Triggers met:** [d016_4]

**Triggers rationale:** Operator-marked load-bearing (d016_4) for session-housekeeping per the Session 005 D-033 / Session 006 D-043 / Session 008 D-052 / Session 009 D-056 / Session 010 D-059 / Session 011 D-062 / Session 012 D-065 precedent of a final per-session OI-state-update decision. d016_1/2/3 not triggered: no kernel change; no spec creation or substantive revision; no reasonable-practitioner-disagreement surfaced on the state updates themselves (they are bookkeeping over the session's production record). d023_1/2/3/4 not triggered: no kernel modification; no D-023 spec-family revision; no OI-004 state change (the tally gains criterion-3 data points but does not cross any threshold and does not change status; this is within the Session 008 D-052 literal reading that "no change" is not "change" per D-023.4).

**Decision.** Update `open-issues.md` as follows.

**OI-001 (Naming the methodology):** Closed (Session 012 per D-064). Session 013 does not revisit. The name **Selvedge** is not referenced in the Session 013 revised artefact (external artefact is household-facing; methodology name belongs in methodology-facing contexts per `specifications/identity.md` §scope). WX-12-6 (Selvedge-steering-effect) spot-checked against Session 013 content in the assessment's Session 012 fidelity audit (§4): no textile-metaphor leakage, no methodology-vocabulary leakage, Selvedge's three-trait frame absent as implicit rhetorical shape. Audit: clean.

**OI-002 (Threshold for substantive revision vs. minor correction):** Unchanged (no specification revision in Session 013). **Session 013 observation recorded** (not a formal data point): the OI-002 heuristic's scope is *specification* revisions. Session 013 performs an *external-artefact* revision, which lies outside OI-002's existing scope. The pattern Session 013 uses operationally (preserve prior version with `-v1` suffix, mark `status: superseded`, update canonical-path frontmatter with `version:`, `supersedes:`, and `last-revised-session:`) is analogous to but not identical with the specification-revision pattern. See WX-13-6 for the question of whether this pattern should be formalised into `workspace-structure.md` §applications. For now, Session 013 uses the pattern operationally without formalising it.

**OI-004 (Incorporating genuinely independent perspectives):** **Status unchanged at closable-pending-criterion-4-articulation** (tally holds at 4 of 3 per Session 011 D-062; unchanged at 4 of 3 per Session 012 D-065). Session 013 is the **fifth consecutive voluntary-inclusion-without-d023-trigger session** (Sessions 007, 008, 010, 012, and now 013; Session 013 is also the ninth heterogeneous-participant deliberation overall). Criterion 3 (recorded impact on outcomes) gains **five concrete Outsider-sourced contributions**: (1) "follow-through" as the preferred Move 5 title noun over "owner"; (2) social-permission framing of the question form shaping Move 1 example-opener selection; (3) split-follow-through example structure shaping Move 5; (4) register-drift watchlist adopted as Produce-check; (5) three-policy-choice structure for OI-016. Cumulative criterion-3 data points across Sessions 005–013: **thirty-four** (twenty-nine through Session 012 per D-065; five added in Session 013).

**Watchable pattern update:** Voluntary-to-required ratio is now 5:4 (five voluntary non-advancing sessions: 007, 008, 010, 012, 013 vs. four required-trigger sessions: 005, 006, 009, 011). This is the first session where voluntary count exceeds required. For any future OI-004 closure deliberation reviewing criterion 2's robustness, the 5:4 ratio is additional evidence that the methodology's cross-model discipline is sustained across both required and voluntary contexts, tilting toward voluntary.

**OI-005 (Sub-activities and work-type variants):** Unchanged — unblocked-available-for-future-deliberation (per Session 010 D-059 and the Session 011 D-060 W1-addressed update). Session 013 did not deliberate sub-activities.

**OI-006 (Cross-references between specifications):** Unchanged. Session 013 did not touch.

**OI-007 (Scaling the open issues format):** Count increments from **12 to 13** after Session 013 (OI-016 opened per D-067; no closures). Direction reverses back to upward after the Session 012 decrement (which was itself the first downward reversal since Session 009). Monitor.

**OI-008 (Persisting validation reports):** Unchanged. Session 013's `00-validate-user-report.md` records the user's full verbatim report inside the provenance directory, which is the current pattern; ephemerality of `tools/validate.sh` output remains.

**OI-009 (Monitor for drift-to-ritual in multi-agent deliberation):** **Monitor.** Session 013's primary work is external-artefact revision (driven by a Validate receipt from a domain-actor), not self-work. G/O/K/S does not apply directly as a ritual-tracking filter (per D-059 precedent for external-application work). The G/O/K/S criterion-package remains the operational OI-009 criterion for any future self-work.

**OI-010 (Cross-model or human participation mechanism):** Remains closed (Session 005 per D-032). Session 013 is the ninth operational use of the mechanism with no incidents. The mechanism continues to work as specified.

**OI-011 (Intra-family model mixing as a deliberation-quality lever):** Unchanged.

**OI-012 (`validate.sh` hard-coded `02-decisions.md` path):** **Monitor, with a minor data point.** Session 013 placed the external artefact revision at `applications/010-household-decision-protocol/house-decision-five-moves.md` and preserved v1 as `house-decision-five-moves-v1.md` in the same directory — outside any provenance directory. Provenance files in `provenance/013-artefact-revision/` follow the standard `01-...`, `02-decisions.md`, `03-close.md` numbering without collision. The hard-coded path continues to not actively bite. However, Session 013 is **the first session to preserve a v1 alongside a revised external artefact** in `applications/`. This pattern may become common if external-artefact revisions become regular; OI-012's re-visit trigger is unchanged (variable decisions-file numbering or second independent concrete collision), but the new pattern is recorded here for WX-13-6 consideration.

**OI-013 (Non-file external artefacts):** Unchanged — monitor. Session 013's artefact is file-shaped (Markdown revision of a file-shaped original). Activation trigger has not fired.

**OI-014 (Domain-actor receipt shape variance):** **Monitor, with explicit note of future-interdependence with OI-016.** Session 013's Validate receipt for the Session 010 artefact is a continuation of the Session 008 single-user-self-report shape (same user, written report, post-live-use, timely). It is not a material variance; OI-014's "materially differs" activation trigger has *not* fired in Session 013. **However, OI-016's activation (any Session 014+ that proposes producing a new external artefact) will force a choice about alternative validator shapes; if the option-(a) resolution is adopted ("recruit alternate domain validators"), the alternate validator's receipt will by construction materially differ from the Session 008/010 shape, automatically activating OI-014.** The two OIs are interdependent. Recorded here as OI-014 annotation for clarity.

**OI-015 (Laundering enforcement gap in domain reading):** Unchanged — monitor; activation trigger specified. Session 013's assessment noted Section 1 Read had both workspace reading (full workspace state) and domain reading (user's verbatim Validate report as primary domain input). No laundering occurred: the user's report is preserved verbatim in `00-validate-user-report.md` and re-examined explicitly in the deliberation's Q1-Q6 rather than being absorbed silently as Read-activity context. Session 013 is a positive example of the reconciliation working; no activation of OI-015.

**OI-016 (Domain-validation pathway under user unavailability):** **New.** Opened per D-067. Text above.

**Session 013 minor corrections:** None. No specification changes.

**Substantive-versus-minor classification per OI-002 heuristic.** Not applicable — no specification is being revised.

**Key arguments carried.**

1. **OI-004 criterion-3 data points advance by five** — the largest single-session addition since Session 011 (five) and Session 012 (five). Consistency-of-contribution across three sessions suggests the Outsider mechanism continues to produce distinct content at a stable rate.

2. **Voluntary-to-required ratio crosses 5:4** — a quantitative threshold the methodology has not previously seen. Evidence for any future criterion-2-robustness review.

3. **OI-014 and OI-016 interdependence is load-bearing** — recorded explicitly rather than left implicit. The interdependence is the kind of inter-OI relationship OI-006 (cross-references between specifications) anticipated but was deferred; this is the first inter-OI reference-by-construction in the workspace, and a minor data point for OI-006's eventual activation.

4. **OI-007 count direction reverses upward to 13** — first increment since Session 011; not yet threshold-breaching but worth monitoring if the trend continues.

5. **OI-016 opening does not require D-023 triggering** — per the literal reading of D-023 clauses 1 (kernel), 2 (multi-agent-deliberation spec), 3 (validation-approach spec), 4 (OI-004 state change). Opening a *new* OI is not an OI-004 state change. This is recorded for future sessions that may assume new-OI-opening is D-023-triggering by analogy to OI-004 closure.

**Rejected alternatives (preserved as dissent).** None substantial. The alternative of not opening OI-016 was rejected in D-067; the alternative of opening OI-016 with a hard-pause default was also rejected in D-067. No Session 013 watchpoints (WX-13-1 through WX-13-6) are opened as formal OIs — they are recorded in D-066/D-067 provenance per the Session 010 D-058 precedent.

**Non-Claude participation:** Included (Outsider). Not required per D-023.

---

**End of decisions. Session 013 records three decisions: D-066 (artefact revision), D-067 (open OI-016), D-068 (OI state housekeeping). Cumulative decision count after Session 013: 68.**
