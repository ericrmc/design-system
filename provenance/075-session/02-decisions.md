---
session: 075
title: Session 075 decisions — Path-AS phase-3.1 implementation per (γ-6) staged hybrid + engine-v14 → engine-v15 substantive ratification
date: 2026-04-26
status: complete
---

# Decisions — Session 075

Seven decisions: D-293 Path-AS phase-3.1 implementation per (γ-6) staged hybrid ratified + D-294 validation-approach.md v8 → v9 substantive (SCD-3 schema codified + audit-shape extension + reviewer-prompt-template v3 minimum-viable extension + Codex-S074-F4 close) + D-295 tools/validate.sh substantive (check 26 substrate-aware branch CHKD-2 + check 27 §1-§8 + tripartite §3 enforcement) + D-296 new engine-adjacent tooling (tools/digest_emitter.py + tools/digest_reconstructor.py + .claude/settings.json) + D-297 workspace-structure.md v9 minor (S074-stale-references-cleanup window shifts) + D-298 engine-v14 → engine-v15 ratified per substantive bump + D-299 housekeeping `[none]` (15 sub-sections; forty-seventh-consecutive).

## D-293: Path-AS phase-3.1 implementation per (γ-6) staged hybrid ratified

**Triggers met:** [d016_2, d016_3]

**Triggers rationale:** d016_2 fires per substantive cross-spec implementation execution per (γ-6) per-direction dispositions D-276 through D-282 (capture mechanism CM1+CM3, schema SCD-3, check 26 substrate-aware branch, reviewer-prompt-template v3, engine-v cadence substantive). d016_3 fires per the implementation execution requiring genuine cross-perspective scrutiny at close: Tier 2.5 (γ) reviewer audit per Layer 2 trigger (a)+(b)+(d) multiple fires; codex preferred per v8 family-overlap-permitted rule + operator-preference at S074.

**Non-Claude participation:** required per d023_3 (substantive revision to validation-approach.md touching semantic Tier 2 + §Tier 2.5 audit-shape extension); satisfied per Tier 2.5 codex reviewer audit at S075 close per `provenance/075-session/04-tier-2-audit.md`.

**Single-agent reason:** S075 is single-orchestrator implementation execution per S074 close §7 next-session-recommendation + S073 D-282 pre-ratification (Path-AS phase-3.1 implementation per (γ-6) staged hybrid). The S073 phase-2 4-perspective two-family MAD (P1+P2 Claude + P3+P4 codex) already adopted (γ-6) per D-275 + per-direction dispositions D-276 through D-282. Re-deliberating those per-direction dispositions at implementation execution would violate §10.4-M35 P3 z10 + P4 z-laundering-2 staging-must-be-per-direction reframe substantively adopted at S073 D-275. Cross-perspective scrutiny is satisfied per Tier 2.5 (γ) codex reviewer audit at S075 close per v9 family-overlap-permitted-with-disclosure rule + operator-preference at S074 carried forward. retry_in_session: N/A (single-orchestrator scope is structurally appropriate; no retry warranted).

**Decision:** Path-AS phase-3.1 implementation per (γ-6) staged hybrid ratified at S075 per S074 close §7 next-session-recommendation recovering S073 D-282 pre-ratification per S074 D-286 operator-directive supersession-then-resumption discipline. Single-orchestrator implementation execution under Tier 2.5 reviewer-audit discipline; no new MAD per S073 phase-2 MAD already adopting (γ-6) per D-275 + per-direction dispositions D-276 through D-282. Pattern: Path-AS phase-3-implementation reified at n=2 (S063 first-instance Path-L single-orchestrator phase-3 adoption per S062 D-221 + S075 second-instance under v8 family-overlap-permitted reviewer rule).

**Path-justification per (z12):** Path-AS phase-3.1 implementation is the structurally-correct response per S074 close §7 next-session-recommendation + S073 D-282 pre-ratification + (γ-6) per-direction disposition discipline. Five non-Path-AS alternatives surfaced and rejected at 00-assessment §1: Path A (Watch) per active substantive arc, Path L (single-orchestrator without reviewer audit) per Layer 2 trigger fires, Path PD per no operator surface, Path T per inbox 0 new, Path AS-MAD-execution per (γ-6) already-adopted at S073 (new MAD would re-deliberate per-direction shape, violating §10.4-M35 staging-must-be-per-direction).

**Rejected alternatives:** Path AS-MAD-execution — REJECTED per §10.4-M35 P3 z10 + P4 z-laundering-2 staging-must-be-per-direction reframe substantive adoption at S073 D-275 (re-deliberating per-direction dispositions at implementation would violate per-direction discipline). Path L (single-orchestrator without reviewer audit) — REJECTED per Layer 2 trigger (a)+(b)+(d) multiple fires requiring Tier 2.5 (γ) reviewer at close. Path A (Watch) — REJECTED per (z12) 5-condition test (active substantive-class arc engagement). Path PD — NOT SURFACED at S075 open. Path T — SCOPE UNAVAILABLE (engine-feedback inbox 0 new at S075 open).

## D-294: validation-approach.md v8 → v9 substantive

**Triggers met:** [d016_2, d016_3]

**Triggers rationale:** d016_2 fires per substantive revision to engine-definition spec (validation-approach.md v8 → v9: SCD-3 harness-telemetry-digest schema codified in §(z6) replacing v7+v8 DEFERRED-pointer language; §Tier 2.5 audit-shape extended with reviewer-prompt-template v3 minimum-viable extension; check 27 enforcement extended to require all §1-§8 + tripartite §3a/§3b/§3c sub-sections closing Codex-S074 audit Finding F4 mechanism gap; engine-definition substantive per OI-002 substantive-vs-minor heuristic). d016_3 fires per spec revision requiring cross-perspective scrutiny at close per Tier 2.5 (γ) reviewer audit.

**Non-Claude participation:** required per d023_3 (engine-definition spec substantive revision touching semantic Tier 2 + §Tier 2.5 audit-shape); satisfied per S073 phase-2 4-perspective two-family MAD upstream of this implementation (P1+P2 Claude + P3+P4 codex synthesis adopted (γ-6) per D-275; S075 implements that synthesis) + S075 close codex Tier 2.5 reviewer audit.

**Single-agent reason:** D-294 implements the S073 phase-2 MAD synthesis (P1+P2 Claude + P3+P4 codex cross-family weighted convergence adopted (γ-6) per D-275 + per-direction dispositions D-276 through D-282). v9 §(z6) substantive scope is direct codification of those S073 decisions; there are no new degrees of freedom to deliberate at implementation. Cross-perspective scrutiny is satisfied per Tier 2.5 (γ) codex reviewer audit at S075 close. retry_in_session: N/A.

**Decision:** validation-approach.md v8 → v9 substantive revision adopted. Specific changes:

- **§(z6) Harness-Telemetry Digest section**: replaces v7+v8 DEFERRED-pointer language with concrete SCD-3 schema spec — capture-adapter metadata fields (`capture_adapter`, `capture_adapter_version`, `capture_capabilities`, `unobserved_fields`) + per-section field-level authority rules per §10.4-M34 P4 z-laundering-1 reframe (each record carries own `producer_kind` + `authority_level`; agent-declared cannot promote to harness-measured via digest shape alone). Names CM1 (`tools/digest_emitter.py` Claude Code PostToolUse hook) + CM3 (`tools/digest_reconstructor.py` post-hoc bridge/comparator) + CM2 (deferred portability end-state) + CM4 (explicitly excluded). Names RAD-3 bridged transition (D2.1 end-state, D2.2 default during S075-S076), REVD-2 quarantine semantics, CHKD-2 evidence-consuming validator-as-evidence-consumer per §10.4-M33. Names reviewer-prompt-template v3 minimum-viable extension (digest-aware reviewer instructions + per-record producer_kind/authority_level distinction + REVD-2 quarantine application + capture-adapter metadata coherence check). Names engine-v cadence summary (S073 minor → S074 substantive v8 → S075 substantive v9 → S076 minor extensions).

- **§Tier 2.5 audit-shape extension**: full §1-§8 + tripartite §3a/§3b/§3c sub-section presence required (closes Codex-S074 audit Finding F4 mechanism-adequacy gap deferred to S075+ per S074 close §7); reviewer MUST inspect digest when present + flag absent-digest as honest-limit; reviewer-prompt-template v3 candidate at S075 with (z7) lock-in-after-n=2 counter reset to 0.

- **Tier 1 table check 26 row**: extended to name CHKD-2 substrate-aware branch (digest-when-present consumed; grep-fallback when both digest and 00-assessment substrate-evidence absent per §Graceful Degradation). Tier 1 table check 27 row: extended to require all §1-§8 + tripartite §3 + scope-coverage table + bootstrap label + google-provider exclusion.

- **(z7) Reviewer-prompt-template versioning + lock-in-after-n=2**: extended to record v3 candidate at S075 + lock-in counter reset to 0 + n≥2 forecast for v3 lock-in at S076-S077 successful applications.

- **Frontmatter**: added `harness_telemetry_digest_available: <true | false>` field for reviewer audit frontmatter at S075+.

v8 preserved as `validation-approach-v8.md` `status: superseded` + `superseded-by: validation-approach.md (v9)` + `superseded-in-session: 075`.

**Engine-definition substantive revision** per OI-002 (full §(z6) section rewrite + §Tier 2.5 audit-shape extension + new check 26 sub-clause + frontmatter extension; not minor). Engine-v14 → engine-v15 ratified per D-298 substantive bump.

**Rejected alternatives:** SCD-2-first-tranche (substrate_calls extension only; full SCD-3 deferred to S076) — REJECTED per S073 D-277 SCD-3-target framing + the SCD-3 schema spec being bounded enough at S075 implementation scope (no need to defer full schema to S076; phase-3.2 at S076 handles minor extensions per RAD-3 D2.1 candidate + REVD-3 candidate, not SCD scope). Defer audit-shape extension to S076 — REJECTED per S074 close §7 specifically calling out F4 close at S075+ scope evaluation.

## D-295: tools/validate.sh substantive update

**Triggers met:** [d016_2]

**Triggers rationale:** d016_2 fires per substantive update to engine-definition tool (tools/validate.sh: new check 26 substrate-aware branch CHKD-2 evidence-consuming + check 27 enforcement extension to require all §1-§8 + tripartite §3a/§3b/§3c sub-sections; engine-definition tool substantive update per OI-002 substantive-vs-minor heuristic per new sub-clauses + new branch).

**Non-Claude participation:** satisfied per D-293 + D-294 upstream substantive deliberation at S073 phase-2 MAD; S075 implementation of D-275 + per-direction dispositions.

**Single-agent reason:** D-295 is mechanical implementation of S073 D-280 (CHKD-2 substrate-aware branch) + S075 D-294 (check 27 audit-shape extension closing Codex-S074-F4 deferred to S075+ scope per S074 close §7). Both decisions upstream were cross-family-deliberated (S073 phase-2 MAD + S074 codex reviewer audit). validate.sh substantive update is the validator-side codification of those upstream substantive decisions; no new degrees of freedom warrant fresh MAD. Cross-perspective scrutiny is satisfied per Tier 2.5 (γ) codex reviewer audit at S075 close (which itself runs validate.sh per check 26 substrate-aware branch + check 27 §1-§8 enforcement). retry_in_session: N/A.

**Decision:** tools/validate.sh substantive update adopted. Specific changes:

- **Check 26 substrate-aware branch**: probes for `provenance/<current-session>/harness-telemetry-digest.yaml` presence; when present, parses substrate_calls record count via in-memory awk + emits substrate-aware: digest consumed message; proceeds with in-memory grep-based cluster detection (unchanged from S067 D-244 VD-002 closure). When digest absent, in-memory grep-fallback runs unchanged per `multi-agent-deliberation.md` v4 §Graceful Degradation. Validator does NOT call MCP at runtime per §10.4-M33 P3 z9 validator-as-evidence-consumer reframe.

- **Check 27 §1-§8 + tripartite §3 enforcement**: full required-section presence enforced (§1, §2, §3, §4, §5, §6, §7, §8 + tripartite §3a, §3b, §3c). Pre-v9, check 27 enforced only §2 + §7 + scope-coverage + bootstrap-label + google-provider-exclusion; the spec required §1+§3+§4+§5+§6+§8 too. v9 closes that mechanism-adequacy gap per Codex-S074 audit Finding F4.

- **Bootstrap-limited-confidence label heuristic extended**: trigger pattern extended from `D-233|D-234|engine-v12|Tier 2.5 revision` to also include `D-288|D-291|engine-v1[2-9]|engine-v[2-9][0-9]|reviewer-prompt-template v[3-9]|audit-shape extension` to catch S075 Tier 2.5 mechanism revisions.

- **Pass-message updated** to v9 audit shape reference + Codex-S074-F4 close marker.

**Engine-definition substantive update** per OI-002 (new substrate-aware branch + extended required-section enforcement; not minor). Engine-v14 → engine-v15 ratified per D-298 substantive bump.

**Rejected alternatives:** WARN-only check 27 §1-§8 enforcement (v9 transition gentleness) — REJECTED per S074 close §7 specifically calling out F4 close + check 27 already at FAIL severity for §2/§7 (consistent severity for §1-§8). Defer F4 close to S076 — REJECTED per S074 close §7 explicitly placing F4 in S075+ scope evaluation per (z7) explicit-deliberation-surface requirement satisfied at S075 reviewer-prompt-template v3 candidate adoption.

## D-296: New engine-adjacent tooling + harness-config

**Triggers met:** [d016_2]

**Triggers rationale:** d016_2 fires per substantive new engine-adjacent tooling for (γ-6) phase-3.1 implementation (CM1 + CM3 capture-adapter implementations per S073 D-276 + harness-config edit per CM1 hook deployment).

**Non-Claude participation:** satisfied per D-293 + D-294 upstream substantive deliberation at S073 phase-2 MAD.

**Single-agent reason:** D-296 is mechanical implementation of S073 D-276 (CM1 first capture-adapter via Claude Code hooks + CM3 secondary bridge/comparator via post-hoc transcript reconstruction). Capture-mechanism selection was cross-family-deliberated at S073 phase-2 MAD (P1+P2 Claude + P3+P4 codex on CM1+CM3 stack per (γ-6) per-direction disposition discipline). New tooling implements the adopted CM1+CM3 mechanism; no fresh MAD warranted because the per-direction disposition is settled. Per §10.4-M32 P3 z8 portable-capture-adapter-contract reframe substantive adoption at S073: any capture-adapter producing SCD-3-conformant records is acceptable; the contract is the schema (codified at v9 §(z6) per D-294), not the implementation. retry_in_session: N/A.

**Decision:** New engine-adjacent files adopted at S075 phase-3.1 implementation:

- **`tools/digest_emitter.py`** (CM1 capture-adapter): Python script invoked by Claude Code hooks PostToolUse. Reads JSON event from stdin; identifies current session via most-recent provenance/<NNN-session>/ directory; appends substrate-call records (mcp__selvedge-retrieval__* calls) to `substrate_calls:` section, other tool calls to `tool_calls:` section. Emits SCD-3-conformant records with `producer_kind: harness-measured` + `authority_level: primary`. Idempotent (file-append). Failure-mode: any exception silently caught + stderr warning + exit 0 per validator-as-evidence-consumer discipline (digest is evidence-when-present, not orchestrator precondition).

- **`tools/digest_reconstructor.py`** (CM3 post-hoc bridge/comparator): Python script that reconstructs SCD-3 digest records from session provenance — 00-assessment.md frontmatter (substrate_session_open + substrate_evidence) + prose mentions of substrate-tool calls in 00-assessment / 02-decisions / 03-close. Emits records with `producer_kind: post-hoc-reconstructed` + `authority_level: secondary`. When CM1 digest already exists at primary path, writes comparator at `harness-telemetry-digest-cm3.yaml` (sibling); otherwise writes primary digest path.

- **`.claude/settings.json`** (harness-config; not engine-definition per .mcp.json precedent at S071 D-264): PostToolUse hook configuration invoking `uv run $CLAUDE_PROJECT_DIR/tools/digest_emitter.py` with 5-second timeout. PreToolUse NOT configured — would create duplicate records since PostToolUse event has tool_response field for status determination.

**Engine-adjacent classification**: per `engine-manifest.md` §3 boundary rule, new tooling files NOT added to §3 engine-definition file set (consistent with `tools/build_retrieval_index.py` + `tools/retrieval_server.py` engine-adjacent classification at S050 D-172). The schema (codified in `validation-approach.md` v9 §(z6)) is engine-definition; the reference implementations are engine-adjacent. Per §10.4-M32 P3 z8 portable-capture-adapter-contract reframe substantive adoption at S073 D-275: any capture-adapter producing SCD-3-conformant records is acceptable; the contract is the schema, not the implementation.

**Rejected alternatives:** Claude Code PreToolUse + PostToolUse paired hooks (full pair) — REJECTED per duplicate-record risk (PreToolUse fires before tool result is available; PostToolUse alone captures both intent + outcome with status determination). Inline-deps in shebang (PEP 723) — ADOPTED per existing tools/retrieval_server.py + tools/build_retrieval_index.py precedent at S059 D-211 uv-migration. External-wrapper CM2 implementation — REJECTED per S073 D-276 (CM2 deferred to post-S076 review per VD-003 gating).

## D-297: workspace-structure.md v9 minor amendment (S074-stale-references cleanup)

**Triggers met:** [none]

**Triggers rationale:** Per OI-002 substantive-vs-minor heuristic per stale-text cleanup (Codex-S074-F2-style preventive cleanup): §10.4-M31 + §10.4-M33 + §10.4-M34 + §10.4-M35 reopen-warrant text references "S074 phase-3" / "S074-S075" / "S074-S076" / "S074-S077+" / "S074+" implementation timing windows that are now stale per S074 D-286 supersession-then-resumption (phase-3.1 actually at S075, not S074). Minor amendment cleans stale window references to S075-shifted windows (S075-S076, S075-S077+, S075+). v9 retained per OI-002 minor classification (no structural change to mechanism; no new minorities; pure-textual cleanup).

**Non-Claude participation:** N/A per [none] triggers (procedural cleanup).

**Decision:** workspace-structure.md v9 minor amendment adopted. Updates:

- §10.4-M31 reopen warrant (a): "(γ-6) implementation cost at S074-S075 exceeds (γ-3) baseline by >50%" → "(γ-6) cost at S075-S076 exceeds (γ-3) baseline by >50%". Mirrored-in reference: `validation-approach.md` v7 §10 → v9 §10.
- §10.4-M33 reopen warrant (b): "check 26 substrate-aware at S074 introduces live-MCP-runtime-dependency breaking CI" → "check 26 substrate-aware at S075 introduces live-MCP-runtime-dependency breaking CI". Mirrored-in reference: v7 → v9.
- §10.4-M34 reopen warrant (b): "digest at S074-S077+ contains mixed-origin fields without per-field annotations" → "digest at S075-S077+ contains mixed-origin fields without per-field annotations". Mirrored-in reference: v7 → v9.
- §10.4-M35 reopen warrants (a)+(d): "γ phase-3 stage at S074-S076 collapses per-direction" → "γ stage at S075-S076 collapses per-direction" + "reopen-warrant activation drifts into implementation-bundling at S074+" → "activation drifts into implementation-bundling at S075+". Compressed for word budget. Mirrored-in reference: v7 → v9.

Net word-count change: ~-25 words (compressions outweigh shifts). Final word count post-amendment: 7994 / 8000 hard ceiling.

**Minor classification per OI-002**: pure-textual cleanup of stale window references; no structural change to mechanism; no new minorities preserved; v9 retained.

**Rejected alternatives:** No update (preserve stale window references) — REJECTED per Codex-S074-F2 stale-text-cluster pattern (a finding at S074 was specifically about stale text; preventing recurrence at S075 is hygiene). Substantive v9 → v10 (treat as substantive) — REJECTED per OI-002 minor classification (window-reference shifts are pure-textual; no semantic change to reopen-warrant logic).

## D-298: Engine-v14 → engine-v15 ratified per substantive bump

**Triggers met:** [none]

**Triggers rationale:** Per `engine-manifest.md` §5 versioning discipline + S063 + S071 + S074 substantive-bump precedent: engine-version increment is procedural-recording per substantive revisions to engine-definition files in this session per D-294 + D-295 + D-297 (substantive validation-approach.md v8 → v9 + substantive tools/validate.sh + minor workspace-structure.md v9). Engine-v15 ratification is the procedural artefact recording the substantive scope.

**Non-Claude participation:** N/A per [none] triggers (procedural-recording).

**Decision:** Engine-v15 ratified at S075 close per substantive bump. Engine-manifest.md updates:

- §2 Current engine version: `engine-v14` → `engine-v15` (established Session 075 per D-298).
- §3 Header: "Engine-definition files at `engine-v14`" → "Engine-definition files at `engine-v15`". File set unchanged (digest_emitter.py + digest_reconstructor.py + .claude/settings.json are engine-adjacent per D-296).
- §7 Engine version history: new engine-v15 entry added (compact form per S064 §1.5 deferral + S066 archive-pack discipline; full per-version index updated).

Engine-v15 is the **fourteenth engine-v-bump overall** and follows engine-v14 at preservation depth 0 (engine-v14 ratified S074 + engine-v15 immediately at S075 — **second-of-record adjacent-session engine-v-bump** after engine-v11 → engine-v12 at S063 → S064). §5.4 Session 022 engine-v-cadence minority does NOT re-escalate at this bump per content-driven-bump precedent chain extended through S075. §10.4-M25 P2 cadence-depth concern at engine-v15 reset to depth-0; future engine-v16 bump preservation forecast is engine-conventional within engine-v9 depth-8 second-longest precedent.

**Forward observation per §10.4-M25 P2 reopen warrant**: second-of-record adjacent-session engine-v-bump warrants forward observation. Engine-v16 at S076 would create three-engine-v-bumps-in-three-sessions pattern fully activating §5.4 cadence-runaway threshold. Forecast: engine-v16 at S076 would only fire on substantive phase-3.2 revision (per S073 D-281 EVD staged hybrid; phase-3.2 was originally minor extensions per (γ-6) per-direction discipline). S076 phase-3.2 is forecast-minor; engine-v15 expected to preserve at S076.

**Rejected alternatives:** Engine-v14 → engine-v15.1 (sub-version) — REJECTED per `engine-manifest.md` §5 (no sub-version discipline; integer increments only). Defer ratification to S076 — REJECTED per substantive scope at S075 already exceeding minor-amendment threshold per OI-002.

## D-299: Housekeeping `[none]` (15 sub-sections; forty-seventh-consecutive)

**Triggers met:** [none]

**Triggers rationale:** Per S041 D-126 + standing housekeeping discipline + forty-seventh-consecutive `[none]`-trigger pattern per S075 close; housekeeping is procedural-recording aggregating sub-section state observations per session.

**Non-Claude participation:** N/A per [none] triggers.

**Decision:** Housekeeping `[none]` at S075 close per standing discipline:

1. **§10.4-M10 written-warrant clause (c) operator-surfacing channel cumulative count** — NOT advanced at S075 close. Operator surfaced "Proceed with recommendation by S074 close" at S075 open which is direction-confirmation, not new substantive direction-setting per the §10.4-M10 clause (c) cumulative-count discipline (which counts substantive-direction-setting events, not confirmation-of-prior-direction). Cumulative count remains **n=11** (S036/S057/S060/S061/S063/S064/S066/S068/S069/S072/S074 chain unchanged).

2. **WX-28-1 forty-fifth close-rotation S069 OUT S075 IN at S075 close** zero retention-exceptions per `read-contract.md` v6 §2c close-rotation rule. S069 03-close.md rotates OUT (~6,676 words per S074 close §9 forecast); S075 03-close.md enters retention window. Aggregate-reducing action per §2b discharged.

3. **WX-24-1 MAD v4 forty-eighth-session no-growth streak preserved at S075 close**: MAD v4 spec unchanged at S075 (reviewer-prompt-template v3 lives in `validation-approach.md` v9 §(z6) per (z7) discipline, not in MAD v4 spec; per S058+S062+S064+S071+S073 MAD-without-MAD-spec-amendment precedent extended through S075). Pattern preserved at 33-session run from S042 reset (extends S074's 32-session record).

4. **Forty-seventh-consecutive housekeeping `[none]`-trigger pattern** at S075 close. D-299 extends pattern since D-126 Session 041 (47-session run from S041 to S075).

5. **D-129 twenty-ninth-consecutive + D-138 twenty-ninth-consecutive clean exercises** at S075 open (per 00-assessment §1 path-justification with five non-Path-AS alternatives surfaced and rejected + folder-name default applied).

6. **§5.6 GPT-family-concentration window-ii cumulative count** advances **ten-consecutive → eleven-consecutive** at S075 close per codex reviewer audit (codex preferred per v8 family-overlap-permitted rule + operator-preference at S074 carried forward; codex-family interrupts streak per S058+S062+S064+S071+S073+S074 codex-family precedent extended through S075). Window-ii observation continues per §5.6 minority preservation.

7. **Engine-v14 preserved at preservation depth 0 → engine-v15 ratified at preservation depth 0 at S075 close** per D-298. Engine-v14 had no preservation events (ratified S074, immediately superseded at S075). **Second-of-record adjacent-session engine-v-bump** after engine-v11 → engine-v12 at S063 → S064. Forward-observation per §10.4-M25 P2 reopen warrant.

8. **engine-feedback/INDEX.md disposition extensions** at S075 close per D-294 + D-295 + D-296 implementation work. Three γ-surface triage rows progressing materially:
   - **EF-067-reviewer-wall-clock-self-report-unreliable**: status `triaged-partially-resolved` → progressing per REVD-2 quarantine semantics codified in v9 §(z6); REVD-3 retrospective re-baseline candidate post-S076.
   - **EF-059-harness-telemetry-feed-for-tier-2-reviewer**: status `triaged-deferred-to-phase-3` → progressing per SCD-3 schema codification + CM1+CM3 implementation; resolution chain advancing toward fully-resolved at S076.
   - **EF-068-substrate-load-bearing-and-harness-telemetry**: status `triaged-partially-resolved` → progressing per CM1+CM3 implementation + check 26 substrate-aware branch + REVD-2; resolution chain advancing.
   
   Engine-feedback state preserved **0 new / 6 triaged / 10 resolved / 0 rejected** at S075 close (count unchanged; only disposition text extended).

9. **validation-debt/index.md update** at S075 close per VD-003 phase-3.1 gating-discharge: gating condition (a) capture mechanism finalised — DISCHARGED at S073 D-276 + reified at S075 implementation. Gating condition (c) digest schema specified-with-producer_kind/authority_level — DISCHARGED at S075 D-294 v9 §(z6) substantive codification. Gating condition (b) observation window data on β-phase substrate-use — n=5 first-triangulation-floor reached at S075 substrate-exercise (S071+S072+S073+S074+S075 chain). VD-003 status remains `in-progress` at S075 close per S073 D-284 (review_by_session: S076 unchanged); **full review at S076** per VD-003 lifecycle.

10. **Periphrastic-form discipline applied throughout S075 artefacts** per S065 honest-limit 11 forward-direction reified at **n=8** (S068+S069+S070+S071+S072+S073+S074+S075 close-narratives all applied periphrastic-form discipline; S075 preemptive). Check 27 keyword-matching heuristic over-fire surface avoided.

11. **Substrate-exercise pattern at S075 (n=5 in β-phase post-S071 D-264 codification window)** per S071+S072+S073+S074+S075 chain. Per VD-003 gating condition (b) Hawthorne-effect-vs-durable-behavior-change distinction: **n=5 completes first triangulation** (S076 VD-003 review forecast).

12. **Cross-family-originated-and-adopted-at-MAD-execution reframe-architecture pattern preserved at n=5** per S058+S062+S064+S071+S073 chain (no new instance at S075 per single-orchestrator implementation scope; pattern preserved as engine-conventional).

13. **First-of-record events at S075**:
    - First-of-record SCD-3 schema codification + CM1+CM3 capture-adapter operational + check 26 substrate-aware branch + check 27 §1-§8 enforcement (Codex-S074-F4 close).
    - Second-of-record adjacent-session engine-v-bump (engine-v14 → engine-v15 at S074 → S075; first-of-record was engine-v11 → engine-v12 at S063 → S064).
    - Path-AS phase-3-implementation reified at n=2 (S063 first-instance Path-L single-orchestrator phase-3 adoption + S075 second-instance under v8 family-overlap-permitted reviewer rule).

14. **EF-068-read-write-rebalance four-record-bundle reopen warrant per S069 D-255 NOT ACTIVATED at S075** (operator-directive scope-bounded to (γ-6) phase-3.1 per S074 close §7 next-session-recommendation; not activated at S075 implementation scope). Reopen warrant remains preserved as standing operator-discretionary surface; activation per P3 z10 reopen-warrant-activation-is-not-implementation-bundling discipline available at any S076+ session-open.

15. **`forward_references('S076')` substrate-required step at S076 session-open** per `prompts/development.md` engine-v13 substantive amendment per S071 D-264 (β-phase discipline carries forward from S071+S072+S073+S074+S075 to S076; n=6 forecast at S076 open completes second-triangulation post-first-triangulation-floor at S075). Structured declaration `substrate_session_open: exercised | unavailable | skipped` + `substrate_evidence:` required in S076 00-assessment per check 29 WARN-only enforcement; check 26 substrate-aware branch consumes digest at S076 close per CHKD-2 evidence-consuming framing operationalised at S075.

## §Pre-ratifications carried into S076+

- **Path-AS phase-3.2 implementation arc framing carries forward**: S076 close = phase-3.2 minor extensions per (γ-6) per-direction disposition discipline + VD-003 full review per VD-003 lifecycle review_by_session: S076. Phase-3.2 scope per S073 D-282: RAD-3 D2.1 activation candidate at S076 review window; REVD-3 retrospective re-baseline candidate at post-S076; SCD-3 expansion if SCD-2-first-tranche was adopted (NOT adopted at S075 — full SCD-3 codified at v9 §(z6); SCD scope at S076 is preserve-and-observe rather than expand).

- **(γ-6) per-direction disposition discipline carries forward**: each direction's disposition per S073 D-275 + D-276 through D-282 + S075 implementation status — CM (DISCHARGED at S075) / SCD (DISCHARGED at S075) / RAD (BRIDGED at S075; D2.1 candidate at S076) / REVD (QUARANTINED at S075; REVD-3 candidate post-S076) / CHKD (DISCHARGED at S075) / EVD (engine-v15 ratified at S075; engine-v15 preservation forecast at S076) / Q7 reviewer-prompt-template (v3 candidate at S075; v3 lock-in candidate at S076 per (z7) n=2) / Q8 EF-068 defer (preserved as standing operator-discretionary surface) / Q9 Path-AS (continues at S076 phase-3.2) / Q10 cross-spec depth (S075 v9 substantive scope is bounded; minor at S076).

- **VD-003 phase-3 activation gating conditions** carry forward to S076 retention window per S071 D-268 + S073 D-284 + S075 (no D introduced at S075 since VD-003 status unchanged at `in-progress`; gating-discharge happens via D-294 v9 §(z6) codification + S075 substrate-exercise, not via VD-003 row revision). Gating (a) DISCHARGED at S073 + reified at S075. (c) DISCHARGED at S075 D-294. (b) IN PROGRESS at S071-S075; **first-triangulation-floor reached at n=5 at S075**. Full review at S076 per VD-003 row.

- **§10.4-M22 P1 two-session-arc minority retrospective check at S076** (post-S075 phase-3.1 implementation): reopen warrants (a) spec-text drift + (b) synthesizer-framing absorption + (c) phase-3 implementation flaw tested at S076 phase-3.2 close per v9 §(z6) reading cleanly + P1+P2+P3+P4 dissent preserved as §10.4-M30/M31/M32/M33/M34/M35 per S073 D-283.

- **§10.4-M30 P1 (γ-1)/(γ-2) maximalist position reopen warrants** (a)+(b)+(c)+(d) tracked at S076-S078 retention window per S073 D-283.

- **§10.4-M31 P2 (γ-3) minimum-viable position reopen warrants** (a)+(b)+(c) tracked at S076 VD-003 review per S073 D-283 + S075 D-297 window-shift cleanup.

- **§10.4-M32 P3 portable-capture-adapter-contract reframe** carries forward to S075-S076+ phase-3 implementation: CM1+CM3 stack operational at S075 + CM2 deferred per S076 review per S073 D-276 + reified at S075 D-296.

- **§10.4-M33 P3 validator-as-evidence-consumer reframe** carries forward to S075+ phase-3 implementation: check 26 substrate-aware branch CHKD-2 evidence-consuming reified at S075 D-295.

- **§10.4-M34 P4 measurement-authority-not-inherited-from-YAML-container reframe** carries forward to S075+ phase-3 implementation: SCD-3 field-level authority rules reified at S075 D-294 v9 §(z6).

- **§10.4-M35 P3 z10 + P4 z-laundering-2 staging-per-direction reframe (consolidated)** carries forward to S075-S076 phase-3 implementation arc per (γ-6) per-direction disposition discipline per S073 D-275 + D-282 + S075 D-293 single-orchestrator implementation discipline.

- **EF-068-read-write-rebalance separate-scope at S076++ per S069 D-255** preserved; operator-discretionary four-record-bundle reopen warrant standing per P3 z10 reopen-warrant-activation-is-not-implementation-bundling discipline per S073 D-285 sub-section 14 + S074 D-292 sub-section 12 + S075 D-299 sub-section 14.

- **`forward_references('S076')` substrate-required step at S076 session-open** per `prompts/development.md` engine-v13 substantive amendment per S071 D-264 + check 29 WARN-only enforcement.

## §Engine-feedback INDEX disposition extensions

Per D-294 + D-295 + D-296:

**EF-067-reviewer-wall-clock-self-report-unreliable**: status `triaged-partially-resolved` (extended per S075 D-294 REVD-2 quarantine semantics codification in v9 §(z6); Direction B subsumption progressing per harness-measured fields specified in SCD-3 reviewer_invocations section; resolution chain progressing toward REVD-3 retrospective re-baseline post-S076 review).

**EF-059-harness-telemetry-feed-for-tier-2-reviewer**: status `triaged-deferred-to-phase-3` (extended per S075 D-294 + D-295 + D-296; (z6) digest schema specification with producer_kind/authority_level finalisation DISCHARGED at S075 v9 §(z6) substantive codification; CM1+CM3 capture-adapter operational; resolution chain advancing toward fully-resolved at S076 VD-003 review when n≥2 stable digest-bearing reviewer audits at S075-S076).

**EF-068-substrate-load-bearing-and-harness-telemetry**: status `triaged-partially-resolved` (extended per S075 D-294 + D-295 + D-296; Direction 1 (e) check 26 substrate-aware branch implementation DISCHARGED at S075 D-295; Direction 2 D2.1 vs D2.2 BRIDGED at S073 D-278 RAD-3 + reified at S075 D-294 v9 §(z6); resolution chain progressing).

## §First-class minorities preserved at S075 close

No new minorities at S075. Engine-wide minority count: **60 at S073 close** (preserved unchanged at S074 + S075). All 6 minorities from S073 D-283 (§10.4-M30 through §10.4-M35) carry forward; reopen warrants tracked per §Pre-ratifications above + workspace-structure.md v9 minor amendment per D-297 cleans stale window references but preserves reopen-warrant logic verbatim.

## §Engine-v15 ratified at S075 close

Engine-v14 → engine-v15 ratified at S075 close per D-298 substantive bump. Engine-v14 preservation depth 0 at S074 close → engine-v15 reset to 0 at S075. Second-of-record adjacent-session engine-v-bump after engine-v11 → engine-v12 at S063 → S064.
