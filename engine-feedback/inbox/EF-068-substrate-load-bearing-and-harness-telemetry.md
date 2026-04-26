---
feedback_id: EF-068-substrate-load-bearing-and-harness-telemetry
source_workspace_id: selvedge-self-development
source_session: 068
created_at: 2026-04-26T13:30:00Z
reported_by: operator
target: methodology
target_files:
  - PROMPT.md
  - prompts/development.md
  - specifications/retrieval-contract.md
  - specifications/validation-approach.md
  - tools/validate.sh
  - .mcp.json
  - engine-feedback/inbox/EF-059-harness-telemetry-feed-for-tier-2-reviewer.md
  - engine-feedback/inbox/EF-067-reviewer-wall-clock-self-report-unreliable.md
severity: friction
status: new
---

## Observation

Substrate use is opt-in and the orchestrating agent (Case Steward) defaults to opt-out. Across S067 + S068 (the two most recent sessions, executed in operator's presence with substantive engineering work), the orchestrator made **zero** `mcp__selvedge-retrieval__*` calls — neither `forward_references` at session-open (despite `prompts/development.md` §How to operate paragraph encouragement) nor `resolve_id` for ID resolution nor `search` for prose lookup. Read/Grep/Bash were used throughout. The orchestrator self-reported at S068 post-close (operator-surfaced question): "Once I read [X] in-context, I felt I 'knew' forward-commitments and didn't need to query."

This self-report is **structurally identical to the Gemini wall-clock self-report flagged at EF-067** — agent claims "I have it" as evidence-of-engagement; nothing mechanically checks the claim. It is the same laundering-shape that EF-058-tier-2-validation surfaced for cross-session honest-limit text propagation (S051-S058 chain). The principled-asymmetry articulation in `validation-approach.md` v7 names this directly: "claims about unresolved validation debt, substantive progress, engine-definition change, and repeated warnings require stateful or distinct review" — precisely because in-session self-assessment is empirically insufficient.

Compounding observations:

1. **`tools/validate.sh` check 26 substrate-aware branch is documented but never executed.** The code says "Substrate-aware variant uses mcp__selvedge-retrieval__search; grep-based fallback" — but only the grep-fallback runs. The canonical engine-definition tool does not exercise the substrate it claims to prefer. This is a strong signal across the workspace that substrate use is operationally aspirational.

2. **Deferred-tool friction.** `mcp__selvedge-retrieval__forward_references` / `resolve_id` / `search` appear in the agent's deferred-tools list at session-open. Calling them requires a `ToolSearch` step to load schemas. Read/Grep/Bash are loaded by default. The friction differential is small per call but meaningful at the session-open habit-forming moment.

3. **Session-open habit unobservable.** Nothing in the harness records whether the orchestrator called the substrate at session-open or skipped it. The orchestrator's read-discipline behavior is unobservable to the next session, to operator audit, and to the Tier 2.5 reviewer. EF-059's (z6) harness-telemetry-digest scope is exactly the instrument that would address this — but EF-059 is deferred, and its activation preconditions accrued via EF-067 (reviewer self-report) without yet capturing the prior-side concern (orchestrator self-report).

4. **Cumulative structural finding from S062 EF-058-tier-2-validation MAD**: §Principled Asymmetry articulation states that routine claims may remain self-assessed but cross-session-state claims require stateful or distinct review. The default-read surface enumerated in `read-contract.md` v6 §1 is sufficient for routine claims; it is **not sufficient for cross-session-state claims**. The substrate is the workspace's tool for the latter. The substrate's non-use means cross-session-state claims continue to ride on agent self-report.

## Why It Matters

This is the engine's outermost laundering surface, and it is structurally invisible. The operator's framing post-S068: "I don't know why the system is so passive with this laundering and maintenance." The passivity is observable across multiple data points:

- **EF-058-tier-2-validation** surfaced self-assessment-empirically-insufficient at S058 close. Twenty-one sessions have elapsed (S058 → S068). The structural mechanisms adopted (Tier 2.5 reviewer + (z5) lifecycle ledger + check 26 + check 27 + check 28) are spec-side encoded. Harness-side enforcement on the orchestrator's read behavior has not been adopted. Twenty-one-session delay between problem-articulation and root-cause-fix is the cadence-of-passivity.

- **(z6) harness-telemetry-digest** has activation preconditions, all satisfied at S067, and was triaged substantive-class arc deferred at S068 D-250. The deferral is principled per joint-scope MAD discipline, but the time-to-implement is a multi-session arc when harness-instrumentation is the load-bearing piece for the engine's own discipline-discovery.

- **Validate.sh check 26 substrate-aware branch unimplemented** demonstrates that even when the engine-definition tool spec-encodes substrate preference, the implementation defaults to fallback. The fallback path is the path-of-least-resistance; substrate-preferred is aspirational.

- **`forward_references('S<NNN>')` framed as "organic-use opportunity"** in `prompts/development.md` per S054 D-187. Three sessions of organic-use clean-propagation tracking (S055 + S056 + S057) showed n=4+ + n=1 + n=0 use; subsequent sessions (S060+, S061+, S067+, S068+) show n=0 use. The "organic-use opportunity" framing produces n→0 use. Encouragement-without-enforcement is empirically insufficient.

If the system continues passive: the laundering surfaces accumulate; structural mechanisms continue to be added (Tier 2.5; (z5); future (z6); check 26/27/28; future check 29+); but the orchestrator's actual read-discipline behavior remains unmeasured and self-reported. Each new structural mechanism adds spec-side discipline without adding harness-side enforcement; the cadence-of-passivity compounds.

The principled-asymmetry articulation at v7 §Principled Asymmetry already names the gap: "Routine workspace checks may remain self-assessed (Tier 2 Q1-Q9). The aliasing risk for these is bounded by Tier 1 + next-session Read + operator-discretionary audit." But "next-session Read" is itself self-reported — the next session reads the prior session's close-narrative claims about read-engagement and treats those claims as evidence. The asymmetry is articulated; the asymmetry's enforcement is missing.

## Suggested Change

This record proposes **two coupled directions**, intended for joint-scope with EF-059 + EF-067 (which were already bundled at S068 D-251 for S069+ Path-AS Shape-1 phase-1 synthesis). EF-068-substrate-load-bearing extends that joint-scope.

**Direction 1 (group i): Make substrate use load-bearing at session-open.**

- Promote `forward_references('S<NNN>')` from "organic-use opportunity" in `prompts/development.md` to **required step** at session-open.
- Promote substrate availability at session-open from optional-aside to **required precondition**: if substrate unavailable, session opens with explicit honest-limit + degradation per `multi-agent-deliberation.md` v4 §Graceful Degradation.
- **Load MCP retrieval tools by default** in the harness configuration (no `ToolSearch` step required). This is a `.mcp.json` / harness-config change; not a spec change.
- Add `tools/validate.sh` check (call it check 29 candidate) that probes whether the current session's `00-assessment.md` or `03-close.md` cites substrate-call evidence (e.g., a `forward_references` invocation result or `resolve_id` lookup recorded in honest-limits or read-discipline-coverage section). Without such evidence, emit WARN (or FAIL after grace period).
- Implement the `tools/validate.sh` check 26 substrate-aware branch (currently aspirational; needs to actually call `mcp__selvedge-retrieval__search` when available + degrade to grep-fallback when not). This is the canonical demonstration that the engine's own tool exercises the substrate it claims to prefer.

**Direction 2 (group ii): Implement (z6) harness-telemetry digest substantively.**

- EF-059's (z6) scope as filed: failed-tool-call detection + repeated-Read pattern detection + reviewer-cost measurement (per EF-067 cross-linkage).
- **Extend (z6) scope to include orchestrator-side read-discipline telemetry**: `substrate_calls_at_session_open` + `files_read_at_session_open` + `decision_claims_with_evidence_pointers` (e.g., decision rationale citing specific spec section numbers + ledger row IDs + minority warrants invoked). Make orchestrator read-behavior observable across sessions.
- The digest record itself becomes Tier 2.5 reviewer input per `validation-approach.md` v7 §Tier 2.5 audit shape (currently lists harness-telemetry digest as required-when-available; "when available" should become "always available, always read"). Reviewer audits orchestrator read-behavior alongside close-narrative claims.

**Joint-scope cross-linkage with EF-059 + EF-067 + EF-068 (this record)**:

The S068 D-251 joint-scope decision pre-ratified S069+ Path-AS Shape-1 phase-1 synthesis on EF-059 + EF-067. **EF-068 (this record) extends that joint-scope** to a three-record bundle: the design-space at S069+ surveys (z6) digest scope × EF-067 reviewer self-report directions × EF-068 orchestrator-side read-discipline telemetry. All three concerns share the harness-side-enforcement structural surface.

Phase-2 MAD at S069+1 deliberates direction. Phase-3 implementation arc per phase-2 MAD outcome.

**Minimum-viable-response candidate (for design-space deliberation)**:

If the joint-scope MAD prefers minimum-viable-response per S062 §10.4-M16 P2 precedent: the smallest-scope change that addresses the laundering surface is:

- (a) Load MCP tools by default (.mcp.json / harness-config change; immediate; no spec change).
- (b) Add `prompts/development.md` minor amendment promoting `forward_references` to required step.
- (c) Add `tools/validate.sh` check that probes for substrate-call evidence in close-narrative; WARN-only initially.

Larger-scope candidates (full (z6) digest implementation; full check-29-equivalent harness-side enforcement) are reserved for sustained-pattern-evidence per minimum-viable-precedent discipline.

## Evidence

- S067 close §6 WX-62-1 5-field block: cumulative pattern S063+S064+S067 with reviewer-cost as reviewer-self-report (flagged at EF-067).
- S068 post-close discussion: orchestrator confirmed zero `mcp__selvedge-retrieval__*` calls across S067 + S068.
- `tools/validate.sh:1224-1320` check 26 implementation: substrate-aware branch documented in inline comment; only grep-fallback executed in code.
- `prompts/development.md` §How to operate paragraph: `forward_references('target')` framed as "useful diagnostic" / "additive to the contract minimum"; not required.
- S054 D-187 + S055/S056/S057 organic-use clean-propagation tracking; subsequent sessions n=0 use.
- `engine-feedback/inbox/EF-059-harness-telemetry-feed-for-tier-2-reviewer.md` activation preconditions all satisfied at S067/S068.
- `engine-feedback/inbox/EF-067-reviewer-wall-clock-self-report-unreliable.md` reviewer self-report parallel.
- S058 records-substrate phase-1 + S062 EF-058-tier-2-validation arc + v7 §Principled Asymmetry articulation: 21-session delay between problem-articulation (S058 close honest-limit chain naming) and root-cause-fix.

## Application-Scope Disposition

**Self-development workspace** (this workspace). The observation surfaced post-S068 close in operator-surfaced discussion. S068 close is committed and immutable per D-017; this EF record is the formal capture for S069+ scope.

S069+ joint-scope expansion: bundled with EF-067 + EF-059 in S068 D-251 pre-ratified design-space. **EF-068 extends the bundle** to three records, all addressing harness-side-enforcement of cross-session-state-claim discipline.

The S069+ Path-AS Shape-1 design-space.md should survey:
- EF-067 directions A/B/C (drop self-report fields / subsume into (z6) / honest-limit-only).
- EF-059 (z6) scope: failed-tool-call detection + repeated-Read + fallback-event + anomalous-pattern + reviewer-cost.
- EF-068 directions: load MCP by default / promote `forward_references` to required / check 29 candidate / extend (z6) scope to orchestrator read-telemetry / implement check 26 substrate-aware branch.
- Q1-Q10 design questions including: harness-side-enforcement vs spec-side-encouragement balance; minimum-viable per S062 §10.4-M16 P2 precedent vs full architectural shift; load-by-default vs preserve-deferred-tools-friction; (z6) scope breadth.
- Pre-ratification of phase-2 MAD per S057 D-196 precedent.

**Operator-audit cadence note**: this EF surfaced via operator-discretionary post-close audit per `validation-approach.md` v7 §Bootstrap-Paradox Layered Handling Layer 6.2. **Third-of-record operator-audit-catches-what-in-session-discipline-missed event** at S068 post-close (S063+S064 first-of-record arc; S067+S068 second-of-record EF-067; S068+S069 third-of-record EF-068). The pattern is reifying — operator audit consistently surfaces concrete substantive concerns that in-session orchestrator + (γ) reviewer + Tier 2 self-assessment do not catch. This itself is evidence that the engine's in-session discipline mechanisms are bounded and that operator-audit is currently the load-bearing cross-check; harness-side enforcement (EF-068's direction) would shift some of that load from operator to engine.
