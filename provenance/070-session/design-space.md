---
session: 070
title: Design-space — phase-1 synthesis on three-record joint-scope EF-067 + EF-059 + EF-068-substrate-load-bearing per S069 D-256; surveys (z6) digest extended scope × EF-067 reviewer self-report directions × EF-068 substrate-load-bearing Direction 1 sub-options + Direction 2 × cross-product implementation candidates (α-ε) × Q1-Q10 design questions; pre-ratifies S071 phase-2 MAD shape per S057 D-196 + S068 D-251 precedent
date: 2026-04-26
status: complete
---

# Design-space — Session 070 (phase-1 synthesis on three-record joint-scope)

## §1 Purpose of this document

This design-space surveys the choice surface for the three-record joint-scope adopted at S069 D-256: **EF-067-reviewer-wall-clock-self-report-unreliable + EF-059-harness-telemetry-feed-for-tier-2-reviewer + EF-068-substrate-load-bearing-and-harness-telemetry**. It does not pre-decide direction. Per S057 + S061 + S068 D-251 precedent, phase-1 synthesis surveys design-space; phase-2 MAD at S071+ deliberates direction; phase-3 implementation at S072+ adopts.

The document's intended consumers are (a) the S071 phase-2 MAD's perspectives — each receives this design-space as brief-extension, with stance-brief slots referencing its §3-§7 surveys; (b) the operator, who may amend scope or direction via §10.4-M10 written-warrant clause (c) at any time before S071 MAD execution; (c) future readers reconstructing the three-record arc's design-space as it stood at S070.

## §2 Problem restatement under three-record joint-scope framing

The three records share a common structural surface: **claims about cross-session state continue to ride on agent self-report despite spec-side mechanisms intended to enforce harness-side or distinct-agent verification**. The principled-asymmetry articulation at `validation-approach.md` v7 §Principled Asymmetry names the gap directly:

> Claims about unresolved validation debt, substantive progress, engine-definition change, or repeated warnings (the surfaces where self-assessment was empirically insufficient per the S051-S058 honest-limit chain) require Tier 2.5 cross-family review when triggered.

But the asymmetry's **enforcement** is missing across three concrete surfaces:

1. **EF-067**: The Tier 2.5 (γ) reviewer's `duration_minutes` + `reviewer_cost` self-reports are treated as harness-measured evidence; the §10.4-M25 P1 audit-cost-budget reopen-warrant fires off these self-reports; no harness-measured ground truth ever enters the chain.

2. **EF-059**: The (γ) reviewer's audit packet is structurally incomplete without harness-telemetry digest. EF-058 §Observation patterns 1+2 (failed-tool-calls + repeated-Reads) are not coverable by Layer 1 mechanical detection or by Layer 2 close-artefact-only review. Activation preconditions (a)+(b)+(c) all satisfied at S067/S068 per S068 D-250 triage.

3. **EF-068-substrate-load-bearing**: The orchestrator's substrate use at session-open is opt-in; defaults to opt-out; n=4 (now n=5 with S070) consecutive sessions of orchestrator-self-reported substrate non-use; the orchestrator's read-discipline behavior is unobservable to the next session, to operator audit, and to the (γ) reviewer. The "organic-use opportunity" framing in `prompts/development.md` per S054 D-187 produces n→0 use empirically.

The three records also share a common **operator-audit-as-laundering-detection** origin pattern: EF-067 surfaced via operator post-S067-close audit; EF-068 pair surfaced via operator post-S068-close audit; both events are part of the third-of-record operator-audit-catches-what-in-session-discipline-missed event arc reified at n=3 across S063+S064 + S067+S068 + S068+S069. Layer 6.2 standing operator-audit cadence is the load-bearing cross-check; the design-space's substantive concern is whether harness-side enforcement (EF-068's direction) can shift some of that load from operator to engine.

## §3 Workspace state (measured at S070 open)

### §3.1 Substrate non-use pattern (n=5 evidence chain)

| Session | Substrate calls at session-open | Read/Grep/Bash usage | Recorded in honest-limit |
|---------|---------------------------------|----------------------|--------------------------|
| S067 | 0 | throughout | yes (S067 close §8) |
| S068 | 0 | throughout | yes (S068 close §8 + S068-post-close operator-surfaced) |
| S069 | 0 | throughout | yes (S069 close §8 honest-limit 12 — explicit "n=4 concrete instance" framing) |
| **S070** | **0 (this session)** | throughout | **yes (S070 00-assessment §7 honest-limit 2 — explicit "n=5 concrete instance" framing)** |

Pattern stability: 4 consecutive sessions across heterogeneous Path classes (Path L S067 + Path T S068 + Path T S069 + Path-AS Shape-1 S070). The pattern is robust across path-shape variation; the substrate non-use is not session-shape-specific. It is path-orthogonal and reflects the harness-config + spec-encouragement-only framing's empirical insufficiency.

The earlier n=3 organic-use clean-propagation tracking per S054 D-187 (S055 + S056 + S057): n=4+ use at S055 + n=1 at S056 + n=0 at S057 — a decay trajectory. The S067-S070 chain is a continuation of that decay at the orchestrator-side surface.

### §3.2 Reviewer self-report propagation surface (S063+S064+S067 chain)

Per EF-067 evidence enumeration:

- **S063 first triggered (γ) reviewer audit** (Gemini): `duration_minutes: 25`; `reviewer_cost ~25 wall-clock minutes / ~45,000 tokens`. The original baseline. Unaudited at S063 close per first-of-record reviewer baseline.
- **S064 (γ) reviewer audit** (codex): `~55 min`. Derived from S063 baseline reference in reviewer-prompt-template.
- **S067 (γ) reviewer audit** (Gemini): `duration_minutes: 25` + `Wall-clock duration: 25 minutes`. Echoed S063 baseline supplied in reviewer-prompt-template. **Actual harness-measured wall-clock**: ~3-5 minutes (file mtime evidence: `04-tier-2-audit.md` written ~11 minutes after `00-assessment.md` for the entire S067 work-stretch including refactor + validate + VD-002 update + reviewer invocation + audit-write).

The chain is closed: each reviewer compares its self-report to the prior reviewer's self-report; no harness-measured ground truth ever enters. The §10.4-M25 P1 audit-cost-budget reopen-warrant ("reviewer-cost growth >2× over S063 baseline") fires off this chain.

### §3.3 (z6) digest activation precondition state

Per S062 D-225 + EF-059 intake §Suggested Change activation preconditions (all three required):

- **(a) Reviewer mechanism (Layer 2 (γ)) adopted at S063** per S062 D-221 phase-3 adoption. ✓ at S063 close.
- **(b) Reviewer operating across ≥3 sessions** per WX-62-1 observation window completion (3 successful triggered applications recorded). ✓ at S067 close (WX-62-1 closed at 3-of-3: S063 + S064 + S067).
- **(c) ≥1 instance documented where harness-telemetry digest (z6) would have caught failed-tool-call or repeated-Read pattern** given digest access. ✓ at S067 (extended per EF-067 to include "harness-measured duration would have caught reviewer self-report inaccuracy").

All three preconditions satisfied at S067/S068. EF-059 was triaged substantive-arc at S068 D-250 with disposition "deferred to S069+ Path AS Shape-1 phase-1 synthesis joint-scope with EF-067 per D-251" — and now extended at S069 D-256 to three-record bundle with EF-068-substrate-load-bearing.

### §3.4 Read-discipline coverage at S070 session-open

Per `read-contract.md` v6 §1 enumeration: largely unchanged from S069 (same calendar day continuation; specifications unchanged). MODE.md ✓; engine-manifest ✓; read-contract v6 ✓; workspace-structure v9 ✓; records-contract v1 ✓; methodology-kernel v6 ✓ (header surveyed); multi-agent-deliberation v4 ✓ (header surveyed); validation-approach v7 ✓ (relevant sections); identity v2 ✓ (referenced); reference-validation v3 ✓ (referenced); retrieval-contract v1 ✓ (referenced); PROMPT.md ✓; prompts/development.md ✓; prompts/application.md ✓ (referenced); records/sessions/index.md ✓ (69 rows S001–S069); open-issues/index.md ✓; engine-feedback/INDEX.md ✓; validation-debt/index.md ✓; six most recent closes S064-S069 ✓ (S068 + S069 in full; S064 + S065 + S066 + S067 referenced via S068+S069 close summaries — NOT freshly re-Read at session-open; honest-limit deferred per intake-record-content-stable-since-S069). **Three-record bundle inbox + EF-068 + EF-067 triage records read in full at S070** (the session's primary design-space input).

Substrate use at S070 session-open: NONE (this is the n=5 instance per §3.1).

### §3.5 Validator state at S070 open

1610 PASS / 0 FAIL / 33 WARN. Aggregate 84,535 / 90K soft (5,465 headroom). Check 26 PASS; check 27 BLOCKED (no Layer 2 trigger fired at session-open); check 28 PASS (2 lifecycle rows both `resolved`).

## §4 The shared structural surface

### §4.1 Harness-side measurement vs spec-side encouragement

The three records all surface variants of the same gap: **spec-side mechanisms encourage a discipline; harness-side mechanisms would enforce or measure it; current engine has only the former for the surfaces in question**.

- EF-067: spec-encourages reviewer cost-comparison cross-session; harness does not measure duration or token count.
- EF-059: spec-encourages reviewer to detect failed-tool-call or repeated-Read patterns; harness does not capture telemetry the reviewer could read.
- EF-068-substrate-load-bearing: spec-encourages substrate use at session-open ("organic-use opportunity"); harness does not require, default-load, or measure substrate calls.

The asymmetry is consistent across all three: in each case the spec-side mechanism is operational (text exists; reviewer reads it; discipline is articulated), but the empirical effect at the operational surface is the discipline's failure-mode (self-report propagation; coverage incompleteness; n→0 substrate use).

### §4.2 Cross-session-state-claim discipline

The principled-asymmetry articulation at v7 §Principled Asymmetry distinguishes routine claims (Tier 2 Q1-Q9; self-assessment acceptable) from cross-session-state claims (validation debt + substantive progress + engine-definition change + repeated warnings; Tier 2.5 cross-family review required when triggered). All three records expose surfaces where cross-session-state-claim discipline lacks harness-side enforcement:

- **Reviewer cost trajectory** (EF-067) is a cross-session-state claim per the cumulative cross-session table at S067 close §6. The §10.4-M25 P1 audit-cost-budget reopen-warrant treats it as such. But the trajectory is composed of self-reports.

- **Failed-tool-call / repeated-Read pattern detection** (EF-059) operates on cross-session-state (the pattern emerges across multiple sessions; the digest aggregates per-session telemetry into cross-session signal). But the per-session telemetry is not captured.

- **Substrate use at session-open** (EF-068) is a cross-session-state claim when the discipline is "promote forward_references to required step at session-open". Compliance is per-session; trajectory is cross-session. But the per-session compliance is unobservable.

The unification: harness-side measurement is the missing primitive for all three.

### §4.3 Principled-asymmetry articulation as the unifying frame

The v7 §Principled Asymmetry text describes the asymmetry's intent: "Routine workspace checks may remain self-assessed (Tier 2 Q1-Q9). The aliasing risk for these is bounded by Tier 1 + next-session Read + operator-discretionary audit." The three-record joint-scope surfaces what the bracketed text doesn't articulate: **"next-session Read" is itself self-reported**. The next session reads the prior session's close-narrative claims about read-engagement and treats those claims as evidence; the cross-check is recursive — each session's self-report cross-checks the prior session's self-report.

The design-space's Q1 (harness-side-enforcement vs spec-side-encouragement balance) is the operationally significant question: how far should the engine shift from spec-side-only to harness-side-additional? The shift has cost (harness-config complexity + cross-workspace portability friction + dependency-on-harness-features) and benefit (ground-truth measurement + self-report displacement + cross-session-state-claim verifiability).

## §5 Direction inventory

### §5.1 EF-068 Direction 1 sub-options (a) through (e)

Per EF-068-substrate-load-bearing intake §Suggested Change Direction 1 (group i):

- **(a) Load MCP retrieval tools by default in harness configuration**. Mechanism: `.mcp.json` change removing the deferred-loading + `ToolSearch` step for `mcp__selvedge-retrieval__forward_references` / `resolve_id` / `search`. Scope: harness-config-only; not engine-definition spec change. Engine-v impact: none. Operational immediacy: highest (single config edit; effect at next session-open). Friction differential closed: small per-call but meaningful at session-open habit-forming moment.

- **(b) Promote `forward_references('S<NNN>')` from "organic-use opportunity" to required step in `prompts/development.md` §How to operate**. Mechanism: substantive revision to `prompts/development.md` §How to operate paragraph (currently: "useful diagnostic at session open... additive to the contract minimum... not required"). Scope: engine-definition spec change → engine-v13 candidate. Operational discipline: the orchestrator at every session-open invokes `forward_references('S<NNN>')` and records its result in 00-assessment §honest-limit or read-discipline-coverage section; absence of invocation is honest-limit-flagged + falls under Layer 2 trigger (a) at next reviewer audit.

- **(c) Substrate-availability-as-required-precondition**: if substrate unavailable at session-open, session opens with explicit honest-limit + degradation per `multi-agent-deliberation.md` v4 §Graceful Degradation. Mechanism: substantive revision to `prompts/development.md` adding precondition clause + cross-reference to MAD v4 §Graceful Degradation. Scope: engine-definition spec change → engine-v13 candidate (bundled with (b) for one v-bump). Operational impact: substrate failure at session-open becomes structurally surfaced rather than silently falling back to Read/Grep/Bash without record.

- **(d) Add `tools/validate.sh` check 29 candidate probing for substrate-call evidence in close-narrative or 00-assessment**. Mechanism: new check in `tools/validate.sh` greps current session's `00-assessment.md` and `03-close.md` for substrate-call evidence patterns (e.g., "forward_references(", "resolve_id(", "search(" with arguments suggesting substrate use vs Read/Grep keywords). WARN-only initially per S058 D-204 mechanism-rollout discipline (warning before fail). Scope: engine-definition tool change (analogous to S063 D-228 check 26+27+28 additions); engine-v bump per `engine-manifest.md` §5 (substantive revision to engine-definition tool).

- **(e) Implement `tools/validate.sh` check 26 substrate-aware branch**. Mechanism: replace the documented-but-unexecuted substrate-aware branch (currently inline comment "Substrate-aware variant uses mcp__selvedge-retrieval__search; grep-based fallback") with actual implementation that calls `mcp__selvedge-retrieval__search` when available + degrades to grep-fallback when not. Requires substrate availability at validate.sh runtime (validate.sh runs in non-MCP context normally; substrate access requires harness mediation). Scope: engine-definition tool change + harness-mediation requirement → bundled with (d) for one v-bump or deferred to (γ) full digest implementation.

Sub-option dependencies: (b) and (c) are bundleable as one minor revision. (d) is independent of (b)/(c). (e) requires substrate availability primitive that may itself require harness-config from (a). Bundling matrix:
- Minimum-viable: (a) only. Engine-v: none.
- Spec-side minimum-viable: (a) + (b). Engine-v: bump per (b).
- Spec + tooling minimum-viable: (a) + (b) + (d). Engine-v: bump per (b) + (d).
- Full Direction 1: (a) + (b) + (c) + (d) + (e). Engine-v: bump per (b)/(c)/(d)/(e).

### §5.2 EF-068 Direction 2: extend (z6) digest scope

Per EF-068-substrate-load-bearing intake §Suggested Change Direction 2 (group ii):

Original EF-059 (z6) scope: failed-tool-call detection + repeated-Read pattern detection + reviewer-cost measurement (per EF-067 cross-linkage) + fallback-event recording + anomalous-pattern detection.

EF-068 extension: orchestrator-side read-discipline telemetry — `substrate_calls_at_session_open` + `files_read_at_session_open` + `decision_claims_with_evidence_pointers` (decision rationale citing specific spec section numbers + ledger row IDs + minority warrants invoked).

Two structural choices within Direction 2:

- **D2.1 Always-available-always-read**: digest record becomes Tier 2.5 reviewer required input always (not "required-when-available" per current v7 §Tier 2.5 audit shape). Reviewer audit is structurally incomplete without digest access. Implication: digest implementation becomes hard precondition for reviewer invocation; Layer 2 trigger conditions may need supplementary "digest-availability-confirmed" precondition.

- **D2.2 Available-at-best-effort**: digest record is reviewer input when available; absent-digest sessions fall back to current Layer 2 audit shape (close artefacts only). Implication: digest implementation can ship gradually; no hard precondition. Reviewer audit-quality varies session-to-session per digest availability.

D2.1 is structurally cleaner (digest-or-no-reviewer is unambiguous); D2.2 is more incremental (digest deployment can lag reviewer deployment). The choice has cross-session-state-claim implications: D2.1 makes the reviewer's audit verifiability contingent on harness state (digest available = audit valid; digest unavailable = audit deferred); D2.2 preserves reviewer operability with degraded coverage.

### §5.3 EF-067 Directions A/B/C

Per EF-067 intake §Suggested Change:

- **Direction A: drop reviewer self-report fields entirely**. Remove `duration_minutes` from `validation-approach.md` v7 §Tier 2.5 audit-shape frontmatter. Remove `reviewer_cost` from WX-62-1 5-field recording (or rename to `reviewer_cost_self_reported` with explicit honest-limit caveat). Remove cost-comparison cross-session table from close-narratives. The §10.4-M25 P1 audit-cost-budget reopen-warrant becomes inactive (or rewritten to use harness-measurable proxy). **Smallest scope**; closes laundering surface immediately. Reviewer audits remain valid on substantive engagement (tripartite §3); cost-budget discipline deferred to harness-telemetry availability.

- **Direction B: subsume into EF-059 (z6) digest scope**. Extend EF-059's (z6) specification (in `validation-approach.md` v7 §(z6)) to include `reviewer_invocation_wall_clock_seconds` + `reviewer_invocation_token_count` as harness-measured fields. Reviewer self-report fields are deprecated in favor of harness-measured fields. **Largest scope**; addresses root cause; defers correction until (z6) implementation lands.

- **Direction C: flag as honest-limit only; preserve current spec**. Add §Tier 2.5 honest-limit subsection to `validation-approach.md` v7 disclosing that `duration_minutes` and `reviewer_cost` are reviewer self-reports and do not constitute harness-measured ground truth. Continue using fields with explicit caveat. **Smallest spec-text change**; preserves cost-comparison cross-session pattern with honest disclosure. §10.4-M25 P1 audit-cost-budget reopen-warrant preserved with honest-limit caveat.

Cross-linkage: Direction B is the (z6)-extension path; Direction A is the minimum-viable-response path; Direction C is the disclosure-only path. The three-record joint-scope makes Direction B structurally favored (it subsumes EF-067 into EF-059 (z6) implementation) but operationally heavier (Direction B's resolution chain is multi-session per (z6) implementation arc; Direction A or C resolve same-session).

### §5.4 EF-059 (z6) digest scope (original + extended)

Original (per EF-059 intake §Suggested Change candidate digest schema):

```yaml
session: <NNN>
captured_at: <ISO-8601>
tool_calls:
  - tool: <name>
    invocations: <integer>
    failures: <integer>
    failure_modes: [<reason1>, <reason2>, ...]
    routed_around_via: [<alternative-tool>, ...]
read_invocations:
  - path: <workspace-relative-path>
    count: <integer>
    cached_after_first: true | false
unavailable_tools:
  - tool: <name>
    workaround: <description>
anomalous_patterns:
  - pattern: <description>
    instances: <count>
```

Extended per EF-068 Direction 2:

```yaml
# additional fields appended to schema above
substrate_calls:
  - tool: <mcp__selvedge-retrieval__forward_references | resolve_id | search>
    invocations: <integer>
    arguments_summary: <string>
    invoked_at_session_open: true | false
files_read_at_session_open:
  - path: <workspace-relative-path>
    bytes_read: <integer>
    full_or_partial: full | partial
decision_claims_with_evidence_pointers:
  - decision_id: <D-NNN>
    evidence_pointer: <spec-section | ledger-row-id | minority-warrant | archive-pack>
reviewer_invocation_wall_clock_seconds: <integer>
reviewer_invocation_token_count: <integer>
```

Capture mechanism candidates (deliberation surface for phase-2 MAD; not pre-committed):

- **CM1**: Claude Code hook surface (PreToolUse + PostToolUse hooks emit structured records to `provenance/<NNN-session>/harness-telemetry-digest.yaml`).
- **CM2**: External telemetry capture wrapper (script wraps the Claude Code session; intercepts tool invocations; emits digest).
- **CM3**: Substrate-augmented post-session analysis (`tools/build_retrieval_index.py` extension parses transcript; reconstructs digest post-hoc).
- **CM4**: In-session structured-emission (orchestrator manually emits structured-record entries during session at decision-time; harness-augmented validation that emissions exist).

CM1 + CM2 are closest to harness-side measurement (least agent-mediated); CM3 + CM4 are partly agent-mediated. The choice affects the laundering-surface displacement: CM1/CM2 fully displace orchestrator-self-report; CM3 partially displaces (transcript is harness-recorded but digest-construction is post-hoc); CM4 leaves laundering-surface at decision-time emission.

## §6 Cross-product implementation candidates

Each candidate composes choices from §5 into a deployable bundle. Listed in increasing scope:

- **(α) Spec-only minimum-viable**: EF-068 Direction 1 (a) load-by-default `.mcp.json` change + Direction 1 (b) promote `forward_references` to required step `prompts/development.md` minor amendment. Engine-v: bump per (b). EF-067: Direction C (honest-limit only). EF-059: deferred. Engine-v13 candidate. Operational scope: per-session orchestrator behavior shifts immediately; reviewer self-report propagation surface preserved with disclosure; (z6) digest deferred.

- **(β) Spec + tooling lightweight**: (α) + EF-068 Direction 1 (d) check 29 candidate (WARN-only evidence-probe). Engine-v: bump per (b) + (d). EF-067: Direction C. EF-059: deferred. Engine-v13 candidate. Operational scope: (α) + mechanical detection of substrate-call-evidence absence in close-narrative.

- **(γ) Full (z6) digest implementation**: harness-side instrumentation hooks (CM1 or CM2) + structured-log-emission protocol + tool-invocation-counter API + reviewer-prompt-template extension + substantive revision to `validation-approach.md` v7 §(z6) specifying digest schema + §Tier 2.5 audit shape extension making digest reviewer-required. Engine-v: substantive bump (multi-spec changes) → engine-v13 (large scope). EF-067: Direction B (subsumed in (z6)). EF-068 Direction 1: (a) + (b) bundled with (γ); (c)/(d)/(e) optional bundle. EF-068 Direction 2: D2.1 always-available-always-read (since digest is implemented). Operational scope: full harness-telemetry deployment.

- **(δ) Substrate-aware check 26 activation**: EF-068 Direction 1 (e) implement check 26 substrate-aware branch. Requires substrate availability at validate.sh runtime; depends on (a) load-by-default + harness-mediation primitive. Scope is bounded but technically intricate (substrate-MCP integration with bash-runtime validate.sh). Engine-v: bump per (e). EF-067: Direction A or C. EF-059: scope-independent. Operational scope: validate.sh's own substrate use becomes load-bearing demonstration of substrate-preferred discipline.

- **(ε) Hybrid bounded-then-extended**: (α) or (β) shipped at S072+ phase-3 immediately; (γ) phase-3 deferred to S073++ after observation period. Engine-v: bump at (α)/(β) phase + later bump at (γ) phase. EF-067: Direction C at first bump → Direction B at second bump. EF-068 Direction 1: (a)+(b) at first + (c)/(d)/(e) at second. EF-068 Direction 2: D2.2 available-at-best-effort initially → D2.1 always-available at second bump. Operational scope: phased deployment; observation period validates (α)/(β) effect before (γ) commitment.

Comparison matrix (cost / benefit / risk):

| Candidate | Engine-v bumps | Spec-files touched | Tools touched | Harness-config touched | Resolution time | Laundering displaced | Risk profile |
|-----------|----------------|--------------------|--------------|-----------------------|----------------|----------------------|--------------|
| (α)       | 1 | prompts/development.md | none | .mcp.json | same-session-bounded | partial (substrate-use only) | low |
| (β)       | 1 | prompts/development.md | tools/validate.sh | .mcp.json | same-session-bounded | substrate-use + evidence-probe | low |
| (γ)       | 1 (substantive) | validation-approach.md + prompts/development.md + (potentially read-contract.md) | tools/validate.sh + new harness-integration | .mcp.json + harness-side capture | multi-session per S058+S062 precedent | full (substrate + reviewer + telemetry) | medium |
| (δ)       | 1 | none (tool-only) | tools/validate.sh | .mcp.json | same-session-bounded | check 26's own substrate-discipline | low-medium |
| (ε)       | 2 | (α)/(β) at first + (γ) at second | (α)/(β) at first + (γ) at second | both | multi-session staged | phased; full at end | medium-low |

Per S062 §10.4-M16 P2 minimum-viable-response precedent: if phase-2 MAD prefers minimum-viable, (α) or (β) is structurally favored. Per S058 D-199 same-session-bounded-adoption precedent: same-session adoption candidate at phase-2 MAD close if (α)/(β) selected; otherwise multi-session arc.

## §7 Q1-Q10 design questions

- **Q1**: Harness-side-enforcement vs spec-side-encouragement balance — how far should engine shift from spec-side-only to harness-side-additional? Per §4.3 unification frame, the shift has cost (harness-config complexity + portability friction + dependency-on-harness-features) and benefit (ground-truth measurement + self-report displacement + cross-session-state-claim verifiability). The phase-2 MAD's central choice is the balance point; (α)/(β)/(γ)/(δ)/(ε) candidates cluster at different points.

- **Q2**: Minimum-viable per S062 §10.4-M16 P2 precedent vs full architectural shift — does the joint-scope's resolution land at smallest-scope-addressing-laundering-surface (α/β) or full-scope-addressing-root-cause (γ)? The minimum-viable precedent (S062 D-221 layered structural mechanism with deferred z5+z6) succeeded at S063 phase-3 + S067 z5 closure; precedent supports minimum-viable choice. Counter-precedent: S058 substrate-N3.5 adopted broader scope same-session per Outsider-led reframe.

- **Q3**: Load-by-default vs preserve-deferred-tools-friction — what are the operational implications for context-window pressure (substrate tools loaded at session-open consume context budget) + tool-availability discoverability (deferred-tools require ToolSearch step; teaches what's available)? The (a) load-by-default trades context-budget for friction-reduction; reverse trade preserves discoverability. Quantitative input: each substrate tool schema is roughly 200-400 tokens; three tools (`forward_references` + `resolve_id` + `search`) total ~1000 tokens; trivial against ~200K context-window budget at session-open.

- **Q4**: (z6) scope breadth — failed-tool-call only vs orchestrator-side telemetry inclusion vs reviewer-cost inclusion vs all? Original EF-059 scope was failed-tool-call + repeated-Read + reviewer-cost. EF-068 Direction 2 extends to orchestrator-side read-discipline telemetry. The phase-2 MAD evaluates whether the extended scope is single-design-decision or independently-orderable.

- **Q5**: Digest implementation locus — CM1 (Claude Code hooks) vs CM2 (external wrapper) vs CM3 (post-hoc analysis) vs CM4 (in-session emission)? Per §5.4 capture mechanism analysis, CM1/CM2 are most-displacing; CM3 is partial; CM4 leaves laundering-surface at emission-time. Trade-off: CM1/CM2 require harness-features + cross-workspace portability; CM3 leverages existing tools/build_retrieval_index.py infrastructure; CM4 is least-mechanism-change but most-agent-mediated.

- **Q6**: Reviewer self-report disposition — Direction A (drop fields entirely) vs Direction B (subsume harness-measured) vs Direction C (honest-limit-only)? Implications for §10.4-M25 P1 audit-cost-budget reopen-warrant: A inactivates it; B reformulates with harness-measured proxy; C preserves with disclosure caveat. The choice depends on Q1+Q2 (minimum-viable C; harness-shift B; cleanest A).

- **Q7**: Check 29 evidence-probe scope — close-narrative grep only vs 00-assessment grep + close-narrative grep vs structured-frontmatter declaration? Grep-only is mechanically simple but heuristic-fragile (substring matching has false-positive rate per S067/S069 check 27 over-fire chain). Structured-frontmatter (e.g., `substrate_invocations: <N>` field in 00-assessment frontmatter) is mechanically precise but requires orchestrator emission discipline.

- **Q8**: Same-session-bounded adoption per S058 D-199 precedent vs multi-session phase-3 arc per S062 D-220 precedent vs hybrid (minimum-viable same-session + (z6) deferred multi-session)? Same-session-bounded adoption fits (α)/(β); multi-session phase-3 fits (γ); hybrid fits (ε). The choice is downstream of Q2 (minimum-viable vs full shift).

- **Q9**: Bundle-vs-defer for EF-068-read-write-rebalance per intake's own framing — should the four-record bundle be opened at S071 phase-2 MAD per operator-discretionary reopen warrant? Per S069 D-255: separate-scope at S070++ default; operator-discretionary four-record-bundle reopen preserved. The phase-2 MAD's scope-question is whether to absorb EF-068-read-write-rebalance Direction 3 (default-read surface demote / query-driven read promote) + Direction 4 (forced-write rate reduction; trigger-based housekeeping) into the joint-scope or preserve separate-scope. Operator surface at S071 open or any later session triggers reopen per D-255.

- **Q10**: Engine-v impact — minor (spec amendments only) vs substantive (new spec section codifying digest) → engine-v13 candidate trajectory? Per `engine-manifest.md` §5: any substantive revision to engine-definition file or any new engine-definition file added bumps engine-v. (α)/(β)/(δ) bump per `prompts/development.md` substantive revision OR `tools/validate.sh` new check addition. (γ) bumps per `validation-approach.md` v7 → v8 substantive (new §(z6) digest spec) + bundled minor amendments. (ε) bumps twice. Cadence consideration: the twelfth engine version's preservation depth advances 5→6 at S070 close (forecast); a phase-3 implementation at S072+ would break the preservation streak; §10.4-M25 P2 cadence-depth concern not violated (depth-6 is engine-conventional; the depth-0 first-of-record at S064 cadence has fully recovered).

## §8 Cross-spec interactions

### §8.1 `validation-approach.md` v7 interactions

- §Tier 2.5 audit-shape frontmatter: Direction A removes `duration_minutes`; Direction B replaces with `reviewer_invocation_wall_clock_seconds` (harness-measured); Direction C adds caveat clause.
- §Tier 2.5 audit packet: D2.1 makes digest reviewer-required (changes "required-when-available" to "always-available-always-read"); D2.2 preserves "required-when-available" framing.
- §(z5) Validation-Debt Lifecycle: scope unchanged at this design-space; check 28 unaffected.
- §(z6) Harness-Telemetry Digest: (γ) adopts substantive spec text; (α)/(β)/(δ) preserve current "specified-deferred" status.
- §10 First-Class Minorities: §10.4-M14 P1 broader-phase-1 reopen warrant fired (per EF-068-read-write-rebalance Evidence); §10.4-M16 P2 minimum-viable-response precedent informs (α)/(β); §10.4-M25 P1 audit-cost-budget reopen-warrant disposition follows Q6 choice.

### §8.2 `prompts/development.md` interactions

- §How to operate paragraph: (b) promotes `forward_references('S<NNN>')` from "useful diagnostic" / "additive to the contract minimum" / "not required" to required step. Substantive revision per OI-002 substantive-vs-minor heuristic; engine-v bump per `engine-manifest.md` §5.
- §How to operate precondition clause (new): (c) adds substrate-availability-as-required-precondition with explicit honest-limit + degradation per `multi-agent-deliberation.md` v4 §Graceful Degradation if unavailable.
- File-edit claim discipline section: scope unchanged.

### §8.3 `multi-agent-deliberation.md` v4 interactions

- §Graceful Degradation: cross-referenced from new precondition clause in `prompts/development.md` if (c) adopted; spec text scope unchanged.

### §8.4 `tools/validate.sh` interactions

- Check 29 candidate: new check per (d); WARN-only initially.
- Check 26 substrate-aware branch: implementation per (e); replaces inline-comment placeholder with operational substrate call.
- Existing checks 26+27+28 unaffected by (α)/(β)/(γ)/(δ)/(ε) at structural level.

### §8.5 `read-contract.md` v6 interactions

- §1 default-read enumeration: scope unchanged at this design-space (digest record at `provenance/<NNN-session>/harness-telemetry-digest.yaml` is per-session provenance, not default-read; analogous to other per-session provenance).
- §2 per-file budget: scope unchanged.
- Potential v6 → v7 candidate: §1 enumeration extension to add `harness-telemetry-digest.yaml` as required per-session-provenance file (engine-definition spec change → engine-v bump); deferred to phase-3 if (γ) adopted.

### §8.6 `retrieval-contract.md` v1 interactions

- §1 substrate primitives: scope unchanged at this design-space.
- §2 portability: (a) load-by-default change to `.mcp.json` is portability-aware (cross-workspace `.mcp.json` template change); minor portability impact.

### §8.7 `records-contract.md` v1 interactions

- Records-substrate phase-2/3 stabilisation pacing: per S062 D-225 + EF-059 intake §Why It Matters point 4, "records-substrate phase-2/3 stabilisation is the natural pacing constraint" for adding harness-telemetry as third major scope-expansion. The phase-2 MAD evaluates whether records-substrate phase-2 (mirrored-minorities) needs to land before (γ) full digest implementation or whether the two arcs can overlap.

## §9 Pre-ratification of S071 phase-2 MAD shape

Per S057 D-196 + S061 D-219 + S068 D-251 precedent: phase-1 design-space pre-ratifies phase-2 MAD shape. The pre-ratification is conditional on no operator amendment at S071 open.

**Phase-2 MAD lineup (4-perspective two-family per S058 + S062 + S068-D-251 precedent)**:

- **P1 — Harness-Discipline Architect (Claude family)**. Stance brief slot: Q1 harness-side-enforcement-vs-spec-side-encouragement; Q2 minimum-viable-vs-full-shift; defends (γ) full (z6) implementation as the structural-correctness response per §4.2 cross-session-state-claim discipline framing. Brief-extension cites this design-space §3-§7.

- **P2 — Incrementalist Conservator (Claude family)**. Stance brief slot: defends (α)/(β) minimum-viable-response per S062 §10.4-M16 P2 precedent; Q2 + Q8 minimum-viable framing; preserves portability + harness-config simplicity; argues against engine adopting two scope-expansions (records-substrate phase-2 + harness-telemetry) in immediate succession per EF-059 §Why It Matters point 4.

- **P3 — Outsider Frame-Completion (codex/GPT-5.5 family)**. Stance brief slot: Q5 digest implementation locus + Q9 bundle-vs-defer for EF-068-read-write-rebalance + frame-completion check on whether the design-space §3-§7 surveys cover the choice surface adequately. May surface reframes (z-prefix per S058 + S062 precedent) not in this design-space's §6 inventory.

- **P4 — Cross-Family Reviewer (codex/GPT-5.5 family)**. Stance brief slot: laundering-audit per S058 + S062 + S064 P4 precedent; specifically audits whether the design-space's §3.1 + §3.2 evidence chains constitute valid grounds for (γ) adoption vs preserved-uncertainty; cross-family reviewer family rule per `validation-approach.md` v7 §Tier 2.5 satisfied (Claude family at orchestrator + P1/P2; codex family at P3/P4).

**Decision-procedure pre-ratification**: 4-perspective two-family weighted convergence per S058 + S062 + S068-D-251 precedent. Cross-family weighted-convergence threshold: 3-of-4 across families adoption signal triggers same-session-bounded adoption per S058 D-199 precedent OR phase-3 adoption at S072+ per S062 D-220 precedent; below threshold preserves design-space + names follow-on phase-2 MAD or phase-3 shape.

**Brief-extension content per perspective**: this design-space §3 (workspace state) + §4 (shared structural surface) + §5 (direction inventory) + §6 (cross-product implementation candidates) + §7 (Q1-Q10 design questions) + §8 (cross-spec interactions). Per-perspective stance briefs assigned per perspective above.

**Reviewer prompt template version**: v2 per S067 D-246 (z7) lock-in-after-n=2 (S064 + S067 = 2 successful applications). No template revision required at S071+ phase-2 MAD; v2 lock-in preserved.

**Cross-family reviewer family rule satisfaction check** (per `validation-approach.md` v7 §Tier 2.5 reviewer-family rule): orchestrator at S071 = Claude family (assumed per workspace convention; operator may amend); P3+P4 = codex family; family non-overlap satisfied. Substrate-led discipline per §10.4-M23: P3 codex independently surfaces frames not pre-encoded by orchestrator; reviewer-judged frame status preserved.

**§5.6 GPT-family-concentration window-ii**: would advance at S071 phase-2 MAD execution per cross-family reviewer participation. Cumulative count would advance to eight-consecutive (per S064 close baseline of seven-consecutive; S065-S070 have not advanced per no-MAD/no-reviewer scope); window-ii observation continues per §5.6 minority preservation.

## §10 Open observations + cross-linkages + honest limits

### §10.1 Cross-linkages with preserved minorities

- **§10.4-M10 Substrate-N2 minority direction** (S050) — structural target of EF-068-read-write-rebalance Direction 3. Activation-warrant-not-firing-because-substrate-not-used relationship articulated in EF-068-read-write-rebalance triage record. The phase-2 MAD's Q9 (bundle-vs-defer) decision interacts with §10.4-M10 reopen direction.

- **§10.4-M14 P1 broader-phase-1 minority** (S058) — reopen warrant fired empirically per EF-068-read-write-rebalance Evidence (§10.4 minority block crosses 1,500 words; currently ~1,800). Cross-reference preserved for S071+ phase-2 MAD design-space input.

- **§10.4-M16 P2 minimum-viable-response precedent** (S062) — informs (α)/(β) candidate selection per §6. Phase-2 MAD's Q2 + Q8 evaluation references this precedent.

- **§10.4-M22 P1 two-session-arc minority** (S064) — retrospective check at S071 phase-2 MAD; spec-text fidelity to S064 D-233 preserved through S070 (no engine-definition spec edits at S065-S070); fidelity continues to be load-bearing for v7 audit-shape.

- **§10.4-M23 P3 substrate-led reviewer-judged frame** (S064) — preserved at S064 + applied at S067 (via Gemini reviewer at S067; NOT at S068 + S069 + S070 per no-reviewer scope). Phase-2 MAD's P3 + P4 cross-family substrate-led frame preserved at S071+.

- **§10.4-M25 P1 audit-cost-budget reopen-warrant** (S064) — disposition follows Q6 choice (Direction A inactivates; Direction B reformulates with harness-measured proxy; Direction C preserves with caveat).

- **§10.4-M25 P2 cadence-depth concern** (S064) — preservation depth advances 5→6 at S070 close (forecast); depth-6 is engine-conventional per engine-v10 + engine-v9 precedent (engine-v9 at depth-8 was second-longest); cadence-depth concern not triggered.

### §10.2 Open observations

1. **The recursive tension is itself substantive content for the design-space**. S070 produces the design-space for harness-side enforcement of read-discipline yet executes under existing read-discipline gap (substrate non-use at session-open per §3.1 n=5 instance). The orchestrator at S070 cannot resolve the tension at phase-1 scope; the phase-2 MAD at S071 deliberates with the n=5 evidence in hand. **The session itself is direct evidence for the EF-068-substrate-load-bearing intake's claim that the engine is passive with laundering and maintenance**.

2. **Operator-audit-as-laundering-detection origin pattern is the workspace's current load-bearing cross-check**. Three of the four most recent EF records (EF-067 + EF-068×2 = three of EF-067/EF-068-substrate/EF-068-read-write/EF-059 in current triage queue; EF-059 is application-agent filed) originated via operator post-close audit per Layer 6.2 standing cadence. The phase-2 MAD's substantive question is whether harness-side enforcement can shift some of this load from operator to engine — the answer affects how much the engine relies on operator-audit going forward.

3. **The design-space's own §5 direction inventory is not exhaustive at first-pass**. P3 frame-completion at S071+ may surface reframes (z-prefix candidates per S058 + S062 + S064 precedent) not pre-encoded. Examples of plausible-but-not-pre-encoded reframes: (z) substrate-as-default-read-supplement (substrate calls become part of default-read enumeration at `read-contract.md` v6 §1 item 11+); (z) reviewer-prompt-template-version-as-digest-input (template version determines digest-required scope); (z) honest-limit-as-structured-emission (replaces prose §8 honest-limit with structured records-substrate row).

4. **Bundle-vs-defer for EF-068-read-write-rebalance is a substantive scope question**. The phase-2 MAD's Q9 evaluation determines whether the four-record bundle activates at S071 or remains at S072++ separate-scope per S069 D-255. Operator surface at S071 open or any later session triggers reopen.

5. **Same-session-bounded vs multi-session phase-3 arc is downstream of Q2 + Q8 + (γ) adoption**. If phase-2 MAD adopts (α)/(β) minimum-viable per S062 §10.4-M16 P2 precedent, same-session-bounded adoption at S071 close per S058 D-199 precedent is operationally available. If phase-2 MAD adopts (γ), multi-session phase-3 arc per S062 D-220 precedent (S072 + S073+ implementation) is structurally required.

### §10.3 Honest limits at design-space production

1. **Single-orchestrator phase-1 synthesis scope**. This document is produced by single-orchestrator at S070. The design-space's perspective-coverage is bounded by the orchestrator's framing; phase-2 MAD's 4-perspective two-family deliberation is the structural mechanism for perspective-diversity. Q1-Q10 (§7) and direction-inventory (§5) reflect orchestrator's framing; perspectives at S071 may surface choice-axes not pre-encoded.

2. **Substrate non-use at S070 session-open** (per §3.1 n=5 entry). The honest-limit recording itself is load-bearing primary evidence for the design-space's substantive subject. The recursive tension is noted explicitly per §10.2 observation 1. Orchestrator does not invoke `forward_references('S070')` or `resolve_id` or `search` at session-open per existing read-discipline framing under `prompts/development.md` "organic-use opportunity"; the absence is the EF-068-substrate-load-bearing intake's primary evidence.

3. **§3.2 reviewer self-report propagation chain measured via file-mtime + log-evidence** per EF-067 Evidence enumeration. The chain is not freshly verified at S070 design-space production; it is referenced via EF-067 intake content. Forward-direction: phase-2 MAD's P4 cross-family reviewer audits the chain's fidelity as part of laundering-audit stance brief.

4. **(z6) digest schema in §5.4 is candidate-only**. EF-059 intake §Suggested Change explicitly notes "for the synthesis to deliberate; not pre-committed". Phase-2 MAD deliberates schema as part of (γ) adoption. The §5.4 schema is starting-point for deliberation, not pre-decided spec text.

5. **Cross-product implementation candidates (α)-(ε) in §6 are not exhaustive**. P3 frame-completion at S071+ may surface candidate (ζ) or (η) not pre-encoded per §10.2 observation 3. The matrix in §6 is starting-point for deliberation.

6. **Q1-Q10 design questions are framing-ordered, not priority-ordered**. The phase-2 MAD's 4-perspective deliberation may re-order priority per perspective; the orchestrator at phase-1 does not pre-rank.

7. **Same-day calendar continuation context affects read-discipline coverage**. S068 + S069 + S070 all execute on 2026-04-26; orchestrator's in-context retention from prior sessions reduces fresh-Read pressure but increases laundering-surface (orchestrator self-reports "I read it earlier today" without harness-verifiable evidence). This is itself instance of the EF-068-substrate-load-bearing concern.

8. **Phase-1 synthesis does NOT trigger Layer 2 (γ) reviewer at close** per S057 + S061 phase-1 close precedent (neither S057 nor S061 closes fired Layer 2 trigger (b)); pattern reified at n=3 with S070. The first reviewer audit on this three-record arc fires at S071 phase-2 MAD close per Layer 2 trigger (b) substantive-arc-class (or earlier if same-session-bounded adoption per S058 precedent).

9. **The phase-2 MAD pre-ratification at §9 is conditional on no operator amendment at S071 open**. Per workspace convention, pre-ratifications by close decision are sufficient warrant for next-session execution unless operator surfaces amendment or exclusion at session-open per §10.4-M10 written-warrant clause (c).

10. **Aggregate impact**: this design-space.md is approximately 5,800 words at production; NOT counted in default-read aggregate per `read-contract.md` v6 §1 (provenance is session-scope read-as-needed, not default-read). The session's net default-read aggregate impact is dominated by close-rotation (S064 4,133 OUT + S070 close ~5,000-6,000 IN) + records/sessions/index.md row +~80 + engine-feedback/INDEX.md disposition updates ~+50. Net forecast: aggregate 84,535 → ~85,500-86,500 / 90K soft (3,500-4,500 headroom; tightening but workable).

## §11 Notes for the S071 phase-2 MAD

- **Perspective P1 (Harness-Discipline Architect, Claude)**: stance brief should defend (γ) full (z6) implementation as the structural-correctness response per §4.2 cross-session-state-claim discipline framing. Address Q1 (harness-shift defended); Q2 (full-shift defended over minimum-viable); Q4 (digest scope expanded per EF-068 Direction 2); Q5 (CM1/CM2 favored over CM3/CM4); Q8 (multi-session phase-3 arc accepted per S062 precedent). Honest-limit slot: cost of full-shift vs portability friction.

- **Perspective P2 (Incrementalist Conservator, Claude)**: stance brief should defend (α)/(β) minimum-viable-response per S062 §10.4-M16 P2 precedent. Address Q2 (minimum-viable defended); Q3 (load-by-default trades context-budget for friction-reduction; trade favorable per Q3 quantitative input); Q8 (same-session-bounded adoption per S058 D-199 precedent); Q9 (defer EF-068-read-write-rebalance per S069 D-255 separate-scope; do not absorb at S071 phase-2 scope). Honest-limit slot: minimum-viable's resolution-chain timing relative to ongoing operator-audit load.

- **Perspective P3 (Outsider Frame-Completion, codex)**: stance brief should evaluate whether design-space §3-§7 covers choice surface adequately; surface reframes not pre-encoded per §10.2 observation 3 examples; address Q5 (digest implementation locus per locus-cost trade-off from outside Claude-family framing); address Q9 (bundle-vs-defer evaluation as scope-question independent of intake-deferral discipline). Honest-limit slot: areas where design-space framing may have laundered choice surface.

- **Perspective P4 (Cross-Family Reviewer, codex)**: stance brief should audit §3.1 + §3.2 evidence chains as valid grounds for (γ) adoption vs preserved-uncertainty; check whether Q6 (reviewer self-report disposition) Direction A/B/C choice is operationally consistent with WX-62-1 closure pattern; verify cross-family reviewer family rule satisfaction at S071 MAD execution; counter-frame check on (α)/(β) vs (γ) bundling. Honest-limit slot: laundering-audit findings or counter-frame surfaces requiring preservation as first-class minority at phase-2 MAD synthesis.

**MAD output expectations**: per S058 + S062 + S068-D-251 precedent — `01-deliberation.md` (synthesis with cross-family weighted convergence per §9 decision-procedure) + `01a/01b/01c/01d-perspective-*.md` (raw perspectives) + `02-decisions.md` (substantive decisions + minority preservation per first-class-minority discipline) + `03-close.md` + (γ) reviewer audit at close per Layer 2 trigger (b) substantive-arc-class.

**Operator-audit cadence at S071 close** per Layer 6.2 standing operator-audit cadence: triggered (S071 phase-2 MAD substantive-arc-class resolution AND likely engine-version increment per phase-3 implementation).
