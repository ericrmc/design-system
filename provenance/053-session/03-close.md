---
session: 053
title: Close — Path A (Watch) pure ratified; single-orchestrator default-agent session; two decisions D-183 Path A + D-184 housekeeping (13 sub-sections); engine-v9 preserved preservation window count 2→3; WX-50-1 third-and-last post-S050 3-field recording session — gate does NOT fire under stricter counting; EF-053 inbox intake (search query parser treats unquoted hyphen as FTS5 NOT operator; engine-adjacent friction); inbox 0 new → 1 new; 36 first-class minorities preserved unchanged; 13 active OIs unchanged; D-129 eighth-consecutive + D-138 eighth-consecutive clean exercises; WX-28-1 twenty-third close-rotation zero retention-exceptions; WX-24-1 MAD v4 twenty-sixth-session no-growth new record; WX-34-1 remediation preserved (SESSION-LOG ~5.4K post-row well under 6K soft); twenty-sixth-consecutive housekeeping [none]-trigger
date: 2026-04-25
status: complete
---

# Close — Session 053

## §1 Artefacts produced

### §1a Provenance (`provenance/053-session/`)

- `00-assessment.md` (~3,200 words; commit `bc1e8f5`) — pre-work commit per D-017 spirit + S048/S049/S050/S051/S052 precedent chain. Proposed Path A (Watch) pure per `prompts/development.md` §How to operate + operator "do not halt". §3 determination + §3a minority-activation-warrant zero fire independently + §3b WX-50-1 phase-2 gate status under stricter-vs-permissive counting + §3c MCP stdio transport unverified. §4a D-129 eighth-consecutive exercise with five considered-and-rejected non-Path-A alternatives. §5 ten-step work plan. §7 ten honest limits including WX-50-1 stricter-vs-permissive counting + MCP transport unverified + §5.6 window-ii reopen-warrant interpretation.
- `02-decisions.md` (~2,600 words; this close commit) — **two decisions**: D-183 Path A (Watch) ratified `[none]` single-agent reason + D-184 housekeeping `[none]` with 13 sub-sections a–m.
- `03-close.md` — this file.

No `STATUS.md` (single-orchestrator). No `01-brief-shared.md` / `01X-perspective-*.md` / `01-deliberation.md` / `manifests/` / `participants.yaml` (no MAD convened; Path A is single-orchestrator per D-183). No archive subdirectories (no current-session raw exceeds 8K hard ceiling). No external artefact in self-dev.

### §1b Specification changes THIS session

**None.** No engine-definition specification edited. No v-bump on any spec; no engine-v bump; no minor bug-fix-style source-realignment edit this session (S053 does not extend the 7-precedent chain). Per D-183 classification, S053 is pure Path A Watch — observation + housekeeping + inbox intake + preservation only.

All active specs remain at their S052-close versions: `PROMPT.md` unchanged; `MODE.md` unchanged; `prompts/development.md` unchanged; `prompts/application.md` unchanged (v8); `methodology-kernel.md` v6 unchanged; `multi-agent-deliberation.md` v4 unchanged; `validation-approach.md` v5 unchanged; `workspace-structure.md` v6 unchanged; `identity.md` v2 unchanged; `reference-validation.md` v3 unchanged; `read-contract.md` v5 unchanged; `retrieval-contract.md` v1 unchanged; `engine-manifest.md` unchanged; `specifications/aliases.yaml` schema_version 1 unchanged; `.mcp.json` unchanged; `tools/validate.sh` unchanged; `tools/build_retrieval_index.py` unchanged; `tools/retrieval_server.py` unchanged (S052 Direction B fix preserved); `tools/bootstrap-external-workspace.sh` unchanged.

### §1c Development-provenance files amended (WX-35-1 claim discipline)

Per WX-35-1 standing discipline, each claimed file amendment is verified via `git log --oneline <path>` at close and explicitly retracted if not committed.

- **`engine-feedback/INDEX.md`** — **EDITED this close commit**. Status summary: `0 new / 1 triaged / 4 resolved / 0 rejected` → **`1 new / 1 triaged / 4 resolved / 0 rejected`**. EF-053 row added as first entry in Records table (per post-S052 INDEX ordering new entries appear near top for operational reachability).
- **`engine-feedback/inbox/EF-053-search-query-parser-unquoted-hyphen-fts5-not-operator.md`** — **CREATED this close commit**. Self-dev-originated inbox intake record per `workspace-structure.md` v5 §engine-feedback schema (`source_workspace_id: selvedge-self-development`; `source_session: 053`; `reported_by: application-agent`; `target: engine-adjacent`; `severity: friction`; `status: inbox`). Three repair directions proposed (A query-sanitization / B structured-error-response / C spec-narrowing); Direction A most likely. Triage scheduled S054+.
- **`SESSION-LOG.md`** — **EDITED at close** (S053 thin row appended per Q5=(a) ≤180-word target).
- **`provenance/053-session/00-assessment.md`** — **CREATED** (commit `bc1e8f5` pre-work).
- **`provenance/053-session/02-decisions.md`** — **CREATED this close commit**.
- **`provenance/053-session/03-close.md`** — **CREATED this close commit** (this file).
- **`specifications/*.md`** — **NOT edited** per WX-35-1 explicit retraction. No spec edit this session per §1b.
- **`specifications/aliases.yaml`** — **NOT edited** per WX-35-1 explicit retraction. Schema unchanged; seed entries unchanged.
- **`specifications/engine-manifest.md`** — **NOT edited** per WX-35-1 explicit retraction. No engine-v bump.
- **`tools/validate.sh`, `tools/build_retrieval_index.py`, `tools/retrieval_server.py`, `tools/bootstrap-external-workspace.sh`** — **NOT edited** per WX-35-1 explicit retraction.
- **`open-issues/*.md`** — **NOT edited** per WX-35-1 explicit retraction. No OI opened/resolved/amended this session; 13 active OIs unchanged. EF-053 did not promote to OI (not yet triaged; classification deferred).
- **`open-issues/index.md`** — **NOT edited** per WX-35-1 explicit retraction.
- **`PROMPT.md`, `MODE.md`, `prompts/development.md`, `prompts/application.md`, `CLAUDE.md`** — **NOT edited** per WX-35-1 explicit retraction.
- **`engine-feedback/triage/*.md`** — **NOT edited** per WX-35-1 explicit retraction. Existing 4 triage files (EF-001 + EF-047-retrieval-discipline + EF-047-session-inputs + EF-047-brief-slot-template + EF-051) unchanged.
- **`.mcp.json`, `.gitignore`** — **NOT edited** per WX-35-1 explicit retraction.
- **`.cache/venv/`, `.cache/retrieval.db`** — **PRE-EXISTING mid-session use** (gitignored; not committed). S051-created venv + S051-built DB re-used for due-diligence substrate queries; no mutation (DB is read-only this session).

### §1d Validator status at close

Actual validator state at close: to be recorded post-commit. Forecast: **1236+ PASS / 0 FAIL / 12–14 WARN → PASS**.

- Aggregate default-read surface: forecast **~70,300 words across 21 files** (close-rotation S047 OUT ~5,500 words; S053 enters ~3,500 words; net delta ~-2,000). Under §2b 90K soft with comfortable ~19,700 words headroom.
- SESSION-LOG.md post-thin-row: ~5,366 words (well under 6K soft; well under 8K hard). WX-34-1 remediation preserved.
- Check 20 per-file: PASS (unchanged from S052 — no file added/removed; MAD 6,637 + reference-validation 7,160 soft-warnings persist).
- Check 20 aggregate: PASS.
- Check 21 archive-pack manifest integrity: PASS (no new archive-pack this session).
- Check 22 archive-pack citation consistency: PASS (no new archive citations; existing citations unchanged).
- Check 23 MODE.md presence: PASS.

Expected 12–14 warnings breakdown:
- 2 spec soft-warnings (`multi-agent-deliberation.md` 6,637 + `reference-validation.md` 7,160; unchanged; designed).
- 10 pre-existing "no rejected alternatives found" design-intent warnings (2 per session × S046/S047/S048/S051/S052).
- 0–2 new "no rejected alternatives" warnings for S053 `02-decisions.md` D-183 + D-184 (both cite alternatives via cross-file reference to `00-assessment.md` §4a; validator regex matches per-decision body).

### §1e Engine-version status THIS session

**Engine-v9 preserved** at S053 close; preservation window count **2 → 3** (S051 first post-v9 + S052 second post-v9 + S053 third post-v9). Engine-v9 established S050 per D-172; no engine-v bump this session. §5.4 cadence minority does not re-escalate (non-bump session; precedent chain v5–v9 intact per S028 D-096 / S033 D-107 / S036 D-114 / S048 D-154 / S050 D-172).

## §2 Operational warrants changed or advanced

1. **WX-50-1 third-and-last post-S050 3-field recording session executed.** See §6 below for full payload. Under **stricter counting** (S052 D-182h recommended methodology), phase-2 gate does NOT fire across the S050–S053 observation window; per `retrieval-contract.md` v1 §6, phase-1 is paused (not deprecated) and phase-1 tools remain available for organic use in S054+. Under **permissive counting**, Condition 1 satisfies (S051 + S052 + S053 all recorded ≥1 `results_used` entry). Case Steward recommendation at S053 close is stricter counting; operator-authoritative at any subsequent session per §6 closing paragraph.

2. **EF-053 inbox intake (search query parser unquoted-hyphen FTS5 NOT operator).** Surfaced during S053 due-diligence substrate queries; `search("D-129 standing discipline")` crashed with `sqlite3.OperationalError: no such column: 129` because FTS5 parser treats unquoted hyphen as NOT operator. Contradicts `retrieval-contract.md` v1 §2.1 ("Tokenisation MUST treat hyphen, underscore, and § as word-internal") at query-parser level (tokenizer-time compliance already present; query-parser-time compliance missing). Three repair directions proposed; Direction A query-sanitization most likely. Triage S054+. Engine-feedback state 0 new → 1 new.

3. **D-129 standing discipline eighth-consecutive clean exercise.** Five considered-and-rejected non-Path-A alternatives in `00-assessment.md` §4a. §5.12 Path-Selection Defender reopen warrant (a) does not fire.

4. **D-138 folder-name default eighth-consecutive clean exercise.** `provenance/053-session/` no suffix, no slug.

5. **WX-28-1 twenty-third close-rotation zero retention-exceptions.** S047 rotates OUT at S053 close; S053 enters. Retention window post-rotation: S048/S049/S050/S051/S052/S053.

6. **WX-24-1 MAD v4 twenty-sixth-session no-growth streak new record.** `multi-agent-deliberation.md` v4 stable at 6,637 words. New record from S042 reset point (S043–S053 all no-growth).

7. **WX-34-1 remediation preserved.** SESSION-LOG.md post-thin-row ~5,366 words (under 6K soft with ~630 words headroom). Compression at S051 holds; no new pressure.

8. **Substrate-smoke-test / due-diligence pattern continues to surface defects.** S050 §8 forward-commitment pattern: code-review-only at adoption + first-real-use at next-session + defect-surfaces-as-engine-feedback-intake. S051 surfaced EF-051 (alias-indirection); S052 resolved EF-051; S053 surfaces EF-053 (search query parser hyphen) during due-diligence. Three consecutive substrate-exercise sessions have each produced actionable observations. The substrate-use-surfaces-defects pattern is reinforced.

9. **§10.4-M2 (Skeptic-preserver premature-feedback-pathway) continued preservation.** Engine-feedback pathway exercised again at EF-053 intake without structural retrofit. Activation warrant "10 sessions post-S036 with zero external engine-feedback inbox + no external in flight" does not fire — pathway has accumulated 5 intake records (1 external EF-001 + 4 self-dev EF-047×3 + EF-051) at S052 close; S053 adds EF-053 for a total of 6 intakes. Pathway is in use; minority preserved-unactivated.

10. **§10.4-M7 P2 minimum-adoption / defer-with-instrumentation — partial activation warrant firing**. Activation warrant first clause satisfies at S053 close under stricter counting (WX-50-1 gate did NOT fire across S050–S053). Second clause does NOT satisfy (phase-1 tools WERE used — S051 7 calls + S052 7 calls + S053 12 calls). Minority preserved-unactivated pending both clauses.

11. **No new first-class minority preserved.** Single-orchestrator Path A; no deliberation; no dissent surface. 36 minorities preserved unchanged.

12. **Twenty-sixth-consecutive housekeeping `[none]`-trigger decision**. D-184 extends the pattern (housekeeping consolidation decisions with `[none]` triggers since D-126 Session 041). Pattern now deeply instantiated.

## §3 Engine-v disposition and preservation depth

**Engine-v9 preserved at S053 close; preservation window count = 3.**

S053 is the third post-engine-v9 session. Engine-v9 established at S050 per D-172 (MAD-adopted new engine-definition spec bump-provenance class). §5.4 cadence minority does not re-escalate.

Forward observation: engine-v9 preservation window will close at depth TBD. Candidate triggering events:
- Phase-2 substrate extensions per WX-50-1 firing — **under stricter counting at S053 close, gate does NOT fire; phase-1 paused; phase-2 adoption requires future re-evaluation at operator discretion or via new triggering events.**
- EF-053 resolution at S054+ is classified minor per OI-002 if Direction A implementation-only (most likely); no engine-v bump unless Direction C spec-narrowing is adopted alone (substantive candidate).
- Post-arc `selvedge-disaster-response` review triggering any of S047 D-150 three deferred candidates (i)/(ii)/(iii) could produce engine-v10.

## §4 Preserved first-class minorities at S053 close

**36 first-class minorities preserved engine-wide at S053 close** — unchanged from S052. No new minority preserved; no minority discharged; no minority activated.

Full enumeration per `specifications/workspace-structure.md` v6 §10.4 (M1–M11) + §5.1/§5.4/§5.5/§5.6/§5.7/§5.8/§5.9/§5.10/§5.11/§5.12/§5.13/§5.14 + Session 024 A.4 four minorities + Session 027 §A/§B/§C + existing preserved-minorities in `reference-validation.md` v3 §10.1/§10.2/§10.3 + `retrieval-contract.md` v1 §7.1–§7.5 (mirrored with workspace-structure §10.4-M7–M11).

Per §D-184j observation-window advances: §10.4-M7 partial-activation (first clause only; not both); §10.4-M8/-M9/-M10/-M11 preserved-unactivated; §5.6 worst-case-side carries forward with window-ii observation.

## §5 Watchpoints status at S053 close

- **WX-24-1** — MAD v4 stable 6,637 words. **Twenty-sixth-session no-growth streak** (S043–S053). New record.
- **WX-24-3** — reference-validation label discipline n=8 stable.
- **WX-27-1** — stable.
- **WX-28-1** — **twenty-third close-rotation** (S047 rotates OUT; S053 enters); zero retention-exceptions.
- **WX-33-2** — reference-validation.md v3 7,160 words stable.
- **WX-34-1** — **remediation preserved**. SESSION-LOG ~5,366 post-row; no new breach pressure.
- **WX-35-1** — standing discipline applied cleanly; explicit retractions recorded in §1c.
- **WX-43-1** — cumulative baseline n=6-of-8 + explicit-instruction variant n=0-of-9 (S047+S049+S050+S051+S052+S053). OI-promotion discharged-as-not-warranted per S050 D-176. No sub-agents convened at S053; cumulative n unchanged.
- **WX-44-1** — codex-CLI independence-phase breach n=3 across S044+S045+S047. Not exercised this session (no codex invocation). Forward-convention candidate held cleanly by trivial non-exercise.
- **WX-44-2** — codex CLI model-version-drift discipline: not exercised this session.
- **WX-47-1** — codex-CLI argv `---` YAML parsing fragility: not exercised this session.
- **WX-50-1** — **third-and-last-of-3 post-S050 3-field recording executed** per §6 below. Phase-2 gate does NOT fire under stricter counting; phase-1 paused. Phase-1 tools remain available for organic use S054+.

## §6 Retrieval substrate use (WX-50-1)

Per `retrieval-contract.md` v1 §6, every session close S050 through S053 records substrate use in 3 fields. S053 is the third and last session of the observation window.

**`tool_calls_by_type`**: `{search: 4, resolve_id: 8}`.

All 12 successful invocations this session were to the substrate at `.cache/retrieval.db` via the S051-created `.cache/venv/` python (not via MCP stdio transport — workspace Claude Code session does not have `selvedge-retrieval` MCP server connected; `ToolSearch` query "mcp selvedge retrieval" returned non-substrate MCP surfaces per §1c). The 12 calls were due-diligence verification of citation locations used in `00-assessment.md` + `02-decisions.md` (see §8 honest limit 1 for load-bearing analysis):

**resolve_id calls (8 successful)**:
1. `resolve_id("D-172")` → direct-canonical → `provenance/050-session/02-decisions.md:4` (verified engine-v9 establishment location).
2. `resolve_id("§10.4-M5")` → direct-canonical → `provenance/042-session-assessment/00-assessment.md:13` (verified minority first-appearance; actual canonical appearance in `workspace-structure.md` v6 §10.4-M5 is a later line).
3. `resolve_id("WX-50-1")` → direct-canonical → `specifications/retrieval-contract.md:10` (verified phase-2-gate canonical location).
4. `resolve_id("D-129")` → direct-canonical → `provenance/044-session-assessment/02-decisions.md:4` (verified D-129 standing-discipline decision location — wait, D-129 was established at S043 per SESSION-LOG; this result points to S044 first-citation which is the first post-adoption application per forward-convention pattern; note for self: D-129 first-appearance via Strategy 1 finds first index record, not necessarily semantic first-definition).
5. `resolve_id("D-138")` → direct-canonical → `provenance/045-session-assessment/02-decisions.md:4` (verified D-138 folder-name-default decision location).
6. `resolve_id("engine-v9")` → direct-canonical → `provenance/051-session/00-assessment.md:10` (verified engine-v9 first-citation in subsequent-session assessment; canonical engine-manifest.md §2 definition is at `specifications/engine-manifest.md:32` per file-position but first index-record-ordered-by-line-asc in assessment-document is earlier).
7. `resolve_id("M5")` → **alias-indirection via Strategy 1.5** → canonical `§10.4-M5` → `provenance/042-session-assessment/00-assessment.md:13` (verified S052 D-181 Direction B fix operational).
8. `resolve_id("phase-2 gate")` → **alias-indirection via Strategy 1.5** → canonical `WX-50-1` → `specifications/retrieval-contract.md:10` (verified S052 D-181 Direction B fix operational for multi-word alias).

**search calls (4 successful + 1 failed)**:
1. `search("Path A Watch preserve", k=3)` → 3 results (top: `provenance/035-session-assessment/02-decisions.md` score=-2.004). Used-in-cite: verified Path A precedent chain for §D-184c.
2. `search("D-129 standing discipline", k=3)` **→ FAILED** with `sqlite3.OperationalError: no such column: 129`. **Root cause**: FTS5 query parser treats unquoted hyphen as NOT operator; EF-053 records this defect.
3. `search('"D-129" standing discipline', k=3)` → 3 results (top: `provenance/044-session-assessment/00-assessment.md` score=-5.506). Used-in-cite: verified D-129 standing-discipline precedent.
4. `search('"WX-50-1" "phase-2 gate"', k=3)` → 3 results (top: `provenance/050-session/03-close.md` score=-14.210). Used-in-cite: verified WX-50-1 phase-2-gate cross-references.
5. `search('"engine-v9" preservation window', k=3)` → 3 results (top: `provenance/050-session/03-close.md` score=-7.372). Used-in-cite: verified engine-v9 preservation-window framing.

**`results_used_with_artefact_id`** (transparent under both counting interpretations per S052 D-182h honest-limit):

**Under permissive counting (12 entries)**:
- 8 resolve_id results as listed above (each entry shape `{tool, query, returned_artefact_path, used_in}`).
- 4 search results as listed above.

**Under stricter counting (0 entries)**: none of the 12 successful invocations produced decision content I could not have produced from Read alone. The resolve_id calls verified citation locations I already knew; the search calls returned expected ranked results. All due-diligence verification, not content-generating. Under stricter counting the `results_used_with_artefact_id` field is `[]` for S053.

**`fallbacks_due_to_missing_capability`**: **1 new entry**.

```yaml
- query_intent: "search for occurrences of hyphenated identifier D-129 in workspace using phrase-unquoted query form"
  why_phase_1_did_not_suffice: "FTS5 query parser treats unquoted hyphen as NOT operator; search('D-129 standing discipline') is parsed as 'D NOT 129 standing discipline' and crashes with sqlite3.OperationalError: no such column: 129. Contradicts retrieval-contract.md v1 §2.1 ('Tokenisation MUST treat hyphen, underscore, and § as word-internal') at query-parser level — tokenizer-time compliance already present via tokenize='porter unicode61 tokenchars -_§'; query-parser-time compliance missing. Workaround is to quote hyphenated identifiers: search('\"D-129\" standing discipline') succeeds and returns correctly ranked results. Recorded as engine-feedback intake EF-053-search-query-parser-unquoted-hyphen-fts5-not-operator; three repair directions proposed (A query-sanitization / B structured-error-response / C spec-narrowing). Category: query-parser behaviour. NOT structured-filter or graph-traversal; does NOT advance phase-2 gate Condition 2."
```

**Phase-2 gate status at S053 close (final recording session)**:

- **Condition 1** (≥2 sessions in S050–S053 with ≥1 `results_used_with_artefact_id` entry):
  - Under **permissive counting**: S050 = 0; S051 = 2; S052 = 7; S053 = 12. **Satisfied** (≥2 sessions recorded ≥1 entry).
  - Under **stricter counting**: S050 = 0; S051 = arguable-2; S052 = 0; S053 = 0. **Unsatisfied** (at most 1 session, and that session's entries are themselves arguable).
- **Condition 2** (≥1 session records ≥1 fallback where missing capability is structured-filter OR graph-traversal): S051 fallback = alias-indirection (resolved S052). S053 fallback = search-query-parser hyphen behaviour. Neither category is structured-filter or graph-traversal. **NOT satisfied** across observation window.
- **Condition 3** (≥1 external-workspace adoption records ≥1 useful domain-context query): `selvedge-disaster-response` has not been re-bootstrapped with substrate. **NOT satisfied**.

**Gate firing decision at S053 close**:

Case Steward recommendation under stricter counting (the honest reading per S052 D-182h): **phase-2 gate does NOT fire**. Per `retrieval-contract.md` v1 §6 closing paragraph: *"If phase-2 does NOT fire in S050–S053, phase-1 is paused (not deprecated); the §7.1 minority's activation warrant evaluates next."*

§7.1 minority activation warrant (per `retrieval-contract.md` v1 §7.1): "if the WX-50-1 gate fails to fire across S050–S053 AND zero use recorded for phase-1 tools in ≥3 consecutive sessions, revisit whether phase-1 should have shipped at all." First clause **satisfies** at S053 close under stricter counting. Second clause (zero use across 3+ consecutive sessions) **does NOT satisfy** — S051 = 7 calls, S052 = 7 calls, S053 = 12 calls (non-zero use with reasonable cadence). Minority preserved-unactivated.

**Phase-1 pause state**: phase-1 tools remain available for organic use in S054+. The contract is unchanged; implementation is unchanged; aliases.yaml seeds preserved. Phase-2 adoption requires new triggering events (Condition 2 structured-filter/graph-traversal fallback; Condition 3 external-workspace adoption; or operator surfacing).

**Phase-2 re-evaluation trigger candidates (forward observation)**:
- EF-053 triage at S054+ may adopt Direction A (query-sanitization) in a minor engine-adjacent fix; if adopted, S054+ becomes a candidate session for renewed substrate usage (more searchable queries) and Condition 1 could re-satisfy organically.
- `selvedge-disaster-response` re-bootstrap at operator discretion would activate Condition 3 paths.
- Future self-dev sessions using substrate for genuine navigation (multi-hop cross-reference queries; structured filtering) would activate Condition 2 paths.

Operator-authoritative per §6 closing paragraph; S053 close records the stricter-counting recommendation and the phase-1 pause state transparently.

## §7 Next-session items and forward observations

**Session 054 recommendation**: default-agent session. Priorities:

- **Inbox check at open**: `engine-feedback/inbox/` has **1 new record** (EF-053) at S053 close. If operator surfaces no higher-priority agenda, S054 is a candidate Path T (Triage) session for EF-053. Most-likely disposition per S052 D-181 EF-051 precedent: minor implementation edit to `tools/retrieval_server.py` adopting Direction A (query-sanitization before FTS5 invocation); same-session resolution shape as S052 (Path T+L bundled label n=2 reification candidate).
- **WX-50-1 observation window closed**. No further session-close 3-field recording obligation post-S053. Phase-1 tools remain usable for organic navigation; usage no longer tracked at per-session schema level. Future operator-discretion on phase-2 evaluation.
- **External-application arc progression**: `selvedge-disaster-response` arc S002–S005 pending operator transport; substrate available via bootstrap-refresh (operator-discretionary). Not S054-actionable absent operator surfacing.
- **Post-arc self-dev review obligation** (carrying from S047 D-150): three remaining deferred spec-amendment candidates (i)/(ii)/(iii) preserved for post-arc review. Unchanged at S053.

**S054 close should evaluate**:
- EF-053 triage disposition (resolved / deferred / rejected).
- Engine-v9 preservation (window count would reach 4 if S054 preserves).
- D-129 ninth-consecutive exercise.
- D-138 ninth-consecutive folder-name default.
- §5.6 GPT-family-concentration fifth-consecutive observation if MAD convenes; else N/A.
- WX-28-1 twenty-fourth close-rotation (S048 rotates OUT; S054 enters).
- WX-24-1 MAD v4 twenty-seventh-session no-growth (if no MAD edit).
- If EF-053 is resolved same-session via Path T+L pattern: Path T+L bundled label reification at n=2 (S052 first-instance + S054 second-instance).

## §8 Honest limits at close

1. **WX-50-1 counting interpretation is recorded transparently but unresolved without operator.** Under permissive counting, gate fires; under stricter counting, gate does not fire. Case Steward recommends stricter counting at S053 close (my resolve_id + search calls verified known locations; did not produce unique decision content). Operator may revise at any subsequent session per `retrieval-contract.md` v1 §6. If operator at phase-2 MAD time (or any future session) adopts permissive counting retrospectively, gate fires at S053 close retroactively.

2. **MCP stdio transport remains unverified in-session.** Same limit as S051 + S052 close §8. `ToolSearch` query "mcp selvedge retrieval" at S053 did NOT surface `mcp__selvedge_retrieval__*` tools; workspace session uses direct SQLite via `.cache/venv/` python. Substrate SQL-contract behaviour is verified through the direct path; FastMCP stdio wiring is NOT verified. Deferred to a session where the MCP server is connected OR operator runs the server explicitly.

3. **EF-053 defect scope potentially broader than observed.** I exercised one specific FTS5 query form (`D-129 standing discipline` unquoted); similar unquoted hyphenated identifiers (`OI-NNN`, `EF-NNN`, `WX-N-N`, etc.) likely exhibit the same behaviour. The EF-053 intake describes the defect class; a more thorough triage at S054+ may want to enumerate failure modes across the full ID-pattern family.

4. **Due-diligence query count (12 successful + 1 failed) is higher than typical Path A session.** The intent was to exercise the substrate for legitimate navigation + WX-50-1 final recording. A pure-minimum Path A would be 0 queries; S029 Path A had 0 substrate calls (pre-substrate); S042 Path A had 0 substrate calls. S053's 12 queries reflect the WX-50-1 recording obligation. Not a budgetary concern; forward observation for future Path A + substrate sessions.

5. **The 8 resolve_id calls' "first line" attribution is imperfect for cross-cutting canonicals.** E.g., `resolve_id("engine-v9")` returned `provenance/051-session/00-assessment.md:10` (first index-record-ordered-by-line-asc in assessment document); the canonical `specifications/engine-manifest.md:32` definition is at a later record. This is phase-1-design-as-specified (resolve_id returns first occurrence found; §2.2 "If `alias` is a known identifier pattern..., returns the first occurrence found in the indexed corpus"). Not a bug per contract; honest observation for future phase-2 consideration (multi-match disambiguation with canonical-definition-location preference would be a phase-2 feature).

6. **Assessment commit was `bc1e8f5`** (`provenance/053-session/00-assessment.md`). Per WX-35-1 claim-discipline audit: file actually committed at `bc1e8f5`; claim stands verified.

7. **S053 thin-row in SESSION-LOG.md** targeted ≤180 words per Q5=(a); actual word-count to be verified at commit.

8. **Path A default-ratified without operator Halt-1 response.** Selection made by Case Steward per `00-assessment.md` §4 rationale. If operator at a future session prefers a different path reconstruction of S053, the session's artifacts (assessment + decisions + close + intake + INDEX update + SESSION-LOG row) are preserved for reference; the path-selection decision is the one reversible element (new decision in subsequent session could supersede).

9. **Validator at close not yet recorded**; to be recorded post-commit. Expected PASS.

10. **§5.6 window-ii reopen-warrant status** recorded transparently in `00-assessment.md` §7 honest-limit 7. Window reading depends on whether "session" in the warrant text means "MAD session" (interpretation A) or "any session" (interpretation B). Under interpretation B, the window is already passed (>6 sessions since S043 Gemini was the last non-GPT-non-Claude MAD participant). Under interpretation A, only 4 MAD sessions have occurred post-S043 (S044 OC + S045 OS + S047 OS + S050 AS) all with GPT-family-concentration worst-case-side; window is at 4-of-6 (MAD count). Path A has no MAD where the warrant could be actioned even if it fires. Forward observation: next MAD that is GPT-family-concentration worst-case-side may trigger reopen-warrant activation depending on interpretation adopted; reopen-warrant text ambiguity flagged at S053 as candidate for clarification at next MAD-involving session.

## §9 Aggregate default-read surface impact at close

Pre-close aggregate (at S053 open per validator): 72,332 words across 21 files.

**Actual post-close per validator** (run immediately before this close was finalised): **74,449 words across 21 files** → +2,117 words net. Comfortable ~15,551 words headroom to §2b 90K soft ceiling.

Breakdown of actual delta:
- Close-rotation: S047 `provenance/047-session/03-close.md` rotates OUT (2,938 words; much smaller than my earlier mis-estimate of ~5,500); S053 `provenance/053-session/03-close.md` enters (4,476 words). Net close-rotation delta **+1,538 words**.
- `SESSION-LOG.md` growth: +544 words (5,186 → 5,730 post-S053-thin-row append; exceeds Q5=(a) ≤180-word target per §8 honest limit 7).
- `engine-feedback/INDEX.md` growth: ~+35 words (EF-053 row + status summary update).
- Other small adjustments: 0 (no spec edits; no new archive-packs).

Forecast error: my pre-close §9 estimated -7,020 net; actual is +2,117. Primary drivers: (a) S047 close size mis-estimated by ~2,500 words (actual 2,938 vs estimated ~5,500); (b) S053 close itself came in at 4,476 words vs estimated ~3,700; (c) SESSION-LOG row at ~544 words vs estimated ≤180. Recorded transparently per WX-22-1 honest-limits discipline; content-adaptive density for S053's substantive content (WX-50-1 terminal recording + EF-053 intake + stricter-vs-permissive counting rationale + §5.6 window-ii ambiguity flag) justifies the larger-than-target sizes per S051 close §8 precedent ("content-adaptive density is appropriate per workspace-structure.md v6 §SESSION-LOG").

Net aggregate at 74,449 is 2.1K higher than S052 close's 72,332 but 15.6K below the 90K soft ceiling — comfortable forward headroom. No pressure signal. WX-34-1 remains remediated.

During-session max: `00-assessment.md ~3,200` + `02-decisions.md ~2,600` + `03-close.md 4,476` = ~10,276 words default-read while session open (per read-contract v5 §1 item 8); these rotate to archive-surface post-close except `03-close.md` which enters the 6-session retention window. Mid-session validator run would therefore show ~84K; terminal close-state is 74.4K.

## §10 S053 meta-observations

1. **Third-consecutive substrate-exercise session surfaces third-consecutive actionable observation.** S051 → EF-051 alias-indirection; S052 → resolve EF-051 via Direction B; S053 → EF-053 search-query-parser hyphen. The substrate is operationally mature enough to be used but not mature enough to be used without surfacing defects. Forward-observation candidate: substrate defect-surfacing cadence is approximately one defect per substrate-exercise session at phase-1 maturity. Triage cost is bounded (1 intake + 1 subsequent triage + 1 minor fix if Direction A); preservation cost is bounded (the contract declares behaviour; observations refine the implementation). Pattern is sustainable.

2. **Path A with inbox intake is new-to-the-precedent-record but discipline-consistent.** Prior Path A sessions (S025/S026/S029/S034/S037/S038/S039/S042) did not produce inbox intakes (engine-feedback pathway adopted S036; Path A sessions S037+ could have but did not). S053 is the first Path A + inbox-intake session. Discipline permits it (intake is observation-recording, not substantive revision); convention now has a data point. If future Path A sessions continue to surface substrate defects via organic navigation, the Path A + intake shape reifies as routine.

3. **WX-50-1 observation window closes with clean honest recording.** The S050 adoption deliberately scheduled a 4-session observation window (S050–S053) to let phase-1 use empirically determine phase-2 warrant. The window ran cleanly: S050 = adoption baseline (0); S051 = first-real-use + EF-051 defect surface (7 calls + 1 fallback); S052 = defect resolution (7 calls + 0 new fallbacks; EF-051 resolved in-session); S053 = due-diligence + EF-053 defect surface (12 calls + 1 fallback). Empirical pattern: phase-1 tools are used; defects are surfaced and tractable; neither phase-1 non-use nor phase-2-forcing evidence materialised. Per-counting-rule the gate interpretation differs; Case Steward records stricter counting at S053 close as the honest reading. Phase-1 paused; available for organic use.

4. **Engine-v9 preservation window advances to depth 3** — still modest compared to engine-v7's 11-session record. Engine-v9's trajectory is substrate-adoption-plus-three-observation-sessions; typical preservation depths after content-driven bumps (v5–v8) ranged from 2 to 11 sessions. v9 depth forecast: TBD; EF-053 resolution (if Direction A) is minor and preserves v9; EF-053 resolution (if Direction C) would bump v10; other S053+ triggers preserved unchanged.

5. **Twenty-sixth-consecutive housekeeping [none]-trigger decision pattern.** Not strictly a streak counter but pattern now deeply instantiated. Forward observation: the `[none]` housekeeping pattern is engine-conventional.

6. **Due-diligence discipline surfaced at S053** — running `resolve_id` on citations-about-to-be-written in decisions is a disciplined practice; it catches citation errors before they land in the close narrative. S053 did not find any citation errors (resolve_id results either matched expectations or surfaced the "first-line" observation at honest limit 5). Practice could be adopted as a convention for future sessions; not formalised at S053 (Path A minimal intervention).

## §11 Commit and close

This close file is committed with the S053 artefacts:
- `provenance/053-session/00-assessment.md` (pre-work commit `bc1e8f5` already done).
- `provenance/053-session/02-decisions.md` (this close commit).
- `provenance/053-session/03-close.md` (this file; this close commit).
- `engine-feedback/INDEX.md` (status summary 0-new → 1-new + EF-053 row addition; this close commit).
- `engine-feedback/inbox/EF-053-search-query-parser-unquoted-hyphen-fts5-not-operator.md` (this close commit).
- `SESSION-LOG.md` (S053 thin row append; this close commit).

Engine-v9 stands. 36 first-class minorities preserved. 13 active OIs. Engine-feedback state 0 new / 1 triaged / 4 resolved / 0 rejected → **1 new** / 1 triaged / 4 resolved / 0 rejected (EF-053 intake). WX-50-1 observation window closes; phase-2 gate does NOT fire under stricter counting; phase-1 paused per `retrieval-contract.md` v1 §6. Path A (Watch) reified as post-v-bump preservation shape again (ninth instance counting S025 + S026 + S029 + S034 + S037 + S038 + S039 + S042 + S053). WX-34-1 remediation preserved. Third-consecutive substrate-exercise session produces third-consecutive actionable observation (EF-053); pattern sustainable.
