---
session: 015
title: Assessment — Session 015 Agenda Shortlist (Post-Session-014 Reference-Validation Mechanism Un-Exercised)
date: 2026-04-22
status: draft — halt for user ratification before proceeding
---

# Assessment — Session 015

## 1. Read (workspace state)

Ran `tools/validate.sh` at session open: **353 pass, 0 fail, 0 warnings**. Sixth consecutive clean run at a session-opener.

Active specifications (6):

- `methodology-kernel.md` v4 (last-updated Session 014, D-069 — §7 Validate revised to name three senses: Workspace, Domain, Reference).
- `workspace-structure.md` v2 (last-updated Session 009, D-054).
- `multi-agent-deliberation.md` v3 (last-updated Session 006, D-041).
- `validation-approach.md` v3 (last-updated Session 006, D-041).
- `identity.md` v1 (created Session 012, D-063).
- `reference-validation.md` v1 (created Session 014, D-069) — **un-exercised**.

Superseded files preserved (8): `methodology-kernel-v1.md`, `-v2.md`, `-v3.md`; `workspace-structure-v1.md`; `multi-agent-deliberation-v1.md`, `-v2.md`; `validation-approach-v1.md`, `-v2.md`.

External artefacts (2 canonical, 1 superseded):

- `applications/008-morning-unfurl/morning-unfurl.md` (Session 008; Domain-validated via `provenance/009-external-validate-receipt/00-validate-user-report.md`).
- `applications/010-household-decision-protocol/house-decision-five-moves.md` v2 (Session 013 revision; v1 Domain-validated; v2 **not domain-validated** per user standing constraint).
- `applications/010-household-decision-protocol/house-decision-five-moves-v1.md` (superseded, preserved).

Open issues: **12 active** (OI-002, OI-004, OI-005, OI-006, OI-007, OI-008, OI-009, OI-011, OI-012, OI-013, OI-014, OI-015). **4 resolved** (OI-001, OI-003, OI-010, OI-016 — OI-016 resolved-provisional per D-070).

Most-recent session context: Session 014 designed and adopted the reference-validation mechanism, revised kernel §7 v3 → v4 substantively, created `specifications/reference-validation.md` v1, moved OI-016 to `Resolved — provisionally addressed pending first-exercise` with six automatic re-opening triggers, and preserved four first-class minorities within the resolution. OI-004 tally advanced 4-of-3 → 5-of-3 (fifth required-trigger deliberation); voluntary-to-required ratio rebalanced 5:5; criterion-3 gained six Outsider-sourced contributions (cumulative 40 across Sessions 005–014). Criterion 4 remains unmet.

## 2. Audit of Session 014 synthesis fidelity

The Session 014 close asked Session 015 to examine four specific questions. New-eyes findings against the raw perspective outputs:

### 2.1 — 3-1 Q3 hand-off-vs-within-session split: genuine honouring of Architect minority?

**Partially. The close's framing overstates the mitigation.**

Architect's raw Q3 position (`01a` lines 67–91) is specific: iteration-within-single-session with three internal roles, because hand-off "introduces session boundaries in the middle of what should be a continuous design feedback loop … the validation signal cannot re-enter the Produce step — it can only trigger a new Produce step in Session N+2, with all the context reconstruction costs that entails." Architect's core structural concern is the **validation-signal-to-Produce feedback path**, not emergent-constraint-release responsiveness.

The adopted sealed three-cell protocol retains Cell 2's up-to-2-internal-iterations. The Session 014 close (`03-close.md`) asserts this "mitigates Architect's continuous-loop concern via Cell-2 iteration budget." Reading the spec (`reference-validation.md` §3 Cell 2): "Up to 2 internal iterations triggered by in-session Validate findings or emergent-constraint-release events."

**Where the close is right.** In-session Validate findings *do* trigger Cell 2 iteration — this is a genuine mitigation of the validation-to-Produce feedback concern *within a session*. Cell 2 does preserve within-session iteration between its internal Produce rounds.

**Where the close overstates.** Cell 2 iteration is bounded at 2 rounds within Cell 2. Cross-session validation signal (Cell 3 verdict) can only re-enter Produce via Session N+2's Cell 2 re-run, which is exactly the hand-off cost Architect named. The "Cell 2 iteration budget" does not address the cross-session feedback loop Architect's Q3 objection pointed at; it addresses within-session iterative responsiveness to emergent constraints and in-session Validate findings, which is a different (though related) concern.

**Operative warrant.** WX-14-2 is correctly scoped: "whether Cell-2-to-Cell-3 hand-off consistently loses design-intent information that continuous-loop would have preserved" — this is the Architect's actual concern, not the close's paraphrased mitigation claim. The minority is preserved with an operative warrant. The close's language just overstates how fully the adopted shape mitigates it.

**Session 015 implication.** If Option A is pursued and Session 016 (Cell 3) produces a verdict that would have prompted a Produce-side design revision, the hand-off cost will be observable as context reconstruction overhead in any Session 017 Cell 2 re-run. Keep this observable explicit in Cell 3 close.

### 2.2 — 2-2 OI-016 disposition split: genuine cross-model+adversarial convergence or synthesiser-reaching?

**Genuine.**

Skeptic Q7 (`01c` lines 146–177) argues with structural force that "reference-validation produces a third kind of evidence, and it is *closer in kind to workspace-validation than to domain-validation*" and that "OI-016 should remain open, flagged as 'provisionally addressed by reference-validation mechanism, with the prior structural concern preserved.'" Explicitly rejects close-as-resolved framing.

Outsider Q7 (`01d` line 760, independently arrived at): "even if this mechanism works, it validates a narrower claim than the old loop did. It can support 'the methodology can derive artefacts that resemble proven solutions under blinded staged constraints.' It cannot honestly mean 'the methodology's new external artefacts work in live domains.'"

The two positions are **independently load-bearing** — Skeptic's framing operates via evidence-kind taxonomy (workspace/domain/reference = three different objects); Outsider's framing operates via claim-scope narrowness. Neither is an echo of the other. Both resist plain-close. Both converge on the operational direction: the OI stays operative in some form, not closed.

The adopted disposition ("Resolved — provisionally addressed pending first-exercise" with six automatic re-opening triggers and four preserved first-class minorities) captures both positions operationally. The synthesis shifted from Architect+Operationalist's close-with-minority to a stronger state-change because the cross-model+adversarial weight was genuine, not synthesiser-reaching.

**Verdict: cleanly honoured.** This is the third occurrence of Skeptic+Outsider alignment against Claude-majority (after Session 010 Q5 and Session 013 Q2/Q6); the pattern is worth continuing to track.

### 2.3 — Kernel §7 v4 scope-statement carrying Skeptic's "provisional substitute" dissent without the word

**Content partially preserved; structural framing rejected. A live question, not settled.**

Skeptic Q5 (`01c` lines 106–122) uses "provisional substitute" as the organising phrase: "Reference validation is a *provisional substitute* for domain validation, usable only when no domain-actor is available and the alternative is producing an artefact without any external check." Skeptic explicitly states (line 118) the language choice is load-bearing: "the language 'provisional substitute' is deliberate: I refuse to let reference-validation be named alongside domain-validation as an equal third pillar, because it isn't one."

The adopted kernel §7 v4 does name reference-validation as a third pillar ("Three senses of validation apply"). The anti-substitution content is captured:

> *Reference validation supplies evidence about the methodology's capacity to derive artefacts under stated constraints. It does not establish that the artefact functioned in its intended use. It does not substitute for Domain validation when a domain-actor is available.*

This preserves Skeptic's operational claim (no intended-use establishment; no substitution when domain-actor available) but rejects the structural framing (equal-pillar vs provisional-substitute). The adopted text treats reference-validation as a distinct sense with scope-caveats; Skeptic wanted it treated as a lesser-standing fallback.

**Load-bearing question for Session 015+.** Whether the scope-statement carries the dissent content *in practice* depends on how the kernel text is read and cited. If "three senses of validation" is the line picked up in external communication and the scope-statement is not, label discipline collapses (OI-016 trigger 6). The Skeptic's framing becomes the preferred revision direction at that point (per the minority's operational warrant in `reference-validation.md` §10).

**Verdict:** reasonable synthesis judgment, but the Skeptic's structural objection is NOT settled — it is parked behind an observable collapse trigger. Session 015 should treat the "provisional substitute" framing as a live minority, especially when composing any external citation of reference-validated artefacts.

### 2.4 — Reference-validation.md §1 eight-criterion list executable as selection guidance

**Executable in principle. Empirical question: whether a candidate pool survives all eight criteria simultaneously.**

Eight criteria summarised:
- C1 Documented solution with auditable provenance (≥12 months old, snapshot committed).
- C2 Constraint-legibility without solution-smuggling.
- C3 Low saturation in common training distributions (non-Claude + independent-Claude constraints-only test, <30% 5-gram overlap).
- C4 Staged-constraint structure (tranche-0 ≤60%, at least 2 emergent tranches, author-documented problem-shape change).
- C5 Domain-legibility to judges.
- C6 Bounded effort (<10K tokens, 1–3 KB constraint statement, one Cell-1 session).
- C7 Representativeness of the methodology's external-artefact claim (movement-sequence / decision-aid / structured procedure / concise specification / checklist).
- C8 Pre-LLM-co-design + falsification-admitting + uncertainty-declared.

**The spec itself flags the central tension** (§1 line 46): C5 (legibility) and C8 (pre-LLM) are in structural tension with C3 (low-saturation). A domain legible to Claude judges pre-dating late 2022 is almost by construction well-represented in pretraining. The contamination canary (L1) and saturation test try to probe around this; the tension is not resolved in spec.

**Executability assessment.**

- *Concrete and testable.* Each criterion specifies what to check (e.g., C3: "both a non-Claude model via `codex exec` and an independent Claude instance each given only the constraint statement"). An agent can act on them.
- *High up-front cost.* The C3 saturation gate alone requires running two constraints-only production tests *before* a case is adopted. If a case fails, the pre-work is wasted. Expected-value selection requires pre-shortlisting candidates likely to survive C3 before formal gating.
- *Pool-survival is the empirical unknown.* Whether N=5 cases can be found within reasonable effort across ≥3 domains with ≥1 difficult-to-contaminate-tail case — as required for methodology-level pass — is only testable by first-exercising.

**Verdict:** §1 is operationally executable; first-exercise will produce the evidence about whether the criteria empty the candidate pool at sustainable rate. The §1 flagged tension itself carries an operational consequence (§8(c) mechanism-failure trigger if pool empties at sustainable rate).

### Overall audit verdict

Session 014 synthesis fidelity is **mostly clean**. Findings:

- **One overstated claim** in the close (2.1: Cell-2 iteration budget mitigating Architect's cross-session feedback concern — it mitigates emergent-constraint-responsiveness, not the cross-session validation-to-Produce loop). The operative warrant WX-14-2 is correctly scoped to the Architect's actual concern, so the minority is not operationally lost; only the close's framing overstates.
- **One live question parked behind a trigger** (2.3: Skeptic's "provisional substitute" structural framing is captured in content but rejected in form; label-discipline-collapse trigger 6 carries it forward).
- **One empirical unknown** (2.4: whether the §1 eight-criterion list empties the candidate pool at sustainable rate is testable only by first-exercising).
- **One clean honouring** (2.2: cross-model+adversarial OI-016 disposition is genuine convergence).

None of these findings require immediate workspace revision. The first (2.1 framing overstatement) is a note for the session-015+ reader; the second (2.3) is already operationalised via trigger 6; the third (2.4) is exactly what first-exercise is for; the fourth (2.2) is a positive confirmation.

## 3. Agenda options considered

Per Session 014 close (D-069 next-session section):

### A. First-exercise of the reference-validation mechanism

**Scope.** Per `reference-validation.md` §3 session shape: Session N = Cell 1 (Curation) + Cell 2 (Produce). Cell 3 (Validation) lives in Session 016. Up to 2 further iteration sessions possible (N+2 Cell 2 re-run, N+3 Cell 3 re-comparison).

**Session 015 would contain:**
- Source a candidate reference case against the eight C1–C8 criteria (WebFetch, pre-shortlisting).
- Run the C3 saturation gate (constraints-only Claude + non-Claude produce, <30% 5-gram test).
- Run the L1 contamination canary (thin prompts to ≥2 model families, reject on spontaneous reference emission).
- Package the sealed case pack: tranche-0 brief, emergent-constraint schedule with release triggers, reference envelope sealed, contamination-audit plan. Commit anti-drift witness hash.
- `brief-gatekeeper.md` at exercise-provenance root.
- If Cell 1 completes within session budget, proceed to Cell 2 Produce: 2–4 methodology-following perspectives, constraint-to-decision trace per round, up to 2 internal iterations.

**Why this option is highest-leverage.**
- The mechanism is un-exercised. Per PROMPT.md ordering: "If the workspace has defined a structure but not yet applied it, the next work is to begin applying it." Reference-validation is the clearest instance of structure-defined-not-yet-applied in workspace history.
- All six OI-016 re-opening triggers require first-exercise data.
- WX-14-1 through WX-14-6 are first-exercise-gated (Cell-2 iteration budget load-bearing? Cell 2→Cell 3 context loss? brief-gatekeeper post-sealing drift? sourcing-session-budget feasibility? methodology-version count reset? label-discipline vs three-pillar framing?).
- The methodology's claim to produce external artefacts is under-evidenced until at least one reference-validation exercise completes. Session 014's mechanism is evidence-paper-only without first-exercise.
- Subsequent agenda items (OI-004 criterion-4, OI-015) can be reframed or deprioritised based on first-exercise observations — advancing A produces information about B, C, D; advancing B/C/D does not produce information about A.

**Open questions requiring user input before Session 015 proceeds to deliberation:**

*Q1. Reference case domain.* `reference-validation.md` §1 C7 requires representativeness of the methodology's external-artefact claim. Existing external artefacts are:
- `morning-unfurl` (movement sequence, 8 moves, supine → close).
- `house-decision-five-moves` v2 (household decision protocol, 5 moves, question-open → close-and-follow-through).

Options:
- *Same-domain adjacent* (another short sequence; another two-person decision protocol; another short structured procedure). Lower domain-variance; stronger C5 legibility; stronger representativeness. Narrower evidence about cross-domain generalisation.
- *Different-domain representative* (e.g., a pre-LLM-era checklist, a published protocol, a documented procedure from a different practice tradition). Broader C7 representativeness; weaker C5 legibility risk; opens the methodology-level cross-domain claim.
- *User-selected.* User picks the reference or pool.

**Proposed default if no steering:** source a candidate pool of 3–5 cases spanning both same-domain-adjacent and different-domain-representative; shortlist 1 for Cell 1 based on C1–C8 evaluation; present shortlist to user for ratification before sealing.

*Q2. Case Steward role independence.* §3 Cell 1 constrains: "Case Steward does not read the reference after sealing." The orchestrating agent in Session 015 is the only Case Steward candidate available absent specific user steering. Independence concerns:
- Same orchestrating agent that Case-Stewards will also (across Sessions 015-016) drive Cell 2 Produce (via multi-agent subagents) and Cell 3 Validation (via multi-agent subagents including non-Claude).
- The agent will see the reference during Case Steward packaging; must not see it again during Produce or Validation roles in subsequent sessions. Enforcement is by commit-discipline and not by mechanical isolation (a limitation).
- `reference-validation.md` §3 allows "one or two Case Stewards (non-Produce, non-Validation)" — suggesting role-separation *across agents*. Within a single orchestrating agent's purview, the separation is temporal (Cell 1 concludes before Cell 2 opens) and artefact-mediated (the sealed case pack is the only information transferred).

**Proposed approach:** the orchestrating agent acts as Case Steward for Cell 1; the reference envelope is committed-but-not-referenced after sealing; Cell 2 subagents receive tranche-0 brief only via brief-gatekeeper.md; the orchestrating agent's own context across sessions is bounded by the committed sealed pack (re-reading only tranche-0 and release schedule, not the sealed reference). Flag this as a known limitation in the exercise's contamination-audit file per §4.L2.

*Q3. Session 015 stop-point.* Two candidate stop-points:
- **(Stop 3a) Cell 1 complete.** Session 015 seals the case pack, halts, commits. Session 016 opens Cell 2 and attempts Cell 3 in succession, or spans Cell 2 + Cell 3 over Sessions 016–017.
- **(Stop 3b) Cell 1 + Cell 2 complete** per §3 default session shape. Session 015 seals and produces; Session 016 opens Cell 3 with three judges including non-Claude.

Stop 3a is more conservative (ratification point between Curation and Produce); Stop 3b follows the spec's default.

**Proposed default if no steering:** Stop 3b (follow spec default), but with an explicit user-ratification halt between the selection-shortlist stage and the seal commit — so the user sees the chosen reference candidate before Cell 1 closes.

**Cost/risk.** Cell 1 alone is substantial work: 3–5 candidate sourcing; C3 saturation tests (2 constraints-only runs per candidate); L1 contamination canaries; tranching with author-documented problem-shape change evidence; sealed pack preparation; anti-drift commit. Running to Stop 3b within one session application is plausible but not guaranteed; Cell 1 alone may be the realistic scope.

### B. OI-004 closure criterion-4 articulation

**Scope.** Deliberate a definition of "substantively different training provenance" and enumerate acceptable participant kinds for cross-model requirements. Would close OI-004 (the longest-standing open issue) if successful. D-023-triggering (would require non-Claude participation).

**Why lower-priority than A.**
- Criteria 1, 2, 3 are satisfied (5-of-3 required-trigger tally; 40 criterion-3 data points). Criterion 4 is a bookkeeping/articulation closure, not a methodology capability gap.
- First-exercise of reference-validation is methodology-capability-gated; criterion-4 articulation is not.
- Formal closure does not unlock new methodology capabilities; it finalises a metadata status.
- OI-004 has accumulated well-structured deferral rationales across Sessions 007-014 without the criterion being a bottleneck in practice.

**Why might still be picked.** If the user is allergic to compounding scope (two uncertain agendas A + C both running in parallel across sessions), picking B is a bounded, defined-scope session of its own that does not compete with A's multi-session arc.

### C. OI-015 laundering-gap deliberation

**Scope.** Session 011 four-way convergent concern: kernel §1 Read reconciliation surfaces domain inputs but kernel §4 Deliberate / §5 Decide do not require re-examination of domain inputs as choices. A pretrained intuition could be laundered through domain-reading and absorbed as given context. Would be D-023-triggering (kernel revision).

**Why lower-priority than A, but higher than B.**
- The reference-validation mechanism adds a new surface where laundering could occur (Produce agent importing reference from pretraining while labelling the action "following the methodology"). The seven-layer defence stack is an operational partial-mitigation; the kernel §4/§5 enforcement question is structurally independent.
- Session 015 option A run concurrently with unaddressed OI-015 means any first-exercise laundering observation has no pre-defined remediation path at the kernel level.
- But: OI-015 remediation at kernel §4/§5 likely requires first-exercise data to design well (abstract laundering-detection rules without operational observations tend to underfit).

**Tactical consideration.** Addressing OI-015 now means Session 015 does a kernel revision without the operational data that would inform it; addressing it after first-exercise means any kernel revision is evidence-informed. The latter is preferable unless first-exercise is blocked.

### D. OI-005 broader sub-activities

**Scope.** Remaining §2 Assess, §3 Convene, §5 Decide, §6 Produce, §8 Record, §9 Close sub-activity deliberation. Sprawling scope, six activities.

**Why lowest-priority.**
- W1 (§1 Read) and W4 (§7 Validate) were each substantial single-session deliberations. Doing six in one session invites the ceremony-without-advance failure mode (OI-009 re-activation risk).
- No operational pressure; no external-artefact session has surfaced a specific remaining-sub-activity gap.
- Best addressed one-activity-at-a-time when specific pressure surfaces.

## 4. Recommendation

**Option A — first-exercise of reference-validation — with specific scoping.**

- Proposed session-015 scope: Cell 1 (Curation) with user-ratification halt between selection-shortlist and seal commit. Progression to Cell 2 Produce within the same session only if Cell 1 completes with reasonable budget remaining.
- Proposed default reference domain: source candidate pool spanning both same-domain-adjacent and different-domain-representative; present shortlist for user ratification.
- Proposed Case Steward: orchestrating agent (with known-limitation flag per §4.L2).

Rationale: the methodology's most-recent substantive specification is un-exercised; the primary structural commitment from Session 014 (six OI-016 re-opening triggers) requires first-exercise data to be meaningful; all other agenda options are better informed after at least one exercise.

## 5. Halt for user ratification

Session 015 halts here for user ratification of:

- **Agenda choice** (A / B / C / D, or hybrid).
- **If A**: reference-case domain direction (same-domain-adjacent / different-domain-representative / user-selected / default "mixed shortlist with ratification halt").
- **If A**: stop-point (Stop 3a = Cell 1 only; Stop 3b = Cell 1 + Cell 2 within session budget).
- **If A**: any specific steering on candidate reference cases the user has in mind (e.g., "pick a pre-2022 published movement sequence," or "not in the movement domain this time").

Pre-commitment: if Option A is chosen, Session 015 will engage the six OI-016 re-opening triggers as operational commitment; any trigger firing during Cell 1 or Cell 2 re-opens OI-016 immediately and returns the methodology to the pause state specified in `reference-validation.md` §9.

Session 015 will not proceed to Cell 1 case sourcing or any other agenda's deliberation launch before this ratification.
