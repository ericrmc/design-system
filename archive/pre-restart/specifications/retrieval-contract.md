---
title: Retrieval Contract
version: 1
status: active
created: 2026-04-24
created-in-session: 050
last-updated: 2026-04-24
updated-by-session: 050
supersedes: none
---

# Retrieval Contract

## Purpose

This specification declares the retrieval capabilities that every Selvedge workspace — self-development and external-application — must expose to support agent-scale read-side operations on the workspace's markdown corpus. It fixes the **contract** (required tool names, signatures, failure behaviour, workspace-local state, and bootstrap obligations) without fixing the **implementation** (the specific SQL engine, indexer code, or MCP server binary).

This split is deliberate: the engine owns the contract; the implementation is engine-adjacent (not enumerated in `engine-manifest.md` §3). Implementations may evolve independently of the methodology's version line, and external workspaces may ship updated implementations via routine `tools/bootstrap-external-workspace.sh` refreshes without requiring engine-version churn.

Adopted Session 050 per D-170 + D-172 as resolution of `engine-feedback/inbox/EF-047-retrieval-discipline-and-text-system-scaling-ceiling.md` and subsequent Q1–Q8 MAD synthesis. First phase of a staged adoption: phase-1 scope is declared here; phase-2 extensions are gated on the WX-50-1 retrieval-substrate-use evidence window (§6 below).

## Specification

### §1 Scope and framing

The retrieval substrate is a **read model** over the workspace's canonical markdown corpus. Markdown files remain the source of truth; the substrate provides fast, structured, and prose-indexed access to them. The substrate does NOT replace, shadow, or derive authority from any active specification; where the substrate and the source disagree, the source is correct.

Three framings the contract explicitly rejects:

1. **Substrate as source of truth.** Rejected at phase-1. The P3 Substrate-N2 (structured artefacts replace prose) reframe is preserved as §7.4 below as a first-class minority; any future move in that direction is a multi-session arc requiring its own deliberation.
2. **Substrate as ceremony.** The contract does not require retrieval-tool usage for its own sake. Every required capability answers a real query class the methodology regularly exercises. The WX-50-1 gate (§6) makes phase-2 expansion earn its scope.
3. **Operator-mentioned candidates carrying deliberation weight.** Retracted per S050 00-assessment §2a. Every candidate is evaluated on technical merits; no substrate inherits prior status from operator surfacing.

### §2 Required capabilities (phase-1 contract)

At phase-1 adoption (Session 050) every Selvedge workspace MUST expose two retrieval tools and one alias file.

#### §2.1 Tool: `search`

Signature:

```
search(query: str, k: int = 10) -> list[{path: str, snippet: str, score: float}]
```

Semantics:
- Returns the top-`k` markdown files by BM25-ranked relevance to `query` over each file's title and body.
- `snippet` is a focused excerpt (~120 chars) containing the highest-scoring match window.
- `score` is the BM25 score (higher = more relevant). Absolute values are implementation-defined; relative ordering is contract.
- Tokenisation MUST treat hyphen, underscore, and `§` as word-internal so that IDs (`D-152`, `d016_2`, `§10.4-M5`) tokenise atomically rather than splitting.
- Returns an empty list if no match. Never raises on empty match.

#### §2.2 Tool: `resolve_id`

Signature:

```
resolve_id(alias: str) -> {canonical: str, kind: str, source_path: str, line: int, context: str} | None
```

Semantics:
- Returns the canonical identifier, its kind, the markdown file path where its canonical definition lives, the line number, and a ~120-char context excerpt.
- If `alias` matches a `canonical` value directly, returns that record.
- If `alias` matches an `aliases[]` entry in `specifications/aliases.yaml`, resolves to the corresponding canonical.
- If `alias` is a known identifier pattern (matches `D-NNN`, `OI-NNN`, `§N(.N)*(-MN)?`, `WX-N-N`, `engine-vN`, `EF-NNN-...`) but no canonical entry exists, returns the first occurrence found in the indexed corpus.
- If no resolution is possible, returns `None`. Never raises on unknown alias.

#### §2.3 File: `specifications/aliases.yaml`

Two-label schema with versioned top-level shape:

```yaml
schema_version: 1
aliases:
  - canonical: <canonical-id-string>
    kind: <minority | decision | open-issue | watchpoint | session | engine-version | feedback | trigger | other>
    aliases: [<alias-string>, ...]
    # optional:
    added_session: <NNN>
    last_seen_session: <NNN>
    notes: <str>
```

Starts with ≥3 seed entries at S050 close (see `specifications/aliases.yaml`); populated incrementally as aliases are identified in subsequent sessions.

Phase-3+ may upgrade to SKOS three-label (`prefLabel` / `altLabel` / `hiddenLabel`). The `schema_version` field is the migration gate: bump to 2 at that point.

### §3 Required failure behaviour

An implementation conforming to this contract MUST:

1. **Report availability.** If the substrate's storage or server is unavailable, tool calls MUST return a structured error with `{available: false, reason: str}` rather than timing out silently.
2. **Report index freshness.** Tool responses MUST include the index's mtime (or an equivalent freshness marker). Stale-index results MUST be distinguishable from fresh-index results.
3. **Surface degraded mode.** If an implementation operates in a degraded mode (e.g., missing aliases file, missing identifiers table), tool responses MUST carry `{degraded: true, missing: [str]}`.
4. **Refuse silent fallback.** Silent drop-back to lexical tools (grep, ripgrep) without a surfaced error is a contract violation. A session operating under such silent fallback cannot claim substrate-backed retrieval in its provenance.

A session whose retrieval substrate is unavailable MAY proceed under prose-scan fallback. When it does, its `03-close.md` honest-limits section MUST record the substrate unavailability and the scope of fallback.

### §4 Workspace-local state

- The retrieval index lives at `.cache/retrieval.db` (workspace-local; gitignored).
- A workspace's substrate queries only that workspace's corpus. Cross-workspace queries are out of scope at phase-1.
- The workspace-local path is relative to the workspace root. An implementation MAY relocate the cache via a per-workspace config file in phase-2+; phase-1 path is fixed.
- Rebuild trigger: session-open mtime check (MCP server compares `max(*.md mtime) > retrieval.db mtime` at startup; rebuilds if stale). No git post-commit hook at phase-1 per D-168.

### §5 Bootstrap contract for external-application workspaces

When `tools/bootstrap-external-workspace.sh` initialises a new external-application workspace (per `engine-manifest.md` §6), it MUST additionally:

1. Copy the engine-adjacent implementation files from the source self-dev workspace:
   - `tools/build_retrieval_index.py` (carries PEP 723 inline metadata declaring `pyyaml` dependency)
   - `tools/retrieval_server.py` (carries PEP 723 inline metadata declaring `mcp[cli]` + `pyyaml` dependencies)
   - `specifications/aliases.yaml` (scaffold with `schema_version: 1` + empty `aliases: []`; workspace-local aliases accumulate fresh in the external workspace)
   - `.mcp.json` (template; see §5.1 below for the required shape)
2. Print operator instructions for runtime install:
   ```
   # Ensure uv is installed (https://github.com/astral-sh/uv).
   # The substrate scripts carry PEP 723 inline metadata; uv resolves
   # dependencies automatically per `uv run`. No pip+venv setup required.
   ```
3. Build the initial index via `uv run tools/build_retrieval_index.py` (may be no-op on empty workspace).
4. Validate that `search` and `resolve_id` work against the bootstrapped workspace via a smoke-test (e.g., `search("brief")` returns at least the workspace's `applications/001-<slug>/brief.md` once the brief is populated).

The bootstrap contract does NOT require:
- Git hooks installation.
- An MCP server auto-launch.
- Any network access (beyond uv's first-run dependency resolution; subsequent runs use cached deps).

#### §5.1 `.mcp.json` template shape

Every workspace's `.mcp.json` that implements this contract declares a `selvedge-retrieval` server entry of shape:

```json
{
  "mcpServers": {
    "selvedge-retrieval": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "tools/retrieval_server.py"],
      "env": {}
    }
  }
}
```

`.mcp.json` is committed to the workspace's git. Claude Code picks it up at project scope. The `uv run` invocation resolves `tools/retrieval_server.py`'s PEP 723 inline-metadata dependencies (`mcp[cli]` + `pyyaml`) on first run and caches them for subsequent invocations. Per S059 D-210 minor amendment from prior `command: "python3"` shape (resolves S051-S058 MCP stdio transport unverified honest-limit chain by aligning runtime with operator standing instruction in CLAUDE.md §Tools).

### §6 Phase-2 gate (WX-50-1 retrieval-substrate-use recording)

Every session close from S050 through S053 inclusive records retrieval substrate use in a `## Retrieval substrate use (WX-50-1)` section with three fields:

- `tool_calls_by_type`: counts of `search` and `resolve_id` invocations in the session.
- `results_used_with_artefact_id`: list of `{tool, query, returned_artefact_path, used_in_decision_or_oi_or_minority_id}`.
- `fallbacks_due_to_missing_capability`: list of `{query_intent, why_phase_1_did_not_suffice}`.

**Phase-2 fires** iff any of:
- ≥2 sessions in S050–S053 record ≥1 entry in `results_used_with_artefact_id`.
- ≥1 session in S050–S053 records ≥1 entry in `fallbacks_due_to_missing_capability` where the missing capability is structured-filter (frontmatter_kv) or graph-traversal (edges/traverse).
- ≥1 external-workspace adoption records ≥1 useful domain-context query.

**If phase-2 fires**, a dedicated MAD session adopts (selectively, not automatically all):
- `edges` table + `traverse` MCP tool.
- `frontmatter_kv` table + `list_identifiers` MCP tool.
- `warrants_currently_met` MCP tool.
- `verify_archive_path` MCP tool.
- Soft kernel §1a Warrant-evaluation sub-activity amendment to `methodology-kernel.md` (tool-optional; prose-scan fallback retained).
- Validator check 24 (preserved-minority substrate-pointer coverage + archive-path verification; skip-if-substrate-absent).
- Re-examination of Q6 `syncs_with:` field question with §7.5 distinction preserved.

**If phase-2 does NOT fire** in S050–S053, phase-1 is paused (not deprecated); the §7.1 minority's activation warrant evaluates next.

Phase-3+ extensions (SKOS three-label alias vocabulary; post-commit git hook; engine-manifest §3 promotion of implementation files; DuckDB-structured-first substrate pivot per §7.2 minority; Substrate-N2 structured-artefacts-as-source-of-truth per §7.4 minority) require their own dedicated MADs at that time.

### §7 Preserved first-class minorities (Session 050 retrieval-substrate MAD)

Five first-class minorities preserved from the S050 MAD per `multi-agent-deliberation.md` v4 §Preserve dissent. Engine-wide minority count at S050 close: **36** (31 at open + 5 new). Minority-index authoritative cross-reference lives in `specifications/workspace-structure.md` v6 §10.4-M7 through §10.4-M11; this §7 block duplicates the activation-warrant language for retrieval-contract-local readability and is kept in sync at the same schema version.

#### §7.1 P2 minimum-adoption / defer-with-instrumentation

**Position**: adoption should earn expansion through measured use, not anticipated architecture. If phase-1 proves unused, phase-1 should not have shipped.

**Source**: `provenance/050-session/01b-perspective-incrementalist-skeptic.md` §1.3.

**Activation warrant**: if the WX-50-1 gate fails to fire across S050–S053 AND zero use recorded for phase-1 tools in ≥3 consecutive sessions, revisit whether phase-1 should have shipped at all.

**Reopen warrants**: (a) WX-50-1 non-firing + zero-use across 3+ consecutive sessions — revisit phase-1 adoption; (b) phase-1 tool maintenance becomes operationally burdensome relative to evidence of value.

#### §7.2 DuckDB structured-first substrate

**Position**: if structured filters and graph traversal prove dominant, SQLite FTS5 may be the wrong long-term substrate despite winning phase-1.

**Source**: `provenance/050-session/01a-perspective-substrate-architect.md` §1.2 + §2 counter-frames; `01d-perspective-cross-family-reviewer.md` §7 dissent-rec 2.

**Activation warrant**: any session in which phase-1 tool use shows structured-filter + graph-traversal queries dominate prose-search queries by ≥3× count over a 5-session window.

**Reopen warrants**: (a) query-class data demonstrates structured-first dominance; (b) SQLite FTS5 ecosystem churn that DuckDB-FTS does not share.

#### §7.3 P1 engine-definition-at-adoption

**Position**: the capability is important enough that it warrants engine-definition classification now, not deferred. The current contract adopts engine-adjacent per D-170; this minority preserves the opposite for evidence-triggered reconsideration.

**Source**: `provenance/050-session/01a-perspective-substrate-architect.md` §4.1; `01d-perspective-cross-family-reviewer.md` §7 dissent-rec 3.

**Activation warrant**: if an external-workspace adoption exposes inconsistent inheritance (workspace A and workspace B have divergent substrate implementations producing different answers on equivalent queries), re-enter the engine-definition case.

**Reopen warrants**: (a) inconsistent-inheritance signal; (b) ≥3 stable substrate versions + ≥1 successful external-workspace adoption + operator surfacing promotion.

#### §7.4 Substrate-N2 structured-artefacts-as-source-of-truth reframe

**Position**: the shared markdown-plus-index frame should not be mistaken for the only scalable answer. Decisions, OIs, minorities, watchpoints, etc. may eventually become structured records with markdown as witness.

**Source**: `provenance/050-session/01c-perspective-outsider-frame-completion.md` §2 Substrate-N2.

**Activation warrant**: if substrate phase-2+ maintenance cost exceeds projections by ≥2× OR multi-hop cross-reference queries become the dominant operational burden, revisit Substrate-N2 as a multi-session arc.

**Reopen warrants**: (a) cumulative phase-2+ maintenance time exceeds projection 2× across 3 consecutive sessions; (b) multi-hop cross-reference query class dominates ≥5× prose-search over a 5-session window.

#### §7.5 `syncs_with:` declaration-of-intent distinction

**Position**: extracted edges may not replace explicit co-evolution commitments. Edges answer "what is cited"; `syncs_with:` would answer "what must co-evolve." The distinction is load-bearing; phase-2 deliberation on edges MUST explicitly deliberate whether to preserve or fold `syncs_with:`.

**Source**: `provenance/050-session/01c-perspective-outsider-frame-completion.md` Q6; `01d-perspective-cross-family-reviewer.md` §7 dissent-rec 5.

**Activation warrant**: at phase-2 deliberation on the `edges` table, the fold-vs-preserve question on `syncs_with:` is explicitly on the agenda; auto-fold is not permitted.

**Reopen warrants**: (a) cross-spec drift that an `edges` table did not catch; (b) declared co-evolution relationships that are not citation-observable.

### §8 Versioning

This specification is at **v1**. Version bumps follow the standard spec-revision discipline in `workspace-structure.md`:

- **v1 → v2**: phase-2 adoption (see §6 above). Adds required tools `traverse`, `list_identifiers`, `warrants_currently_met`, `verify_archive_path`; adds `edges` table + `frontmatter_kv` table; adds check 24; adds kernel §1a amendment.
- **v2 → v3**: phase-3+ adoption. May include SKOS alias migration, engine-definition promotion of implementation files, DuckDB pivot per §7.2, post-commit hook adoption, or substrate-N2 arc entry.

Each phase transition is a MAD-required substantive revision per `multi-agent-deliberation.md` v4 §When Multi-Agent Deliberation Is Required.

## Validation

To validate this specification:

1. Confirm `specifications/aliases.yaml` exists with `schema_version: 1` frontmatter.
2. Confirm `.mcp.json` at workspace root declares the `selvedge-retrieval` server per §5.1.
3. Confirm `tools/build_retrieval_index.py` and `tools/retrieval_server.py` exist (engine-adjacent; not required to be byte-identical across workspaces, but must exist).
4. Confirm `.cache/retrieval.db` is gitignored (either via explicit `.cache/` or `.cache/retrieval.db` line in `.gitignore`).
5. If the MCP server is available in the agent's execution context, confirm `search(query="retrieval contract", k=1)` returns a result pointing to this file.
6. Confirm `resolve_id("§10.4-M5")` returns a record pointing to `specifications/workspace-structure.md` (if a seed alias is present) — per §2.2 semantics, unresolved aliases return `None` rather than raising.

Validator check 24 is deferred to phase-2 per §6; this §9 section is adequate at phase-1.

### §10 Honest limits

- **Query-class measurement is qualitative at adoption.** The `01-deliberation.md §2` and `design-space.md §11` acknowledge that no quantitative actual-query-class frequency measurement exists for this workspace. The WX-50-1 gate (§6) fills this gap by making phase-1 use empirical.
- **Substrate implementation is engine-adjacent, not engine-definition.** External-workspace inheritance depends on `tools/bootstrap-external-workspace.sh` copying the implementation at bootstrap. Once bootstrapped, an external workspace's implementation is frozen to that point in time unless the operator re-runs bootstrap or manually updates. This is the known promotion question preserved as §7.3.
- **MCP API stability is uncertain over 2–5 year horizon.** FastMCP and the Anthropic Python SDK are under active development. Implementations MUST keep the tool surface small and standard (`search`, `resolve_id`) so that MCP API evolution can be accommodated with minor implementation edits.
- **Silent-fallback risk in practice.** §3 declares silent fallback a contract violation, but implementations may develop silent-fallback surfaces in specific error modes that have not been anticipated. The WX-50-1 `fallbacks_due_to_missing_capability` field surfaces this.
- **Aliases file is authoritative only for listed aliases.** For unlisted identifiers the `resolve_id` tool returns the first occurrence found; this is best-effort and may be non-authoritative for ambiguous identifiers. Alias hygiene grows incrementally; do not treat phase-1 `aliases.yaml` coverage as complete.
- **External-workspace portability tax is reduced but persistent.** Every external-application workspace pays a single-tool `uv` prerequisite at bootstrap (the substrate scripts carry PEP 723 inline metadata so uv resolves `mcp[cli]` + `pyyaml` automatically per `uv run`; no separate pip-install step or per-workspace venv to manage). This is materially less burdensome than the pre-S059 `pip install 'mcp[cli]' pyyaml` two-package install path, but is a real constraint on the methodology's reach into environments without Python or uv; the §7.4 Substrate-N2 minority preserves the broader reframe.
- **No cross-workspace query composition.** A self-dev workspace's substrate cannot answer questions about an external-application's corpus, and vice versa. If cross-workspace queries become needed (e.g., "show every preserved minority across all Selvedge workspaces the operator runs"), that is a future contract-revision question.
