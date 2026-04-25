---
triage_id: EF-054-triage
feedback_ref: ../inbox/EF-054-forward-reference-mcp-tool-for-session-open-commitment-audit.md
triaged_in_session: 054
triaged_at: 2026-04-25
status: resolved
classification: minor
disposition: Direction A (forward_references MCP tool) adopted this session via minor implementation extension to tools/retrieval_server.py paired with minor documentary amendment to prompts/development.md §How to operate naming the new tool; phase-1-compatible additive extension per retrieval-contract.md v1 §2 (contract names search + resolve_id as required minimum; additional tools permitted); operator framing "do not introduce queries rather add MCP features" (post-S053 commit message + EF-054 inbox record) directly honoured by adding the MCP surface rather than instructing agents to write SQL at session open
opened_issue: null
spec_amendments:
  - path: prompts/development.md
    classification: minor
    note: "§How to operate paragraph following inbox-triage clause adds a sentence naming the forward_references(target) MCP tool as a useful diagnostic at session open for surfacing forward-commitments; explicitly notes the tool is additive to the contract minimum and not required (agents using prose-scan reading still satisfy the read discipline)"
tool_amendments:
  - path: tools/retrieval_server.py
    classification: minor
    note: "new @mcp.tool() forward_references(target: str) -> dict; queries identifiers WHERE id_text=? OR canonical=? ORDER BY source_path, line; returns {results: [{path, line, context, kind}], count, available, degraded, missing, index_mtime, index_fresh, rebuilt_on_demand}; never raises on unknown target (count=0 + empty results); placement after _match_payload helper inside build_server closure (before return mcp)"
decision_records:
  - D-185
  - D-187
engine_version_impact: engine-v9 preserved (no bump; minor per OI-002 ninth source-realignment-or-extension precedent chain S022/S030/S033/S040/S046/S051/S052/S054-EF-053/S054-EF-054; prompts/development.md amendment is minor per engine-manifest §5 "Minor elaborations within an existing spec's scope per the OI-002 substantive-vs-minor heuristic" — names a new available tool, does not change methodology)
direction_selected: A
alternative_directions_deferred:
  - direction: B
    label: commitments_landing_at(session) semantic variant
    why_deferred: Direction A delivers the structural "all occurrences" surface; Direction B's semantic classification (commitment_type derived from regex on context_snippet) adds complexity without demonstrated value at this scale. If Direction A is in routine use after several sessions and forward-commitment-fidelity demonstrably improves, Direction B becomes a natural upgrade. Deferred-additive-compatible (Direction B is a strict superset of Direction A; can layer on top).
  - direction: C
    label: forward_commitments frontmatter convention + list_commitments_at MCP tool
    why_deferred: Substantive (adds frontmatter field to engine-definition close-file shape; touches prompts/development.md §Close obligation; possible engine-v bump). Depends on phase-2 frontmatter_kv table per S050 D-171 (currently deferred). Long-horizon target if substrate eventually moves toward structured-artefact framings (cf. §10.4-M10 Substrate-N2 minority); not phase-1-compatible and not appropriate at S054 minor triage.
---

# Triage — EF-054 forward-reference-mcp-tool-for-session-open-commitment-audit

## Classification

**Target**: engine-adjacent (implementation-level extension; minor documentary amendment to engine-definition prompt). **Severity on inbox record**: friction (forward-commitments are load-bearing methodology mechanism; selection-bias in close-narrative-only relay was empirically demonstrated to drop S050-issued P1 Criterion 3 + Criterion 6 commitments through S051 → S052 → S053). **Source**: `selvedge-self-development` Session 053 post-session operator-surfaced observation (`reported_by: operator`); recorded as direct-to-inbox per S050/S051 self-dev-originated convention.

**Disposition**: **resolved** this session via Direction A implementation extension + paired minor documentary amendment. Narrow directionally-clear extension; single-orchestrator same-session resolution per S048 D-152 + S052 D-181 precedent. EF-054 inbox record itself flagged Direction A as "most likely path" and named the paired `prompts/development.md` amendment.

## Defect summary (from inbox record)

Forward-commitments — preserved-minority activation warrants, watchpoint windows, "evaluate at S{NNN}" decisions, scheduled-MAD adoption sessions, criterion-firing checkpoints, "carry-forward to S{NNN}" notes — are recorded across prior sessions' provenance and must be re-discovered at every session open. The current discipline relies on close-narrative §7 next-session-recommendation sections, which relays only what each closing session's Case Steward chose to surface (selection-bias prone).

Empirical demonstration in EF-054 record: `SELECT * FROM identifiers WHERE id_text='S053'` returned 19 line-precise records all in `provenance/050-session/`. Of those 19, S053 only addressed ~17 in close: two P1-raw-perspective commitments (Criterion 3 rebuild-latency p95 ≤ 500ms across 10 rebuilds; Criterion 6 adoption-sunset two-consecutive-session check-24-failure) were silently dropped through the S050 → S051 → S052 → S053 close-narrative relay chain.

The contract's `resolve_id` returns first-occurrence (§2.2); `search` returns BM25-ranked documents (§2.1). Neither tool returns *all* occurrences of an identifier as a structured list — which is exactly what session-open forward-commitment audit requires. Substrate phase-1 data is sufficient (the `identifiers` table is line-keyed and indexed at every session open per §4); the MCP surface was the gap.

Operator framing recorded in post-S053 commit message: *"do not introduce queries rather add MCP features"*. Direction A honours this directly by adding an MCP tool that exposes the existing line-keyed data, rather than instructing agents to write SQL queries at session open.

## Adoption — Direction A (`forward_references` MCP tool)

Per inbox record §Suggested Change Direction A:

> Add a new MCP tool to `tools/retrieval_server.py`:
>
> ```
> forward_references(target: str) -> list[{path: str, line: int, context: str, kind: str}]
> ```
>
> **Semantics**:
> - Returns *all* occurrences of `target` in the `identifiers` table (NOT just the first per `resolve_id` semantics; NOT BM25-ranked per `search` semantics).
> - Sorted by `source_path` then `line` for deterministic output.
> - `kind` propagated from the existing `identifiers.id_kind` column.
> - Returns empty list (not error) if target is unindexed.

Implementation (`tools/retrieval_server.py`, this session):

1. Added new `@mcp.tool()` decorated function `forward_references(target: str) -> dict` inside `build_server` closure, placed after `_match_payload` helper and before `return mcp`.
2. Query: `SELECT source_path, line, context_snippet, id_kind FROM identifiers WHERE id_text = ? OR canonical = ? ORDER BY source_path, line`. The `OR canonical = ?` clause makes the tool more useful than the EF-054 record's `WHERE id_text='S053'` baseline: it captures references regardless of whether the surface form matches the canonical (e.g., `Session 053` text rendered as `S053` canonical via `build_retrieval_index.py` session-pattern normalisation).
3. Result envelope: `{results: [{path, line, context, kind}], count, available, degraded, missing, index_mtime, index_fresh, rebuilt_on_demand}` — same envelope shape as `search` and `resolve_id` for consistency. `count` is `len(results)` for caller convenience.
4. Failure mode: `ensure_index` exception returns `{available: False, reason: str(e), results: [], count: 0}` per `retrieval-contract.md` v1 §3 clause 1. `degraded: False` and `missing: []` because `forward_references` does not consume `aliases.yaml` — pure `identifiers`-table query (Strategy 1-equivalent).
5. Never raises on unknown target: returns `{available: True, count: 0, results: []}` for unindexed input.

Paired minor documentary amendment to `prompts/development.md` §How to operate adds a sentence naming the new tool as a useful diagnostic at session open. Single sentence; explicitly notes the tool is additive (not required); agents using prose-scan reading still satisfy the read discipline.

## Smoke-test evidence

Test harness at session-scope. Index rebuilt this session (461 documents / 51,724 identifiers; rebuild triggered by mtime check after S054 00-assessment.md was committed) so EF-054 inbox record is captured.

| Target | Expected | Result |
|--------|----------|--------|
| `S054` | ≥1 record, including own assessment file + EF-053/EF-054 inbox files | PASS (57 records across 8 files) |
| `D-172` | ≥1 record pointing to engine-v9 establishment | PASS (54 records across multiple files) |
| `EF-053` | ≥1 record in own inbox file + S053 close + S054 assessment | PASS (44 records across 6 files) |
| `EF-054` | ≥1 record in own inbox file + S054 assessment | PASS (25 records across 2 files; assessment file dominant — expected, since EF-054 is a new identifier) |
| `§10.4-M5` | ≥1 record across workspace-structure.md + retrieval-contract.md + many cites | PASS (103 records across 38 files) |
| `NONEXISTENT-999` | 0 records, no error | PASS (count=0; empty results) |
| `D-185` (this session's path-ratification decision) | ≥1 record (in 00-assessment.md cite) | PASS (3 records) |

7-of-7 PASS via `tools["forward_references"](target=...)` invocation of the FastMCP tool closure.

**Operational evidence**: `forward_references("S054")` at session-open (post-rebuild) returned 57 records including 5 from `engine-feedback/inbox/EF-054-forward-reference-mcp-tool-for-session-open-commitment-audit.md` and 1 from `provenance/053-session/00-assessment.md`. This confirms the tool would have surfaced the EF-054 record itself if it had existed at S054 open as a forward-commitment from S053. The pattern works as designed.

## Classification — minor per OI-002

Ninth minor bug-fix-style-or-extension implementation-realignment in engine history. Precedent chain:

1. S022 R8a — SESSION-LOG.md thin-index restoration.
2. S030 D-100 — `workspace-structure.md` §SESSION-LOG stale-literal cleanup.
3. S033 D-108 — `validate.sh` check 22 loop-bug repair.
4. S040 D-123 — SESSION-LOG.md thin-index preemptive restoration.
5. S046 D-143 — `validate.sh` empty-provenance nounset + check 23 ls-glob set-e guards.
6. S051 D-178 — SESSION-LOG.md forced thin-index restoration per WX-34-1 breach.
7. S052 D-181 — `retrieval_server.py` Strategy 1.5 alias-indirection (EF-051).
8. S054 D-186 — `retrieval_server.py` `_sanitize_query()` query-parser fix (EF-053).
9. **S054 D-187** — `retrieval_server.py` `forward_references` tool extension + `prompts/development.md` documentary amendment (EF-054).

Per OI-002 bug-fix-style-or-additive-extension-without-semantic-change heuristic + engine-manifest §5 "Minor elaborations within an existing spec's scope per the OI-002 substantive-vs-minor heuristic": the contract `retrieval-contract.md` v1 §2 explicitly permits additional tools beyond the required minimum (`search` + `resolve_id`); §6 phase-2 list names further tools but does not forbid pre-phase-2 additions. The `prompts/development.md` amendment names a new available tool without changing the Read activity's substantive content. No engine-v bump. Engine-v9 preserved.

## Direction B + Direction C deferred

**Direction B** (`commitments_landing_at(session)` semantic variant) is **not adopted** this session. Rationale:

1. Direction A delivers the structural "all occurrences" surface that the inbox record's empirical demonstration shows is sufficient (the operator's own `SELECT * FROM identifiers WHERE id_text='S053'` query is the same shape).
2. Direction B's semantic classification (commitment_type derived by regex on context_snippet) adds runtime complexity without demonstrated value at this scale — the agent can apply per-call classification heuristics on the returned records if needed, without bundling them into the tool contract.
3. Direction A is **additive-compatible** with Direction B — Direction B is a strict superset of Direction A; can layer on top if the structural surface proves insufficient.

**Direction C** (`forward_commitments:` frontmatter convention + `list_commitments_at` MCP tool) is **rejected for S054** per inbox record's own analysis. Rationale:

1. Substantive: adds a frontmatter field to engine-definition close-file shape; touches `prompts/development.md` §Close obligation; possible engine-v bump.
2. Depends on phase-2 `frontmatter_kv` table per S050 D-171 (currently deferred to phase-2 gating).
3. Long-horizon target if substrate eventually moves toward structured-artefact framings (cf. §10.4-M10 Substrate-N2 minority); not phase-1-compatible.

## Forward observations

- **First-instance multi-intake same-session resolution.** S054 resolves both EF-053 + EF-054 in the same session (Path T+L bundled label, n=2 reification). Prior precedent: S048 EF-001 (Path T single record, single direction); S052 EF-051 (Path T+L single record, Direction B); S054 EF-053 + EF-054 (Path T+L two records, both Direction A). Pattern is discipline-permissible: each record gets its own decision (D-186 + D-187) and triage record (this file + EF-053-triage); no laundering of unrelated work.
- **`forward_references` exercising at S055+ is the demonstration window.** S054 implements + smoke-tests the tool but does not exercise it in routine session-open audit (which would be S055+ behaviour per the paired `prompts/development.md` amendment). The empirical demonstration that the tool catches missed forward-commitments will require S055+ practice. If S055 Case Steward calls `forward_references(f"S{555:03d}"... wait, `forward_references("S055")`)` at session open and surfaces a forward-commitment that close-narrative relay had dropped, the value-evidence accumulates organically.
- **Phase-1 paused state at S054 (per S053 close §6) is unchanged by this addition.** WX-50-1 phase-2 gate did NOT fire under stricter counting at S053 close. EF-054 Direction A is an additive phase-1-compatible tool; it does not force phase-2 adoption nor extend the WX-50-1 observation window. Phase-2 re-evaluation triggers per S053 close §6 forward observation continue to apply (EF-053 organic-use-case, external-workspace adoption, structured-filter / graph-traversal fallback).
- **Operator framing "do not introduce queries rather add MCP features" honoured.** The amendment to `prompts/development.md` does NOT instruct agents to write SQL at session open; it names the MCP tool that exposes the same data. This preserves the agent's discipline of using the documented MCP surface rather than direct DB queries (which would tightly couple agent behaviour to the substrate's schema).
- **`OR canonical = ?` clause makes tool slightly more useful than the inbox record's baseline.** The inbox demonstration used `WHERE id_text='S053'` (returning 19 records). My implementation uses `id_text = ? OR canonical = ?` (returning 40+ records for `S053` post-rebuild including matches where `id_text='Session 053'` canonicalizes to `S053`). This is a mild scope-expansion documented for transparency; if it proves noisy, future tuning can narrow to id_text-only.
- **Idempotence and stability of forward_references**: the tool depends only on the `identifiers` table; no aliases, no FTS5, no query parser involvement. It cannot exhibit the EF-053 hyphen-as-NOT-operator pathology because the comparison operator is `=` (exact match) on text, not FTS5 MATCH.

## OI impact

No OI opened. No OI resolved. OI-019 unchanged by this triage (sub-questions (a)–(f) not touched). EF-054's mention of "forward-commitment-fidelity" is operationally orthogonal to OI-019's path-selection-work-channel scope.

## Subsumed deferred candidates

None. S047 D-150 three remaining deferred candidates (i)/(ii)/(iii) unchanged.
