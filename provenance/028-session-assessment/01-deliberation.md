---
session: 028
title: Deliberation synthesis — §5.3 Pacer aggregate-hard-budget activation response
date: 2026-04-23
status: complete
synthesizer: claude-opus-4-7 (orchestrator; not a deliberation perspective)
synthesized_at: 2026-04-23T00:00:00Z
participants_family: cross-model
cross_model: true
non_claude_participants: 1
oi004_qualifying_participants: [Outsider]
brief_anchor_commit: d0d81e4
---

# Deliberation Synthesis — Session 028

## §1 Frame

Four perspectives deliberated on the §5.3 Pacer aggregate-hard-budget minority, which activated at Session 027 close when aggregate crossed 100,000 words. Three Claude Opus 4.7 subagents (Pacer-advocate, Skeptic-preserver, Synthesiser-integrator) and one non-Claude Outsider (OpenAI GPT-5 via `codex exec`). Brief committed at commit `d0d81e4` before any perspective launched (MAD v4 §Brief immutability).

Citations: `[01a, Qn]` Pacer-advocate, `[01b, Qn]` Skeptic-preserver, `[01c, Qn]` Synthesiser-integrator, `[01d, Qn]` Outsider. `[synth]` marks synthesizer-original integrative claims.

## §2 Q1 Adopt-or-preserve

**3-of-4 cross-family convergence on adoption-with-revision. 1-of-4 dissent for continued preservation.**

Adoption positions (3-of-4):
- **[01a, Q1]** "Convert §5.3 to active specification. This is the moment the minority was preserved for, and the engine's integrity as a system that honours its own commitments depends on honouring it now. ... Revision-in-light-of-post-activation-information is the one legitimate variation I will consider."
- **[01c, Q1]** "Partial adoption with revision: convert §5.3 to an active specification, but not at the minority's preserved values and not as a single-lever response. ... Adoption-with-revision honours preservation if the revision is faithful to the minority's structural intent (forcing function; bounded aggregate) and adjusts only what five sessions of evidence warrant adjusting (values; paired mechanism)."
- **[01d, Q1]** "Convert §5.3 into active specification now, but do **not** convert it by simply copying its original 90K/80K numbers into the spec. ... So my answer is: **adopt, and revise §5.3 in light of post-activation information.**"

Preservation position (1-of-4, adversarial role):
- **[01b, Q1]** "Continue preservation with activation recorded; defer conversion pending evidence from softer interventions. ... Record the activation-firing as specified. Execute a softer intervention bundle: old-close rotation (move `03-close.md` files from Sessions 022–024 to archive-surface, retaining 025+ in default-read) + prompt-level close-budget guidance. ... Re-measure aggregate at Session 029 close with the softer intervention in place."

Synthesis:

The cross-family adoption direction is load-bearing. Per MAD v4 §Synthesis conventions, cross-family composition weighting at 3-of-4 (including the one non-Claude participant) supports adoption. The dissenting Skeptic-preserver position is preserved as first-class minority with activation warrant per §6 below — the Session 027 §5.2 vindication precedent shows preservation-with-warrant can vindicate; Skeptic-preserver's position must be afforded the same governance respect.

A genuinely new-information question runs through the dissent: **[01b, Q7]** "The net new information since Session 023 runs *against* conversion, not toward it." The adoption majority disputes this:
- **[01a, Q7]** "Honouring it is not circular self-confirmation; it is the majority's own prior commitment coming due."
- **[01c, Q7]** "The warrant entitles the minority to serious review and preferred-direction status, not to automatic adoption at preserved values."
- **[01d, Q7]** "Activation says the direction is now preferred. It does not erase the right to revise the exact shape in light of the trajectory observed since Session 023."

The adoption majority's position is that §5.3 activation is itself coherent continuation of preservation discipline (preservation resolves per warrant language; §5.2 resolved null-outcome; §5.3 resolves positive-activation), and that post-activation information supports adoption at revised values. The dissent's position is that activation-firing alone is insufficient empirical evidence without first trying softer interventions.

Both positions are argued in good faith. The deliberation's majority direction is adoption. `[synth]`

## §3 Q2 Budget values

**Four distinct value recommendations. Cross-family weighted plurality for 100K hard / 90K soft.**

The candidate value matrix:

| Perspective | Soft | Hard | Trim required from 105,399 |
|---|---|---|---|
| **[01a] Pacer-advocate** | 85K | 95K | ~20,400 words to reach soft |
| **[01b] Skeptic-preserver** | — (preservation) | — | n/a; if forced: 100K/105K (~5,400 to soft) |
| **[01c] Synthesiser-integrator** | 110K | 120K | 0 (hard above current) |
| **[01d] Outsider** | 90K | 100K | ~15,400 words to reach hard, ~15,400+ to reach soft |

The positions are genuinely divergent. The synthesiser's 120K/110K sits above current state; the Pacer's 95K/85K sits well below; the Outsider's 100K/90K sits between (hard at the fired-activation threshold); the Skeptic declines to pick.

**The Outsider's cross-family critique of above-current values**:
- **[01d, Q2]** "110K/100K or 120K/110K would launder the activation. If the engine crosses a pre-named 100K threshold and then answers by putting the new hard ceiling above the current state, it is effectively saying: 'the trigger fired, so we moved the trigger.' That is exactly the kind of self-protective drift this methodology is supposed to resist."

This critique directly contradicts the Synthesiser's "specification-in-violation" argument:
- **[01c, Q2]** "Setting hard at 90K when actual is 105K means the budget is born in violation. A budget in violation is a restructure-forcing event, not a steady-state specification."

Both arguments engage genuine design tensions. The synthesizer-original resolution `[synth]`: the tensions are reconcilable by pairing adoption at Outsider's 100K/90K with immediate remediation (per §4 below) sufficient to return under hard within Session 028 close. This avoids both:
- Laundering (hard ceiling remains at the activation threshold that fired, not moved above it).
- Specification-in-steady-state-violation (Session 028 close executes remediation that brings aggregate back under 100K).

The Pacer's 85K/95K is coherent with the Pacer's principle ("name a budget below current state; force restructure") but its gap-to-advisory collision (hard below §2a advisory 90K) is its own admitted problem:
- **[01a, Q2]** "Hard ceiling is below §2a advisory (90K) — that's incoherent, because it would mean the advisory layer never gets to fire before the hard ceiling already has. ... The only coherent placements are: (a) Hard budget *between* advisory and activation (soft somewhere below). This is 95K/85K territory."

But the Pacer's resolution — placing hard between advisory (90K) and activation (100K) — inherits the Outsider's "moving the trigger" critique from a different direction: the hard is below activation, meaning the 100K activation threshold loses its distinctive signal.

**The Outsider's placement (hard at 100K = activation; soft at 90K = advisory) preserves the clean semantic layering** `[synth]`: §2a advisory (90K, reporting "pressure is real") and §2a activation (100K, reporting "structural revision warranted") retain their signals; the budget layer uses the same numbers but as enforcement ceilings rather than report-only. No double-signal at different numbers; no trigger-moving.

**Cross-family weighting for adoption at 100K/90K**:
- Outsider (non-Claude, cross-family) explicitly recommends 100K/90K with structural argument against alternatives.
- Pacer-advocate's rejection of own-2023-values (80K/90K) and preference for values above advisory aligns with "not below advisory" but differs in placement (Pacer: 85K/95K between advisory and activation; Outsider: 90K/100K matching advisory/activation).
- Synthesiser's 110K/120K is contradicted by Outsider's laundering critique; Synthesiser-original `[01c, Q2]` "adoption-in-violation is bad specification design" critique applies to Pacer's 85K/95K but does not cleanly apply to Outsider's 100K/90K paired with remediation (remediation means the engine enters compliance in the same session it adopts the budget).
- Skeptic's 100K/105K fallback (if conversion forced) is close to the Outsider's 100K/90K; both prefer field-tested numbers.

**Synthesis decision-weight: adopt at 100K hard / 90K soft** `[synth]`. Decision record proposes this shape for Decide; alternative shapes (85K/95K Pacer; 110K/120K Synthesiser; no-conversion Skeptic) are preserved as first-class minorities with activation warrants per §6.

## §4 Q3 Remediation mechanism

**4-of-4 convergence on close-rotation as primary mechanism. 3-of-4 convergence on structured two-stage soft/hard response. Detail divergence on retention window (3, 6, or 10 sessions).**

Convergence on close-rotation:
- **[01a, Q3]** "Rotate aged close files to archive-surface. ... Proposed revision: close files older than the three most recent sessions rotate to archive-surface."
- **[01b, Q3]** "[The softer-intervention path includes] old-close rotation (move `03-close.md` files from Sessions 022–024 to archive-surface, retaining 025+ in default-read)." [Effectively 3 sessions retained]
- **[01c, Q3]** "**Close-rotation rule**: `03-close.md` files from sessions older than the current session minus **10** are rotated from default-read to archive-surface."
- **[01d, Q3]** "Rotate aged `03-close.md` files to archive surface first. ... I recommend the most recent **6** session closes, plus any older close that is explicitly cited by an active specification or open issue for currently load-bearing governance."

Divergence on retention window: 3 (Pacer, Skeptic), 6 (Outsider), 10 (Synthesiser).

Two-stage soft/hard mechanism structure:
- **[01a, Q3]** Tier-1 soft 85K: "next close must include restructure block with named target trim and post-trim aggregate." Tier-2 hard 95K: "restructure is immediate ... no new substantive-deliberation content may be added to default-read until aggregate returns below 85K."
- **[01c, Q3]** Tier-1 soft 110K: "validator emits a remediation directive ... next session must include at least one aggregate-reducing action." Tier-2 hard 120K: "session that crosses it cannot close without executing a remediation action that returns aggregate below 118K."
- **[01d, Q3]** Tier-1 soft 90K: "session close must report aggregate total, delta from prior close, and the main growth driver; must name a concrete remediation candidate for the next crossing, chosen from a closed list." Tier-2 hard 100K: "session cannot close cleanly unless it also executes a restructuring that returns the default-read surface below hard. The remediation must be structural, not summarising."

`[synth]` The three adoption positions converge on: close-rotation as primary; two-stage response; hard threshold triggers mandatory-same-session restructure; soft threshold triggers next-session directive (or current-session reporting). Values differ, mechanisms converge.

**Retention window decision-weight**: Outsider's 6-session recommendation plus cited-exception carries cross-family weighting and specific empirical reasoning (**[01d, Q3]** "Every `03-close.md` stays default-read. That is a rule, not an accident. Once the engine sees that the append-only class is the main pressure source, the response should target the rule"). The Synthesiser's 10-session window reasoning (minority-review cadences at 5–10 sessions) is considered but is preservable via the "cited-by-active-spec-or-OI" exception: minorities still being tracked (e.g., §5.3 activation at Session 027 referenced from §5.3 text itself) would keep their originating close in default-read via the citation exception.

**Synthesis decision-weight: adopt close-rotation with 6-session retention window + cited-by-active-spec-or-OI exception** `[synth]`. Pacer's 3-session window is preserved as first-class minority; Synthesiser's 10-session window is preserved as first-class minority.

## §5 Q4 / Q5 / Q6 / Q7 — Convergences and fine structure

### §5a Q4 (per-file interaction)

**4-of-4 convergence on orthogonal + supplementary.**

- **[01a, Q4]** "Orthogonal but reinforcing."
- **[01b, Q4]** "If adopted, aggregate ceilings must be explicitly specified as orthogonal, not override-capable."
- **[01c, Q4]** "Orthogonal supplement, not override."
- **[01d, Q4]** "Supplementary and orthogonal."

Adoption per 4-of-4 convergence. No minority preserved here (no dissent surfaced). `[synth]`

### §5b Q5 (engine-version interaction)

**3-of-4 convergence on: engine-v5 bump per substantive revision; keep §5.4 cadence separate per OI-018. 1-of-4 (Synthesiser) prefers "engage engine-version in this deliberation, not separately" — but this reduces to the same outcome (engine-v5 bump now) with different framing (record interaction with §5.4 without re-opening OI-018).**

- **[01a, Q5]** "Engage minimally here; keep the substance under OI-018. ... What I am proposing clearly warrants a version bump. I am not arguing for re-examining cadence policy in this deliberation."
- **[01b, Q5]** "Do not engage §5.4 cadence in this deliberation; keep separate per OI-018."
- **[01c, Q5]** "Engage engine-version in this deliberation, not separately. ... engine-v5 supersedes engine-v4. ... A legitimate substantive-revision bump does not re-engage cadence minority."
- **[01d, Q5]** "Treat engine-version cadence as a separate issue per OI-018, not as a co-decided question inside this deliberation. ... this bump is content-driven rather than ceremonial, responds to a pre-named activation condition, and does not by itself settle OI-018 one way or the other."

Synthesis `[synth]`: engine-v4 → engine-v5 bump adopted per substantive revision. §5.4 cadence minority remains activated-not-escalated; OI-018 remains open; this bump does not escalate §5.4 (not a cadence event in the R9 sense; R9 aged out Session 026).

### §5c Q6 (methodology-level observation)

**Mixed: Pacer says mechanism-working; Skeptic says mechanism-gap; Synthesiser and Outsider say working-with-revealed-gap. Net: 3-of-4 acknowledge some gap exists; 1-of-4 (Pacer) treats the gap as a Pacer-vindication-data-point rather than a mechanism-gap.**

- **[01a, Q6]** "Mechanism-working. ... This is not a mechanism gap — §2a was designed to be advisory-plus-activation ... but it is evidence that advisory-only reporting does not by itself change behaviour."
- **[01b, Q6]** "§2a fired as designed at the arithmetic level, but its firing has exposed a gap in what 'firing as designed' means for a numerically-specified watchpoint. ... the gap the Pacer-advocate names (watchpoint-without-action) is not cured by hard-budget (action-without-calibration). It is cured by calibration — by pairing the threshold with a pressure-signal audit."
- **[01c, Q6]** "Partially fired as designed, and partially revealed a mechanism gap. ... The gap is the absence of a **between-stage procedure**: what happens between advisory emission and activation crossing?"
- **[01d, Q6]** "Mechanism working, with one revealed gap: the sensing worked, but the actuation was deferred. ... The engine already had a sensor. It did not yet have a controller. This deliberation should add the controller."

Substantive convergence `[synth]`: the mechanism "sensed" correctly but lacked "actuation" path between advisory and activation. The Outsider's control-systems framing (sensor + controller) is the clearest articulation. Session 028's adoption of budget-tier with two-stage response adds the actuation path. Skeptic-preserver's "pressure-signal audit" dimension (calibration against observed friction rather than arithmetic alone) is a separate concern — preserved as first-class minority per §6.

Synthesiser's proposed new OI ("Specify advisory-review procedure in `read-contract.md` so advisory emissions link to explicit decision-points rather than relying on voluntary between-stage response") `[01c, Q6]`: subsumed by Session 028's adoption (the new budget tier's soft-warning directive serves as the decision-point). No separate OI opened.

### §5d Q7 (anti-laundering self-check)

**3-of-4 (Pacer, Synthesiser, Outsider) judge that new information since Session 023 justifies adoption while requiring revision. 1-of-4 (Skeptic-preserver) judges new information as insufficient and running against conversion.**

The key disagreement is over what counts as "new information":
- Adoption majority: the empirical trajectory (83K → 105K over six sessions), the identification of close-file accretion as dominant growth driver, the observed §2a-advisory-insufficiency pattern (3 sessions of advisory without remediation), and the retroactive §5.2 vindication all constitute substantial new information.
- Skeptic-preserver dissent: trajectory data is expected; growth-driver identification argues for softer intervention; §5.2 vindication argues *against* conversion (precedent for preserve-through-threshold-firing).

The Outsider's cross-family position: **[01d, Q7]** "Does activation-firing itself count as new information? **Yes, but only procedurally.** It tells you that a pre-named condition has now occurred. It does **not** by itself prove that the original minority's exact numbers were correct. Treating activation as automatic proof of 90K/80K would be a laundering move in the opposite direction: turning 'reconsider now' into 'adopt literally.'"

`[synth]` This is the synthesis view: activation-firing is procedural evidence that the pre-committed condition obtained, which authorises re-deliberation at preferred-direction status but does not mandate adoption at preserved values. Session 028's adoption-with-revision honours this discipline. The Skeptic-preserver dissent on whether adoption-at-all is warranted remains a first-class minority.

## §6 First-class minorities preserved at Session 028 close

Three minority positions from this deliberation are preserved with activation warrants:

### §6.1 — Skeptic-preserver defer-to-softer-intervention minority (adversarial role)

**Position:** Continue preservation of §5.3 rather than converting. Execute softer intervention bundle (close-rotation alone + prompt-level guidance) and observe at Session 029–031 whether softer mechanisms suffice before adopting a hard budget. Activation-firing is procedurally acknowledged but empirically insufficient evidence for conversion in this session.

**Arguments preserved** `[01b, Q1–Q7 passim]`: (i) 100K threshold set without empirical grounding; crossing is arithmetic, not pressure-evidence; (ii) §5.2 vindication precedent supports preservation-through-activation-firing; (iii) aggregate hard budgets are higher-order intervention than per-file — warrant more deliberation than one session allows; (iv) proportionate response to activation is softer-intervention-first, with conversion reserved for if soft fails; (v) Session 024 A.4 carry-the-warning deliberation precedent against bind-by-budget applies here.

**Activation warrant:** If within 3 sessions (Session 029, 030, 031) of Session 028 adoption the new budget (100K/90K) fires only through accretion-growth with no observable operational friction, and a Session-031 retroactive measurement shows softer interventions alone (close-rotation + prompt-guidance, without hard-budget compliance-forcing) would have achieved equivalent aggregate reduction, the Skeptic-preserver position is retroactively vindicated. Session 031+ should revisit whether the hard-budget formalism was operationally necessary or ceremonially sufficient.

### §6.2 — Pacer-advocate 85K/95K tighter-values minority

**Position:** If adopting conversion, use 85K soft / 95K hard (between §2a advisory and activation). Forces near-term restructure more aggressively than 90K/100K; exerts stronger forcing function.

**Arguments preserved** `[01a, Q2]`: the Outsider's 90K/100K adoption leaves the engine hovering just-at ceilings; 85K/95K gives enforcement-side headroom below the reporting-side signals. "Soft 85K / Hard 95K ... requires trimming ~20,400 words to reach soft. That's substantial — it's about 19% of current default-read content. It is not trivial, but it is tractable."

**Activation warrant:** If within 5 sessions (Session 029–033) of Session 028 adoption the new budget (100K/90K) fires twice or more without compensating restructure forcing actual remediation, the Pacer-advocate tighter-values position becomes preferred revision direction. Tighter values would have forced remediation earlier. Session 033+ should reconsider 85K/95K values.

### §6.3 — Synthesiser-integrator 110K/120K headroom-values minority

**Position:** If adopting conversion, use 110K soft / 120K hard (above current-state aggregate). Avoids specification-in-violation; gives 2–3 sessions of forcing-function horizon before next contact.

**Arguments preserved** `[01c, Q2]`: "The engine should not engineer emergencies into its specifications. ... Setting hard at 120K gives roughly 14K headroom, which under current growth rates means approximately 2–3 sessions before the next proximity event."

**Activation warrant:** If within 3 sessions (Session 029, 030, 031) of Session 028 adoption the paired close-rotation + 100K/90K budget causes remediation-chaos (forced restructure in mid-deliberation; content-coherence damage from emergency compliance; deliberation distortion to stay under hard), the Synthesiser-integrator headroom-values position becomes preferred revision direction. Higher values with more headroom would have permitted smoother adaptation.

### §6.4 — Synthesiser-integrator 10-session retention-window minority

**Position:** If adopting close-rotation, use 10-session retention window (rather than 6). Minority-review cadences historically operate in 5–10 session range (§5.4 aged out at 9, §5.2 vindicated at 5); retaining 10 preserves the full recent-history band.

**Arguments preserved** `[01c, Q3]`: "Cross-session patterns (close-verbosity flagged at n=2, activation warrants firing at n=4) operate in the 3–7 session range. Ten sessions retains the full recent-history band while releasing older history to archive-surface."

**Activation warrant:** If within 6 sessions of Session 028 adoption the 6-session window + cited-exception mechanism produces a case where a 7–10-session-back close is consulted via citation-fetch more than twice per session on average (indicating the 6-session window is too narrow), the Synthesiser 10-session window becomes preferred revision direction.

### §6.5 — Pacer-advocate 3-session retention-window minority

**Position:** If adopting close-rotation, use 3-session retention window. Aggressive; simpler; maximises aggregate reduction; matches Skeptic's softer-intervention framing.

**Arguments preserved** `[01a, Q3]`: "Rotate aged close files to archive-surface. ... Proposed revision: close files older than the three most recent sessions rotate to archive-surface."

**Activation warrant:** If within 6 sessions of Session 028 adoption the 6-session window proves insufficient for aggregate control (sessions consistently approach the new soft 90K), the Pacer 3-session window becomes preferred revision direction.

### §6.6 — Skeptic-preserver pressure-signal-audit minority (new methodological observation)

**Position (methodology-level, not tied to a specific revision):** Numerically-specified watchpoints with no pressure-signal pairing can fire mechanistically without corresponding to the state they were meant to indicate. The engine should audit existing watchpoints (per-file budgets, aggregate budget, tokenisation-drift watches) for whether they pair with pressure-signal evidence.

**Arguments preserved** `[01b, Q6]`: "A well-designed watchpoint would either: (a) be calibrated against observed pressure signals, so that firing carries information about actual state, not just arithmetic; or (b) be paired with a pressure-signal audit that runs at firing-time to validate whether the threshold crossing corresponds to operational reality."

**Activation warrant:** If any Session 029+ budget-firing (per-file or aggregate) surfaces a case where the firing triggers remediation work that later proves operationally unnecessary (i.e., no observable friction would have resulted from non-remediation), this minority's preferred revision direction is to add pressure-signal audit procedures to `read-contract.md` §8 and to `validate.sh` checks 20/21/22.

## §7 Limitations (per MAD v4 §Limitations — mandatory content)

- **All four Claude-subagent perspectives share the Claude model family** (Pacer-advocate, Skeptic-preserver, Synthesiser-integrator). The Outsider provides one cross-family participant; three Claude perspectives share priors.
- **Intra-Claude-family size-mixing did not occur this session** (all three Claude perspectives were Opus 4.7).
- **Parallel isolation prevented conversational anchoring** (each Claude subagent launched independently via Agent tool with no cross-visibility during independent phase). It does not prevent training-distribution anchoring.
- **Brief-writing had no adversary.** The convener (orchestrator Claude Opus 4.7) wrote the brief. Framing choices propagated identically to all perspectives via the byte-identical §§1–3, §5–§6 content. Role-specific §4 stances did vary; the Outsider received a differently-framed §4 (no role-pole pushed) per MAD v4 standard Outsider convention.
- **Synthesis step is the pattern's highest-risk single-agent re-entry point.** This synthesis is produced by the orchestrator Claude Opus 4.7. Mitigations applied: citation requirement (all perspective-attributed claims cite source file and question), synthesizer-original `[synth]` marking, dissent-preservation (§6 first-class minorities with activation warrants), quote-over-paraphrase for load-bearing claims.
- **Non-Claude participation depended on convener fidelity.** The Outsider response was committed verbatim from codex exec output; verification against original stdout is possible via the saved codex output file path recorded in the Outsider manifest `transport_notes`. No automated verification of faithfulness; the transport guarantee is over the record, not the generation.
- **A single non-Claude participant narrows OI-004 less than its presence suggests.** One Outsider selected via pre-registered CLI pathway from OpenAI does not eliminate model-family effects in how the question is framed. Closure of OI-004 requires sustained practice; this session contributes voluntary:required ratio progression (9→10:8) and criterion-3 data point (67→68) per §8.

## §8 OI-004 contribution

- **Participant qualifies** per MAD v4 §Criterion-4 Articulation: `participant_organisation: openai`; `claude_output_in_training: known-no`; `independence_basis: organization-distinct`; stable attribution at `provider` / `model_family` / `model_id` / `model_version` granularity (some fields are `unknown` per disclosed operational limits but provider + family + id are known).
- **Criterion-3 evidence (recorded impact)**: the Outsider's "laundering the activation" critique `[01d, Q2]` materially shaped the synthesis decision on values (adopt 100K/90K rather than 110K/120K or 85K/95K). This is a documented cross-lineage divergence-from-Claude-consensus where synthesis adopted the non-Claude position — the three Claude perspectives each proposed different values (85K/95K, no-conversion, 110K/120K); the Outsider's 100K/90K plus its laundering critique is the load-bearing argument that disambiguated the value decision.
- **OI-004 tally update**: voluntary:required 9:8 → 10:8; criterion-3 cumulative 67 → 68.
- **Cross-family contradiction-prevailing data point**: the laundering critique prevails over the Synthesiser's headroom argument in the synthesis. Per Session 021 D-082 P4 Assertion requirement, this is a cross-lineage divergence case where synthesis adopted a position that substantively augments Claude-consensus — "laundering" as a framing was not in any Claude perspective; it entered via Outsider and structured the final values decision.

## §9 Brief-factual-error check (per Session 023 precedent)

The Outsider's Honest Limits declared workspace reads: read-contract.md, engine-manifest.md, OI-018.md, validate.sh aggregate-report section, Session 027 close, Session 028 00-assessment.md. No brief-factual-errors flagged by the Outsider in its Q1–Q7 content. The brief's §3 aggregate-trajectory table matches validator-measured values `[01d, Q7]` "At Session 027 close it was 105,399 words at Session 028 open" — the Outsider cites the measured 105,399 matching the brief.

## §10 Recommendation to Decide

1. **Adopt §5.3 direction as active specification** per 3-of-4 cross-family weighted convergence.
2. **Budget values: 100K hard / 90K soft** aggregate default-read surface per cross-family weighted plurality.
3. **Close-rotation with 6-session retention window + cited-by-active-spec-or-OI exception** per cross-family weighted plurality.
4. **Per-file budgets retained unchanged** (orthogonal supplement, 4-of-4 convergence).
5. **Engine-v4 → engine-v5** per substantive revision (4-of-4 acknowledgement that bump follows).
6. **§5.4 cadence minority remains activated-not-escalated**; OI-018 remains open per 3-of-4 convergence on "keep separate."
7. **§2a advisory/activation thresholds retained** as sensor layer; the new budget layer adds the actuation path.
8. **Six first-class minorities preserved** per §6 above with specific activation warrants.
9. **Session 028 close executes immediate remediation** (close-rotation) sufficient to return aggregate below new 100K hard, avoiding specification-in-violation at adoption time.
10. **OI-004 tally updates**: voluntary:required 9:8 → 10:8; criterion-3 cumulative 67 → 68.

The Decide step (`02-decisions.md`) operates on this recommendation.
