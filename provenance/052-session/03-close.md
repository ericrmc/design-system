---
session: 052
title: Close — Path T+L (Triage-classify + minor Path L implementation fix) first-instance for EF-051 (aliases.yaml not consulted at query time); Direction B adopted via tools/retrieval_server.py Strategy 1.5 + load_aliases_map() + degraded-mode disclosure; smoke-test 8-of-8 PASS (5 alias-indirection + 2 direct-canonical + 1 None-case); three decisions D-180 Path T+L ratification + D-181 Direction B adoption + D-182 housekeeping (14 sub-sections); engine-v9 preserved preservation window count 1→2; Path T reified at n=2 (S048 + S052); Path T+L bundled label first-instance reification-deferred-until-n=2; EF-051 inbox→triaged→resolved lifecycle complete within single session; engine-feedback state 1 new / 1 triaged / 3 resolved → 0 new / 1 triaged / 4 resolved; 36 first-class minorities preserved unchanged; 13 active OIs unchanged; WX-24-1 MAD v4 25-session no-growth new record; WX-28-1 twenty-second close-rotation zero retention-exceptions (S046 rotates OUT); WX-50-1 phase-2 gate Condition 1 arguable-satisfied-pending-operator-interpretation (7 results_used entries at S052 all from smoke-test); WX-34-1 remediation preserved (SESSION-LOG ≈5000 words post-thin-row); D-129 seventh-consecutive clean exercise + D-138 seventh-consecutive folder-name default; seventh minor bug-fix-style source-realignment per OI-002 precedent chain (S022/S030/S033/S040/S046/S051/S052)
date: 2026-04-25
status: complete
---

# Close — Session 052

## §1 Artefacts produced

### §1a Provenance (`provenance/052-session/`)

- `00-assessment.md` (2,400 words; commit `bcdbc0c`) — pre-work commit per D-017 spirit + S048/S049/S050/S051 precedent chain. Proposed Path T+L for EF-051 resolution; §3b technical verification of defect across both implementation layers; §4a D-129 seventh-consecutive exercise with five considered-and-rejected non-Path-T+L alternatives; §4b Direction B selection rationale; §4c classification minor per OI-002 per seventh source-realignment precedent chain; §5 twelve-step work plan; §7 Halt 1 default-ratified per operator "do not halt".
- `02-decisions.md` (~4,000 words; this close commit) — three decisions: D-180 Path T+L ratified `[none]` single-agent reason; D-181 Direction B adopted for EF-051 `[none]` minor implementation edit to `tools/retrieval_server.py`; D-182 housekeeping `[none]` with 14 sub-sections a–n.
- `03-close.md` — this file.

No `STATUS.md` (single-orchestrator). No `01-brief-shared.md` / `01X-perspective-*.md` / `01-deliberation.md` / `manifests/` / `participants.yaml` (no MAD convened; Path T+L is single-orchestrator per D-180). No archive subdirectories (no current-session raw exceeds 8K hard ceiling). No external artefact in self-dev.

### §1b Specification changes THIS session

**None.** No engine-definition specification edited. Per D-181 classification, the fix is engine-adjacent implementation realignment to already-specified contract (retrieval-contract.md v1 §2.2). No v-bump on any spec; no engine-v bump; seventh minor bug-fix-style source-realignment per OI-002 heuristic.

All active specs remain at their S051-close versions: `PROMPT.md` unchanged; `MODE.md` unchanged; `prompts/development.md` unchanged; `prompts/application.md` unchanged (v8 from S048); `methodology-kernel.md` v6 unchanged; `multi-agent-deliberation.md` v4 unchanged; `validation-approach.md` v5 unchanged; `workspace-structure.md` v6 unchanged (from S050); `identity.md` v2 unchanged; `reference-validation.md` v3 unchanged; `read-contract.md` v5 unchanged; `retrieval-contract.md` v1 unchanged; `engine-manifest.md` unchanged; `specifications/aliases.yaml` schema_version 1 unchanged; `.mcp.json` unchanged; `tools/validate.sh` unchanged; `tools/build_retrieval_index.py` unchanged; `tools/bootstrap-external-workspace.sh` unchanged.

### §1c Development-provenance files amended (WX-35-1 claim discipline)

Per WX-35-1 standing discipline, each claimed file amendment is verified via `git log --oneline <path>` at close and explicitly retracted if not committed.

- **`tools/retrieval_server.py`** — **EDITED this close commit**. Direction B implementation per D-181: (a) `import yaml` with ImportError-tolerant fallback added at top; (b) `load_aliases_map(workspace: Path) -> dict` module-level function added; (c) in `build_server()`, `aliases_map` + `aliases_available` + `aliases_present` loaded once at server startup; (d) Strategy 1.5 inserted between Strategy 1 and Strategy 2 in `resolve_id()`; (e) `_match_payload` signature extended with `degraded: bool` + `missing: list | None` defaults; (f) degraded-mode disclosure in no-match return now reports accurate `missing` list; (g) Strategy 2 inline comment updated to describe current behaviour accurately; (h) no-match `reason` string updated to `"no match in identifiers table or aliases.yaml"`. Net diff: ~60 lines added/modified out of ~290-line file.
- **`engine-feedback/INDEX.md`** — **EDITED this close commit**. Status summary: 1 new / 1 triaged / 3 resolved / 0 rejected → **0 new / 1 triaged / 4 resolved / 0 rejected**. EF-051 row `status: new` → `status: resolved (S052 D-180 + D-181)`; OI/Disposition column rewritten to reflect Direction B adoption + smoke-test 8-of-8 PASS + Direction A deferred as optional additive; triage-link added to first column.
- **`engine-feedback/triage/EF-051-aliases-yaml-not-consulted-at-query-time.md`** — **CREATED this close commit**. Triage record per `workspace-structure.md` v6 §engine-feedback triage schema with `status: resolved`, `classification: minor`, `decision_records: [D-180, D-181]`, `engine_version_impact: engine-v9 preserved`, `direction_selected: B`, `alternative_directions_deferred: [A]`. Body: §Classification + §Defect summary + §Adoption §Direction B + §Smoke-test evidence + §Classification minor per OI-002 + §Direction A deferred + §Forward observations + §OI impact + §Subsumed deferred candidates.
- **`SESSION-LOG.md`** — **EDITED at close** (S052 thin row appended per Q5=(a) ≤180-word target).
- **`provenance/052-session/00-assessment.md`** — **CREATED** (commit `bcdbc0c` pre-work).
- **`provenance/052-session/02-decisions.md`** — **CREATED this close commit**.
- **`provenance/052-session/03-close.md`** — **CREATED this close commit** (this file).
- **`specifications/*.md`** — **NOT edited** per WX-35-1 explicit retraction. No spec edit this session per §1b.
- **`specifications/aliases.yaml`** — **NOT edited** per WX-35-1 explicit retraction. Schema unchanged; seed entries unchanged.
- **`specifications/engine-manifest.md`** — **NOT edited** per WX-35-1 explicit retraction. No engine-v bump (minor per OI-002).
- **`tools/validate.sh`** — **NOT edited** per WX-35-1 explicit retraction. No new check; no constant change.
- **`tools/build_retrieval_index.py`** — **NOT edited** per WX-35-1 explicit retraction. Direction B is a server-only fix (Direction A would edit the indexer; Direction A not adopted this session).
- **`tools/bootstrap-external-workspace.sh`** — **NOT edited** per WX-35-1 explicit retraction. No bootstrap-contract change.
- **`.mcp.json`, `.gitignore`** — **NOT edited** per WX-35-1 explicit retraction.
- **`open-issues/*.md`** — **NOT edited** per WX-35-1 explicit retraction. No OI opened/resolved/amended this session; 13 active OIs unchanged. EF-051 did not promote to OI (classification minor per OI-002; implementation-level fix self-contained).
- **`open-issues/index.md`** — **NOT edited** per WX-35-1 explicit retraction.
- **`PROMPT.md`, `MODE.md`, `prompts/development.md`, `prompts/application.md`, `CLAUDE.md`** — **NOT edited** per WX-35-1 explicit retraction.
- **`engine-feedback/inbox/EF-051-*.md`** — **NOT edited** per `workspace-structure.md` v6 §engine-feedback "intake files preserved verbatim" convention; `status: inbox` frontmatter unchanged; lifecycle state carried by triage file + INDEX.md.
- **`.cache/venv/`** — **PRE-EXISTING mid-session use** (gitignored; not committed). S051-created venv re-used this session for smoke-test python invocation.
- **`.cache/retrieval.db`** — **PRE-EXISTING mid-session use** (gitignored; not committed). S051-built 34.1 MB SQLite DB unchanged at S052 (Direction B is query-time fix not requiring rebuild).

### §1d Validator status at close

Actual validator state at close (post-edit + triage record + INDEX update + SESSION-LOG thin-row): to be recorded post-commit. Forecast: **1224+ PASS / 0 FAIL / 10–12 WARN → PASS**.

- Aggregate default-read surface: forecast ~70–71K words across 20 files (close-rotation S046 OUT; S052 enters; net aggregate approximately neutral). Under §2b 90K soft with comfortable headroom.
- SESSION-LOG.md post-thin-row: ~5,000 words (well under 6K soft; well under 8K hard). WX-34-1 remediation preserved.
- Check 20 per-file: PASS (unchanged).
- Check 20 aggregate: PASS (unchanged).
- Check 21 archive-pack manifest integrity: PASS on existing archive-packs (no new archive-pack this session).
- Check 22 archive-pack citation consistency: PASS on existing citations.
- Check 23 MODE.md presence: PASS.

Expected 10–12 warnings breakdown:
- 2 spec soft-warnings (`multi-agent-deliberation.md` 6,637 words + `reference-validation.md` 7,160 words; both designed per S024 A.4 + S033 carry-forward; unchanged from S052 open).
- 8 pre-existing "no rejected alternatives found" design-intent warnings across S046/S047/S048/S051 `02-decisions.md` files (unchanged from S052 open).
- 0–2 new "no rejected alternatives" warnings for S052 `02-decisions.md` D-180 + D-182 which reference alternatives cross-file to 00-assessment §4a rather than listing per-decision (validator regex matches per-decision bodies). D-181 DOES list alternatives inline; likely 0–1 warnings attributable to S052 decisions.

### §1e Engine-version status THIS session

**Engine-v9 preserved** at S052 close; preservation window count **1 → 2** (S051 first post-v9 + S052 second post-v9). Engine-v9 established S050 per D-172; no engine-v bump this session. §5.4 cadence minority does not re-escalate (non-bump session; precedent chain v5–v9 intact).

## §2 Operational warrants changed or advanced

1. **EF-051 inbox→triaged→resolved lifecycle complete within single session.** Second-ever complete inbox→triage→resolved lifecycle within a single session (S048 EF-001 was first; S052 EF-051 is second). First-ever for self-dev-originated defect (EF-001 originated in external workspace; EF-051 originated in self-dev substrate-smoke-test). Lifecycle schema at `workspace-structure.md` v6 §engine-feedback continues operational; no structural retrofit required.
2. **Path T reified at n=2.** S048 first instance (EF-001 + EF-047 triage) + S052 second instance (EF-051 triage). Path T is now a reified default-agent path-label for inbox-triage default-agent sessions. Forward-naming convention: path-labels reify at n=2 (S051 Path L+A precedent).
3. **Path T+L bundled label first-instance at S052.** Combining Path T (triage-classify) + Path L (minor implementation fix) in a single session as "T+L" is a new bundled forward-naming candidate. Reification deferred until n=2. If a future session bundles triage + same-session implementation fix with recognisable T+L shape, the bundled label reifies.
4. **WX-50-1 phase-2 gate second-session 3-field recording.** See §6 below for full payload. Condition 1 arguable-satisfied-pending-operator-interpretation (7 `results_used` entries at S052 all from smoke-test); Conditions 2 + 3 not satisfied. Gate firing determined at S053 close per operator interpretation.
5. **Substrate-smoke-test pattern vindicated a second time.** S050 §8 forward-commitment (code-review-only at adoption + first-real-use at next-session + defect-surfaces-as-engine-feedback-intake) exercised at S050→S051 first (surface EF-051) + S051→S052 second (resolve EF-051). Pattern repeatable for future substrate adoptions that defer smoke-testing to the next session.
6. **D-129 standing discipline seventh-consecutive clean exercise.** Five considered-and-rejected non-Path-T+L alternatives in `00-assessment.md` §4a per standing discipline since S046 D-146. §5.12 Path-Selection Defender reopen warrant (a) does not fire.
7. **D-138 folder-name default seventh-consecutive clean exercise.** `provenance/052-session/` no suffix, no slug. S046/S047/S048/S049/S050/S051/S052 all clean.
8. **WX-28-1 twenty-second close-rotation zero retention-exceptions.** S046 rotates OUT at S052 close; S052 close enters. Retention window post-rotation: S047/S048/S049/S050/S051/S052. Streak continues well past S038 10-of-10 vindication threshold.
9. **WX-24-1 MAD v4 twenty-fifth-session no-growth streak new record.** `multi-agent-deliberation.md` v4 stable at 6,637 words. New record from the S042 reset point (S043–S052 all no-growth).
10. **WX-34-1 remediation preserved.** SESSION-LOG.md post-thin-row: ~5,000 words (under 6K soft warning). Compression at S051 holds; no new pressure.
11. **§10.4-M2 (Skeptic-preserver premature-feedback-pathway) continued preservation.** Pathway exercised further at EF-051 triage + resolution without structural retrofit. Continued preservation consistent.
12. **Degraded-mode disclosure per retrieval-contract v1 §3 clause 3 now actually fires.** Pre-S052, `degraded: false` was hardcoded in `_match_payload`; `missing: []` was always empty. S052 implementation reports `degraded: true` + `missing: ["pyyaml"]` or `["specifications/aliases.yaml"]` when the alias-support dependencies are missing. Small sub-fix within D-181; no separate decision record.
13. **No new first-class minority preserved.** Single-orchestrator Path T+L; no deliberation; no dissent surface. 36 minorities preserved unchanged.
14. **20 alias-to-canonical mappings observed** loaded from 8 canonical entries in `specifications/aliases.yaml`. This is a factual observation for documentation; EF-051's original description of "8 seed entries" referred to the 8 canonical rows in aliases.yaml; the full alias fan-out is 20 mappings across those canonicals.

## §3 Engine-v disposition and preservation depth

**Engine-v9 preserved at S052 close; preservation window count = 2.**

S052 is the second post-engine-v9 session. Engine-v9 established at S050 per D-172 (MAD-adopted new engine-definition spec bump-provenance class). §5.4 cadence minority does not re-escalate (non-bump session; precedent chain v5–v9 intact).

Forward observation: engine-v9 preservation window will close at depth TBD. Candidate triggering events:
- Phase-2 substrate extensions per WX-50-1 firing (gate evaluation at S053 close or operator-defined later point) would produce engine-v10 at that phase-2 adoption session.
- Post-arc `selvedge-disaster-response` review triggering any of S047 D-150 three deferred candidates (i)/(ii)/(iii) adoption could produce engine-v10.
- EF-051 resolution at S052 is classified minor per OI-002 per the bug-fix-style precedent chain; no engine-v bump.

## §4 Preserved first-class minorities at S052 close

**36 first-class minorities preserved engine-wide at S052 close** — unchanged from S051. No new minority preserved; no minority discharged; no minority activated.

Full enumeration in `specifications/workspace-structure.md` v6 §10.4 (M1–M11) + §5.1/§5.4/§5.5/§5.6/§5.7/§5.8/§5.9/§5.10/§5.11/§5.12/§5.13/§5.14 + Session 024 A.4 four minorities + Session 027 §A/§B/§C + existing preserved-minorities in `reference-validation.md` v3 §10.1/§10.2/§10.3 + `retrieval-contract.md` v1 §7.1–§7.5 (mirrored with workspace-structure §10.4-M7–M11).

## §5 Watchpoints status at S052 close

- **WX-24-1** — MAD v4 stable 6,637 words. **Twenty-fifth-session no-growth streak** (S043–S052). New record from S042 reset point.
- **WX-24-3** — reference-validation label discipline n=8 stable.
- **WX-27-1** — stable.
- **WX-28-1** — **twenty-second close-rotation** (S046 rotates OUT; S052 enters); zero retention-exceptions. Streak continues well past S038 10-of-10 vindication threshold.
- **WX-33-2** — reference-validation.md v3 7,160 words stable.
- **WX-34-1** — **remediation preserved** per §2 Observation 10 above. SESSION-LOG at ~5,000 words post-thin-row; no new breach pressure.
- **WX-35-1** — standing discipline applied cleanly; explicit retractions recorded in §1c.
- **WX-43-1** — cumulative baseline n=6-of-8 + explicit-instruction variant n=0-of-9 (S047+S049+S050+S051+S052). OI-promotion discharged-as-not-warranted per S050 D-176. S052 is second post-discharge data point; no sub-agents convened this session; cumulative n unchanged.
- **WX-44-1** — codex-CLI independence-phase breach n=3 across S044+S045+S047. Not exercised this session (no codex invocation). Forward-convention candidate held cleanly at S052 by trivial non-exercise.
- **WX-44-2** — codex CLI model-version-drift discipline: not exercised this session.
- **WX-47-1** — codex-CLI argv `---` YAML parsing fragility: not exercised this session.
- **WX-50-1** — **second-session 3-field recording executed** per §6 below. Phase-2 gate Condition 1 arguable-satisfied-pending-operator-interpretation (7 `results_used` entries at S052 all from smoke-test); Conditions 2 + 3 not satisfied. Evaluation continues at S053.

## §6 Retrieval substrate use (WX-50-1)

Per `retrieval-contract.md` v1 §6, every session close S050 through S053 records substrate use in 3 fields. S052 is the second session with non-baseline-zero entries.

**`tool_calls_by_type`**: `{search: 0, resolve_id: 7}`.

All 7 `resolve_id()` invocations this session were to the substrate at `.cache/retrieval.db` via the S051-created `.cache/venv/` python (not via MCP stdio transport — workspace Claude Code session does not have `selvedge-retrieval` MCP server connected; ToolSearch did not surface `mcp__selvedge_retrieval__*` tools). The 7 invocations were all part of the EF-051 fix smoke-test:

1. `resolve_id("M5")` → `§10.4-M5` (alias-indirection via new Strategy 1.5) at `specifications/retrieval-contract.md:40`.
2. `resolve_id("Reviser OI-tag-only")` → `§10.4-M5` (alias-indirection) at `specifications/retrieval-contract.md:40`.
3. `resolve_id("Decision 172")` → `D-172` (alias-indirection) at `specifications/engine-manifest.md:23`.
4. `resolve_id("phase-2 gate")` → `WX-50-1` (alias-indirection) at `specifications/engine-manifest.md:175`.
5. `resolve_id("OI 19")` → `OI-019` (alias-indirection) at `specifications/reference-validation.md:316`.
6. `resolve_id("D-172")` → `D-172` (direct-canonical via unchanged Strategy 1) at `specifications/engine-manifest.md:23`.
7. `resolve_id("§10.4-M5")` → `§10.4-M5` (direct-canonical) at `specifications/retrieval-contract.md:40`.

Plus one no-match verification: `resolve_id("NONEXISTENT-999")` → None (per §2.2 "Never raises on unknown alias"). Not counted in `tool_calls_by_type` if "calls that return match" is the counter; recorded in sprit of transparency: 7 match-returns + 1 None-return = 8 total invocations.

**`results_used_with_artefact_id`**:

All 7 match-returning invocations have artefact paths attested by the smoke-test and were used in D-181's rationale citation of "smoke-test 8-of-8 PASS". Per retrieval-contract v1 §6 `results_used` shape `{tool, query, returned_artefact_path, used_in_decision_or_oi_or_minority_id}`:

1. `{tool: "resolve_id", query: "M5", returned_artefact_path: "specifications/retrieval-contract.md:40", used_in: "D-181 §Smoke-test evidence (PASS via alias-indirection)"}`.
2. `{tool: "resolve_id", query: "Reviser OI-tag-only", returned_artefact_path: "specifications/retrieval-contract.md:40", used_in: "D-181 §Smoke-test evidence (PASS via alias-indirection)"}`.
3. `{tool: "resolve_id", query: "Decision 172", returned_artefact_path: "specifications/engine-manifest.md:23", used_in: "D-181 §Smoke-test evidence (PASS via alias-indirection)"}`.
4. `{tool: "resolve_id", query: "phase-2 gate", returned_artefact_path: "specifications/engine-manifest.md:175", used_in: "D-181 §Smoke-test evidence (PASS via alias-indirection)"}`.
5. `{tool: "resolve_id", query: "OI 19", returned_artefact_path: "specifications/reference-validation.md:316", used_in: "D-181 §Smoke-test evidence (PASS via alias-indirection)"}`.
6. `{tool: "resolve_id", query: "D-172", returned_artefact_path: "specifications/engine-manifest.md:23", used_in: "D-181 §Smoke-test evidence (PASS via direct-canonical)"}`.
7. `{tool: "resolve_id", query: "§10.4-M5", returned_artefact_path: "specifications/retrieval-contract.md:40", used_in: "D-181 §Smoke-test evidence (PASS via direct-canonical)"}`.

**`fallbacks_due_to_missing_capability`**: `[]` — none recorded this session. The EF-051 alias-indirection fallback recorded at S051 is **resolved** at S052 by D-181; no new fallback category surfaces.

**Phase-2 gate status after S052**:
- Condition 1: ambiguous-pending-operator-interpretation. S051 + S052 are the ≥2 sessions with ≥1 `results_used` entry each, BUT S052's entries are all from smoke-test. If smoke-test invocations count, Condition 1 satisfies; if they do not, Condition 1 is unsatisfied and evaluation continues at S053.
- Condition 2: not satisfied. No structured-filter or graph-traversal fallback recorded at S050/S051/S052.
- Condition 3: not satisfied. No external-workspace substrate adoption.

**Gate status at S052 close**: unfired conservatively; fired under permissive counting rule. Operator-authoritative per retrieval-contract v1 §6 closing paragraph.

**Note on counting methodology conservatism** (WX-50-1 forward observation): honest-limit of this session is that the 7 `results_used` entries here are artefacts of smoke-testing a specific fix rather than organic session-work retrieval. A stricter counting rule would require "≥2 sessions record ≥1 entry used to produce decision content that could not have been produced without the substrate"; under that rule, S051 contributes but S052 does not (the fix itself is the decision; verification is via any mechanism). Recorded transparently; operator decides at phase-2 MAD time or S053 close.

## §7 Next-session items and forward observations

**Session 053 recommendation**: default-agent session. Priorities:

- **WX-50-1 final recording session** (third-and-last of three post-S050 observation sessions). If S053 substantive work uses substrate in MCP-transport normal-session-work flow, Condition 1 satisfies unambiguously via S051 + S053 (S052 ambiguity becomes moot). If S053 does not use substrate in normal flow, operator-interpretation question becomes load-bearing at S053 close Case-Steward call.
- **Inbox check at open**: engine-feedback/inbox/ has 0 new records at S052 close. If operator transports new records from external workspace or surfaces new self-dev defect between sessions, S053 may adopt Path T.
- **External-application arc progression**: `selvedge-disaster-response` arc S002–S005 pending operator transport; substrate available via bootstrap-refresh (operator-discretionary). Substrate at external workspace does not yet include Direction B fix (external workspace inherited pre-S052 substrate at S046 D-142 bootstrap; operator-mediated transport of the S052 `tools/retrieval_server.py` update into external workspace is a between-sessions operator action).
- **Post-arc self-dev review obligation** (carrying from S047 D-150): three remaining deferred spec-amendment candidates (i)/(ii)/(iii) preserved for post-arc review. Unchanged at S052.

**S053 close should evaluate**:
- WX-50-1 phase-2-gate firing decision (operator-authoritative; may require phase-2 MAD session).
- Engine-v9 preservation (window count would reach 3 if S053 preserves).
- D-129 eighth-consecutive exercise.
- D-138 eighth-consecutive folder-name default.
- §5.6 GPT-family-concentration fifth-consecutive observation if MAD convenes; else N/A.
- WX-28-1 twenty-third close-rotation (S047 rotates OUT; S053 enters).
- WX-24-1 MAD v4 twenty-sixth-session no-growth (if no MAD edit).

## §8 Honest limits at close

- **Smoke-test exercised core SQL paths directly, not via MCP stdio transport.** Same limit as S051: workspace Claude Code session lacks MCP server connection. The D-181 implementation edit is verified at SQL-contract layer; MCP stdio wiring (FastMCP server startup + tool registration + JSON-RPC transport) is not smoke-tested this session. MCP transport verification deferred to a session where the MCP server is connected OR operator runs the server explicitly.
- **Re-used S051-built `.cache/retrieval.db`** (34.1 MB; 448 docs / 48,852 identifiers). Direction B is a query-time fix; DB rebuild is not required for correctness. However, any subsequent smoke-test would need to rebuild if aliases.yaml changes (aliases.yaml changes are picked up at server restart under Direction B, but the DB itself is rebuilt only on mtime-staleness of *.md files; aliases.yaml is a *.yaml file not *.md so it doesn't trigger mtime-rebuild — forward observation, not this-session defect).
- **Aliases.yaml mtime-watcher is not implemented in Direction B.** Server restart required to pick up aliases.yaml changes. Acceptable at phase-1 per operator discretion; phase-2+ may add hot-reload if desired. Not a contract violation (retrieval-contract v1 does not require aliases.yaml to trigger rebuild; §4 rebuild-trigger is scoped to markdown mtime).
- **Condition 1 phase-2 gate firing is ambiguous-pending-operator-interpretation.** All 7 `results_used` entries at S052 are from smoke-test rather than organic session-work retrieval. Recorded transparently in §6 + D-182h; decision deferred to operator.
- **Direction A remains available as optional additive.** Not adopted this session; not foreclosed. If a future session surfaces need for alias-text FTS search (e.g., `search("Reviser OI-tag-only")` returning the canonical's location via BM25 scoring rather than just alias-indirection via resolve_id), Direction A is the repair path.
- **`resolve_id("NONEXISTENT-999")` test** counted as 1 invocation in the 7-count of `tool_calls_by_type`? Answer: no. The 7 counts match-return invocations only; the None-case is additional. Total 8 invocations of which 7 produced matches. Recorded per-interpretation transparency.
- **Validator at close not yet recorded**; to be recorded post-commit. Expected PASS.
- **Self-ratification of Direction B selection.** Operator said "do not halt"; selection was made by Case Steward per `00-assessment.md` §4b rationale. If operator at a future session prefers Direction A or both, the edit is reversible (Strategy 1.5 can be removed; Direction A is additive-compatible).
- **Assessment commit was `bcdbc0c`** (provenance/052-session/00-assessment.md) pre-work. Per WX-35-1 claim-discipline audit: file was actually committed at `bcdbc0c`; claim stands verified.
- **S052 thin-row in SESSION-LOG.md** targeted ≤180 words per S050/S051 precedent; actual word-count to be verified at commit.

## §9 Aggregate default-read surface impact at close

Pre-close aggregate (per S051 close §9 forecast): ~68,765 words across 20 files (actual post-S051-close value per validator at open: 71,061 words / 21 files — the S051 forecast was conservative; actual was slightly higher due to close-rotation mechanics).

S052 changes:
- `tools/retrieval_server.py` edit: ~60 LOC added; adds no new default-read-enumerated file. `tools/*` is not in read-contract v5 §1 default-read enumeration (only engine-manifest-listed `tools/validate.sh` is default-read by proxy; `retrieval_server.py` is engine-adjacent per D-170 not engine-definition).
- `engine-feedback/INDEX.md` edit: ~50 net words added (EF-051 row rewrite + status summary update).
- `engine-feedback/triage/EF-051-*.md` created: ~1,100 words; NOT in default-read enumeration (only INDEX.md is).
- Currently-active-session provenance (per read-contract v5 §1 item 8): `00-assessment.md 2,400` + `02-decisions.md ~4,000` + `03-close.md ~3,500` estimate = ~9,900 words default-read while session open.

Post-close: session-scope provenance rotates to archive-surface per read-contract v5 §1 item 8. Close-rotation: S046 `provenance/046-session/03-close.md` rotates OUT (~2,800 words); S052 `provenance/052-session/03-close.md` enters (~3,500 estimated). Net close-rotation delta +700 words.

Net aggregate change from S052 open to S052 close:
- Pre-close delta: +9,900 (session-scope provenance while open) + 50 (INDEX growth) = +9,950 words at max-during-session.
- At close: -9,900 (session-scope provenance becomes archive-surface except the 03-close which enters via §1 item 7 close-rotation) + 3,500 (03-close.md enters) - 2,800 (S046 close rotates OUT) + 50 (INDEX growth) + ~180 (SESSION-LOG row) = +930 net.
- Forecast post-S052-close aggregate: **~71,991 words across 20 files** (comfortable under §2b 90K soft with ~18K headroom).

Actual aggregate to be reported in validator output post-commit.

## §10 S052 meta-observations

1. **Second-ever complete inbox→triage→resolved lifecycle within single session** (S048 EF-001 first; S052 EF-051 second). First-ever for self-dev-originated defect. Demonstrates lifecycle schema robustness.
2. **Path T reified at n=2**; Path T+L bundled label first-instance. Forward-naming convention: path-labels reify at n=2 per S051 Path L+A precedent.
3. **Seventh minor bug-fix-style source-realignment** per OI-002 heuristic. Precedent chain stable at seven precedents; pattern established as routine for engine-adjacent implementation realignment to already-specified contracts.
4. **Substrate-smoke-test pattern vindicated a second time** (S050→S051 surface + S051→S052 resolve). Pattern: code-review-only at adoption session + first-real-use at next-session + defect-surfaces-as-engine-feedback-intake + resolution at session-after-next. Four-session arc for a substrate adoption + smoke-test + defect-surface + defect-resolve.
5. **WX-50-1 phase-2 gate Condition 1 ambiguity surfaces operator-interpretation question**. Honest recording allows operator to decide at S053 close or phase-2 MAD time. Recorded the stricter and more permissive counting rules both; final call is operator's.
6. **Engine-v9 preservation window advances to depth 2** — modest depth compared to engine-v7's 11-session record. Preservation depth is not a metric to maximise; correct depth for v9 will be determined by substrate-related work surfacing over the next several sessions.

## §11 Commit and close

This close file is committed with the S052 artefacts:
- `provenance/052-session/00-assessment.md` (pre-work commit `bcdbc0c` already done).
- `provenance/052-session/02-decisions.md` (this close commit).
- `provenance/052-session/03-close.md` (this file; this close commit).
- `tools/retrieval_server.py` (Direction B implementation edit; this close commit).
- `engine-feedback/INDEX.md` (status summary + EF-051 row update; this close commit).
- `engine-feedback/triage/EF-051-aliases-yaml-not-consulted-at-query-time.md` (triage record create; this close commit).
- `SESSION-LOG.md` (S052 thin row append; this close commit).

Engine-v9 stands. 36 first-class minorities preserved. 13 active OIs. Engine-feedback state 0 new / 1 triaged / 4 resolved / 0 rejected. WX-50-1 phase-2 gate: Condition 1 arguable-satisfied-pending-operator-interpretation; Conditions 2 + 3 not satisfied; evaluation continues at S053. Path T reified at n=2. Path T+L bundled label first-instance (reification deferred to n=2). WX-34-1 remediation preserved. Seventh minor bug-fix-style source-realignment edit complete.
