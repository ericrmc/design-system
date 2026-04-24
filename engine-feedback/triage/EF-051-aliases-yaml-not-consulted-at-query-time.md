---
triage_id: EF-051-triage
feedback_ref: ../inbox/EF-051-aliases-yaml-not-consulted-at-query-time.md
triaged_in_session: 052
triaged_at: 2026-04-25
status: resolved
classification: minor
disposition: Direction B (query-time aliases consultation) adopted this session via minor implementation edit to tools/retrieval_server.py; Strategy 1.5 added between direct-canonical and id_text lookup; aliases.yaml loaded once at server startup via load_aliases_map(); retrieval-contract.md v1 §2.2 alias-indirection clause now fulfilled; smoke-test verifies 0-of-8 → 8-of-8 seed-alias resolution (8 cases pass including 5 alias-indirection + 2 direct-canonical + 1 None-case per §2.2 "Never raises on unknown alias")
opened_issue: null
spec_amendments: []
tool_amendments:
  - path: tools/retrieval_server.py
    classification: minor
    note: Strategy 1.5 (alias-indirection via load_aliases_map) added to resolve_id(); degraded-mode disclosure per retrieval-contract §3 clause 3 when pyyaml or aliases.yaml absent
decision_records:
  - D-180
  - D-181
engine_version_impact: engine-v9 preserved (no bump; minor per OI-002 seventh source-realignment precedent chain S022/S030/S033/S040/S046/S051/S052)
direction_selected: B
alternative_directions_deferred:
  - direction: A
    label: index-time reverse-remap
    why_deferred: Direction B is minimal surface change (server-only; no indexer edit; no schema change); Direction A additive-compatible if FTS search over alias text later becomes desired; no foreclosure
---

# Triage — EF-051 aliases-yaml-not-consulted-at-query-time

## Classification

**Target**: engine-adjacent (implementation-level, not engine-definition). **Severity on inbox record**: friction (substrate partially unfulfilled; primary ID resolution worked at S051 smoke-test). **Source**: `selvedge-self-development` Session 051 substrate-smoke-test (S051 D-179 §D-179a defect finding; first engine-feedback intake from substrate exercise per S050 §8 honest-limit forward-commitment pattern).

**Disposition**: **resolved** this session via Direction B implementation fix. Narrow directionally-clear defect; single-orchestrator same-session resolution per S048 D-152 Path T precedent (where direction is clear, triage + adoption execute in same session).

## Defect summary (from inbox record)

`specifications/retrieval-contract.md` v1 §2.2 declares: "If `alias` matches an `aliases[]` entry in `specifications/aliases.yaml`, resolves to the corresponding canonical."

Pre-S052 implementation:
- **Layer 1** (`tools/build_retrieval_index.py` `load_aliases()` at lines 128–149; UPDATE at lines 235–241): remaps `identifiers.canonical` WHERE `id_text = alias`. But `id_text` rows only exist for strings matching ID_PATTERNS regexes. Non-ID-pattern aliases (e.g., `"M5"`, `"Reviser OI-tag-only"`) have no `id_text` row to UPDATE; the alias is inert.
- **Layer 2** (`tools/retrieval_server.py` `resolve_id()` at lines 169–229): three strategies (direct-canonical / id_text / ID_LIKE_RE-LIKE-prefix); none consult `aliases.yaml` at query time.

S051 smoke-test: 0-of-8 seed-alias canonicals resolved via `resolve_id(alias)`.

## Adoption — Direction B (query-time aliases consultation)

Per §Suggested Change bullet "Direction B — Query-time aliases consultation (modify `retrieval_server.py`)":

> Load `specifications/aliases.yaml` once at server startup into a dict `{alias: canonical}`. In `resolve_id()`, add a Strategy 1.5 between Strategy 1 (canonical direct lookup) and Strategy 2 (id_text lookup): if `alias` is a key in the aliases dict, recursively look up the resolved `canonical` via Strategy 1. This makes the aliases.yaml file authoritative at query time without requiring a reindex when aliases.yaml changes.

Implementation (`tools/retrieval_server.py`, this session):

1. Added `import yaml` with ImportError-tolerant fallback (`yaml = None` if unavailable) at top of module.
2. Added `load_aliases_map(workspace: Path) -> dict` function (module-level) returning `{alias: canonical}` dict from `specifications/aliases.yaml`; returns `{}` if pyyaml unavailable, aliases.yaml absent, or YAML malformed.
3. In `build_server()`, loaded `aliases_map = load_aliases_map(workspace)` once at server startup (closure-scope; re-load requires server restart, consistent with mtime-rebuild semantics for the DB).
4. Added `aliases_available` + `aliases_present` + `missing` tracking for degraded-mode disclosure per retrieval-contract §3 clause 3.
5. In `resolve_id()`, inserted **Strategy 1.5** between Strategy 1 (direct canonical) and Strategy 2 (id_text): looks up `resolved_canonical = aliases_map.get(alias)`; if present and distinct from `alias`, re-runs the Strategy 1 canonical lookup against `resolved_canonical`.
6. Extended `_match_payload` to carry `degraded` + `missing` through from the calling site; all three return paths now report accurate degraded-mode state.
7. Updated Strategy 2 inline comment to describe the current behaviour accurately (no false promises about alias remapping).
8. Updated the no-match return's `reason` to `"no match in identifiers table or aliases.yaml"`.

## Smoke-test evidence

Test harness at session-scope (not committed to tools/; provenance captured via S052 03-close.md §6 WX-50-1 3-field recording). 8 test cases exercised against `.cache/retrieval.db` (S051-built; unchanged this session — Direction B is a query-time fix not requiring rebuild):

| Alias | Expected canonical | Strategy | Result |
|-------|---------|---------|--------|
| `"M5"` | `§10.4-M5` | alias-indirection (new) | PASS |
| `"Reviser OI-tag-only"` | `§10.4-M5` | alias-indirection (new) | PASS |
| `"Decision 172"` | `D-172` | alias-indirection (new) | PASS |
| `"phase-2 gate"` | `WX-50-1` | alias-indirection (new) | PASS |
| `"OI 19"` | `OI-019` | alias-indirection (new) | PASS |
| `"D-172"` | `D-172` | direct-canonical (unchanged) | PASS |
| `"§10.4-M5"` | `§10.4-M5` | direct-canonical (unchanged) | PASS |
| `"NONEXISTENT-999"` | None | no-match | PASS (no raise per §2.2) |

8-of-8 PASS. Alias-indirection path exercised 5 times; unchanged direct-canonical path exercised 2 times; None-case exercised 1 time. Aliases map size observed: **20 alias→canonical mappings** across 8 canonical entries in `specifications/aliases.yaml`.

## Classification — minor per OI-002

Seventh minor bug-fix-style implementation-realignment in engine history. Precedent chain:

1. S022 R8a — SESSION-LOG.md thin-index restoration (post-accretion source-realignment).
2. S030 D-100 — `workspace-structure.md` §SESSION-LOG stale-literal cleanup (OI-002 13th data point).
3. S033 D-108 — `validate.sh` check 22 loop-bug repair.
4. S040 D-123 — SESSION-LOG.md thin-index preemptive restoration.
5. S046 D-143 — `validate.sh` empty-provenance nounset + check 23 ls-glob set-e guards.
6. S051 D-177 — SESSION-LOG.md forced thin-index restoration per WX-34-1 breach.
7. **S052 D-181** — `retrieval_server.py` Strategy 1.5 implementation fix per EF-051.

Per OI-002 bug-fix-without-semantic-change heuristic: the contract `retrieval-contract.md` v1 §2.2 is unchanged (and was correct as written); the implementation previously did not fulfill it; Direction B brings the implementation into fulfillment. No engine-v bump. Engine-v9 preserved.

## Direction A deferred (optional additive)

Direction A (index-time reverse-remap; modify `build_retrieval_index.py` to INSERT synthetic `identifiers` rows for each alias at index-build time) is **not adopted** this session. Rationale:

1. Direction B alone is sufficient for §2.2 alias-indirection compliance (smoke-test proves 8-of-8 resolution).
2. Direction A's distinctive benefit (alias text searchable via BM25 `search()`) is not on the current requirements surface. No evidence alias-text-FTS-search is needed.
3. Direction A is **additive-compatible** with Direction B — both can coexist if alias-text-search becomes desired later (Direction A adds rows; Direction B adds query-time lookup; either can satisfy §2.2 alone, and together they produce redundant coverage).
4. Minimal surface change principle (Direction B is server-only; Direction A would edit indexer + schema).

Deferred-candidate status: Direction A remains available for future adoption if operational need emerges (e.g., a session where `search("Reviser OI-tag-only")` is attempted and fails due to alias text not being indexed). No forward-session obligation; no preserved-minority needed (no deliberation occurred).

## Forward observations

- **First-ever inbox→triaged→resolved lifecycle within a single session for a defect originating in self-development** (distinguished from S048 EF-001 which originated in external workspace). EF-051 is self-dev-originated per S050/S051 direct-to-inbox convention (`source_workspace_id: selvedge-self-development` accurately reflects origin).
- **Substrate first-real-use smoke-test pattern (S051) produced actionable engine-feedback within one session**. Vindicates the S050 §8 forward-commitment pattern (code-review-only at adoption session + first-real-use at next session + defect-surfaces-as-engine-feedback-intake). Pattern repeatable for future substrate adoptions that defer smoke-testing to the next session.
- **Direction B preserves mtime-rebuild semantics via server-restart-required**. Unlike the DB's session-open mtime check which triggers rebuild automatically, aliases.yaml changes require MCP server restart to be picked up. This is acceptable at phase-1 per the operator discretion of when to restart the server; phase-2+ may add an aliases.yaml mtime watcher if hot-reload becomes desired.
- **Degraded-mode disclosure per retrieval-contract §3 clause 3 now actually fires when aliases are missing**. Pre-S052, `degraded: false` was hardcoded. S052 implements the contract's intent: when `pyyaml` or `aliases.yaml` is missing, `resolve_id` returns `degraded: true` + `missing: ["pyyaml"|"specifications/aliases.yaml"]`. This is a small sub-fix within the same change; no separate decision record.
- **WX-50-1 second-session 3-field recording** exercised per this session's smoke-test. See S052 03-close.md §6.

## OI impact

No OI opened. No OI resolved. OI-019 unchanged by this triage (sub-questions (a)–(f) not touched).

## Subsumed deferred candidates

None. S047 D-150 three remaining deferred candidates (i)/(ii)/(iii) unchanged (candidate (iv) was subsumed at S048 D-153).
