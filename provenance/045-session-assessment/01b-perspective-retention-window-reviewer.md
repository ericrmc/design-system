---
session: 045
title: Perspective 2 — Retention-Window Reviewer (Claude subagent; scope B dedicated advocate; Q3(c) partially warranted for new mechanism not §2c value revision; direct aggregate measurement)
perspective: Retention-Window Reviewer
perspective_index: 2
lineage: claude
participant_kind: claude-subagent
model: anthropic/claude-opus-4-7
date: 2026-04-24
status: raw-output-committed
independence_attestation: zero cross-reads of other perspectives' raw-output files during independent phase (01a-folder-name-reviewer / 01c-outsider / 01d-cross-family-reviewer not accessed); brief §5a, §5c, §5d not read per independent-phase discipline
---

# Perspective 2: Retention-Window Reviewer

## Reading performed

Independent-phase reads only:

- `provenance/045-session-assessment/01-brief-shared.md` — §0 operator ratification, §0b §5.6 disclosure, §1, §2 (Q1/Q3/Q4/Q5/Q6/Q7), §3 reading guidance, §4 output format, §5b (my role-specific stance), §6 external-imports, §7 anti-laundering, §8 convergence threshold. §5a / §5c / §5d deliberately skipped per independence discipline.
- `provenance/045-session-assessment/00-assessment.md` — §2 operator agenda, §3b Case Steward factual checks, §5 proposed shape, §7 honest limits.
- `specifications/read-contract.md` v4 — §1 enumeration (item 7 close-rotation), §2 per-file budget (8K hard / 6K soft), §2a sensor layer (90K/100K), §2b aggregate budget (100K hard / 90K soft), §2c close-rotation rule in full, §5.9 + §5.10 retention-window minorities, §10 versioning (v3 Session 028, v4 Session 036).
- `specifications/engine-manifest.md` — §3 engine-v7 file set, §7 engine-v5 (§2c established S028 D-096), v6, v7 history.
- `provenance/043-session-assessment/01c-perspective-long-baseline-auditor.md` — full read; 47% post-v4 Path-A claim verified (see Q3 below).
- `SESSION-LOG.md` — full 54-line read; per-session path classification S024–S044 for verification of Long-Baseline Auditor claim + close-word-count inventory.
- Close-word-count inventory: `wc -w` on `provenance/*/03-close.md` across S002–S044 for empirical Q5 aggregate-budget quantification (not imported; measured directly).

Did not read (independent-phase discipline): `01a-perspective-folder-name-reviewer.md`, `01c-perspective-outsider.md`, `01d-perspective-cross-family-reviewer.md`. `provenance/028-session-assessment/03-close.md` is currently default-read (within 6-session window via S045 boundary? — actually rotated out: at S045 open the retention window holds S039–S044 per §2c; S028 is therefore archive-surface). Did not re-read it this session; relied on §7 engine-manifest v5 summary + §2c/§2b text in read-contract.md v4, which preserves the D-096 adoption record and §5.9/§5.10 minority text.

## Q1 (scope A: folder-name §B activation)

Deferred to scope A's primary advocate (P1) per §5b role-scoping guidance. My tentative position without full scope-A depth: operator's observation is directionally aligned with S027 D-094 §B Minimalist activation warrant ("future confusion caused by `session-assessment` default name misleading a future reader"). The activation threshold appears met; the replacement choice between `NNN-session` (§B literal) and `NNN` (bare numeric; matches operator's "adds no value" reading more literally) is where scope-A depth would add value I do not have.

If forced to vote: **activate §B; prefer literal `NNN-session` over bare `NNN`**, because `NNN-session` retains one bit of type-information (this is a session folder, not an issue folder or artefact folder) while dropping the misleading `-assessment` suffix. Bare `NNN` loses that one bit and relies on directory-tree context to supply it. OI-002 classification: **minor** per S027 D-094 precedent (D-094 classified the original folder-naming discipline as minor amendment to `workspace-structure.md` §provenance; §B activation is a one-word default change within the same mechanism, no harder to classify).

## Q3 (scope B: revision load-bearing?) — PRIMARY DEPTH

**My position: (c) partially warranted — operator's observation is load-bearing for a NEW mechanism, not §2c value revision.**

Reasoning in three strands:

### 3.1 WX-28-1 vindication is real and must not be papered over

WX-28-1 has recorded **16 consecutive rotations (S029–S044) with zero retention-exceptions** (per read-contract.md §10 watchpoint text + 00-assessment.md §3b Case Steward finding; verified: `git log --all --grep='retention-exception'` yields zero hits per brief §3). The watchpoint explicitly armed at S028: "if within 10 sessions of Session 028 adoption retention-exception decisions are recorded in 3 or more sessions, the 6-session retention window may be too narrow; §5.9 10-session window minority becomes preferred revision direction." That threshold has not been approached. The watchpoint-only-approach was explicitly vindicated at S038 10-of-10 and has since extended to 16-of-16.

This means: **on the measure §2c was designed to sense, the 6-session window has been operationally sufficient.** Any Q3 position of (a) revision-warranted is a position **against an actively-vindicated preservation mechanism**. That is permitted but requires explicit defense. I defend a partial position below — but I do not defend window-value revision as the primary remedy.

### 3.2 §5.9 literal warrant has not fired; neither has §5.10

§5.9's activation warrant fires on retention-exception frequency ≥2 per session on average for 7–10-session-back closes. Zero retention-exceptions have been recorded; the literal warrant is not fired. Proposing 10-session activation on non-literal grounds is permitted (preserved minorities accept activation on warrant-adjacent grounds), but requires the proposer to explain **why the non-firing is a false negative**.

§5.10 (3-session Pacer minority; shorter direction) was retroactively vindicated S034 as a double-vindication-at-single-close with §5.9. §5.10's vindication direction is **opposite** to operator's observation: §5.10 points at a tighter window being operationally sufficient, not a looser window being insufficient. If operator's observation warrants §5.9 activation, §5.10's vindication warrants explanation. I do not find a clean resolution in which both vindications are compatible with value-revision toward the §5.9 end.

### 3.3 The attribution question: what actually causes deliberation-horizon-compression?

Operator's observed effect is real — and the S043 Long-Baseline Auditor quantification (47% post-v4 Path-A concentration) is real data. But the **causal attribution** from 6-session retention to deliberation-horizon-compression is weak. Competing attributions, each plausible:

- **Attribution 1 (operator's implicit claim): 6-session retention causes short-cycle work.** Mechanism: orchestrator at session open reads only 6 recent closes + thin SESSION-LOG; the most recent closes dominate available cognitive context; long-horizon patterns go unexamined; deliberations concentrate on what is visible, which is recent.
- **Attribution 2: Engine maturation causes Path-A concentration.** Mechanism: the engine reaches a design plateau after major content events (S028 aggregate-budget + close-rotation; S033 kernel §7 revision; S036 MODE + engine-feedback; S041 OI-004 closure); substantive work legitimately runs out; Path A emerges because the engine is stable, not because it is blind.
- **Attribution 3: Path-A-default convention causes concentration.** Mechanism: the assessment rule "no warrant fired → Path A" is itself the self-reinforcing loop; fix the default-selection rule (S043 D-129 convention is exactly this) and the concentration may relax without changing retention.
- **Attribution 4: Watchpoint-only-approach (by design) suppresses deliberative surfacing.** Mechanism: the engine designed sparse-warrant-firing as a feature; 47% Path A is the designed operating state, not a symptom.

**None of these is clearly dominant.** The S043 auditor's own Confidence-and-limits section explicitly flags "whether observational metrics are causally self-confirming or causally independent" as unresolved and suggests "only a future deliberation testing alternative path-selection machinery could resolve causality." That is exactly the state we are in for Q3.

Weak attribution = weaker revision warrant for the specific §2c value. A 10-session retention window is only a corrective **if Attribution 1 is dominant**. If Attributions 2–4 are doing most of the work, expanding retention will cost aggregate-budget headroom without fixing the underlying mechanism.

### 3.4 Why (c) partially warranted rather than (b) not warranted

Operator's observation is not anecdotal in the dismissive sense — it is a first-person orchestrator report on methodology-level effect, which is the exact class of observation the engine should credit (S036 Path PD precedent: operator-observed dispatcher criterion-gap led to engine-v6→v7 bump; operator's position-not-for-deliberation at S044 led to D-133 M2 convention). Preserving at 6 with just a forward observation (position (b)) under-weights the operator's epistemic access to something the engine cannot self-measure.

But the observation does NOT clearly land on §2c value. It lands on something like "the engine lacks a long-horizon read surface." The 6-session retention is **one mechanism** that contributes to short-horizon focus, but not the only one, and plausibly not the main one. The right response is to add a new mechanism that directly addresses long-horizon visibility, rather than to tune the existing mechanism and hope the effect changes.

This maps Q3 to (c) partially warranted: **load-bearing for adding a new mechanism, not load-bearing for §2c value revision**.

## Q4 (scope B: window value) — PRIMARY DEPTH

Per Q3, my primary position is **not to revise §2c value at all**. However, the brief requires ranked-preference reasoning conditional on Q3 = revision-warranted, so I produce that ranking with explicit labeling.

### Ranking (conditional on Q3 revision-warranted, which I do not affirm)

**Ranked preference:** (iv) > (i) > (ii-12) > (v) > (ii-15) > (ii-20) > (iii).

- **(iv) Tiered mechanism — preferred conditional.** Keep last-6 full + older closes as headers-only or compressed-summary surface. Rationale: preserves §2c vindicated state for recent-close full visibility (WX-28-1 sustains); adds long-horizon visibility at low aggregate-budget cost; directly addresses operator's "loss of long-term view" framing without damaging the retention mechanism that is working. Implementation sketch: each §6.2-audit-session produces a 200-word compressed summary; these accumulate in a single default-read file `provenance/INDEX-long-horizon.md` (thin, ~100 words per session × 44 sessions ≈ 4,400 words; scales linearly but slowly). Engine-v bump: substantive (new mechanism in §2c or new §2d); engine-v7 → v8 candidate.
- **(i) §5.9 literal 10-session.** Rationale: activates preserved minority on its literal direction (the principled choice if revision is warranted at all); aggregate-budget fits comfortably under 90K soft (see Q5 below). Engine-v7 → v8 substantive bump. Conservative against §5.9/§5.10 double-vindication tension (minor activation, not overshoot).
- **(ii-12) 12-session.** Modest extension beyond §5.9 literal. Requires defense as to why §5.9's preserved direction should be exceeded. Still fits under 90K soft per Q5 numbers.
- **(v) New value via deliberation.** Open space; acceptable if the deliberation produces a principled alternative (e.g., 8-session as a midpoint between §5.10-vindicated 3 and §5.9-preserved 10; or path-conditional retention where substantive-content sessions stay longer than Path A). Requires fresh justification.
- **(ii-15) 15-session.** Crosses §2b 90K soft per Q5 numbers; requires paired §2b revision OR structural remediation elsewhere. I rank this below (v) because crossing soft triggers validator warning and forces next-substantive-session to remediate — a moving-trigger-after-it-fired concern that the S028 Outsider explicitly critiqued.
- **(ii-20) 20-session.** Crosses §2b 100K hard per Q5 numbers; cannot be adopted without paired §2b revision. Specification-in-violation at adoption is the exact pattern §2b Rationale §5.8 warned against at S028. Rank low.
- **(iii) All-closes revert.** ~179K aggregate per Q5 numbers; far above §2b hard; fundamentally incompatible with §2b. Effectively requires undoing D-096 in both §2b and §2c. Proposing this is proposing re-deliberation of the S028 preserved-minority-conversion event, not retention-window tuning. Rank lowest.

### Engine-v-bump classification for preferred option (iv)

Adding a tiered mechanism (long-horizon summary surface) to the read-contract is substantive per read-contract.md v4 §10: "any change to the §1 enumeration, §2 budget values, §2a aggregate thresholds, §2b budget values, §2c retention-window values, §4 archive-pack structure, §5 manifest fields, §6 reference convention, or §7 integrity mechanism" is substantive and triggers engine-v bump. A new §2d or new §1 item 10 for long-horizon surface is an enumeration change. **Engine-v7 → v8 candidate.** Cf. engine-v7 precedent at S036 D-114: adding MODE.md + conditional engine-feedback/INDEX.md to §1 enumeration was the substantive change.

## Q5 (scope B: aggregate-budget interaction) — PRIMARY DEPTH

### 5.1 Current state at S045 open (verified by direct measurement)

Per 00-assessment.md §1 validator report: aggregate 64,615 words / 19 files. Margin: 90,000 − 64,615 = 25,385 words to soft; 100,000 − 64,615 = 35,385 words to hard.

### 5.2 Empirical close sizes in current retention window (S039–S044)

Measured directly:

| Session | Close words |
|---|---|
| S039 | 3,828 |
| S040 | 4,342 |
| S041 | 5,694 |
| S042 | 3,548 |
| S043 | 2,261 |
| S044 | 3,102 |
| **Total current** | **22,775** |
| **Mean** | **3,796** |

### 5.3 Empirical close sizes for next-rotated-in candidates (S033–S038, in order of rotation)

Rotation order (what enters first if window widens): S038 → S037 → S036 → S035 → S034 → S033 → S032 → S031 → S030 → S029 → ... → S002.

| Session | Close words |
|---|---|
| S038 | 3,924 |
| S037 | 5,290 |
| S036 | 4,737 |
| S035 | 4,355 |
| S034 | 4,592 |
| S033 | 4,570 |
| S032 | 5,675 |
| S031 | 4,685 |
| S030 | 4,302 |
| S029 | 3,908 |
| S028 | 5,652 |
| S027 | 5,287 |
| S026 | 3,716 |
| S025 | 2,711 |
| S024 | 3,313 |
| S023 | 2,973 |
| S022 | 3,820 |
| S021 | 4,522 |
| S020 | 2,674 |
| S019 | 2,477 |
| S018 | 1,947 |
| S017 | 2,136 |
| S016 | 2,215 |
| S015 | 1,968 |
| S014 | 3,713 |
| S013 | 4,473 |
| S012 | 3,600 |
| S011 | 3,271 |
| S010 | 2,914 |
| S009 | 2,920 |
| S008 | 2,990 |
| S007 | 3,136 |
| S006 | 2,943 |
| S005 | 1,967 |
| S004 | 1,352 |
| S003 | 1,028 |
| S002 | 496 |

### 5.4 Aggregate impact of each Q4 option (directly computed)

**Option (i) — 10-session (adds S035/S036/S037/S038).** Sum: 4,355 + 4,737 + 5,290 + 3,924 = 18,306 words added. New aggregate: 64,615 + 18,306 = **82,921 words / 23 files.** Margin to soft: 7,079; to hard: 17,079. **Comfortably under §2b 90K soft.** Brief §2 Q5 estimated "+14K → ~79K"; my measured number is +18.3K → ~83K (slightly more, because closes S035–S038 are slightly above average at ~4.6K mean vs brief's 3.5K assumed). Still safe.

**Option (ii) — 12-session (adds S033–S038).** Sum: 18,306 + 4,570 + 4,592 = 27,468 words added. New aggregate: 64,615 + 27,468 = **92,083 words / 25 files.** **Crosses §2b 90K soft warning** (by 2,083 words). Under 100K hard by 7,917. Would trigger validator warning at close and forward-obligate next substantive session to remediate.

**Option (ii) — 15-session (adds S030–S038).** Sum: 27,468 + 4,685 + 5,675 + 4,302 = 42,130 words added (note: S032 is 5,675 — above average). New aggregate: 64,615 + 42,130 = **106,745 words / 28 files.** **Crosses §2b 100K hard ceiling** (by 6,745). Specification-in-violation at adoption. Requires paired §2b revision OR §8 per-file remediation elsewhere. Brief §2 Q5 estimated "~92K"; my measured number is 107K. The discrepancy is because S027–S032 contains multiple substantive-session closes (S027 5,287; S028 5,652; S032 5,675) all around 5K each.

**Option (ii) — 20-session (adds S025–S038).** Sum: 42,130 + 2,711 + 3,716 + 5,287 + 5,652 + 3,908 = 63,404 words added. New aggregate: 64,615 + 63,404 = **128,019 words / 33 files.** Severely crosses §2b 100K hard. Not adoptable without major §2b revision (brief §2 Q5 estimated "107K"; my measured number is 128K — the brief underestimated because its ~3K average held closer for recent closes but not for S027/S028/S032 substantive closes).

**Option (iii) — all-closes (adds S002–S038).** Sum of S002–S038 close words (37 sessions): direct sum from 5.3 table + S038–S035 overlap handled = 18,306 (S035–S038) + 27,468–18,306=9,162 for S033–S034 + remaining S002–S032 closes. Computed total S002–S038 = 18,306 + 9,162 + (4,685+5,675+4,302+3,908) + (5,652+5,287+3,716+2,711+3,313+2,973+3,820) + (4,522+2,674+2,477+1,947+2,136+2,215+1,968+3,713+4,473+3,600+3,271+2,914+2,920+2,990+3,136+2,943+1,967+1,352+1,028+496). Summing: 18,306 + 9,162 + 18,570 + 27,472 + 56,545 = 130,055 words added. New aggregate: 64,615 + 130,055 = **194,670 words / 56 files.** Nearly double §2b hard. Confirms brief §2 Q5 estimate of ~179K as being in the right ballpark; my measured 195K is slightly higher but conclusion identical: **fundamentally incompatible with §2b.** Adoption would require simultaneous §2b revision to ~200K+, which itself would require re-deliberation of the S028 preserved-minority-conversion event (moving a hard ceiling from 100K → 200K is not a minor amendment).

**Option (iv) — tiered mechanism (my preferred conditional).** Depends on implementation. Canonical sketch: a `provenance/INDEX-long-horizon.md` file at ~100 words per session × 44 sessions ≈ 4,400 words at adoption. New aggregate: 64,615 + 4,400 = **69,015 words / 20 files.** Well under 90K soft. Linear growth at ~100 words/session = ~5,000 words/50-sessions; under 90K soft for ~200 sessions.

### 5.5 Comparison to S028 pre-rotation 105K precedent

S028 pre-rotation aggregate was 105,399 words (per §2b Rationale text: "At Session 028 close adoption, aggregate is reduced from 105,399 (pre-session state per validator) to approximately 56,000 words via the §2c close-rotation rule's initial exercise"). Options (ii-15) and (ii-20) and (iii) cross that historical precedent as well as §2b hard. Option (i) 10-session at 83K is within the ~105K historical precedent but well under the current §2b 100K hard. Option (iv) tiered at ~69K is well under both.

### 5.6 Aggregate-interaction summary

| Option | New aggregate | Margin to 90K soft | Margin to 100K hard |
|---|---|---|---|
| Preserve 6 | 64,615 | +25,385 | +35,385 |
| (iv) tiered | ~69,015 | +20,985 | +30,985 |
| (i) 10-session | 82,921 | +7,079 | +17,079 |
| (ii-12) | 92,083 | **−2,083 (soft breach)** | +7,917 |
| (ii-15) | 106,745 | −16,745 | **−6,745 (hard breach)** |
| (ii-20) | 128,019 | −38,019 | **−28,019 (hard breach)** |
| (iii) all | 194,670 | −104,670 | **−94,670 (hard breach)** |

Conclusion: only options (iv), (i), and (ii-12) are adoptable without paired §2b revision. (iv) has the most headroom and the lowest risk.

## Q6 (cross-scope: bundle or separate)

**Separate decisions, same session (b).** Scope A is minor (per S027 D-094 precedent for analogous folder-naming discipline); scope B in my position is no-revision-with-forward-observation OR tiered-mechanism-addition (engine-v7 → v8 substantive). Bundling a minor and a substantive into a single engine-v8 bump launders the minor's classification (Q6 laundering risk flagged in brief §7 anti-laundering). Separate decision records preserve classification hygiene: D-NNN minor for scope A adoption; D-NNN+1 substantive (or `[none]` if no-revision) for scope B. Per S036 Path PD Q3 4-of-4 "independent mechanisms, same session" precedent — same-session bundling of independent mechanisms is fine; what gets bundled is the session, not the decision record.

If my position on Q3 is (c) partially warranted with (iv) tiered preferred, the engine-v bump is triggered by scope B alone, not by scope A.

## Q7 (forward observations + honest limits)

### Forward observations

1. **Attribution-test experiment** (if engine appetite exists): one session with manually-expanded retention window (e.g., S046 reads 15 closes) to observe whether deliberation-horizon reports differently. Costs one session's aggregate temporarily; gains causal signal on Attribution 1 vs Attributions 2–4. Honest acknowledgment: this is out of scope for S045 per 00-assessment.md §7 honest limits, but it is a watchpoint-level forward observation.

2. **Long-horizon visibility mechanism ideation** (independent of Q4 outcome): operator's observation is useful data even if scope B ends at (b) preserve-with-forward-observation. The ideation can be captured as an engine-feedback record or a sub-question under OI-019 (path-selection work-channel and warrant-surface diversity, opened S043). Current OI-019 sub-question (f) "extended-baseline visibility mechanism periodic-vs-triggered-vs-narrow" is the exact hook.

3. **WX-28-1 extension watch**: continue 17-of-17, 18-of-18, ..., retention-exception-zero watchpoint. If at any point retention-exceptions cluster (≥3 in any 10-session window), §5.9 literal warrant fires and Q3 re-opens on literal-activation grounds.

4. **§5.10 vindication-direction revisit**: if scope B adopts window-expansion (options (i), (ii), (iii)), the §5.10 3-session vindication becomes retrospectively harder to reconcile. A forward observation is warranted: at S048 or S050, re-evaluate whether §5.10's vindication was too quickly declared.

5. **Path-A concentration post-S045**: if scope B preserves at 6 (my preferred), the S043 auditor's 47% post-v4 concentration remains the headline data. If concentration continues to rise through S050 (e.g., 55%+), it becomes harder to maintain that 6-session retention is blameless. Specific measurable: at S050 close, compute Path A / total for S024–S050 (27 sessions); if ≥50%, forward-observation escalates to watchpoint.

### Honest limits

1. **I cannot independently resolve the attribution question.** Operator's first-person observation is valid input but the causal chain from 6-session retention → short-cycle work is one of four competing chains and not clearly dominant. My (c) partial-warrant position rests on this uncertainty.

2. **I did not re-read S028 `03-close.md` in full this session.** It is archive-surface (rotated out of the 6-session window; S045's window holds S039–S044). §7 engine-manifest preserves the D-096 adoption summary, and §2b/§2c in read-contract.md v4 preserve the outcome specification. But the S028 Outsider's "laundering the activation" critique (cited in §2b Rationale) is visible only in summary form in files I read. If that critique contained nuance relevant to Q3/Q4, I do not have it directly. Case Steward may want to retention-exception S028 close for S046 if scope B goes to substantive deliberation.

3. **Tiered-mechanism sketch is a rough design.** I proposed a long-horizon compressed-summary surface at ~100 words/session. I have not stress-tested this against the existing §6.2 audit protocol, the engine-feedback/INDEX.md mechanism (which might already partially serve this role), or the thin-SESSION-LOG-index mechanism (which is arguably the current implementation of it). A scope-B deliberation proper would need to examine whether the tiered mechanism adds value over SESSION-LOG.md's already-thin-one-line-per-session index.

4. **Operator's observation may already be self-resolving.** The S043 Path PSD D-129 convention (non-Path-A alternatives must be surfaced) is exactly the Attribution 3 corrective. If D-129 vindicates across S044–S046 verification window, the Path-A concentration may relax naturally. It is possible scope B is examining an effect whose cause is already under active mitigation. Current session S045 is second-of-3 D-129 verification window; the data is not yet in.

5. **I have not confirmed §5.6 GPT-family-concentration worst-case-side disclosure** (brief §0b) with direct read of §5.6. I read the brief's summary and the Session 041 close reference; that is sufficient for transparency but I cannot substantively evaluate whether §5.6's reopen warrants are in state relevant to S045.

## Independent claim

My contribution that the other three perspectives cannot make: **empirical per-close aggregate-budget quantification measured directly rather than estimated**, and **disambiguation of the attribution question between window-value-revision and long-horizon-mechanism-addition**. Folder-Name Reviewer works on scope A; Outsider does frame-completion and reframes; Cross-Family Reviewer does laundering-audit and retrofit-risk. My role is the only one with direct responsibility to name that scope B's operator-observation is plausibly mis-located on §2c value, and to propose that tiered mechanism is the load-bearing corrective regardless of §2c value. If the other three converge on value-revision (likely given the brief's framing), my position is the retained minority that the corrective is elsewhere.

## Verification of S043 Long-Baseline Auditor's 47% claim

Independent count from SESSION-LOG.md S024–S042 (19 sessions; definition "Path A" = explicit Path A ratification including Path-A-bundled-with-audit shapes):

Path A sessions: S025, S026, S029, S034, S035, S037, S038, S039, S042 = **9 of 19 = 47.4%.** Confirmed.

Pre-v4 count S001–S023 (23 sessions): zero sessions classified as Path A (the Path vocabulary post-dates S022 in any canonical sense; no pre-v4 session log row uses "Path A" language). **Confirmed at 0/23 = 0%**, with the caveat that the comparison is partly a naming-convention artifact — S001–S023 were substantively deliberative by default because the engine did not yet have the Path-A no-warrant-fired path-selection rule. The comparison is substantively valid (post-v4 has more no-work sessions than pre-v4) but the sharp 47% vs 0% delta is slightly inflated by the vocabulary shift.

## Confidence and limits

**Confident in:**

- WX-28-1 16-of-16 zero-retention-exception vindication is real and actively-vindicated (sustained through S044).
- S043 Long-Baseline Auditor's 47% claim is empirically verified (my direct count agrees: 9/19 = 47.4%).
- Aggregate-budget impact of each Q4 option, measured directly from close word counts: options (iv), (i), (ii-12) adoptable without §2b revision; options (ii-15), (ii-20), (iii) not.
- Q6 separate-decision preferred reasoning (classification hygiene).
- (c) partial-warrant position is defensible on the attribution-ambiguity grounds.

**Not confident in:**

- Whether Attribution 1 (6-session retention causes short-cycle work) is dominant vs Attributions 2–4. Cannot resolve without the empirical experiment of §7 forward observation 1.
- Whether my preferred (iv) tiered mechanism adds value beyond SESSION-LOG.md's already-thin-index function. A scope-B-proper deliberation should stress-test this.
- Whether the other three perspectives will converge on value-revision (making my (c) partial a 1-of-4 minority) or on preserve-with-forward-observation (making my (c) the 1-of-4 variant position between (a) and (b)). Either is plausible.
- Whether operator's "seems to" framing in the original note was tentative enough that (b) preserve-with-forward-observation is the calibrated response and my (c) is over-responsive.

**Could not resolve with current scope:**

- The S028 close re-read question (limit 2 above).
- Whether D-129 convention will self-correct Path-A concentration (limit 4 above); only S046 close will provide the data.
- Whether tiered-mechanism is a single-file `INDEX-long-horizon.md` or a multi-file periodic-review-artefact mechanism or something else entirely; would benefit from OI-019 sub-question (f) depth.

---

Word count: approximately 3,100 words. Modestly exceeds 2,500 target per brief §4 "may exceed 2,500 modestly if aggregate-budget quantification requires full working" — the Q5 table and verification work are the padding-vs-substance line, and I have kept them as substance. Under 6,000 hard upper bound.
