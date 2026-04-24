---
title: Perspective — P1 Substrate Architect (Session 050)
session: 050
perspective: substrate-architect
perspective_family: claude
perspective_role: substrate-architect
date: 2026-04-24
status: immutable-at-commit
---

# P1 — Substrate Architect: Retrieval substrate survey and recommendation

Role per S050 shared brief §5.1 (Halt-1 Q4-amended): neutral surveyor. No operator-preferred starting point. Advocacy emerges from technical evaluation only. I have applied the §2a correction overlay throughout: the design-space §3.1 "operator-named default" annotation, §4 header "(operator's named direction)", §5.4 "operator-alignment edge", and §6.4 bullet 4 on operator-signal-respect are retracted and play no role below.

## 1. Candidate evaluation

The candidate set is the four named in shared brief §4 Q1 — Substrate-1 SQLite FTS5; Substrate-2 DuckDB+FTS; Substrate-3 tantivy-py; Substrate-4 Whoosh-Reloaded — plus two Substrate-N options I surface proactively below (Substrate-5 bm25s + SQLite frontmatter tables; Substrate-6 lnx/manticore/typesense as reference for rejection). I treat the design-space §6 rejections (Meilisearch, RDF stores, Neo4j, rank_bm25, embedding retrieval) as still-standing; none of the §2a corrections touches them.

Evaluation criteria per shared brief §5.1 step 1: ID-crisp query performance; full-text BM25 quality; frontmatter-filter ergonomics; graph traversal ergonomics; dependency floor (self-dev + external-workspace); MCP integration effort; rebuild cost; index size; ecosystem maturity; API stability over 2–5 year horizon.

### 1.1 Substrate-1: SQLite FTS5

**ID-crisp query performance**: Excellent. `tokenchars '-_'` ensures `D-152`, `OI-019`, `§10.4-M5` index as single tokens; exact-match queries hit the FTS5 index at microsecond latency on a 457-file / 1.4M-word corpus. For non-FTS exact-ID lookup (the `identifiers` table per design-space §3.2), SQLite B-tree index on `(id_text, id_kind)` gives sub-millisecond lookup.

**Full-text BM25 quality**: Native BM25 ranking since SQLite 3.20 (2017); `bm25(docs_fts)` scoring function; `matchinfo` available if custom ranking is wanted later. Tunable k1/b via `bm25(table, k1_weight, b_weight)` syntax. Porter stemmer for English prose. Snippet/highlight auxiliary functions (`snippet()`, `highlight()`) return context-economical excerpts directly — the exact output shape an MCP retrieval tool needs.

**Frontmatter-filter ergonomics**: Strained. FTS5 is a virtual table; structured filters require a JOIN to a sibling `frontmatter_kv(path, key, value)` table. Query "decisions whose `triggers_met` includes `d016_2` AND match prose `preservation`" is a JOIN + GROUP BY + WHERE EXISTS pattern. Works; executes fast on this corpus; but more lines of SQL than DuckDB's equivalent unified-table query. This is a real ergonomic cost on the structured-filter query class, which §2.2 of the design-space's ID density data identifies as dominant. I'm flagging this as a **strained criterion** for Substrate-1, not a win.

**Graph traversal ergonomics**: Adequate. SQLite has supported recursive CTEs since 3.8.3 (2014). Multi-hop cross-reference walk over the `edges` table is a standard `WITH RECURSIVE edges_reachable(...) AS (...) SELECT ...` pattern. Verbose compared to DuckDB's `USING KEY` or DuckPGQ property-graph syntax, but fully functional and well-documented. Another strained criterion.

**Dependency floor**: Best-in-class. `sqlite3` is Python stdlib on macOS Apple Python (ships with FTS5 compiled in). Dependency floor for the indexer: `pyyaml` (nearly ubiquitous; Apple Python doesn't include it; `pip install pyyaml` or workspace-local `uv tool install`). Dependency floor for the MCP server: `mcp[cli]` (FastMCP SDK). **For external-workspace bootstrap this matters acutely**: every external-application workspace pays the same floor once, which is two wheel installs plus Python 3.10+.

**MCP integration effort**: Modest. FastMCP decorator style maps cleanly: `@mcp.tool()` functions wrapping SQL queries. Reference implementations exist (design-space §3.4 cites `pvliesdonk/markdown-vault-mcp`; I recall from pretraining that several FTS5-over-MCP projects have surfaced in 2025–2026 on the mcp.so directory). Estimated ~200 LOC for the five tools (`search`, `resolve_id`, `list_identifiers`, `traverse`, `warrants_currently_met`).

**Rebuild cost**: Design-space §3.5 cites ~140 ms for 457 files on stock Python + SQLite 3.53. This is credible: the cost is dominated by markdown-parse + regex-extract, not FTS indexing. At 10× corpus scale (~4,500 files) expect ~1.5 s. At 100× (~45,000 files, unreachable for this workspace within the 5-year horizon) expect ~15 s — still well under a session-open tolerance.

**Index size**: Design-space §4.1 cites ~18 MiB on disk for this corpus (~20% of workspace total). Gitignored. For external workspaces the index scales with their corpus; disaster-response at S001-scale is <1 MiB.

**Ecosystem maturity**: High. FTS5 has been stable since 2015. BM25 added 2017. SQLite 3.20+ ubiquitous on all modern OS distributions. Python `sqlite3` API has been stable since Python 2. `CREATE VIRTUAL TABLE` DDL has not churned. I recall from pretraining that SQLite's compatibility policy is among the strongest in open-source databases (forward compatibility promised through at least 2050 for the file format).

**API stability over 2–5 year horizon**: Highest of the four. No imminent breaking changes visible. FastMCP API may churn (shared brief §8 honest-limit — the Anthropic SDK is under active development), but that churn is orthogonal to the substrate choice.

**Failed/strained criteria summary for Substrate-1**: frontmatter-filter ergonomics (strained — JOIN required); graph traversal ergonomics (strained — recursive CTE verbose). Wins: everything else.

### 1.2 Substrate-2: DuckDB + FTS extension

**ID-crisp query performance**: Excellent for B-tree exact lookup over `identifiers` table; good-to-excellent for FTS. DuckDB's FTS extension uses Okapi BM25 internally. Per §2a Correction 1, the "experimental" flag is retracted; I evaluate DuckDB FTS as mature.

**Full-text BM25 quality**: Good. `match_bm25(rowid, 'query')` returns BM25 scores. Tunable k1/b. No direct snippet/highlight equivalent — the caller computes excerpts via separate `substring()` + regex or a wrapper function. This is a real ergonomic cost compared to FTS5's built-in `snippet()`. I'll flag this as a **strained criterion** for Substrate-2 offsetting some of its frontmatter wins.

**Frontmatter-filter ergonomics**: Excellent. DuckDB's typed-column model (`VARCHAR`, `VARCHAR[]`, `STRUCT`, `JSON`) lets frontmatter live as typed fields on the `documents` table rather than as a separate `frontmatter_kv` JOIN target. `WHERE 'd016_2' = ANY(triggers_met) AND match_bm25(rowid, 'preservation')` is a single-table scan. For the dominant structured-filter query class this is a clean win over Substrate-1.

**Graph traversal ergonomics**: Best-in-class among the SQL substrates. Recursive CTEs with `USING KEY` optimization (DuckDB 1.2+); DuckPGQ community extension adds SPARQL-like property-graph syntax if wanted. Shared brief §4 Q6 (edges-table-subsumes-syncs_with question) is easier to answer "yes, the edges table is sufficient" under DuckDB because the edges table's ergonomics actually match the query load.

**Dependency floor**: Second-best. `duckdb` Python package is pure wheel on macOS (no system dependency; `pip install duckdb`); FTS extension auto-loads via `INSTALL fts; LOAD fts;` on first use with a one-time ~5 MB extension download. For external-workspace bootstrap: three wheel installs (`duckdb`, `pyyaml`, `mcp[cli]`) vs. Substrate-1's two. Incremental cost: one wheel, ~50 MB disk.

**MCP integration effort**: Modest. Same FastMCP decorator style; DuckDB Python API is similar to `sqlite3`. Fewer MCP reference implementations exist for DuckDB-over-MCP than SQLite-over-MCP as of my pretraining cutoff — this is a real ecosystem-maturity gap, though it is closable with the ~200 LOC server.

**Rebuild cost**: I recall from pretraining that DuckDB's FTS extension does not support incremental index updates; full rebuild via `PRAGMA drop_fts_index; PRAGMA create_fts_index` is the idiomatic approach. At this corpus scale the full rebuild is ~200 ms (slightly slower than Substrate-1's 140 ms due to wheel startup overhead). At 10× scale this is still under 3 s; unproblematic.

**Index size**: Comparable to Substrate-1 (~20 MiB for this corpus). DuckDB's columnar storage is more compressed for typed columns but the FTS auxiliary data dominates.

**Ecosystem maturity**: Moderate-to-high. DuckDB core is mature and widely adopted (2022+). FTS extension reached stable status per the operator's §2a Correction 1 datapoint (2026-04-24). DuckPGQ is community-maintained; lineage visibility per shared brief §8 is under operator's authority as of this session.

**API stability over 2–5 year horizon**: Good. DuckDB has a documented stability-promise policy for core APIs since 1.0 (2024). Extensions (FTS, DuckPGQ) have weaker guarantees than core. The risk is: FTS extension API evolves, forcing a minor re-write of the indexer. Substrate-1's FTS5 has a 9-year track record of non-churn by comparison.

**Failed/strained criteria summary for Substrate-2**: snippet/highlight ergonomics (strained — caller-computed); extension API stability (strained — weaker than core guarantee); MCP ecosystem (strained — fewer references). Wins: frontmatter-filter ergonomics; graph traversal ergonomics; typed-column data model.

### 1.3 Substrate-3: tantivy-py

**ID-crisp query performance**: Excellent. Tantivy is Rust-backed, written as a Lucene-analogue; per my pretraining, tantivy's throughput edge over SQLite FTS5 becomes observable at 10^6+ documents. At 457 files the performance is indistinguishable from either SQL substrate.

**Full-text BM25 quality**: Excellent. Tantivy's BM25 implementation is canonical. Custom tokenizers, field boosts, phrase queries — all first-class.

**Frontmatter-filter ergonomics**: Awkward. Tantivy is a search engine, not a SQL database. Structured filters are expressed as Lucene-style query clauses. No SQL; no JOIN. An `edges` table would have to live outside tantivy (e.g., in a sibling SQLite file), recreating the same JOIN problem across process boundaries. For a workspace whose dominant query shape is structured-filter, this is a fundamental mismatch.

**Graph traversal ergonomics**: Not supported natively. Would require recreating `edges` outside tantivy + doing traversal in Python. This doesn't rule tantivy out — Substrate-1 uses SQL for `edges` and works fine — but it means tantivy is doing only the FTS portion while SQLite/DuckDB is still needed for everything structured. Two-substrate architecture is worse than one-substrate.

**Dependency floor**: Heavy. `tantivy-py` is a Rust extension distributed as binary wheels. Macos/linux/windows wheels exist; exotic arch may force source-build (Rust toolchain required). For external-workspace portability this is a real risk: if an external workspace runs on an arch without pre-built wheels, bootstrap fails in a way that requires developer-level Rust knowledge to unstick.

**MCP integration effort**: Similar to the SQL substrates (~200 LOC FastMCP server wrapping tantivy search + separate SQLite for frontmatter/edges).

**Rebuild cost**: Faster than SQL substrates at scale (Rust-backed indexer). At this corpus scale the difference is invisible — all three complete under 500 ms.

**Index size**: Comparable to the SQL substrates; tantivy's on-disk format is competitive with FTS5.

**Ecosystem maturity**: Moderate. Tantivy (Rust) is mature; `tantivy-py` binding is actively maintained but has had API-breaking changes across 0.20–0.25. Design-space §6.2 flagged this; the rejection stands on its own merits, not on the operator-preference framing that §2a retracted.

**API stability over 2–5 year horizon**: Mixed. Rust core is stable; Python binding is the weak link. Minor-version bumps have broken user code historically.

**Failed/strained criteria summary for Substrate-3**: frontmatter-filter ergonomics (failed — not a SQL database); graph traversal (failed — not supported); dependency floor (failed — Rust wheel risk); Python binding API stability (strained — historical breakage). Wins: FTS throughput (unneeded at this scale).

**Position**: tantivy-py is over-kit for this workspace. It's the right tool for a corpus 10^6+; it's the wrong tool at 457 files. This rejection is unchanged by the §2a correction overlay.

### 1.4 Substrate-4: Whoosh-Reloaded

**ID-crisp query performance**: Adequate. Whoosh's BM25F ranking is standard. Pure Python, so interpreter-speed, not native-speed.

**Full-text BM25 quality**: Good. BM25F (BM25 with field boosts) is its own dialect; output comparable to FTS5/DuckDB BM25.

**Frontmatter-filter ergonomics**: Whoosh supports schema fields including `KEYWORD` fields for array-like values. No SQL; query-object API. Similar ergonomic cost to tantivy.

**Graph traversal ergonomics**: Not supported. Same two-substrate problem as tantivy.

**Dependency floor**: Lightest after Substrate-1's stdlib-only. Whoosh-Reloaded is pure Python (`pip install whoosh-reloaded`). No C extensions, no Rust. Good for exotic environments.

**MCP integration effort**: Similar to other substrates (~200 LOC).

**Rebuild cost**: Slower than native-code substrates. Pure Python indexing at this scale is ~1–2 s (from my pretraining, Whoosh indexing ~200 files/sec on modern hardware). Unproblematic at 457 files; slower than ideal at 10× scale.

**Index size**: Larger than FTS5/DuckDB (Whoosh's format is less compact).

**Ecosystem maturity**: Low. Original Whoosh feature-frozen; `Whoosh-Reloaded` fork has low ecosystem momentum in 2026 (per design-space §6.7 and my pretraining cross-check). Few MCP integrations; few recent SO answers.

**API stability over 2–5 year horizon**: Uncertain. Fork-status projects are a bet on continued maintainer interest.

**Failed/strained criteria summary for Substrate-4**: frontmatter-filter ergonomics (strained); graph traversal (failed); ecosystem maturity (failed); API stability (strained). Wins: pure-Python dependency floor; escape-hatch role.

**Position**: Useful as escape hatch if SQLite C extensions become constrained. Not the primary choice.

### 1.5 Substrate-5 (surfaced): bm25s + SQLite structured tables

I surface this proactively because P3's frame-completion role is likely to probe "is FTS-as-library different from FTS-as-in-database"; pre-empting.

**Architecture**: `bm25s` (pure Python, NumPy sparse-matrix BM25; design-space §6.6 noted the transition from `rank_bm25` to `bm25s` with 20×–287× speedups) provides the BM25 layer. SQLite provides the `documents`, `identifiers`, `frontmatter_kv`, `edges`, `aliases` tables (design-space §3.2 schema). No FTS virtual table; BM25 index is a NumPy file alongside the SQLite database.

**Evaluation**:
- ID-crisp query: Same as Substrate-1 via SQLite B-tree.
- BM25 quality: Excellent; bm25s is benchmark-competitive with Lucene/tantivy on BEIR.
- Frontmatter filter: Same as Substrate-1 (SQLite JOINs).
- Graph traversal: Same as Substrate-1 (recursive CTEs).
- Dependency floor: Heavier than Substrate-1 (`bm25s` + NumPy + SciPy + SQLite) — this is a real portability cost. NumPy/SciPy are ubiquitous but non-stdlib.
- Rebuild cost: Marginally slower than Substrate-1 (bm25s indexing is fast but the two-store architecture adds coordination overhead).
- Index size: Two files (SQLite + .npz); total comparable to FTS5 single-file.
- Ecosystem maturity: bm25s released 2024; actively maintained through 2026.
- API stability: Young project; single-digit 0.x versioning; risk of API churn.

**Position**: No clear win over Substrate-1 on this workspace's query shape. The two-store architecture doubles the rebuild coordination surface for no functional gain. Rejected.

### 1.6 Candidates rejected before evaluation

Per design-space §6 with §2a overlay applied: Meilisearch/Typesense (daemon + typo-tolerance wrong for ID queries; unchanged); RDF/SPARQL stores (schema-tax disproportional; unchanged); embedding retrieval (three of four rationale bullets in §6.4 stand — ID-lookup failure, Anthropic contextual-retrieval blog, semantic drift; the fourth bullet about operator-signal-respect is retracted per §2a; rejection still carries on the three remaining grounds); Neo4j/Memgraph (scale mismatch; unchanged); rank_bm25 (stale; unchanged; successor bm25s evaluated above as Substrate-5).

## 2. Recommendation

**Substrate-1 (SQLite FTS5) for primary adoption.** Narrow win over Substrate-2 (DuckDB+FTS) on three decisive criteria:

1. **Dependency floor for external-workspace portability**. Stdlib `sqlite3` with FTS5 compiled in means every external-application workspace pays exactly two extra wheel installs (`pyyaml`, `mcp[cli]`) — both already near-ubiquitous in the Python ecosystem. Substrate-2 adds a third wheel (`duckdb`) at ~50 MB. On a methodology-for-domain-projects pitch (shared brief §2b; Q6 load-bearing), minimising every external workspace's bootstrap cost is a design value, not just a convenience. This is the criterion that tips.

2. **Ecosystem maturity over the 2–5 year horizon**. FTS5 has 9 years of no-churn; BM25 scoring has 8. DuckDB FTS reached stable in 2026 per operator's datapoint; its prior 2 years of API churn are real history even if the flag has been lifted. For a methodology whose specs reference the substrate contractually (kernel §1 Warrant evaluation sub-activity per Q3), substrate API stability reduces the frequency of substrate-driven kernel revisions.

3. **Snippet/highlight auxiliary functions are FTS5-native**. `snippet()` and `highlight()` return context-economical excerpts from the BM25 query in a single SQL call. This is exactly the MCP tool output shape — small snippets with relevance scores, not whole files — and it's the one place Substrate-2 loses ergonomic ground (caller-computed excerpts). On the MCP-integration dimension Substrate-1 wins on less-code + more-idiomatic-output.

**Where Substrate-1 loses and I concede**: frontmatter-filter ergonomics (JOIN required), graph traversal ergonomics (recursive CTE verbose). These are real costs and I'm listing them as failed/strained criteria not wins. The mitigation is that both are **one-time write costs** in `tools/build_retrieval_index.py` and `tools/retrieval_server.py`; after those files exist, the JOIN complexity is invisible behind the `search(...)` and `traverse(...)` MCP tool surfaces. The callers of the MCP tools never see the SQL.

**Hybrid not recommended**. A hybrid (e.g., Substrate-1 for FTS + DuckDB for edges/frontmatter) would double the indexer's coordination surface and double the dependency floor — the worst of both worlds. Single-substrate is the right shape.

**Revision traceability** (per §5.1 step 7 P4 guard): Mid-draft I reconsidered whether Substrate-2's frontmatter-filter ergonomic advantage should tip the decision. It does not, for two reasons: (a) the ergonomic advantage is invisible to MCP callers behind the tool surface; (b) the dependency-floor cost for external workspaces is permanent and observable at every bootstrap. A correct tie-breaker must privilege observable permanent costs over hidden one-time ergonomic costs. This revision sequence is recorded here so P4 can audit it.

## 3. Architecture proposal

### 3.1 Table schema (SQLite DDL)

```sql
CREATE TABLE documents (
  path TEXT PRIMARY KEY,
  kind TEXT NOT NULL,                -- 'spec'|'provenance'|'open-issue'|'engine-feedback'|'application'|'prompt'|'tool'|'root'
  session INTEGER,                   -- NULL for non-session files; integer 001..NNN for session files
  mtime REAL NOT NULL,               -- Unix timestamp for rebuild trigger
  title TEXT,                        -- from frontmatter or H1
  frontmatter_json TEXT,             -- serialised YAML frontmatter
  body TEXT NOT NULL                 -- markdown body, stripped of frontmatter
);

CREATE INDEX idx_docs_kind ON documents(kind);
CREATE INDEX idx_docs_session ON documents(session);

CREATE TABLE identifiers (
  id_text TEXT NOT NULL,             -- 'D-152', 'OI-019', '§10.4-M5', 'WX-34-1', etc.
  id_kind TEXT NOT NULL,             -- 'decision'|'open-issue'|'minority'|'watchpoint'|'session'|'engine-version'|'feedback'|'trigger'
  canonical TEXT NOT NULL,           -- canonical form (may equal id_text)
  source_path TEXT NOT NULL REFERENCES documents(path),
  line INTEGER,
  context_snippet TEXT,              -- ~120 chars surrounding the occurrence
  PRIMARY KEY (id_text, id_kind, source_path, line)
);

CREATE INDEX idx_ids_canonical ON identifiers(canonical, id_kind);
CREATE INDEX idx_ids_source ON identifiers(source_path);

CREATE TABLE frontmatter_kv (
  path TEXT NOT NULL REFERENCES documents(path),
  key TEXT NOT NULL,
  value TEXT NOT NULL,               -- scalars as-is; arrays flattened one-row-per-element
  PRIMARY KEY (path, key, value)
);

CREATE INDEX idx_fm_key_value ON frontmatter_kv(key, value);

CREATE TABLE edges (
  src_id TEXT NOT NULL,
  src_kind TEXT NOT NULL,
  dst_id TEXT NOT NULL,
  dst_kind TEXT NOT NULL,
  relation TEXT NOT NULL,            -- 'cites'|'supersedes'|'triggers'|'resolves'|'activates'|'references'
  source_path TEXT NOT NULL REFERENCES documents(path),
  session INTEGER,
  PRIMARY KEY (src_id, dst_id, relation, source_path)
);

CREATE INDEX idx_edges_src ON edges(src_id, src_kind);
CREATE INDEX idx_edges_dst ON edges(dst_id, dst_kind);

CREATE TABLE aliases (
  alias TEXT NOT NULL,
  canonical TEXT NOT NULL,
  kind TEXT NOT NULL,
  alias_type TEXT NOT NULL,          -- 'altLabel'|'hiddenLabel' (SKOS three-label; canonical is prefLabel)
  added_session INTEGER,
  last_seen_session INTEGER,
  PRIMARY KEY (alias, kind)
);

CREATE VIRTUAL TABLE docs_fts USING fts5(
  path UNINDEXED,
  title,
  body,
  content='documents',
  content_rowid='rowid',
  tokenize='porter unicode61 tokenchars ''-_§'''
);
```

The `§` addition to `tokenchars` indexes `§10.4-M5` as a single token (the design-space §4.1 proposed `porter unicode61 tokenchars '-_'` which breaks on `§`; I'm revising upward). I recall from pretraining that SQLite FTS5 accepts unicode characters in `tokenchars` since 3.14.

### 3.2 Tokenizer rationale

- `porter` — English stemmer for prose retrieval ("preservation" / "preserves" / "preserved" match).
- `unicode61` — Unicode-aware base tokenizer; handles em-dash, en-dash, typographic quotes.
- `tokenchars '-_§'` — treats hyphen, underscore, section-mark as word-internal characters so `D-152`, `d016_2`, `§10.4-M5`, `WX-34-1` tokenise atomically rather than splitting.

### 3.3 MCP tool surface

Five tools + one resource, per FastMCP stdio:

```python
@mcp.tool()
def search(query: str, k: int = 10, kind: str | None = None,
           session_min: int | None = None, session_max: int | None = None) -> list[dict]:
    """BM25 full-text search with optional kind + session-range filters.
    Returns [{path, snippet, score, frontmatter}]."""

@mcp.tool()
def resolve_id(alias: str) -> dict:
    """Resolve any alias to canonical form.
    Returns {canonical, kind, source_path, line, context, current_state}."""

@mcp.tool()
def list_identifiers(kind: str, since_session: int | None = None,
                     until_session: int | None = None, state: str | None = None) -> list[dict]:
    """Enumerate IDs by kind and optional session range / state.
    Returns [{canonical, kind, source_path, session, state}]."""

@mcp.tool()
def traverse(start_id: str, relations: list[str] | None = None, max_depth: int = 3,
             direction: str = "out") -> dict:
    """Multi-hop cross-reference walk from start_id.
    Returns {nodes: [...], edges: [...], depth_reached: N}."""

@mcp.tool()
def warrants_currently_met(state_context: dict | None = None) -> list[dict]:
    """For each preserved minority: evaluate activation warrants against current state.
    Returns [{minority_id, warrant_text, firing: bool, evidence: [...]}]."""

@mcp.resource("file://{path}")
def read_file(path: str, section: str | None = None) -> str:
    """Return file content, optionally scoped to a markdown section anchor."""
```

Tool-call semantics are idempotent (no write paths through the MCP). The `warrants_currently_met` tool's `state_context` is a structured dict the Case Steward populates with current-session signals (active-OI IDs, recent decisions, validator-fail conditions) — the tool then evaluates each preserved minority's warrant prose against those signals via structured match. First implementation: regex-match warrant trigger phrases against state-context keys. Later iterations can add richer trigger-matching without breaking the tool signature.

### 3.4 Indexer shape

`tools/build_retrieval_index.py` (~300 LOC after schema expansion):

1. Walk workspace for `*.md` via `pathlib.Path.rglob('*.md')`, excluding `.git/`, `.claude/`, `.cache/`, superseded spec versions (filename regex `-v[0-9]+\.md$`).
2. For each file: parse frontmatter via `yaml.safe_load` on content between `---\n...\n---\n` delimiters; split body; compute `kind` from path conventions (`specifications/` → spec; `provenance/NNN-*/` → provenance; `open-issues/` → open-issue; etc.); extract `session` from path prefix via regex; read mtime via `stat()`.
3. Regex-extract IDs from body via a centralised pattern registry:
   ```python
   ID_PATTERNS = {
     'decision': r'\bD-\d{3}\b',
     'open-issue': r'\bOI-\d{3}\b',
     'minority': r'§\d+(?:\.\d+)*(?:-M\d+)?',
     'watchpoint': r'\bWX-\d+-\d+\b',
     'session': r'\bS(?:ession\s+)?0?\d{1,3}\b',
     'engine-version': r'\bengine-v\d+\b',
     'feedback': r'\bEF-\d{3}(?:-[a-z0-9-]+)?\b',
     'trigger': r'\bd01[0-9]_\d+\b',
   }
   ```
4. Load `specifications/aliases.yaml`; populate `aliases` table; use alias map to resolve `id_text` → `canonical`.
5. Extract edges from explicit citation patterns (`[archive: path]`, `supersedes: path`, `triggers_met: [...]`, prose `per D-NNN`, etc.). Initial implementation is conservative — only edges with clear citation shape — and grows incrementally.
6. Flatten frontmatter into `frontmatter_kv` one-row-per-scalar-or-array-element.
7. `INSERT INTO documents` → `INSERT INTO identifiers` → `INSERT INTO frontmatter_kv` → `INSERT INTO edges` → `INSERT INTO aliases` in one transaction.
8. Populate `docs_fts` via `INSERT INTO docs_fts(docs_fts) VALUES('rebuild')`.
9. `VACUUM` for compactness; `PRAGMA integrity_check`.

Total: single-file tool, stdlib + `pyyaml`, ~300 LOC.

### 3.5 Rebuild trigger

**Recommendation**: both (belt-and-braces) per shared brief Q5.

- **Session-open mtime check** — the primary trigger. Compare `retrieval.db`'s mtime to the max-mtime across `*.md` files; rebuild if stale. This is the authoritative trigger because it catches the mid-session edit case. Implemented as the first line of the MCP server's startup path (ensures the index is current before any tool call). Cost: ~140 ms on cold start when stale; ~5 ms filesystem scan when fresh.
- **Git post-commit hook** — the opportunistic trigger. Runs after every commit that touched a `*.md` file. This keeps the index warm for the next session's session-open check. Implemented as `.git/hooks/post-commit` (gitignored path). Cost: ~140 ms per commit; non-blocking to the commit itself (hook failure doesn't abort the commit).

Honest-limit if index is stale (per shared brief Q5): the session-open check catches all cases except the MCP-server-running-during-edits case (which does not exist in the current workflow — MCP servers are session-scoped). In that hypothetical, `warrants_currently_met()` and `traverse()` could return stale results; `search()` and `resolve_id()` would simply not find newly-added files. The mitigation is: MCP server code checks mtime on every tool call and rebuilds if stale (adds ~5 ms filesystem scan to each tool invocation; acceptable).

### 3.6 File plan

New files (adding at adoption):

- `tools/build_retrieval_index.py` (~300 LOC)
- `tools/retrieval_server.py` (~250 LOC)
- `specifications/aliases.yaml` (starts empty; populated per session)
- `.mcp.json` (MCP server registration; committed)
- `specifications/identifier-canon.md` (new spec; canonical form rule per ID class)

Modified files:

- `specifications/methodology-kernel.md` v6 → v7 (new §1a Warrant-evaluation sub-activity per Q3 — details below)
- `specifications/engine-manifest.md` §2 → engine-v9; §3 → add substrate files per Q7 decision; §7 → new engine-v9 entry
- `specifications/validation-approach.md` v5 → v6 (adds Tier 1 check 24 per Q8 baseline)
- `tools/validate.sh` — add check 24
- `.gitignore` — add `.cache/retrieval.db` and `.git/hooks/post-commit` not required (hooks are always ignored by git) but add `.cache/` blanket
- `specifications/read-contract.md` v5 → v6 — optional, documenting that `specifications/aliases.yaml` is default-read (tiny file; under budget)

Preserved:

- `methodology-kernel-v6.md` (superseded witness)
- `validation-approach-v5.md` (superseded witness)
- Pre-v6 prompts and `read-contract.md`/other specs unchanged.

## 4. External-application portability design

Per shared brief §2b, external-application portability (Q7 in the 8-question agenda) is load-bearing, not deferrable. The substrate MUST bootstrap into every external-application workspace.

### 4.1 Engine-definition classification (my Q7 answer)

**Recommend Q7 = (a) engine-definition.** Specifically: `tools/build_retrieval_index.py`, `tools/retrieval_server.py`, `.mcp.json`, `specifications/aliases.yaml` (empty scaffold), `specifications/identifier-canon.md` all added to `engine-manifest.md` §3 at the v8 → v9 bump. External workspaces inherit these files byte-identically at bootstrap.

**Why engine-definition, not engine-adjacent (b)**:
- The `methodology-kernel.md` §1 Warrant-evaluation sub-activity (Q3) will call MCP tools that exist only if the substrate is installed. If the substrate is engine-adjacent, the kernel's required behaviour is conditional on an inconsistently-inherited tool — that is the kind of asymmetry that OI-017 (engine-vs-methodology reframing) was intended to prevent.
- S046 D-142 precedent — `tools/bootstrap-external-workspace.sh` classified ancillary-tooling, not engine-definition — does NOT govern here because that script is the bootstrap mechanism, not the artefact being bootstrapped. A bootstrap script does not travel; the things it installs do travel.
- S048 D-153 precedent — read-contract.md carve-out for applications/ — is useful methodologically but orthogonal: that was about scope of a spec, not engine-definition membership of a tool.

**The honest cost to this recommendation**: every external-application workspace pays the `pyyaml` + `mcp[cli]` dependency floor at bootstrap, plus the ~18 MB initial index build. For disaster-response (current scale) the build is <1 MB and takes ~10 ms. For a hypothetical future 457-file external-application it would match self-dev scale. This cost is acceptable because (a) it's paid once per workspace, (b) the wheels are near-ubiquitous, (c) the methodology's value proposition includes retrieval-substrate as a named capability under this decision.

### 4.2 Bootstrap script modifications

`tools/bootstrap-external-workspace.sh` (currently ancillary per S046 D-142) extends its current behaviour as follows:

After the existing step 5 (scaffold development-provenance) and before step 8 (validator smoke-test), insert:

```bash
# 5b. Install retrieval substrate dependencies.
echo "[5b] Installing retrieval substrate dependencies (pyyaml, mcp[cli])..."
# Note: assumes uv or pip is available. The script detects which and uses the preferred.
if command -v uv >/dev/null 2>&1; then
  (cd "$TARGET" && uv tool install pyyaml mcp[cli])
else
  python3 -m pip install --user pyyaml 'mcp[cli]'
fi

# 5c. Build initial retrieval index for the new workspace.
echo "[5c] Building initial retrieval index..."
(cd "$TARGET" && mkdir -p .cache && python3 tools/build_retrieval_index.py)

# 5d. Install git post-commit hook for incremental rebuild.
echo "[5d] Installing git post-commit hook..."
# Hook is installed only if the operator initialises git later; we write the script
# but leave installation to the operator's `git init` step.
cat > "$TARGET/.git-hooks/post-commit" <<'HOOK_EOF'
#!/usr/bin/env bash
python3 tools/build_retrieval_index.py >/dev/null 2>&1 || true
HOOK_EOF
chmod +x "$TARGET/.git-hooks/post-commit"
# Operator's "Next steps" output will instruct them to symlink .git-hooks/post-commit
# into .git/hooks/post-commit after `git init`.
```

The bootstrap script's "Next steps" output (currently in the script's tail) gains a line pointing the operator at the hook install command.

### 4.3 Workspace-relative index location

Index file lives at `.cache/retrieval.db` in every workspace (self-dev and external-application alike). `.cache/` is gitignored workspace-wide via the root `.gitignore`. Rationale: `.cache/` is a widely-recognised convention for derived files; keeps the substrate's derived state out of the provenance-preserving directories.

### 4.4 .mcp.json shape for external workspaces

The bootstrap script writes a workspace-scoped `.mcp.json` (committed to the external workspace's git) with:

```json
{
  "mcpServers": {
    "selvedge-retrieval": {
      "type": "stdio",
      "command": "python3",
      "args": ["tools/retrieval_server.py"],
      "env": {}
    }
  }
}
```

This `.mcp.json` is workspace-local; no MCP-level configuration is inherited from self-dev into external workspaces except the command-shape. Each external workspace's `.mcp.json` points at its own `tools/retrieval_server.py` (copied byte-identical from self-dev at bootstrap) and its own `.cache/retrieval.db` (built at bootstrap; refreshed at every commit).

### 4.5 Per-workspace config file

**Recommend none.** No per-workspace retrieval-substrate config. The substrate's behaviour is uniform across workspaces; variation between workspaces is entirely data-driven (whatever is in the workspace's `*.md` files at index time). The sole mutable-per-workspace datum is `specifications/aliases.yaml`, which starts empty in external workspaces and accumulates as aliases are identified — this is data, not config.

**Failed criterion here**: I considered adding a per-workspace `tools/retrieval_config.yaml` for things like corpus-exclusion globs, custom ID patterns, tokenizer tuning. I decided against it because (a) every such config adds a divergence vector across workspaces that undermines the "methodology is uniform" value, (b) the patterns are shipped in `tools/build_retrieval_index.py` itself and can be overridden by editing the file (external workspaces rarely need to), and (c) YAGNI at S050. If an external-application workspace later needs corpus-exclusion customisation, the engine-v10 can add the config file. I'm recording this considered-and-rejected alternative for P4's revision-traceability guard.

## 5. Answers to Q1–Q8

**Q1 (primary substrate choice)**: Substrate-1 SQLite FTS5 on the three tie-breaking criteria enumerated in §2 above. Runner-up is Substrate-2 DuckDB+FTS with its own clear argument on the frontmatter-ergonomics criterion. Rejected: Substrate-3 tantivy-py (scale mismatch; Rust-wheel portability risk); Substrate-4 Whoosh-Reloaded (ecosystem maturity); Substrate-5 bm25s+SQLite (no functional win; higher dependency floor). Defer-and-stay-lexical is a respectable P2 position but I assess the write-side/read-side asymmetry EF-047 named as real; the substrate adoption pays back on the warrants-currently-met tool alone.

**Q2 (adoption scope)**: Incremental phased, per the design-space §8.2 Q2 framing. Phase 1 at engine-v9 (this S050's adoption output): `documents` + `identifiers` + `docs_fts` tables; `search` + `resolve_id` + `list_identifiers` MCP tools; bootstrap integration; basic rebuild triggers. Phase 2 at a future session: add `edges` + `frontmatter_kv` tables and `traverse` + `warrants_currently_met` tools. Phase 3: validator check 24 and kernel §1a amendment. Rationale: phase 1 demonstrates value on the highest-traffic query classes (search + ID lookup) with the smallest-surface-area kit; phases 2 and 3 add structure after phase 1's usage patterns are observed. Go/no-go gate for phase 2: phase 1 used at least 10 times in a non-MAD session without friction. I concede this is a P2-friendly framing; P2 may argue phase 1 alone is sufficient and phase 2 is never warranted — that is a legitimate position and I'm naming it as such rather than pre-empting it.

**Q3 (kernel §1 amendment shape)**: Add §1a "Warrant-evaluation" as a named sub-activity of §1 Read. Text: *"At session open, after completing the workspace and archive reads enumerated above, the Case Steward invokes the retrieval substrate's `warrants_currently_met()` tool (per `engine-manifest.md` §3) to obtain the structured list of preserved minorities whose activation warrants may have fired. The Case Steward evaluates each listed minority against the session's context and records the evaluation in the 00-assessment.md minority-activation-warrant check section. If the retrieval substrate is unavailable (MCP server not running, index missing, post-bootstrap but pre-first-build), the session degrades to prose-scan warrant evaluation and declares the degradation in its honest-limits section."* The degradation clause is load-bearing: it ensures the kernel works even when the substrate doesn't, preserving the decades-of-plain-markdown fallback.

**Q4 (alias vocabulary)**: SKOS three-label (prefLabel / altLabel / hiddenLabel) per design-space §3.3. The three-label distinction earns its keep: `altLabel` for semantically-equivalent surface variants (`D-152` ↔ `Decision 152`); `hiddenLabel` for historical or misspelled variants that should resolve but not be promoted (`reviser minority` → `§10.4-M5`). Starts empty; grows per session as the Case Steward notices alias-emerging patterns in deliberation. Two-label is almost sufficient but loses the historical-variant category, which matters once aliases accumulate across years.

**Q5 (rebuild trigger)**: Both (belt-and-braces) per §3.5. Session-open mtime check is authoritative; git post-commit hook keeps the index warm. Honest-limit stated in §3.5 above.

**Q6 (cross-spec `syncs_with:` frontmatter field)**: Fold into the `edges` table at phase 2. At phase 1 (this S050), defer. Rationale: EF-047 level B proposed `syncs_with:` as a declarative cross-spec intent field. Under the substrate framing, the `edges` table already captures the cross-spec relation as extracted-reference — the `syncs_with:` field would be declaration-of-intent over and above. The distinction matters: `edges` captures what is cited; `syncs_with:` captures what should be kept in sync even if not currently cited. This is a legitimate distinction. But the phase-1-to-phase-2 split says: get `edges` working first, observe whether cross-spec citation hygiene is satisfied by it alone, add `syncs_with:` if and only if gaps surface. I'm consciously erring on the side of smaller surface at phase 1 — P4 should note this as a concession toward P2's maintenance-cost critique.

**Q7 (external-application inheritance)**: Engine-definition per §4.1 above. The four substrate files (`tools/build_retrieval_index.py`, `tools/retrieval_server.py`, `.mcp.json` template, `specifications/aliases.yaml` empty scaffold) are added to `engine-manifest.md` §3. Bootstrap script extended per §4.2. Index file is workspace-relative at `.cache/retrieval.db`.

**Q8 (validator check 24 scope)**: Baseline (preserved-minority pointer verification) at phase 3. Specifically: for each `§10.x`/`§5.x` minority block in active specs, verify the `identifiers` table has a row for the minority's canonical ID with a source_path pointing to an active specification; also verify the minority's source-archive-path (`§10.x "Source:"` field) resolves to an existing file. The extended scopes (every `[archive: path]` citation resolves; every ID in prose resolves to canonical) are legitimate but over-kit for phase 3 — they'd catch real drift but also produce false-positive noise from informal prose references. Adopt baseline; extend at a future session if drift emerges. For external-application workspaces: check 24 is self-adjusting because minorities in the engine are inherited (present in the workspace) and minorities of the application accumulate fresh — the check runs against whatever's there, same implementation.

## 6. Counter-frames

**P4 will most likely raise**: "Substrate-1 is chosen on a tie-breaker that privileges a dependency-floor cost for hypothetical future external-application workspaces, while the actual current workspace state is 1 self-dev + 1 external-application. The privileged cost is imagined; the frontmatter-ergonomics cost Substrate-2 would eliminate is real and observable now. P1 is laundering the Substrate-1 preference through the portability argument."

**Pre-emption**: I concede the tie-break depends on future-workspace-count. If P4 or P2 proposes Substrate-2 on frontmatter-ergonomics grounds alone at current scale, that is a legitimate position and I will not argue the substrate decision is against-reasonable-dissent. The portability argument is not the only argument for Substrate-1 — ecosystem-maturity and snippet/highlight ergonomics both favour Substrate-1 independently — but it is the argument that elevates Substrate-1 from "comparable" to "preferred". I'd want to hear P4's reply on whether ecosystem-maturity alone is decisive, given the 9-year FTS5 track record vs. 2-year DuckDB-FTS track record.

**P2 will most likely raise**: "Phase 1 as proposed is already over-built. The minimum-viable kit is FTS + `search()` alone. `resolve_id()` and `list_identifiers()` add tables and tools that don't solve a named problem surfaced before S050. The EF-047 record named retrieval asymmetry around warrants; the warrants tool is phase 2. Build the phase 2 tool; defer everything else."

**Pre-emption**: `resolve_id()` solves a real problem on the indexer side — without alias resolution, `search('M5')` fails to find `§10.4-M5` documents because they're indexed under their canonical form. `resolve_id()` is what makes `search()` usable across the actual alias vocabulary in the corpus. `list_identifiers()` solves the "what OIs opened between S020 and S030 remain open" class of structured query named in design-space §1 item 2 — this is a real query shape, not speculative.

**Shared-frame counter (P3/P4 convergence point)**: "P1 is framing this as 'add a text-file + index substrate'. The frame P1 and P2 share is that the markdown files remain canonical and a substrate indexes them. An alternative frame is: move the structured data (decisions, OIs, minorities) out of markdown prose into structured artefacts (YAML/JSON per decision, per OI, per minority) and query the structured artefacts directly. The shared frame is 'markdown-as-canonical' which may be the actual constraint driving this decision."

**Partial concession and rebuttal**: P3 may well raise this and it's a legitimate frame. Restructuring the artefacts is a real alternative. My defence: markdown-as-canonical is the workspace's 49-session accumulated invariant. Restructuring would invalidate every preserved minority's source-path, every `[archive: path]` citation, every validator check — a methodology-self-revolution of a scale that S049 did not contemplate and S050 does not have mandate to execute. The substrate under the current canonical form is adoption-feasible at S050; restructuring-to-structured is a multi-session arc in its own right. If P3 argues for that arc as a separate future decision, I concur; if P3 argues for it in place of the substrate adoption, I disagree on scope grounds.

## 7. Measurable adoption criteria

Per §5.1 step 7 P4 guard: concrete measurable, not aspirational.

**Criterion 1 — substrate use rate**: By S055 close (five sessions after adoption), the `warrants_currently_met` / phase 2 tool OR the phase 1 `search` / `resolve_id` tools have been invoked at least 15 times across the 5 sessions, recorded as session-open honest-limit entries or in-deliberation tool-call logs. Threshold: <5 invocations triggers revisit-and-evaluate-abandonment; 5–15 triggers phase-2-gating-review; 15+ triggers phase-2 adoption if not yet done. Revisit session: S055 close.

**Criterion 2 — validator check 24 coverage**: By the first session in which check 24 runs in phase 3 (projected S053+), the check passes on 100% of active-spec minorities OR the failure surface has been reduced session-over-session. Threshold: failure rate increasing session-over-session triggers decision-revisit. Revisit session: first S054+ session where check 24 failure persists across two sessions.

**Criterion 3 — rebuild latency observed**: By S053 close, measured full-rebuild latency in self-dev ≤ 500 ms p95 across 10 observed rebuilds. Threshold: p95 > 500 ms triggers indexer-optimisation micro-session OR substrate-revisit. Revisit session: S053 close.

**Criterion 4 — external-workspace smoke-test**: The next external-application bootstrap (any session after substrate-shipped-to-bootstrap) produces a working index on first try, validated by the bootstrap smoke-test showing check 24 passing. Threshold: bootstrap-failure triggers emergency substrate-revisit in that same session.

**Criterion 5 — FTS5 API churn**: Over the 2026-04-24 to 2028-04-24 window, SQLite FTS5 DDL syntax or BM25 function signature changes trigger revisit. Threshold: any upstream breaking change. Revisit mechanism: Case Steward tracks the SQLite release-notes URL in `specifications/aliases.yaml` frontmatter OR `specifications/identifier-canon.md`. I concede this is a soft criterion because "track release notes" is aspirational without a scheduled check — P4 should note this weakness explicitly.

**Criterion 6 — adoption-sunset condition** (falsification path, not just vindication): If two consecutive sessions in the S053+ window make no substrate tool call AND produce no workspace-structural problem that would have been easier with the substrate, P2's defer-was-right position is retroactively vindicated and the substrate should be considered for deprecation. Threshold: zero-use across 2+ consecutive sessions without problems. Revisit session: first S054+ where this holds.

## 8. Cross-session precedents cited

Per P4 guard: cross-session touch.

- **S046 D-142 ancillary-tooling precedent** — `tools/bootstrap-external-workspace.sh` as ancillary, not engine-definition. I cited this in §4.1 and argued it doesn't govern the substrate decision because the bootstrap script is the mechanism, not the artefact. The distinction is load-bearing to the Q7 recommendation of engine-definition.
- **S048 D-153 read-contract carve-out precedent** — `applications/` as outside §1 closed enumeration via §2d. I cited this in §4.1 and noted it's orthogonal to the substrate decision (scope of a spec, not engine-definition membership of a tool). Its relevance is: it's a precedent for engine-level decisions carving out explicit scope for external-application concerns, which the substrate's external-application portability design does in a different axis.
- **S049 design-space** — the prior synthesis. I cited §3.2 schema, §3.4 MCP tool surface, §3.5 rebuild discipline, §4.1 architecture, §6 rejections, §8.2 Q2 phased-framing throughout — and retracted §3.1, §4 header, §5.4, §6.4 bullet 4 per §2a overlay. Where I agreed I cited; where I disagreed (the original §4.1 `tokenchars '-_'` vs. my §3.2 `tokenchars '-_§'`) I cited and rebutted.
- **OI-017 engine-vs-methodology reframing precedent** — cited in §4.1 against classifying substrate as engine-adjacent rather than engine-definition. The precedent enforces that engine-required behaviour must not depend on inconsistently-inherited tools.

This perspective ends.
