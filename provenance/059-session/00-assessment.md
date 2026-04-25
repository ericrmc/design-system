---
session: 059
title: Assessment — Path T+L bundled scope (Triage-Classify of 3 EF-058 inbox records + Path L EF-058-uv-migration single-session resolution + records-substrate bootstrap discharge of S058 honest-limit #2 + minor retrieval-contract.md §5.1 template amendment); engine-v10 preserved (no engine-definition spec edits beyond minor template sync); first WX-58-1 second-observation 5-field recording per records-contract.md v1 §6
date: 2026-04-25
status: complete
---

# Assessment — Session 059

## §1 Operator input

Initial input: `/clear` followed by `PROMPT.md`. Thin operator input; default-agent dispatch path.

The session-open state at S059 is informed by **three operator-surfaced post-session intake records** filed direct-to-inbox at S058-post-session per `engine-feedback/INDEX.md` Note-on-direct-to-inbox-placement convention:

- `engine-feedback/inbox/EF-058-substrate-runtime-uv-migration-recommended-path.md` — operator intake disposition: defect-fix-shape Path T+L recommended for same-session resolution; six-step recommended path; preserves engine-v10.
- `engine-feedback/inbox/EF-058-claude-md-tools-clause-not-cross-checked-by-mad.md` — operator intake disposition: methodology-observation; substantive-arc-shape; **NOT recommended for same-session resolution**; defer.
- `engine-feedback/inbox/EF-058-tier-2-validation-discipline-by-distinct-agent.md` — operator intake disposition: meta-pattern subsuming the other two; substantive-arc-shape per S057 EF-055 precedent chain; operator-stated preference at intake **"should go through MAD"**; defer.

Plus one S058 honest-limit-deferred work item per S058 close §8 honest-limit #2: `tools/bootstrap-external-workspace.sh` records-substrate-bootstrap extension specified at `records-contract.md` v1 §5 but actual implementation deferred to "a minor follow-up session given S058 scope limits."

Absent operator override, the engine-conventional dispatch for S059 follows the three intake dispositions + bundles the S058 honest-limit-deferred work because EF-058-uv-migration also edits `tools/bootstrap-external-workspace.sh` (bundling-by-coincidence per S054 D-185 + D-186 precedent).

## §2 Workspace state at S059 open

Per `prompts/development.md` §How to operate Read activity:

- `MODE.md` — self-development; engine-v10 at S058 close.
- Active specs (engine-v10): `methodology-kernel.md` v6 / `multi-agent-deliberation.md` v4 / `validation-approach.md` v5 / `workspace-structure.md` v7 / `read-contract.md` v6 / `reference-validation.md` v3 / `retrieval-contract.md` v1 / `records-contract.md` v1 (NEW S058) / `engine-manifest.md` (versioning) / `identity.md` v2.
- `records/sessions/index.md` — 58 rows S001-S058; thin pointer-only file ~1,458 words; default-read replacing pre-engine-v10 SESSION-LOG.md per `read-contract.md` v6 §1 item 5.
- `open-issues/index.md` — 13 active OIs unchanged from S058 close; OI-016 counter at 2-of-3.
- 6-session retention window at S059 open: S053 / S054 / S055 / S056 / S057 / S058 closes default-read.
- `engine-feedback/INDEX.md` — status summary **3 new / 1 triaged / 7 resolved / 0 rejected** (3 new from S058-post-session intake; 1 triaged = EF-047-brief-slot-template deferred per S050 D-174).

**Primary inputs** for the S059 work:
- All three EF-058 inbox records (read in full at session-open).
- S058 close §7 next-session items + §8 honest-limit #2 deferred-bootstrap-implementation.
- `specifications/records-contract.md` v1 + `specifications/retrieval-contract.md` v1 (active engine-definition specs read in full at session-open).
- `tools/retrieval_server.py` + `tools/build_retrieval_index.py` + `.mcp.json` + `tools/bootstrap-external-workspace.sh` (target files for the Path L implementation).

**Substrate state at session-open**: pre-S059 retrieval index reflects S058 close state (549 documents / 58,198 identifiers). MCP stdio transport remains unverified per S051-S058 chain; the EF-058-uv-migration Path L work is the resolution path. Substrate exercised at session-open via mtime-rebuild check; `forward_references('S059')` available as organic-use diagnostic per `prompts/development.md` §How to operate.

## §3 Determination

**Path T+L bundled scope** (per S054 D-185 + D-186 precedent class): single-session default-agent triage-classify of all three EF-058 inbox records + Path L implementation of EF-058-uv-migration's six-step recommended path + records-substrate bootstrap implementation discharging S058 honest-limit #2 + minor amendment to `retrieval-contract.md` v1 §5.1 + §5 + §10 for template-shape sync.

Determined by:

1. **Three operator-surfaced intake dispositions converge on this shape.**
   - EF-058-uv-migration explicitly recommends Path T+L single-session per S054 D-185 + S052 D-180 precedent.
   - EF-058-claude-md-drift explicitly recommends defer-to-substantive-arc.
   - EF-058-tier-2-validation explicitly recommends defer-to-substantive-arc per operator "should go through MAD" preference.

2. **CLAUDE.md §Tools standing operator instruction** specifies `uv tool` install path — the Path L implementation aligns with the standing instruction (uv via PEP 723 inline metadata + `uv run`); resolves the S050 MAD's pretraining-default-pip+venv drift identified by EF-058-claude-md-drift at the operational layer (the methodological-pattern resolution remains deferred).

3. **WX-58-1 phase-2 gate cannot fire at S059** per `records-contract.md` v1 §6. Phase-2 fires iff ALL of: check 25 PASS at S058 + S059 close, ≥95% migrated-ID resolution at S059 close, fallback-index-readable at S058 close, zero record-witness drift through S059 close, S059 adds session record without editing SESSION-LOG.md (which is by then archive-surface). At S058 close: only one observation recorded; S059 must record second observation; S060 evaluates phase-2 firing. Therefore S059 cannot itself adopt phase-2 mirrored-minority migration. WX-58-1 5-field recording at S059 close is mandatory regardless of path.

4. **MAD not required.** Per `multi-agent-deliberation.md` v4 §When Multi-Agent Deliberation Is Required (d016 triggers):
   - **d016_2 (substantive spec revision):** the only spec-touching change is a minor amendment to `retrieval-contract.md` v1 §5.1 template shape + §5 dependency-install instructions + §10 honest-limit nuance — minor per OI-002 per S048 D-153 sub-pattern (template-shape-sync with implementation; ninth source-realignment-or-extension precedent chain S022/S030/S033/S040/S046/S051/S052/S054/S059). Spec content unchanged; v1 preserved.
   - **d016_3 (reasonable-disagreement):** the EF-058-uv-migration six-step path is concrete, technically bounded, operator-recommended; no reasonable disagreement.
   - **d016_4 (engine-version impact):** engine-v10 preserved; no engine-v bump.
   Single-orchestrator default-agent path per S052 D-180 + S054 D-185 + D-186 precedent.

5. **Triage classification of all three EF-058 records is single-orchestrator-tractable** per S048 D-153 / S054 D-185 precedent. Triage produces `engine-feedback/triage/EF-*.md` records carrying `triage_classification:` and `disposition:` fields; substantive resolution (for EF-058-claude-md-drift + EF-058-tier-2-validation) is deferred to dedicated MAD per their intake recommendations.

6. **Bundling of EF-058-uv-migration Path L with records-substrate bootstrap** is justified by:
   - Both edits touch `tools/bootstrap-external-workspace.sh`.
   - records-substrate bootstrap is S058 honest-limit #2 deferred-explicitly-to-follow-up-session; S059 is "follow-up session."
   - Bundling avoids two separate sessions editing the same file (precedent: S054 D-185 + D-186 bundled query-sanitization with aliases-consultation in same file).
   - records-substrate bootstrap is engine-adjacent implementation (records-contract.md v1 §5 specifies the obligation; implementation is engine-adjacent per the contract-vs-implementation split).

### §3a Engine-v10 preservation depth at this session

S059 = first post-engine-v10 session. **Path T+L preserves engine-v10** because the only spec edit is minor (retrieval-contract.md v1 template-shape sync) per OI-002 heuristic. Engine-v10 preservation depth at S059 close = 1 (continues).

Engine-v7 11-session record (S036→S048) and engine-v9 8-session record (S050→S057) remain references; engine-v10's preservation trajectory is unconstrained by this session's scope.

### §3b D-129 standing discipline (fourteenth-consecutive exercise)

Per D-129 standing discipline since S046 D-146 graduation. Per the discipline, surface considered-and-rejected non-Path-T+L alternatives at session-open assessment.

**Five considered-and-rejected non-Path-T+L alternatives**:

1. **Path A (Watch) pure** — rejected: three operator-surfaced intake records present non-trivial S059 agenda; default Path A would defer all three to a later session without triage, contradicting the EF-058-uv-migration intake's "resolve same-session" recommendation and leaving the eight-session MCP-transport-unverified chain unresolved into a ninth session.

2. **Path AS-MAD-execution (substantive-arc adoption for EF-058-tier-2-validation)** — rejected: per the EF-058-tier-2-validation intake disposition itself, the substantive-arc requires a phase-1 synthesis / design-space session BEFORE phase-2 MAD execution per S057 EF-055 precedent chain. S059 cannot skip phase-1; defer phase-1 synthesis to a dedicated future session that has scope-budget for it (likely S060+ post-WX-58-1 phase-2 evaluation).

3. **Path AS-MAD-execution phase-2 (records-substrate mirrored-minority migration)** — rejected: WX-58-1 phase-2 gate cannot fire until S060 close evaluation per records-contract.md v1 §6 (needs S059 close 5-field observation first). Cannot phase-2 at S059.

4. **Compressed single-session resolution-of-all-three EF records via single-orchestrator** — rejected: single-orchestrator can resolve EF-058-uv-migration (concrete defect-fix per OI-002 minor) but cannot single-orchestrate EF-058-claude-md-drift or EF-058-tier-2-validation per d016_2 + d016_3 substantive-revision triggers; the operator-stated "should go through MAD" preference for EF-058-tier-2-validation is explicit.

5. **Defer EF-058-uv-migration to substantive-arc-with-tier-2-validation** — rejected: the operational defect (MCP stdio transport unverified across 8 sessions) is well-understood and concrete; the EF-058-tier-2-validation deliberation will be more grounded if substrate-transport is resolved first (the records-substrate becomes truly first-class affordance for any future Tier-2-reviewer's mechanical-detection layer per EF-058-tier-2-validation candidate (α) "extend tools/validate.sh with new check that detects honest-limit text repetition across §2c retention-window's `03-close.md` files. Substrate-aware extension: use resolve_id / search over records-substrate when available"). Resolving substrate-transport is the prerequisite for the most-leverage Tier-2-reviewer mechanism candidate.

§5.12 Path-Selection Defender reopen warrant (a) "D-129 convention degradation" does NOT fire.

### §3c D-138 folder-name default (fourteenth-consecutive exercise)

`provenance/059-session/` per D-138 default convention since S045 / S046 D-146 graduation. No suffix, no slug. Convention scales across fourteen heterogeneous session classes (S046 / S047 / S048 / S049 / S050 / S051 / S052 / S053 / S054 / S055 / S056 / S057 / S058 / S059).

### §3d WX-58-1 records-discipline-soak observation second observation

Per `records-contract.md` v1 §6 phase-2 gate: every session close from S058 through S060 inclusive records records-discipline use in a `## Records substrate use (WX-58-1)` section with five fields:

- `check_25_status`: pass | fail | warn.
- `migrated_id_resolution`: count of `records/<family>/*.md` ids resolved by `resolve_id` / total records.
- `fallback_index_readable`: yes | no | not-tested.
- `record_witness_drift`: count of detected drifts.
- `session_record_added_without_editing_accretive_block`: yes | no | n/a.

S059 second observation expected:
- `check_25_status`: pass (post-implementation; assumes no record-witness drift introduced).
- `migrated_id_resolution`: post-uv-migration smoke-test will determine; the S058 first observation was 58-of-58 pre-MCP-transport-resolution.
- `fallback_index_readable`: yes (records/sessions/index.md remains flat-Markdown-readable independent of substrate transport).
- `record_witness_drift`: 0 (S059 adds S059.md record + appends index row consistently).
- `session_record_added_without_editing_accretive_block`: yes (S059 closes by writing records/sessions/S059.md + appending index row; no SESSION-LOG.md to edit because file no longer exists post-S058).

### §3e Substrate at session open

`forward_references('S059')` organic-use opportunity per `prompts/development.md` §How to operate paragraph (added S054 D-187). Pattern observation across S055-S058: tool value tracks inversely with prior close-narrative discipline thoroughness. S058 close §7 enumerated S059-landing forward-commitments (Path AS-MAD-execution phase-2 candidate; Path A; Path L+A; Path PD/OS); plus three EF-058 records explicit. Expected n=0 surface (clean propagation; all forward-commitments accounted for).

MCP stdio transport status unchanged from S051–S058 chain at session-open; the S059 Path L work is the resolution path.

## §4 Plan

### §4a Steps

1. **Pre-commit `00-assessment.md`** per S048-S058 precedent chain (this file; pre-work commit per D-017 spirit).
2. **Read activity completion**: full re-read of all 3 EF-058 inbox records ✓; records-contract.md v1 ✓; retrieval-contract.md v1 ✓; tools/retrieval_server.py ✓; tools/build_retrieval_index.py (top) ✓; tools/bootstrap-external-workspace.sh ✓; .mcp.json ✓.
3. **Triage all three EF-058 inbox records** per `workspace-structure.md` v7 §engine-feedback discipline:
   - `engine-feedback/triage/EF-058-substrate-runtime-uv-migration-recommended-path.md` — classify defect-fix-shape Path T+L; same-session resolution; resolved_by pointer to S059.
   - `engine-feedback/triage/EF-058-claude-md-tools-clause-not-cross-checked-by-mad.md` — classify substantive-arc-shape; deferred to dedicated future MAD per intake disposition.
   - `engine-feedback/triage/EF-058-tier-2-validation-discipline-by-distinct-agent.md` — classify substantive-arc-shape per S057 EF-055 precedent chain; deferred per operator-stated MAD preference at intake.
4. **Implement EF-058-uv-migration six-step Path L per intake recommendation**:
   - 4a. Add PEP 723 inline-deps to `tools/retrieval_server.py` (deps `mcp[cli]`, `pyyaml`).
   - 4b. Add PEP 723 inline-deps to `tools/build_retrieval_index.py` (deps `pyyaml`).
   - 4c. Update `.mcp.json`: command `python3` → `uv`; args `["tools/retrieval_server.py"]` → `["run", "tools/retrieval_server.py"]`.
   - 4d. Refactor `tools/bootstrap-external-workspace.sh`: replace pip-install instructions with uv-only path; remove `.cache/venv/` setup; bundle records-substrate-bootstrap per records-contract.md v1 §5.
   - 4e. Remove `.cache/venv/` directory (gitignored; verify no references).
   - 4f. Smoke-test `uv run tools/retrieval_server.py` startup + `uv run tools/build_retrieval_index.py` rebuild. Full MCP stdio smoke-test requires Claude Code restart; record honest-limit if not verifiable in-session.
5. **Bundle records-substrate-bootstrap implementation** in step 4d above:
   - Add `records-contract.md` to `SPEC_FILES` array.
   - Replace SESSION-LOG.md scaffolding with `records/` + `records/sessions/` directories + thin `records/sessions/index.md` per records-contract.md v1 §5 obligations.
   - Update validator smoke-test step (already in step 8 of bootstrap script; check 25 will assess records-substrate integrity).
   - Discharge S058 close §8 honest-limit #2 deferred-bootstrap-implementation.
6. **Minor amend `retrieval-contract.md` v1**:
   - §5.1 `.mcp.json` template: command `python3` → `uv`; args `["tools/retrieval_server.py"]` → `["run", "tools/retrieval_server.py"]`.
   - §5 step 2 dependency-install instructions: pip-install path → uv-only path (PEP 723 self-resolves).
   - §10 honest-limits: portability-tax language nuance (mcp[cli]+pyyaml two-package install → single-tool uv install; substrate scripts self-resolve deps via PEP 723).
   - Spec content (§1 scope, §2 capabilities, §3 failure behaviour, §4 workspace state, §6 phase-2 gate, §7 minorities, §8 versioning, §9 validation) unchanged.
   - Minor per OI-002 (template-shape sync with implementation; ninth source-realignment-or-extension precedent chain).
   - v1 preserved (no version bump).
7. **Run validator** `tools/validate.sh` post-implementation; record PASS/FAIL/WARN counts. Verify check 25 records-substrate integrity passes. Verify check 1 + check 6 records-substrate-aware updates passing.
8. **Rebuild retrieval index** post-spec-edits (`uv run tools/build_retrieval_index.py`).
9. **Update `engine-feedback/INDEX.md`**: status summary `3 new / 1 triaged / 7 resolved / 0 rejected` → `0 new / 3 triaged / 8 resolved / 0 rejected`. Add disposition narrative to each EF-058 row.
10. **Write `02-decisions.md`** with decisions:
    - D-206 Path T+L bundled scope ratified [default-agent].
    - D-207 EF-058-uv-migration adopted via 6-step Path L [default-agent + operator-recommended at intake; minor per OI-002].
    - D-208 EF-058-claude-md-drift triaged substantive-arc-deferred [default-agent triage].
    - D-209 EF-058-tier-2-validation triaged substantive-arc-deferred per operator MAD preference [default-agent triage].
    - D-210 minor `retrieval-contract.md` v1 §5.1 + §5 + §10 template-shape-sync amendment [default-agent; minor per OI-002].
    - D-211 records-substrate bootstrap implementation in `tools/bootstrap-external-workspace.sh` discharges S058 honest-limit #2 [default-agent; minor per OI-002 per records-contract.md v1 §5 spec].
    - D-212 housekeeping `[none]`-trigger pattern (thirty-first-consecutive).
11. **Add S059 session record** at `records/sessions/S059.md` per records-contract.md v1 §2.1 (id, session, date, title, summary, status: closed, anchor_close).
12. **Append S059 row** to `records/sessions/index.md` per records-contract.md v1 §2.2 thin pointer-only pattern.
13. **Write `03-close.md`** per S058 precedent: §1 artefacts / §1b spec changes / §1c WX-35-1 / §1d validator / §1e engine-v / §2 operational warrants / §3 engine-v disposition / §4 minorities / §5 watchpoints (WX-58-1 second observation 5-field) / §6 substrate / §7 next-session / §8 honest limits / §9 aggregate / §10 meta-observations / §11 commit-and-close.
14. **Commit + push** all changes with concise message per `CLAUDE.md` §Commit workflow.

## §5 Halt points

- **Halt-1 (engine-conventional first-step)**: ratify Path T+L bundled scope before triage-write commit. **Default**: proceed per §3 determination. If operator surfaces revision (e.g., "actually phase-2 records-substrate first"), ratify revised scope. Default-proceed adopted absent operator surface.
- **Halt-2 (informal)**: mid-session if Path L implementation surfaces non-trivial defect (e.g., FastMCP version pinning issue under uv run; PEP 723 resolution failure; .mcp.json command not picked up by Claude Code). Per EF-058-uv-migration intake §Suggested Change: "If the smoke-test surfaces a non-trivial defect (FastMCP version pinning issue; stdio handshake mismatch; uv run PATH issue under Claude Code's spawn environment), reclassify as substantive substrate fix and open new EF record. The current scope assumes config-shape problem with config-shape fix."
- **Halt-3 (close ratification)**: ratification of close at end. **Default**: proceed to close; engine-v10 preserved; spec edit minor; archive-packs not needed (no destructive changes).

## §6 Session forecast (rough; for honest-limits)

- **Decisions**: 7 expected: D-206 Path T+L bundled scope; D-207 uv-migration; D-208 claude-md-drift triage; D-209 tier-2-validation triage; D-210 retrieval-contract.md template amendment minor; D-211 records-substrate bootstrap; D-212 housekeeping `[none]`.
- **Spec edits**: 1 minor (retrieval-contract.md v1 §5.1 + §5 + §10 documentary). v1 preserved (no version bump).
- **Engine-v**: engine-v10 preserved.
- **New first-class minorities**: 0 (no MAD; no contested deliberation). Engine-wide minority count remains 40.
- **Aggregate forecast**: ~78,000–79,500 words / 22 files (S053 close ~3,800 rotates OUT; S059 close ~2,500–3,500 estimated; spec edit ~+200 minor; index file +25-40 row). Headroom to 90K soft ~10,500-12,000.
- **Validator forecast**: ~1,350+ PASS / 0 FAIL / 22-26 WARN.

## §7 Honest limits

1. **Path T+L bundled scope proceeds per intake-disposition + S058 honest-limit #2 alignment absent operator override.** Reversibility: operator may surface revision at any halt point. Default-proceed honoured per S048 D-152 / S054 D-185 / S055 D-189 / S056 D-191 / S057 D-194 / S058 D-198 precedent chain.

2. **MCP stdio transport smoke-test partially in-session.** The full smoke-test requires Claude Code restart (the MCP server is spawned at Claude Code project-load time per `.mcp.json`); this session can verify `uv run tools/retrieval_server.py` startup + dependency resolution + `uv run tools/build_retrieval_index.py` rebuild but cannot verify the MCP tool surface appears in the agent context until next session-open. If next session-open shows `mcp__selvedge-retrieval__search` etc. appear and `resolve_id("S058")` returns the records/sessions/S058.md record via tool call, the smoke-test passes; otherwise reclassify per §5 Halt-2.

3. **Records-substrate bootstrap implementation is normative-spec-aligned, not deeply user-tested.** records-contract.md v1 §5 specifies the obligations; the implementation in `tools/bootstrap-external-workspace.sh` follows the spec but has not been exercised against a fresh-bootstrap target until next external-workspace bootstrap. Honest-limit: external-workspace bootstrap with records-substrate is post-S059 first-exercise candidate.

4. **EF-058-claude-md-drift + EF-058-tier-2-validation triage-with-defer is interim disposition.** The substantive-arc resolution paths require dedicated future MAD per S057 EF-055 precedent chain. S059's triage classifies and defers; S060+ phase-1 synthesis (Path AS Shape-1) for EF-058-tier-2-validation could begin once S060 close evaluates WX-58-1 phase-2 firing per records-contract.md v1 §6.

5. **Read-discipline coverage at session open**: per `read-contract.md` v6 §1 enumeration: MODE.md ✓; engine-manifest ✓; read-contract ✓; workspace-structure ✓; retrieval-contract ✓; records-contract ✓; methodology-kernel ✓ (referenced via S058 close); multi-agent-deliberation ✓ (referenced via S058 close); validation-approach ✓ (referenced via S058 close); identity ✓ (referenced via S058 close); reference-validation ✓ (referenced via S058 close); PROMPT.md ✓; prompts/development.md ✓; records/sessions/index.md ✓; open-issues/index.md ✓; engine-feedback/INDEX.md ✓; S058 close in detail ✓; 3 EF-058 inbox records in detail ✓. **Honest-limit deferred**: S053-S057 closes not freshly re-read in detail at S059 open beyond their content as referenced via S058 close §3 + §7 + §8 narratives. methodology-kernel.md / multi-agent-deliberation.md / validation-approach.md / identity.md / reference-validation.md / prompts/application.md not freshly re-read in detail at S059 open per content-stability across engine-v10 boundary (no substantive changes since engine-v9 boundary at S050 close). Recorded transparently per WX-22-1.

6. **Tier-2-self-validation discipline gap acknowledged.** Per EF-058-tier-2-validation: this S059 session itself exercises the same Tier-2-by-the-doing-agent discipline that the deferred substantive-arc will deliberate on. Per EF-058-tier-2-validation §Application-Scope Disposition: "the recursive concern (who Tier-2-validates the MAD that decides Tier-2-validation) is a feature not a bug." S059 proceeds with default discipline; voluntary application of an unspecified mechanism would be premature-formalisation; the methodology's resolution path is the dedicated MAD that will define the discipline.

7. **WX-44-1 + WX-44-2 + WX-47-1 codex-CLI discipline NOT exercised at S059** because no codex CLI invocation is required (no MAD; no cross-family reviewer). Watchpoint cumulative counts unchanged.

8. **§5.6 GPT-family-concentration window-ii observation NOT advanced at S059** because no MAD convenes; window-ii substantive-deliberation data point chain (S044+S045+S047+S050+S058) does not extend at S059.

9. **WX-43-1 explicit-instruction variant** cumulative tracking continues; S059 self-orchestrator may have one or more invocations of subagents (e.g., for triage-record review or close-narrative review) — track per-invocation explicit-instruction adherence in 02-decisions.md if any.

10. **Aggregate forecast imprecise.** Per S054-S058 close §9 WX-22-1 honest-limits chain. Forecast ~78,000-79,500 may be ±2,000 words from actual.

11. **Records-substrate bootstrap may surface scope creep.** The records-contract.md v1 §5 bootstrap obligations are well-defined (5 numbered steps); however integrating with existing bootstrap-external-workspace.sh + ensuring the validator smoke-test step still works on the empty-records-substrate-aware workspace state may surface unexpected friction. If non-trivial: split into two minor decisions (D-211a uv-migration bootstrap update; D-211b records-substrate bootstrap deferred to S060) per CLAUDE.md commit-rather-than-amend discipline.

12. **D-129 fourteenth-consecutive + D-138 fourteenth-consecutive** clean exercises. Per the discipline, surfacing five non-Path-T+L alternatives is the standing-discipline pattern (per §3b). No degradation surface.
