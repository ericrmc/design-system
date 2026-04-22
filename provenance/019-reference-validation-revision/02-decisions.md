---
session: 019
title: Decisions — reference-validation.md v1 → v2 Adoption; OI Housekeeping
date: 2026-04-22
status: complete
---

# Decisions — Session 019

**Notice.** Per D-037/D-038/D-039 (adopted Session 006), every decision in a post-adoption session (≥006) carries `**Triggers met:**` and `**Triggers rationale:**` inline. Session 019 is a post-adoption session; decisions below follow the schema.

Session 019 contains **two decisions**: D-078 (adopt R1–R6 revisions to `reference-validation.md` v1 → v2) and D-079 (OI state housekeeping).

---

## D-078: Adopt Session 019 deliberation recommendation R1–R6 — `reference-validation.md` v1 → v2 substantive revision; kernel §7 v4 unchanged; `multi-agent-deliberation.md` v3 unchanged

**Triggers met:** [d016_2, d016_3]

**Triggers rationale:** d016_2 fires (substantive revision to an existing specification in `specifications/` — `reference-validation.md` v1 → v2 per OI-002 heuristic: new normative rejection conditions at §1 C3, new §9 triggers, new L1 two-stage structure). d016_3 fires (the deliberation resolved reasonable-disagreement: four perspectives produced distinct positions on Q1 revise-now-vs-defer, Q5 kernel-§7-preemptive-activation, and Q2 which findings to revise on). No d023_* trigger fires: the adopted outcome does not revise `methodology-kernel.md` (d023_1), does not revise `multi-agent-deliberation.md` (d023_2), does not revise Tier 2 `validation-approach.md` (d023_3), and does not assert an OI-004 state change (d023_4). Session 019 is voluntary non-Claude participation without d023_* trigger firing on adopted decisions, analogous to Sessions 007, 008, 010, 012, 013 precedent.

**Decision:**

The operator ratified the six recommended revisions R1–R6 as synthesised in `01-deliberation.md` §5. Adopted spec changes:

1. **R1 — `reference-validation.md` §1 C3 restructure.** Replaced the single-paragraph test with a two-stage operational test: (a) thin-prompt contamination canary (per §4 L1a); (b) full-constraint saturation test (per §4 L1b) with three rejection conditions — (1) >30% shared 5-gram token overlap, (2) zero-tolerance verbatim distinctive-phrase / section-heading / named-label emission, (3) cross-family retrieval asymmetry. Added explicit acknowledgment that stage (a) is necessary-but-not-sufficient per WX-18-2.

2. **R2 — `reference-validation.md` §1 Flagged tension strengthening.** Preserved Session 014 Skeptic Q1 text; added annotation citing Session 018 empirical materialisation (WX-18-3); added explicit statement that threshold-tuning cannot resolve the tension; pre-committed that a second structurally-different-domain rejection fires §9 trigger 7.

3. **R3 — `reference-validation.md` §4 L1 two-stage restructure.** Replaced single-paragraph L1 with L1a (thin-prompt canary, known-limitation acknowledged per WX-18-2) + L1b (full-constraint saturation test; mandatory for seal; preserves prompts / model families / outputs in seal record).

4. **R4 — `reference-validation.md` §4 L3 pre-seal interpretation.** Preserved existing L3 Cell 3 language; added Session 019 revision clause: pre-seal cross-family divergence at §1 C3 stage (b) or §4 L1b is a contamination diagnostic, not design evidence; **a candidate that fails C3 is not rescued by cleaner output from another family**; design evidence interpretation requires the candidate to have first passed L1.

5. **R5 — `reference-validation.md` §9 trigger strengthening.**
   - Trigger 5 sharpened: "gap-surfaced non-pass" explicitly includes pre-seal Cell 1 rejections; Session 018 counts as exercise 1.
   - Trigger 6 extended: added "or §1 C3 narrowed from cross-family contamination screening to family-conditional screening without explicit concurrent narrowing of claim language and labels" (blocks a specific laundering path — using non-Claude Produce as an escape hatch for Claude-saturated references).
   - New trigger 7: two pre-seal C3 rejections in structurally-different domains with verbatim or near-verbatim reproduction by the Cell 2 Produce-default family activate the Session 014 Skeptic "provisional substitute" minority warrant as a required kernel §7 revision consideration and re-open OI-016 to Open state pending that consideration.

6. **R6 — `reference-validation.md` §10 preserved-minorities update.** Three Session 014 minorities preserved verbatim with Session 019 annotations; three new Session 019 minorities added with operational warrants:
   - Session 019 Minimalist defer-revision minority (warrant: Session 020 Cell 1 pass would vindicate premature-amendment claim).
   - Session 019 Skeptic preemptive-activation minority (warrant: second structurally-different-domain rejection on §9 trigger 7 fire would vindicate broad-reading).
   - Session 019 Reviser asymmetry-probe minority (warrant: future Session 020+ inability to judge WX-18-5 pattern due to absence of probe records would vindicate).

**Version preservation.** `reference-validation.md` v1 preserved at `specifications/reference-validation-v1.md` with frontmatter `status: superseded`, `superseded-by: reference-validation.md (v2)`. Active `specifications/reference-validation.md` carries v2 frontmatter.

**NOT adopted (4-of-4 or 3-of-4 cross-family against in the deliberation):**

- Kernel §7 v4 revision to use "provisional substitute" phrase or add mandatory-dissent clause. 3-of-4 cross-family (Reviser + Minimalist Claude + Outsider non-Claude) read the Session 014 Skeptic §10 warrant narrowly: the operational trigger is label-discipline collapse (§9 trigger 6), not empirical vindication of the §1 tension. Skeptic's broad-reading minority preserved in revised §10. n=2 structurally-different-domain rejection will automatically activate kernel §7 revision consideration per new §9 trigger 7 — the Skeptic's concern is operationalised as a pre-committed future trigger.

- `multi-agent-deliberation.md` v3 Cell 2 Produce default revision. 4-of-4 cross-family against adopting a WX-18-5 default change on n=1 (Kerth is in one domain — agile retrospectives; one reference's saturation does not demonstrate a family-level pattern across domains). Strongest convergence of the session. WX-18-5 remains as watchpoint; Session 020+ data required before this question can be re-opened.

- §4 L1 asymmetry-probe clause per Reviser R2. 3-of-4 (Minimalist + Skeptic + Outsider) held that watchpoint WX-18-5 suffices on n=1 and that the probe clause risks over-reading into `multi-agent-deliberation.md` territory prematurely. Reviser's position preserved as Session 019 minority in revised §10.

- §1 "Known structural limit" standalone subsection per Skeptic R3. Reviser's smaller-scope strengthening of the existing Flagged-tension paragraph adopted instead; Skeptic's narrow-sweet-spot content is preserved via the R2 strengthening's explicit "threshold-tuning cannot resolve the tension" clause and via the Session 019 Skeptic preemptive-activation minority in §10.

- §7 mechanism-failure text edit per Reviser R4 (pre-seal rejection disambiguation). 3-of-4 against editing §7. Disambiguation content captured here in D-078's triggers rationale: Session 018's Cell 1 C3 rejection is the mechanism operating correctly, not a mechanism failure; it counts toward §9 trigger 5 and (on recurrence in a different domain) toward new §9 trigger 7.

**Why:** Session 018's empirical first-exercise finding (Claude-verbatim reproduction of the Kerth Prime Directive from a constraint statement that did not name it) was a single data point but an analytic one — the thin canary is structurally a proper subset of the full constraint statement, and the verbatim emission at ~94% overlap is not a noisy signal. Three of four perspectives (two Claude + one non-Claude cross-family) converged that tight-scope revision was warranted now: tighten C3 to a two-stage test with expanded rejection conditions; make L1 match; name cross-family divergence at pre-seal as diagnostic-not-design-evidence (blocking the accommodation path of escaping to the non-Claude family); strengthen §9 triggers to pre-commit responses to observed patterns.

The Skeptic's adversarial push for kernel §7 revision preemptive-activation was considered seriously (Q5). The majority's narrow-reading of the §10 warrant was adopted, but with the Skeptic's concern operationalised as new §9 trigger 7. This honours the Session 014 Skeptic's preserved minority warrant on its own terms (label-discipline collapse is the specific activator) while giving the Session 019 Skeptic's broad-reading a pre-committed future activation path. The Skeptic's broad-reading position is preserved as first-class Session 019 minority.

All six revisions passed both per-perspective and aggregate anti-laundering checks (synthesis §8). Nothing in the adopted text lowers a threshold, drops a check, softens a mechanism-failure criterion, or widens a label. Every edit is either an extension of a rejection surface, a strengthening of a re-opening trigger, or a preservation of dissent.

### Rejected alternatives (preserved)

- **Rejected: defer all revision to n=2 exercise evidence** (Minimalist). Preserved as Session 019 Minimalist minority in revised §10 with explicit falsifiability warrant.

- **Rejected: revise kernel §7 now to adopt "provisional substitute" + mandatory-dissent clause on broad-reading of §10 warrant** (Skeptic). Preserved as Session 019 Skeptic minority with warrant activating on §9 trigger 7 fire.

- **Rejected: add §4 L1 asymmetry-probe clause** (Reviser). Preserved as Session 019 Reviser minority.

- **Rejected: add §1 standalone "Known structural limit" subsection** (Skeptic R3). Content folded into R2 strengthening.

- **Rejected: edit §7 mechanism-failure text** (Reviser R4). Disambiguation captured in decision provenance only.

### What remains open

- Cell 2 execution on a passing C3 candidate. Session 018 did not reach Cell 2; no post-revision Cell 1 attempt has yet been made.
- Whether `multi-agent-deliberation.md` v3's Cell 2 Produce default warrants revision per WX-18-5 and accumulated §4 L1b rejection data from future sessions.
- Whether OI-016 should transition from Resolved-provisional based on first Cell 3 verdict (pass or fail, not pre-seal rejection).
- Whether `methodology-kernel.md` §7 should be revised per the Skeptic preemptive-activation minority; pre-committed to activate on §9 trigger 7 fire.

### Pre-commitment

None for Session 020. The operator may steer Session 020 toward: (a) Cell 1 re-attempt with S1 or S2 under the revised two-stage C3; (b) Cell 1 re-attempt with a fresh candidate; (c) shift agenda to OI-004 criterion-4 articulation, OI-015 laundering-gap, first-exercise of H4 application-initialisation, or other priorities.

---

## D-079: OI state housekeeping — OI-004 tally unchanged at 6-of-3 (voluntary non-advancing); OI-016 unchanged; five concrete Outsider-sourced contributions recorded; OI-002 gains eighth data point

**Triggers met:** [none]

**Triggers rationale:** No kernel modification (no d016_1, d023_1). No additional specification revision beyond D-078's `reference-validation.md` revision (no d016_2 beyond what D-078 already carries). No reasonable-disagreement deliberation (no d016_3 in this housekeeping decision itself — it records consequences of D-078 without new deliberative content). Not operator-marked load-bearing (no d016_4). No OI-004 state change (no d023_4 — Session 019 is voluntary non-Claude inclusion without d023_* trigger firing on D-078's adopted decisions; tally unchanged at 6-of-3). No `multi-agent-deliberation.md` revision (no d023_2). No `validation-approach.md` Tier 2 revision (no d023_3). Follows D-065 / D-068 / D-077 precedent for OI housekeeping declaring `[none]` when the session's substantive decision (D-078) carries the triggers and the housekeeping decision records consequences only.

**Decision:**

1. **OI-004 tally unchanged at 6-of-3.** Session 019 included non-Claude participation (Outsider = OpenAI GPT-5.4 via `codex exec`, session id `019db44c-e6a3-7140-8aee-a0fdc1d44877`, reasoning effort xhigh, 26,112 tokens) with a full D-024 manifest. However, none of D-078's triggers include a d023_* clause: D-078 revises `reference-validation.md` (not in D-023's enumerated list of kernel / `multi-agent-deliberation.md` / Tier 2 `validation-approach.md` revisions) and does not assert an OI-004 state change. Per the strict v3 spec closure-criterion-2 reading and Sessions 007 / 008 / 010 / 012 / 013 precedent, Session 019's deliberation was voluntary non-Claude participation without a required-trigger firing; the sustained-practice tally does **not** advance. Tally remains at 6-of-3.

   This is the **sixth non-advancing non-Claude session** after Sessions 007, 008, 010, 012, and 013. **Voluntary-to-required ratio rebalances from 5:6 (after Session 017) to 6:6** (voluntary advances by 1). The voluntary and required counts are now even for the first time since Session 017.

   **Five concrete Outsider-sourced contributions materially shaped adopted Session 019 content** (criterion-3 data points):

   1. **§4 L3 "not rescued by cleaner output from another family" pre-seal interpretation** — no Claude perspective framed the anti-laundering-from-cross-family-asymmetry path at this specific §4 L3 placement. Reviser and Skeptic placed cross-family asymmetry in §1 C3 as a rejection condition (which was also adopted); only the Outsider named the §4 L3 downgrade that blocks the "pass only when one family clean" accommodation path.

   2. **§9 trigger 6 extension** — the addition "or §1 C3 narrowed from cross-family contamination screening to family-conditional screening without explicit concurrent narrowing of claim language and labels" closed a specific laundering route (using non-Claude Produce as an escape hatch for Claude-saturated references) that no Claude perspective explicitly named at this precision.

   3. **§1 C3 two-stage structural clarity with canary-as-early-warning-only framing** — Reviser R1 and Skeptic R2 also proposed two-stage structures, but Outsider's framing ("Canary survival is early-warning only and does not satisfy C3 on its own") was the clearest supplementary-vs-decisive formulation; adopted content in §1 C3 and §4 L1 uses this framing.

   4. **Explicit naming / distinctive-sequence recovery as standalone rejection basis** — Outsider's Q3 draft explicitly listed "explicitly names the reference" and "reproduces its distinctive labelled sequence" as rejection triggers separate from percentage overlap. Reviser R1(2) proposed similar zero-tolerance phrasing; the adopted C3 condition (2) draws on both.

   5. **Screening/confirmatory-mismatch framing** (marked `[synth]` from testing methodology) — clarified why WX-18-2 is a structural observation entailed by the canary's construction rather than an n=1 anomaly. This framing informed synthesis §2 Q1's cross-family weighting and justified the 3-of-4 revise-now adoption against the Minimalist's statistical-deferral argument.

   **Cumulative criterion-3 data points across Sessions 005–019: 50** (45 through Session 017; 5 added in Session 019). Criterion 4 (articulated definition of "substantively different training provenance") remains unmet.

2. **OI-016 unchanged: Resolved — provisionally addressed pending first-exercise.** §9 re-opening triggers evaluated against Session 019's actions:
   - Trigger 1 (three-core-properties test failure): NOT activated. No Cell 2/3 run; Blindness/Stageability/Discriminability not tested.
   - Trigger 2 (counterfactual-probe inversion): NOT activated.
   - Trigger 3 ("too fast" pattern): NOT activated.
   - Trigger 4 (noise-floor inversion): NOT activated.
   - Trigger 5 (three-consecutive-gap-surfaced-non-passes): **monitoring**. Session 018 was exercise 1; Session 019 is a spec-revision session, not an exercise attempt. Trigger-5 counter remains at 1.
   - Trigger 6 (label discipline / scope softening): NOT activated. Kernel §7 not revised; no softening of anti-substitution clause; no `validation: reference-validated` artefact used without qualification. D-078's revisions are strengthenings (extended rejection conditions, new triggers), not softenings. The extended trigger 6 text itself (per D-078 R5) does not fire on its own adoption — it specifies a *future* condition for activation.
   - Trigger 7 (two structurally-different-domain rejections): NOT activated. Session 018's D2 rejection is one data point; trigger 7 requires a second.

   OI-016 remains Resolved-provisional with the updated re-opening trigger text (now seven triggers rather than six; see revised §9).

3. **OI-002 gains eighth data point (substantive revision).** `reference-validation.md` v1 → v2 is **substantive** per the OI-002 heuristic — adds new normative rejection conditions (verbatim-phrase zero-tolerance at §1 C3 condition (2); cross-family retrieval asymmetry at §1 C3 condition (3)), new §9 re-opening trigger (trigger 7), and new L1 two-stage structure with preserved-record obligation at L1b. File-level version preservation applied per discipline; v1 at `specifications/reference-validation-v1.md` with `status: superseded`, `superseded-by: reference-validation.md (v2)`; v2 at canonical path with `supersedes: reference-validation-v1.md`. No OI-002 formal heuristic update this session; the observation that the heuristic continues to hold stable is recorded. The n=3 narrow-single-purpose-spec-creation pattern (identity.md + reference-validation.md + engine-manifest.md) noted by Session 017 is unchanged by Session 019 (no new spec created).

4. **OI-007 count unchanged at 12.** No OI opened; no OI resolved. All Session 019 watchpoint-level findings are carried at the spec's §10 preserved-minorities (three new Session 019 minorities with operational warrants) rather than opened as new OIs — this continues Session 015/016/018 precedent of preferring spec-internal annotations over new OIs when the annotation can carry the operational warrant. OI-007 scaling pressure continues to argue against redundant OI proliferation.

5. **OI-005, OI-006, OI-008, OI-009, OI-011, OI-012, OI-013, OI-014, OI-015 unchanged.**

   - OI-009 G/O/K/S evaluation for Session 019's self-work: passes (G) the revisions serve the methodology's external-artefact evidence claim under user-unavailability; passes (O) — Session 019 narrows the action space by adopting specific spec revisions that extend rejection surfaces; passes (K) — external reader would see the methodology responding to first-exercise empirical evidence with traceable revisions and preserved minorities; passes (S) — Session 019 resolves the "Session 018 findings pending revision deliberation" standing condition. OI-009 does not activate.

6. **D-072 status:** unchanged (discharged per Session 018 D-076 §4). Session 020+ open under no default pre-commitment.

**Why:** D-079 records the OI consequences of D-078 and verifies that no OI re-opening triggers activate. The pattern is conservative and honest: the spec revision strengthens re-opening machinery without asserting any state change beyond what D-078's own actions warrant. Session 019's non-Claude participation was voluntary (no d023_* trigger fires on D-078); recording the five concrete Outsider contributions as criterion-3 data points without advancing the criterion-2 tally preserves criterion integrity per Sessions 007/008/010/012/013 precedent.

### Rejected alternatives (preserved)

- **Rejected: advance OI-004 tally to 7-of-3 on the grounds that the deliberation was pre-declared D-023-triggering.** Pre-declaration is not a trigger firing. The adopted outcome (D-078) does not fire any d023_* clause. Tally advancement requires actual trigger firing on the adopted decision, per strict v3 reading and precedent.

- **Rejected: open a new OI for "reference-validation post-v2 first-exercise re-attempt."** Watchpoint-style tracking via §10 preserved minorities (Minimalist, Skeptic, Reviser Session 019 minorities) with operational warrants suffices per OI-007 scaling pressure.

- **Rejected: re-open OI-016 based on Session 018's pre-seal rejection + Session 019's substantive revision.** The pre-seal rejection is §9 trigger 5 territory (counter at 1); the substantive revision is a strengthening, not a §9 trigger 6 softening. No re-opening trigger fires.

### OI state after this decision

- **Open issues: 12 active** (OI-002, OI-004, OI-005, OI-006, OI-007, OI-008, OI-009, OI-011, OI-012, OI-013, OI-014, OI-015). Unchanged from Session 017 / 018 close.
- **Resolved: 5** (OI-001, OI-003, OI-010, OI-016 provisional, OI-017).
- **OI-004 status:** Closable pending criterion-4 articulation. Tally 6-of-3; voluntary:required 6:6.
- **OI-016 status:** Resolved — provisionally addressed pending first-exercise; now with seven re-opening triggers (§9 of revised spec).
- **New watchpoints opened in Session 019:** WX-19-1 first-class minority record-keeping discipline (see Close §Honest notes); otherwise Session 019 watchpoints are carried at `reference-validation.md` v2 §10 rather than as standalone WX-entries.
