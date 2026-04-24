---
title: Perspective — P3 Outsider / Frame-Completion (Session 050)
session: 050
perspective: outsider-frame-completion
perspective_family: codex-gpt-5.5
perspective_role: outsider-frame-completion
date: 2026-04-24
status: immutable-at-commit
provenance_note: verbatim from codex exec --sandbox read-only -o output; raw log at codex-outsider-raw-output.log; model gpt-5.5 reasoning-effort xhigh per ~/.codex/config.toml; Case Steward wrapped with frontmatter only (no body edits)
---

# P3 — Outsider / Frame-Completion

## 1. Frame Critique

The substrate question is real, but it is slightly misnamed. The problem is not primarily "which database indexes Markdown fastest?" It is: **what makes Selvedge claims, warrants, identifiers, and cross-session obligations reliably answerable at read time, across workspaces, without depending on an agent remembering where to look?**

That distinction matters. A SQLite or DuckDB file can make search fast, but it does not by itself decide which questions must be asked, which answer shapes count as sufficient, or which retrieved facts become session obligations. The S049 design-space already hints at this in §2.5: `tools/validate.sh` is "already a retrieval substrate" because it encodes assertions over the corpus. That is closer to the real substrate than FTS alone. The substrate is the combination of answerable records, query contracts, validation, and operational habit. The database is a read model.

I recall from pretraining that many systems distinguish durable source-of-truth records from query-optimized read models. That framing fits here. The Selvedge source of truth can remain Markdown, but the retrieval decision should define a **retrieval contract** first: canonical IDs resolve; warrants can be enumerated; archive paths can be verified; cross-spec obligations can be listed; query results carry file pointers and confidence limits. Once that contract is fixed, SQLite, DuckDB, or a generated registry is an implementation choice.

The S050 correction overlay should be taken seriously. DuckDB must not be penalized as experimental, and SQLite must not inherit any operator-preference weight. After that correction, the choice is less about maturity and more about distribution: every external workspace pays the dependency floor, debugging surface, and bootstrap behavior. That pushes against cleverness. It also pushes against treating MCP as the substrate. MCP is an access path; the workspace-relative index and its query contract are the substrate.

The strongest dissolving reframe is: **Selvedge may not need a search product as much as it needs a fact discipline.** The corpus is already heavily ID-structured. If each session writes durable thin rows for decisions, open issues, minorities, edges, and archive references, then a database can be rebuilt from those rows without re-interpreting prose. Full-text search remains useful, but it becomes supporting evidence rather than the foundation of methodology memory.

## 2. Candidate Additions

### Substrate-N1: Retrieval Ledger And Query Contract

This option makes retrieval activity itself a durable artefact. Each session records material retrieval queries, result sets, and unresolved queries in a structured log, for example `provenance/050-session/retrieval-log.jsonl` or a session-close section with machine-readable rows. Saved query templates define required checks: `resolve_id`, `minorities_with_possible_warrants`, `archive_path_exists`, `sync_obligations_for_spec`, and `recent_decisions_touching_id`.

On the P1 criteria: ID-crisp lookup is only as strong as the backing resolver, so this is not a standalone replacement for SQLite or DuckDB. BM25 quality is delegated. Frontmatter-filter ergonomics are good because common filters become named templates. Graph traversal is modest but auditable because traversed paths can be logged. Dependency floor is nearly zero if JSONL plus existing validation are used. MCP integration is simple: `run_saved_query`, `list_required_queries`, `record_retrieval`. Rebuild cost is negligible because the ledger is append-only. Index size is tiny. Ecosystem maturity is high at the pattern level but not as an off-the-shelf library. API stability is excellent if the log schema is owned by Selvedge.

The advantage is methodological: it measures actual query demand instead of guessing. S049 §11 admits query-class measurement is qualitative. A retrieval ledger makes that empirical by Session 055.

### Substrate-N2: Structured Artefacts Replace Prose-As-Database

This is the fundamentally different option. Decisions, OIs, minorities, watchpoints, archive citations, session summaries, and cross-spec sync obligations become structured source-of-truth records, with Markdown rendered or assembled from those records. The durable substrate is not "Markdown plus index"; it is a structured fact corpus, perhaps JSONL files under `records/` or a workspace-local SQLite database with exportable Markdown witnesses.

On the criteria: ID-crisp performance is excellent because IDs are primary keys. BM25 over prose is weaker unless rendered bodies are indexed too. Frontmatter filters become ordinary fields, not parsed metadata. Graph traversal becomes first-class if edges are records. Dependency floor can be low with JSONL plus Python stdlib, or higher if SQLite is source-of-truth. MCP integration is straightforward because the tools query facts directly. Rebuild cost is low if records are canonical. Index size is small. Maturity is conceptually strong but adoption risk is high because it changes authoring practice. API stability depends on schema governance.

This option is probably too disruptive for S050 adoption, but it is the correct counter-frame. If Selvedge expects many external workspaces, structured artefacts may eventually be simpler than repeatedly teaching agents to infer structure from prose.

### Substrate-N3: Write-Time Registries Plus Generated Read Model

This is the practical bridge. Keep Markdown as source of truth, but require close-time append or regeneration of structured registries: `identifiers.jsonl`, `edges.jsonl`, `archive_paths.jsonl`, `minorities.jsonl`, perhaps `sessions.jsonl`. The SQLite or DuckDB database is then a generated read model from registries plus Markdown FTS. This shifts work from "read-time scrape the whole corpus" to "write-time declare what changed."

On the criteria: ID-crisp lookup is excellent because registries are compact and canonical. BM25 remains available through whichever FTS backend is chosen. Frontmatter filters improve because important fields are normalized into registries. Graph traversal is good because edges are explicit. Dependency floor can stay at Python stdlib plus SQLite. MCP integration is clean: tools query the generated database but can cite registry rows. Rebuild cost is low; full rebuild remains possible. Index size is modest. Maturity is local rather than external, but API stability is high because Selvedge owns the registry schema.

This is my preferred Substrate-N shape: not "choose DuckDB or SQLite and hope extraction is right", but "make the facts explicit, then choose the smallest durable read model."

## 3. External-Application Portability Reframe

The engine-definition versus engine-adjacent versus ancillary axis is a governance axis, not a portability mechanism. The load-bearing mechanism should be: **engine-defined interface, bootstrapped implementation, workspace-local generated state.**

The engine definition should specify the retrieval contract, registry schemas, required tool names, failure behavior, and validator expectations. The implementation should live as adjacent-but-copied tooling installed by `tools/bootstrap-external-workspace.sh`, with a version marker so external workspaces know which retrieval contract they run. The generated database belongs under each workspace, for example `.cache/selvedge/retrieval.db`, and is never shared across workspaces.

This avoids two bad options. If all implementation code is engine-definition, every substrate code edit becomes methodology-version churn. If it is merely ancillary, external workspaces do not reliably inherit the capability the operator explicitly expanded scope to require. The middle path is a small engine-defined contract plus a copied library/tool bundle. Bootstrap creates `.mcp.json` from a template using workspace-relative paths, runs an initial build or marks first-use build required, and validates that `resolve_id` and `search` work locally.

## 4. Answers To Q1-Q8

**Q1 - Primary substrate choice.** I would choose Substrate-N3 as the primary shape: write-time registries plus a generated workspace-local read model, implemented initially with Substrate-1 SQLite FTS5. SQLite wins here not because it was operator-mentioned, but because external workspaces should not pay a dependency unless the gain is load-bearing. With the correction overlay, DuckDB is a legitimate mature choice and may be technically cleaner for structured filters, but the first adoption should minimize distribution risk. If S050 insists on choosing only among S049 backends, choose SQLite FTS5. If allowed to choose architecture, choose registries-plus-SQLite.

**Q2 - Adoption scope.** Adopt incrementally, but not as "FTS search only." Minimal FTS search is too easy to ignore and does not address the warrant/identifier problem. Phase 1 should include `documents`, `identifiers`, `archive_paths`, and a minimal `edges` registry, plus MCP tools for `search`, `resolve_id`, and `verify_archive_path`. Defer `warrants_currently_met` automation until there is enough structured minority data to avoid fake certainty. The first increment should prove that the substrate answers required questions, not just that BM25 works.

**Q3 - Kernel §1 amendment shape.** Kernel §1 should gain a retrieval-backed Read sub-activity, but phrase it as "required retrieval checks" rather than "call this one substrate tool." When unavailable, the session may proceed only in degraded mode: the Case Steward records substrate unavailable, runs documented lexical fallbacks for required checks, and treats any warrant or archive-path conclusion as lower confidence. Unavailability should be visible in the session record. A stale or missing index is not fatal, but silent fallback is a methodology failure.

**Q4 - Alias vocabulary.** Do not adopt full SKOS three-label vocabulary yet. Use a two-level local schema: `canonical` and `observed_aliases`, with optional fields for `kind`, `source_session`, and `notes`. `hiddenLabel` is useful in library systems, but here it risks inventing taxonomy before alias behavior is observed. The retrieval ledger can record failed lookups and near-misses; promote recurring aliases later. A compact alias file is better than a semantically rich one nobody maintains.

**Q5 - Rebuild trigger.** Use both, but make session-open mtime checking authoritative. Git post-commit hooks are helpful in self-development, but external workspaces may bootstrap, edit, or run sessions before clean commit discipline exists. At session open, if any indexed source is newer than the database or the registry schema version differs, rebuild. Post-commit rebuild is a convenience. The honest limit is simple: query results must report index timestamp and stale/fresh status, and stale results cannot support closure-critical claims without fallback verification.

**Q6 - `syncs_with:` frontmatter.** Keep `syncs_with:` as a declaration of intent, not as a replacement for extracted edges. An `edges` table tells us what references exist; `syncs_with:` tells us which documents are supposed to co-evolve. Those are different facts. The field should be sparse and meaningful, not a general citation list. Validator logic can then check whether declared sync partners were considered when one side changes. That is a maintenance obligation, not merely a graph edge.

**Q7 - External-application inheritance.** Reject ancillary-local. Use engine-defined contract plus adjacent-copied implementation. `engine-manifest.md` should enumerate the retrieval contract and required bootstrap behavior; the tooling bundle can be copied by `tools/bootstrap-external-workspace.sh` into each external workspace. Bootstrap should create workspace-local cache directories, write or update `.mcp.json`, run a smoke index, and record the retrieval tool version. This gives external applications the capability without making every implementation file part of the engine-definition surface.

**Q8 - Validator check 24 scope.** Start with preserved-minority pointer verification plus archive-path verification. Do not immediately require every prose ID reference to resolve; that will produce noise from historical prose, examples, and partial references. Instead, add a report-only unresolved-ID inventory, then promote classes to hard failures once false positives are understood. Check 24 should run in external workspaces, but distinguish inherited engine minorities from application-local minorities. Application workspaces need their own preserved-minority checks as they accumulate local provenance.

## 5. Counter-Frames For The Dominant Claude Position

If P1 and P2 converge on "SQLite FTS5 incremental adoption," the shared assumption to name is that the main decision is backend selection for a Markdown corpus. That convergence may miss the deeper question: which facts must be made explicit so retrieval answers are trustworthy? SQLite FTS5 is a good read model, but it is not a fact discipline.

If they converge on DuckDB, the shared assumption is likely that ergonomic structured querying is more important than dependency propagation. The correction overlay makes DuckDB viable, but external-application bootstrap changes the weight. A dependency that is trivial in the self-development workspace becomes part of the methodology's carried surface.

If they converge on any text-file-plus-index design, the shared blind spot is read-time extraction. They may assume the indexer can reliably infer identifiers, edges, warrants, and current states from prose indefinitely. That is exactly the scaling pressure EF-047 surfaced in another form. The alternative is to stop making the reader rediscover facts that the writer already knew at close.

A second shared assumption is that MCP is the natural access layer. MCP is useful, but Selvedge should not make methodology validity depend on a live MCP server. The substrate must have a CLI or validator path with the same semantics, because validation and bootstrap need to work outside an agent session.

A third shared assumption is that portability is solved by copying files. External workspaces need a versioned bootstrap contract: what gets installed, what is generated locally, how stale state is detected, and how a workspace upgrades when the engine evolves. Without that, S050 will have chosen a local convenience and called it a substrate.
