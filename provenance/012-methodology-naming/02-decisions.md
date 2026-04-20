---
session: 012
title: Decisions — OI-001 Methodology Naming
date: 2026-04-20
status: complete
---

# Decisions — Session 012

**Notice.** Per D-037/D-038/D-039 (adopted Session 006), every decision in a post-adoption session (≥006) carries `**Triggers met:**` and `**Triggers rationale:**` inline. Session 012 is a post-adoption session; decisions below follow the schema.

Decisions recorded in this session: **D-063 through D-065** (three decisions).

---

## D-063: Adopt the name "Selvedge" for the methodology; create `specifications/identity.md` as canonical placement

**Triggers met:** [d016_2, d016_3, d016_4]

**Triggers rationale:** Creates a new specification file in `specifications/` (d016_2). Reasonable practitioners disagreed: three viable candidate names on the shortlist (Selvedge, Sediment, Strata); four distinct placement proposals (kernel frontmatter only, kernel title + PROMPT.md + identity.md, identity.md only, refuse); Skeptic adversarial position arguing against any naming (d016_3). Operator-marked load-bearing: closes OI-001, the longest-deferred open issue in the workspace, surfaced at Session 001 and carried forward across eleven sessions (d016_4). d023_1/2/3/4 not triggered: the new file is `specifications/identity.md`, not `methodology-kernel.md`, `multi-agent-deliberation.md`, or `validation-approach.md`; no OI-004 state change asserted in this decision.

**Decision:** The methodology is named **Selvedge**. The canonical placement for the name is `specifications/identity.md`, a new single-purpose specification file whose sole scope is the name, its origin, its intended use, and the reopening conditions under which the naming question would become legitimately reopenable.

**Rationale:**

The four-perspective deliberation produced a 3-of-4 majority favouring naming (Namer, Steward, Outsider conditional-yes or yes) against the Skeptic's refuse-to-name minority. The Skeptic's refuse-case is preserved as first-class dissent per `provenance/012-methodology-naming/01c-perspective-skeptic.md` and per the Reopening conditions in `specifications/identity.md`.

Among the candidate names proposed across the four perspectives, three survived cross-model scrutiny (Selvedge, Sediment, Strata) after filtering out:
- Internal-vocabulary compound names (Record Kernel, Session Kernel, Kernel Method) per Outsider's cross-training divergence flag at `[01d, Q2]`: *"I would expect Claude-family perspectives to cluster around explicit compounds like 'Provenance Kernel' or 'Session Method.' I think that would be a mistake. The name should not freeze the current glossary into the methodology's public face."* The Namer (Claude) did indeed produce three such compounds as its top three, confirming the prediction.
- Count-ossified names (Ninefold, The Nine) per the pre-commitment risk to exactly nine activities.
- Severe-collision names (Kernel Method — ML literature; Provenance (bare) — W3C PROV / data-provenance; Trace — general software; Loom — many products).

User ratification (recorded at Session 012 open after synthesis): *"Name, to avoid de-facto naming, noting that it's only a light-touch canonical name. Selvedge. `specifications/identity.md` as recommended."* This ratification honours the synthesis Recommendation 1 (name; avoid the informal-de-facto-naming risk Outsider flagged at `[01d, Q6]`: *"it would also increase the chance of informal de facto naming later, which is a worse form of commitment because it arrives without a recorded decision"*), Recommendation 2 (Selvedge is Outsider's top pick; lowest collision risk of the three shortlisted), and Recommendation 3 (identity.md-only is the three-of-four cross-model preferred placement).

**Key arguments carried:**

1. **Outsider's cross-training divergence critique of internal-vocabulary compounds** `[01d, Q2]` was adopted as the filter that removed Record Kernel, Session Kernel, and Kernel Method from the shortlist. No Claude perspective produced this meta-level pattern critique; it is Outsider-originated.

2. **Outsider's candidate Selvedge** `[01d, Q2]` with the "self-edge" etymology mapping to self-hosting + anti-unraveling preservation + multi-strand-held-together. The three traits the metaphor names correspond to three of the methodology's distinctive commitments. No Claude perspective proposed this candidate or any textile-metaphor candidate.

3. **Outsider's preferred placement `specifications/identity.md` with concrete proposed file text** `[01d, Q4]`. The placement's "smallest blast radius" (no kernel v-bump; no PROMPT.md stickiness; no kernel-as-defining-organ overclaim) is argued specifically by the Outsider; Skeptic converges conditionally on the same placement as "lightest available" if refusal is overruled.

4. **Light-touch canonical name framing** `[01d, Q1]`: *"a reference handle, not a brand layer."* Shapes the scope of the `specifications/identity.md` file — deliberately narrow; name + origin + intended use + reopening conditions only; no mission statement, values, or manifesto content.

5. **Skeptic's four falsifiability conditions** `[01c, Q5]` are incorporated into `specifications/identity.md` as explicit Reopening conditions. These make the naming decision genuinely revisable rather than merely notionally so; they preserve the Skeptic's minority position operationally, not only as dissent text.

6. **Steward's identity-fit framework** `[01b, Q1 Q3]` — "name only the mature dimensions" — is honoured by the choice of Selvedge, which accents self-hosting and preservation (mature) without accenting external-adoption-breadth, community-scale, or domain-proven-practice (under-developed). The Steward's own candidate Sediment also satisfies this criterion but accents preservation specifically rather than the three-trait combination Selvedge names.

7. **Namer's honesty in ranking Record Kernel as #1 while also arguing the refuse-case has comparable strength** `[01a, Q5]` was honoured by preserving the Namer's honest ambivalence rather than forcing a false unanimity. Record Kernel is recorded in the shortlist archive as the Claude-family first preference but not on the user-ratified shortlist.

8. **Three-of-four cross-model rejection of kernel-title canonicalisation and PROMPT.md-first placement** shaped the chosen `specifications/identity.md`-only placement. Kernel-title would have over-stated the kernel's centrality relative to the methodology's other components; PROMPT.md-first would have made the name constitutive of every future session-start rather than referential.

**Rejected alternatives:**

- **Record Kernel** (Namer #1 candidate). Rejected on three-of-four cross-model convergence against kernel-vocabulary compounds. Preserved in the Namer's raw output and in this decision's archive as the Claude-family first preference.
- **Sediment** (Steward candidate). Rejected on the user's ratification choosing Selvedge. Sediment is a live alternative; its preservation-specific accent made it strong on one dimension but narrower than Selvedge's three-trait metaphor. Preserved as shortlist candidate #2.
- **Strata** (Namer #4 / Outsider #3, only cross-perspective overlap). Rejected on cross-model-convergent collision-risk concerns (both Namer and Outsider cite heavy existing usage). Preserved as shortlist candidate #3.
- **Ninefold / Session Kernel / Kernel Method / The Nine / Provenance (bare)**. Rejected per reasons in the synthesis; ossification, collision, or compound-overfitting respectively.
- **Braid / Trace / Loom** (Outsider candidates #2, #4, #5). Outsider's own ranking placed these below Selvedge; the synthesis did not re-elevate them for the shortlist.
- **Refuse to name** (Skeptic primary position). Rejected on user ratification favouring naming to avoid informal de-facto naming. Preserved as first-class minority with four falsifiability conditions operationalised as Reopening conditions in `specifications/identity.md`.
- **Kernel title or frontmatter as canonical placement** (Steward-favoured; Namer-favoured). Rejected on three-of-four cross-model preference for identity.md-only and on the specific Outsider critique of kernel-title-overclaiming. Preserved as available via normal supersession revision if a future session finds identity.md-only too peripheral.
- **PROMPT.md first-paragraph self-reference** (Steward supplementary). Rejected as too sticky and constitutive of every session-start. Preserved as available for future revision.
- **SESSION-LOG.md header only**. Rejected as retrospective not normative (Outsider). Preserved as record via the SESSION-LOG entry naming the adopted identifier.
- **No canonical placement, external-references only**. Rejected on the Outsider observation that this is functionally a refusal to name, and the user's explicit choice to avoid informal de-facto naming.

**Non-Claude participation:** present (Outsider = OpenAI GPT-5 via `codex exec`, session id `019daa64-f24f-7402-be96-565c135009a1`, reasoning effort xhigh, 22,575 tokens). Full D-024 manifest at `manifests/outsider.manifest.yaml`. Five concrete Outsider-sourced contributions materially shaped the adopted decision (enumerated above under "Key arguments carried"). Non-Claude participation was voluntary for this decision — d023_1/2/3/4 did not fire — but was included per the methodology's sustained-practice convention across Sessions 005-011 and the Q2/Q4/Q5 questions where independently-trained perspective was expected to differ meaningfully from Claude-family output.

---

## D-064: Close OI-001 (methodology naming); record resolution with Skeptic dissent preserved

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** Reasonable practitioners disagreed on whether to close or hold open (d016_3): Skeptic argued explicitly against closure on "methodology's own disciplines argue against premature closure" grounds; Namer argued the refuse-case is comparably strong; Steward argued closure-by-naming on friction-tax grounds; Outsider argued closure satisfies G/O/K/S on K+S criteria. Operator-marked load-bearing: OI-001 is the longest-open issue in the workspace (surfaced Session 001); closure changes what subsequent sessions may reference without parenthetical disclaimers (d016_4). d016_1/d016_2 not asserted: no kernel change; no new spec creation in this decision (that is D-063). d023_* not triggered: OI-001 is not OI-004; no kernel modification; no multi-agent-deliberation or validation-approach revision.

**Decision:** OI-001 (methodology naming) moves to **Resolved** status. Resolution record added to `open-issues.md` Resolved Issues table. Resolution cites D-063 (name adoption) and this decision (OI-001 closure), with pointer to `specifications/identity.md` Reopening conditions.

**Rationale:**

OI-001's original surfacing condition (Session 001 Q6 resolution): *"Naming is recorded as an open issue for future sessions to address when the methodology has enough identity to name meaningfully."* The Session 012 deliberation addressed this question explicitly.

Three of four perspectives found identity sufficient for a light-touch canonical name (conditional-yes from Namer and Steward; yes-light-touch from Outsider). The Skeptic found identity insufficient. The methodology's multi-perspective-with-preserved-dissent discipline does not require unanimity for closure; it requires that the minority position be preserved at its strongest and that the closure reasoning be load-bearing on its own terms, not by overruling dissent.

The closure is load-bearing on:
- Outsider's G/O/K/S evaluation `[01d, Q5]`: satisfies K (external-reader visibility — namelessness is a visible weakness); satisfies S (closes an articulated long-deferred open issue; changes what later sessions reference).
- The Steward's friction-tax argument `[01b, Q5]`: applications/ references that would otherwise accumulate awkwardness under sustained "the methodology" formulation.
- The user's ratification reasoning: *"to avoid de-facto naming"* — the de-facto-naming risk is the Outsider's `[01d, Q6]` warning that deferred naming produces informal naming-by-habit without recorded decision, which is a worse form of commitment.

The Skeptic's dissent is preserved operationally via the Reopening conditions in `specifications/identity.md`. These four conditions are the Skeptic's falsifiability conditions `[01c, Q5]`, adopted as the explicit triggers under which a future session may legitimately reopen the naming question. The Skeptic's concern that "even a 'provisional' name tends to stick" remains honestly acknowledged: reopening requires genuine evidence (not merely preference), and the burden for reopening-in-absence-of-evidence is explicitly recorded.

**Rejected alternatives:**

- **Refuse-to-name and leave OI-001 open** with updated notes (Skeptic's primary proposal). Rejected on three-of-four majority favouring naming and user ratification. The reasoning that supports this rejection is preserved in the decision record and in `specifications/identity.md` Reopening conditions; it is not a dismissed position but a minority position the closure works around rather than over.
- **Close OI-001 and retire the question** (i.e., remove reopenability). Rejected. The methodology's preservation-and-reversibility discipline does not retire questions; it closes them with conditions under which reopening would be legitimate. This is how OI-010 was closed (in Session 005, per D-032 with the cross-model participation mechanism moving into sustained practice under OI-004). OI-001's closure follows the same pattern with the Skeptic's falsifiability conditions as reopening triggers.
- **Partial closure** (e.g., close "should we name?" but leave "which name?" open). Rejected. The deliberation addressed both together; splitting them would fragment the closure without methodological benefit.

**Non-Claude participation:** present via D-063's Outsider participation, which materially shaped closure criteria via the light-touch-canonical-name framing and the Reopening-conditions incorporation. Voluntary (not d023-required).

---

## D-065: OI state housekeeping; Session 012 watchpoints; WX-11-3 pattern novel data recorded

**Triggers met:** [d016_4]

**Triggers rationale:** Operator-marked load-bearing (d016_4) for session-housekeeping per the Session 005 D-036 / Session 006 D-043 / Session 007 D-049 / Session 008 D-052 / Session 010 D-059 / Session 011 D-062 precedent of a final per-session OI-state-update decision. d016_1, d016_2, d016_3 not triggered: no kernel change; no spec creation or substantive revision in this decision (identity.md was created in D-063); no reasonable-practitioner-disagreement surfaced on the state updates themselves (they are bookkeeping over D-063 and D-064's adopted content). d023_* not triggered: no kernel modification; no D-023 spec-family revision; no OI-004 state change — Session 012 is a voluntary-Outsider-no-d023-trigger session (the fourth after Sessions 007, 008, 010), so the OI-004 criterion-2 tally does not advance per Session 007 D-049 precedent. Criterion-3 data-point accumulation is not itself an OI-004 state change per the Session 008 D-052 / Session 010 D-059 reading.

**Decision:** Session 012 OI-state updates and new watchpoints recorded:

### 1. OI-001 closure (per D-064)

OI-001 moves from Open to Resolved. `open-issues.md` updated: OI-001 entry moves to Resolved Issues table; Active count decrements 13 → 12.

### 2. OI-002 (threshold for substantive revision vs. minor correction)

Session 012 creates `specifications/identity.md` as a new specification. This is a **creation**, not a revision — outside OI-002's binary of substantive-vs-minor-revision. No v-bump applies; no supersession; the specification is v1 with `supersedes: none` per the v1-spec convention. OI-002's heuristic does not cover the new-file case; Session 012 records this as a small observation for OI-002's future heuristic development but does not add a formal data point to OI-002.

### 3. OI-004 (incorporating genuinely independent perspectives)

**Tally:** unchanged at 4 of 3 (beyond satisfied threshold, reached in Session 011 per D-062). Session 012 is the **fourth non-advancing non-Claude-voluntary session** after Sessions 007, 008, and 010. No d023_* trigger fired in Session 012 (see this decision's triggers rationale above), so per the Session 007 D-049 / Session 008 D-052 / Session 010 D-059 precedent the tally does not advance.

**Criterion-3 evidence base:** gains **five concrete Outsider-sourced contributions** materially shaping D-063:
1. Cross-training divergence critique of internal-vocabulary compounds as name-family (Outsider-originated meta-pattern; no Claude perspective produced this at perspective-level).
2. Selvedge candidate with self-edge etymology and three-trait metaphor mapping (Outsider-originated; no Claude textile-metaphor candidate produced).
3. `specifications/identity.md` placement with concrete proposed file text (Outsider-primary; Skeptic-conditional convergence on placement form; Outsider-unique on the file-text proposal).
4. Light-touch canonical name framing (Outsider's Q1 conditional-yes framing as "reference handle, not brand layer" shaped the scope of identity.md as narrow single-purpose file).
5. Mostly-Claude-process maturity-risk asymmetry argument (Outsider's `[01d, Q5]` claim that internal coherence outruns external legitimacy in model-mediated processes; shaped the synthesis's weighting of the Skeptic's refuse-case seriously rather than dismissively).

**Cumulative criterion-3 data points across Sessions 005–012:** twenty-four through Session 011 per D-062; five added in Session 012 (above); total **twenty-nine**. Criterion 3 was satisfied since Session 005; Sessions 009, 010, 011, 012 extend the evidence base with five sessions' worth of concrete per-session influence records.

**Closure status:** unchanged from Session 011 — *closable pending criterion-4 articulation*. Criteria 1, 2, and 3 remain satisfied; criterion 4 ("articulated definition of 'substantively different training provenance' and enumerated acceptable participant kinds") remains unmet and requires an explicit closure deliberation that Session 012 did not pursue.

### 4. OI-005 (sub-activities)

No change. W1 and W4 addressed via Sessions 009/011 respectively; sub-activities across §2 Assess, §3 Convene, §4 Deliberate, §5 Decide, §6 Produce, §8 Record, §9 Close remain deliberable in future sessions. Session 012 did not address any further sub-activities.

### 5. OI-007 (scaling open issues format)

Active open-issue count decrements from **13 to 12** after OI-001 closure via D-064. File remains readable; directory-per-issue migration still not urgent; monitor.

### 6. OI-009 (monitor for drift-to-ritual)

**Status:** Monitor. Session 012 self-work (naming) was evaluated against G/O/K/S criterion-package per D-048. Three-of-four perspectives concluded the work passes G/O/K/S on K+S criteria (Outsider explicit at `[01d, Q5]`; Namer and Steward implicit in recommending naming). Skeptic's `[01c, Q1]` argument that the session's primary work bounced and the deliberation is motivated self-work is preserved as minority position; Session 012 honoured the concern by (a) applying G/O/K/S explicitly in the Q5 analysis; (b) adopting the lightest-defensible placement (identity.md-only) consistent with the Skeptic's "if overruled, lightest available" conditional preference; (c) incorporating the Skeptic's falsifiability conditions as operational reopening triggers. OI-009 does not activate on Session 012.

### 7. OI-012 (`validate.sh` hard-coded `02-decisions.md` path)

No change. Session 012's artefact is at `specifications/identity.md` (outside provenance/); provenance files follow standard numbering. No collision pressure this session. Monitor.

### 8. OI-013 (non-file external artefacts)

Not applicable. The artefact this session produces (`specifications/identity.md`) is a workspace specification, not an external-application artefact. OI-013's activation trigger (first non-file-shaped external artefact) unchanged.

### 9. OI-014 (domain-actor receipt shape variance)

Not applicable this session (no external-application validation receipt received or produced). OI-010 Validate still pending per user report at Session 012 open. Monitor.

### 10. OI-015 (laundering enforcement gap in domain reading)

**Observed, not activated.** Session 012's Read activity (the orchestrating agent's absorption of the workspace before Assess) was bounded and cited: the assessment explicitly notes which prior-session artefacts were consulted. The deliberation brief's domain knowledge was sourced from PROMPT.md, Session 001 Q6 reasoning, and the accumulated specifications — all **workspace reading** per kernel v3 §1, not domain reading. No laundering pattern observed. Activation trigger (first post-Session-011 external-artefact session observing laundering) unchanged; Session 012 is not an external-artefact session in the relevant sense.

### 11. Session 012 Watchpoints

- **WX-12-1 (claim-of-maturity):** EXAMINED. The Q1 deliberation honestly tested the identity threshold; 3-of-4 conditional-yes with specific mature-vs-underdeveloped markers named; Skeptic's "accumulation ≠ maturation" argument preserved. Not activated this session.
- **WX-12-2 (self-referential naming):** EXAMINED. Selvedge is an external metaphor (textile) not derived from workspace internal vocabulary. The three internal-vocabulary compounds the Namer produced (Record Kernel, Session Kernel, Kernel Method) were explicitly demoted in synthesis per Outsider's cross-training flag. Not activated.
- **WX-12-3 (Outsider-third-way pattern continuation from WX-11-3):** **NOVEL DATA RECORDED.** The pattern observed in Sessions 009/010/011 (Outsider third-way resolving 2-2 Claude splits) does not continue in its Session 009/010/011 form. Session 012's Outsider contribution is a **genre-level cross-training critique** (Claude-compound-names vs metaphors) rather than a split-resolving third-way. Session 012's Q4 Outsider position converges with Skeptic-conditional rather than third-waying between two Claude positions. First session since Session 008 where Outsider-third-way-split-resolution does not occur; pattern-evolution evidence for WX-11-3 under continued observation.
- **WX-12-4 (brief-priming):** EXAMINED. Fifth consecutive brief-priming-absent session (Sessions 008–012). Session 012 brief avoided Session 011 distinctive vocabulary ("intake vs commitment", "laundering", "ratchet", "routing clause", "inline-bolded-names") beyond minimal necessary context. Discipline confirmed.
- **WX-12-5 (WX-11-4 activation check):** EXAMINED. Session 012 does not cite Session 011 as precedent for self-work pivot. Assessment direction-determination applied G/O/K/S independently; the counterfactual "does the assessment's OI-001 selection stand if Session 011 did not exist?" is yes — OI-001 is the cleanest G/O/K/S pass among available options regardless of Session 011 precedent. WX-11-4 not activated.

### 12. New Session 012 Watchpoints

- **WX-12-6 (Selvedge-steering-effect):** First-instance track. Session 012 is the first session producing the named methodology; future sessions' self-presentation, brief-authoring, and artefact framing should be watched for over-reliance on textile metaphors, over-accentuation of preservation relative to other mature dimensions (self-hosting; multi-strand), or tacit extension of the metaphor into specifications (e.g., renaming activities, sub-sectioning, watchpoints) beyond its honest scope. Activation trigger: the second session-production artefact or specification that uses textile vocabulary beyond the name itself.
- **WX-12-7 (identity.md scope-creep):** First-instance track. `specifications/identity.md` was created as a deliberately narrow single-purpose file. Activation trigger: any proposal to add mission statements, values, principles, or general identity content beyond the name and its immediate reasoning to this file. The file's own scope section specifies this should go in a separate specification; WX-12-7 watches whether the scope is respected.
- **WX-12-8 (Reopening-conditions monitoring):** Ongoing. The Skeptic's four falsifiability conditions for OI-001 reopening are recorded in `specifications/identity.md`. Future sessions should check at Read/Assess whether any condition has come to hold; the check itself (sessions tracking the conditions) is the monitoring. Activation trigger: any future session that claims one or more conditions is met, or any future session that reopens OI-001 under these conditions.

### 13. Cross-model-deliberations count

Session 012 is the **eighth heterogeneous-participant deliberation** with non-Claude participation (Sessions 005, 006, 007, 008, 009, 010, 011, 012). Of these: **four are required-trigger** (Sessions 005, 006, 009, 011); **four are voluntary** (Sessions 007, 008, 010, 012). The voluntary count now equals the required count for the first time. This is a watchable pattern for any future OI-004 closure deliberation that reviews whether criterion-2's "≥3 required-trigger" bar captures the methodology's actual cross-model discipline correctly.

**Rationale:** Housekeeping consolidation, consistent with Session 005 D-036 / Session 006 D-043 / Session 007 D-049 / Session 008 D-052 / Session 009 D-056 / Session 010 D-059 / Session 011 D-062 closing-accounting patterns. Session 012 is a voluntary-Outsider-no-d023-trigger session; tally-non-advance extends the pattern to four instances (Sessions 007, 008, 010, 012). Session 012 opens zero new formal open issues (WX-12-6/7/8 are session watchpoints, not OIs, per the Session 011 D-061 precedent of recording watchpoints in decisions rather than elevating to OIs unless they name a specific methodology mechanism not covered by existing OIs).

**Rejected alternatives:**

- **Elevate WX-12-6/7/8 to formal OIs.** Rejected. Per D-061 precedent, watchpoints are recorded in decisions; elevation to OI requires a specific methodology-mechanism gap not covered by existing OIs. WX-12-6 and WX-12-7 are steering-effect monitors specific to the Selvedge-naming adoption, appropriately recorded here; WX-12-8 operationalises the OI-001-reopening conditions already recorded in `specifications/identity.md`.
- **Propose a revision to closure-criterion-2 to count voluntary non-Claude inclusion.** Rejected as scope-creep for Session 012 and per Session 007 D-049 / Session 008 D-052 / Session 010 D-059 "wait for a concrete pattern" principle. Four consecutive voluntary-non-advancing sessions is now a pattern; a future criterion-4-articulation deliberation (or a dedicated closure deliberation) is the appropriate venue.
- **Record WX-11-3 novel-data as a new OI.** Rejected. Novel data about an existing watchpoint pattern belongs in that watchpoint's record, not as a new OI. WX-11-3 is a session-level watchpoint recorded in Session 011 D-058 / D-062; Session 012's novel data extends its record as expected.

**Non-Claude participation:** present via D-063's Outsider participation. Voluntary.

---

**End of decisions. Session 012 records three decisions: D-063 (name adoption + identity.md creation), D-064 (OI-001 closure), D-065 (OI state housekeeping + watchpoints). Cumulative decision count after Session 012: 65.**
