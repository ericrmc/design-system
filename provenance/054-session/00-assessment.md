---
session: 054
title: Open assessment — Path T+L (Triage-Classify + minor Path L Implementation Fix) ratified per default-agent path; bundled triage of EF-053 (search query parser unquoted-hyphen FTS5 NOT operator) + EF-054 (forward-reference MCP tool for session-open commitment audit) with both Direction A adoptions; first-instance multi-intake same-session resolution; engine-v9 preservation window count 3→4 forecast; Path T+L reified at n=2 (S052 first-instance + S054 second-instance with multi-intake extension)
date: 2026-04-25
status: open
---

# Session 054 — Open assessment

## §1 State at session open

**Engine version**: engine-v9 preserved at S053 close (preservation window count 3 — third post-v9 session). v9 established S050 per D-172 (substrate adoption + new engine-definition spec `retrieval-contract.md` v1).

**Active OIs**: 13 (unchanged from S053 close). OI-016 hybrid-state (resolved-provisionally-v2). No OI promotion candidates from current inbox queue — both EF-053 and EF-054 classify as minor per OI-002 if Direction A adopted (the most-likely path).

**First-class minorities preserved engine-wide**: 36 (unchanged from S053 close). Per `specifications/workspace-structure.md` v6 §10.4 (M1–M11) + `reference-validation.md` v3 §10.1/§10.2/§10.3 + `retrieval-contract.md` v1 §7.1–§7.5 + assorted §5.1–§5.14 in workspace-structure.md + Session 024 A.4 + Session 027 §A/§B/§C. None fire activation warrants independently this session.

**Engine-feedback state at S053 close → S054 open**: **2 new** / 1 triaged / 4 resolved / 0 rejected. Two records await triage:
- **EF-053-search-query-parser-unquoted-hyphen-fts5-not-operator** (self-dev-originated; target engine-adjacent; severity friction; source_session 053; reported_by application-agent). Three directions A/B/C. Direction A most likely.
- **EF-054-forward-reference-mcp-tool-for-session-open-commitment-audit** (self-dev-originated post-S053-close operator-surfaced; target engine-adjacent; severity friction; source_session 053; reported_by operator). Three directions A/B/C. Direction A most likely.

**Validator at open**: 1246 PASS / 0 FAIL / 14 WARN → PASS (matches post-S053-close commit `6336795` recorded state).

**Aggregate default-read surface**: ~74,449 words across 21 files at S053 close per validator. ~15,551 words headroom to §2b 90K soft.

**SESSION-LOG.md** at open: ~5,730 words post-S053-row append. Well under 6K soft and 8K hard (WX-34-1 remediation preserved per S051 D-178 forced-restructure compression).

**WX-50-1**: observation window closed at S053 close per `retrieval-contract.md` v1 §6. Phase-2 gate did NOT fire under stricter counting (Case Steward recommendation per S052 D-182h). Phase-1 paused (not deprecated); phase-1 tools available for organic use S054+. §7.1 minority (P2 minimum-adoption) preserved-unactivated under partial-activation interpretation (first clause satisfies; second clause "zero use across 3+ consecutive sessions" does NOT satisfy since substrate was used S051/S052/S053).

**Substrate**: `.cache/retrieval.db` and `.cache/venv/` present from S051; index 448 docs / 48,852 identifiers per S051 close §6 record. Substrate is operational (S053 used it via `.cache/venv/` python; both `search` and `resolve_id` work as expected at the existing tool surface). No mtime-rebuild required at session open if no spec mtime advanced since last rebuild.

## §2 Operator agenda

Operator input is thin: `/clear` followed by literal `PROMPT.md`. No declared scope; no Halt directive surfaced. Per `prompts/development.md` §How to operate: "If `engine-feedback/INDEX.md` shows feedback records with `status: new`, the session's Assess activity should consider whether triage of one or more inbox items is the right increment for this session."

Two `status: new` records present. EF-053 was scheduled for S054 triage per S053 close §7. EF-054 was added post-S053-close per operator-surfaced observation; the inbox record itself flags "if S054 also triages EF-053 in the same session, it would bundle EF-053 + EF-054 in a Path T++ or Path T+L+L shape — first instance of multi-intake same-session resolution."

The post-S053 commit message captures explicit operator framing: *"intake records explicit 'do not introduce queries rather add MCP features' operator framing per post-session direction."* This is direction not deliberation: when forward-commitment audit becomes a workflow shape, prefer adding MCP features (Direction A) over adding queries to the agent's reading discipline (which would be the alternative-but-rejected shape of "tell agents to write SQL at session open"). EF-054 Direction A is the implementation that honours this framing.

## §3 Determination

### §3a Path classification

**Path T+L** (Triage-Classify + minor Path L Implementation Fix), n=2 reification (S052 first-instance + S054 second-instance), with first-instance multi-intake bundling (two records resolved same-session).

S054 is a default-agent session that:
1. Triages two engine-feedback inbox records (EF-053 + EF-054).
2. Adopts Direction A for both (minor implementation-only edits to `tools/retrieval_server.py`; no engine-v bump).
3. Adds a paired minor documentary amendment to `prompts/development.md` §How to operate naming the new `forward_references` tool (per EF-054 Direction A pairing).
4. Smoke-tests both fixes against the existing substrate via `.cache/venv/` python.

Single-orchestrator (Case Steward role); no MAD convened. Per `multi-agent-deliberation.md` v4 §When MAD Is Required: deliberation is not required for minor implementation fixes that bring source-realignment into compliance with already-deliberated contract semantics (EF-053 Direction A) or that are additive engine-adjacent extensions to the contract's permitted-extensions surface (EF-054 Direction A).

### §3b Minority-activation-warrant check

**None fire independently** at S054 open. Survey:

- **§5.1–§5.14** (workspace-structure.md): no warrant fires. §5.6 GPT-family-concentration window-ii observation continues (no MAD this session); reopen-warrant interpretation flagged S053 carries forward unchanged.
- **§10.4-M1 through M11** (workspace-structure.md): all preserved-unactivated or in-observation-window. M2 continued-preservation (engine-feedback pathway in active use; 6 intakes at S053 close + 0 new at S054 — 2 status-new + 4 resolved + 1 triaged = 7 lifecycle records). M5 discharged-as-vindicated S048. M7–M11 (retrieval-contract.md §7.1–§7.5 mirrored): M7 partial-activation first-clause-only (carries forward); M8/M9/M10/M11 preserved-unactivated.
- **§10.1/§10.2/§10.3** (reference-validation.md): no warrant fires.
- **§A/§B/§C** (Session 027): no warrant fires.
- **A.4** (Session 024 4-minorities): no warrant fires.

### §3c WX-50-1 phase-2 gate status at S054

Observation window closed at S053. Per §6 closing paragraph: phase-1 paused; phase-1 tools available for organic use. EF-053 Direction A adoption at S054 removes a known friction in `search` query-parser behaviour; this organically supports phase-1 use forward. EF-054 Direction A introduces a new MCP tool (`forward_references`) which is permitted per §2 ("the contract names `search` + `resolve_id` as required minimum at phase-1; additional tools are permitted" — paraphrasing §2 + §6 phase-2 list which names additional tools without forbidding pre-phase-2 additions).

S054 does not advance phase-2 gate (gate is already closed-and-not-fired); EF-054 is an additive phase-1-compatible tool extension, not a phase-2 commitment. The contract `retrieval-contract.md` v1 is unchanged this session; only the engine-adjacent implementation evolves.

### §3d MCP stdio transport status

Same limit as S051/S052/S053: workspace Claude Code session does not have `selvedge-retrieval` MCP server connected. Smoke-tests proceed via direct SQL through `.cache/venv/` python (the established substrate-mirror path). FastMCP stdio wiring remains unverified in-session; the new `forward_references` tool will be smoke-tested at the SQL-equivalent level, not the MCP-stdio level. Honest-limit recorded.

## §4 Decisions to ratify

### §4a Path selection — D-129 standing-discipline exercise (ninth-consecutive)

Per D-129 standing discipline (graduated S046 D-146; S047/S048/S049/S050/S051/S052/S053 eight-consecutive clean exercises), session-open assessment MUST surface ≥1 considered-and-rejected non-Path-T+L alternative. Surfacing five:

1. **Path A (Watch) pure** — REJECTED. Inbox has 2 status-new records; treating them as observation-only would defer triage indefinitely. EF-051 precedent at S051→S052 demonstrated same-session resolution is feasible and discipline-permissible. Path A would be appropriate only if neither record were ready for triage; both are technically clear and direction-narrow.

2. **Path T pure (triage-only, defer Path L)** — REJECTED. Both records have direction-clear minor-implementation paths (Direction A); same-session resolution is the S052 D-181 precedent. Splitting triage from implementation would add a second session of overhead with no methodological gain.

3. **Path L pure (skip triage, just implement)** — REJECTED. Skipping the triage record would break the `engine-feedback/` lifecycle convention per `workspace-structure.md` v6 §engine-feedback (intake → triage → resolved). The triage record is the discipline-mediated transition, not optional.

4. **Path MAD (substantive multi-perspective deliberation)** — REJECTED. Per `multi-agent-deliberation.md` v4 §When MAD Is Required: minor implementation fixes that bring source-realignment into compliance with already-deliberated contract semantics (EF-053) or that are additive engine-adjacent extensions (EF-054) do not require MAD. The Direction A path for both is technically clear; no rejected-alternatives surface needs cross-family adjudication.

5. **Path OS (operator-surfaced agenda)** — REJECTED. Operator input is thin (`PROMPT.md` only) with no declared scope. The post-S053 commit message captures operator framing about MCP-tool-additions over agent-query-additions, but this is direction-context for the existing inbox record, not a separate operator-surfaced agenda item demanding its own MAD.

### §4b Direction selection for EF-053

**Direction A — query sanitization at server level** is selected.

- Adopts implementation-only minor edit to `tools/retrieval_server.py`: scan query for hyphenated identifier patterns (D-NNN, OI-NNN, WX-N-N, EF-NNN-..., engine-vN, §N(.N)*(-MN)?, d01N_N) before passing to FTS5; wrap matched substrings in phrase quotes so they tokenize atomically rather than being parsed as NOT-operator expressions.
- Satisfies `retrieval-contract.md` v1 §2.1 ("Tokenisation MUST treat hyphen, underscore, and § as word-internal so that IDs ... tokenise atomically") at the query-parser level (tokenizer-time compliance was already present; query-parser-time compliance was missing).
- Does not change `retrieval-contract.md` v1 (contract is correct as written; implementation was the gap).
- Direction B (structured error response) is preserved as optional defensive complement; not in scope for S054 (Direction A solves the user-expected-atomic-token behaviour; Direction B would only surface the error mode without solving it).
- Direction C (spec narrowing) is rejected per S048 D-153 precedent (fix implementation to match contract; do not narrow contract to match implementation).

Classification: minor per OI-002. Eighth bug-fix-style source-realignment in the precedent chain (S022 R8a + S030 D-100 + S033 D-108 + S040 D-123 + S046 D-143 + S051 D-178 + S052 D-181 + S054). No engine-v bump.

### §4c Direction selection for EF-054

**Direction A — `forward_references` MCP tool** is selected, paired with a minor documentary amendment to `prompts/development.md`.

- Adds a new MCP tool to `tools/retrieval_server.py`:

  ```
  forward_references(target: str) -> {results: [{path, line, context, kind}], count, ...}
  ```
  
  Returns *all* occurrences of `target` in the `identifiers` table (NOT just the first per `resolve_id` semantics; NOT BM25-ranked per `search` semantics). Sorted by `source_path` then `line` for deterministic output. Empty results if target unindexed (returns count=0; not error).

- Pairs with a minor documentary sentence in `prompts/development.md` §How to operate naming the new tool as available at session open for forward-reference / commitment audit. Existing read-discipline is unchanged; the new tool is named-but-not-required.
- Does not require contract revision per `retrieval-contract.md` v1 §2 (the contract names `search` + `resolve_id` as required minimum at phase-1; additional tools are permitted; §6 phase-2 list names further tools but does not forbid pre-phase-2 additions).
- Direction B (`commitments_landing_at`) is rejected for S054 (semantic-aware classification adds complexity without demonstrated value at this scale; can be added later if Direction A demonstrates its worth).
- Direction C (`forward_commitments:` frontmatter convention + `list_commitments_at`) is rejected for S054 (substantive; depends on `frontmatter_kv` table deferred to phase-2 per S050 D-171; not phase-1-compatible).

Classification: minor per OI-002. Ninth bug-fix-style-or-extension in the precedent chain (S022 R8a + S030 D-100 + S033 D-108 + S040 D-123 + S046 D-143 + S051 D-178 + S052 D-181 + S054 EF-053 + S054 EF-054). No engine-v bump for the implementation; the documentary amendment to `prompts/development.md` is also minor (names a new tool that's available; does not change methodology) per `engine-manifest.md` §5 ("The engine version does not increment on... Minor elaborations within an existing spec's scope per the OI-002 substantive-vs-minor heuristic").

### §4d Engine-v disposition

**Engine-v9 preserved**. Preservation window count 3 → 4. No spec edit at engine-definition substantive level; both Direction A's are engine-adjacent implementation edits + one minor documentary spec edit. §5.4 cadence minority does not re-escalate per the v5–v9 content-driven-bump precedent chain.

### §4e Forward-convention observations

- **Path T+L reification at n=2**: S052 first-instance + S054 second-instance. Path T+L bundled label (Triage-Classify + minor Path L Implementation Fix) becomes a routine pattern.
- **First-instance multi-intake same-session resolution**: S054 resolves two records same-session. EF-054 record itself flags this as a candidate; if successful, the pattern reifies as discipline-permissible.
- **D-129 standing discipline ninth-consecutive clean exercise**: five considered-and-rejected non-Path-T+L alternatives surfaced above.
- **D-138 folder-name default ninth-consecutive clean exercise**: `provenance/054-session/` no suffix, no slug.

## §5 Work plan

Eleven steps, ordered:

1. **Commit `00-assessment.md` pre-work** per D-017 spirit + S048/S049/S050/S051/S052/S053 precedent chain. Establishes assessment as preserved provenance before substantive edits.

2. **Implement EF-053 Direction A** in `tools/retrieval_server.py`:
   - Add module-level `_ID_TOKEN_RE` regex matching the ID family (D-NNN, OI-NNN, WX-N-N, EF-NNN-..., engine-vN, §N(.N)*(-MN)?, d01N_N).
   - Add module-level `_sanitize_query(query: str) -> str` helper that wraps recognized ID patterns in phrase quotes, leaving already-quoted IDs untouched.
   - Modify `search()` to call `_sanitize_query()` on the input query; pass the sanitized result to FTS5 as the primary query (not phrase-wrapped); fall back to the full-phrase form on `OperationalError` (defensive).

3. **Implement EF-054 Direction A** in `tools/retrieval_server.py`:
   - Add a new `@mcp.tool()` decorated function `forward_references(target: str) -> dict`.
   - Query: `SELECT source_path, line, context_snippet, id_kind FROM identifiers WHERE id_text = ? OR canonical = ? ORDER BY source_path, line`.
   - Result envelope: `{available, degraded, missing, index_mtime, index_fresh, rebuilt_on_demand, results: [{path, line, context, kind}], count}`.

4. **Smoke-test both fixes** via `.cache/venv/bin/python` direct invocation (substrate-mirror path consistent with S051/S052/S053):
   - EF-053 expected: `search("D-129 standing discipline")` returns ≥1 result without crash; `search("WX-50-1 phase-2 gate")` returns ≥1 result; `search("retrieval contract")` (non-hyphenated control) still returns expected results.
   - EF-054 expected: `forward_references("S053")` returns 19 records all in `provenance/050-session/` (matching the EF-054 record's empirical demonstration); `forward_references("D-172")` returns ≥1 record pointing to engine-v9 establishment; `forward_references("NONEXISTENT-999")` returns count=0 + empty results (not error).

5. **Amend `prompts/development.md`** §How to operate adding a sentence naming `forward_references` as available at session open (minor documentary). Single sentence; non-prescriptive.

6. **Create triage records**:
   - `engine-feedback/triage/EF-053-search-query-parser-unquoted-hyphen-fts5-not-operator.md` per `workspace-structure.md` v6 §engine-feedback schema. `disposition: resolved-via-direction-a`. Reference D-186.
   - `engine-feedback/triage/EF-054-forward-reference-mcp-tool-for-session-open-commitment-audit.md` per same schema. `disposition: resolved-via-direction-a`. Reference D-187.

7. **Update `engine-feedback/INDEX.md`** status summary: 2 new / 1 triaged / 4 resolved → 0 new / 1 triaged / 6 resolved. Update Records table dispositions for EF-053 + EF-054.

8. **Write `02-decisions.md`** with four decisions:
   - **D-185** Path T+L ratified `[none]` single-agent reason.
   - **D-186** EF-053 Direction A adoption + `tools/retrieval_server.py` edit `[d016_2]` minor (per OI-002 + 8-precedent chain).
   - **D-187** EF-054 Direction A adoption + `tools/retrieval_server.py` extension + `prompts/development.md` documentary amendment `[d016_2 + d016_3]` minor (per OI-002 + 9-precedent chain).
   - **D-188** Housekeeping `[none]` consolidation.

9. **Write `03-close.md`** with WX-35-1 claim discipline §1c, validator-status §1d, engine-v disposition §1e, operational warrants §2, engine-v §3, minorities §4, watchpoints §5, no-substrate-§6 (S054 is post-window so no WX-50-1 recording obligation; observational note only), forward observations §7, honest limits §8, aggregate impact §9, meta-observations §10, commit §11.

10. **Append `SESSION-LOG.md`** thin-index row per `workspace-structure.md` v6 §SESSION-LOG. ≤180-word target per Q5=(a).

11. **Validate, commit, push**. Run `tools/validate.sh`; expect PASS with similar warning profile to S053 close (12-14 warnings; +0–2 new "no rejected alternatives" for D-185–D-188 design-intent).

## §6 Halt/operator-question state

Operator path is default-ratified (no Halt-1 surfaced; operator input is thin `PROMPT.md` only). Q1–Q5 standard defaults apply:

- **Q1** (path classification): (a) Path T+L ratified.
- **Q2** (Direction A vs B vs C for EF-053): (a) Direction A.
- **Q3** (Direction A vs B vs C for EF-054): (a) Direction A.
- **Q4** (engine-v disposition): (a) engine-v9 preserved.
- **Q5** (SESSION-LOG row size target): (a) ≤180 words thin-index per workspace-structure.md v6 §SESSION-LOG.

Recommended-default for each.

## §7 Honest limits

1. **MCP stdio transport remains unverified in-session.** Same as S051/S052/S053. Smoke-tests use `.cache/venv/` direct SQL/Python; FastMCP stdio wiring is not exercised. The new `forward_references` tool's MCP-stdio behaviour is inferred from the equivalent SQL behaviour, not directly verified. If the MCP server were started, `forward_references` would be callable via the same MCP protocol as `search`/`resolve_id`; this inference is sound but unverified.

2. **Substrate cache state assumed-working from S053.** `.cache/retrieval.db` and `.cache/venv/` are gitignored and survive across sessions; S053 used them successfully. If `.cache/retrieval.db` is missing or stale, the smoke-test will rebuild it via the existing mtime trigger before testing the fixes — adds rebuild time but does not block.

3. **EF-053 ID pattern set is curated, not exhaustive.** I'll match D-NNN, OI-NNN, WX-N-N, EF-NNN-..., engine-vN, §N(.N)*(-MN)?, d01N_N. Identifiers outside this family (e.g., d016_2 trigger codes are inside; `S053` is a session pattern; `[d008_2_convention_forward_discipline]` style trigger codes wider than the curated regex) may still hit the FTS5 NOT-operator parse failure if used directly in `search()`. The curated set covers the dominant ID families exercised in the workspace's provenance; broader coverage can be added later if friction reappears.

4. **EF-054 Direction A is additive; observational value unproven.** S054 implements + smoke-tests `forward_references` but does not exercise it in routine session-open audit (which would be S055+ behaviour per the paired `prompts/development.md` amendment). The empirical demonstration that the tool catches missed forward-commitments will require S055+ practice. Honest-limit recorded.

5. **`prompts/development.md` amendment is minor but is an engine-definition file edit.** Per `engine-manifest.md` §5, minor elaborations within scope do not bump engine-v. This amendment names a new tool that's available; does not redefine the Read activity. Classification minor per OI-002 16th data point (S041 D-126 last-updated count) + 17th data point.

6. **Forward-commitment relay still depends on close-narrative discipline.** EF-054 Direction A surfaces an MCP tool that lets agents query for forward-commitments at session open; it does NOT change the upstream discipline that close-narrative §7 should enumerate forward-commitments accurately. The S053 EF-054 demonstration showed two P1-raw commitments (Criterion 3 rebuild-latency, Criterion 6 adoption-sunset) were silently dropped at S050→S051→S052→S053 close-narrative relay. The new tool catches the gap structurally; the upstream discipline remains a separate concern.

7. **Path T+L reification at n=2 with multi-intake extension is a new pattern variant.** S052 was Path T+L with 1 record. S054 is Path T+L with 2 records (multi-intake). The pattern-name remains "Path T+L"; the n-counter advances by 1 (not 2) per `provenance/051-session/03-close.md` §10 reification convention. Multi-intake variant could be observed forward as a sub-pattern but is not formally distinguished at S054 close.

8. **Operator framing about "do not introduce queries rather add MCP features" is recorded in the post-S053 commit message and the EF-054 inbox record, not in operator session input at S054 open.** I'm treating this as durable direction (operator's stance recorded in workspace artefacts) rather than session-open Halt input. If the operator's S054 actual stance differs, the path-selection decision is the one reversible element (new decision in subsequent session could supersede).

9. **D-129 standing discipline ninth-consecutive clean exercise but partial overlap with operator-direction-already-given case.** The five rejected alternatives surfaced are honestly considered, but the choice was strongly indicated by both (a) the EF-054 inbox record's own pattern proposal and (b) the post-S053 commit message's operator framing. The "considered" qualification is genuine but not deeply uncertain. Honest-limit recorded.

10. **Substrate-smoke-test bias toward known-good queries.** S053 honest-limit 4 noted 12-query session was higher than typical Path A. S054 will smoke-test EF-053 fix on `search("D-129 standing discipline")` (the original failure case) + 1–2 control queries; smoke-test EF-054 on `forward_references("S053")` (the original demonstration case) + 1–2 controls. Cherry-picked to demonstrate fix; not exhaustive against the broader query-class space. Sufficient for source-realignment confidence; not a substitute for organic use over multiple sessions.

## §8 Carry-forwards to close

Items to revisit at S054 close:
- D-129 ninth-consecutive verification (path: clean exercise).
- D-138 ninth-consecutive folder-name-default verification (path: `054-session` clean).
- Engine-v9 preservation window count 3 → 4 (path: preserved at close unless Direction C alternative emerges mid-session, which it will not).
- WX-28-1 twenty-fourth close-rotation (S048 rotates OUT; S054 enters).
- WX-24-1 MAD v4 twenty-seventh-session no-growth (path: unchanged unless MAD edit, which there will not be).
- WX-34-1 remediation preservation (path: SESSION-LOG growth ≤180 words; total at close ~5,910 words; well under 6K).
- WX-35-1 standing discipline applied at close (claim discipline §1c).
- §10.4-M2 continued-preservation; §10.4-M5 discharged-as-vindicated already; §10.4-M7 partial-activation observation continues; M8/M9/M10/M11 preserved-unactivated.
- S047 D-150 three deferred candidates (i)/(ii)/(iii) preserved for post-arc review (unchanged at S054).
- Path T+L reification at n=2 + multi-intake first-instance observation.
- §5.6 GPT-family-concentration window-ii ambiguity flag carries forward (no MAD this session; observation state unchanged).

## §9 Validator forecast

At close, expect: **1246+ PASS / 0 FAIL / 12–16 WARN → PASS**.

- 2 spec soft-warnings (`multi-agent-deliberation.md` 6,637 + `reference-validation.md` 7,160).
- 12 pre-existing "no rejected alternatives found" design-intent warnings (2 per session × S046/S047/S048/S051/S052/S053).
- 0–4 new "no rejected alternatives" warnings for S054 `02-decisions.md` D-185+D-186+D-187+D-188 (each cites alternatives via cross-file reference to `00-assessment.md` §4a/§4b/§4c; validator regex matches per-decision body).

Aggregate default-read forecast: ~73,000 words across 21 files at close (S048 rotates OUT ~3,500 words; S054 enters ~3,800 words; net delta ~+300; SESSION-LOG growth ~+150). Comfortable headroom to §2b 90K soft.

## §10 Halt state at end of assessment

Session remains open. Proceeding to Step 2 (implement EF-053 Direction A) immediately after committing this assessment.

Halt-1 default-ratified. No operator question pending. If operator surfaces any divergence post-assessment-commit, the path-selection decision is reversible via subsequent-session decision; assessment + decision-commits are append-only provenance.
