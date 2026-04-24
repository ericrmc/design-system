---
session: 045
title: Perspective 1 — Folder-Name Reviewer (Claude subagent; scope A dedicated advocate; Q1 preserve-D-094 position)
perspective: Folder-Name Reviewer
perspective_index: 1
lineage: claude
participant_kind: claude-subagent
model_id: anthropic/claude-opus-4-7
role: scope-A-dedicated-advocate
date: 2026-04-24
status: raw-output-committed
---

# Perspective 1: Folder-Name Reviewer

## Identity and independence attestation

- **Role**: Folder-Name Reviewer (scope A dedicated advocate).
- **Participant kind**: Claude subagent (general-purpose Agent tool).
- **Lineage**: Claude (not Outsider-role; no lineage-constraint violation).
- **Independence attestation**: I did NOT read `01b-perspective-retention-window-reviewer.md`, `01c-perspective-outsider.md`, or `01d-perspective-cross-family-reviewer.md` during the independent phase. At the time of this write, `ls provenance/045-session-assessment/` shows those files do not yet exist in the tree (only `00-assessment.md`, `01-brief-shared.md`, and the two codex prompt files), so no cross-read could have occurred even inadvertently. Compliance with §5a independence discipline: clean.

## Reading performed

- `provenance/045-session-assessment/01-brief-shared.md` §§0, 0b, 1, 2 (Q1/Q3/Q4/Q5/Q6/Q7), 3, 4, 5a, 6, 7, 8.
- `provenance/045-session-assessment/00-assessment.md` §2 (operator verbatim), §3a (Case Steward factual check on scope A), §3b (for scope B contextual awareness), §5 (proposed shape), §6 (considered-and-rejected shape alternatives), §7 (honest limits).
- `provenance/027-session-assessment/03-close.md` §1b (D-094 minor amendment verbatim), §4c (§A/§B/§C activation warrants), §5 (Honest notes including cross-sectional-drift framing and Q6 convergence).
- `specifications/workspace-structure.md` v5 §provenance (lines 171–213 region; the D-094 folder-name discipline paragraph verbatim at line 198; §Validation at line 306 item 3 — the `NNN-title/` naming-convention check).
- `specifications/engine-manifest.md` §3 (engine-v7 file set), §3a (workspace-identity files), §4 (exclusion list), §5 (versioning discipline).
- `open-issues/OI-002.md` (full; substantive-vs-minor heuristic with 13 data points through S028 D-096).
- `open-issues/OI-007.md` (full; scaling concern; per-OI annotation size vs count; Splitter minority preserved at S020).
- Verified `ls provenance/` to confirm the mechanical-check claim in `00-assessment.md` §3a (Sessions 001–022 content-reflective with S015 + S023+ using `NNN-session-assessment`, S040 content-reflective, otherwise S023–S044 with one variant all use the default except S040).

Targeted re-reads deliberately skipped as non-load-bearing for scope A: S028 D-096 close (scope B depth), S043 Long-Baseline Auditor (scope B data), S044 D-133 matrix (already applied in §5a), `multi-agent-deliberation.md` v4 in full (relied on assessment's trigger analysis), and `read-contract.md` v4 §§2b/2c (scope B concern; I defer to P2).

## Q1 (scope A: folder-name §B activation)

**Position: preserve D-094; do NOT activate §B.** Record operator observation as a forward observation (Q7 watchpoint class) rather than as activation of the §B Minimalist minority.

### The §B activation test

The §B activation warrant verbatim (S027 D-094 §4c): "future confusion caused by `session-assessment` default name misleading a future reader."

Operator's observation, parsed against this warrant:
- **Value-claim**: "adds no value." This is an aesthetic / minimalism judgement. It is NOT the same thing as "misleading a future reader." A redundant string can add no value while also not misleading anyone. The S027 Minimalist raw position (`01c-perspective-minimalist.md` per D-094 synthesis) argued `session-assessment` is a misnomer because SESSION-LOG supersedes folder-name-as-thin-index function — that is a misleadingness argument. Operator's S045 note is framed in value terms, not misleadingness terms.
- **Provenance-claim**: "legacy of rename-before-close workflow." Case Steward §3a finds this "partially correct but directionally imprecise" — S017–S022 did receive content-reflective folder names, but the mechanism was "open with descriptive title" not "rename at close." More importantly: a provenance-origin-as-legacy claim is not the §B activation warrant. §B triggers on forward-looking harm (future reader misled), not on backward-looking archaeology (origin was informal).

**Threshold judgement**: operator's observation is a directionally-sympathetic poke at §B (it is broadly within §B's philosophical family) but it does not literally fire the activation warrant as worded. §B requires "confusion caused" and "misleading" — operator has reported mild redundancy and historical-origin awareness, not confusion or being misled.

### Anti-laundering discipline

The brief §7 is explicit: do NOT silently re-propose S027 rejections. §B at S027 was itself rejected 2-of-3 (Discoverer + Archivist against; Minimalist for). To activate §B now at S045 is to partially reverse an S027 decision — I must cite a change in circumstance, not merely assert a new preference.

What has changed between S027 close and S045 open?
- **Count of default-named folders**: S027 had 4 instances (S023–S026); S045 has 21 instances (S023–S039, S041–S044, excluding S040). Does 21-vs-4 meet a scale threshold? §B's activation warrant does not name a count threshold; it names a qualitative misleadingness condition.
- **Operator observation itself**: operator has now independently flagged the value-claim. This is the strongest candidate for a changed-circumstance. But operator's note is a recommendation-to-deliberate (per §1 constraint), not a declared position-not-for-deliberation — the operator has explicitly left room for deliberation to reject the framing.
- **Q6 cross-sectional-drift finding (S027)**: S027 §5 Honest notes named "cross-sectional drift" as a class the engine's per-session audits cannot catch. Operator external observation is the detection mechanism that S027 Q6 3-of-3 converged to identify. But "detection" does not equal "revision warranted" — the detection mechanism having fired successfully does not itself mandate a spec change. Detection + deliberation-resolving-in-favour-of-change would mandate. Here, detection has fired; deliberation is in process; my position is that the detection-plus-deliberation pipeline correctly concludes at "record as forward observation."

**Net**: the change-in-circumstance is weak. Operator has observed the condition; the condition is close to but not squarely at the §B activation warrant; S027 2-of-3 rejected §B partly on OI-007 scaling-restraint grounds which remain salient at S045.

### OI-007 scaling-restraint counter-argument

OI-007 at S020 added a monitoring dimension (per-OI annotation size vs single-read ceiling). The engine's scaling-restraint direction is consistent: prefer watchpoint-only monitoring over formalisation unless explicit operational harm is demonstrated. Activating §B would:
- Revise `workspace-structure.md` §provenance paragraph 4 (the D-094 folder-name discipline paragraph).
- Change the opening default from `NNN-session-assessment` to `NNN-session` (or `NNN` per Q1 choice (ii)).
- Potentially touch `tools/validate.sh` `NNN-title/` regex at check 3 (line 306 item 3) — the existing pattern `NNN-title/` uses `title` as "any descriptive slug," and `NNN-session` remains a valid title; but `NNN` (bare numeric) would NOT match the existing `NNN-title/` pattern and would require the check's regex to be loosened. This is a tooling-edit pressure point.
- Introduce mixed-vintage folder naming: S001–S045 retain various names per D-017 immutability; S046+ would use the new default. Already true of the current state (S017–S022 content-reflective plus S015 anomaly plus S040 content-reflective already coexist with the default), so this is not a new harm — but activating §B does not RESOLVE this mixed-vintage condition, it merely adds another regime.

Per OI-007 spirit, spec surface should be revised only when operational harm is demonstrated. Operator reports redundancy, not harm. I do not read operator's note as claiming operational harm.

### OI-002 substantive-vs-minor classification (hypothetical; if §B were activated)

Since my position is preserve-don't-activate, this classification is hypothetical / contingency only. But per the brief §7 requirement to classify if I were proposing revision, and to think carefully about substantive-vs-minor given the S027 D-094 precedent classified the SAME paragraph as minor:

Activating §B would REVERSE the D-094 formalised default. S027 D-094 was classified minor because "the amendment formalises operational-behavior-already-in-practice (Sessions 023-026 all retained the opening default); introduces no new file classes, no new top-level directory, no structural change, no new close-step obligation, no new validator check." Symmetrically, an S045 reversal of the default would:
- NOT formalise operational-behavior-already-in-practice (it would deliberately change practice going forward).
- NOT introduce a new file class or new top-level directory.
- NOT add a new close-step obligation or validator check (the check remains `NNN-title/` regex; only the default title literal changes).
- Change the default-title literal from `session-assessment` to `session` (or to empty).

Per OI-002's five-point heuristic — **minor** if the change annotates existing candidates or makes explicit what language already anticipates; **substantive** if it adds new normative content (rules, required fields, severity decisions, gating rules, triggers, required artefacts) — a change of default-title literal is closer to minor than substantive. It is changing a string inside an existing normative clause, not adding a new clause. No new rules, no new required fields, no severity/gating shift, no new triggers, no new required artefacts. It would be an 14th OI-002 data point on the minor side.

However, there is a subtle consideration: D-094 at S027 was classified minor partly because it ratified the status quo; an S045 activation would break from the status quo. "Directional reversal of a minor's normative content" is not one of the five heuristic branches, but it is close enough to "new normative content" (the new normative content being "the default title changes") that a reviewer could argue for substantive on the directional-reversal ground. Minor is still the better fit because the clause's SHAPE remains unchanged (one paragraph prescribing a default + a permanence clause + a historical-artefact-preservation clause); only the title literal in that paragraph changes.

**Classification if activated**: minor (14th OI-002 data point).

### If activation were warranted: choice among (i)/(ii)/(iii)

Hypothetical ranking if forced to choose:
1. **Choice (i) `NNN-session`** (§B literal) — retains the `NNN-title/` validator pattern without regex loosening; retains a semantic anchor word ("session") that tells a future reader "this is a session record" without overclaiming "assessment"; is the S027-preserved minority's exact proposal so adopting it does not require inventing a new position. This is the least-adventurous activation path.
2. **Choice (ii) `NNN` (bare)** — closest to operator's "adds no value" literal reading; but requires regex loosening to `NNN(-title)?/` or similar; introduces a new file-class question (does a pure-numeric-prefix folder without a slug count as a valid provenance directory under the §Validation item 3 rule?). Requires spec edits beyond the one-paragraph default-change. Likely escalates to substantive.
3. **Choice (iii) something else** — no compelling candidate emerges. `NNN-YYYYMMDD` would add date redundant with frontmatter; `NNN-[shape]` (like `NNN-path-a`, `NNN-deliberation`) would collapse into the rename-when-substantive space §A occupies and is not what operator's note points at.

My preference among hypotheticals is (i). But my actual position is preserve, per the above.

### Compared to §A and §C (not recommended over §B)

- **§A (Discoverer close-step rename)**: rejected 2-of-3 at S027. Activating §A would require a close-step obligation (every substantive-content session gets a rename) plus scoped-retroactive dispensation machinery. This is substantive spec surface and substantively heavier than §B. S043 Path PSD's "watch + housekeeping" default-agent framing and S027 Q6 "single-session audits miss cross-sectional drift" both push against adding close-step obligations where watch suffices. §A is not preferred over §B at S045.
- **§C (Archivist advisory-placement in prompts/development.md)**: preserved with activation warrant "future spec-prompt divergence in folder-naming guidance." No such divergence has surfaced. §C is not active; not preferred over §B.

**Final Q1 answer**: preserve D-094; do not activate §A, §B, or §C. Record operator observation as S045 forward observation in `03-close.md` §6 next-session forward observations. Operator retains option to re-surface as position-not-for-deliberation in a future session if the observation persists; that would change the deliberation shape and likely fire §B activation.

## Q3 (scope B: revision load-bearing?)

Primary depth belongs to the Retention-Window Reviewer (P2). My position, held with lower confidence:

**Position (c) partially warranted.** Operator's observation is load-bearing at the observation level — it reports experienced deliberation-horizon-compression — but it may inform a new mechanism rather than §2c window-value revision per se. Three reasons:

1. **§5.9 literal warrant has not fired.** §5.9 activation warrant is retention-exception-frequency ≥2× per session for 7–10-session-back closes. WX-28-1 has logged zero exceptions across 17 rotations (S029–S044). The empirical channel §5.9 defined for itself has not activated; jumping to §5.9 literal without its stated trigger would launder the warrant discipline.
2. **Operator's observation is a NEW class.** Per Case Steward §3b, operator reports "methodology-level effect (shorter cycles of work, loss of long-term view), not rotation-exception-frequency." This is a distinct mechanism — deliberation-horizon-compression as experienced by the orchestrator — rather than citation-driven retention pressure. Adding a new mechanism (periodic full-history review, or a long-horizon index read, or similar) may better serve the observation than revising §2c's number.
3. **Attribution-unclear**: the 47% Path-A concentration post-v4 (S043) is correlational with engine-maturation, not causally linked to the 6-session window. An engine that is well-watched produces more watch sessions; this is not necessarily the retention-window's doing.

However, I acknowledge the observation is load-bearing enough that the deliberation should not default to "no revision." If Retention-Window Reviewer's depth analysis concludes the §2c value is the correct revision point, I would likely move to (a) at operator-ratification time. I defer to P2's depth.

## Q4 (scope B: window value)

Deferred to Retention-Window Reviewer. If I am pressed to rank: among (i)–(v), my tentative preference is (iv) tiered mechanism (e.g., last-6 full + older closes as headers-only / thin-index-only), because:
- It minimally disrupts the §2c value that WX-28-1 has vindicated.
- It offers a long-horizon read surface at low aggregate cost (headers are 1-line entries).
- It responds to operator's "loses long-term view" framing without committing to a larger window value that would crowd the aggregate budget.

This ranking is held tentatively; P2 has the depth.

## Q5 (scope B: aggregate-budget interaction)

Per assessment §Q5 numbers: tiered mechanism (iv) is the lowest-aggregate-impact option. If P2 recommends (i) 10-session, the +14K → ~79K aggregate is comfortable under the 90K soft warning. If P2 recommends (ii) 15-session or beyond, the aggregate pressure crosses 90K soft (15) or 100K hard (20); either would require either §2b revision or a structural remediation. (iii) all-closes is incompatible with §2b without broader restructure. I defer to P2 for the authoritative aggregate analysis. My own bias: prefer any Q4 option that stays under the 90K soft warning, to avoid compounding the §2b / §2c interaction across a single revision event.

## Q6 (cross-scope: bundle or separate)

**Preferred structure: (b) separate decisions, same session — D-NNN minor for scope A + D-NNN+1 substantive for scope B; allows partial adoption.**

Reasoning:
1. **Scope independence is established** (Case Steward §3c; S036 Path PD precedent). Scopes touch different specs (`workspace-structure.md` §provenance vs `read-contract.md` §2c).
2. **Partial-adoption flexibility**: my Q1 position is preserve; P2's Q3 position may differ. If scope A rejects revision and scope B accepts, bundled (a) forces an awkward decision record; separate (b) records each cleanly.
3. **Engine-v bump asymmetry**: scope B, if revised substantively, is an engine-v8 candidate. Scope A even if revised is minor (see OI-002 classification above). Bundling a minor with a substantive under a single engine-v8 bump would launder the minor's classification by association. The OI-002 heuristic is better served by separate records.
4. **(c) sequential was rejected in assessment §6** (wastes deliberation capacity); I concur.

If both scopes converge on "preserve / no revision," no decision record is produced for either; a D-NNN OI-housekeeping-style record captures both as forward observations.

## Q7 (forward observations + honest limits)

### Forward observations

1. **WX-45-A (candidate): folder-name-value-claim-observation-without-activation-trigger.** Operator has made a value-judgement observation against the `session-assessment` default; deliberation has (per my Q1 position) declined to activate §B on §B's-own-warrant-terms. This pattern — a directionally-sympathetic operator observation that does not literally meet the preserved minority's activation warrant — is worth watching. If operator re-surfaces at S046+ or if a new reader (perhaps an external reviewer, perhaps a non-Claude sensor layer at some future session) reports actual confusion, the §B activation warrant fires literally. Tracking: if operator re-surfaces within 6 sessions (S046–S051), §B activation warrant is retroactively considered fired at S045 and an S052 close audit should note the belated activation.

2. **Count-threshold question for §B warrant wording**: §B warrant as worded is qualitative ("future confusion"). At S045 open there are 21 default-named folders; at a hypothetical S100 there would be ~80. Is there a count beyond which the cumulative mass of the default literal becomes self-evidently confusing? S027 Q6 cross-sectional-drift observation suggests the answer is yes, but the inflection point is unknown. Consider adding a numeric sub-warrant to §B (e.g., "or count of default-named folders exceeds 50 without any operator observation noting confusion") as a quantitative companion to the qualitative warrant — but this would itself be spec-surface expansion and OI-007 pushes against it. Status: watch; do NOT add numeric sub-warrant at S045.

3. **Cross-sectional-drift vocabulary still unformalised** (S027 §5 Honest notes observation). S027 chose not to formalise; S045's Q1 deliberation is another exercise of detecting cross-sectional drift (via operator external observation). The detection mechanism works; the vocabulary is still informal. A future session may choose to formalise; S045 does not propose it (OI-007 restraint).

4. **D-094 paragraph stability**: the `workspace-structure.md` §provenance D-094 paragraph has held unrevised across 18 sessions (S028–S045). If S045 adopts my preserve recommendation, the paragraph extends to 19 sessions unrevised — longest stability run of any minor-amendment paragraph in the engine's history. Watch as a vindication data point for OI-007-style restraint.

### Honest limits

1. **Confidence on §B warrant literal fire**: the distinction between "adds no value" (operator's language) and "misleading a future reader" (§B warrant language) is a judgement call I made. A reviewer could reasonably read operator's note as firing §B — if "value" means "semantic information value" and "legacy of rename-before-close" implies "currently misleading about what the folder is," then the operator IS saying the default misleads (by suggesting a content-reflective title was produced when in fact none was). I do not think this is the strongest reading, but I acknowledge it is plausible. If the Outsider or Cross-Family Reviewer reaches this reading, 3-of-4 convergence could move to activate §B and my position would become the minority.

2. **Retroactive / Q2-dropped question**: Q2 (retroactive treatment of S023–S044 folders) is dropped per operator R3. I respected this. If a future operator rescinds R3, retroactive becomes deliberable; D-017 immutability would still protect historical records but a narrow-dispensation under §A's closed-enumeration mechanism could be proposed. I explicitly do NOT propose this at S045.

3. **Scope B depth deferred**: my Q3/Q4/Q5 positions are held with lower confidence than my Q1 position. P2 has the depth. If P2's analysis diverges from my (c) / (iv) tentative preferences, I expect to update toward P2 unless P2's reasoning invokes a laundering surface I catch.

4. **Independence-phase clean but interpretability-opaque**: I have not cross-read P2/P3/P4; I cannot know whether they are reaching similar conclusions. If the Outsider produces a reframe that recasts scope A as a different deliberation entirely (e.g., reframes "folder-name default" as "archival-discoverability pattern"), my Q1 position may be obsolete before synthesis. I accept this and will defer to Case Steward's synthesis if it reveals a reframe I did not consider.

5. **Aggregate-budget quantification not independently verified**: I used the assessment §Q5 arithmetic without independently re-measuring S039–S044 close sizes. If the arithmetic is off by more than 20%, my Q5 deference to P2 still holds but my bias toward sub-90K-aggregate options is contingent on the numbers being approximately right.

## Independent claim

What this perspective contributes that the other three cannot: **a rigorous S027-precedent-aware test of the §B activation warrant's literal wording against operator's observation's literal wording**, applied with anti-laundering discipline (explicit refusal to silently re-propose the S027-rejected §B position without citing what has changed, and explicit acknowledgment that what has changed is weak). P2 has scope-B depth; P3 (Outsider) will seek reframes; P4 (Cross-Family Reviewer) will audit retrofit-risks and laundering surfaces. None of them is structured to execute the specific `operator-claim vs §B-warrant-text` threshold comparison at the level of textual fidelity that scope A's minor classification requires. That is my contribution.

## Confidence and limits

**Confident in:**
- Q1 preserve recommendation (high confidence); the §B warrant literal fire is not met by operator's observation as-worded.
- OI-002 minor classification (hypothetical, if activated); 14th data point would sit cleanly in the minor branch.
- Q6 separate-decisions (high confidence); scope-independence is established and partial-adoption flexibility is valuable.
- Independence attestation (clean; files do not exist on disk).

**Not confident in:**
- Q3/Q4/Q5 positions (scope B); these are deferred-weight, Retention-Window Reviewer has depth.
- The exact inflection point for §B warrant literal fire (alternative reading plausible per honest-limit 1).
- Whether the Outsider will produce a reframe that reshapes the deliberation (cannot know without cross-reading).

**Could not resolve:**
- Whether the 21-default-named-folders count itself is or should be a §B quantitative sub-trigger. I recommend NOT adding one (OI-007 restraint) but acknowledge this is a preference, not a demonstrated best answer.
- Whether operator's recommendation-to-deliberate vs position-not-for-deliberation framing should bias the deliberation toward activation (on deference grounds) or preserve (on explicit-deliberation-space grounds). I read it as preserve-tolerant per operator's own framing.

**Word count**: approximately 2,400 words (within 1,200–2,500 target; under 6,000 hard).
