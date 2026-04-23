---
session: 032
title: Decisions — Cell 1 L1b REJECT for PD-A; §9 trigger 7 fires; OI-016 re-opens; kernel §7 revision required Session 033; engine-v5 preserved
date: 2026-04-23
status: complete
---

# Decisions — Session 032

## D-104: PD-A (Rule of St. Benedict Ch 58) L1b saturation test REJECT on Condition 2; OI-016 re-opens; kernel §7 revision required Session 033 per §9 trigger 7

**Triggers met:** [none]

**Triggers rationale:** Cell 1 Case Steward work under Path C-fresh operator ratification with public-domain constraint. Single-orchestrator Cell 1 step execution per `reference-validation.md` v2 §3 Cell 1 "one or two Case Stewards (non-Produce, non-Validation)" — Session 018 D-076 / Session 031 D-102 precedent for single-orchestrator Cell 1 with mechanical cross-family invocation for saturation testing. No methodology-kernel.md revision proposed THIS session (d016_1 not fired this session — kernel §7 revision is *required for Session 033* per §9 trigger 7 mandate, but Session 032 does not perform the kernel revision; anti-laundering: do not retrofit the spec in the same session that surfaces the firing pattern). No specification creation or substantive revision (d016_2 not fired — Session 032 executes existing spec mechanism, surfaces a §9 trigger firing, but does not revise the spec). No multi-perspective deliberation convened; Cell 1 saturation testing is mechanical (did the outputs reproduce the reference's distinctive labels?) not design-contested in a deliberative sense (d016_3 not fired). Operator load-bearing input was the path-and-constraint ratification + the REJECT verdict confirmation when surfaced (d016_4 latent; the REJECT verdict was the operator's confirmed direction among the strict-vs-lenient reading dichotomy — see verdict §1 last paragraph). d023_1/2/3 not in scope (no kernel/MAD/validation-approach-Tier-2 revision THIS session). d023_4 not fired (no OI-004 state change; Case Steward work does not advance OI-004 tally; mechanical cross-family invocation per Session 031 D-102 precedent).

**Single-agent reason:** Cell 1 Case Steward execution per `reference-validation.md` v2 §3 role-specification and Session 018 D-076 / Session 031 D-102 precedent. Mechanical cross-family invocation for L1b saturation testing (codex exec + independent Claude Agent-tool subagent) is documented at the participants-level per MAD v4 §mechanical_cross_family_invocation block at sealing. Sealing was NOT pursued this session because L1b REJECT terminates Cell 1 before sealing; no `participants.yaml` finalisation needed for the mechanical invocation per the Session 031 deferred-pattern (mechanical invocation block is recorded at sealing or at REJECT-recording session close).

**Decision:**

Execute reference-validation Cell 1 per Path C-fresh ratification with operator public-domain constraint. L1a thin-prompt canary + L1b full-constraint saturation test on candidate PD-A (Rule of St. Benedict Chapter 58 "Of the Discipline of Receiving Brothers", Cardinal Gasquet 1909 / Hunter Blair 1886 PD English translations) carried out per v2 §4 L1a + L1b. Test inputs and outputs recorded at `provenance/032-session-assessment/cell1/`:

- `00-public-domain-candidate-survey.md` — six PD candidates surveyed against C1–C8; PD-A selected as top candidate; operator ratified with PD-B Vitruvius Book I Ch 4 noted as next candidate.
- `01-constraint-statement.md` + `constraint-prompt.txt` — problem-shape statement with §2 forbidden-terms discipline (religious-tradition vocabulary, RoSB-specific tokens, indirect-tip vocabulary all excluded via mechanical grep audit).
- `l1a-thin-prompt.txt` — thin prompt for L1a canary.
- `l1a-codex-raw.txt` — codex L1a output (PASS — no RoSB-distinctive markers).
- `l1a-claude-raw.md` — Claude L1a output (PASS — no RoSB-distinctive markers).
- `02a-l1a-canary-verdict.md` — L1a verdict PASS for both families.
- `02a-l1b-codex-raw.txt` — codex L1b output (~1,150 words reader-facing).
- `02b-l1b-claude-raw.md` — Claude L1b output (~1,070 words reader-facing).
- `02-l1b-verdict.md` — L1b verdict REJECT.

**L1b verdict: REJECT on §1 C3 Stage (b) Condition 2.**

- **Condition 1** (>30% 5-gram overlap): PASS (qualitative). Neither output reproduces RoSB Ch 58's prose at scale; no Suscipe formula, no 2/6/4-month interval enumeration, no three-vow stability/conversion/obedience formula, no "Here is the law under which you wish to fight" quotation. Estimated overlap qualitatively under 30%.
- **Condition 2** (verbatim distinctive label/heading from reference, zero-tolerance): **FIRES on both families.** Codex emits "Postulancy", "Novitiate or Candidacy" as section headings; "postulant", "novitiate", "vigil", "place of worship", "give the peace", "devotions", "rule" (capitalized contextually) inline. Claude emits "POSTULANCY", "NOVITIATE", "PROFESSION" as section headings; "postulant", "novice", "habit" (as religious clothing at full membership), "fasts", "doorkeeper", "rule of the house" inline. These labels are FROM RoSB Ch 58's English-translation tradition (novice, novitiate, profession, habit appear in Hunter Blair 1886 / Gasquet 1909 directly; postulancy is RoSB-derivative Catholic religious-formation terminology). All these labels are in the §2 forbidden-terms list of `01-constraint-statement.md`; constraint statement was mechanically grep-audited at §4 confirming zero forbidden-term occurrences. Both models emit them despite constraint-statement absence — structural retrieval despite lexical filtering.
- **Condition 3** (cross-family retrieval asymmetry with reproduction): PASS — pattern is cross-family CONVERGENCE on RoSB-tradition framing, not asymmetry. Methodologically interesting (cross-family-shared saturation; both OpenAI and Anthropic pretraining densely-trained on RoSB-religious-formation tradition) but not a Condition 3 fire.

**Cross-family convergence vs Session 031 PASS-with-genre-saturation distinction.** Session 031's S1 PASS recorded somatic-genre convergence (body scan, micro-movement) shared across multiple non-Feldenkrais traditions (Alexander, BMC, MBSR, Yoga Nidra) — generic genre, not lesson-specific. Session 032's PD-A REJECT records RoSB-tradition-distinctive label convergence (postulancy/novitiate/profession/habit) which uniquely identifies the Catholic-religious-formation lineage that RoSB Ch 58 founds. The distinction matters operationally: genre-tradition labels FROM the reference's lineage fire condition 2; generic-tradition features SHARED across multiple non-reference lineages do not. Session 031 PASS and Session 032 REJECT are consistent applications of the same standard.

**§9 trigger 7 FIRES.** Counter advances 1-of-2 → 2-of-2:
- Session 018 D2 (agile-retrospective domain): C3 rejection with ~94% Claude verbatim text reproduction.
- Session 032 PD-A (community-admission domain): L1b Condition 2 rejection with Claude near-verbatim reproduction of distinctive RoSB-tradition labels and stage-structure (gate/POSTULANCY/NOVITIATE/PROFESSION/INTEGRATION pattern matches RoSB Ch 58 + tradition near-verbatim).

Per §9 trigger 7 mandate:

(i) **Activate the Session 014 Skeptic "provisional substitute" minority warrant** (per `reference-validation.md` v2 §10.1) **as required kernel §7 revision consideration in Session 033.**

(ii) **Re-open OI-016 to Open state pending kernel §7 revision deliberation.** OI-016 status changes: "Resolved — provisionally addressed pending first-exercise" → "Open — pending kernel §7 revision per §9 trigger 7 firing at Session 032 PD-A REJECT". Status updated in `open-issues/OI-016.md` and `open-issues/index.md`.

(iii) **Saturation-gate false-negative pattern observable as pattern.** PD-A passed L1a clean (`02a-l1a-canary-verdict.md` documents no RoSB markers in either family's thin-prompt output) then rejected L1b (full-constraint saturation surfaces RoSB-tradition labels). Session 018 S1 had structurally-similar pattern (passed L1a; never tested at L1b in Session 018; passed L1b with genre-saturation observation in Session 031). The L1a-pass-but-L1b-reveal pattern is now n=2 observable (Session 018 S1 ambiguous case + Session 032 PD-A clean case).

**§9 trigger 5 counter advances 1-of-3 → 2-of-3.** Three-consecutive-gap-surfaced-non-passes counter (Session 031 close §4c precedent: PASS does not reset). Session 018 D2 + Session 032 PD-A = 2 non-passes; Session 031 S1 PASS does not reset. Trigger does not fire (3-of-3 required); Session 033 next reference-validation exercise risks firing trigger 5 if rejection.

**§10 minority status changes:**

- **§10.1 Skeptic "provisional substitute" framing minority** (Session 014, 01c Q5) — **ACTIVATED** per trigger 7 firing. Required kernel §7 revision direction: use phrase "provisional substitute"; add mandatory-dissent clause; strengthen scope-statement.
- **§10.1 Skeptic+Outsider joint narrower-claim minority** (Session 014, 01c+01d Q7) — **vindicated-direction** (Session 032 REJECT is evidence the methodology validates a narrower claim than originally framed; the joint minority's standing-warrant is structurally consistent with the trigger 7 firing).
- **§10.2 Skeptic preemptive-activation minority** (Session 019, 01c Q5/Q7) — **VINDICATED.** The minority predicted exactly this outcome: "if a second structurally-different-domain rejection fires §9 trigger 7 (or if interim citation drift occurs per §8 before n=2 is reached), the broad-reading preemptive activation position is vindicated and kernel §7 revision is the preferred response." Session 032 produces the second structurally-different-domain rejection. Skeptic preemptive-activation minority is the second §10.2 minority (after §10.1 Skeptic provisional-substitute framing) confirming the same revision direction.
- **§10.2 Minimalist defer-revision minority** (Session 019, 01b Q1/Q7) — **NOT VINDICATED.** Position: "if Session 020's Cell 1 attempt passes C3 stage (a) and (b) without triggering any of the three rejection conditions, the revised §1 C3 / §4 L1 did no work v1 would not also have done." Status at Session 032: Session 031's S1 passed L1b under v2's protocol (the v2-upgraded L1b discriminated and PASS-direction); Session 032's PD-A rejected at L1b under v2's protocol (the v2-upgraded L1b discriminated and REJECT-direction). The revised v2 §1 C3 / §4 L1 text DID work that v1 would not have done in BOTH directions. Minimalist minority not vindicated; v2 revisions are operationally load-bearing.
- **§10.2 Reviser asymmetry-probe minority** (Session 019, 01a Q3 R2) — **partial-vindication-asymmetric, not-engaged-symmetric.** The asymmetry-probe minority's predicted utility (recording which family reproduced) holds for Session 018 D2 asymmetric pattern (Claude reproduced ~94%; codex from-scratch). Session 032 PD-A pattern is symmetric (both families converge on RoSB-tradition); asymmetry-probe records would NOT detect symmetric saturation. The probe clause is partially vindicated for asymmetric cases; symmetric cross-family saturation requires a different observation mechanism. Carry forward as observation.

**Engine-v5 preserved.** Session 032 produces no engine-definition file revision in this session. Engine-v5 preservation window extends to 4 sessions (Sessions 029, 030, 031, 032 all non-bump). Session 033 kernel §7 revision will be a substantive engine-definition file change requiring `methodology-kernel.md` v5 → v6 substantive revision and engine-v5 → engine-v6 bump per `engine-manifest.md` §5.

**OI-016 re-opening — full status text:** "Open — pending kernel §7 revision per §9 trigger 7 firing at Session 032 PD-A REJECT (per D-104, Session 032). State changed from 'Resolved — provisionally addressed pending first-exercise' by §9 trigger 7 (two pre-seal C3 stage (b) rejections in structurally-different domains with near-verbatim Claude-family reproduction): Session 018 D2 (agile-retrospective domain) + Session 032 PD-A (community-admission domain). Per `reference-validation.md` v2 §9 trigger 7 mandate, the next-session (Session 033) must include kernel §7 revision deliberation; the Session 014 §10.1 Skeptic 'provisional substitute' framing minority is activated as the required revision direction; the Session 019 §10.2 Skeptic preemptive-activation minority is vindicated."

**Sealing not pursued.** L1b REJECT terminates Cell 1 for PD-A. No reference-envelope, no brief-gatekeeper.md, no Cell 2 Produce. The PD source-text fetch path (in-session WebFetch from archive.org) is not exercised this session because there is no candidate to seal; PD-source-fetchability remains structurally available for future PD candidates that pass L1b.

**Rejected alternatives:**

- **Alternative 1: Override to PASS-with-religious-formation-genre-saturation observation.** Rejected by operator after Case Steward surfaced the strict-vs-lenient reading dichotomy. The strict reading (REJECT on Condition 2 due to forbidden-terms-list emission and RoSB-tradition-lineage labels) is the honest verdict; the lenient reading (PASS-with-genre-saturation by Session 031 analogy) is rejected because the labels emitted (postulancy/novitiate/profession/habit) UNIQUELY identify the RoSB-derived Catholic-religious-formation tradition, which is qualitatively different from Session 031's somatic-genre features shared across multiple non-Feldenkrais traditions. The analogy-distinction is recorded in verdict §3.
- **Alternative 2: Defer verdict to Session 033 operator + Case Steward joint review.** Rejected by operator at Case Steward halt-and-surface. Operator confirmed REJECT directly without deferral, satisfying the L2 mitigation requirement (operator second-judgment on the strict-vs-lenient call).
- **Alternative 3: Switch to PD-B Vitruvius and re-test in same session.** Rejected because (i) bounded-session-scope per Session 018 / Session 031 precedent (one candidate per Cell 1 session); (ii) PD-A REJECT advances a load-bearing methodology event (§9 trigger 7 firing) that warrants its own session-recording weight; (iii) PD-B testing should occur after kernel §7 revision (Session 033+) so the revised reference-validation framing informs the test design — testing PD-B in Session 032 would lock in the v2-protocol verdict before the Session 033 revision changes the framing.
- **Alternative 4: Propose `reference-validation.md` v2 → v3 revision in this session to add a Condition 4 (cross-family-shared-tradition-label saturation).** Rejected per anti-laundering — do not retrofit the spec in the same session that surfaces the pattern (Session 027 / Session 028 / Session 031 close framings; Session 031 close §5 "honest sealing-deferral" parallel discipline). Session 033 may consider the spec revision direction after kernel §7 revision and after Session 032 verdict has stabilised in the record.
- **Alternative 5: Classify Session 032 as not-counting-toward-trigger-7 because PD-A condition 2 fire is on labels-from-tradition (not labels-from-text-of-Ch58-itself).** Rejected because (i) the §2 forbidden-terms list explicitly named these terms as "indirect-tip vocabulary" derived FROM the reference's lineage; (ii) the spec text §1 C3 Stage (b) condition 2 does not distinguish "label from reference text" vs "label from reference's lineage" — distinctive labels uniquely identifying the reference fire condition 2; (iii) the labels DO appear in the English translations of RoSB Ch 58 itself (novice, novitiate, profession, habit are in Hunter Blair 1886 / Gasquet 1909 inline); (iv) anti-laundering against verdict-softening.

---

## D-105: OI state housekeeping; §10 minority status changes summary; minority data points; watchpoint advancements; close-rotation fourth steady-state data point

**Triggers met:** [none]

**Triggers rationale:** OI housekeeping + minority activation-clock evaluation + watchpoint advancement per the long precedent chain (D-073 through D-103). The substantial state changes from D-104 (OI-016 re-opening; §10 minority status changes) are recorded in D-104 itself; D-105 records the secondary OI/minority/watchpoint observations not load-bearing for D-104. No new normative content. d023_4 not in scope (OI-016 re-opening is recorded in D-104 not D-105; D-104's OI state-change is the load-bearing record).

**Decision:**

### OI-002 — threshold for substantive vs minor

No data point this session. Session 032 produced no specification revision. Status text unchanged. Forward note: Session 033 kernel §7 revision will be a substantive revision (engine-v5 → engine-v6 bump), providing OI-002 data point 14.

### OI-004 — cross-perspective participation

Tally unchanged at 8-of-3 required; voluntary:required unchanged at 10:8; criterion-3 cumulative unchanged at 68. Session 032 invoked codex exec for L1a + L1b mechanical saturation testing (two invocations); per MAD v4 §Acceptable Participant Kinds, mechanical cross-family invocation outside the perspective-deliberation frame is NOT a participant kind for OI-004 narrowing. Eleventh consecutive non-advancing required-trigger session since Session 021 criterion-4 articulation. Session 033 kernel §7 revision will require non-Claude perspective participation per MAD v4 §When Non-Claude Participation Is Required clause 1 (modifies methodology-kernel.md) — that participation will advance OI-004 voluntary:required.

### OI-007 — scaling the open-issues format

Active count advances from 13 → 13 (OI-016 status change does not increment count; OI-016 was already in the active list per index.md hybrid-state convention). The kernel §7 revision direction Session 033 may consider opening a new OI to track the revised reference-validation's claim-narrowness; deferred to Session 033 deliberation.

### OI-015 — laundering enforcement gap

Count unchanged at 6 (positive-exercise data points). Session 032 is not a positive-exercise case in OI-015's tracked sense (OI-015 tracks domain-reading laundering prevention; Session 032 is Cell 1 saturation testing).

### OI-016 — domain-validation pathway under user unavailability

**Re-opened to Open state per D-104.** State change recorded in D-104 above and in `open-issues/OI-016.md` State history section + `open-issues/index.md` row.

### OI-018 — engine-manifest §5 bump-trigger criteria

Status unchanged: Open — deferred. Engine-v5 preserved at Session 032. Session 033 kernel §7 revision will be the fifth engine-v-bump (021/022/023/028 + Session 033 = bumps 1/2/3/4/5). §5.4 cadence minority remains activated-not-escalated; the next engine-v bump is content-driven (§9 trigger 7 mandates kernel §7 revision; not cadence-driven), so §5.4 does not re-escalate by analogy to Session 028 D-096 (3-of-4 convergence to keep cadence question separate from substantive bump).

### §5.6 vindicated-complete (Session 031); §5.8 vindicated-complete (Session 031)

No ongoing tracking required at Session 032+. Forward records carry the vindication-status.

### §5.7 Pacer-advocate 85K/95K — 4-of-5 data point

Vindication-direction data point recorded at Session 032 close. Zero §2b budget-fires this session (aggregate well below 90K soft). Window completes at Session 033 close — if Session 033 also produces zero budget-fires, §5.7 vindicates retroactively at Session 033 close (4-of-5 + Session 033 = 5-of-5 vindication-direction).

### §5.9 Synthesiser-integrator 10-session retention-window — 4-of-6 data point

Vindication-direction data point recorded. Zero retention-exceptions at Session 032. Window continues Sessions 033–034.

### §5.10 Pacer-advocate 3-session retention-window — 4-of-6 data point

Vindication-direction data point recorded. Aggregate well below 90K soft. Window continues Sessions 033–034.

### §5.11 Skeptic-preserver pressure-signal-audit — no data point

No budget-firing event at Session 032.

### Reference-validation §10 minority status

Recorded in D-104 (load-bearing for OI-016 re-opening). Not duplicated here.

### WX-24-1 — MAD growth

**10-session no-growth streak at 6,386 words.** Sessions 023 through 032 inclusive. Longest in watchpoint history; extends Session 031's 9-session record.

### WX-24-2 — budget-literal drift forward discipline

Flag-resolved Session 030 per D-100. Watchpoint continues as forward discipline. No exercise required at Session 032.

### WX-24-3 — Outsider pre-response workspace exploration pattern

**n=5 stable.** Session 032 codex exec invocation was for L1a + L1b mechanical saturation testing (mechanical cross-family invocation), not participant-perspective Outsider deliberation. Session 033 kernel §7 revision deliberation WILL include perspective-Outsider per MAD v4 §When Non-Claude Participation Is Required clause 1, advancing WX-24-3 to n=6 at that session.

### WX-27-1 — archive-token citation fragility

**n=3 stable.** Session 032 close validator run confirmed; no new archive-token citation issues at Session 032 (no new `[archive:` citations were composed in default-read files this session). Threshold-reached state from Session 031 close §4b carries; minor-amendment to `read-contract.md` §6 guidance remains a Session 033+ Path L candidate.

### WX-28-1 — close-rotation-exception-frequency

**Fourth steady-state data point recorded: zero retention-exceptions.** Counter at 0-of-4 in the 10-session window (Sessions 029, 030, 031, 032). Observational; pattern held across four steady-state rotations.

### Saturation-gate false-negative pattern (NEW observational, originates §9 trigger 7 mandate at Session 032)

Per §9 trigger 7 mandate: "Make the saturation-gate false-negative pattern (a candidate surviving L1a canary but rejected at L1b full-constraint probe) observable as a pattern rather than a single-session artefact." Pattern instances:

- **Session 018 S1**: passed L1a in Session 018; never tested at L1b in Session 018 (pre-v2); passed L1b in Session 031 with genre-saturation observation. Boundary case (passed both stages but with observation).
- **Session 032 PD-A**: passed L1a in Session 032 (clean canary; no RoSB-distinctive markers); rejected at L1b on Condition 2 (full-constraint saturation revealed RoSB-tradition labels). **Clean false-negative case for L1a.**

The pattern is operationally observable: the L1a-PASS-but-L1b-REJECT case (n=1 clean; PD-A) demonstrates that thin-prompt canary under-detects saturation when the triggering content is distributed across the requirements rather than concentrated in problem-shape — reproducing the WX-18-2 finding from Session 018 with a cleaner second-instance demonstration.

This pattern is recorded as an observation at Session 032 close; Session 033 kernel §7 revision deliberation may incorporate it. Not opened as separate OI per OI-007 scaling discipline (subsumed under OI-016 re-opening; observation lives in `reference-validation.md` v2 §9 trigger 7 record + Session 032 close).

### Close-rotation at Session 032 close

Per `read-contract.md` v3 §2c, default-read enumeration at Session 032 close: top 6 session closes by NNN prefix = Sessions 027, 028, 029, 030, 031, 032. **Session 026 close rotates OUT of default-read** (moves to archive-surface-by-exclusion per §3); Session 032's own close (this session's) enters the window. Net default-read close-file count: 6, unchanged. Physical paths unchanged. No retention-exception decisions recorded.

**Fourth close-rotation steady-state rotation** since Session 028 initial exercise.

**Rejected alternatives:**

- **Alternative 1: Open a formal OI tracking the saturation-gate false-negative pattern.** Rejected per OI-007 scaling discipline; pattern is observed within `reference-validation.md` v2 §9 trigger 7 record and the OI-016 re-opening already carries the pattern as load-bearing.
- **Alternative 2: Record `reference-validation.md` v2 §10 minority status changes (vindications/activations) in `read-contract.md` v3 §2b minority block too.** Rejected because the minority-status records in D-104 reference `reference-validation.md` v2 §10 minorities (not `read-contract.md` minorities); `read-contract.md` minorities are budget-related (§5.6/§5.8 vindicated Session 031); the two minority-tracking surfaces are independent.
- **Alternative 3: Advance OI-004 criterion-3 cumulative count for the L1a + L1b dual mechanical invocations.** Rejected per MAD v4 §Acceptable Participant Kinds (mechanical invocation does not narrow OI-004); cumulative 68 unchanged.
- **Alternative 4: Trigger §5.4 engine-v-cadence re-escalation in anticipation of Session 033 v6 bump.** Rejected because §5.4 R9 aged out Session 026; Session 028 v5 bump did not re-escalate per 3-of-4 convergence; Session 033 v6 bump is content-driven (§9 trigger 7 mandates) not cadence-driven; same precedent applies. §5.4 does not re-escalate.
