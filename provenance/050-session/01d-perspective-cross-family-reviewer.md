---
title: Perspective — P4 Cross-Family Reviewer / Laundering Audit (Session 050)
session: 050
perspective: cross-family-reviewer
perspective_family: codex-gpt-5.5
perspective_role: cross-family-reviewer
date: 2026-04-24
status: immutable-at-commit
provenance_note: verbatim from codex exec --sandbox read-only -o output; raw log at codex-cross-family-reviewer-raw-output.log; model gpt-5.5 reasoning-effort xhigh per ~/.codex/config.toml; Case Steward wrapped with frontmatter only (no body edits)
---

# P4 — Cross-Family Reviewer / Laundering Audit

## 1. Laundering-Audit of P1

P1 largely satisfies the anti-laundering requirement to list strained criteria, not only wins. The candidate survey explicitly marks SQLite FTS5 as strained on "frontmatter-filter ergonomics" and "graph traversal ergonomics"; DuckDB as strained on snippet/highlight ergonomics, extension API stability, and MCP ecosystem maturity; tantivy-py as failed on structured filters, graph traversal, dependency floor, and binding stability; Whoosh-Reloaded as failed or strained on graph traversal, maturity, and API stability. This is a real audit-positive feature: P1 does not present Substrate-1 as cleanly dominant.

The risk is subtler: P1's final recommendation turns the strained SQLite criteria into "one-time write costs" hidden behind MCP tools. That may be true, but it is also the move by which the dominant structured-query burden disappears from the decision calculus. If structured-filter and graph-traversal queries are actually the load-bearing class, then hiding SQLite's awkwardness behind `tools/retrieval_server.py` does not eliminate the cost; it relocates it into code the methodology must maintain for years. P1 acknowledges the cost but then discounts it without measured query-class data.

Revision traceability is present but uneven. P1 records that it reconsidered whether DuckDB's frontmatter advantage should tip the decision, and later records rejecting a per-workspace retrieval config file. It also revises the design-space tokenizer from `tokenchars '-_'` to include `§`. These are good trace points. The problem is that P1's own adoption scope is internally unstable. The architecture section proposes the full schema, `traverse`, `warrants_currently_met`, file-plan edits to `methodology-kernel.md`, `engine-manifest.md`, `validation-approach.md`, `validate.sh`, and `read-contract.md`. But Q2 later says phase 1 is only `documents` + `identifiers` + `docs_fts` plus `search`, `resolve_id`, and `list_identifiers`; phase 2 adds edges/frontmatter and `traverse`/`warrants_currently_met`; phase 3 adds validator check 24 and kernel amendment. Q3 then again says "Add §1a Warrant-evaluation." This is the highest laundering risk in P1: a full-kit surface is partly preserved while the answer labels itself phased.

Cross-session precedent coverage is strong. P1 explicitly cites S046 D-142, S048 D-153, S049 design-space, and OI-017. It also applies the S050 correction overlay by retracting operator-preference weighting and DuckDB-experimental framing. The precedent usage is not neutral, though. P1 distinguishes away S046 D-142 to justify engine-definition classification, arguing the bootstrap script is ancillary but the installed retrieval substrate is engine-definition. That is coherent, but it is a contested use of the precedent, not a settled consequence of it.

P1's measurable criteria are mixed. Concrete criteria include rebuild p95 ≤500ms across 10 rebuilds by S053, invocation thresholds by S055, external-bootstrap smoke-test success, and check-24 coverage. Weaker criteria include "failure surface has been reduced session-over-session," "used at least 10 times … without friction," and FTS5 API churn tracked through release notes. The API-churn criterion is explicitly admitted soft. The invocation criteria also conflict: Q2 says 10 uses in a non-MAD session; §7 says 15 uses across five sessions. P1 meets the measurable-criteria bar in places, but the criteria need normalization before adoption.

## 2. Laundering-Audit of P2

P2 does not merely critique. It gives a positive path: Substrate-1 SQLite FTS5, phase 1 only, with one regular FTS table, two MCP tools, two-label aliases, workspace-relative `.cache/`, lazy rebuild, and engine-adjacent bootstrap. It also gives a serious defer case with falsifying conditions F1–F4. That is audit-positive: P2 names what would force adoption rather than treating skepticism as unfalsifiable posture.

P2 engages the design-space architecture on its merits. It rejects the five-table design, not because tables are bad, but because unmeasured query classes do not justify the maintenance surface. It identifies what phase 1 fails to do: no graph traversal, no frontmatter filters, no `warrants_currently_met`, no kernel amendment, no SKOS vocabulary, no validator check 24. It then states why those failures are acceptable for 6–12 months. That is the right form of incremental argument.

The main laundering risk in P2 is the phrase "the operator framing closes" defer. The shared brief explicitly says defer-and-stay-lexical-tools-only is respectable for P2 to argue. P2 does argue it, but then partly launders adoption through presumed operator intent. The stronger P2 position would be: "defer is evidence-valid, but if the MAD decides adoption now, phase 1 must be minimal." P2 mostly lands there, but the operator-framing language muddies the falsifiability of the defer case.

P2's minimal design also has a small technical under-specification. It proposes `resolve_id(alias) -> {canonical, source_path}` while rejecting an identifiers table in phase 1. That can work only if `aliases.yaml` carries source paths, or if `resolve_id` performs a live lookup into FTS/file text, or if a minimal identifier index exists despite being excluded. The phase-1 shape should not smuggle an identifiers table under the name "alias resolver."

P2's criteria are generally stronger than P1's. F1–F4 are concrete harm conditions; P2-a/b/c are concrete phase-2 gates; the smoke tests are operational. Some remain self-report dependent, especially "materially changed a synthesis decision" and "would have missed." Those become measurable only if session-close records include the exact query, returned artefact, and decision/open-issue/minority affected.

## 3. Convergence-Check

P1 and P2 converge on SQLite FTS5 as the primary substrate. The strongest counter-frame is DuckDB-as-structured-first: the S050 correction removes the "experimental" penalty, and if structured filters plus graph traversal are genuinely dominant, DuckDB's unified typed model may reduce long-term maintenance more than SQLite reduces dependency floor. Both P1 and P2 mention DuckDB, but neither can settle the query-class question because the design-space §11 admits it is unmeasured.

They converge on markdown remaining canonical with a derived local index. The strongest counter-frame is source-of-truth restructuring: decisions, open issues, minorities, warrants, and references become structured records first, with markdown generated as a human-readable witness. Both Claude perspectives treat that as too disruptive; neither gives it a full adoption-path analysis.

They converge on MCP as the exposure layer. The strongest counter-frame is a stable CLI/library substrate with MCP as an adapter. MCP API stability is explicitly an honest limit in the shared brief, yet both P1 and P2 make MCP central from phase 1.

They converge that external workspaces should carry workspace-local indexes. The strongest counter-frame is versioned distribution: a package, template repo, or pinned tool version installed by bootstrap, rather than byte-copying evolving files or classifying them as engine-definition.

They mostly converge on deferring `syncs_with:` and broad validator scope. The strongest counter-frame is that `syncs_with:` is not redundant with extracted edges: it declares intended co-evolution where no citation may yet exist. If cross-spec drift is the failure mode, waiting for an edges table may delay the one field that would expose intent.

They diverge on adoption scope, kernel timing, alias vocabulary, rebuild trigger, portability classification, and validator timing. P1 leans larger, engine-definition, SKOS, both rebuild triggers, and kernel coupling. P2 leans minimal, engine-adjacent, two-label, lazy rebuild, and advisory tooling until evidence accumulates.

## 4. Shared-Frame-Blindness Assessment

The shared frame is: "plain markdown remains canonical; a local Python-built index sits underneath; FastMCP exposes query tools; external workspaces receive the same mechanics through bootstrap; each workspace indexes itself in isolation." This frame is reasonable, but it is still a frame.

The blind spots are: structured artefacts as source of truth; query-log instrumentation before architecture; versioned package distribution instead of copied tool files; a CLI-first retrieval contract with MCP as replaceable adapter; and domain-specific external-workspace ID patterns that may not fit the self-development regex registry. P2 names some alternatives, especially query-log instrumentation and structured artefacts, but treats them as fallback or rejection rather than as coequal designs.

## 5. Answers to Q1–Q8

**Q1 — Primary substrate choice.** I would accept SQLite FTS5 only as a provisional phase-1 substrate, not as a fully laundered final answer. P1 and P2 convergence is meaningful because SQLite has maturity, inspectability, snippets, and a low database dependency floor. But the convergence is not decisive proof: DuckDB remains the strongest minority substrate if structured frontmatter and graph traversal become dominant. The final decision should preserve that counter-frame and require measured query evidence before foreclosing DuckDB.

**Q2 — Adoption scope.** P2's phase-1 minimum is the safer adoption shape. Ship `search` and a clearly specified `resolve_id`; do not silently adopt P1's larger table/tool surface under phased language. If `resolve_id` requires an identifiers table, name that table explicitly and keep it minimal. Edges, frontmatter filters, `warrants_currently_met`, validator check 24, and kernel amendment should require phase gates.

**Q3 — Kernel §1 amendment shape.** Do not make a hard kernel amendment in phase 1. A kernel rule that depends on an unproven MCP server creates a methodology/tool coupling before operational evidence exists. If amended later, it should be soft: call `warrants_currently_met()` if available; otherwise perform prose-scan warrant evaluation and record the fallback in honest limits.

**Q4 — Alias vocabulary.** Use two-label vocabulary first: canonical plus aliases. P1's SKOS three-label model is tidy, but premature. `hiddenLabel` becomes useful only after enough historical/misspelled aliases accumulate to need different treatment. The migration path from two-label to SKOS is straightforward if the YAML schema is versioned.

**Q5 — Rebuild trigger.** Prefer session-open mtime check, optionally repeated on tool call if cheap. Do not adopt post-commit hooks in phase 1. Hooks are invisible state, poorly portable across fresh clones and external workspaces, and awkward to guarantee through bootstrap. P1's "both" is robust locally but increases operational surface before need is shown.

**Q6 — Cross-spec `syncs_with:` frontmatter field.** Defer the field, but preserve the distinction. Extracted edges answer "what is cited"; `syncs_with:` answers "what must co-evolve." Those are not the same. If future sessions record cross-spec drift that edges did not catch, `syncs_with:` should be reconsidered as declaration-of-intent, not as a duplicate of graph extraction.

**Q7 — External-application inheritance.** Choose engine-adjacent tooling for now, installed by `tools/bootstrap-external-workspace.sh`, with workspace-relative `.cache/retrieval.db`. P1's engine-definition argument becomes stronger only after the substrate is stable and kernel-load-bearing. Before that, engine-definition classification risks propagating substrate churn into every external application. Promotion should require multiple stable sessions and at least one successful external-workspace use.

**Q8 — Validator check 24 scope.** Defer check 24 until the substrate has the identifiers needed to support it. When added, scope it narrowly to preserved-minority pointer coverage and source archive-path existence. It should skip cleanly if the substrate is absent during advisory phase, and fail only once the substrate is declared required. Do not extend initially to every `[archive: path]` or every prose ID reference; that invites noisy false positives.

## 6. Measurable Adoption Criteria Recommendation

Criteria that meet the concrete-measurable bar: rebuild latency ≤500ms p95 across a named number of rebuilds; index size ≤20 MiB at current scale; smoke queries returning named expected records; external-bootstrap smoke-test success; check-24 100% coverage once check 24 exists; and P2's F-incr-1 if session closes record exact missing query type.

Criteria that are weak or aspirational: "without friction," "materially changed synthesis" without a recorded artefact ID, "failure surface reduced," "track release notes," and raw invocation count alone. Invocation count can measure use, not value.

Recommended normalized gate: through S053, every session close records retrieval use in three fields: tool calls by type; result used with artefact ID; fallback because missing capability. Phase 2 fires only if two sessions record useful substrate results, one session records phase-1 insufficiency on a structured/graph query, or an external workspace records a useful domain query. Otherwise pause expansion, not necessarily deprecate.

## 7. Dissent-Preservation Recommendation

Preserve these as first-class minorities if they lose synthesis:

1. **P2 minimum-adoption / defer-with-instrumentation**: adoption should earn expansion through measured use, not anticipated architecture.

2. **DuckDB structured-first substrate**: if structured filters and graph traversal prove dominant, SQLite may be the wrong long-term substrate despite winning phase 1.

3. **Engine-adjacent before engine-definition**: portability can be load-bearing without making unstable retrieval code part of the engine-definition file set.

4. **Structured artefacts as source-of-truth reframe**: the shared markdown-plus-index frame should not be mistaken for the only scalable answer.

5. **`syncs_with:` as declaration-of-intent**: extracted edges may not replace explicit co-evolution commitments.
