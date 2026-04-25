---
feedback_id: EF-053-search-query-parser-unquoted-hyphen-fts5-not-operator
source_workspace_id: selvedge-self-development
source_session: 053
created_at: 2026-04-25
reported_by: application-agent
target: engine-adjacent
target_files:
  - tools/retrieval_server.py
  - specifications/retrieval-contract.md
severity: friction
status: inbox
---

# EF-053 — Search query parser treats unquoted hyphen as FTS5 NOT operator, crashing on hyphenated identifiers

## Observation

During Session 053 due-diligence substrate queries, `search("D-129 standing discipline")` raised an uncaught `sqlite3.OperationalError: no such column: 129` rather than tokenizing the hyphenated identifier `D-129` atomically and returning BM25-ranked results.

Root cause: SQLite FTS5's built-in query parser interprets unquoted hyphen as the `NOT` operator. The query `D-129 standing discipline` is parsed as `D NOT 129 standing discipline` (i.e., "documents containing D but not 129 standing discipline"). The token `129` is not a column in the `docs_fts` virtual table, so FTS5 raises the operational error.

Workaround: wrap hyphenated identifiers in phrase quotes. `search('"D-129" standing discipline')` succeeds and returns three correctly-ranked results (provenance/044-session-assessment/00-assessment.md top-ranked).

Concretely, S053 observed:

- **Fails**: `search("D-129 standing discipline")` → uncaught `sqlite3.OperationalError: no such column: 129`.
- **Succeeds**: `search('"D-129" standing discipline')` → 3 results; top: `provenance/044-session-assessment/00-assessment.md` score=-5.506.
- **Succeeds**: `search('"WX-50-1" "phase-2 gate"')` → 3 results; top: `provenance/050-session/03-close.md` score=-14.210.
- **Succeeds**: `search('"engine-v9" preservation window')` → 3 results; top: `provenance/050-session/03-close.md` score=-7.372.

## Why It Matters

1. **Contract §2.1 compliance gap**: `specifications/retrieval-contract.md` v1 §2.1 requires: *"Tokenisation MUST treat hyphen, underscore, and § as word-internal so that IDs (`D-152`, `d016_2`, `§10.4-M5`) tokenise atomically rather than splitting."* The implementation satisfies this at the **indexing-time tokenizer** level (`tokenize='porter unicode61 tokenchars '-_§''`). It does **NOT** satisfy this at the **query-parser** level: users searching for `D-129` without phrase quotes get a crash rather than atomic-token behaviour. A reasonable reader of §2.1 would expect the search tool to handle `D-129` the same way whether indexing or querying.

2. **§3 clause 4 silent-fallback-adjacent behaviour**: §3 clause 1 requires "tool calls MUST return a structured error with `{available: false, reason: str}` rather than timing out silently." While the raw `sqlite3.OperationalError` is not silent (it raises), it is also not a structured contract-compliant error response. A caller can't distinguish "index unavailable" from "FTS5 query syntax error" from "index corruption" without parsing the exception message. §3's discipline reads toward structured error envelopes, not raw exception propagation.

3. **Operational friction for agent users**: Agents querying the substrate — Claude, operator, or external agents via MCP — will naturally write queries of the form `D-129` or `§10.4-M5 minority` without quoting. Under current behaviour these queries crash; under §2.1's intent they should tokenize atomically and return BM25-ranked results. The workaround (quote hyphenated identifiers) is trivial once known but is not discoverable from the contract text; the error message is also not actionable for a user who doesn't know FTS5 internals.

4. **Undetected by S051/S052 smoke-tests**: S051 and S052 exercised resolve_id heavily (which is unaffected) and search only lightly (`search("retrieval contract" k=3)` + `search("WX-34-1" k=2)` — both non-hyphenated). The hyphen-parser issue was invisible until S053's due-diligence broadened the search-query variety.

## Suggested Change

Three candidate directions (non-exclusive; operator chooses at triage):

**Direction A — Query sanitization at server level (implementation-only)**: before passing a query to FTS5, detect hyphenated identifier patterns matching the ID regex family (`D-\d{3}`, `OI-\d{3}`, `WX-\d+-\d+`, `§N(.N)*(-MN)?`, `engine-v\d+`, `EF-\d{3}`, `d01\d_\d+`) and automatically wrap matched substrings in phrase quotes. Transparent to caller; satisfies §2.1 intent without spec change. Engine-adjacent tooling change in `tools/retrieval_server.py`; classification minor per OI-002 per 7-precedent bug-fix-style source-realignment chain (if adopted).

**Direction B — Structured error response with hint (partial fix)**: catch `sqlite3.OperationalError` inside `search()` and return a structured error per §3: `{available: true, error: "FTS5 query syntax error", hint: "quote hyphenated identifiers, e.g. '\"D-129\"'", raw: str(e)}`. Does not solve the user-expected-atomic-token behaviour but surfaces the error-mode structurally. Can be combined with Direction A as defensive fallback.

**Direction C — Spec narrowing**: add §2.1 sentence clarifying that search queries containing hyphenated or reserved-character identifiers must be phrase-quoted; update `aliases.yaml` seed entries or bootstrap documentation to include this guidance. Classification: substantive (narrows contract semantics); engine-v bump candidate if adopted alone. Least-preferred per the S048 D-153 precedent of fixing implementation to match contract rather than narrowing contract to match implementation.

Direction A is most likely the right fix: it satisfies §2.1 without contract change, is additive, and has a trivial implementation (regex-replace on query string before FTS5 invocation). Direction B is a defensive-engineering complement. Direction C is least-preferred per precedent but preserved for operator consideration.

## Evidence

- Reproduction pathway: `.cache/venv/bin/python` inline script calling FTS5 directly (same mechanism as S051 smoke-test + S052 Direction B smoke-test). Session 053 close §6 WX-50-1 `fallbacks_due_to_missing_capability` entry references this record.
- FTS5 query syntax documented at https://www.sqlite.org/fts5.html#full_text_query_syntax — "A hyphen character (`-`) or exclamation mark (`!`) is used to denote the NOT operator."
- Contract reference: `specifications/retrieval-contract.md` v1 §2.1 sentence 4 ("Tokenisation MUST treat hyphen...").

## Application-Scope Disposition

Session 053 is Path A (Watch); no triage or resolution at S053. Observation recorded as inbox intake per `workspace-structure.md` v5 §engine-feedback intake-preserved-verbatim convention. Triage scheduled for S054+ at operator discretion (analogous to EF-051 at S051: intake at discovery session, triage at next session).

Engine-v impact at triage: minor per OI-002 if Direction A (implementation-only); substantive if Direction C (spec narrowing) is adopted alone. Direction B alone is minor. Most likely path is Direction A minor, preserving engine-v9.
