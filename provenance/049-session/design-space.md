---
session: 049
title: Design-space — retrieval substrate for the Selvedge methodology workspace (synthesis + S050 MAD menu)
date: 2026-04-24
status: synthesis-artefact
author: Case Steward (single-orchestrator synthesis with research sub-agents)
scope: input to Session 050 dedicated multi-agent deliberation
---

# Design-space — retrieval substrate for the Selvedge methodology workspace

## Purpose of this document

This document synthesises a design-space for the retrieval-substrate question surfaced in `engine-feedback/inbox/EF-047-retrieval-discipline-and-text-system-scaling-ceiling.md`. Per operator scope revision at S049 Halt 1 ("recommendations should include data structure changes rather than 'discipline' only … real scalable technical solutions … not constrained by 'watching' growth or summarising or archiving … it demands real engineering rigour"), the EF-047 record's original level (A) framing (kernel-discipline-only minor) is set aside; the session's scope becomes synthesis + options + meta-decision, deferring substantive adoption-deliberation to Session 050.

The document is designed to be loaded as input to the S050 MAD. It is not itself a decision record; S050 produces the decision record.

## 1. Problem restatement under operator-revised framing

The EF-047-retrieval-discipline record named three converging pressures (retrieval asymmetry; index-of-indices ceiling; agents cannot look where indices don't point) and offered three adoption levels (A minimum-viable kernel amendment; B cross-spec `syncs_with` field; C structured retrieval substrate). The operator's revision at S049 reframes this: treat the problem as a **substrate question**, not a **discipline question**. The "watch growth / archive / summarise" mechanisms currently in place are write-side guarantees; the gap is a read-side substrate that can:

1. **Resolve identifiers.** Given any ID form (`§10.4-M5`, `M5`, `Reviser OI-tag-only`, `D-152`, `OI-019`, `WX-34-1`, `EF-047-*`, `d016_2`), return the canonical form + authoritative location + current state.
2. **Answer structured queries.** "Every decision whose `triggers_met` includes `d016_2` across all sessions." "Every preserved minority whose activation warrant references `WX-28-1`." "Every OI opened between Sessions 020 and 030 that remains open."
3. **Answer prose queries.** "Which sessions contain substantive discussion of retrieval discipline?" With ranked relevance (BM25 or equivalent), not just grep hit-lists.
4. **Traverse the cross-reference graph.** "From this decision, show me every OI it cites, every watchpoint it references, every session that cited it back, every spec it modified." Multi-hop.
5. **Do this fast, from an agent context, without burning the session's context budget.** Sub-second query latency; results small enough to compose with further reads without blowing the 200K-token working budget.

The operator explicitly named five candidate mechanisms (inverted index with BM25, identifier normalization with alias tables, structured frontmatter with metadata filters, key-value lookup for direct ID resolution, regex for exact patterns), and a target deployment shape (local FTS5 index over full files exposed via MCP as a fast lookup layer). The remainder of this document evaluates that direction against the workspace's concrete state and positions it on a menu of alternatives.

## 2. Workspace state (measured, not estimated)

Measurements taken at S049 open (pre-assessment-commit state):

### 2.1 Scale

| Metric | Value | Source |
|--------|-------|--------|
| Total markdown files (workspace-wide) | **457** | `find … -name '*.md' \| wc -l` |
| Total words across all markdown | **1,417,639** | `wc -w` over the same set |
| Default-read surface (§1 enumeration) | 66,372 words / 19 files | `tools/validate.sh` check 20 |
| `provenance/` directory size | 15 MiB | `du -sh` |
| `specifications/` directory size | 740 KiB | `du -sh` |
| `open-issues/` directory size | 176 KiB | `du -sh` |
| `engine-feedback/` directory size | 80 KiB | `du -sh` |
| Session count | 49 | `provenance/NNN-*/` directory count |

**Implication.** The full workspace is ~20× the default-read aggregate. A retrieval substrate covers the full corpus (archive surface included); the default-read surface is only the subset guaranteed to be loaded at session-open. This matters: the retrieval-discipline gap is precisely about traversing the archive surface when needed, not just the default-read subset.

### 2.2 Identifier densities (measured grep counts)

| ID class | Approximate grep count (workspace-wide) | Authoritative source |
|----------|-----------------------------------------|----------------------|
| `D-NNN` (decisions) | ~4,362 | `provenance/NNN-*/02-decisions.md` |
| `OI-NNN` (open issues) | ~4,243 | `open-issues/OI-NNN.md` + `resolved/OI-NNN.md` |
| `Session NNN` / `S0NN` | ~10,286 | folder prefix on `provenance/NNN-*/` |
| `WX-NN-N` (watchpoints) | high hundreds | scattered across spec `§10.x` blocks + close files |
| `engine-vN` (engine versions) | ~1,458 | `specifications/engine-manifest.md` §7 |
| `EF-*` (engine-feedback records) | ~60 (new class; inbox + triage + cross-refs) | `engine-feedback/{inbox,triage}/` |
| `[archive: path]` (archive-pack references) | low dozens | validator check 22 tracked |
| `d016_N`, `d023_N` (MAD triggers) | dense per-decision | every post-S006 decision carries annotation |

**Implication.** IDs are the dominant query vocabulary. The workspace is ID-crisp, not semantically-fuzzy. This shapes substrate choice: **lexical / exact-match / structured-filter retrieval is aligned with query shape; semantic / embedding retrieval is misaligned** (see §6.4 below).

### 2.3 Preserved-minority density

31 first-class minorities currently preserved across active specifications. Highest density in:
- `workspace-structure.md` v5 §10.4-M1 through §10.4-M6 (6 Session 036 minorities)
- `read-contract.md` v5 §5.1 through §5.14 (multiple minorities across sessions)
- `reference-validation.md` v3 §10.1 through §10.8 (Cell 1 + Cell 2 + Cell 3 minorities)

Every minority has **write-side pointers**: archive path to its source `provenance/NNN-*/01X-perspective-*.md`, activation-warrant prose with specific firing condition, reopen-warrants where applicable. **Read-side retrievability is prose-scan-dependent**: a Case Steward at session-open must manually walk each spec's §10 block to evaluate whether any activation warrant has fired against current session context. No validator check, no default-read index, no query surface enumerates "which minorities have warrants currently met?"

### 2.4 Cross-reference frontmatter fields (catalogue)

From the codebase survey, distinct frontmatter fields that carry cross-reference values:

- `supersedes:`, `superseded-by:`, `superseded-in-session:` — spec version chain
- `last-updated:`, `updated-by-session:`, `created_session:`, `marker_adopted_session:` — temporal markers
- `engine_version_at_creation:`, `engine_version_at_marker_adoption:`, `engine_version_at_load:` — version pointers
- `feedback_ref:`, `triaged_in_session:`, `scheduled_mad_session:` — feedback lifecycle
- `source_workspace_id:`, `source_session:` — engine-feedback origin attribution
- `operator_directed_resolution:` — S048 new field
- `opened_issue:`, `resolved-in-session:`, `surfaced-in-session:` — OI lifecycle
- `status:` — multi-use ({active, superseded, open, resolved, new, triaged, inbox})
- `mode:`, `workspace_id:` — workspace identity
- `id:` — OI/EF unique identifier (frontmatter-declared)
- `triggers_met:`, `triggers_rationale:` — per-decision (body annotation, not frontmatter)

**Implication.** Frontmatter is already a structured index in all but name. Extracting it into a relational table is a near-trivial transformation; the structure is there, just not indexed.

### 2.5 `tools/validate.sh` is already a retrieval substrate

Validate.sh performs 1,129 structural assertions across 23 checks. Effective queries it executes:

- Existence, cardinality, schema, consistency, integrity, reference-resolution, state, budget, membership, temporal.

In relational terms: it's a shell-implemented set of SELECT-JOIN-AGGREGATE queries over the file system, encoded as bash arrays + grep pipelines. The EF-047 record's observation is correct: **the workspace is already running a database, just without saying so.**

### 2.6 Git history as implicit retrieval

Commits carry very long prose bodies (recent commit messages are 800–1,070 words each). `git log -S '<string>'` returns sessions where a specific ID was introduced, cited, or removed. This is a **temporal** retrieval substrate that no in-workspace text file reproduces — once a statement is removed from an active file, git is the only remaining substrate that surfaces it without opening archive-packs.

## 3. The core decision for S050

The retrieval-substrate decision reduces to a set of coupled choices:

### 3.1 Primary substrate (pick exactly one)

- **P1 SQLite FTS5** — stdlib, zero install, fast, mature, BM25 native. Regular (content-carrying) table shape. This is the operator-named default.
- **P2 DuckDB + FTS extension + `edges` table** — strongest competitor. Table-centric model unifies frontmatter-filter queries with prose FTS without a JOIN across virtual+real tables. FTS extension is flagged experimental upstream. Property-graph extension (DuckPGQ) available for cross-reference traversal.
- **P3 tantivy-py** — Rust-backed, higher throughput. Overkill at 457 files; reject unless future external-application scale forces re-evaluation.
- **P4 Whoosh-Reloaded** — pure-Python fallback for environments where SQLite C extensions are awkward. Not the primary choice; escape hatch.

### 3.2 Schema shape (pick the shape; bound to the substrate choice)

Proposed schema (applies to P1 and P2 with syntax variation):

```
documents         (path, kind, session, mtime, title, frontmatter_json, body)
identifiers       (id_text, id_kind, canonical, source_path, line, context_snippet)
frontmatter_kv    (path, key, value)         -- flattened YAML
edges             (src_id, src_kind, dst_id, dst_kind, relation, source_path, session)
aliases           (alias, canonical, kind, added_session, last_seen_session)
docs_fts          (FTS5 virtual table OR DuckDB fts-indexed column)
```

Five tables + one FTS structure. The indexer parses markdown + YAML + regex-extracts IDs + resolves aliases → all five tables. Estimated complexity: ~250–400 LOC Python, single-file tool.

### 3.3 Alias discipline (SKOS-inspired three-label vocabulary)

A canonical form rule recorded in a new or amended specification, plus a YAML alias file at `specifications/aliases.yaml`:

```yaml
- canonical: "§10.4-M5"
  kind: minority
  aliases:
    - "M5"
    - "Reviser OI-tag-only"
    - "§10.4-minority-5"
  hidden:
    - "reviser minority"
- canonical: "D-152"
  kind: decision
  aliases:
    - "Decision 152"
    - "the Path T decision"
```

SKOS `prefLabel / altLabel / hiddenLabel` maps cleanly. No RDF infrastructure needed; plain YAML + a regex normalizer is sufficient. The file feeds the `aliases` table at indexer run.

### 3.4 Exposure layer (MCP server)

FastMCP (official Anthropic Python SDK, `pip install "mcp[cli]"`) as a stdio MCP server at `tools/retrieval_server.py`. Registered in `.mcp.json` at project scope (committed to the repo). Exposed tools and resources:

- `search(query, k, filters)` — FTS query with BM25 ranking + optional frontmatter filters. Returns `[{path, snippet, score, frontmatter}]`.
- `resolve_id(alias)` — resolves any alias to canonical form; returns `{canonical, kind, source_path, current_state}`.
- `list_identifiers(kind, since_session, filter)` — enumerate IDs by kind/session/state.
- `traverse(start_id, relations, max_depth)` — multi-hop cross-reference walk.
- `warrants_currently_met()` — scan preserved minorities; evaluate activation warrants against current state; return firing candidates.
- Resource: `file://{path}` with optional `#section` anchor for segment retrieval.

Reference implementation that matches the target shape: `pvliesdonk/markdown-vault-mcp` (FTS5 + frontmatter-aware indexer + MCP server).

### 3.5 Rebuild discipline

The index file (`retrieval.db` or `index.duckdb`) is **gitignored**. Source of truth remains markdown. Two trigger points:

- **Git post-commit hook** — rebuild on every commit.
- **Session-open mtime check** — if any `*.md` has mtime newer than the index file, rebuild. This handles the case where a session edits files without committing mid-session.

Measured rebuild cost (from research): **~140 ms for 457 files on stock Python + SQLite 3.53**. Fast enough to be invisible.

### 3.6 Coupled decisions

- **Validator check extension**: add check 24 verifying that every preserved minority's activation-warrant text has a corresponding pointer in the `identifiers` table (i.e., that the retrieval substrate has actually indexed the minority). This closes the "write-side discipline has no read-side enforcement" loop.
- **Kernel §1 Read amendment**: add a "Warrant evaluation" sub-activity pointing to `warrants_currently_met()` tool output; the tool returns a structured list that the Case Steward evaluates at session-open. This was the original EF-047 level A; under the revised framing it becomes **the tool-backed version** of the kernel-amendment rather than a prose-discipline-only rule.
- **Spec `syncs_with:` frontmatter field** (original EF-047 level B): defer or fold into the `edges` table — both substrates carry this information; no frontmatter field is strictly required if the indexer extracts it from prose citations.

## 4. Option A: SQLite FTS5 + structured tables + MCP (operator's named direction)

### 4.1 Architecture

- Single SQLite database at `.cache/retrieval.db` (gitignored).
- Five tables (§3.2) + one FTS5 virtual table.
- FTS5 tokenizer: `porter unicode61 tokenchars '-_'` — ID-aware (indexes `D-152` as a single token), stems English prose, handles unicode punctuation.
- Regular (content-carrying) FTS5 shape, not contentless, so `snippet()` and `highlight()` work — these are the auxiliary functions that make the substrate MCP-useful.
- Indexer script in Python stdlib only (`sqlite3`, `pathlib`, `re`, `yaml`). ~250 LOC.
- MCP server: FastMCP stdio, ~200 LOC.
- Dependencies added: `mcp[cli]` (the Anthropic SDK) + `pyyaml` if not already present. Everything else is stdlib.
- Total new LOC: ~400–500.
- Total new files: `tools/build_retrieval_index.py`, `tools/retrieval_server.py`, `specifications/aliases.yaml`, `.mcp.json`.
- Index size: ~18 MiB on disk (~20% of workspace total; gitignored).
- Query latency: sub-millisecond on this corpus. Rebuild latency: ~140 ms.

### 4.2 Strengths

- **Zero install cost** for the database (Python stdlib `sqlite3` ships with FTS5 enabled on macOS).
- **BM25 native**, mature since 2015, well-documented.
- **`snippet()` + `highlight()` auxiliary functions** give focused excerpt returns — exactly the output shape an MCP retrieval tool wants (returns context-economical chunks rather than whole files).
- **Schema is inspectable with stock `sqlite3` CLI** — operators can `sqlite3 retrieval.db '.schema'` and audit.
- **Single-file database** — easy to wipe and rebuild; easy to inspect; easy to copy into external-application workspaces if they adopt the same substrate.
- **Fits macOS dev environment** — no daemon, no port, no lifecycle management.

### 4.3 Weaknesses

- **FTS5 is tokenizer-opinionated**: hyphen handling requires custom `tokenchars`; unquoted `D-152` parses as boolean `D NOT 152` without customisation. Mitigation is one line of `CREATE VIRTUAL TABLE` DDL, but it's a footgun to document.
- **Frontmatter filter queries are awkward**: FTS5 is index-centric; querying "decisions with `triggers_met` containing `d016_2`" requires a JOIN between the FTS5 virtual table and a plain `frontmatter_kv` table. Works, but syntactically heavier than DuckDB's unified-table model.
- **Graph traversal via recursive CTEs** is supported by SQLite since 3.8.3 but syntactically heavier than DuckDB's `USING KEY` optimization.

### 4.4 Library / tool recommendations

- `sqlite3` stdlib (ships with Apple Python; FTS5 compiled in).
- `mcp[cli]` for FastMCP SDK.
- `pyyaml` for frontmatter parsing.
- Reference implementation: `pvliesdonk/markdown-vault-mcp` — same shape; different polyfill.

## 5. Option B: DuckDB + FTS extension + `edges` table + MCP (strongest competitor)

### 5.1 Architecture

- Single DuckDB file at `.cache/retrieval.duckdb` (gitignored).
- DuckDB FTS extension loaded at startup (`INSTALL fts; LOAD fts;`).
- Table-centric schema: `documents` table with `body TEXT`, `frontmatter STRUCT(...)` (native JSON-like typing), `triggers_met VARCHAR[]` (native array type). FTS index created via `PRAGMA create_fts_index('documents', 'path', 'body')`.
- Additional `edges` table for cross-reference graph: `(src_id VARCHAR, dst_id VARCHAR, relation VARCHAR, session INT)`. Recursive CTEs with `USING KEY` (DuckDB 1.2+) for multi-hop.
- DuckPGQ community extension optionally for SQL/PGQ property-graph syntax if the MAD decides graph-query ergonomics are load-bearing.
- Indexer + MCP server similar to Option A but uses `duckdb` Python package instead of `sqlite3`.

### 5.2 Strengths over Option A

- **Unified frontmatter + FTS queries without JOINs**. `WHERE 'd016_2' = ANY(triggers_met) AND match_bm25(rowid, 'preservation minority')` is a single table scan.
- **Native JSON support** — frontmatter is stored typed, queryable without a separate `frontmatter_kv` table.
- **Native array operations** — `triggers_met`, `aliases`, `minorities` as arrays with `ANY`/`ALL` operators.
- **Recursive CTEs are first-class** for graph traversal; DuckPGQ adds SPARQL-like property-graph syntax if wanted.
- **Python `duckdb` package** is pure wheel on macOS, no system dependency.

### 5.3 Weaknesses

- **DuckDB FTS extension is flagged experimental upstream.** Works; BM25 ranking is correct; but the extension's API has churned over 2024–2025 minor versions. This is the biggest stability concern.
- **FTS rebuild is not incremental**: `PRAGMA drop_fts_index` + `PRAGMA create_fts_index` to refresh. At ~150 ms on this corpus, this is fine; at 10× scale it would need rethinking.
- **Adds one dependency** that SQLite FTS5 does not (`duckdb` Python package).
- **Less mature ecosystem for MCP integration** — more reference implementations exist for SQLite-over-MCP than DuckDB-over-MCP as of 2026.
- **`snippet()` and `highlight()` equivalents are less ergonomic** — DuckDB FTS returns scored row IDs; the caller computes snippets via separate string functions.

### 5.4 When Option B is worth adopting over Option A

If the S050 MAD concludes that the **structured-filter + graph-traversal queries** are the dominant query class (e.g., "show me every decision that modified a spec that a minority's activation warrant depends on"), DuckDB's ergonomic advantage compounds. If the dominant query class is **prose full-text search with snippets** (e.g., "find sessions discussing 'retrieval discipline' and show me 30-token excerpts"), SQLite FTS5 is the better fit.

**My read of the workspace's query shape** (from the §2 ID-density data): structured-filter queries dominate. This argues modestly for Option B. But the operator named FTS5 specifically; Option A has the edge on operator alignment + zero install + ecosystem maturity. This is a deliberation question, not a defaulted answer.

## 6. Rejected alternatives (rationales to record at S050)

### 6.1 Meilisearch / Typesense (standalone search servers)

**Reject because**: daemon-based, multi-tenant, frontend-UI-oriented. Typo tolerance is **actively wrong** for ID-crisp queries (`OI-019` fuzzy-matching `OI-018` would produce incorrect results with high confidence). Operational weight (port management, master-key lifecycle, version-upgrade coupling) disproportional to single-dev local scale.

### 6.2 Tantivy / tantivy-py (Rust full-text library)

**Reject because**: scale mismatch. Tantivy's throughput edge over FTS5 only matters above ~10^6 documents. At 457 files, both substrates return results in microseconds. `tantivy-py` binding has had API-breaking changes across minor versions (0.20–0.25) which is maintenance tax on a workspace whose substrate should be stable for years.

### 6.3 Oxigraph / Jena / rdflib (RDF triple stores + SPARQL)

**Reject because**: RDF's schema-design tax is proportional to ontological ambition, not data volume. The workspace would have to declare an ontology, mint IRIs for every entity, write a markdown-to-Turtle transformer, and issue SPARQL — all to produce cross-reference queries that DuckDB edges + recursive CTEs produce directly. Re-evaluate at 10^4+ formal entities (which the workspace will not reach for many years).

### 6.4 Vector / embedding retrieval (explicit rejection with rationale)

**Reject with recorded rationale**: semantically-wrong on the primary query class.

1. **ID-lookup failure mode.** Dense vectors fail at exact-ID lookup. `OI-019` and `OI-018` embed to near-identical vectors (both are "open issues in a methodology workspace"; adjacent numeric; same prefix). A semantic retriever returns them with near-identical scores, a wrong answer with high confidence. The workspace's dominant query is precisely this ID-crisp shape.
2. **Anthropic's own contextual-retrieval guidance.** Per the Anthropic contextual-retrieval blog post, knowledge bases under ~200K tokens fit in context directly; RAG/embeddings are not needed. This workspace's default-read surface is 66K; even loading the full archive surface (~1.4M words total but much smaller at read time) is within an Opus 200K-token context window.
3. **Semantic drift.** Embeddings reward topical similarity. The workspace rewards precise citation fidelity. Objectives are in tension, not alignment.
4. **Operator did not name embeddings.** This is a signal worth respecting. The rejection is explicit and time-scoped: if a future external application produces a large paraphrased-conceptual corpus (e.g., domain-knowledge for a software-engineering project), embeddings may be the right tool for that corpus; they are not right for the methodology workspace itself.

### 6.5 Neo4j / Memgraph (standalone graph databases)

**Reject because**: scale mismatch. These scale to 10^9 edges; the workspace has <10^4. ~500MB RAM floor, commercial licensing friction on Neo4j Community/Enterprise split, daemon operational weight.

### 6.6 `rank_bm25` Python library

**Reject because**: last release 2022-02-16; stale. Successor is `bm25s` (NumPy sparse-matrix implementation; 20×–287× faster on BEIR benchmarks; released 2026-04 actively maintained). If a pure-Python BM25 is wanted (rather than SQLite FTS5's native BM25), `bm25s` is the right library, not `rank_bm25`.

### 6.7 `whoosh` (unmaintained fork)

**Reject because**: original project feature-frozen; Sygil-Dev `Whoosh-Reloaded` fork exists but has low ecosystem momentum in 2026. Useful escape hatch if SQLite C-extension loading becomes constrained; not the primary choice.

### 6.8 `llm` CLI (Simon Willison) / agent-as-retrieval

**Not a substrate choice; a complementary pattern.** The operator's shrinking discipline (close-rotation §2c, archive-pack §4–§9, default-read budget §2b) is the write-side answer; a retrieval substrate is the read-side answer. These are complementary, not competitive. The S050 MAD should name this explicitly: adopting a retrieval substrate does not substitute for continuing the shrinking discipline.

## 7. Complementary components (not primary-substrate choices; adopt alongside)

### 7.1 Git-as-temporal-substrate

`git log -S '<string>'` (pickaxe) and `git log -G '<regex>'` are the only substrate that surfaces **historical prose that has been removed from active files**. Unique capability; no in-workspace text-file substrate reproduces it. Adopt as complement: `tools/git-retrieve.sh` wrapper standardising `when-introduced <id>`, `prose-for-commit <hash>`, `when-last-touched <path>` queries. Zero new dependencies.

### 7.2 ripgrep as baseline floor

Any adopted substrate MUST beat `rg -l '<id>'` on the ID-lookup case. Otherwise the added infrastructure is pure tax. FTS5 and DuckDB both easily clear this bar (sub-millisecond vs ~50–150 ms `rg` scan). The floor check belongs in the adoption criteria, not as a separate substrate.

### 7.3 `validate.sh` extension (new check 24)

New validator check: for every preserved minority in active specs, verify that the retrieval substrate's `identifiers` table contains a row for the minority's canonical ID, with a pointer to the source provenance file. Closes the asymmetry: write-side preserves; substrate indexes; validator enforces both.

### 7.4 NetworkX (Python graph library) as optional complement

If multi-hop graph queries grow beyond what DuckDB recursive CTEs ergonomically support, NetworkX loads the `edges` table into an in-memory graph at query time. Not a substrate choice; an optional complement.

## 8. Recommended S050 MAD structure

### 8.1 Perspective composition (4-perspective two-family per operator S044 R2 standing preference)

- **P1 — Substrate Architect (Claude subagent)**. Proposes specific architecture (tables, tokenizer config, MCP tool surface, indexer shape). Advocates for one of Options A/B with concrete rationale.
- **P2 — Incrementalist / Maintenance Sceptic (Claude subagent)**. Challenges the adoption scope. Asks: does this need to be built in one go, or can we ship Option A-minimal (FTS5 + MCP tools for `search` + `resolve_id` only) and iterate? What is the smallest possible useful substrate; and when does each subsequent addition (edges table; warrants_currently_met; alias table) pay back?
- **P3 — Outsider (Codex/GPT-5.5)**. Frame-completion. Asks: is the problem being framed correctly as a substrate question? Is there a sixth alternative not on the menu (e.g., "agent memory as retrieval" via Claude projects; "make the substrate smaller rather than queryable" via aggressive write-side compression; a hybrid where FTS5 + embeddings serve different query classes and a router picks)? Names the 5th option the Claude perspectives have not considered.
- **P4 — Cross-Family Reviewer (Codex/GPT-5.5)**. Laundering audit per S047 P4 convention. Examines P1+P2 proposals for Claude-lineage reasoning patterns. Applies the P4 anti-laundering guards: failed/strained criteria listing; revision traceability; cross-session touch; concrete measurable adoption criteria.

Convening per D-133 M2 Convene-time role/lineage 7-column matrix populated at MAD launch. Outsider seat MUST be non-Claude (21-for-21 convention). Synonym-drift guard: P3 frame-completion distinct from P4 laundering-audit.

### 8.2 Questions for S050 MAD

**Q1 — Primary substrate choice.** Option A (SQLite FTS5) vs Option B (DuckDB + FTS) vs partial-hybrid vs defer-and-stay-lexical-tools-only. Perspectives state positions; synthesis converges or preserves minority.

**Q2 — Adoption scope.** Full-kit (all five tables + FTS + aliases + MCP server + validator check 24 + kernel §1 amendment) vs incremental (FTS + search + resolve_id MCP tools in phase 1; edges + traversal + warrants_currently_met in phase 2; validator extension in phase 3).

**Q3 — Kernel §1 amendment shape.** If the retrieval substrate ships, does the kernel §1 Read activity gain a "Warrant evaluation" sub-activity that calls the tool? What happens when the tool is unavailable (e.g., index not rebuilt, MCP server not running)?

**Q4 — Alias vocabulary.** Adopt SKOS three-label (prefLabel/altLabel/hiddenLabel) in `specifications/aliases.yaml`? Or simpler two-label (canonical + aliases)? Or defer alias discipline to a later session once substrate is operational?

**Q5 — Rebuild trigger.** Git post-commit hook (auto) vs session-open mtime check (lazy) vs both (belt-and-braces). What is the honest-limit if the index is stale?

**Q6 — Cross-spec `syncs_with:` frontmatter field (EF-047 original level B).** Under the substrate framing, is this field redundant with the `edges` table (which already captures the cross-spec relation), or is it load-bearing at the spec layer as a declaration-of-intent distinct from extracted-references? Deliberate as spec-shape question.

**Q7 — External-application inheritance.** Does the retrieval substrate ship as part of the engine-definition (enumerated in `engine-manifest.md` §3), or as engine-adjacent tooling (ancillary per S046 D-142 precedent)? The distinction is consequential: engine-definition travels byte-identically to external applications; ancillary is local-only.

**Q8 — Validator check 24 scope.** Preserved-minority pointer verification (baseline); OR extended to verify every `[archive: path]` citation resolves through the substrate; OR extended further to verify every ID reference in prose resolves to a known canonical form.

### 8.3 Bundled-minors under the revised S049 framing

The two bundled-minor EF-047 records (brief-slot-template + session-inputs) were bundled with the S049 MAD per S048 D-155 + operator Q4=(b) ratification. Under the revised S049 framing (synthesis + meta-decision; no substantive adoption this session), both bundled minors **defer to S050 alongside the retrieval MAD**. Option set unchanged from S048 triage records.

The session-inputs record's forward observation is methodologically relevant to S050: "**shared-frame blindness potential** in the S047 MAD's 4-of-4 convergence on the session-inputs pattern. S049's 4-perspective two-family MAD on retrieval-discipline + bundled-minor should include an explicit convergence-check step (naming counter-frames for each proposed adoption; any 4-of-4 convergence at S050 is a data point on whether the shared-frame blindness pattern recurred)." S050 MAD should carry this convergence-check as a P4 responsibility.

## 9. Implementation sketch (Option A, if adopted)

### 9.1 File plan

New files:

- `tools/build_retrieval_index.py` (~250 LOC): walks `*.md`; parses frontmatter via `yaml.safe_load`; regex-extracts IDs; loads `aliases.yaml`; builds five SQLite tables + FTS5 virtual table.
- `tools/retrieval_server.py` (~200 LOC): FastMCP stdio server; exposes `search`, `resolve_id`, `list_identifiers`, `traverse`, `warrants_currently_met` tools; `file://{path}` resource.
- `specifications/aliases.yaml` (empty at adoption; populated incrementally): SKOS three-label vocabulary.
- `.mcp.json` (project-scoped MCP server registration; committed to repo).
- `specifications/identifier-canon.md` (optional new spec): canonical form rule per ID class.

Modified files:

- `specifications/methodology-kernel.md` v6 → v7 (new §1a Warrant evaluation sub-activity).
- `methodology-kernel-v6.md` preserved as superseded witness.
- `tools/validate.sh`: add check 24 (preserved-minority substrate-pointer verification).
- `specifications/engine-manifest.md`: frontmatter + §2 current-version + §3 engine-definition file list (+ `tools/build_retrieval_index.py` + `tools/retrieval_server.py` + `.mcp.json` + `specifications/aliases.yaml`?) + §7 new engine-v9 history entry.
- `.gitignore`: add `.cache/retrieval.db` and `.cache/retrieval.duckdb`.

### 9.2 Engine-definition vs ancillary classification

Per S046 D-142 precedent (`tools/bootstrap-external-workspace.sh` classified ancillary-tooling, not engine-definition), S050 needs an explicit decision on where the retrieval tooling lives:

- **Engine-definition** (travels byte-identical to external applications): `tools/retrieval_server.py`, `tools/build_retrieval_index.py`, `.mcp.json`. External applications would inherit the substrate and use it for their own domain artefacts.
- **Ancillary** (local-only; external applications build their own): simpler; avoids forcing a Python + MCP dependency on every external application.

The Q7 deliberation at S050 resolves this.

### 9.3 Testing plan

- Smoke test: index builds successfully against the current workspace (all 457 files); FTS query returns non-empty results for `"§10.4-M5"`, `"d016_2"`, `"retrieval discipline"`, `"preservation"`.
- Round-trip test: every ID in the `identifiers` table has a `resolve_id(canonical)` result pointing back to an existing file at the declared line.
- Rebuild cost benchmark: `time python tools/build_retrieval_index.py` under 500 ms on this corpus.
- MCP server registration: `claude mcp list` shows `cse-retrieval` registered at project scope.
- Integration test: from within a session, call `mcp__cse_retrieval__search("preservation minority")` and verify ranked results include at least one file from `workspace-structure.md` §10.4.

### 9.4 Validator check 24 (proposed specification)

```
[24] Preserved-minority substrate-pointer coverage
     For each §10.x / §5.x preserved-minority block in active specifications:
       - Extract canonical minority ID (e.g., "§10.4-M5").
       - Query identifiers table: SELECT * FROM identifiers WHERE id_text = ? AND id_kind = 'minority'.
       - Assert: exactly one row matches; source_path points to an active specification.
       - Assert: the minority's source-archive-path (§10.x "Source:" field) resolves to an existing file.
     FAIL if any assertion violated.
```

Conditional on retrieval substrate adoption (gated by `RETRIEVAL_SUBSTRATE_ADOPTION_SESSION=NNN` constant).

## 10. What this session's meta-decision does and does not foreclose

### 10.1 Foreclosed at S049 close

- S049 does NOT adopt any substrate. No `methodology-kernel.md` v6 → v7 bump.
- S049 does NOT write any code file. `tools/build_retrieval_index.py` and `tools/retrieval_server.py` remain unwritten.
- S049 does NOT amend `tools/validate.sh`.
- Engine-v8 → v9 candidate is deferred; engine-v8 preserved at S049 close (preservation window count 1).

### 10.2 Produced at S049 close

- This design-space document (synthesis + options + rejection rationales).
- 02-decisions.md recording: scope revision ratified; S050 MAD pre-ratified on shape; bundled minors deferred to S050; substrate deliberation menu locked; perspectives and questions for S050 specified.
- Three triaged EF-047 records remain at `triaged` status (not `resolved`) pending S050.

### 10.3 Preserved for S050

- Q1–Q8 in §8.2 above are the S050 MAD agenda.
- P1–P4 perspective shape in §8.1 is the S050 convening.
- Option A + Option B + rejection rationales in §4–§6 are the S050 MAD input.
- Implementation sketch in §9 is non-binding design input; S050 may revise.

### 10.4 Preserved for post-S050 (if substrate adopts)

- Substrate implementation is itself a multi-step process; even if S050 adopts, the actual indexer + MCP server + validator-check-24 code is written in S051+ sessions per the MAD's incremental adoption schedule (if Q2 incremental wins) or in one S051 session (if Q2 full-kit wins).
- External-application inheritance (Q7) may require `engine-manifest.md` §6 bootstrap-contract amendment if engine-definition classification wins.
- `aliases.yaml` population is a sustained-practice concern; starts empty at substrate adoption and populates as aliases are identified over subsequent sessions.

## 11. Honest limits of this synthesis

- **Single-orchestrator synthesis.** The design-space document is produced by the Case Steward with research sub-agents. It is not a MAD output. The MAD at S050 may reject the framing, surface alternatives not considered here, or re-weight the tradeoffs. This document is input, not foregone conclusion.
- **Measured vs estimated.** Workspace size measurements (§2.1) are measured. ID-density counts (§2.2) are grep counts that include reference mentions, not distinct IDs (e.g., 4,362 `D-NNN` grep hits vs 164 distinct decisions per provenance enumeration). The ratio is informative — every decision is cited ~25× on average — and is itself a retrieval-relevance signal.
- **Research sub-agent summaries.** The three parallel research sub-agent outputs (codebase survey, operator-named candidates deep-dive, adjacent alternatives) were consolidated here with the Case Steward's judgment on emphasis and composition. The raw sub-agent reports are not preserved as separate files per S049's single-orchestrator synthesis shape (they are recoverable from the session's transcript if needed; this is an honest-limit on research-provenance preservation relative to a true MAD).
- **Operator-named candidate bias.** The operator named five candidates in a specific framing. This synthesis treats that framing as load-bearing but not exclusive — §6 documents six alternatives outside the operator's framing, with rejection rationales. If the operator has additional candidates not on either list, S050 should surface them.
- **Query-class measurement is qualitative.** §2.2 and §3 claim "structured-filter queries dominate" but no quantitative measurement of actual-query-class frequency has been performed. S050 MAD perspectives may have different weights on query-class distribution.
- **DuckDB FTS extension's "experimental" flag** is taken from upstream docs at time of research; the flag may be removed in future DuckDB releases. A pre-S050 spot-check of current DuckDB release notes is recommended.
- **MCP API stability.** FastMCP and the Anthropic Python SDK are under active development in 2026; adoption at S050 commits to an API that may evolve. The substrate design should be resilient to MCP API changes (e.g., keep the tool surface small and standard).

## 12. Ready for S050

This document is stable input for the S050 dedicated multi-agent deliberation. It contains:

- Problem restated under operator revision (§1)
- Workspace state measured (§2)
- Core decision structure (§3)
- Option A detailed (§4)
- Option B detailed (§5)
- Six rejected alternatives with rationale (§6)
- Three complementary components (§7)
- MAD perspectives + questions (§8)
- Implementation sketch for Option A (§9)
- Scope boundaries of S049 meta-decision (§10)
- Honest limits (§11)

S050 proceeds as: convene four-perspective two-family per §8.1; produce shared brief referencing this document as the Read input; eight questions per §8.2; synthesis → decide → produce → validate → record → close. Substrate adoption decision is S050's to make.
