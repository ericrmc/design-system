---
session: 007
title: Decisions — External Application Re-examination and Launch Preparation
date: 2026-04-19
status: complete
---

# Decisions — Session 007

**Notice.** Per D-037/D-038/D-039 (adopted Session 006), every decision in a post-adoption session (≥006) carries `**Triggers met:**` and `**Triggers rationale:**` inline. Session 007 is a post-adoption session; decisions below follow the schema.

**Framing note.** Session 007's work-product is classified as **external-application preparation**, not as self-infrastructure work. This classification is load-bearing for OI-009's treatment (see D-048) and honours the Skeptic+Outsider framing convergence while being operationally consistent with Generalist+Steward content.

---

## D-044: External application is overdue; Session 007 produces the launch preparation; Session 008 executes first external application

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** Genuine reasonable disagreement on timing and framing — Position A vs Position B in the brief were both defensible; the Skeptic additionally rejected the brief's binary framing entirely (D-016.3). Operator-marked load-bearing because this decision determines the methodology's immediate trajectory and the OI-009 monitor's status (D-016.4). No D-023 trigger fires: this decision does not modify `methodology-kernel.md`, does not create or substantively revise `multi-agent-deliberation.md` or `validation-approach.md`, and does not assert a change in OI-004's state.

**Decision:**

1. **External application is overdue.** Four-way convergence on Position A from four independent rationales: confirmation-bias (Generalist), highest-value-uncertainty (Outsider), accumulating-validation-conflict (Skeptic, forced-choice), process-gap-not-readiness-gap (Steward).

2. **Session 007's work is external-application preparation.** The session produces: (a) first-target selection criteria (D-046); (b) selection mechanism including the user-ask (D-045); (c) stress-test watchpoints for first external application (D-047's companion); (d) a binding pre-commitment for Session 008 (this decision plus D-048). This work is not self-infrastructure; it is the operational handoff from generic kernel to first external application.

3. **Session 008 executes first external application.** Session 008 is constrained to target ratification and first external application; no unrelated self-work is permitted in Session 008 without explicit invocation of a newly-surfaced, specifically-named blocker, recorded as a decision with its load-bearing claim defended (not asserted).

4. **If Session 008 does not execute first external application**, OI-009 escalates per D-048 and the methodology's domain-generality claim is downgraded per D-048's consequence clause.

**Rationale:** The four-way Position A convergence is genuine at the direction level; the four rationales do not reduce to one another. The Skeptic's evidence that would change the position ("a specific, named weakness... that can be fixed only through self-work") and the equivalent criteria from the other three perspectives all require a concrete blocker to be articulable — none was surfaced in the deliberation. [`01-deliberation.md`, Q1].

The session's work-product as "external-application preparation" honours the Skeptic's framing concern: "if continued self-work happens, the honest increment is to do the external-application re-examination itself as the session's content" [`01c-perspective-skeptic.md`, Q5]. It is operationally identical to what the Generalist and Steward proposed as "the last self-increment before external" [`01a`, Q5; `01b`, Q5] and to what the Outsider proposed as "a narrowly scoped first-application launch protocol" [`01d-perspective-outsider.md`, Q5]. The four perspectives converged on content; the synthesizer's judgment is that the honest label is "external-application preparation."

**Rejected alternatives:**

- **Begin first external application in Session 007 itself** (not argued by any perspective as the primary path, but implicit in strict Position A; Skeptic considers it): rejected because (a) no target has been selected through any accountable mechanism; (b) selecting unilaterally is what Session 006 explicitly rejected on authority grounds; (c) the Q2 convergence requires user involvement before target-selection, which requires the user-ask to be delivered and responded to.
- **Continue self-work with new justification distinct from Session 006's** (Position B / the brief's explicit continued-self-work path): rejected because no perspective produced a concrete articulable self-work blocker that external application would not better surface. [`01b`, Q1, evidence-criteria for B; `01c`, Q1, "no one in this deliberation has produced one yet"].
- **Do the external application re-examination as pure research, commit nothing durable** (hypothetical; not argued): rejected because the re-examination's Session-006 mandate requires a decision, not an abstract analysis.

**What remains open:**

- Session 008's actual execution of first external application is the test. Failure to execute activates OI-009 hard per D-048.
- The Skeptic's audit of Session 006's close (that OI-009 was redefined without deliberation) is a real finding that this session does not formally close — D-048 treats it explicitly, but the underlying question of how close-reports can introduce normative content without deliberation is a pattern concern that future sessions should watch.

---

## D-045: Selection mechanism — criteria-first plus user-ask in close plus user-direction or ratification before Session 008

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** Genuine reasonable disagreement — three-of-four convergence on criteria-first-plus-user-direction; Skeptic dissent on "criteria-first is circular, just ask" (D-016.3). Operator-marked load-bearing because the mechanism determines how Session 008 opens (D-016.4). No D-023 trigger.

**Decision:**

1. **Session 007 produces selection criteria (D-046).** These are the criteria by which any candidate first target is evaluated.

2. **Session 007's close includes an explicit user-ask.** The close report explicitly asks the user: (a) whether they have a specific domain and problem they want as first external target; (b) whether, if they have no target in mind, they want the orchestrating agent to propose a target meeting D-046's criteria for their ratification; (c) whether any domains are explicitly ruled out. The ask is phrased so that user silence past a reasonable window is itself a valid response that the methodology has a defined handler for.

3. **Session 008 opens under one of the following branches, determined by the user's response before Session 008 begins:**

   - **Branch A — user-directed target.** User has named a domain and problem. Session 008's Assess activity checks the user-directed target against D-046's criteria; if the target fails any criterion, Session 008 records the conflict and either (i) re-asks the user with the conflicting criterion named, or (ii) proceeds with the user's target on the grounds that user-direction overrides agent-selection defaults (provided the target is not disqualified on hard criteria such as absence of a Validate analogue — see D-046).
   - **Branch B — user-ratified agent proposal.** User has delegated target selection to the orchestrating agent. Session 008's Assess activity produces a shortlist of up to three candidates meeting D-046's criteria plus one recommended pick with reasoning; the user's accept/reject is recorded as provenance before Session 008's Produce activity begins. Session 008 may proceed with Branch B in-session (using available communication channels) or halt and await response.
   - **Branch C — fallback default (user-silent).** If the user has not responded within the window defined in the close, Session 008 proceeds with a single narrowly-scoped candidate target selected by the orchestrating agent using D-046's criteria, with the absence of user input explicitly recorded and the selection marked as subject to retroactive veto. The fallback is tagged `non_unilateral_because_mechanism_exhausted: true` in the Session 008 decision record.

4. **The close's user-ask is the load-bearing act** that distinguishes Session 007's preparation from ritual-tracking deferral. Failure to deliver the ask is itself an OI-009 activation per D-048.

**Rationale:** Three-of-four convergence on combination mechanism [`01a`, Q2; `01b`, Q2; `01d`, Q2]. The Outsider's framing — "define criteria now, obtain user nomination or ratification next, and only then launch the first external session" [`01d`, Q2] — is adopted as the cleanest summary of the three-of-four position.

The Skeptic's critique (criteria-first is circular because criteria are validated against prior self-work [`01c`, Q2]) is acknowledged and partially addressed: D-046's criteria are derived from the deliberation itself, not from prior self-work artefacts, and two of the criteria (mid vocabulary distance; not pre-shaped by agent) explicitly guard against the methodology's own preferences propagating into selection. The Skeptic's "just ask" position is operationally encoded in D-045.2 — the user-ask *is* the cleanest ask, presented with criteria as context, not as a filter imposed on the user's answer. `[synth]` The Skeptic's operational concern is met; the framing preference (ask first, criteria as context) is preserved as minority framing.

**The ask itself is not gated by the criteria.** A user-directed target that does not meet all of D-046's criteria is still accepted under Branch A per D-045.3 (user-direction overrides agent-selection defaults); the criteria bind the *agent-selection* paths (Branches B and C).

**Rejected alternatives:**

- **Pure user-direction alone** [`01d`, Q2 rejected-alternatives]: fails under broad or ambiguous direction.
- **Multi-agent selection session** [`01b`, Q2; `01d`, Q2 both reject]: risks becoming more methodology-about-methodology at exactly the point where external contact is needed.
- **Unilateral proposal for user ratification (without prior criteria)** [`01d`, Q2 rejects]: weakens provenance — later readers would see a pick but not the standard.
- **Criteria-only, target-later indefinitely** [`01b`, Q2 explicitly rejects as permanent-deferral-artifact]: the criteria are not a deferral mechanism; Session 008 must open under one of Branches A, B, or C.
- **Just-ask (no criteria-first), Skeptic's preferred form** [`01c`, Q2]: preserved as lead rejected alternative; the difference in practice is whether the user sees criteria alongside the ask. The chosen form provides the user with criteria as context for a more informed response; the Skeptic's form would be simpler but risks criteria being produced post-hoc to rationalise the user's answer.

**What remains open:**

- The window length for user silence before Branch C activates. Proposed: 72 hours or the next session's open, whichever is later. This is set in the close (see 03-close.md).
- Whether D-045's branches become part of a new specification in a future session (once the mechanism has been exercised at least once). Not pursued this session per D-047.

---

## D-046: First-target criteria — bounded, reversible, validatable, mid-distance, externally-legible; software-adjacency ruled out of agent-selection default

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** Genuine reasonable disagreement — four-way convergence on shape but 2-2 cross-model split on software-adjacency as acceptable first-target (D-016.3). Operator-marked load-bearing because the criteria bind Session 008's target selection (D-016.4). No D-023 trigger.

**Decision:**

The following eight criteria, in this order, constitute the first-target criteria for first external application. A candidate target must satisfy all criteria to be selectable by agent-selection paths (D-045 Branches B and C). User-directed targets (Branch A) override criteria 1 and 8 only; criteria 2–7 are hard requirements that the methodology cannot honestly work around even under user direction.

1. **Bounded scope.** The target admits a first-session executable increment — Session 008 produces a concrete external artefact (specification, decision, deliberation-record, design fragment) in one session without closing the entire problem. Open-ended first targets are disqualified. Multi-session continuation is expected; un-bounded scope is not.

2. **Reversibility / low stakes.** The first external artefact is advisory or sandboxed — failure of the methodology on the target cannot produce real-world harm. Commit-now irreversible first targets (legal documents, safety-critical design, clinical decisions) are disqualified.

3. **Validate analogue required.** The target must admit a non-trivial Validate activity within the methodology's terms — a test, a peer-review pass, a pilot exercise, a reviewer panel, a reproducibility check, or a comparable domain-native mechanism. Targets where "validation" reduces to "does the spec read coherently" are disqualified because the methodology's Validate activity degenerates to self-assessment [`01b`, Q3; `01c`, Q3; `01d`, Q3].

4. **Mid vocabulary distance.** The target's vocabulary must differ from the methodology's native self-description (activities, specifications, provenance, deliberations, triggers, manifests) but overlap enough to translate. [`01a`, Q3; `01b`, Q3; `01c`, Q3; `01d`, Q3].

5. **Externally legible.** The target's outcome must be readable and judgeable by someone outside this workspace who has not internalised the methodology's provenance. If the first external artefact is only interpretable by readers who have read `multi-agent-deliberation.md`, no external evidence has been produced [`01c`, Q3].

6. **Not pre-shaped by orchestrating agent.** If the target is selected by the orchestrating agent (Branches B, C), the selection must visibly resist the agent's expected-to-succeed bias. This is operationalised as: the selection record must name one target property the agent expected would be challenging, and the reason the agent proceeded nonetheless [`01c`, Q3].

7. **Domain-accessible from available materials.** The work of Session 008 must be executable from a bounded brief plus materials the user can provide; it must not require fieldwork, proprietary data, gated external APIs, or physical artefacts the workspace cannot handle. The Skeptic's position that "accessibility should be a *problem to solve*, not a *criterion to satisfy*" [`01c`, Q3] is partially adopted — accessibility is a floor (work must be *possible*), not a ceiling (targets should not be chosen *because* they are easy); this is why criterion 6 exists as a counter-weight.

8. **Software-adjacency ruled out of agent-selection default.** Domains whose vocabulary is software-design, tool-building, specification-management, or workspace-engineering are **disqualified as agent-selection defaults** (Branches B, C) because the methodology was built in a software-shaped workspace and success on software-adjacent targets is indistinguishable from confirmation bias [`01a`, Q3; `01c`, Q3]. However, if the user directs a software-adjacent target under Branch A, the target is accepted — user-direction overrides this criterion. The 2-2 cross-model split on this question is recorded explicitly: Outsider and Steward accepted software-adjacent as candidates [`01b`, Q3; `01d`, Q3]; Generalist and Skeptic rejected. The decision adopts the stricter position for agent-selection and the permissive position for user-direction.

**Rationale:** Criteria 1–5 are four-way convergences [`01-deliberation.md`, Q3]. Criterion 6 is Skeptic-unique coverage; adopted because it addresses the "agent picks a target it expects to succeed" failure mode [`01c`, Q3]. Criterion 7 is a four-way convergence with Skeptic's qualification absorbed. Criterion 8 is the 2-2 split resolved in favour of the stricter position for agent-selection, with user-direction overriding.

The criteria are deliberately not written as a new specification. Per D-047, no new specification is created this session; these criteria live as D-046's content and are referenced from D-045 and the close. A future session may promote them to a specification after Session 008 has exercised them at least once.

**Rejected alternatives:**

- **Include software-adjacency as acceptable for agent-selection defaults** (Outsider + Steward position [`01b`, Q3; `01d`, Q3]): rejected for agent-selection on confirmation-bias grounds; preserved for user-direction via Branch A.
- **Omit criterion 6 (not pre-shaped by agent)** (no perspective argued for omission; candidate from general scepticism about over-specification): rejected because the failure mode is real and the criterion's cost is minimal (one sentence in the selection record).
- **Write criteria as a new specification** (`external-application-protocol.md` or similar; Generalist and Steward implied support in Q5): rejected per D-047 on Skeptic+Outsider cross-model grounds about pre-use spec creation. Can be revisited after Session 008.
- **Remove criterion 8 entirely and let the user decide** (hypothetical; a pure-user-direction position): rejected because agent-selection paths (Branches B, C) need a default — silence on software-adjacency for agent paths would produce de-facto software-adjacent picks because the methodology's priors lean there.

**What remains open:**

- Whether criterion 8 should expand to include other "methodology-adjacent" domains (e.g., design-of-AI-systems, deliberation-of-deliberation) that were not specifically named in the deliberation. Deferred; Session 008 or later may refine as experience accumulates.
- Whether criterion 7's "workspace-accessible materials" bar should be tightened (Skeptic's concern: "too close") or relaxed (Outsider: "solvable from a bounded brief plus materials the user can provide"). Deferred; practical balance will be tested on first external application.

---

## D-047: No pre-use specification or kernel changes; stress-test watchpoints recorded for Session 008's probing

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** Genuine reasonable disagreement — 2-2 cross-model split, Skeptic and Outsider against pre-use changes, Generalist and Steward for minor pre-use changes (D-016.3). Operator-marked load-bearing because this decision determines whether Session 008 opens under the current specifications (unmodified) or under preparatory spec revisions (D-016.4). No D-023 trigger — explicitly, this decision *rejects* specification revisions; creating no revisions does not trigger D-023.1–3, and no OI-004 state change is asserted.

**Decision:**

1. **No pre-use specification or kernel changes in Session 007.** The four active specifications (`methodology-kernel.md` v1, `workspace-structure.md` v1, `multi-agent-deliberation.md` v3, `validation-approach.md` v3) remain unmodified going into Session 008. This decision honours the Skeptic+Outsider cross-model convergence: "pre-emptive changes would be a warning sign" (Outsider) [`01d`, Q4]; "pain is the signal. Removing the pain removes the learning" (Skeptic) [`01c`, Q4]. The Generalist+Steward position (three specific pre-use gaps — Read clarification; `applications/` top-level; validation self-reference audit) is preserved as stress-test watchpoints per D-047.2.

2. **Session 008 records stress-test watchpoints.** The following specification-gap hypotheses are recorded in Session 008's Assess activity for explicit probing during first external application:

   - **Watchpoint W1: Read activity specification for external domains.** The kernel's Read activity assumes finite prior provenance (the workspace). An external domain may have no prior workspace provenance or a large external corpus. Session 008 records, as provenance, how the Read activity was performed for its external target and whether the existing kernel wording was sufficient, under-specified, or misleading. [`01a`, Q4; `01b`, Q4].
   - **Watchpoint W2: Workspace structure for external work-products.** Currently `specifications/` and `provenance/` are implicitly about the methodology itself. Session 008 records what directory structure it used for external work-products and whether mixing them with methodology self-artefacts produced confusion, category errors, or ambiguity. [`01a`, Q4; `01b`, Q4; `01c`, Q4].
   - **Watchpoint W3: Self-referential phrasing in active specifications.** Tier 2 guided questions and some portions of multi-agent-deliberation.md and validation-approach.md may read as self-referential when applied to external work. Session 008 records every place where spec phrasing required on-the-fly reinterpretation [`01a`, Q4; `01b`, Q4].
   - **Watchpoint W4: Validate activity for external domains.** The Validate activity's domain-native analogue (D-046 criterion 3) must be exercised. Session 008 records how Validate was performed and whether the methodology's Validate framing was adequate for the external domain's test-analogue [`01b`, Q4; `01c`, Q4; `01d`, Q4].

3. **Watchpoints are records, not revisions.** Session 008 is not obligated to fix the watchpoints mid-session; it is obligated to *observe and record*. A future session (Session 009 or later) may use the accumulated watchpoint records to propose specification revisions that are grounded in empirical contact rather than pre-emptive anticipation.

**Rationale:** The Skeptic+Outsider cross-model convergence is a stronger signal than the Generalist+Steward pair argument because it crosses the model-family axis [`01-deliberation.md`, Cross-Model Observations, Pattern 1]. The substantive Skeptic argument (pain is the signal; revisions before contact contaminate the test) and the substantive Outsider argument (pre-emptive changes are a warning sign that the methodology is protecting itself from the test) are independent; neither reduces to the other.

The Generalist+Steward named gaps are not rejected as false — they may well bite on first external application. The methodology's disposition is that they should bite visibly and be recorded, rather than being patched over in anticipation. Watchpoints preserve the Generalist+Steward content (the specific hypothesised gaps) while honouring the Skeptic+Outsider procedural constraint.

**Rejected alternatives:**

- **Adopt the Generalist+Steward three minor pre-use changes** (Read kernel clarification; `applications/` top-level; validation self-reference audit). Rejected on cross-model grounds (Skeptic+Outsider converge against); preserved as watchpoints (W1, W2, W3).
- **Adopt only one or two of the three pre-use changes** (e.g., only the `applications/` top-level; the Steward noted this specific change could be "deferred to Session 008" [`01b`, Q4]). Rejected: partial adoption would halve the Skeptic+Outsider concern without resolving it, and would still contaminate the test to some degree.
- **Create a new external-application-protocol specification to house D-045 and D-046** (not explicitly argued by any perspective as primary; Generalist and Steward implied this by "producing the criteria as a durable package"). Rejected per the same Skeptic+Outsider principle extended to new specs: creating a new normative spec before first external use over-formalises the selection mechanism and gives it a durability the mechanism has not yet earned. Can be revisited after Session 008 exercises D-045/D-046 at least once.
- **Record stress-test watchpoints as specification-level revisions with `status: proposed`** (hypothetical; a middle path). Rejected because a `status: proposed` specification has all the weight of a specification without the legitimacy of having been exercised; watchpoints-as-decisions avoid this category error.

**What remains open:**

- Whether, after Session 008, the watchpoint records warrant specification revisions. Deferred to Session 009+ as a function of what Session 008 surfaces.
- The Skeptic's broader concern about same-voice-on-both-sides (assessment and close written by the same orchestrating agent). This is a structural concern the Session 007 close addresses explicitly; not a per-decision matter here.

---

## D-048: OI-009 conditional escalation, Session 008 constraint, and methodology-claim downgrade provision

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** Genuine reasonable disagreement — three-of-four that Session 007's outcome can avoid OI-009 activation conditional on Session 008 execution; Skeptic dissent that OI-009 is activated regardless (D-016.3). Operator-marked load-bearing because this decision determines OI-009's operational state and Session 008's binding constraints (D-016.4). No D-023 trigger — this decision changes OI-009's state, not OI-004's; no kernel modification and no specification revision.

**Decision:**

1. **OI-009 status is conditional.** Session 007 produces external-application preparation (per D-044, D-045, D-046, D-047). This work-product satisfies the Generalist+Outsider+Steward criteria under which OI-009 is not activated for Session 007 [`01-deliberation.md`, Q6]. The Skeptic's "activated regardless" dissent is preserved.

2. **Session 007 adopts the four-perspective disjunctive criterion-package for OI-009 assessment going forward.** Self-work in any future session is load-bearing iff it satisfies at least one of:

   - **(G)** *Translation-to-external-frame* — the need for the increment can be stated in terms that refer to the methodology's asserted external use, not only in terms that refer to the methodology's self-description [Generalist, `01a`, Q6].
   - **(O)** *Narrows-external-action-decision-space* — the increment removes a concrete blocker to a named next external action [Outsider, `01d`, Q6].
   - **(K)** *External-reader visibility* — the weakness the increment addresses would be visible to a reader outside the workspace reading the specs for the first time [Skeptic, `01c`, Q6].
   - **(S)** *Specific-obstacle resolution* — the increment resolves a specific articulable obstacle that blocks a named next step, where the obstacle was identified in provenance and the next step is concrete, OR closes an open issue whose closure changes what later sessions can do [Steward, `01b`, Q6].

   Self-work satisfying none of (G), (O), (K), (S) is ritual-tracking and activates OI-009.

3. **Session 008 is constrained to target ratification and first external application.** Specifically:

   - Session 008 must open with a target under Branch A, B, or C of D-045.3.
   - Session 008's primary work-product is a first external application artefact per D-046's bounded-scope criterion.
   - Session 008 may not substitute unrelated self-work for first external application.
   - If a newly-surfaced blocker arises during Session 008 that makes first external application infeasible, the blocker must be recorded as an explicit decision with its load-bearing claim defended (not asserted), and OI-009 activates.

4. **Methodology-claim downgrade provision.** If Session 008 does not execute first external application AND does not surface an articulable blocker meeting the standard in D-048.3, the methodology's domain-generality claim is downgraded by explicit edit to PROMPT.md (or a `README.md` or equivalent top-level artefact) from "domain-general design methodology" to "promising but unvalidated self-hosting methodology" [Outsider-unique proposal, `01d`, Q6]. The downgrade is itself a substantive revision requiring its own deliberation and is not preemptively authorised here; this clause is a *commitment mechanism* that Session 009 (or whichever session confronts the failure) must either execute or explicitly deliberate against. Failure to either execute the downgrade or deliberate against it would be the clearest possible OI-009 activation.

5. **Session 007 explicitly records the Skeptic's OI-009-redefinition audit** [`01c`, Q1] as a finding that Session 006's close introduced a count-based criterion without prior deliberation. The criterion-package in D-048.2 supersedes the count-based criterion: *Session 007 adopts the four-part disjunction (G, O, K, S) as the operational OI-009 criterion, and the count-of-consecutive-self-sessions is no longer the primary criterion.* Counts may be a secondary heuristic but are not load-bearing.

**Rationale:** Three-of-four convergence on conditional-avoidability [`01a`, Q6; `01b`, Q6; `01d`, Q6]. The Skeptic's "activated regardless" position [`01c`, Q6] is preserved as the lead rejected alternative; its substantive concern (that the deferral-count criterion was smuggled into Session 006's close) is absorbed into D-048.5.

The four-part criterion package (G, O, K, S) is `[synth]`-adopted on the grounds that no single criterion subsumes the others; the disjunction is more robust than any single. Each of the four criteria was independently proposed by a distinct perspective [`01-deliberation.md`, Q6]. The disjunction honours the four perspectives without collapsing them.

The Outsider's downgrade-of-claim proposal is unique coverage [`01d`, Q6]. No Claude perspective surfaced this specific consequence mechanism. It is adopted as D-048.4 because it provides a concrete consequence for continued deferral that is visible externally (in PROMPT.md) and is therefore externally legible (satisfying the Skeptic's criterion K for OI-009 assessment of that decision when it is made).

**Rejected alternatives:**

- **OI-009 activated regardless of Session 007's outcome** (Skeptic's position [`01c`, Q6]): rejected as binding; Skeptic's underlying concern (the deferral-count criterion is under-deliberated) is absorbed into D-048.5's criterion-package supersession. Preserved as lead rejected alternative.
- **Adopt only one of the four criteria (G, O, K, or S) as the OI-009 criterion**: rejected because each criterion exposes a different failure mode; single-criterion adoption would miss load-bearing cases. The disjunctive package is stricter and more honest.
- **Keep the Session 006 close's count-based criterion unchanged**: rejected per D-048.5 — the count was introduced without deliberation and the four-perspective deliberation produced content-based criteria that supersede it.
- **Omit the methodology-claim downgrade provision**: rejected on the grounds that OI-009 "active warning" without a concrete consequence is toothless. The Outsider's framing — "An open issue that never changes behavior is itself part of the ritual it was opened to detect" (paraphrased from Skeptic [`01c`, Q6] but consonant with Outsider [`01d`, Q6]) — is load-bearing.
- **Execute the downgrade in Session 007 itself** (hypothetical): rejected because the downgrade is a substantive revision of PROMPT.md-level content that requires its own deliberation when and if the trigger condition fires.

**What remains open:**

- How Session 009+ assess OI-009 activation on sessions that do not clearly satisfy (G), (O), (K), or (S) — judgment calls are expected.
- Whether the criterion-package (G, O, K, S) should itself be promoted to a specification or to an OI-009 entry expansion. Not pursued this session; a future session may elevate if the package is used repeatedly.
- Whether the methodology-claim downgrade mechanism should be documented as a general pattern (for other OIs with "active warning" status) or kept specific to OI-009. Not pursued this session.

---

## D-049: OI state housekeeping — OI-009 conditionally escalated; OI-004 tally unchanged; no new OIs; no D-023 triggered this session

**Triggers met:** [d016_4]

**Triggers rationale:** Operator-marked load-bearing because OI-state housekeeping records the session's OI impact and the sustained-practice-tally determination for OI-004 (D-016.4). The decision does not create reasonable-disagreement beyond what D-044–D-048 already address (D-016.3 absorbed in those decisions). No D-023 trigger: this decision asserts *no* change in OI-004's state; "no change" is not "change" per D-023.4's literal reading (consistent with Session 006 D-043's interpretation that *any* change to OI-004's state — including a tally advance — is a state change; here the tally is explicitly unchanged).

**Decision:**

1. **OI-009** — conditionally escalated per D-048. Status updated: "Active warning (conditional): continues if Session 008 executes first external application; activates hard with methodology-claim-downgrade provision if Session 008 does not execute." The four-part criterion package (G, O, K, S) from D-048.2 replaces the count-based criterion from Session 006's close.

2. **OI-004** — status unchanged (`narrowed-pending-sustained-practice`); sustained-practice **tally unchanged at 2 of 3**. Session 007's deliberation included a non-Claude participant (Outsider) per D-021 Shape A with full D-024 manifest, but **none of Session 007's decisions trigger D-023**:

   - D-023.1 (modifies `methodology-kernel.md`): not triggered — no kernel modification.
   - D-023.2 (creates or substantively revises `multi-agent-deliberation.md`): not triggered.
   - D-023.3 (creates or substantively revises `validation-approach.md` in Tier-2-touching ways): not triggered.
   - D-023.4 (asserts change in OI-004 state): not triggered — this decision asserts *no* change; the tally stays at 2 of 3 and the status label is unchanged.

   Per the strict v3 spec closure-criterion-2 reading ("Non-Claude participation has occurred in at least three required-trigger deliberations across different sessions"), Session 007's deliberation was not a required-trigger deliberation; the tally does not advance.

   The honest recording: **non-Claude participation was included conservatively because the deliberation's outcome space included D-023.1-triggering kernel-revision possibilities (ultimately not taken); the outcome did not fire any D-023 trigger; the sustained-practice tally remains at 2 of 3.** This is a new pattern for the methodology — a third non-Claude session that does not advance the required-trigger tally. Future sessions may consider whether criterion 2 should expand to include voluntary non-Claude inclusion, but this session does not propose that expansion.

3. **OI-001** (naming the methodology) — open, unchanged. Not addressed this session; four-way rejected as primary Session 007 work in Q5 [`01-deliberation.md`, Q5].

4. **OI-002** — open, unchanged. No spec revisions this session; no new data point.

5. **OI-005, OI-006, OI-007, OI-008, OI-011** — open, unchanged. OI-005 (sub-activities) is specifically flagged by the deliberation as still-blocked on first external application [`01-deliberation.md`, Q5]; Session 008 is expected to either (a) surface enough work-type variance from first external application to make OI-005 addressable in a subsequent session, or (b) if the first external application is too narrow, leave OI-005 blocked pending additional applications.

6. **No new open issues opened.** Candidates considered and rejected:

   - **OI-012 (hypothetical): Voluntary cross-model deliberations that don't trigger D-023 — how should the sustained-practice tally treat them?** The Session 007 deliberation is a real instance of this question. Rejected per the Session 006 D-043 Archivist precedent ("wait for a real instance to surface" — here the instance is real but the methodology's honest answer is "do not advance the tally; let the criterion stand as written"). Opening an OI to revisit the criterion would be reactive; the criterion is defensible as written and should be revisited only if the methodology accumulates multiple voluntary-inclusion sessions whose non-advance feels perverse.
   - **OI-013 (hypothetical): Same-voice-on-both-sides concern (Skeptic's audit finding).** The Skeptic's concern that the orchestrating agent writes both the assessment (pro-external) and the close (determines outcome) is a structural observation. Rejected as standalone OI because the four-perspective deliberation is the methodology's designed counter-weight and has operated as intended in Session 007; the concern is recorded in the Points of Disagreement and in this decision's rationale, and future sessions should watch the pattern but do not need an OI to do so.

**Rationale:** Housekeeping consolidation, consistent with Session 005 D-036 and Session 006 D-043 closing-accounting patterns. The no-tally-advance recording is novel for the methodology and must be explicit — previous sessions' closings have either advanced the tally (Session 005 to 1, Session 006 to 2) or not included non-Claude participation; this is the first session to include non-Claude participation without advancing the tally.

**The deliberation's recorded cross-model impact on outcomes** (criterion-3 evidence for OI-004, even though the tally doesn't advance):

- **Pattern 1**: Skeptic+Outsider cross-model convergence against pre-use spec changes — shaped D-047 directly [`01-deliberation.md`, Cross-Model Observations, Pattern 1]. This is impact-of-cross-model-presence on outcomes and is the strongest criterion-3 evidence from this session.
- **Pattern 2**: Outsider's downgrade-of-claim proposal [`01d`, Q6] unique among perspectives — shaped D-048.4 directly. This is impact-of-cross-model-presence on outcomes.
- **Pattern 3**: Outsider's ratification-as-third-path framing [`01d`, Q2, Meta-note] informed D-045's Branch B articulation.

Three concrete influences. The absence of a tally advance does not erase the impact — the impact is recorded regardless. Whether this counts toward OI-004's closure criterion 3 ("Recorded impact on outcomes") is a question the v3 spec does not explicitly address; the synthesizer's reading is that criterion 3 is met independent of criterion 2's tally.

**Rejected alternatives:**

- **Assert OI-004 tally advance 2→3** (hypothetical; not argued by any perspective): rejected because no D-023 trigger fires for any Session 007 decision. Declaring a tally advance without a D-023 trigger would be dishonest under the current criterion 2.
- **Assert that Session 007's deliberation retroactively fires D-023** (hypothetical, if one of D-044–D-048 is re-classified as kernel-touching or spec-creating): rejected because D-047 explicitly decides *not* to modify specs or create new ones; reclassifying D-047 as a D-023 trigger for its *decision-not-to-revise* would be inconsistent with the literal D-023.2/3 wording ("creates or substantively revises").
- **Propose a revision to v3 spec closure criterion 2 to count voluntary non-Claude inclusion** (hypothetical): rejected as scope-creep for Session 007 and on the Skeptic principle that such a revision should be triggered by a concrete pattern of perverse outcomes, not pre-emptively. Future sessions may revisit if the pattern arises.

**What remains open:**

- Whether future sessions will accumulate enough voluntary-inclusion-no-tally-advance instances to warrant revising criterion 2.
- OI-004 closure criteria 1 (participant independence) and 3 (recorded impact) continue to be met for Session 007 (three concrete cross-model influences recorded); criterion 2 (sustained practice) remains at 2 of 3; criterion 4 (articulation of "substantively different training provenance") remains unaddressed.
- Session 008's outcome determines whether OI-009 resolves its conditional status per D-048.
