---
triage_id: EF-053-triage
feedback_ref: ../inbox/EF-053-search-query-parser-unquoted-hyphen-fts5-not-operator.md
triaged_in_session: 054
triaged_at: 2026-04-25
status: resolved
classification: minor
disposition: Direction A (query-sanitization at server level) adopted this session via minor implementation edit to tools/retrieval_server.py; module-level _ID_TOKEN_RE regex + _sanitize_query() helper added; search() now wraps recognised hyphenated identifier patterns in phrase quotes before passing the query to FTS5; original failure case search("D-129 standing discipline") now returns 3 BM25-ranked results without crashing; retrieval-contract.md v1 §2.1 query-parser-time hyphen-as-word-internal compliance now matches indexing-time tokenizer compliance
opened_issue: null
spec_amendments: []
tool_amendments:
  - path: tools/retrieval_server.py
    classification: minor
    note: "_ID_TOKEN_RE module-level regex matching D-NNN / OI-NNN / WX-N-N / EF-NNN-... / engine-vN / §N(.N)*(-MN)? / d01N_N; _sanitize_query() helper wraps matches in phrase quotes (idempotent — won't double-wrap already-quoted IDs); search() reorders attempts (sanitized first; whole-query phrase-wrap as last-ditch fallback for unrecognised hyphen forms)"
decision_records:
  - D-185
  - D-186
engine_version_impact: engine-v9 preserved (no bump; minor per OI-002 eighth source-realignment precedent chain S022/S030/S033/S040/S046/S051/S052/S054)
direction_selected: A
alternative_directions_deferred:
  - direction: B
    label: structured error response with hint
    why_deferred: Direction A solves the user-expected-atomic-token behaviour (no crash + correct results); Direction B would only surface the error mode without solving it. Direction B preserved as optional defensive complement if future error modes outside _ID_TOKEN_RE coverage warrant structured exposure; the existing OperationalError fallback path in search() partially serves this role.
  - direction: C
    label: spec narrowing
    why_deferred: Per S048 D-153 precedent (fix implementation to match contract; do not narrow contract to match implementation). The contract §2.1 is correct as written; the implementation gap was at query-parser time. Direction A closes the gap without touching the contract. Direction C would have required substantive revision and an engine-v bump to retract a sentence the contract does not need to retract.
---

# Triage — EF-053 search-query-parser-unquoted-hyphen-fts5-not-operator

## Classification

**Target**: engine-adjacent (implementation-level, not engine-definition). **Severity on inbox record**: friction (substrate primary `resolve_id` was unaffected; defect was in the `search` query-parser path). **Source**: `selvedge-self-development` Session 053 due-diligence substrate queries (S053 close §6 WX-50-1 fallbacks-due-to-missing-capability entry).

**Disposition**: **resolved** this session via Direction A implementation fix. Narrow directionally-clear defect; single-orchestrator same-session resolution per S048 D-152 + S052 D-181 Path T+L precedent (where direction is clear, triage + adoption execute in same session).

## Defect summary (from inbox record)

`specifications/retrieval-contract.md` v1 §2.1 declares: *"Tokenisation MUST treat hyphen, underscore, and § as word-internal so that IDs (`D-152`, `d016_2`, `§10.4-M5`) tokenise atomically rather than splitting."*

Pre-S054 implementation:
- **Indexing-time tokenizer** (`tokenize='porter unicode61 tokenchars ''-_§'''` in `build_retrieval_index.py`): compliant. IDs tokenise atomically when the corpus is built.
- **Query-parser-time** (`tools/retrieval_server.py` `search()`): non-compliant. The wrapper attempted whole-query phrase-quoting first, fell back to raw query on `OperationalError`. The fallback exposed the user query to FTS5's query parser, which interprets unquoted hyphen as the `NOT` operator. Query `D-129 standing discipline` parsed as `D NOT 129 standing discipline`; FTS5 raised `sqlite3.OperationalError: no such column: 129`.

S053 smoke-test: 1 fallback recorded (`search("D-129 standing discipline")` crashed); workaround was phrase-quoting the identifier manually.

## Adoption — Direction A (query sanitization at server level)

Per inbox record §Suggested Change Direction A:

> Before passing a query to FTS5, detect hyphenated identifier patterns matching the ID regex family (`D-\d{3}`, `OI-\d{3}`, `WX-\d+-\d+`, `§N(.N)*(-MN)?`, `engine-v\d+`, `EF-\d{3}`, `d01\d_\d+`) and automatically wrap matched substrings in phrase quotes. Transparent to caller; satisfies §2.1 intent without spec change.

Implementation (`tools/retrieval_server.py`, this session):

1. Added module-level `_ID_TOKEN_RE` regex matching the curated ID family (`D-\d{3}`, `OI-\d{3}`, `WX-\d+-\d+`, `EF-\d{3}(?:-[a-z0-9-]+)?`, `engine-v\d+`, `§\d+(?:\.\d+)*(?:-M\d+)?`, `d01\d_\d+`). Includes negative lookbehind/lookahead on `"` so already-quoted identifiers are left untouched (idempotent).
2. Added module-level `_sanitize_query(query: str) -> str` helper that returns `_ID_TOKEN_RE.sub(r'"\1"', query)`. Pure function; no DB or workspace dependency.
3. Modified `search()` to call `sanitized = _sanitize_query(query)` and pass the sanitized result as the FTS5 MATCH expression. Reordered attempts: sanitized query is the primary path (correct BM25 ranking for known IDs); whole-query phrase-wrap is the last-ditch fallback (defensive for unrecognised hyphen forms — e.g., `phase-2`, `cross-family` — that fall outside `_ID_TOKEN_RE` coverage).

## Smoke-test evidence

Test harness at session-scope (not committed to `tools/`; provenance captured in S054 03-close.md). Two layers exercised:

**Layer 1 — `_sanitize_query()` unit behaviour** (10 cases; see S054 03-close.md):

| Input | Expected output | Result |
|-------|-----------------|--------|
| `D-129 standing discipline` | `"D-129" standing discipline` | PASS |
| `search for OI-019` | `search for "OI-019"` | PASS |
| `WX-50-1 phase-2 gate` | `"WX-50-1" phase-2 gate` | PASS |
| `engine-v9 preservation` | `"engine-v9" preservation` | PASS |
| `§10.4-M5 minority` | `"§10.4-M5" minority` | PASS |
| `EF-053 hyphen` | `"EF-053" hyphen` | PASS |
| `EF-051-aliases-yaml not consulted` | `"EF-051-aliases-yaml" not consulted` | PASS |
| `plain query no ids` | `plain query no ids` | PASS |
| `"D-129" already quoted` | `"D-129" already quoted` (unchanged; idempotent) | PASS |
| `multiple D-129 and OI-019 ids` | `multiple "D-129" and "OI-019" ids` | PASS |

10-of-10 PASS.

**Layer 2 — `search()` integration via FastMCP tool registration** (4 cases against rebuilt `.cache/retrieval.db`):

| Query | Expected | Result |
|-------|----------|--------|
| `D-129 standing discipline` | ≥1 result, no crash | PASS (3 results) |
| `engine-v9 preservation` | ≥1 result | PASS (3 results) |
| `WX-50-1 phase-2 gate` | ≥1 result, possibly via fallback | PASS (3 results; via fallback because `phase-2` is not in `_ID_TOKEN_RE`) |
| `retrieval contract` (control) | ≥1 result, sanitization no-op | PASS (3 results) |

4-of-4 PASS. The `WX-50-1 phase-2 gate` case demonstrates the fallback path correctly catches unrecognised hyphen forms outside `_ID_TOKEN_RE` coverage; the result set is still useful (top match `provenance/050-session/03-close.md` is correct).

## Classification — minor per OI-002

Eighth minor bug-fix-style implementation-realignment in engine history. Precedent chain:

1. S022 R8a — SESSION-LOG.md thin-index restoration (post-accretion source-realignment).
2. S030 D-100 — `workspace-structure.md` §SESSION-LOG stale-literal cleanup.
3. S033 D-108 — `validate.sh` check 22 loop-bug repair.
4. S040 D-123 — SESSION-LOG.md thin-index preemptive restoration.
5. S046 D-143 — `validate.sh` empty-provenance nounset + check 23 ls-glob set-e guards.
6. S051 D-178 — SESSION-LOG.md forced thin-index restoration per WX-34-1 breach.
7. S052 D-181 — `retrieval_server.py` Strategy 1.5 implementation fix per EF-051.
8. **S054 D-186** — `retrieval_server.py` `_sanitize_query()` implementation fix per EF-053.

Per OI-002 bug-fix-without-semantic-change heuristic: the contract `retrieval-contract.md` v1 §2.1 is unchanged (and was correct as written); the implementation previously did not fulfill it at the query-parser layer; Direction A brings the implementation into fulfillment. No engine-v bump. Engine-v9 preserved.

## Direction B + Direction C deferred

**Direction B** (structured error response with hint) is **not adopted** this session. Rationale:

1. Direction A solves the user-facing problem (query no longer crashes; correct results returned). Direction B would only surface the error structurally without solving it.
2. The existing `except sqlite3.OperationalError` fallback in `search()` partially serves Direction B's defensive role for unrecognised hyphen forms outside `_ID_TOKEN_RE`.
3. If future operational evidence shows the fallback masks a class of errors that should surface structurally, Direction B can be added then; Direction A is additive-compatible.

**Direction C** (spec narrowing) is **rejected** per S048 D-153 precedent (fix implementation to match contract; do not narrow contract to match implementation). The contract §2.1 is correct as written; narrowing it would be substantive (engine-v-bumping) for a fix that Direction A delivers as minor.

## Forward observations

- **Substrate first-real-use → second-real-use → third-real-use defect-surfacing pattern continues** (S051 surfaces EF-051 → S052 resolves → S053 surfaces EF-053 → S054 resolves). Cadence appears stable at ≈1 actionable observation per substrate-exercise session. Triage cost is bounded (1 intake + 1 same-session triage + 1 minor implementation fix); preservation cost is bounded.
- **`_ID_TOKEN_RE` is a curated set, not exhaustive.** Identifiers outside the curated patterns (e.g., generic `word-hyphen-word` like `phase-2`, `cross-family`, `non-Claude`) still trigger the fallback path. This is acceptable: the fallback succeeds without crash; the contract §2.1 is fulfilled for the IDs it explicitly names. Broader coverage can be added if friction reappears.
- **Idempotence of `_sanitize_query`**: callers that already phrase-quote identifiers (e.g., S053's manual workaround `search('"D-129" standing discipline')`) will pass through unchanged. This preserves backward compatibility for any session-scope provenance citing pre-S054 queries.
- **MCP stdio transport remains unverified in-session.** Same limit as S051/S052/S053 close §8 (and S054 00-assessment §7 honest-limit 1). Smoke-tests use `.cache/venv/bin/python` direct invocation of `build_server` and the FastMCP tool-registration internals; FastMCP stdio wiring is not exercised. The new `_sanitize_query()` behaviour is verified at the SQL-equivalent level and at the FastMCP tool-function level; the stdio wire format is inferred from the same registration path used by `resolve_id` and `search` (which the operator has exercised in prior sessions when needed).

## OI impact

No OI opened. No OI resolved. OI-019 unchanged by this triage (sub-questions (a)–(f) not touched).

## Subsumed deferred candidates

None. S047 D-150 three remaining deferred candidates (i)/(ii)/(iii) unchanged.
