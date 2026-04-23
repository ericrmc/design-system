---
session: 028
title: Perspective — Synthesiser-integrator
date: 2026-04-23
status: complete
perspective: Synthesiser-integrator
committed_at: 2026-04-23T00:00:00Z
---

## Q1 Adopt-or-preserve

I recommend **partial adoption with revision**: convert §5.3 to an active specification, but not at the minority's preserved values and not as a single-lever response. The forward problem is different in shape from the Session 023 problem, and the minority's position — preserved verbatim since 023 — encodes a 2023-shaped intuition about an 2026-shaped trajectory. Adoption must honour the activation warrant (the engine promised itself it would treat the preserved position as preferred revision direction once the warrant fired) while integrating everything learned in the five intervening sessions.

The structural framing matters. The engine has six levers (per §4) for managing default-read aggregate. The §5.3 proposal is lever 2 (aggregate hard budget). Levers are not substitutes — they address different aspects of the aggregate-growth problem:

- Lever 1 (per-file) bounds local verbosity.
- Lever 2 (aggregate) bounds system-wide accumulation.
- Lever 3 (enumeration-structural) reshapes what counts as default-read.
- Lever 4 (prompt-level close-size guidance) soft-shapes author behaviour.
- Lever 5 (spec-detail archive-migration) trims without restructuring.
- Lever 6 (advisory-only, status quo §2a) relies on observation and voluntary response.

Reading the 022 → 027 trajectory as a test of lever 6 alone: advisory emitted at Session 024 and the engine did not take remediation. Advisory alone was observationally insufficient. This is genuine new information: before Session 024 we did not know whether §2a's emission-only design would produce voluntary restructure. It did not. So §5.3's core intuition — that naming a budget creates forcing function — is vindicated against the null hypothesis that §2a would suffice.

But vindication of the *intuition* does not mandate adoption of the *specific values* or the *specific mechanism*. The minority position was drafted at Session 023 when the aggregate was ~83K, the advisory threshold was new, and the ten-session projection was uncertain. The minority picked 80K soft / 90K hard in that frame. Five sessions later we have: actual aggregate trajectory data, identification of close-file accretion as the dominant growth driver (not per-file verbosity as lever 1 implicitly assumed, nor uncontrolled sprawl as an aggregate budget implicitly assumes — but enumeration expansion through the "every close enters default-read" rule). We also have Session 022's thin-index precedent (lever 3) that the minority's drafters did not have in operational evidence.

The honest decision is therefore: **adopt the forcing-function principle from §5.3, but use the five sessions of new evidence to set the values and pair the budget with the structural lever that addresses the actual growth driver.** A pure §5.3 adoption at 80K/90K would require immediate aggressive remediation (current aggregate 105K is already 15K above the minority's hard line) — that remediation would necessarily be enumeration-structural (close-rotation) because per-file is already bounded. So the effective adoption of §5.3 at minority values *is* the combination of lever 2 and lever 3. Better to make the combination explicit than to adopt lever 2 and then scramble to invent lever 3 under pressure.

**Preservation discipline**. Preservation is not a promise that minority positions must be adopted unchanged. It is a promise that they are not discarded, that they are evaluated on their merits when the warrant fires, and that the resulting decision records what changed. Adoption-with-revision honours preservation if the revision is faithful to the minority's structural intent (forcing function; bounded aggregate) and adjusts only what five sessions of evidence warrant adjusting (values; paired mechanism). I will specify the revision in Q2 and Q3.

## Q2 Budget values

I recommend **120K hard / 110K soft**, paired with enumeration-structural lever 3 (see Q3). This is higher than the minority's 90K/80K, higher than §2a's 100K/90K, and above the current 105K aggregate. The reasoning is threefold.

First, **the minority's values are obsolete by virtue of being hit**. Setting hard at 90K when actual is 105K means the budget is born in violation. A budget in violation is a restructure-forcing event, not a steady-state specification. If we want §5.3's forcing function to operate prospectively — "bound forward growth" — the budget must be set above current-state so that the forcing function engages on *future* excess rather than on an *existing* excess that requires immediate one-shot compliance. One-shot compliance under time pressure is exactly the pattern §5.3 was designed to avoid.

Second, **§2a's 100K/90K has the same problem with less margin**. 105K exceeds 100K by 5%. Adopting §2a values as budget turns the next session into a compliance emergency. The engine should not engineer emergencies into its specifications.

Third, **headroom above current state reflects how the engine actually works**. Sessions close with close-files that range from ~1,200 words (Path-A-shape) to ~5,250 words (substantive-deliberation-shape). Session 028 will produce a substantive close. If we set hard at 110K (5K headroom above current), a normal-shape Session 028 close would already violate it. Setting hard at 120K gives roughly 14K headroom, which under current growth rates means approximately 2–3 sessions before the next proximity event. That is the right cadence: close enough to exert forcing pressure within the 10-session horizon, far enough that routine close-writing does not trigger it.

The specific recommendation:

- **Aggregate hard ceiling: 120,000 words.** Crossing this ceiling triggers mandatory remediation in the session that crosses it.
- **Aggregate soft warning: 110,000 words.** Crossing this triggers a planned-remediation directive: the next substantive-revision session must include an enumeration or archive-migration action, even if small.
- **§2a advisory 90K/activation 100K retain their current observational function.** They do not disappear. Advisory continues to prompt attention; activation continues to prompt review of whether minority-direction revision is warranted. The new budget sits above them.

Values interaction with current state: 105K is currently between activation (100K) and soft warning (110K). This is the right position for Session 028 — the soft warning has not yet fired, so Session 028 is not under remediation pressure *from this specification*, but the engine has full visibility that the next couple of sessions will bring the soft warning into contact.

**Alternative values I considered and rejected**:

- **85K/75K (tighter than minority)**: encodes ambition about smallness that is not supported by current file-count or content-density evidence. Would require immediate aggressive restructure well below any historical operating point. Too ambitious.
- **130K/120K (generous headroom)**: forcing function too far away to be meaningful within the 10-session horizon. Essentially status quo with a distant ceiling.
- **Minority's 90K/80K exactly**: analysed in Q1. Adoption-in-violation is bad specification design.
- **§2a values as budget 100K/90K**: adoption-in-violation with smaller margin. Same problem.

**Why 120K specifically**. Given current trajectory of +~4K per Path-A session and +~5–6K per substantive session, 120K is approximately three substantive sessions of headroom or four Path-A sessions. That horizon is long enough for the engine to plan and execute enumeration-structural remediation (which takes at least one substantive session of work to specify and execute) before the hard ceiling, and short enough that the ceiling exerts forcing pressure on planning rather than being an abstract future concern.

## Q3 Remediation mechanism

I recommend a **two-tier mechanism** that pairs the aggregate budget (lever 2) with a specific enumeration-structural rule (lever 3). This package addresses both the forcing-function intent of §5.3 and the actual growth driver identified in §3a (close-file accretion).

**Tier 1: Soft warning (110K) — planned remediation directive.**

When aggregate crosses 110K at session close:
1. Validator emits a **remediation directive**: "Aggregate crossed 110K soft warning at Session N close. Session N+1 must include at least one aggregate-reducing action: close-rotation, spec-archive-migration, or enumeration restructure. Minimum reduction target: return aggregate below 108K within two sessions."
2. The next session's opening assessment acknowledges the directive and selects a remediation action.
3. The chosen action is executed as part of the session's substantive work, recorded in its close with before/after aggregate measurement.

**Tier 2: Hard ceiling (120K) — mandatory remediation.**

When aggregate crosses 120K at any point:
1. The session that crosses it cannot close without executing a remediation action that returns aggregate below 118K.
2. Remediation is not optional and cannot be deferred. This is the "forcing function" teeth.
3. Acceptable remediation actions are defined: close-rotation (specified below), spec-archive-migration (per Q4), or enumeration restructure.
4. If the crossing is discovered only at validator run after drafting the close, the close must be revised to include the remediation or the session must continue with an additional remediation work-unit before close-finalisation.

**The close-rotation rule (the structural lever).**

I recommend adopting this as a first-class specification alongside the aggregate budget:

> **Close-rotation rule**: `03-close.md` files from sessions older than the current session minus **10** are rotated from default-read to archive-surface. SESSION-LOG.md entries continue to serve as the default-read index pointing to archive-surfaced close files. Closes are not deleted, edited, or summarised; they move to archive-surface where Deliberate can pull them on demand.

With current aggregate 105K and close-files averaging ~3K (Path-A) to ~5K (substantive), rotating sessions older than N-10 removes roughly 25–35K of aggregate once the rotation first activates (assuming rotation starts from current state and ten prior closes are retained). This would bring aggregate into the 75–85K range — comfortably below the soft warning, with headroom for approximately 10 substantive sessions of growth before next contact.

Rotation triggers:
- Automatic every session close: after the session's own close is written, the oldest default-read close (if it is older than current minus 10) is rotated to archive.
- Does not require separate decision at each session; operates as standing rule.

**Why 10 sessions of retention specifically**. Ten sessions corresponds roughly to the "recent working memory" horizon of the engine. Minorities are typically re-evaluated within a 5–10 session window (§5.4 aged out at 9, §5.2 vindicated at 5). Cross-session patterns (close-verbosity flagged at n=2, activation warrants firing at n=4) operate in the 3–7 session range. Ten sessions retains the full recent-history band while releasing older history to archive-surface where it remains accessible but not loaded by default.

**Why close-rotation rather than other enumeration changes**:
- Addresses the actual growth driver (§3a shows close-file accretion is dominant).
- Preserves all content (no deletion, no editing, no summarisation).
- Reversible: rotated files can be re-included if a pattern needs current-session pressure-testing against older close-content.
- Has precedent in Session 022's thin-index pattern for engine-history sections.
- Does not affect spec files, minority positions, or validator state — those remain in default-read.
- Natural boundary: closes are the accretion surface, so they are the rotation surface.

**Alternative remediation shapes I considered and rejected**:

- **Per-file close budget reduction only** (lever 4). Softest lever. Does not address file-count growth. Even if every future close were 1,500 words, aggregate grows ~1.5K per session without bound.
- **Spec-archive-migration only** (lever 5). Useful but insufficient. Specs are a smaller portion of aggregate than closes; migrating spec history trims 10–15K once and does not address forward accretion.
- **Advisory-only continuation** (lever 6). Tested for five sessions; observationally insufficient.
- **Multi-rule cascade** (e.g., per-file + aggregate + rotation + close-guidance + migration). Overspecified for the current problem. Prefer adopting the minimum necessary mechanism (aggregate budget + rotation rule) and adding further levers only if evidence warrants.

## Q4 Interaction with per-file budgets

The aggregate budget should be **orthogonal supplement, not override**. Per-file budgets bound local verbosity; aggregate budget bounds systemic accumulation. They operate on different axes and interact through file-count — which is exactly why neither alone is sufficient.

Concretely:

- **Per-file budgets retain their current values**: hard ceiling 8,000 / soft warning 6,000. No revision proposed. §5.2 Skeptic's retroactive vindication at Session 027 supports this stability; there is no evidence per-file budgets need tightening.
- **§5.1 Pacer 10K/7.5K per-file minority remains preserved-unactivated**. Its activation warrant (file reaching 7,500 with restructure-for-budget event) has not fired and is not affected by this deliberation.
- **Aggregate budget adds a system-wide constraint**. A file can satisfy per-file budget and still contribute to aggregate-budget pressure simply by existing.
- **Remediation preference order**: when aggregate budget is triggered and per-file budgets are not, remediation prefers enumeration-structural actions (close-rotation, archive-migration) over per-file tightening. The aggregate budget does not authorise compressing individual files below their per-file soft budgets — that would conflate the two axes.

**Interaction with `multi-agent-deliberation.md` at 6,386 words**. This file is in persistent soft-warning territory. The §5.2 vindication at Session 027 recognised this is acceptable steady state given no file reached 7,500 in five sessions. The aggregate budget does not change this analysis. If aggregate pressure develops, `multi-agent-deliberation.md` is not the remediation target — the remediation target is the enumeration (close-rotation).

**Interaction with archive-pack surface**. `read-contract.md` v2 distinguishes default-read from archive-surface. The aggregate budget applies to **default-read aggregate only**. Archive-surface content does not count against the budget. This is a necessary condition for close-rotation (lever 3) to function as remediation — rotating closes to archive reduces default-read aggregate even though content is preserved.

**Interaction with future spec additions**. If Session 028 or later adds a new default-read spec file, that file counts against aggregate. If adding a spec would cross a threshold, the engine must plan compensating remediation. This is appropriate: new default-read specs represent genuine engine-level additions and should be pressure-tested against systemic capacity.

**What this interaction is not**:
- Not a single unified "complexity budget". The two levers are distinct because they address distinct failure modes (per-file readability vs aggregate load).
- Not a replacement for §2a. §2a advisory/activation thresholds continue emitting. The relationship is: §2a tracks trajectory and triggers minority-review; budget thresholds trigger remediation. They are sequential stages of engine response.

## Q5 Engine-version interaction

I recommend **engage engine-version in this deliberation, not separately**. Converting §5.3 from preserved minority to active specification is a substantive revision to `read-contract.md`. Adding the close-rotation rule is a further substantive revision. Both together constitute a non-trivial specification change. This is an engine-v4 → engine-v5 transition.

Reasoning:
- engine-v4 has been preserved Sessions 024–027 (five consecutive non-bumps). That preservation reflects that prior session-level decisions did not substantively revise core specifications.
- Session 028's decision *will* substantively revise `read-contract.md` (adopt §5.3-derived budget, add close-rotation rule, adjust §2a's role to feed-forward into budget tier rather than standalone advisory).
- The engine-manifest's cadence discipline (§5.4 cadence minority) concerns pace of version bumps, not absence. Five sessions of preservation is healthy restraint; bumping on substantive revision is healthy honesty. Both can be true.
- §5.4 aged out at Session 026. OI-018 remains open for engine-manifest §5 revision, but that is separate from whether engine-v5 bumps now — OI-018 concerns the *process* of manifest revision, not the *occasion* for version bump.

**Concrete version plan**:
- Session 028 close produces engine-v5.
- engine-v5 supersedes engine-v4. engine-v4 is preserved per versioning discipline (not overwritten).
- engine-v5 changelog entries:
  - `read-contract.md` v2 → v3: aggregate-budget specification added; §2a role clarified; close-rotation rule added.
  - engine-manifest updated to reference engine-v5 and new `read-contract.md` version.
- Minority tracking: §5.3 status updates from "activated, preferred revision direction" to "converted to active spec at revised values; original minority preserved in §5.3 history block for provenance". A new minority may emerge during Session 028 deliberation (e.g., a position arguing for tighter values or pure-§5.3 values); such new minorities are preserved per schema.

**Why not deferral to a separate session**:
- The activation warrant fired at Session 027 close. Deferring the version bump while executing the substantive revision would create a "shadow revision" where the spec changes but the version does not — that is precisely the failure mode engine-versioning exists to prevent.
- Combining the decision and the version bump in Session 028 keeps the engine's specification history legible: future readers can see that engine-v5 was introduced specifically because the §5.3 warrant fired and the aggregate-budget + rotation package was adopted. Deferral would obscure this link.

**Relationship to §5.4 cadence minority**. §5.4 aged out at Session 026. It does not reactivate for engine-v5 unless the bump is objected to on cadence grounds. A legitimate substantive-revision bump does not re-engage cadence minority; that minority concerned undesired frequent bumps, not necessary ones.

**What the version bump does not do**: it does not re-open every settled specification decision. engine-v5 inherits all engine-v4 specifications except where explicitly revised. The revision surface is bounded to `read-contract.md` aggregate-budget-related content and the manifest reference.

## Q6 Methodology-level observation

§2a **partially fired as designed, and partially revealed a mechanism gap**. The honest characterisation is more nuanced than "mechanism working" or "mechanism broken".

**What worked**:
- §2a emitted advisory at Session 024 (aggregate crossed 90K). Engine became aware.
- §2a emitted activation at Session 027 (aggregate crossed 100K). The activation warrant for §5.3 fired. The minority-review mechanism engaged. Session 028 exists as a deliberate response to the activation. This is the methodology operating as specified.
- Preservation discipline held: §5.3 was preserved verbatim across five sessions, then surfaced for review when its warrant fired. Minorities are genuinely first-class.

**What did not work**:
- §2a's observational-only design assumed advisory emission would produce voluntary engine-level remediation between advisory (90K) and activation (100K). It did not. Sessions 024, 025, 026 received advisory and proceeded without remediation action. The engine did not treat advisory as call-to-action; it treated it as information.
- Between advisory at Session 024 and activation at Session 027, aggregate grew from 92.5K to 105.4K — a 14% growth during a period of explicit advisory. §2a did not slow this trajectory; it only tracked it.
- The observational-only design placed decision-weight on voluntary response, but voluntary response requires a forcing function or at minimum a clear decision procedure. §2a had neither.

**The mechanism gap**:
The gap is not in §2a itself; §2a did what it was specified to do (emit). The gap is the absence of a **between-stage procedure**: what happens between advisory emission and activation crossing? The current answer was "nothing formal", and that turns out to be operationally a null response. A better specification would connect advisory emission to a specific decision-point: e.g., "advisory emission at N triggers review at session N+1 open of whether compensating action is warranted before activation crossing".

**Broader methodology observation**:
The engine's observational-track-then-activate pattern works well when the observation period is short (days, single sessions) and the activation response is swift. It works less well over multi-session horizons where emission becomes background noise. This is a general lesson worth recording: **observational thresholds in multi-session systems need paired decision procedures, not just emissions**.

This lesson does not invalidate preservation-with-warrants as a mechanism; preservation worked. It specifies where to add procedural tissue: the advisory-to-activation gap needs a review-gate. I recommend this as a follow-on observation, not a Session 028 decision:

- **New OI**: "Specify advisory-review procedure in `read-contract.md` so advisory emissions link to explicit decision-points rather than relying on voluntary between-stage response."

The Session 028 decision can land without resolving this OI, because the budget-plus-rotation mechanism adopted in Q2/Q3 has its own explicit decision procedures (soft-warning directive, hard-ceiling mandatory remediation). The OI is about the *next-layer-down* question: should §2a's advisory also acquire review-gate language, or is it sufficient for §2a to feed-forward into the new budget tier and let the budget tier carry the procedural weight? I lean toward the latter — §2a remains purely observational, and the budget tier's soft warning at 110K is the primary forward-looking decision-point. But this can be deliberated separately.

**Mechanism-working vs mechanism-gap verdict**:
- §2a as emission mechanism: working.
- Advisory-to-activation procedural tissue: gap, now filled by the new budget tier in Session 028's adoption.
- Preservation-with-warrants: working.
- Minority vindication and activation recording: working.

The methodology is not broken. It has a specifiable improvement at one layer, which Session 028 provides.

## Q7 Anti-laundering self-check

**What new information has arrived since Session 023?** Five categories:

1. **Trajectory data**: Actual 022 → 027 aggregate growth pattern is now observed rather than projected. Growth rate is ~+3–6% per session, with substantive sessions at the upper end. Projection at Session 023 was uncertain; projection at Session 028 is empirically grounded. This is *genuine* new information.

2. **Growth-driver identification**: Close-file accretion is dominant. Spec-file growth is minor. New-file-additions contribute approximately one file per session regardless of content. This was not clearly established at Session 023; it is established now through per-session delta analysis. Genuine new information.

3. **Advisory-only insufficiency**: §2a's observational design produced no remediation response across three advisory sessions. This is new information bearing directly on the Session 023 deliberation question ("is §2a enough or do we need a named budget?"). Session 023 answered "§2a is enough for now, preserve budget proposal as minority". Session 028 can now answer "advisory alone produced no remediation; budget-shaped forcing function is needed". Genuine new information.

4. **Retroactive §5.2 vindication**: per-file budget stability has been observationally confirmed. This does not directly bear on aggregate budget, but it provides evidence that budget-shaped constraints are compatible with the engine's operating pattern. Indirect new information.

5. **Activation warrant firing**: the warrant itself fired. The minority *predicted its own activation conditions* and those conditions materialised. This is Bayesian evidence for the minority's *diagnostic* accuracy (the minority correctly identified the threshold where intervention becomes preferred). Genuine new information, though with careful interpretation (Q7 follow-up below).

**Does activation-firing itself count as new information?**

Partially yes, partially structural caution warranted. The warrant is a pre-committed condition; its firing is by construction the moment at which the minority is promoted. The activation is not *independent* evidence for the minority's correctness on values or mechanism — it is evidence that the *threshold* condition is met. There is risk of motivated reasoning: "the warrant fired, therefore adopt the minority wholesale". Session 028 must separate threshold-condition-satisfaction (demonstrated) from values-and-mechanism-correctness (still requires deliberation).

This is the anti-laundering discipline: the warrant entitles the minority to **serious review and preferred-direction status**, not to automatic adoption at preserved values. My Q1 recommendation (adoption-with-revision) reflects this discipline. Adopting the forcing-function *principle* is warranted by the advisory-insufficiency evidence (category 3 above). Adopting the *specific values* (90K/80K) is not warranted, because values are independent parameters that the minority proposed in a different context and that new evidence (trajectory, current aggregate 105K) makes obsolete.

**Coherent continuation or reversal of preservation discipline?**

Coherent continuation. Preservation discipline commits the engine to:
- Not deleting minorities under pressure.
- Reviewing them when warrants fire.
- Adopting, revising, or continuing preservation on the review's merits.
- Recording the reasoning.

Session 028's proposed outcome (adopt principle, revise values, pair with lever 3) is within the preservation frame. It is not reversal. Reversal would look like: "we promised to activate when the warrant fired; now the warrant has fired and we decline to act". That is not what I recommend.

Nor is it capitulation. Capitulation would look like: "the warrant fired; adopt verbatim without review". My recommendation requires review of what five sessions of evidence warrant, which is the opposite of capitulation.

**What would count as reversal-shaped risk to watch**:
- Reversing at preservation (no action at all) would signal the engine treats warrants as non-binding, undermining minority-discipline.
- Adopting verbatim without engaging the new evidence would signal the engine treats preservation as automatic adoption, undermining deliberation-discipline.
- Adopting at values that re-violate immediately (e.g., 90K hard when current is 105K) would signal the engine specifies emergencies into itself, undermining operational-discipline.

My recommendation steers between these. The proposed 120K/110K values, the explicit pairing with close-rotation, and the engine-v5 version bump together form a **coherent response that honours the warrant without laundering the deliberation into a pre-committed answer**.

**Self-check on my own reasoning**:
- Am I recommending 120K because it is where current aggregate sits comfortably, rather than because it is the right value? Partially: the "current-plus-headroom" anchor is a defensible design choice (Q2 reasoning), but I note honestly that it is shaped by what is operationally easy. A more ambitious engine might pick 110K hard and require immediate remediation; I chose 120K hard and deferred remediation to the soft-warning tier. This is a design tradeoff I have made explicit rather than concealed.
- Am I recommending close-rotation because it is the obvious structural move, or because I have independently evaluated it against alternatives? Evaluated against alternatives in Q3. Close-rotation is the most aligned with the actual growth driver (§3a), the most reversible, and the most precedent-supported (Session 022 pattern). I believe it is the right choice, but other decision-makers might legitimately prefer a combined softer package (prompt-level close-size guidance + spec-migration) if they weight reversibility lower.
- Am I implicitly converting §5.3 because the synthesiser role is framed around integration and integration naturally produces combinations? Possibly. A pure-skeptic integrator might recommend "wait one more session; see if close-rotation alone (without budget) suffices". I considered that and rejected it because the advisory-insufficiency evidence is already sufficient — waiting another session yields diminishing returns on information gain and defers the warrant-response by one more session, which itself risks sending the signal that warrants are soft commitments.

## Honest Limits

**Limits of this perspective**:

1. **I cannot observe the actual deliberation dynamics**. I am reasoning from the brief's content alone. The Pacer-advocate perspective may produce an argument for pure-minority adoption that I have under-weighted. The Skeptic-preserver perspective may produce an argument for continued preservation that I have under-weighted. My integration is therefore integration of the *brief's framing*, not integration of actual deliberation outputs.

2. **Values are calibrated to plausible-defaults, not to first-principles**. I chose 120K/110K because it sits above current-state with headroom. A first-principles analysis would derive budget values from information-theoretic load limits, cognitive-load research on default-context sizes, or operational-cost calculations. I have not performed such analysis and do not have the data to do so. The recommended values are **plausible defaults**, not derived optima.

3. **Close-rotation-at-10 is a heuristic number**. I justified 10 as "recent working memory horizon" by reference to minority-review and pattern-flagging cadences, but the number is not derived from a formal analysis. 8 or 12 would also be defensible. If the deliberation prefers a different value, the mechanism is indifferent to the specific N.

4. **I have not modelled second-order effects of close-rotation**. Moving old closes to archive-surface may change how the engine reasons about its own history. For example: §5.4 cadence minority aged out at Session 026; if close-rotation happened earlier it is possible age-out would happen differently because the pattern-visibility of cadence events across the default-read surface would be reduced. I note this as a genuine risk without claiming it is decisive. The SESSION-LOG index mitigates but does not eliminate it.

5. **Engine-v5 version bump decision is presented as clear-cut; it is moderately clear-cut**. I argue in Q5 that substantive revision warrants a version bump. A minority view is defensible: "adopt the aggregate budget as a minor refinement to §2a rather than as a new specification layer, and retain engine-v4". I find this less convincing because the close-rotation rule is genuinely new content, not a refinement, but a reasonable deliberator could disagree.

6. **I have not addressed whether the budget specification itself counts toward the budget**. The budget specification text will add some words to `read-contract.md` (part of default-read). This is a trivial self-reference question that I flag without resolving: yes, it counts, but the marginal addition is small (~300–500 words) and does not materially affect the headroom analysis.

7. **OI-018 engine-manifest §5 revision is noted but not integrated**. I recommended engine-v5 bump without specifying how it interacts with OI-018. This is a real loose end: OI-018 concerns the *process* of manifest revision, and bumping to v5 performs a revision. If OI-018's outcome would change how the bump is specified, the bump-now recommendation is premature. I believe OI-018's process question is independent of the bump-occasion question, but I have not verified this against OI-018's actual content.

8. **Recommendation depth assumes deliberation wants implementability**. The brief asks for concrete decision shape. If the deliberation prefers to stop at "adopt principle, defer values and mechanism to a specification-drafting substep", my Q2/Q3 specificity is more than needed. I chose to err on concreteness because vague integrator outputs are not actionable, but I flag that this is a stance choice.

9. **I have not considered adversarial growth patterns**. The analysis assumes future sessions follow the observed 022–027 pattern (organic growth driven by close-file accretion). A substantive-deliberation-heavy future (e.g., a contested engine-architecture question debated across three sessions) could add 15–20K in a single session. The proposed budget would fire immediately and force same-session remediation. This may be desirable (forcing function working as intended) or undesirable (remediation during active deliberation is difficult). I lean toward "working as intended" but acknowledge the stress-case has not been fully explored.

10. **Synthesiser role does not authorise adjudication between the other perspectives**. If Pacer-advocate recommends pure-minority adoption and Skeptic-preserver recommends continued preservation, the resolution between them is not my output — it is the deliberation's output. My output provides the third shape (integration across the design space) for the deliberation to consider alongside the polar positions.
