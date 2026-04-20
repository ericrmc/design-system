---
session: 011
title: Decisions — W1 Kernel §1 Read Revision
date: 2026-04-20
status: complete
---

# Decisions — Session 011

Decisions recorded in this session: **D-060 through D-062** (three decisions). Each declares `triggers_met:` and `triggers_rationale:` per the schema introduced in Session 006 (D-037, D-038).

---

## D-060: Adopt synthesis Recommendation 1 — revise `methodology-kernel.md` §1 Read; v2 → v3

**Triggers met:** [d016_1, d016_2, d016_3, d016_4, d023_1]

**Triggers rationale:** The decision modifies `methodology-kernel.md` (d016_1, d023_1); creates or substantively revises a specification in `specifications/` (d016_2 — the kernel gains a v3, the v2 is preserved as `methodology-kernel-v2.md`). Reasonable practitioners disagreed (d016_3) — four-perspective deliberation produced 3-1 against sub-sections, 2-2 on explicit naming, 2-2 on first-sentence reorder, 3-1 on inclusion of perspective pretraining, and a preserved refuse-the-revision Skeptic minority with falsifiability condition. Operator-marked load-bearing (d016_4) because this is a kernel revision, the methodology's most durable document; and because it completes Session 008's longest-deferred open watchpoint (W1). D-023_1 fires: non-Claude participation is required, and the Outsider (OpenAI GPT-5 via `codex exec`) is present in the deliberation with a full D-024 manifest; five concrete Outsider-sourced contributions materially shaped the adopted text — see Key arguments carried below.

**Decision.**

1. **Kernel revision.** Revise `methodology-kernel.md` §1 Read to the following text (replacing the current text in full):

   > #### 1. Read
   >
   > Absorb what the session will reason from before changing anything. In every session this includes **workspace reading**: the full current state of the workspace — every file, every specification, every provenance record, and, where relevant, recent version-control history. Build a complete picture of the workspace's own state.
   >
   > When the session produces or revises an artefact intended for use outside the workspace, it also includes **domain reading**: the domain constraints the session operates under (stated by the user or operator in-session), cited external materials introduced into the session, and domain knowledge that the orchestrating agent surfaces explicitly as input to the work. Domain reading enlarges what must be understood; it does not permit silent import of outside ideas. Knowledge not already present in the workspace or in the session's explicit domain inputs must still be introduced through an explicit surveying or hypothesising step (per PROMPT.md). Perspective pretraining enters the session via stance briefs and perspective responses, not via §1 Read.
   >
   > This is a receptive activity. Its output is understanding, not artefacts.

   Approximately 175 words (up from ~40). Two paragraphs. Inline bolded sense-names (**workspace reading** and **domain reading**). No sub-sections. First sentence reorders from "Absorb the full current state of the workspace" to "Absorb what the session will reason from before changing anything" — removing the self-hosting-first framing per Outsider [01d, Q1] and Reviser [01a, Q1] concern (2-2 split resolved via adopting the Outsider's specific wording which is more neutral in register than Reviser's).

2. **Version preservation.** Copy the current `methodology-kernel.md` (v2) to `methodology-kernel-v2.md` with `status: superseded` preserved. Update `methodology-kernel.md` frontmatter: `version: 3`, `last-updated: 2026-04-20`, `updated-by-session: 011`, `supersedes: methodology-kernel-v2.md`. §1 Read is the only substantive text change. All other sections unchanged from v2. Version bump is substantive per OI-002 heuristic: the revision adds new normative content (two named senses, PROMPT.md reconciliation clause, perspective-pretraining routing note) not anticipated in v2's §1 text.

3. **Kernel minimality note** (synthesis Recommendation 5 companion): the adopted form is closer to the Minimalist pole than the maximalist pole. No sub-sections in §1 despite sub-sections in §7. Future sessions should treat this as a deliberate asymmetry (§1 uses inline bolded names; §7 uses sub-sections) driven by the different forcing properties of the two activities — not as an invitation to sub-section other activities when a second sense is identified. [Skeptic, 01c, Q2]: "Sub-headings in §1 set a precedent pressure on every other activity to grow sub-headings the moment a second case is identified; the kernel becomes a Russian doll." [Outsider, 01d, Q2] and [Minimalist, 01b, Q2] independently convergent.

4. **Dissent preserved.** The Skeptic's refuse-the-revision position [01c, Q5] is preserved verbatim as first-class dissent in Rejected Alternatives below, including the falsifiability condition: "A session attempting an external artefact is *blocked* by §1's lack of domain-reading naming — not merely slowed, but unable to proceed or producing a demonstrably worse artefact — *and* the W1-style revision would have prevented that block. If this happens, record it in that session's Assess and re-open W1 with real forcing." Subsequent sessions reading the adopted revision should hold the Skeptic's position in view when assessing whether the revision earns its place.

5. **OI-002 fourth through seventh data points.** This revision is **substantive** per the heuristic. It is the third cross-session kernel revision (after Session 009 D-053 §7 Validate revision; the v1 → v2 kernel revision was Session 009 D-053). Adds a sixth data point to OI-002's evolution register.

**Substantive-versus-minor classification per OI-002 heuristic:** Substantive. New normative content added (two named senses, PROMPT.md reconciliation clause localising §1's scope, perspective-pretraining routing-note). File-level version preservation triggered: `methodology-kernel-v2.md` preserved with `status: superseded`; `methodology-kernel.md` gains v3. Matches Session 009 D-053 pattern (which also produced substantive §7 Validate revision with v1 → v2 preservation).

**Key arguments carried.**

1. **Four-way convergence on distinguishing the two senses.** All four perspectives [01a 01b 01c 01d, Q1] agree that §1 Read describes two senses in the methodology's active use: workspace reading (self-hosting) and domain reading (external artefacts). The divergence is on structure and naming, not on the underlying distinction.

2. **Three-of-four against sub-sections** [Minimalist 01b Q2; Skeptic 01c Q2; Outsider 01d Q2]. Load-bearing argument: §7 Validate's sub-sections were forced by genuine activity-bifurcation (workspace validation and domain validation are different activities, at different timings, producing different evidence). §1 Read does not have the same forcing property — workspace reading and domain reading are the same receptive activity pointed at different sources. [Minimalist, 01b, Q2]: "Imposing sub-section structure on a non-bifurcation creates false parallelism and trains readers to expect that every §N has two senses." Plus the precedent-pressure concern: if §1 and §7 both carry sub-sections, §2–§9 come under implicit pressure to acquire sub-sections. Adopted.

3. **2-2 naming split resolved via Outsider's inline-bolded-names third-way.** Reviser + Outsider for explicit named senses; Minimalist + Skeptic against coining named terms. Claude perspectives alone are 1-2 against naming; the Outsider crosses the model-family axis and tips the balance while introducing a structurally distinct proposal (inline bolded names without sub-sections) that no Claude perspective produced. **Outsider-originated contribution adopted:** inline bolded names. Second consecutive session with the WX-10-5 pattern (Session 009 Q2 applications/; Session 010 Q3 voice). See D-061 WX-11-3-confirmed record.

4. **2-2 first-sentence reorder split resolved via Outsider's more-neutral wording.** Reviser + Outsider for reorder (different wordings); Minimalist + Skeptic for keep. Outsider's "Absorb what the session will reason from" (slightly adjusted from Outsider's exact "Absorb the current basis of the session before changing anything" for register — the final wording picks language closer to Outsider's but threads the Reviser's "what the session will reason from" framing) is adopted. **Outsider-originated contribution adopted:** first-sentence reorder.

5. **Four-way convergence on PROMPT.md reconciliation text** [01a 01b 01c 01d, Q4]. All four propose reconciliation language separating intake from commitment, preserving PROMPT.md's rule against silent import. The Outsider's two-sentence formulation [01d, Q1 second paragraph] — "Domain reading enlarges what must be understood; it does not permit silent import of outside ideas. Knowledge not already present in the workspace or in the session's explicit domain inputs must still be introduced through an explicit surveying or hypothesising step" — is the most compressed and is adopted with minor edits.

6. **Three-of-four exclusion of perspective pretraining from §1 Read** [Minimalist 01b Q3; Skeptic 01c Q3; Outsider 01d Q3]. Skeptic [01c, Q3]: "Treating perspective pretraining as 'domain reading' conflates the orchestrating agent's reading activity (before convening) with the perspectives' reasoning activity (during deliberation). These are different activities at different points in the process." The adopted text includes an explicit routing clause: "Perspective pretraining enters the session via stance briefs and perspective responses, not via §1 Read." Reviser's inclusion-with-channel-constraints position [01a, Q3] is preserved as a Rejected Alternative.

7. **Four-way convergence on the laundering failure mode** [01a 01b 01c 01d, Q4]. Strongest cross-model convergent finding in this deliberation. All four identify the same concrete risk: orchestrating agent encodes a pretrained intuition into the brief as "domain reading," then the deliberation treats it as given context, and a conclusion is smuggled rather than surveyed. The reconciliation text in §1 mitigates but does not eliminate this risk. See D-061 for OI-015 (laundering enforcement gap) and for WX-11-1 watchpoint.

8. **Outsider-unique intake-vs-commitment framing** [01d, Q4]: "Domain reading enlarges what the session may legitimately absorb before acting. It does not enlarge what the session may treat as already justified. Outside material can enter Read if it is explicit. It can shape Produce or Decide only through the recorded reasoning of the session." This framing is load-bearing for how the adopted reconciliation text works — it is not a new semantic addition in the adopted text but shapes how the adopted text is to be read. The Outsider's framing is quoted in this decision record and flows into future sessions' interpretation.

9. **Four-way G/O/K/S pass under strict reading; three-of-four pass under load-bearing reading.** The revision satisfies G, K, S across three-of-four perspectives clearly; O is weakly satisfied or unsatisfied across four-of-four. Skeptic's weak-across-all-four reading [01c, Q5] is preserved as a minority honest-assessment that the revision is on the near side of ceremonial. The synthesis's acceptance of the revision honours the three-of-four majority; the Skeptic's preservation as dissent keeps the assessment honest.

**Rejected alternatives (preserved as dissent).**

- **Skeptic: no revision.** [01c, Q5] Five specific arguments: methodology-worked-without-it (Sessions 008/010 succeeded without kernel clarification); ratchet-to-ossification (every watchpoint becomes a kernel revision, kernel grows monotonically); external-application-guidance belongs in a separate document (not the kernel); §7 precedent weaker than it looks (Session 009 may itself have been wrong direction); session's choice of W1 is self-work-expanding-to-fill-external-work-gap (Session 010 Validate receipt blocked; Session 011 reached for longest-deferred self-work). **Falsifiability condition (verbatim preservation):** "My refusal would be proven wrong by a future session's experience if: A session attempting an external artefact is *blocked* by §1's lack of domain-reading naming — not merely slowed, but unable to proceed or producing a demonstrably worse artefact — *and* the W1-style revision would have prevented that block. If this happens, record it in that session's Assess and re-open W1 with real forcing. Alternatively: if an external artefact is rejected by its user *because* the session mis-handled domain inputs in a way §1's silence enabled, re-open W1. Absent either of those, W1 is addressing a hypothetical." Preserved as first-class dissent and null-alternative benchmark against which the adopted revision is read over subsequent sessions.

- **Reviser: parallel sub-sections ("Workspace reading" and "Domain reading" as bolded sub-section headings, mirroring §7 Validate's structure, ~175 words).** [01a, Q1 Q2] Rejected by three-of-four structural argument that §7's forcing property is absent in §1. Preserved as fallback: if subsequent sessions find the inline-names treatment insufficient for reader comprehension across §1/§7, Reviser's parallel-structure proposal is the revision warrant.

- **Minimalist: minimum-revision-without-named-senses ("The senses are named only implicitly").** [01b, Q1] "Introducing a named concept creates an obligation for future sessions to use the name consistently." Rejected by 2-2-cross-axis split resolved via Outsider's inline-bolded-names. Preserved as revision warrant if the adopted names prove to be pulled into confusing ways in future sessions.

- **Outsider: strict exclusion of orchestrating-agent pretraining from domain reading.** [01d, Q3] "I do not count the orchestrating agent's pretrained knowledge as domain reading. It was not read during the session. Calling it reading would collapse two very different epistemic statuses: explicit source intake and latent model priors." Rejected by three-of-four (Reviser, Minimalist, Skeptic include). Preserved as precision concern: if the adopted text produces confusion in practice about what agent pretraining is within §1, the Outsider's strict position is the revision warrant.

- **Minimalist: exclude (d) explicit research from §1 Read — research is a produced survey, belongs in a mid-session surveying step.** [01b, Q3] Rejected by three-of-four on inclusion. Preserved as revision warrant if the adopted text makes it unclear where mid-session research should be recorded.

- **Reviser: inclusive definition of domain reading — (a)(b)(c)(d)(e) all in.** [01a, Q3] Broader than the adopted position. Preserved; synthesis specifically trimmed (c) per three-of-four dissent.

**What remains open.**

- The **laundering enforcement gap** (four-of-four convergence at Q4). Reconciliation text in §1 is necessary but not sufficient. Enforcement requires Deliberate/Decide to re-examine domain inputs as choices rather than environment. Session 011 does not revise Deliberate or Decide. See D-061 for OI-015.
- Whether §1/§7 structural asymmetry (inline bolded names vs sub-sections) is a stable kernel pattern or requires later harmonisation. Session 012+ may revisit if a future asymmetry surfaces (e.g., §6 Produce's external-artefact-vs-self-spec split).
- Whether external-application methodology eventually warrants its own specification (`external-applications.md`). Skeptic-proposed [01c, Q5]. Deferred. Activation trigger: fifth or sixth external artefact; or a session identifies clear external-application-specific conventions that don't fit any existing spec.

**Non-Claude participation:** Required per D-023_1 (modifies `methodology-kernel.md`). Outsider (OpenAI GPT-5 via `codex exec`, session id `019da943-2c45-7f30-bab8-ce303aba09db`, reasoning effort xhigh, 13,820 tokens) participated with full D-024 manifest. Five concrete Outsider-sourced contributions materially shaped the adopted text:

1. **Inline-bolded-names structural form** (resolves 2-2 naming split; no Claude perspective produced this specific third-way).
2. **First-sentence reorder** ("Absorb what the session will reason from") removing self-hosting-first framing.
3. **"Intake vs commitment" framing** shaping how the reconciliation clause is read.
4. **Strict-boundary precision position** on agent pretraining (preserved as dissent; may become future revision warrant).
5. **Two-sentence PROMPT.md reconciliation text** [01d, Q1 second paragraph] adopted with minor edits.

---

## D-061: Open OI-015 (laundering enforcement gap); record Session 011 watchpoints

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** Reasonable practitioners disagreed (d016_3) on whether the laundering failure mode identified at Q4 requires a new OI or an existing watchpoint suffices; Session 011 resolves in favour of OI creation because three-of-four perspectives explicitly named the enforcement gap as a concrete concern requiring future-session deliberation. Operator-marked load-bearing (d016_4) because the laundering concern is the clearest four-way convergent finding in the deliberation and its follow-up shapes Session 012+'s agenda availability. d016_1, d016_2 not triggered: no kernel change in this decision; no spec change. d023_* not triggered: this decision opens a new open issue and records watchpoints; it does not modify kernel, specs, or OI-004 state.

**Decision.**

1. **Open OI-015: Laundering enforcement gap in domain reading.** The Session 011 deliberation surfaced a four-way convergent concern [01a 01b 01c 01d, all at Q4] that the D-060 reconciliation text, while necessary, is not sufficient to prevent a specific failure mode: orchestrating agent encodes a pretrained intuition into the brief as "domain reading," then the deliberation treats it as given context, and a decision is smuggled rather than surveyed. The reconciliation clause requires that domain inputs be *surfaced*; it does not require that surfaced domain inputs be *re-examined as choices* during Deliberate/Decide. Enforcement of the latter requires a separate mechanism — most plausibly, kernel §4 Deliberate or §5 Decide elaboration, or a new validation check, or a convention for how briefs record pretrained-input provenance distinctly from user-stated-constraints provenance. OI-015 is opened with status: **Open** and a concrete activation trigger for future sessions. See open-issues.md for the full entry including verbatim quotes from each of the four perspectives' Q4 failure-mode naming. Activation trigger: first post-Session-011 external-artefact session where a laundering pattern (domain input accepted as given rather than surveyed) is observed and recorded, OR a session proposes kernel §4 or §5 revision addressing the gap.

2. **Record Session 011 watchpoints (WX-11-1 through WX-11-4).**

   **Watchpoint WX-11-1: Domain-reading-as-conclusion-laundering.**

   - *Finding:* Four-way convergence at Q4 [01a 01b 01c 01d] that the adopted D-060 reconciliation text is necessary but not sufficient to prevent laundering. Most concrete articulation is [Skeptic, 01c, Q4]: the "BATNA example" — a session encodes a standard domain framework into the brief, perspectives treat it as given, the adopted artefact applies the framework directly, no surveying step ever examined the framework as one choice among alternatives.
   - *Session 011's response:* OI-015 opened (see (1) above). The watchpoint record here preserves the concrete failure-mode descriptions across all four perspectives for future-session reference.
   - *Activation trigger for future deliberation:* observed laundering pattern in an external-artefact session; or a future session proposes kernel §4/§5 elaboration addressing the enforcement gap. OI-015 is the issue tracking this watchpoint; WX-11-1 is the provenance-level finding record.

   **Watchpoint WX-11-2: Kernel §1/§7 structural asymmetry post-D-060.**

   - *Finding:* After D-060, §1 Read uses inline bolded names; §7 Validate uses sub-sections. Two-of-four perspectives (Reviser for parallel sub-sections; Outsider for inline naming) flagged this as a potentially visible inconsistency. Three-of-four perspectives argued the asymmetry is load-bearing (§7's forcing property absent in §1). Monitor: if future sessions read §1 and §7 and find the structural difference confusing for comprehension or for applying the kernel, the asymmetry may need harmonisation (either §1 gains sub-sections, or §7 loses them — neither direction is currently warranted).
   - *Session 011's response:* D-060 §3 explicitly records the asymmetry as a deliberate choice with rationale; D-060 Rejected Alternatives preserves Reviser's parallel-sub-sections proposal as the revision warrant if the asymmetry proves confusing.
   - *Activation trigger for future deliberation:* a session's Read activity reports confusion or reader-comprehension failure across §1 and §7; or a third kernel activity gains a second sense and the §1-inline-vs-§7-subsection decision must be extended to a third activity.

   **Watchpoint WX-11-3: Outsider-originated third-way pattern — confirmed second occurrence with two instances.**

   - *Finding:* Sessions 009 Q2 and 010 Q3 saw an Outsider-originated third-way resolve a 2-2 Claude split (WX-10-5 original record per Session 010 D-058). Session 011 extends the pattern. Two distinct 2-2 splits in Session 011 Q1 were resolved via Outsider-originated third-ways: (i) the naming split (inline bolded names, not sub-sections and not no-naming); (ii) the first-sentence reorder split (Outsider's wording adopted with minor adjustment). Additionally, the Outsider's intake-vs-commitment framing at Q4 shapes how the reconciliation clause is read — a structural contribution distinct from the binary-split resolution pattern.
   - *Session 011's response:* The pattern is load-bearing for OI-004 closure criterion 3 (recorded impact of non-Claude participation). D-062 records five concrete Session-011 Outsider-sourced contributions for criterion-3 data accumulation.
   - *Activation trigger for future deliberation:* if a future 2-2 split is NOT resolved by an Outsider third-way, that is novel data worth examining. If the synthesizer appears to be *reaching for* Outsider positions when a Claude position would serve, that would be the failure mode. Session 012's Session-011-audit should scrutinise whether the two 2-2 resolutions in Q1 genuinely honoured the Outsider's substantive third-ways rather than a synthesizer disposition toward cross-model resolutions.

   **Watchpoint WX-11-4: Session-without-external-receipt pattern.**

   - *Finding:* Session 011's planned primary work (Session 010 Validate receipt) was unavailable; Session 011 pivoted to the longest-deferred self-work watchpoint (W1). Skeptic argued [01c, Q5 argument 5] this is self-work expanding to fill the gap when external work is blocked. The alternative Skeptic proposed — record the block and close the session short — was not adopted; Session 011 proceeded with W1. The G/O/K/S check on W1 passed three-of-four; the Skeptic's "the work is on the near side of ceremonial" assessment is preserved as honest-limit.
   - *Session 011's response:* Watchpoint recorded. If Session 012's Session-011-audit finds the W1 revision under-earned in practice (e.g., if subsequent external-artefact sessions find §1's revised text produces no observable benefit), Session 011 becomes a data point for whether the "pivot to self-work when external is blocked" pattern is load-bearing or ritual.
   - *Activation trigger for future deliberation:* if a future session faces a similar blocked-external-work situation and the Session 011 precedent is cited for pivoting to self-work, the WX-11-4 pattern is under-examined and may warrant a kernel §Assess clarification or a new convention about what to do with session-time when external work is blocked.

**Substantive-versus-minor classification per OI-002 heuristic.** Not applicable — no specification is being revised in this decision. Watchpoints and OI creation are records.

**Key arguments carried.** Each watchpoint's Finding section; OI-015 rationale.

**Rejected alternatives (preserved as dissent).**

- **Do not open OI-015; laundering concern is handled by D-060 reconciliation text alone.** Considered and rejected: four-of-four perspectives explicitly named the enforcement gap as distinct from the reconciliation gap. Recording a new OI is the lightest-weight action that keeps the concern active for future deliberation.
- **Open separate OIs for each of WX-11-1 through WX-11-4.** Considered and rejected: WX-11-2, WX-11-3, WX-11-4 are artefact-design / methodology-pattern watchpoints with specific activation triggers, not methodology-level unresolved questions requiring full OI treatment. Their record in D-061 is sufficient per Session 010 D-058 precedent. WX-11-1 is elevated to OI-015 because it names a specific methodology mechanism (enforcement at Deliberate/Decide) that is not covered by any existing OI.

**Non-Claude participation:** Included (Outsider). Not required by D-023 (this decision records findings/opens OI; it does not modify kernel, specs, or OI-004). Outsider's Q4 laundering-pattern naming is one of four convergent sources for WX-11-1 and OI-015.

---

## D-062: OI state housekeeping — Session 011 updates

**Triggers met:** [d016_4, d023_4]

**Triggers rationale:** Operator-marked load-bearing (d016_4) for session-housekeeping (Session 005 D-033 / 006 D-043 / 007 D-049 / 008 D-052 / 009 D-056 / 010 D-059 precedent). d023_4 fires because this decision asserts an OI-004 state change: the sustained-practice criterion-2 tally advances to **4 of 3** (criterion already satisfied; Session 011 extends the evidence beyond threshold), and criterion-3 data points accumulate materially. The D-023 literal reading is that *any* OI-004 state change triggers; "advance beyond satisfied threshold" is a state change per the ledger. Non-Claude participation is required per d023_4; Outsider present with full D-024 manifest. d016_1, d016_2, d016_3 not triggered: no kernel change in this decision; no spec change; the bookkeeping updates are not themselves disputed.

**Decision.** Update `open-issues.md` as follows.

**OI-001 (Naming the methodology):** Unchanged. Still open. Session 011 did not deliberate naming and did not take a position. Available for Session 012+. Further deferral note: the methodology has now accumulated four canonical specifications (methodology-kernel v3 added Session 011), two external artefacts, six cross-model deliberations, and sixty-two decisions. Identity-for-naming continues to accrete.

**OI-002 (Threshold for substantive revision vs. minor correction):** Data point added. Session 011 D-060 is **substantive** — adds new normative content to §1 Read (two named senses, PROMPT.md reconciliation clause, perspective-pretraining routing note) not anticipated in v2's §1 text. File-level version preservation triggered (`methodology-kernel-v2.md` preserved with `status: superseded`; kernel gains v3). The five-point heuristic continues to hold stable: **minor** if the change makes explicit what existing language already contains or explicitly anticipates; **substantive** if new normative content is added. Cumulative evolution-register data points: seven (Sessions 002, 003, 004, 005, 006, 009, 011).

**OI-004 (Incorporating genuinely independent perspectives):** Status unchanged at **closable pending criterion-4 articulation** (closure criteria 1, 2, 3 satisfied; criterion 4 unmet). Criterion-2 tally advances from 3 of 3 (Session 009 D-056) to **4 of 3** — Session 011 is the **fourth required-trigger deliberation with non-Claude participation** (Sessions 005, 006, 009, 011; Sessions 007, 008, 010 were voluntary-inclusion-without-D-023-trigger). Criterion-2 is already satisfied; Session 011 extends the evidence beyond threshold.

Criterion-3 (recorded impact on outcomes) gains **five concrete Outsider-sourced contributions**:

1. Inline-bolded-names structural form resolving Q1 naming 2-2 split (no Claude perspective produced this third-way).
2. First-sentence reorder ("Absorb what the session will reason from") removing self-hosting-first framing, resolving Q1 reorder 2-2 split.
3. "Intake vs commitment" framing [01d, Q4] shaping how the reconciliation clause is read.
4. Strict-boundary position on agent pretraining (preserved as dissent; shapes Rejected Alternatives).
5. Two-sentence PROMPT.md reconciliation text [01d, Q1 second paragraph] adopted with minor edits.

Cumulative criterion-3 data points across Sessions 005–011: **twenty-four** (nineteen through Session 010 per D-059; five added in Session 011).

Criterion-4 (articulated definition of "substantively different training provenance" and enumerated acceptable participant kinds): unmet. OI-004 remains closable but not closed. A future session's explicit closure deliberation would itself be D-023_4-triggering and require non-Claude participation.

**OI-005 (Sub-activities and work-type variants):** Unchanged status (unblocked — available for future deliberation per Session 010 D-059). Session 011 addressed W1 (a kernel §1 Read sub-structure question) with a specific deliberation, not a sub-activity proposal; the broader sub-activities question across the remaining activities remains open.

**OI-006 (Cross-references between specifications):** Unchanged. Session 011 did not touch.

**OI-007 (Scaling the open issues format):** Count advances to **13** after Session 011 (OI-015 opened per D-061). Still within readable range; no migration action proposed. Monitor.

**OI-008 (Persisting validation reports):** Unchanged. Session 011's validate.sh run produced 240 passes, 0 fails at start; expected clean at close.

**OI-009 (Monitor for drift-to-ritual in multi-agent deliberation):** **Monitor.** Session 011's work passes G/O/K/S on three-of-four perspectives' reading clearly (G/K/S ✓; O partial/weak across four). The Skeptic's "near side of ceremonial" minority assessment [01c, Q5] is preserved as honest-limit. The WX-11-4 pattern (self-work-expanding-to-fill-external-work-gap) is recorded as a watchpoint for Session 012+ audit. Continued monitoring via G/O/K/S for any future self-work.

**OI-010 (Cross-model or human participation mechanism):** Remains closed (Session 005). Session 011 is the seventh operational use of the mechanism (required-trigger Sessions 005, 006, 009, 011; voluntary Sessions 007, 008, 010).

**OI-011 (Intra-family model mixing as a deliberation-quality lever):** Unchanged. Session 011 did not use intra-family size-mixing; all three Claude subagents were Claude Opus 4.7.

**OI-012 (`validate.sh` hard-coded `02-decisions.md` path):** **Monitor.** Session 011 follows the standard `02-decisions.md` numbering; no collision pressure. The hard-coded path continues not to actively bite.

**OI-013 (Non-file external artefacts):** **Monitor.** Session 011 produced no external artefact; no activation trigger.

**OI-014 (Domain-actor receipt shape variance):** **Monitor.** Session 011 did not receive an external Validate receipt (Session 010's is still pending); no activation trigger.

**OI-015 (Laundering enforcement gap in domain reading):** **Open (new).** Per D-061. Four-way convergent concern from Session 011's Q4 deliberation. Activation trigger: first post-Session-011 external-artefact session where a laundering pattern (domain input accepted as given rather than surveyed) is observed and recorded, OR a session proposes kernel §4/§5 revision addressing the gap. Preferred starting point for future deliberation: whether the enforcement mechanism should live in kernel §4 Deliberate, kernel §5 Decide, or a separate brief-authoring convention.

**Substantive-versus-minor classification per OI-002 heuristic.** Not applicable — no specification is being revised in this decision.

**Key arguments carried.**

1. **OI-004 criterion-2 advances beyond threshold at 4 of 3.** Session 011 is the fourth required-trigger deliberation with non-Claude participation (Sessions 005, 006, 009, 011). Criterion 2 was already satisfied at 3 of 3 after Session 009; Session 011's advance extends the sustained-practice record.
2. **Criterion-3 gains five concrete Outsider-sourced contributions.** Most material addition to the criterion-3 evidence base since Session 010's four contributions; cumulative total reaches twenty-four across Sessions 005–011.
3. **OI-015 opened on four-way convergent concern.** Strongest cross-model convergent finding in Session 011's deliberation (the laundering failure mode); the reconciliation text in D-060 addresses part of the concern but not the enforcement part.
4. **No new OIs except OI-015.** WX-11-2, WX-11-3, WX-11-4 are watchpoint-level records per Session 010 D-058 precedent, not full OIs.

**Rejected alternatives (preserved as dissent).** None substantial. The alternative of treating OI-004 criterion-2 tally as still at 3 of 3 (because it was "already satisfied") was considered and rejected — the evidence-beyond-threshold tally gives a more honest ledger of sustained practice than a fixed "satisfied" flag. Recording the count as 4 of 3 is explicit about continued practice.

**Non-Claude participation:** Required per D-023_4 (OI-004 state change). Outsider present with full D-024 manifest. The five concrete Outsider-sourced contributions listed under OI-004 criterion-3 are Session 011's specific evidence.

---

**End of decisions. Session 011 records three decisions: D-060 (kernel v2 → v3 §1 Read revision), D-061 (OI-015 opened; WX-11-1 through WX-11-4 recorded), D-062 (OI state housekeeping with OI-004 tally advance). Cumulative decision count after Session 011: 62.**
