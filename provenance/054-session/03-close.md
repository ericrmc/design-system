---
session: 054
title: Close — Path T+L (Triage-Classify + minor Path L Implementation Fix) reified at n=2 with first-instance multi-intake same-session resolution; EF-053 + EF-054 both Direction A adopted; D-185 Path T+L ratified + D-186 EF-053 Direction A + D-187 EF-054 Direction A + D-188 housekeeping (14 sub-sections); engine-v9 preserved preservation window count 3→4; engine-feedback state 2 new / 1 triaged / 4 resolved → 0 new / 1 triaged / 6 resolved; D-129 ninth-consecutive + D-138 ninth-consecutive clean exercises; WX-28-1 twenty-fourth close-rotation zero retention-exceptions; WX-24-1 MAD v4 twenty-seventh-session no-growth new record; WX-34-1 remediation preserved
date: 2026-04-25
status: complete
---

# Close — Session 054

## §1 Artefacts produced

### §1a Provenance (`provenance/054-session/`)

- `00-assessment.md` (~3,800 words; commit `4f698c7`) — pre-work commit per D-017 spirit + S048/S049/S050/S051/S052/S053 precedent chain. Proposed Path T+L (Triage-Classify + minor Path L Implementation Fix) per `prompts/development.md` §How to operate (inbox 2 status:new triggers triage consideration). §3 determination + §3a minority-warrant zero fire + §3b WX-50-1 phase-2 gate post-window state + §3d MCP stdio transport unverified. §4a D-129 ninth-consecutive exercise with five considered-and-rejected non-Path-T+L alternatives. §4b/§4c Direction A adopted for both EF-053 + EF-054. §5 eleven-step work plan. §7 ten honest limits including MCP transport unverified + ID pattern set curated not exhaustive + EF-054 observational value unproven.
- `02-decisions.md` (~3,400 words; this close commit) — **four decisions**: D-185 Path T+L ratified `[none]` single-agent reason + D-186 EF-053 Direction A adopted `[d016_2]` minor + D-187 EF-054 Direction A adopted `[d016_2, d016_3]` minor + D-188 housekeeping `[none]` 14 sub-sections.
- `03-close.md` — this file.

No `STATUS.md` (single-orchestrator). No `01-brief-shared.md` / `01X-perspective-*.md` / `01-deliberation.md` / `manifests/` / `participants.yaml` (no MAD convened; Path T+L is single-orchestrator per D-185). No archive subdirectories (no current-session raw exceeds 8K hard ceiling). No external artefact in self-dev.

### §1b Specification changes THIS session

**Two minor edits** to one engine-definition file + **two minor edits** to one engine-adjacent file:

1. **`prompts/development.md`** (engine-definition; minor per OI-002 per `engine-manifest.md` §5 minor-elaboration heuristic) — added one paragraph in §How to operate following the inbox-triage clause naming the new `forward_references(target)` MCP tool as a useful diagnostic at session open. Single sentence (well, single paragraph of three sentences). Names the tool; states it is additive to the contract minimum (`search` + `resolve_id`); explicitly notes agents using prose-scan reading still satisfy the read discipline. No prior version preserved (per Session 017 + S048 D-153 precedent: prompts/* files are prompt text with history in git rather than versioned-via-suffix documents). Per D-187.

2. **`tools/retrieval_server.py`** (engine-adjacent; minor per OI-002 per the 9-precedent chain) — two distinct edits in one file:
   - **EF-053 fix (per D-186)**: added module-level `_ID_TOKEN_RE` regex (matches the curated ID family with negative lookbehind/lookahead on `"` for idempotence) + module-level `_sanitize_query()` helper. Modified `search()` to call `_sanitize_query()` and pass the sanitized result as the FTS5 MATCH expression as primary path; reordered fallback to whole-query phrase-wrap as last-ditch defensive.
   - **EF-054 extension (per D-187)**: added new `@mcp.tool()` decorated `forward_references(target: str) -> dict` function inside `build_server` closure (placed after `_match_payload` helper and before `return mcp`). Returns all line-precise occurrences of `target` in the `identifiers` table, sorted by `source_path` then `line`.

All other active specs remain at their S053-close versions: `PROMPT.md` unchanged; `MODE.md` unchanged; `prompts/application.md` unchanged (v8); `methodology-kernel.md` v6 unchanged; `multi-agent-deliberation.md` v4 unchanged; `validation-approach.md` v5 unchanged; `workspace-structure.md` v6 unchanged; `identity.md` v2 unchanged; `reference-validation.md` v3 unchanged; `read-contract.md` v5 unchanged; `retrieval-contract.md` v1 unchanged; `engine-manifest.md` unchanged; `specifications/aliases.yaml` schema_version 1 unchanged; `.mcp.json` unchanged; `tools/validate.sh` unchanged; `tools/build_retrieval_index.py` unchanged; `tools/bootstrap-external-workspace.sh` unchanged.

### §1c Development-provenance files amended (WX-35-1 claim discipline)

Per WX-35-1 standing discipline, each claimed file amendment is verified via `git log --oneline <path>` at close and explicitly retracted if not committed.

- **`tools/retrieval_server.py`** — **EDITED this close commit**. Two distinct minor changes per §1b above. Verified via `git log --oneline tools/retrieval_server.py` at close: pending commit will be the latest entry.
- **`prompts/development.md`** — **EDITED this close commit**. One paragraph added in §How to operate per §1b above.
- **`engine-feedback/INDEX.md`** — **EDITED this close commit**. Status summary: `2 new / 1 triaged / 4 resolved / 0 rejected` → **`0 new / 1 triaged / 6 resolved / 0 rejected`**. Records table dispositions for EF-053 + EF-054 updated to `**resolved** (S054 D-185 + D-186)` and `**resolved** (S054 D-185 + D-187)` respectively with full disposition narratives.
- **`engine-feedback/triage/EF-053-search-query-parser-unquoted-hyphen-fts5-not-operator.md`** — **CREATED this close commit**. Triage record per `workspace-structure.md` v6 §engine-feedback schema; `status: resolved`; `disposition: Direction A`; references D-185 + D-186; lists tool amendment to `tools/retrieval_server.py`.
- **`engine-feedback/triage/EF-054-forward-reference-mcp-tool-for-session-open-commitment-audit.md`** — **CREATED this close commit**. Triage record per same schema; `status: resolved`; `disposition: Direction A`; references D-185 + D-187; lists tool amendment to `tools/retrieval_server.py` + spec amendment to `prompts/development.md`.
- **`SESSION-LOG.md`** — **EDITED at close** (S054 thin row appended per Q5=(a) ≤180-word target).
- **`provenance/054-session/00-assessment.md`** — **CREATED** (commit `4f698c7` pre-work).
- **`provenance/054-session/02-decisions.md`** — **CREATED this close commit**.
- **`provenance/054-session/03-close.md`** — **CREATED this close commit** (this file).
- **`engine-feedback/inbox/EF-053-...md`** — **NOT edited** per WX-35-1 explicit retraction. Intake preserved verbatim per `workspace-structure.md` v6 §engine-feedback "intake files preserved verbatim" convention; lifecycle state carried by triage file + INDEX.md.
- **`engine-feedback/inbox/EF-054-...md`** — **NOT edited** per WX-35-1 explicit retraction. Same intake-preserved convention.
- **`specifications/*.md`** (other than the prompt change which is in `prompts/development.md` not `specifications/`) — **NOT edited** per WX-35-1 explicit retraction. No spec edit at engine-definition level this session. No engine-v bump.
- **`specifications/aliases.yaml`** — **NOT edited** per WX-35-1 explicit retraction. Schema and seed entries unchanged.
- **`specifications/engine-manifest.md`** — **NOT edited** per WX-35-1 explicit retraction. No engine-v bump.
- **`tools/build_retrieval_index.py`, `tools/validate.sh`, `tools/bootstrap-external-workspace.sh`** — **NOT edited** per WX-35-1 explicit retraction.
- **`open-issues/*.md`** — **NOT edited** per WX-35-1 explicit retraction. No OI opened/resolved/amended this session; 13 active OIs unchanged. Neither EF-053 nor EF-054 promoted to OI (both classified minor per OI-002; both resolved within the engine-feedback triage lifecycle; OI promotion would have required substantive scope).
- **`open-issues/index.md`** — **NOT edited** per WX-35-1 explicit retraction.
- **`PROMPT.md`, `MODE.md`, `prompts/application.md`, `CLAUDE.md`** — **NOT edited** per WX-35-1 explicit retraction.
- **`engine-feedback/triage/*.md`** (other than the two new files this session) — **NOT edited** per WX-35-1 explicit retraction. Existing 4 triage files (EF-001 + EF-047-retrieval-discipline + EF-047-session-inputs + EF-047-brief-slot-template + EF-051) unchanged.
- **`.mcp.json`, `.gitignore`** — **NOT edited** per WX-35-1 explicit retraction.
- **`.cache/venv/`** — **PRE-EXISTING mid-session use** (gitignored; not committed). S051-created venv re-used for smoke-tests.
- **`.cache/retrieval.db`** — **REBUILT mid-session** (gitignored; not committed). Rebuild triggered by mtime check after `00-assessment.md` was committed; post-rebuild stats: 461 documents / 51,724 identifiers (up from S051's 448 docs / 48,852 identifiers). Re-used for EF-054 smoke-test verification of new files indexing.

### §1d Validator status at close

Actual validator state at close: to be recorded post-commit. Forecast: **1246+ PASS / 0 FAIL / 14–18 WARN → PASS**.

- Aggregate default-read surface: forecast **~73,200 words across 21 files**. Close-rotation S048 OUT (~3,500 words estimate) + S054 enters (~3,900 words estimate this close + ~3,800 assessment + ~3,400 decisions = the close is what enters retention; assessment + decisions are mid-session-only). Net delta from S053 (74,449) approximately -1,200 (close-rotation negative) or comparable. Under §2b 90K soft with comfortable ~16,800 words headroom.
- SESSION-LOG.md post-thin-row: ~5,910 words forecast. Well under 6K soft (~90 words headroom). Well under 8K hard. WX-34-1 remediation preserved.
- Check 20 per-file: PASS (unchanged from S053 — no file added/removed at the spec level; `prompts/development.md` minor amendment grows ~80 words from prior baseline ≈1,580 to ≈1,660; well under any per-file budget; MAD 6,637 + reference-validation 7,160 soft-warnings persist).
- Check 20 aggregate: PASS.
- Check 21 archive-pack manifest integrity: PASS (no new archive-pack this session).
- Check 22 archive-pack citation consistency: PASS (no new archive citations; existing citations unchanged).
- Check 23 MODE.md presence: PASS.

Expected 14–18 warnings breakdown:
- 2 spec soft-warnings (`multi-agent-deliberation.md` 6,637 + `reference-validation.md` 7,160; unchanged; designed).
- 12 pre-existing "no rejected alternatives found" design-intent warnings (2 per session × S046/S047/S048/S051/S052/S053).
- 0–4 new "no rejected alternatives" warnings for S054 `02-decisions.md` D-185 + D-186 + D-187 + D-188 (each cites alternatives via cross-file reference to `00-assessment.md` §4a/§4b/§4c; validator regex matches per-decision body content — D-186 + D-187 each have inline "Alternatives considered" sections; D-185 + D-188 cross-reference §4a).

### §1e Engine-version status THIS session

**Engine-v9 preserved** at S054 close; preservation window count **3 → 4** (S051 first post-v9 + S052 second post-v9 + S053 third post-v9 + S054 fourth post-v9). Engine-v9 established S050 per D-172; no engine-v bump this session. §5.4 cadence minority does not re-escalate (non-bump session; precedent chain v5–v9 intact per S028 D-096 / S033 D-107 / S036 D-114 / S048 D-154 / S050 D-172).

## §2 Operational warrants changed or advanced

1. **EF-053 inbox→triaged→resolved within single session.** Lifecycle complete. Engine-feedback state 1 new / 1 triaged / 4 resolved → 0 new / 1 triaged / 5 resolved (after D-186); subsequent transition to 0 new / 1 triaged / 6 resolved (after D-187). Direction A (query-sanitization at server level) implemented in `tools/retrieval_server.py` via new `_ID_TOKEN_RE` + `_sanitize_query()` + `search()` reordering. Original failure case `search("D-129 standing discipline")` now returns 3 BM25-ranked results without crash. Smoke-test 10-of-10 unit + 4-of-4 integration PASS.

2. **EF-054 inbox→triaged→resolved within single session.** Lifecycle complete. New `forward_references(target)` MCP tool added to `tools/retrieval_server.py`. Paired minor documentary amendment to `prompts/development.md` §How to operate naming the new tool. Smoke-test 7-of-7 PASS via FastMCP tool-registration. Operator framing "do not introduce queries rather add MCP features" honoured directly.

3. **Path T+L reification at n=2 with first-instance multi-intake variant.** S052 first-instance (single record EF-051) + S054 second-instance (two records EF-053 + EF-054). The bundled label "T+L" is now reified. The multi-intake sub-pattern (multiple records resolved same-session under one Path T+L invocation) is first-instance at S054; reification deferred until n=2 (would require future multi-record Path T+L session).

4. **D-129 standing discipline ninth-consecutive clean exercise.** Five considered-and-rejected non-Path-T+L alternatives in `00-assessment.md` §4a. §5.12 Path-Selection Defender reopen warrant (a) does not fire.

5. **D-138 folder-name default ninth-consecutive clean exercise.** `provenance/054-session/` no suffix, no slug.

6. **WX-28-1 twenty-fourth close-rotation zero retention-exceptions.** S048 rotates OUT at S054 close; S054 enters. Retention window post-rotation: S049/S050/S051/S052/S053/S054.

7. **WX-24-1 MAD v4 twenty-seventh-session no-growth streak new record.** `multi-agent-deliberation.md` v4 stable at 6,637 words. New record from S042 reset point (S043–S054 all no-growth; 12-session streak).

8. **WX-34-1 remediation preserved.** SESSION-LOG.md post-thin-row ~5,910 words (under 6K soft with ~90 words headroom). Compression at S051 holds; no new pressure but headroom narrowing.

9. **§10.4-M2 (Skeptic-preserver premature-feedback-pathway) continued preservation.** Engine-feedback pathway exercised twice this session (EF-053 + EF-054 lifecycle transitions). Pathway has now accumulated 7 lifecycle records at S054 close (1 external EF-001 + 4 self-dev EF-047×3 / EF-051 + 2 self-dev EF-053 / EF-054 this session). Pathway is in active routine use; minority preserved-unactivated.

10. **§10.4-M7 P2 minimum-adoption observation continues.** WX-50-1 gate not-fired under stricter counting (first clause satisfies). Phase-1 tools used at S054 (smoke-tests + index rebuild + new forward_references tool exercise) so second clause "zero use across 3+ consecutive sessions" does NOT satisfy. Minority preserved-unactivated under partial-activation interpretation.

11. **No new first-class minority preserved.** Single-orchestrator Path T+L; no deliberation; no dissent surface. 36 minorities preserved unchanged.

12. **Twenty-seventh-consecutive housekeeping `[none]`-trigger decision**. D-188 extends the pattern (housekeeping consolidation decisions with `[none]` triggers since D-126 Session 041). Pattern deeply instantiated.

13. **Substrate first-real-use → second-real-use → third-real-use → fourth-real-use defect-surfacing-and-resolution pattern.** S051 surface EF-051 → S052 resolve EF-051 → S053 surface EF-053 → S054 resolve EF-053 + extend tool surface via EF-054. Cadence stable at ≈1 actionable observation per substrate-exercise session at phase-1 maturity. S054 is first session to RESOLVE both a defect AND extend the tool surface in same session. Total inbox→resolved lifecycle events at S054: 6 (EF-001 + EF-047×3 + EF-051 + EF-053 + EF-054) net of 1 still-triaged (EF-047-brief-slot-template).

14. **First-instance multi-intake same-session resolution sub-pattern.** S054 resolves two records EF-053 + EF-054 in the same session under one Path T+L invocation. Each record gets its own decision (D-186 + D-187) and its own triage record; no laundering of unrelated work. Sub-pattern observation; reification deferred to n=2.

## §3 Engine-v disposition and preservation depth

**Engine-v9 preserved at S054 close; preservation window count = 4.**

S054 is the fourth post-engine-v9 session. Engine-v9 established at S050 per D-172 (MAD-adopted new engine-definition spec bump-provenance class). §5.4 cadence minority does not re-escalate.

Forward observation: engine-v9 preservation window will close at depth TBD. Candidate triggering events:
- Phase-2 substrate extensions per WX-50-1 firing — gate did NOT fire across S050–S053 under stricter counting; phase-1 paused; phase-2 adoption requires new triggering events (Condition 2 structured-filter/graph-traversal fallback; Condition 3 external-workspace adoption; or operator surfacing). EF-054 Direction A is a phase-1-compatible additive extension and does NOT advance phase-2.
- Post-arc `selvedge-disaster-response` review triggering any of S047 D-150 three deferred candidates (i)/(ii)/(iii) could produce engine-v10.
- Operator-surfaced agenda for any engine-definition substantive revision could produce engine-v10 at any session.

## §4 Preserved first-class minorities at S054 close

**36 first-class minorities preserved engine-wide at S054 close** — unchanged from S053. No new minority preserved; no minority discharged; no minority activated this session.

Full enumeration per `specifications/workspace-structure.md` v6 §10.4 (M1–M11) + §5.1/§5.4/§5.5/§5.6/§5.7/§5.8/§5.9/§5.10/§5.11/§5.12/§5.13/§5.14 + Session 024 A.4 four minorities + Session 027 §A/§B/§C + existing preserved-minorities in `reference-validation.md` v3 §10.1/§10.2/§10.3 + `retrieval-contract.md` v1 §7.1–§7.5 (mirrored with workspace-structure §10.4-M7–M11).

Per §D-188 observation-window advances: §10.4-M2 continued-preservation (pathway-in-active-use 7 lifecycle records); §10.4-M7 partial-activation (first clause only; not both); §10.4-M8/-M9/-M10/-M11 preserved-unactivated; §5.6 worst-case-side carries forward with window-ii observation deferred to next MAD-involving session.

## §5 Watchpoints status at S054 close

- **WX-24-1** — MAD v4 stable 6,637 words. **Twenty-seventh-session no-growth streak** (S043–S054). New record (12-session run).
- **WX-24-3** — reference-validation label discipline n=8 stable.
- **WX-27-1** — stable.
- **WX-28-1** — **twenty-fourth close-rotation** (S048 rotates OUT; S054 enters); zero retention-exceptions.
- **WX-33-2** — reference-validation.md v3 7,160 words stable.
- **WX-34-1** — **remediation preserved but headroom much narrower than forecast**. SESSION-LOG actual post-row 5,994 words per validator; ~6 words headroom to 6K soft. Forecast was 5,910 / ~90 words headroom; actual S054 row is ~540 words (slightly over Q5=(a) ≤180-word target per content-adaptive density precedent). Forward observation: S055 row will almost certainly cross the 6K soft warning. Preemptive-restructure candidate at S055 close if S055 row pushes past 6K AND S054 retroactive compression is not undertaken; alternatively, S055 itself may compress the S054 row in a Path L+A move (S051 D-178 precedent).
- **WX-35-1** — standing discipline applied cleanly; explicit retractions recorded in §1c.
- **WX-43-1** — cumulative baseline n=6-of-8 + explicit-instruction variant n=0-of-9 (S047+S049+S050+S051+S052+S053+S054). OI-promotion discharged-as-not-warranted per S050 D-176. No sub-agents convened at S054; cumulative n unchanged.
- **WX-44-1** — codex-CLI independence-phase breach n=3 across S044+S045+S047. Not exercised this session (no codex invocation). Forward-convention candidate held cleanly by trivial non-exercise.
- **WX-44-2** — codex CLI model-version-drift discipline: not exercised this session.
- **WX-47-1** — codex-CLI argv `---` YAML parsing fragility: not exercised this session.
- **WX-50-1** — observation window closed at S053; phase-1 paused; phase-1 tools available for organic use. EF-053 Direction A removes a known friction; EF-054 Direction A adds a new diagnostic tool (`forward_references`). Both improve organic-use ergonomics for S055+ sessions.

## §6 No retrieval-substrate WX-50-1 recording obligation

Per `retrieval-contract.md` v1 §6, the WX-50-1 3-field recording obligation applies to sessions S050 through S053 inclusive. S054 is post-window; no obligation.

**Observational note** (not contract-required): substrate use at S054 was substantial — index rebuild after assessment commit (461 docs / 51,724 identifiers); 14+ smoke-test invocations across `_sanitize_query` unit tests + `search` integration + `forward_references` tool tests + `resolve_id` regression sanity. All invocations were direct via `.cache/venv/bin/python` (substrate-mirror path); FastMCP stdio transport remained unverified in-session per S051/S052/S053 honest-limit chain.

## §7 Next-session items and forward observations

**Session 055 recommendation**: default-agent session. Priorities:

- **Inbox check at open**: `engine-feedback/inbox/` has **0 new records** at S054 close. Path T not indicated unless new intake surfaces between S054 close and S055 open. Default Path A (Watch) most likely if no new state intervenes.
- **`forward_references` first organic-use exercise.** S055 Case Steward may call `forward_references("S055")` at session open as part of the Read activity (per the new `prompts/development.md` amendment). If the call surfaces forward-commitments that close-narrative-only relay would have dropped, EF-054 Direction A's value-evidence accumulates organically. If it surfaces nothing new beyond what S054 close §7 names, the tool is benign-but-unused at S055 specifically.
- **External-application arc progression**: `selvedge-disaster-response` arc S002–S005 pending operator transport; substrate available via bootstrap-refresh (operator-discretionary). Not S055-actionable absent operator surfacing.
- **Post-arc self-dev review obligation** (carrying from S047 D-150): three remaining deferred spec-amendment candidates (i)/(ii)/(iii) preserved for post-arc review. Unchanged at S054.
- **WX-34-1 forward observation**: SESSION-LOG headroom narrowing to ~90 words at S054 close. If S055 + S056 each add ~500 word rows, soft warning fires at S056 close; preemptive restructure candidate at S057. Forward-observation flag.

**S055 close should evaluate**:
- Engine-v9 preservation (window count would reach 5 if S055 preserves; matches engine-v4's 5-session prior record).
- D-129 tenth-consecutive exercise.
- D-138 tenth-consecutive folder-name default.
- §5.6 GPT-family-concentration window-ii observation if MAD convenes; else N/A.
- WX-28-1 twenty-fifth close-rotation (S049 rotates OUT; S055 enters).
- WX-24-1 MAD v4 twenty-eighth-session no-growth (if no MAD edit).
- `forward_references` first organic-use disposition (used / not-used / surfaced-something / surfaced-nothing).
- WX-34-1 SESSION-LOG headroom (preemptive-restructure-pressure or steady).

## §8 Honest limits at close

1. **MCP stdio transport remains unverified in-session.** Same limit as S051/S052/S053 close §8. `ToolSearch` for `mcp selvedge retrieval` at S054 did not surface `mcp__selvedge_retrieval__*` tools in this Claude Code session; substrate use was via `.cache/venv/bin/python` direct SQL + FastMCP `tool_manager` introspection. The new `forward_references` tool's MCP-stdio behaviour is inferred from the FastMCP tool-registration path used by `search` and `resolve_id` (which are themselves never directly exercised over stdio in self-dev sessions per the same chain of honest limits). Inference is sound but unverified.

2. **`_ID_TOKEN_RE` curated set is not exhaustive.** The regex matches D-NNN, OI-NNN, WX-N-N, EF-NNN-..., engine-vN, §N(.N)*(-MN)?, d01N_N. Identifiers outside this family (generic word-hyphen-word like `phase-2`, `cross-family`, `non-Claude`) still trigger the fallback path in `search()`. Smoke-test 4 (`WX-50-1 phase-2 gate`) demonstrates this: the fallback succeeds without crash but loses BM25 ranking precision (whole-query phrase-wrap). Acceptable per the EF-053 record's own scope ("the ID regex family"); broader coverage can be added if friction reappears.

3. **`forward_references` observational value unproven at S054.** S054 implements + smoke-tests the tool but does not exercise it in routine session-open audit (which would be S055+ behaviour per the paired `prompts/development.md` amendment). The empirical demonstration that the tool catches missed forward-commitments will require S055+ practice. The S054 smoke-test demonstrates the tool works (returns expected counts; handles unindexed targets cleanly) but does not demonstrate that it is operationally valuable in the agent workflow.

4. **`forward_references` query expands EF-054 inbox baseline.** The inbox record's empirical demonstration used `WHERE id_text='S053'` (returning 19 records). My implementation uses `id_text = ? OR canonical = ?` (returning 40+ records for `S053`). The `OR canonical = ?` clause makes the tool more useful for surface-form-variant matching but is a mild scope-expansion documented for transparency. If it proves noisy, future tuning can narrow to id_text-only.

5. **`prompts/development.md` amendment is engine-definition file edit but classified minor.** Per `engine-manifest.md` §5, minor elaborations within scope do not bump engine-v. The amendment names a new tool that's available; does not redefine the Read activity. Classification minor per OI-002 17th data point. The classification could be challenged retroactively if the named tool ends up shaping read-discipline materially over multiple sessions; observation-window candidate.

6. **Forward-commitment relay still depends on close-narrative discipline.** EF-054 Direction A surfaces an MCP tool that lets agents query for forward-commitments at session open; it does NOT change the upstream discipline that close-narrative §7 should enumerate forward-commitments accurately. The S053 EF-054 demonstration showed two P1-raw commitments (Criterion 3 rebuild-latency, Criterion 6 adoption-sunset) were silently dropped. The new tool catches the gap structurally; the upstream discipline remains a separate concern. Not addressed at S054.

7. **Path T+L reification at n=2 with multi-intake extension is a sub-pattern.** S052 was Path T+L with 1 record. S054 is Path T+L with 2 records. The pattern-name remains "Path T+L"; the n-counter advances by 1 (not 2) per `provenance/051-session/03-close.md` §10 reification convention. The multi-intake variant is a new sub-pattern at first-instance; reification deferred to n=2.

8. **Smoke-test bias toward known-good queries.** Tests cherry-picked to demonstrate fix, not exhaustive against query-class space. Sufficient for source-realignment confidence at minor classification; not a substitute for organic use over multiple sessions. EF-053 Direction A could exhibit unexpected behaviour for query forms not exercised at S054; if so, future engine-feedback intake captures the next iteration.

9. **Index rebuild during smoke-test is a side-effect of the workflow, not a contract violation.** Substrate's session-open mtime check (per retrieval-contract.md v1 §4) triggered automatically when the smoke-test imported `build_server` (via the `ensure_index` pre-flight). The rebuild is normal substrate behaviour and preserves the contract. Recorded transparently because the rebuild count in the smoke-test summary (461 docs / 51,724 identifiers) is post-rebuild, not pre-S054 baseline.

10. **Operator framing about "do not introduce queries rather add MCP features" is honoured per direction recorded in workspace artefacts (post-S053 commit message + EF-054 inbox record), not in operator session input at S054 open.** I'm treating this as durable direction (operator's stance recorded in workspace artefacts) rather than session-open Halt input. If the operator's S054 actual stance differs, the Direction A choice is the one reversible element (new decision in subsequent session could supersede). The Direction B/C alternatives are preserved in the EF-054 inbox + triage record for re-evaluation.

11. **`prompts/development.md` amendment placement chosen without committee.** I placed the new paragraph immediately after the inbox-triage clause at line 21-23 of the prompt, on grounds of topical adjacency (forward_references is a session-open diagnostic; the paragraph above mentions inbox triage which is also a session-open consideration). An alternative placement could be later in §How to operate after the "do prior provenance consultation" clause. Single-orchestrator decision; no deliberation; if the placement proves awkward in S055+ practice, future minor amendment can relocate.

## §9 Aggregate default-read surface impact at close

Pre-close aggregate (at S054 open per validator): **74,449 words across 21 files** (matches S053 close state).

**Actual post-close per validator** (run mid-finalisation before SESSION-LOG row finalisation; will re-run post-commit for record): **74,994 words across 21 files** → +545 words net. Under §2b 90K soft with comfortable ~15,006 words headroom.

Breakdown of actual delta:
- Close-rotation: S048 close rotates OUT; S054 close enters. Net close-rotation delta ~+400 words (close 4,270 vs S048 close estimate ~3,800).
- `SESSION-LOG.md` growth: actual ~+540 words (S054 row substantially exceeded Q5=(a) ≤180-word target per content-adaptive density precedent given the four-decision two-record-resolution scope). Total SESSION-LOG.md now 5,994 words; ~6 words headroom to 6K soft (forecast 5,910 / ~90 headroom; forecast underestimated row size).
- `prompts/development.md` growth: ~+105 words (added paragraph; was ~1,640; now 1,745).
- `engine-feedback/INDEX.md` growth: ~+100 words (status summary + 2 row dispositions with full narratives).
- Other small adjustments: 0.

Forecast error per WX-22-1 honest-limits discipline: forecast +400 net; actual +545. Drivers: (a) SESSION-LOG row underestimated by ~360 words (forecast ~180; actual ~540); (b) close size underestimated by ~370 (forecast ~3,900; actual 4,270). Recorded transparently per S053 close §9 precedent ("Forecast error: estimated -7,020 net; actual is +2,117. Recorded transparently per WX-22-1 honest-limits discipline; content-adaptive density for substantive content justifies the larger-than-target sizes").

Content-adaptive density justification for S054 specifically: four decisions (vs S053's two) + two record resolutions (vs S053's zero) + smoke-test summaries (10+4+7 cases across two fixes) + new tool surface documentation (forward_references) + WX-34-1 narrowing observation. The thin-index discipline does not preclude variable-length rows for substantively variable sessions per `workspace-structure.md` v6 §SESSION-LOG content-adaptive principle.

During-session max: `00-assessment.md ~3,400` + `02-decisions.md ~3,500` + `03-close.md 4,270` = ~11,170 words default-read while session open (per read-contract v5 §1 item 8); these rotate to archive-surface post-close except `03-close.md` which enters the 6-session retention window. Mid-session validator run would therefore show ~86K; terminal close-state actual 74,994.

WX-34-1 narrowing observation forward: SESSION-LOG.md is now 5,994 / ~6 words from 6K soft. S055 close will likely trigger the soft warning. Per WX-34-1 standing convention, soft warning is informational; a hard-ceiling breach (>8,000 words) would trigger forced-restructure per S051 D-178 precedent. Estimated at ≈540 words/session row growth, hard ceiling would trigger at ~S058 close; preemptive restructure candidate at S055/S056 close before then.

## §10 S054 meta-observations

1. **First session to resolve two engine-feedback records same-session.** S048 resolved one (EF-001) + scheduled three (EF-047×3); S052 resolved one (EF-051); S054 resolves two (EF-053 + EF-054). Multi-intake same-session resolution as a sub-pattern within Path T+L is first-instance at S054; reification deferred to n=2.

2. **Substrate defect-surface-and-resolve cadence has converged on a stable shape.** S050 = adoption baseline; S051 = first-real-use surfaces alias-indirection defect (EF-051); S052 = resolve EF-051; S053 = WX-50-1 final-recording surfaces query-parser defect (EF-053) + post-session operator surfaces forward-reference gap (EF-054); S054 = resolve both. The substrate is operationally mature enough to be used routinely; defects are surfaced and resolved on a session-or-two cadence; preservation cost is bounded; Triage cost is bounded. Pattern is sustainable for the foreseeable horizon.

3. **EF-054 records the first operator-surfaced engine-feedback intake originating from a self-dev workspace post-session observation.** Prior intakes: EF-001 (external-workspace-originated S048); EF-047×3 (self-dev-originated S047 from arc-plan design work); EF-051 (self-dev-originated S051 from substrate smoke-test); EF-053 (self-dev-originated S053 from due-diligence); EF-054 (self-dev-originated S053-post-session from operator observation). EF-054 is the first `reported_by: operator` record (the others are `reported_by: application-agent`). This is a normal use of the engine-feedback pathway and does not require process amendment.

4. **`forward_references` is a step toward partial automation of session-open commitment audit without crossing into substrate-as-source-of-truth (which §10.4-M10 Substrate-N2 minority preserves as a multi-session arc).** The tool exposes the existing `identifiers` table data without reframing what's source-of-truth. Markdown remains canonical; the tool is a read-side diagnostic. No phase-2 commitment, no engine-v bump, no methodology amendment.

5. **Twenty-seventh-consecutive housekeeping `[none]`-trigger decision pattern.** Pattern stably instantiated across the engine. Forward observation: the `[none]` housekeeping pattern is engine-conventional and does not need formalisation as a discipline.

6. **Engine-v9 preservation window count 4 — modest but not anomalous.** Engine-v9's trajectory: substrate-adoption-plus-four-observation-and-routine-use sessions. Engine-v9 is in steady-state organic-use territory now. Future depth depends on operator surfacing (engine-v10 from any direction) or post-arc review.

7. **EF-053 fix's fallback path was useful instrumentation.** The whole-query-phrase-wrap fallback was originally a workaround for the missing query-sanitization. After the EF-053 fix, the fallback is repurposed as a defensive last-ditch for hyphen forms outside `_ID_TOKEN_RE` coverage (e.g., `phase-2`, `cross-family`). The fallback was already there; my change reordered it from primary path to defensive path. This is a kind of "code refactoring without semantic change" within the source-realignment discipline; recorded for future reference.

## §11 Commit and close

This close file is committed with the S054 artefacts:
- `provenance/054-session/00-assessment.md` (pre-work commit `4f698c7` already done).
- `provenance/054-session/02-decisions.md` (this close commit).
- `provenance/054-session/03-close.md` (this file; this close commit).
- `tools/retrieval_server.py` (D-186 `_sanitize_query` + D-187 `forward_references`; this close commit).
- `prompts/development.md` (D-187 paired documentary amendment; this close commit).
- `engine-feedback/triage/EF-053-search-query-parser-unquoted-hyphen-fts5-not-operator.md` (this close commit).
- `engine-feedback/triage/EF-054-forward-reference-mcp-tool-for-session-open-commitment-audit.md` (this close commit).
- `engine-feedback/INDEX.md` (status summary 2-new → 0-new + 4-resolved → 6-resolved + 2 row dispositions; this close commit).
- `SESSION-LOG.md` (S054 thin row append; this close commit).

Engine-v9 stands. 36 first-class minorities preserved. 13 active OIs. Engine-feedback state 2 new / 1 triaged / 4 resolved → **0 new** / 1 triaged / **6 resolved** / 0 rejected (EF-053 + EF-054 both resolved). Path T+L reified at n=2 (S052 first-instance + S054 second-instance) with first-instance multi-intake same-session resolution sub-pattern. WX-34-1 remediation preserved. Substrate defect-surface-and-resolve cadence stable; phase-1 tools improved on two dimensions (query-parser correctness + forward-reference diagnostic surface). D-129 ninth-consecutive + D-138 ninth-consecutive clean exercises.
