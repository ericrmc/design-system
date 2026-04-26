---
feedback_ref: engine-feedback/inbox/EF-068-substrate-load-bearing-and-harness-telemetry.md
triage_session: 069
status: deferred
classification: substantive-arc-via-cross-linkage
---

# Triage — EF-068 Substrate Load-Bearing and Harness Telemetry

## Triage classification

**Classification: substantive-arc-via-cross-linkage**.

EF-068-substrate-load-bearing admits two coupled directions (groups i + ii per intake §Suggested Change). Both are substantive in scope:

- **Direction 1 (group i): make substrate use load-bearing at session-open**.
  - Promote `forward_references('S<NNN>')` from "organic-use opportunity" in `prompts/development.md` to **required step** at session-open.
  - Promote substrate availability at session-open from optional-aside to **required precondition** (with explicit honest-limit + degradation per `multi-agent-deliberation.md` v4 §Graceful Degradation if unavailable).
  - **Load MCP retrieval tools by default** in harness configuration (`.mcp.json` / harness-config change; not a spec change).
  - Add `tools/validate.sh` check (candidate name "check 29") probing for substrate-call evidence in close-narrative or 00-assessment; WARN-only initially.
  - Implement `tools/validate.sh` check 26 substrate-aware branch (currently aspirational; needs to actually call `mcp__selvedge-retrieval__search` when available + degrade to grep-fallback when not).

- **Direction 2 (group ii): implement (z6) harness-telemetry digest substantively**.
  - **Extend EF-059 (z6) digest scope** to include orchestrator-side read-discipline telemetry: `substrate_calls_at_session_open` + `files_read_at_session_open` + `decision_claims_with_evidence_pointers`.
  - Make digest record Tier 2.5 reviewer input always-available-always-read per `validation-approach.md` v7 §Tier 2.5 audit shape (currently lists harness-telemetry digest as required-when-available; intake recommends "when available" → "always available, always read").

The Direction-1-vs-2 choice and the within-direction sub-choices (e.g., Direction 1 (a) load-by-default-only vs (b) load-by-default + promote to required vs (c) full check 29 + check 26 substrate-aware activation) warrant substantive deliberation per `multi-agent-deliberation.md` v4 §When Multi-Agent Deliberation Is Required clause 3 (the question is one on which reasonable practitioners could genuinely disagree — multiple plausible positions namable before deliberation). Cross-linkage with EF-067 + EF-059 makes the design-space joint-scope: Direction 2 is structurally subsumed in EF-059 (z6) digest extended scope; Direction 1 is partially independent of EF-059 implementation (load-by-default + promote-to-required can ship without (z6) digest implementation).

**Per S068 D-251 cross-linkage joint-scope precedent + S061 Path-AS Shape-1 phase-1 synthesis precedent**: substantive-arc-class with cross-linkage is appropriately resolved through Path-AS Shape-1 phase-1 synthesis (design-space.md surveying Direction 1 sub-options × Direction 2 (z6) extended scope × cross-linkage with EF-067 directions A/B/C; Q1-Q10 design questions; pre-ratification of phase-2 MAD).

## Triage disposition

**Disposition**: substantive-arc-deferred-via-cross-linkage to **joint-scope with EF-067 + EF-059** at S070+ Path-AS Shape-1 phase-1 synthesis per **D-256 cross-linkage joint-scope expansion** (S068 D-251 expanded from two-record EF-067 + EF-059 to **three-record EF-067 + EF-059 + EF-068-substrate-load-bearing**).

**Resolution path forecast**:
- **S070+ Path-AS Shape-1**: phase-1 synthesis on three-record joint-scope (EF-067 + EF-059 + EF-068-substrate-load-bearing). Produces `provenance/<NNN-session>/design-space.md` (per S057 + S061 + S068-D-251 precedent) surveying:
  - **EF-059 (z6) digest scope** (primary): failed-tool-call detection; repeated-Read pattern detection; reviewer-cost measurement (per EF-067 cross-linkage); fallback-event recording; anomalous-pattern detection; **+ EF-068 extended scope: orchestrator-side read-discipline telemetry** (substrate_calls_at_session_open + files_read_at_session_open + decision_claims_with_evidence_pointers).
  - **EF-067 Directions** A (drop fields) / B (subsume into (z6) extended scope) / C (honest-limit-only).
  - **EF-068 Direction 1**: load MCP by default / promote `forward_references` to required / check 29 candidate / implement check 26 substrate-aware branch.
  - **EF-068 Direction 2**: extend (z6) scope to orchestrator read-telemetry / make digest always-available-always-read.
  - **Cross-product implementation candidates**: harness-side instrumentation hooks; transcript-parsing post-hoc digest; structured-log-emission protocol; tool-invocation-counter API; check 29 evidence-probe; check 26 substrate-aware activation.
  - **Q1-Q10 design questions** including: harness-side-enforcement vs spec-side-encouragement balance; minimum-viable per S062 §10.4-M16 P2 precedent vs full architectural shift; load-by-default vs preserve-deferred-tools-friction; (z6) scope breadth (failed-tool-call only vs orchestrator-side telemetry inclusion).
  - **Pre-ratification of phase-2 MAD** with 4-perspective two-family lineup per S058 + S062 + S068-D-251 precedent.
- **S070+1 Path-AS-MAD-execution**: 4-perspective two-family MAD per S058 + S062 lineup precedent. Synthesizes adoption direction.
- **S070+2 Path L (single-orchestrator phase-3 adoption)** or same-session-bounded adoption per phase-2 MAD outcome per S062 D-220 + S058 D-199 precedent.

The arc shape is analogous to EF-058-tier-2-validation arc (S061 Shape-1 → S062 MAD-execution → S063 phase-3) and the S068 D-251 pre-ratified two-record arc (now expanded to three-record at D-256).

**Alternative dispositions considered and rejected**:

1. **Same-session-resolution adopting Direction 1 (a) at S069 (load MCP by default; minimum-viable scope)**: rejected at triage scope. Direction 1 (a) is partially a `.mcp.json` / harness-config change (not engine-definition spec change), but Direction 1 (b) "promote `forward_references` to required step" is a substantive revision to `prompts/development.md` § How to operate (engine-definition file class per `engine-manifest.md` §3); engine-version increment to thirteenth-engine-version. Single-orchestrator implementation of bounded Direction 1 (a) only without first surveying Direction-1-vs-2 alternatives + cross-linkage with EF-067/EF-059 in a phase-1 synthesis (per Path-AS Shape-1 precedent) would skip the workspace's design-space-then-decide discipline. **Path L could be adopted at S070+ post-Shape-1 if MAD synthesises Direction 1 (a) as minimum-viable-response per S062 §10.4-M16 P2 precedent**; the triage classification preserves that option without committing to it.

2. **Separate-scope from EF-067 + EF-059 (standalone EF-068-substrate-load-bearing arc)**: rejected per D-256 cross-linkage joint-scope expansion decision (see §Cross-linkage with EF-067 + EF-059 below + D-256). The intake itself frames Direction 2 as "extend EF-059 (z6) digest scope" — structurally subsuming. Direction 1 is partially independent but operationally interacts with (z6) digest via "decision_claims_with_evidence_pointers" telemetry; separate-scope risks downstream rework.

3. **Reject EF-068-substrate-load-bearing (no action warranted)**: rejected because operator surfaced concrete substantive concern (per Layer 6.2 cadence audit at S068 post-close); the laundering surface is real (substrate non-use at S067 + S068 + **S069 session-open per orchestrator-self-recorded honest-limit** — orchestrator-self-report-as-evidence parallel to EF-067); workspace has discipline for addressing operator-surfaced concerns; the third-of-record operator-audit-catches-what-in-session-discipline-missed event is itself evidence the engine's in-session mechanisms are bounded.

4. **Defer EF-068-substrate-load-bearing indefinitely (until additional substrate-non-use instances accumulate)**: rejected because EF-068-substrate-load-bearing is the n=4 concrete instance of the orchestrator-side discipline-gap pattern (S067+S068+**S069** orchestrator substrate non-use, on top of S054 D-187 organic-use clean-propagation tracking n=4 + n=1 + n=0); EF-059's activation precondition (c) is already extended per EF-067 strengthening; the evidence base is sufficient. Indefinite deferral would not advance the engine forward and would compound the cadence-of-passivity the intake critiques.

## Cross-linkage with EF-067 + EF-059

EF-068-substrate-load-bearing extends the S068 D-251 two-record joint-scope (EF-067 + EF-059) to a **three-record bundle** per D-256.

**Structural cross-linkages**:

- **EF-068 Direction 2 (extend (z6) scope) is subsumed in EF-059 (z6) digest extended scope**. The digest's primary scope (failed-tool-call + repeated-Read + reviewer-cost per EF-067) extends to orchestrator-side telemetry (substrate_calls + files_read + decision_claims_with_evidence_pointers). The phase-2 MAD addresses the extended scope as a single design choice.

- **EF-068 Direction 1 (load MCP by default; promote `forward_references` to required) is partially independent** of EF-059 (z6) implementation. Direction 1 (a) (load MCP by default) ships immediately at harness-config change scope; Direction 1 (b) (promote-to-required) ships at `prompts/development.md` minor amendment scope. Both are smaller-arc than EF-059 (z6) digest implementation. The phase-2 MAD evaluates whether to bundle them with (z6) implementation or ship as separate phase-3 implementation.

- **EF-067 cross-linkage: harness-side measurement subsumes both reviewer-cost-self-report (EF-067 Direction B) and orchestrator-side substrate-call-self-report (EF-068 Direction 2)**. The (z6) digest's harness-side measurement principle applies symmetrically to both reviewer and orchestrator; the design-space evaluates whether the unification is operationally significant or whether the surfaces should be addressed independently.

**Joint-scope rationale at D-256 (three-record)**:

1. One design-space surveys all three records' decisions simultaneously.
2. One MAD addresses all three questions per S058 + S062 + S068-D-251 precedent extension.
3. The (z6) digest scope is the structural unifier; EF-067 + EF-068-substrate-load-bearing both extend or are subsumed by it.
4. Implementation arc is unified at phase-3.
5. Engine-conventional pattern for cross-linked substantive-arc records (S058 EF-055 → single arc; S062 EF-058-tier-2-validation → multi-session arc; S068 D-251 → two-record bundle; S069 D-256 → three-record bundle expansion).

**Separate-scope rationale considered and rejected**:

- EF-068 Direction 1 admits minimum-viable-only paths (a) and (b) which don't require EF-059 (z6) implementation. Adopting Direction 1 (a) at S070+ Path L without first surveying Direction-1-vs-2 alternatives + cross-linkage in design-space would skip workspace's discipline.
- Separate-scope risks downstream rework when (z6) digest implementation later extends scope to include orchestrator-side telemetry differently than EF-068 Direction 2 framed it.

**Decision per D-256**: joint-scope adopted; three-record bundle.

## Sequencing relative to EF-068-read-write-rebalance sibling

EF-068-read-write-rebalance is **NOT included in the three-record bundle** at S069 triage per the sibling intake's explicit "blocked-on-sibling" framing + recommended S070++ defer (after this record's harness-side enforcement is operational). Operator did not surface preference for four-record bundle at S069 open. Per EF-068-read-write-rebalance triage record (D-255): separate-scope at S070++ with operator-discretionary four-record bundle reopen preserved.

If at S070+ Path-AS Shape-1 the design-space surfaces strong sequence-coupling between this record and the sibling, the design-space may surface a "bundle-vs-defer" question for MAD deliberation per the sibling intake's "phase-1 design-space at S070+ could include explicit 'bundle-vs-defer' question" framing. The four-record bundle remains operationally available via design-space-question route.

## Forward-recommendation

S070+ Path-AS Shape-1 phase-1 synthesis on three-record joint-scope (EF-067 + EF-059 + EF-068-substrate-load-bearing) per D-256. Pre-ratify phase-2 MAD at S070+1 (or S070 close if operator surfaces preference for combined-session shape).

EF-068-substrate-load-bearing triage record will be updated to `status: resolved` when phase-3 implementation lands (per resolution chain analogous to S058 D-199 → S063 D-228 EF-058-tier-2-validation resolved-via-multi-session-arc).

## Notes

The intake explicitly frames the structural concern as **engine passivity with laundering and maintenance**. The orchestrator's S069 session-open honest-limit recording (substrate not invoked at session-open; Read/Grep/Bash used throughout) is the **n=4 concrete instance** of the orchestrator-side substrate non-use pattern (S067 + S068 + **S069** orchestrator-self-reported substrate non-use). This honest-limit recording is the load-bearing pre-evidence for the substantive-arc at S070+ Path-AS Shape-1 — the design-space at S070+ has the n=4 pattern as concrete data; the MAD at S070+1 deliberates direction with that evidence in hand.

The recursive tension — S069 enacts the very cadence (Path T → Path-AS Shape-1 → MAD → Path L) the intake critiques — is noted explicitly in S069 00-assessment §7 honest-limit 5. Substantive resolution of that tension is the joint-scope MAD's work at S070+; triage scope at S069 is the engine-conventional gate.
