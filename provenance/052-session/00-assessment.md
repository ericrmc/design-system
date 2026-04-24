---
session: 052
title: Assessment — Path T+L default-agent Triage-classify + minor Path L implementation fix for EF-051 (aliases.yaml not consulted at query time); single-orchestrator; operator "Proceed with default agent path and do not halt." treats Halt-1 as default-ratified
date: 2026-04-25
status: in-progress
---

# Assessment — Session 052

## §1 State at session open

**Engine version**: `engine-v9` preserved; preservation window count **1** entering S052 (established S050 D-172; S051 first post-v9 session preserved).

**Validator at open** (pre-edit): `1224 PASS / 0 FAIL / 10 WARN → PASS` (identical to S051 close; no edits between close and open). Ten warnings breakdown:
- 2 spec soft-warnings (`multi-agent-deliberation.md` 6637 + `reference-validation.md` 7160; designed per S024 A.4 + S033 carry-forward).
- 8 "no rejected alternatives found" design-intent warnings across S046/S047/S048/S051 `02-decisions.md` files (2 entries per file for housekeeping decisions where no substantive alternatives exist to list).

**Aggregate default-read surface at open**: ~71,061 words across 21 files (per S051 close §9; well under §2b 90K soft with ~19K headroom). SESSION-LOG.md at ~4,846 words (well under 6K soft with ~1,154 headroom post-S051 compression).

**Active OIs**: 13 unchanged (OI-002 open heuristic-stable 16th data point; OI-005/006/007/008/009/011/012/013/014/015/016/018/019 various states per `open-issues/index.md`). No OI opened/resolved since S048.

**First-class minorities preserved**: 36 engine-wide (§10.4-M1 discharged-not-vindicated / M2 continued preservation / M3/M4/M6 preserved-against-future-event-horizon / M5 discharged-as-vindicated / M7–M11 first observation-window data points from S051 close all non-activating / §5.1/§5.4/§5.5/§5.6/§5.7/§5.8/§5.9/§5.10/§5.11/§5.12/§5.13/§5.14 + S024 A.4 four + S027 §A/§B/§C + reference-validation v3 §10.1/§10.2/§10.3).

**Engine-feedback state at open**: **1 new** (EF-051) / 1 triaged (EF-047-brief-slot-template deferred per S050 D-174) / 3 resolved / 0 rejected. EF-051 was newly intaked at S051 close per D-179 §D-179a substrate-smoke-test defect finding.

**Substrate state**: `.cache/retrieval.db` present (34.1 MB; 448 docs / 48,852 identifiers built at S051 smoke-test). `.cache/venv/` present (pyyaml + mcp[cli] installed at S051). Workspace session does not have MCP server connected (ToolSearch does not surface `mcp__selvedge_retrieval__*`); substrate exercisable only via direct SQL or command-line python.

## §2 Operator agenda

Operator input this session is thin: `/clear` + `PROMPT.md` + verbatim "Proceed with default agent path and do not halt."

No operator-surfaced scope. No Path PD/OS/OC classification triggered. No mid-session ratification halt invited. The "do not halt" directive means all Halt-1 questions are treated as default-ratified at the recommended-option position per this assessment.

## §3 Case Steward factual checks

### §3a Engine-feedback inbox state

Per `prompts/development.md` §How to operate paragraph: "If `engine-feedback/INDEX.md` shows feedback records with `status: new`, the session's Assess activity should consider whether triage of one or more inbox items is the right increment for this session."

EF-051 intake at `engine-feedback/inbox/EF-051-aliases-yaml-not-consulted-at-query-time.md` carries `status: inbox`; INDEX.md reports `status: new`. Triage is an available session increment.

S051 close §7 recommendation: "EF-051 awaits triage; status `new` at S052 open. Recommended: triage at S052 (Path T — per S048 precedent — if inbox becomes primary session agenda) OR bundled with other work if operator surfaces different agenda." Operator surfaced no different agenda. Path T candidate applies.

S048 D-152 Path T precedent: single-orchestrator Case Steward; inbox triage + (where direction is clear) same-session resolution. S048 resolved EF-001 via substantive adoption in-session; triaged three EF-047 records to S049 MAD scheduling. EF-051's proposed dispositions (Direction A index-time reverse-remap; Direction B query-time aliases consultation) are narrow and implementation-level; direction is clear enough for single-orchestrator same-session resolution.

### §3b EF-051 technical substance verification

Per reading `engine-feedback/inbox/EF-051-aliases-yaml-not-consulted-at-query-time.md` + `tools/build_retrieval_index.py` + `tools/retrieval_server.py` + `specifications/aliases.yaml`:

**Layer 1 confirmed.** `build_retrieval_index.py` `load_aliases()` (lines 128–149) loads entries then at lines 235–241 applies:
```python
cur.execute(
    "UPDATE identifiers SET canonical = ? WHERE id_text = ?",
    (canonical, alias),
)
```
The UPDATE is a no-op whenever `alias` is not already present in the `identifiers` table as `id_text`. The `identifiers` table is populated by `extract_identifiers()` (line 109) which only inserts rows matching ID_PATTERNS regexes (D-NNN / OI-NNN / §N.N-MN / WX-N-N / SNNN / engine-vN / EF-NNN-... / d01N_N). An alias like `"M5"` or `"Reviser OI-tag-only"` has no matching regex, so no row exists to UPDATE; the alias is inert.

**Layer 2 confirmed.** `retrieval_server.py` `resolve_id()` (lines 169–229) uses three strategies:
- Strategy 1 (line 185–192): direct `canonical = ?` lookup.
- Strategy 2 (line 197–204): direct `id_text = ?` lookup.
- Strategy 3 (line 208–216): `ID_LIKE_RE` pattern-matched LIKE prefix.

None consults `aliases.yaml` at query time. `ID_LIKE_RE` at line 39–42 requires the same regex set as ID_PATTERNS — `"M5"` alone does not match (`§\d+(?:\.\d+)*(?:-M\d+)?` requires leading `§`).

**Verified defect**: of the 8 seed aliases in `specifications/aliases.yaml`, 0 resolve to their canonicals via `resolve_id()`. This contradicts `retrieval-contract.md` v1 §2.2: "If `alias` matches an `aliases[]` entry in `specifications/aliases.yaml`, resolves to the corresponding canonical."

### §3c Minority-activation-warrant check

- **§10.4-M1** discharged-not-vindicated (S046); unchanged. No trigger fires.
- **§10.4-M2** continued preservation; S051 engine-feedback exercise (EF-051 intake) is further exercise of the pathway. No trigger fires (pathway functioning).
- **§10.4-M3/M4/M6** dispatcher-alternative minorities; unchanged.
- **§10.4-M5** discharged-as-vindicated (S048); unchanged.
- **§10.4-M7** phase-1 WX-50-1 non-firing + zero-use 3+ consecutive sessions activation warrant. S051 exercise was non-zero (2 search + 5 resolve_id). Not activated.
- **§10.4-M8** DuckDB structured-first dominance. No structured-filter queries this session or S051. Not activated.
- **§10.4-M9** engine-definition-at-adoption inconsistent-inheritance. No external-workspace re-bootstrap. Not activated.
- **§10.4-M10** Substrate-N2 reframe. Phase-2 not yet fired. Not activated.
- **§10.4-M11** `syncs_with:` fold-vs-preserve. Phase-2 `edges` deliberation not scheduled. Not activated.
- **§5.12 Path-Selection Defender reopen warrants** (a) D-129 convention degradation: S052 applies D-129 cleanly (this §4a below). (b) OI-019 evidence-free-convergence: not applicable. (c) §5.3-analog recurrence: not applicable. No trigger fires.
- **§5.13/§5.14** unchanged; no trigger fires.
- **read-contract minorities** §5.1/§5.4/§5.5/§5.6/§5.7/§5.8/§5.9/§5.10/§5.11 unchanged; no trigger fires.
- **reference-validation v3 §10.1/§10.2/§10.3** unchanged; no trigger fires.

No minority activation independently of EF-051 triage.

### §3d WX-50-1 phase-2 gate status at S052 open

Per `retrieval-contract.md` v1 §6 recording obligation, S050–S053 close records substrate use. State at S052 open (from S050+S051 closes):
- **Condition 1** (≥2 sessions in S050–S053 record ≥1 `results_used_with_artefact_id` entry): S050 = 0; S051 = 2. **Primed but not yet satisfied** (needs another session with ≥1 entry).
- **Condition 2** (≥1 session records ≥1 fallback where missing capability is structured-filter OR graph-traversal): S051 recorded 1 fallback but category was alias-indirection; **does NOT satisfy**.
- **Condition 3** (≥1 external-workspace adoption records ≥1 useful domain-context query): not yet. selvedge-disaster-response not run.

**S052 WX-50-1 recording obligation**: if S052 substantive work uses substrate queries, record in 3-field section at close. If Direction B fix is adopted and smoke-tested, the smoke-test calls themselves are substrate use eligible for recording.

### §3e SESSION-LOG pressure check

SESSION-LOG.md at open: 4,846 words (compressed at S051). S052 thin-row (≤180 words) forecast ~5,000 post-append; well under 6K soft warning with ~1K headroom. No WX-34-1 pressure.

## §4 Path classification

**Path T+L** (Triage-classify + minor Path L implementation fix). Two-label forward-naming convention:

- **T** = S048 Path T precedent for inbox-triage default-agent path (reified at n=2 if S052 executes the pattern).
- **L** = reified default-agent path-label at n=2 (S040 D-123 + S051 D-177 Path L+A); for minor source-edit work.
- **T+L** = bundled triage + same-session minor-amendment resolution. New forward-naming candidate; first-instance this session.

Single-orchestrator Case Steward per S048 Path T precedent + S051 Path L+A precedent. No MAD (direction is narrow; implementation-level defect with two directionally-clear repair options; not substantive spec revision).

Folder name `052-session` per D-138 standing discipline (seventh consecutive clean exercise after S046/S047/S048/S049/S050/S051).

### §4a D-129 standing discipline — five considered-and-rejected non-Path-T+L alternatives

Per D-129 (S043 forward convention graduated to standing discipline at S046 D-146), session-open assessments MUST surface ≥1 considered-and-rejected non-Path-A alternative with non-vacuous rationale. Seventh-consecutive clean exercise (S046/S047/S048/S049/S050/S051/S052).

1. **Path A (Watch) pure** — rejected. Leaves EF-051 in `status: new` for another session with no operational reason to delay. Contradicts `prompts/development.md` §How to operate which instructs Assess to consider inbox triage when records exist with `status: new`. Path A does not extend preservation value here (engine-v9 window depth 1 → 2 is not a load-bearing milestone).

2. **Path T pure (triage-only, defer implementation)** — rejected. EF-051's proposed directions are narrow and directionally clear; the operator's own intake record recommends "S052 or later — single-orchestrator minor-amendment Path L. Not MAD-required". Triage-only would transition `new` → `triaged` but leave the substrate partially-unfulfilled against the phase-1 contract. Single-orchestrator same-session resolution (S048 Path T precedent for EF-001) is the operational default when direction is clear.

3. **Path L pure (implementation-only, skip triage-record)** — rejected. The `engine-feedback/` lifecycle convention (workspace-structure.md v6 §engine-feedback) requires triage-records per-feedback; skipping would leave INDEX.md with no linkage between the intake and the resolving session's decisions. Triage-record is the canonical resolution pointer per the §engine-feedback "Status lifecycle: outbound → inbox → triaged → resolved | rejected" clause.

4. **Path MAD (4-perspective deliberation on Direction A vs Direction B vs both)** — rejected. No substantive-revision-scale question: neither direction amends `retrieval-contract.md` v1 §2.2 (the contract is correct per its own text); both directions fulfill the contract; minor per OI-002 bug-fix-without-semantic-change heuristic per the 7-precedent chain (S022/S030/S033/S040/S046/S051). MAD convening for a narrow implementation fix would invert proportionality (EF-047-retrieval-discipline warranted MAD at S050 because kernel amendment + new engine-definition spec were on the scope; EF-051 has neither). Convention: substantive scope → MAD; narrow-implementation direction-clear → single-orchestrator.

5. **Path L+A (SESSION-LOG preemptive restructure) again** — rejected. SESSION-LOG at 4,846 words post-S051-compression is well under 6K soft warning; no WX-34-1 pressure triggering restructure. Re-exercising Path L+A twice in two sessions would be premature.

### §4b Direction selection — Direction B (query-time aliases consultation)

Per EF-051 §Suggested Change, two independent directions are proposed. Selection rationale:

- **Direction A** (index-time reverse-remap) adds synthetic `identifiers` rows pointing to the canonical's declared location. Makes aliases searchable via FTS too (alias text becomes indexed). Requires rebuild to pick up `aliases.yaml` edits.
- **Direction B** (query-time aliases consultation) loads `aliases.yaml` once at server startup into a dict; `resolve_id()` gains a Strategy 1.5 between Strategy 1 (canonical direct) and Strategy 2 (id_text). Aliases file becomes authoritative at query time; no rebuild needed when aliases.yaml changes.

**Direction B selected** for these reasons:
1. Minimal surface change (server-only; no indexer edit; no schema change).
2. More consistent with "aliases.yaml is authoritative alias vocabulary" framing per retrieval-contract.md v1 §2.3.
3. Aliases.yaml edits become queryable without `build_retrieval_index.py` re-run — better UX for incremental alias population.
4. Direction A can be added later additively if FTS search over alias text becomes desired (no foreclosure).

Direction A deferred as optional additive. Not adopted this session.

### §4c Classification per OI-002

**Minor** per OI-002 bug-fix-without-semantic-change heuristic. The contract `retrieval-contract.md` v1 §2.2 is unchanged (and is correct as written). The implementation previously did not fulfill the contract; Direction B brings implementation into fulfillment. Per the 7-precedent chain of minor bug-fix-style source-realignments (S022 R8a SESSION-LOG thin-index restoration / S030 D-100 workspace-structure §SESSION-LOG stale-literal cleanup / S033 D-108 validate.sh check 22 loop-bug repair / S040 D-123 SESSION-LOG thin-index restoration / S046 D-143 validate.sh empty-provenance + ls-glob bug fix / S051 D-177 SESSION-LOG thin-index restoration), this is the **seventh minor bug-fix-style implementation-realignment edit**.

No engine-v bump. Engine-v9 preserved; preservation window count advances to 2 at close.

## §5 Proposed work plan

Single-orchestrator Case Steward. Twelve steps:

1. Commit this assessment pre-work per D-017 spirit + S048/S049/S050/S051 precedent chain. (Pre-work commit already scheduled this paragraph.)
2. Read the substrate implementation files in detail (`build_retrieval_index.py` + `retrieval_server.py` + `aliases.yaml`) — COMPLETE pre-assessment.
3. Edit `tools/retrieval_server.py` per Direction B: load aliases at server startup; add Strategy 1.5 to `resolve_id()`.
4. Smoke-test the fix via `.cache/venv` python invocation: verify 4 seed aliases resolve post-fix (`"M5"` → `§10.4-M5`; `"Reviser OI-tag-only"` → `§10.4-M5`; `"Decision 172"` → `D-172`; `"phase-2 gate"` → `WX-50-1`). Verify `"NONEXISTENT-999"` still returns None.
5. Create `engine-feedback/triage/EF-051-aliases-yaml-not-consulted-at-query-time.md` triage record with `status: resolved`, classification `minor`, cross-reference to S052 decision IDs.
6. Update `engine-feedback/INDEX.md`: status summary 1 new / 1 triaged / 3 resolved / 0 rejected → 0 new / 1 triaged / 4 resolved / 0 rejected; EF-051 row `status: new` → `status: resolved (S052 D-181)`.
7. Write `provenance/052-session/02-decisions.md` with decisions:
   - **D-180**: Path T+L ratified; single-agent reason (minor implementation-level fix per seventh source-realignment precedent chain + operator "do not halt" = default-ratified).
   - **D-181**: Direction B applied to `tools/retrieval_server.py` per EF-051 resolution; minor per OI-002; no engine-v bump.
   - **D-182**: Housekeeping (D-129 seventh-consecutive exercise; D-138 seventh-consecutive folder-name default; WX-28-1 twenty-second close-rotation; WX-24-1 twenty-fifth no-growth streak; WX-50-1 second-session 3-field recording; engine-v9 preservation window count 1 → 2).
8. Write `provenance/052-session/03-close.md` with §1a–§11 standard structure + WX-50-1 3-field section.
9. Append S052 thin-row to `SESSION-LOG.md` (≤180 words).
10. Run `tools/validate.sh`; verify PASS.
11. Commit all provenance + spec/tool changes with concise message.
12. Push to remote per `CLAUDE.md` workflow.

## §6 Honest limits

1. **Direction B adopted without deliberation.** Direction A and "both" are alternatives; operator could reject Direction B at any future session. Mitigation: Direction B is additive-compatible with Direction A (both can coexist); the minor implementation fix does not foreclose later additions.
2. **Smoke-test exercises SQL/Python layer directly, not MCP stdio transport.** Same honest-limit as S051 (workspace session has no MCP connection). MCP transport verification deferred.
3. **Smoke-test re-uses `.cache/retrieval.db` from S051 build.** The DB contains stale `identifiers` rows from S051; Direction B is a query-time fix so DB rebuild is not required for correctness. However, ensuring the fix actually queries aliases.yaml means testing against the same DB is adequate.
4. **Triage-record frontmatter schema adherence.** `workspace-structure.md` v6 §engine-feedback specifies triage frontmatter fields; S048 precedent established the active field shape. This session follows S048 precedent.
5. **No operator ratification of the Direction B choice.** The "do not halt" directive means operator accepts the default-agent path's discretion on direction selection.
6. **WX-50-1 second-session recording uses smoke-test calls as eligible entries.** If operator at a future triage disallows smoke-test calls as "session work" for WX-50-1 purposes, the phase-2 gate counts change (S051 + S052 become 1-of-2 eligible rather than 2-of-2). Defensible either way at S053 close per operator interpretation; recorded transparently.
7. **Case Steward synthesis bias** applies per MAD v4 §Limitations even for single-orchestrator work. Mitigated by EF-051 record itself being external input (written at S051 close as a defect finding); S052 is implementation of the recommended resolution.
8. **No new first-class minority preserved.** No deliberation; no dissent surface. 36 minorities preserved unchanged.
9. **This assessment self-grows the default-read aggregate.** S052 currently-active-session provenance is default-read per read-contract v5 §1 item 8 while session is open; becomes archive-surface on close.
10. **Engine-v9 preservation window count 1 → 2 is a modest extension.** Engine-v7 window was 11 (the prior record); engine-v9 at 2 is well below that but aligned with steady-state post-v-bump pattern. No cadence-minority concern.

## §7 Halt 1 — default-ratified per operator "do not halt"

Per operator directive "Proceed with default agent path and do not halt", Halt 1 is skipped. The following questions default-ratify at their recommended options:

- **Q1**: Proceed with Path T+L default-agent path? → (a) yes (default; proceed).
- **Q2**: Direction selection? → (b) Direction B (minimal fix; query-time aliases consultation).
- **Q3**: Smoke-test scope? → (a) test 4 seed aliases + None-case (recommended default).
- **Q4**: Engine-v impact? → (a) preserved engine-v9 (no bump; minor per OI-002 precedent).
- **Q5**: Additional operator agenda? → (default none; operator surfaced none).

Session remains in default-agent shape; no halt.

## §8 Carry-forwards to close evaluation

- **Engine-v9 preservation** window count 1 → 2 if session preserves (non-bump session expected).
- **D-129 seventh-consecutive** clean exercise per §4a above (standing discipline since S046 D-146).
- **D-138 seventh-consecutive** folder-name default exercise (`052-session` no suffix, no slug).
- **WX-28-1 twenty-second close-rotation** (S046 rotates OUT; S052 enters). Zero retention-exceptions expected.
- **WX-24-1** MAD v4 twenty-fifth-session no-growth streak if no MAD edit (expected).
- **WX-34-1** remediated at S051; S052 thin-row at ~180 words expected to maintain remediation.
- **WX-50-1 phase-2 gate second-session 3-field recording**; smoke-test calls eligible for `tool_calls_by_type` + `results_used_with_artefact_id`.
- **Path T+L first-instance**; reification deferred until n=2.
- **EF-051 inbox→triaged→resolved lifecycle** complete; engine-feedback state 1 new / 1 triaged / 3 resolved → 0 new / 1 triaged / 4 resolved.
- **§10.4-M7 activation warrant check**: S052 zero-use test — NOT zero-use if smoke-test calls count; activation warrant does not fire.
- **S047 D-150 three deferred candidates** (i)/(ii)/(iii) preserved for post-arc review. Unchanged.

## §9 Validator forecast at close

Expected: 1224+ PASS / 0 FAIL / 10+ WARN (new warnings possible for S052 02-decisions.md "no rejected alternatives" — D-180/D-182 are housekeeping/ratification without explicit alternatives block; alternatives for D-180 are referenced cross-file in this assessment §4a).

Expected aggregate: current-session provenance becomes archive-surface on close; S046 close rotates OUT; S052 close enters. Net aggregate change: approximately neutral (~70–71K). Well under §2b 90K soft with comfortable headroom.

## §10 Halt state

Session remains **open**. No operator halt invited. Proceeding to §5 step 3 (Direction B implementation edit) on assessment commit.
