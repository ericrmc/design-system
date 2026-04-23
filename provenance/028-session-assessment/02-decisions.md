---
session: 028
title: Decisions — §5.3 Pacer aggregate-hard-budget conversion adopted; close-rotation rule added; engine-v4 → engine-v5
date: 2026-04-23
status: complete
---

# Decisions — Session 028

## D-096: Adopt §5.3 aggregate-hard-budget with revised values and paired close-rotation rule; engine-v4 → engine-v5

**Triggers met:** [d016_2, d016_3]

**Triggers rationale:** d016_2 fires: this decision substantively revises `read-contract.md` v2 → v3 (adds §5 aggregate-hard-budget normative text; adds §6 close-rotation rule; updates §1 item 7; updates §2a to feed-forward into §5; updates §10 versioning). d016_3 fires: the deliberation's Q1 produced 3-of-4 adopt-with-revision vs 1-of-4 preserve; Q2 produced four distinct value recommendations (85K/95K, no-conversion, 100K/90K, 110K/120K); Q3 produced three distinct retention-window recommendations (3, 6, 10). At least two plausible positions were namable before deliberation and substantive disagreement materialised during deliberation.

**Non-Claude participation:** voluntary; Outsider participated (OpenAI GPT-5 via `codex exec`); `participant_organisation: openai`; `claude_output_in_training: known-no`; `independence_basis: organization-distinct`. d023_* does not fire (no methodology-kernel.md revision; no multi-agent-deliberation.md revision; no validation-approach.md Tier 2 revision; no OI-004 state change). Non-Claude participation is "recommended" per MAD v4 §When Non-Claude Participation Is Required. Outsider contributed criterion-3 data point (recorded impact: the "laundering the activation" critique materially shaped the Q2 values decision — see `01-deliberation.md` §8).

**Decision:**

1. **§5.3 status changes from "activated, preferred revision direction" to "converted to active spec at revised values; minority position preserved in §5.3 history block for provenance".** `read-contract.md` v3 §5.3 text updated to record the conversion-with-revision and the historical original-minority text.

2. **Aggregate-hard-budget values adopted: 100,000 words hard ceiling / 90,000 words soft warning** (default-read surface aggregate). These match the §2a thresholds as field-tested values, preserving clean semantic layering (§2a advisory/activation feeds forward into §5 budget enforcement).

3. **Close-rotation rule adopted: most recent 6 session closes remain default-read; older closes are archive-surface by exclusion per §3.** Citation exception: if a session needs to retain an older close in default-read, the session records a retention-exception decision.

4. **Two-tier remediation mechanism:**
   - **Soft (≥90K)**: validator emits remediation directive; next substantive session must include at least one aggregate-reducing action.
   - **Hard (≥100K)**: session cannot close cleanly without executing structural remediation that returns aggregate below 100K.

5. **Per-file budgets unchanged** (8K hard / 6K soft). Orthogonal supplement per 4-of-4 convergence.

6. **§2a retained as sensor layer** (90K advisory emission / 100K activation emission); the new §5 budget layer adds the actuation path per 3-of-4 convergence ("sensor + controller" framing per Outsider `[01d, Q6]`).

7. **Engine-v4 → engine-v5** per substantive revision to `read-contract.md` v2 → v3 and substantive update to `tools/validate.sh` (new constants; check 20 extended with hard/soft pass/fail; new default-read detection using 6-session retention window). `read-contract-v2.md` preserved as superseded. `engine-manifest.md` §2 and §7 updated.

8. **§5.4 cadence minority unchanged** (activated-not-escalated); OI-018 remains open; this bump is content-driven (fourth bump in eight sessions 021/022/023/028, outside R9 window and aged-out per Session 026 D-092).

9. **Close-rotation executed at Session 028 close**: Sessions 002-022 close files (20 files totalling ~56,180 words) rotate to archive-surface by exclusion. Files remain physically at `provenance/NNN-title/03-close.md`; they are simply no longer in the §1 enumeration. Projected post-close aggregate: ~56,000 words / 19 files default-read.

**Rejected alternatives:**

- **Preserve-with-softer-intervention (Skeptic-preserver)** `[01b, Q1]`: adopting close-rotation + prompt-guidance without hard-budget conversion. Rejected on 3-of-4 cross-family weighted grounds (Pacer + Synthesiser + Outsider). Skeptic-preserver's dissent is preserved as first-class minority §6.1 with activation warrant: if within 3 sessions the new budget fires only through accretion-growth with no observable friction and soft interventions alone would have achieved equivalent aggregate reduction, Skeptic position vindicates retroactively.

- **Tighter values 85K/95K (Pacer-advocate)** `[01a, Q2]`: rejected on grounds that hard-below-activation creates double-signal at different numbers and that 85K soft requires ~20,400-word trim which is disproportionate to observed pressure. Pacer's tighter-values position preserved as first-class minority §6.2 with activation warrant: if within 5 sessions the new budget fires twice without compensating restructure, Pacer position becomes preferred revision direction.

- **Higher values 110K/120K (Synthesiser-integrator)** `[01c, Q2]`: rejected on Outsider cross-family critique that above-current hard ceilings "launder the activation" by moving the trigger after it fired `[01d, Q2]`. Synthesiser's headroom-values position preserved as first-class minority §6.3 with activation warrant: if remediation-chaos materialises within 3 sessions (forced restructure in mid-deliberation; deliberation distortion), Synthesiser position becomes preferred revision direction.

- **10-session retention window (Synthesiser-integrator)** `[01c, Q3]`: rejected in favour of Outsider's 6-session recommendation. Synthesiser's 10-session window preserved as first-class minority §6.4 with activation warrant based on cited-exception frequency.

- **3-session retention window (Pacer-advocate, Skeptic-preserver)** `[01a, Q3; 01b, Q1]`: rejected in favour of Outsider's 6-session recommendation. Pacer's 3-session window preserved as first-class minority §6.5 with activation warrant based on aggregate-control insufficiency.

- **Pressure-signal-audit for all watchpoints (Skeptic-preserver)** `[01b, Q6]`: rejected as out-of-scope for this session's Path G. Skeptic's methodology-level observation preserved as first-class minority §6.6 with activation warrant tied to future budget-firing surface.

**Rationale:**

The Outsider's cross-family contribution is load-bearing: the "laundering the activation" critique `[01d, Q2]` disambiguated the Q2 values choice between Pacer's 85K/95K and Synthesiser's 110K/120K. The critique states that moving the hard ceiling above 100K (the activation threshold that fired) is "self-protective drift" — the engine should not answer "the trigger fired" by moving the trigger. Pairing Outsider's 100K/90K with the immediate-remediation requirement (close-rotation reduces aggregate below hard in Session 028 close) avoids both failure modes:
- Not laundering (the hard ceiling remains at the activation threshold that fired, not moved above it).
- Not specification-in-violation-at-steady-state (Session 028 close executes close-rotation to bring aggregate below 100K at session-close time).

The close-rotation mechanism addresses the dominant growth driver: §3a analysis (all 4 perspectives agreed) identifies close-file accretion as the primary factor. Per-file budget revision would not address this (all closes are individually under per-file hard); only enumeration-structural change does. Close-rotation is the minimum necessary mechanism; retention of 6 sessions preserves the recent minority-review window (§5.2 vindicated at 5-session window, §5.4 aged out at 9-session — the Synthesiser 10-session minority is preserved against this concern).

The §5.3 minority's original intent (name a budget; create forcing function) is honoured. The original minority text (Session 023 Pacer 80K/90K proposal) is preserved in `read-contract.md` v3 §5.3 history block per preservation discipline — the engine records what was originally proposed, what was adopted in revision, and why.

Engine-v5 bump per substantive revision. §5.4 cadence minority is activated-not-escalated; this bump does not retrigger R9 (aged out Session 026); the bump is content-driven per a fired minority-activation-warrant per MAD v4 discipline. Any future Session that proposes engine-v6 without similar content-ground justification would engage §5.4 on content grounds.

---

## D-097: OI-004 voluntary:required ratio and criterion-3 update; minority housekeeping

**Triggers met:** [none]

**Triggers rationale:** Housekeeping; no new normative content. OI-004 state unchanged at "articulated; awaiting closure-retrospective" (state 3 of 4). No spec revisions beyond those in D-096. No watchpoints opened. Per Session 023 D-087 / Session 024 D-089 / Session 025 D-091 / Session 026 D-093 / Session 027 D-095 precedent for separate `[none]` housekeeping record.

**Decision:**

1. **OI-004 tally unchanged at 8-of-3 required.** Outsider participation contributed voluntary:required progression 9:8 → **10:8**.

2. **Criterion-3 cumulative data point +1**: 67 → **68**. The load-bearing Outsider contribution `[01d, Q2]` "laundering the activation" critique materially shaped D-096's values decision per §8 of `01-deliberation.md`. This is a cross-lineage contradiction-prevailing case: the Outsider position contradicted the Synthesiser Claude-perspective's 110K/120K recommendation, and the synthesis adopted the Outsider position; structurally meets Session 021 D-082 P4 Assertion shape.

3. **OI-002 heuristic data point n+1 = 13**: D-096's `read-contract.md` v3 revision classified as **substantive** per OI-002 heuristic (changes §5 budget structure by adding new normative enforcement layer; adds new §6 close-rotation rule; adjusts §1 enumeration and §2a role; engine-v bump per engine-manifest §5). Adds one data point to OI-002 substantive tier.

4. **OI-018 note**: engine-v5 bump this session is content-driven (§5.3 warrant-fired response). OI-018 deliberation on engine-manifest §5 bump-trigger criteria remains deferred. Session 028 bump does not engage OI-018 per 3-of-4 convergence in deliberation.

5. **OI-007 active count**: **14** (new OI-019 opened in D-097 step 6 below; see next step). The close-rotation rule's operational framing — "most recent 6 session closes remain default-read; citation-exception via decision record" — may need operational refinement if future sessions require retention-exception decisions frequently. This is tracked as a watchpoint only (WX-28-1 close-rotation-exception-frequency; observational n<3) rather than new OI.

6. **No new OI opened this session.** Synthesiser's proposed new OI ("Specify advisory-review procedure in `read-contract.md` so advisory emissions link to explicit decision-points rather than relying on voluntary between-stage response") `[01c, Q6]` is subsumed by D-096's §5 budget tier adoption (the new soft-warning directive provides the decision-point). Skeptic's pressure-signal-audit observation is preserved as first-class minority §6.6 in the deliberation synthesis rather than opened as OI per 3-of-4 against new-OI-surface direction.

7. **Watchpoints carried forward**:
   - WX-22-1 (witness-dumping pattern): no new data.
   - WX-24-1 (MAD growth): current 6,386 unchanged across six consecutive session closes 023/024/025/026/027/028-projected. Will re-measure at close.
   - WX-24-2 (budget-literal drift forward discipline): **exercised this session** — the D-096 substantive revision names specific new literals (100K hard, 90K soft, 6-session retention) and updates `validate.sh` constants to match. Forward discipline: any future session proposing budget-literal edits must honour the §5 activation warrants in §6 above.
   - WX-24-3 (Outsider pre-response workspace exploration pattern): **n=5** (Session 028 Outsider read workspace files per Honest Limits; pattern now stable at n=5).
   - WX-27-1 (archive-token citation fragility): no new data.
   - **WX-28-1 (new)**: close-rotation-exception-frequency. Observational. Tracks how often future sessions require retention-exception decisions to keep specific older closes in default-read. Activation threshold: if within 10 sessions (Sessions 029–038) retention-exception decisions are recorded in 3 or more sessions, the 6-session retention window may be too narrow; Synthesiser §6.4 10-session minority becomes preferred revision direction.

**Rationale:**

Housekeeping record per precedent. The substantive content of Session 028 is D-096; D-097 records the state accounting and preservation of minorities that don't warrant their own decision record. No new OIs opened because 3-of-4 deliberation convergence directed against adding surface, and the Synthesiser's proposed OI is operationally subsumed by D-096's budget tier.
