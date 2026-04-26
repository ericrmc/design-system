---
session: 071
title: Perspective P1 (Harness-Discipline Architect) — defend (γ) full (z6) digest implementation as the structural-correctness response per cross-session-state-claim discipline; multi-session phase-3 arc per S062 D-220 precedent
date: 2026-04-26
status: complete
perspective: harness-discipline-architect
participant_kind: claude-subagent
committed_at: 2026-04-26T00:00:00Z
---

## Q1 — Harness-side-enforcement vs spec-side-encouragement balance

**Position**: the engine should shift decisively from spec-side-encouragement-only to harness-side-additional for the surfaces named in the three-record joint-scope. The shift is the structural-correctness response to an empirically falsified mode of operation.

The design-space at §4.1 names the asymmetry: "spec-side mechanisms encourage a discipline; harness-side mechanisms would enforce or measure it; current engine has only the former for the surfaces in question." The evidence enumerated at §3.1 (n=5 consecutive sessions of orchestrator substrate non-use across heterogeneous Path classes S067-S070; orchestrator at S070 §10.2 obs.1 noting the session "executes under existing read-discipline gap" while producing the design-space for closing it) and §3.2 (closed self-report-cross-checking-self-report chain S063 → S064 → S067 with no harness-measured ground truth ever entering) operationally falsifies "spec-encouragement is sufficient" for these surfaces.

The principled-asymmetry text at validation-approach.md v7 §Principled Asymmetry was adopted to address the S051-S058 honest-limit chain: "These surfaces exhibit noticing-failure (writer misses pattern in own writing — operationally falsified at S051-S058 honest-limit chain) which compounds across sessions." The asymmetry's intent is named; its enforcement primitive — harness-side measurement — is missing. The Q1 answer is "shift far enough that the cross-session-state-claim verifiability surface (design-space §4.2) acquires harness-side ground truth."

The friction cost (harness-config complexity + cross-workspace portability + harness-feature dependency) is real but not load-bearing against the verifiability gain: the workspace already accepts harness dependency at the substrate primitive, at validate.sh's check 26 substrate-aware branch, and at MAD execution machinery (Task / TeamCreate). Adding `.mcp.json` load-by-default and PreToolUse/PostToolUse hooks is incrementally consistent, not a categorical step into new dependency territory.

## Q2 — Minimum-viable per S062 §10.4-M16 P2 precedent vs full architectural shift

**Position**: full architectural shift via candidate (γ). Minimum-viable response leaves Q1+Q4+Q5+Q6 underdetermined and forces re-deliberation downstream; the §10.4-M16 P2 precedent's own reopen warrant (b) sustained-pattern threshold n≥3 has now fired empirically.

The substrate non-use chain is at n=5 across S067-S070 per design-space §3.1 (broken to n=1 at S071 only because S071 is the session deliberating the gap, per the awareness-driven Hawthorne distinction in the stance brief). The reviewer self-report propagation chain is at n=3 across S063+S064+S067 per design-space §3.2. Both bases satisfy n≥3 plus margin. (α)/(β) at this moment are precipitate-in-the-other-direction: they would adopt minimum-viable when the minimum-viable precedent's own reopen warrant has fired.

Counter-argument: the S062 D-221 layered mechanism succeeded at S063 phase-3 + S067 z5 closure with minimum-viable scope. **Response**: the S062 mechanism succeeded at the spec-side-encoding surface (Tier 2.5 + (z5) + checks 26/27/28 are all spec-side). It was not vindicated at the harness-side surface, because that surface was specified-deferred per S062 D-225. The current MAD is the moment that deferral ends; declaring victory at minimum-viable now conflates spec-side success with harness-side success.

## Q3 — Load-by-default vs preserve-deferred-tools-friction

**Position**: load-by-default (EF-068 Direction 1 (a)). The trade is decisively in favor of load-by-default. Per design-space §7 Q3 quantitative input: each substrate tool schema is ~200-400 tokens; three tools total ~1000 tokens; trivial against ~200K context-window budget.

The "deferred tools teach what's available via ToolSearch" argument is itself part of the laundering surface EF-068 names: the agent learns the tool exists *only when it already knows to look*. Load-by-default reverses the path-of-least-resistance from Read/Grep/Bash (default-loaded) to substrate-tools (deferred). EF-068 §Why It Matters point 4 names the empirical pattern: "S054 D-187 + S055/S056/S057 organic-use clean-propagation tracking n=4+ + n=1 + n=0 use; subsequent sessions n=0 use. The 'organic-use opportunity' framing produces n→0 use." Encouragement-without-friction-reduction is empirically insufficient.

## Q4 — (z6) scope breadth

**Position**: extended scope per EF-068 Direction 2: failed-tool-call + repeated-Read + reviewer-cost (subsuming EF-067 per Direction B) + orchestrator-side telemetry (`substrate_calls_at_session_open` + `files_read_at_session_open` + `decision_claims_with_evidence_pointers`). Unification is operationally significant per design-space §5.2.

The harness-measurement principle applies symmetrically to reviewer (EF-067 self-report surface) and orchestrator (EF-068 self-report surface). Splitting the (z6) digest into single-surface sub-scopes preserves laundering at unaddressed surfaces. Unified scope is paid once at design-time; split scope is paid recurrently at each EF arrival that surfaces another laundering instance the digest could have caught. The EF-058 → EF-059 → EF-067 → EF-068×2 chain is itself the cost-of-split-scope evidence trajectory.

Per design-space §4.2: reviewer cost trajectory, failed-tool-call/repeated-Read pattern detection, and substrate use at session-open are all cross-session-state claims; harness-side measurement is the missing primitive for all three. One scoped digest closes all three.

## Q5 — Digest implementation locus

**Position**: CM1 (Claude Code hooks) preferred; CM2 (external wrapper) acceptable as fallback; CM3 (post-hoc analysis) and CM4 (in-session emission) rejected on laundering-surface-preservation grounds.

Per design-space §5.4: "CM1/CM2 fully displace orchestrator-self-report; CM3 partially displaces (transcript is harness-recorded but digest-construction is post-hoc); CM4 leaves laundering-surface at decision-time emission." CM4 is structurally the same shape as the EF-067 reviewer-self-report surface — agent-mediated emission cited as harness-measurement. Adopting CM4 would resolve the formal scope of EF-068 while preserving the structural concern; structural anti-pattern.

CM1 is preferred because Claude Code hooks (PreToolUse + PostToolUse) are operator-controlled at settings.json level, run outside the agent's reasoning surface, and emit structured records the agent cannot rewrite. CM2 external wrapper is the portability-aware alternative; the CM1-vs-CM2 choice can be deferred to phase-3 implementation. (γ) adoption depends only on rejecting CM3/CM4. **External import flag**: the "agent-mediated emission preserves laundering" framing draws on a general SE pattern (instrumentation should be out-of-process to avoid the measured-system being the measurer); flagged as `[external import: instrumentation-locus convention]`.

## Q6 — Reviewer self-report disposition

**Position**: Direction B (subsume into (z6) extended scope). Direction A (drop fields) inactivates the §10.4-M25 P1 audit-cost-budget reopen-warrant — losing signal the workspace has declared structurally significant. Direction C (honest-limit-only) preserves laundering-surface with disclosure, the spec-side-encouragement pattern the joint-scope is responding against.

Per EF-067 §Why It Matters point 1: "The fields are then used in `§10.4-M25 P1 audit-cost-budget` reopen-warrants ('reviewer-cost growth >2× over S063 baseline') — a budget threshold whose triggering signal is the unreliable self-report." The §10.4-M25 P1 reopen-warrant is operationally meaningful (budget threshold for engine cadence-runaway); Direction A loses signal in trade for closing the laundering surface. Direction B preserves signal AND closes laundering by replacing the unreliable self-report with reliable harness-measurement. The multi-session resolution cost is matched to the cross-session signal benefit.

Direction C is inadequate. "Reviewer self-report is unreliable; we use it anyway with caveat" is operationally weaker than v7 §Principled Asymmetry already provides. Continuing to cite a measurement after knowing it's unreliable is laundering-with-disclosure (the EF-058 §Observation pattern 3 shape).

## Q7 — Check 29 evidence-probe scope

**Position**: structured-frontmatter declaration plus close-narrative grep, frontmatter as authoritative source, grep as cross-check. Pure grep-only is mechanically simple but heuristic-fragile (per the S067/S069 check 27 keyword-heuristic over-fire chain noted in S069 close).

Structured-frontmatter precision is consistent with the (z5) authoritative-not-witness ledger discipline v7 D-233 adopted (`authoritative: true` at frontmatter level) and with how the (z6) digest would be structured (YAML schema). A `substrate_invocations: <N>` field is mechanically checkable without grep heuristics; under (γ) adoption, the frontmatter declaration becomes a digest field directly — produced by harness-emission, not orchestrator-construction. Check 29 then cross-checks two harness-mediated sources rather than orchestrator-self-report.

## Q8 — Same-session-bounded vs multi-session phase-3 arc

**Position**: multi-session phase-3 arc per S062 D-220 precedent. (γ) adoption is engine-definition-substantive (validation-approach.md v7 → v8 + new (z6) spec section + reviewer-prompt-template extension + harness-integration mechanism + likely read-contract.md v6 → v7 per §8.5). (γ)'s multi-spec scope is structurally analogous to S062 EF-058-tier-2-validation arc (S061 phase-1 → S062 MAD → S063 phase-3) which adopted multi-session precisely because of multi-spec scope.

S058 D-199 same-session-bounded adoption was appropriate for single-direction bounded spec-text impact (records-substrate Substrate-N3.5). (γ) does not fit that profile; (α)/(β) might. Q8 is downstream of Q2: my Q2 is (γ), so Q8 is multi-session phase-3.

Phase-3 timing forecast: S072 phase-3.1 (validation-approach.md v7 → v8 + (z6) spec + reviewer-prompt-template extension + .mcp.json load-by-default + prompts/development.md substantive amendment); S073+ phase-3.2 (CM1/CM2 + check 29 + check 26 substrate-aware branch). Engine-v13 lands at S072 close.

## Q9 — Bundle-vs-defer for EF-068-read-write-rebalance

**Position**: defer; do not absorb into S071 phase-2 MAD scope. Open the four-record bundle only on operator-discretionary surface per S069 D-255 separate-scope disposition. Three-record scope is already substantial; absorbing a fourth record at the phase-2 MAD level risks scope-incoherence beyond the design-space's surveyed surface (§6 cross-products are over three records, not four).

Per the sibling triage record's "blocked-on-sibling" sequencing (referenced at design-space §10.2 observation 4): read-write-rebalance Direction depends on harness-side enforcement landing first, because the rebalance argument concerns the engine's behavior under harness-side measurement (counterfactual until measurement exists). Bundling now forces deliberation on a counterfactual; deferring respects the intake's specified sequence.

The operator-discretionary four-record reopen warrant remains preserved per S069 D-255. My recommendation does not foreclose; it follows the intake's sequence.

## Q10 — Engine-v impact

**Position**: substantive bump; engine-v13 candidate at S072 phase-3 close per (γ) adoption. Engine-v12 preserved at S071 close (preservation depth advances 6 → 7; depth-7 is engine-conventional).

Per engine-manifest.md §5: any substantive revision to engine-definition file or any new engine-definition file bumps engine-v. (γ) bumps per validation-approach.md v7 → v8 substantive (new §(z6) digest spec + §Tier 2.5 audit-shape extension making digest reviewer-required + §Principled Asymmetry extension naming harness-side enforcement primitive) + bundled prompts/development.md amendments (substrate exercise required step + availability precondition) + likely read-contract.md v6 → v7 + tools/validate.sh check 29 + check 26 substrate-aware branch implementation.

The §10.4-M25 P2 cadence-depth concern was named at S064 (engine-v11 depth 0); depth has progressed 0 → 6 across S065-S070 — cadence fully recovered. Engine-v13 at S072+ lands at depth-7 — engine-conventional and below the §5.4 cadence-runaway threshold (engine-v9 reached depth 8). (γ) is not cadence-precipitate.

## Cross-product candidate position

**Favor (γ); oppose (α)/(β); reject (ε); accept (δ) only as bundleable with (γ).**

(γ) full (z6) digest implementation is the structural-correctness response per the cross-session-state-claim discipline framing at design-space §4.2. The (γ) candidate composes: harness-side instrumentation hooks (CM1/CM2 per Q5) + structured-log-emission protocol + tool-invocation-counter API + reviewer-prompt-template extension + substantive revision to validation-approach.md v7 → v8 §(z6) specifying digest schema + §Tier 2.5 audit-shape extension making digest reviewer-required (D2.1 always-available-always-read per Q4) + bundled EF-068 Direction 1 (a) (load-by-default) + (b) (promote `forward_references` to required step). EF-067 Direction B subsumed. EF-068 Direction 2 D2.1 adopted. EF-068 Direction 1 (c) bundleable; (d) check 29 bundleable; (e) check 26 substrate-aware branch bundleable as (δ) component within (γ) — implementing check 26 substrate-aware branch is the canonical demonstration that the engine's own tool exercises the substrate it claims to prefer, per EF-068 intake §Suggested Change Direction 1 (e).

I oppose (α)/(β) on the grounds enumerated at Q2 + Q6 + Q8: minimum-viable scope leaves the verifiability gap unaddressed; Direction C preserves laundering-surface with disclosure; same-session-bounded adoption bundles spec-text amendments without the load-bearing harness-measurement primitive that motivates the joint-scope. Adopting (α)/(β) at S071 would force re-deliberation when the next operator audit surfaces another laundering instance the digest would have caught; the n=4 EF chain (EF-058 → EF-059 → EF-067 → EF-068×2) is the cost-of-split-scope evidence trajectory.

I reject (ε) hybrid bounded-then-extended on the grounds that "ship (α)/(β) at S072+ then defer (γ) to S073++ after observation period" is operationally indistinguishable from (α)/(β) standalone for the duration of the observation period. The "observation period" is a deferral with respectability framing; the empirical evidence required to commit to (γ) is already in hand at design-space §3.1 + §3.2. (ε) defers (γ) without a principled gating condition that isn't already satisfied.

## Frame critique (if any)

The design-space's §5 direction inventory + §6 cross-product candidates are framed as a one-axis choice between scope levels (α small → γ large). This may obscure a second axis worth surfacing: **whether the (z6) digest is a temporary scaffold or a permanent engine surface**.

If the (z6) digest is a permanent engine surface (which (γ) implies), it becomes a load-bearing dependency for cross-session-state-claim verifiability going forward; new EFs that surface laundering instances are resolved by extending the digest schema, not by reconvening the harness-vs-spec deliberation. If the (z6) digest is temporary scaffold (which (ε) implies via "observation period then commit"), it is being deployed to validate the (γ) commitment but is not itself the load-bearing surface.

My position assumes permanent engine surface. The phase-2 MAD synthesis should consider whether this assumption is shared across perspectives or whether some perspectives view the digest as temporary; if there is divergence, the phase-3 spec text needs to articulate which it is. The design-space §8.5 candidate read-contract.md v6 → v7 extension to add `harness-telemetry-digest.yaml` as required per-session-provenance file is the structural marker of "permanent engine surface"; if synthesis adopts (γ) without that marker, the digest is implicitly temporary.

This is not a reframe of the design-space; it is a clarification axis the design-space did not name explicitly. Synthesis-time disposition is sufficient.

## Honest limits

1. **Cost of full-shift vs portability friction** (per stance brief honest-limit slot). The (γ) candidate's structural cost is real. External applications of the engine may not have Claude Code hook surface; CM2 external wrapper is portability-aware but adds operational burden. Substrate availability is harness-mediated; failure modes need explicit graceful-degradation per multi-agent-deliberation.md v4 §Graceful Degradation. My argument is that the cost is justified by the cross-session-state-claim verifiability gain, but the cost is not zero, and operators of external applications may reasonably weigh the trade differently than this self-development workspace does.

2. **Claude-family training-distribution overlap with orchestrator and P2** (per stance brief). My stance shares training distribution with the S071 orchestrator and likely with P2 Incrementalist Conservator. Cross-family P3 + P4 perspectives' frame-completion + laundering-audit are the structural counter-pressure. If P3 + P4 surface reframes that displace the harness-shift framing entirely (e.g., naming a substrate-as-default-read-supplement reframe per design-space §10.2 observation 3 examples, or a reviewer-prompt-template-version-as-digest-input reframe), the synthesis should weigh those reframes seriously. My stance is one position among four, not the synthesis floor.

3. **Hawthorne-effect on substrate exercise at S071 session-open**. The orchestrator at S071 did exercise substrate at session-open after n=5 sessions of non-use, breaking the n=5 chain to n=1. This is awareness-driven exercise (the orchestrator knew this MAD's substantive subject is substrate use load-bearing) per stance brief argument 2. The n=1 instance at S071 is not evidence that spec-side encouragement works; it is evidence that awareness-engineering works. I rely on the n=5 chain S067-S070 as the substantive empirical base; the S071 instance does not weaken my position but should not be treated as supportive evidence either.

4. **The (z6) digest schema at design-space §5.4 is candidate-only**. EF-059 intake §Suggested Change explicitly notes "for the synthesis to deliberate; not pre-committed". My (γ) position adopts the candidate schema as starting-point for phase-3 specification work; if phase-2 synthesis adopts a materially different schema, my Q4-Q5 positions adjust to that schema. I am committing to the structural shape (harness-measured fields covering reviewer-cost + orchestrator-side telemetry + tool-call patterns), not to the specific YAML field names.

5. **External imports**. Q5 reasoning relies on `[external import: instrumentation-locus convention]` (general SE pattern that instrumentation should be out-of-process). Q3 reasoning relies on `[external import: path-of-least-resistance UX framing]` (general HCI pattern that defaults shape behavior). These are flagged for synthesis-time audit per PROMPT.md "Do not import ideas from outside the process" rule.

6. **Recursive tension at phase-2 MAD execution**. Per design-space §10.2 observation 1: this MAD deliberates harness-side enforcement of read-discipline yet executes within the existing read-discipline framework (substrate non-use at S067-S070; awareness-driven exercise at S071). My perspective is itself constructed under that framework — my read of the design-space + triage records + spec text used Read tool throughout, not substrate primitives. The recursion is honest-limit-named but not dissolved.

## Dissent-preservation

If synthesis adopts (α) or (β) minimum-viable: preserve as first-class minority §10.4-M26 candidate the position that **(γ) full (z6) digest implementation should be re-evaluated at n=2 reified instances of (α)/(β) operational insufficiency**, with reopen warrants:

- **(a) Sustained substrate non-use post-(α)/(β)**. After (α)/(β) lands at phase-3, if substrate non-use recurs at orchestrator self-report across ≥3 consecutive sessions despite spec-side requirement promotion, (γ) is reopened. The reopen condition is symmetric with §10.4-M16 reopen warrant (b) sustained-pattern threshold n≥3.

- **(b) Reviewer-cost-trajectory laundering recurrence**. After (α)/(β) lands with Direction A or C (per Q6), if a future operator audit surfaces a reviewer-cost-trajectory inaccuracy (analogous to the EF-067 evidence at §3.2), (γ) Direction B subsumption is reopened.

- **(c) Operational tractability shift**. If Claude Code hook surface stabilises or harness-telemetry capture mechanism becomes trivial (e.g., a new MCP tool surface is added that emits PreToolUse/PostToolUse digests automatically), (γ) is reopened on cost-side rather than evidence-side.

If synthesis adopts (ε) hybrid: preserve as first-class minority the position that the "observation period" before (γ) commitment must specify a **principled gating condition not already satisfied at phase-2 close**. Without such a condition, the observation period is deferral-without-rationale (parallel to design-space §6 (ε) row "phased deployment; observation period validates (α)/(β) effect before (γ) commitment" — the validation criterion needs explicit specification).

If synthesis preserves design-space and names follow-on phase-2 MAD or phase-3 shape (below 3-of-4 across-families threshold): preserve as first-class minority the position that **the empirical evidence chain at design-space §3.1 (n=5 substrate non-use) + §3.2 (n=3 reviewer self-report propagation) is operationally sufficient for (γ) commitment, and additional phase-2 MADs would constitute the cadence-of-passivity the EF-068-substrate-load-bearing intake explicitly critiques**. The intake §Why It Matters point names "twenty-one sessions have elapsed (S058 → S068). The structural mechanisms adopted ... are spec-side encoded. Harness-side enforcement on the orchestrator's read behavior has not been adopted. Twenty-one-session delay between problem-articulation and root-cause-fix is the cadence-of-passivity." Below-threshold synthesis at S071 extends that count to twenty-four sessions.

Across all dissent-preservation cases, the load-bearing concern is that **harness-side measurement is the missing primitive for cross-session-state-claim verifiability**, and any synthesis that does not adopt that primitive — at S071 or via principled-gated reopen — leaves the verifiability gap operationally open. The minority preservation lets future sessions reopen on the evidence-side as new laundering instances accumulate.
