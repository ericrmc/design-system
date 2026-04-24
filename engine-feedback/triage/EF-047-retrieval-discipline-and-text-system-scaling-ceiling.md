---
triage_id: EF-047-retrieval-discipline-triage
feedback_ref: ../inbox/EF-047-retrieval-discipline-and-text-system-scaling-ceiling.md
triaged_in_session: 048
triaged_at: 2026-04-24
status: triaged
disposition: adoption scheduled for S050 dedicated multi-agent deliberation per operator Halt-1 scope revision at S049; design-space document produced at provenance/049-session/design-space.md as MAD input; S050 Q1–Q8 agenda covers primary substrate (Option A SQLite FTS5 vs Option B DuckDB+FTS vs defer) + adoption scope + kernel §1 amendment shape + alias vocabulary + rebuild trigger + syncs_with field + external-application inheritance + validator check 24 scope
opened_issue: null
scheduled_mad_session: 050
scheduled_mad_scope: |
  Per S049 D-157 operator-directed scope revision: the original EF-047 level (A) framing (kernel-discipline-only minor amendment) is set aside. Replaced with data-structure + retrieval-substrate direction per operator Halt-1 guidance ("recommendations should include data structure changes rather than discipline only … real scalable technical solutions"). S049 produced synthesis + options meta-decision; S050 executes the substantive MAD.
  S050 MAD menu (per design-space.md §4–§7):
    Option A — SQLite FTS5 + structured tables (documents, identifiers, frontmatter_kv, edges, aliases) + MCP server via FastMCP stdio. Operator-named direction. Zero install cost; BM25 native; snippet()/highlight() auxiliary functions; ~140ms rebuild / sub-millisecond query on this corpus.
    Option B — DuckDB + FTS extension + edges table + MCP server. Strongest competitor to Option A; table-centric model unifies frontmatter filters with prose FTS; DuckPGQ optional for property-graph queries; FTS extension flagged experimental upstream.
    Complementary: git-as-temporal-substrate (git log -S pickaxe); ripgrep-as-floor (baseline that any substrate must beat on ID-lookup); validator check 24 (preserved-minority substrate-pointer coverage); SKOS alias vocabulary at specifications/aliases.yaml.
    Rejected with rationale: Meilisearch/Typesense (typo-tolerance wrong for ID-crisp queries); Tantivy (scale mismatch); RDF stores (schema-tax disproportional); vector/embedding (ID-lookup failure; <200K-token Anthropic contextual-retrieval guidance); Neo4j/Memgraph (scale mismatch); rank_bm25/whoosh (stale/frozen).
  S050 MAD 8-question agenda per design-space §8.2: Q1 primary substrate; Q2 adoption scope (full-kit vs incremental); Q3 kernel §1 amendment shape; Q4 alias vocabulary; Q5 rebuild trigger; Q6 syncs_with: field disposition; Q7 external-application inheritance (engine-definition vs ancillary); Q8 validator check 24 scope.
  S050 convening: 4-perspective two-family per operator S044 R2 (P1 Substrate Architect Claude + P2 Incrementalist Skeptic Claude + P3 Outsider Codex/GPT-5.5 + P4 Cross-Family Reviewer Codex/GPT-5.5) per design-space §8.1.
engine_version_impact_pending: engine-v8 → engine-v9 candidate at S050 close (conditional on substantive adoption)
cross_references:
  - OI-019 sub-question (f): extended-baseline visibility mechanism
---

# Triage — EF-047 retrieval-discipline-and-text-system-scaling-ceiling

## Classification

**Target**: methodology. **Severity on inbox record**: friction. **Source**: `selvedge-self-development` Session 047, direct-to-inbox out-of-session operator observation.

**Disposition**: **triaged; adoption rescheduled to S050 dedicated multi-agent deliberation per S049 D-157 operator scope revision.** The source record is deliberately forceful and explicitly pre-empts the Skeptic/Minimalist/Pragmatist "don't overengineer" response at level (A). Per operator ratification at S048 Halt 1 Q3, S049 was originally scheduled as 4-perspective two-family MAD. At S049 Halt-1 operator delivered scope revision: recommendations should include data structure changes rather than discipline only; real scalable technical solutions; suggested five substrate candidates (inverted index + BM25; identifier alias tables; structured frontmatter metadata filters; key-value lookup for ID resolution; regex for exact patterns; local FTS5 index exposed via MCP). Operator explicitly suggested using S049 for synthesis + options + meta-decision, deferring substantive MAD deliberation to S050. S049 produced the design-space document at `provenance/049-session/design-space.md`; S050 executes the substantive 4-perspective MAD with the design-space as input.

## Why not adopted this session

Level (A) adoption is a **substantive kernel §1 amendment**, triggering MAD v4 §When Multi-Agent Deliberation Is Required. Single-orchestrator adoption would bypass the preservation-and-dissent-recording machinery that substantive kernel revisions require. The operator's pre-emption of the "don't overengineer" response is not a pre-emption of deliberation itself — it is a constraint on one possible rejection path that deliberation might otherwise land on. Deliberation at S049 may still produce dissent on the specific mechanism (which MAY/MUST/MUST NOT modals; which validator check; which spec gains the pointer) or on scope (level (A) alone vs. (A)+(B) vs. (A)+(B)+(C)).

## Scheduled S049 MAD scope

**Level (A) — Kernel §1 Warrant-evaluation sub-activity.** Minimum-viable retrieval discipline:

- **Candidate spec text**: add to `methodology-kernel.md` §1 Read (or as new §1a) a sub-activity instructing the session to scan every active specification's §5 / §10 / preserved-minority / activation-warrant section against the current session's context at session-open, recording whether any warrant's firing condition has been met.
- **Candidate validator check**: new check in `tools/validate.sh` that enumerates all preserved minorities across all active specs + all 02-decisions.md files (both default-read and archive-surface), and for each preserved minority verifies that an active-specification §5/§10 block contains a pointer to it.
- **Classification**: substantive per OI-002 heuristic (new kernel sub-activity + new validator check + new enforcement mechanism).
- **Engine-v impact**: engine-v8 → engine-v9 candidate at S049 close.

**Level (B) — Cross-spec synchronisation first-class.** Medium-scope addition:

- **Candidate spec text**: spec frontmatter gains an optional `syncs_with:` field naming specs whose coherence depends on this one; validator check cross-checks named values (e.g., `read-contract.md` §2 budget values vs. `validate.sh` constants).
- **Classification**: substantive per OI-002 (new frontmatter field + new validator check + new coherence enforcement).
- **Engine-v impact**: engine-v9 candidate at S049 close (conditional on adoption).

**Level (C) — Structured retrieval substrate.** Large-scope direction:

- **Candidate direction**: `tools/query.sh` as a dedicated query tool over markdown + frontmatter; or a SQLite-style index file (committed to git; regenerable from source) indexing every preserved minority, warrant, OI, EF-record, archive-pack, and cross-reference; or full database-backed retrieval layer with text files as canonical source-of-truth.
- **Classification**: substantial methodology-level decision. Likely multi-session design process.
- **Engine-v impact**: undetermined; S049 produces direction-of-travel decision and recommended next-session work rather than full adoption.

## Why S049 specifically

Operator-ratified at S048 Halt 1 Q3 = (i) S049 dedicated MAD. Rationale for same-session-next rather than several-sessions-later:

- Inbox-to-triage-to-adoption latency is itself the kind of asymmetry EF-047-retrieval-discipline flags. Scheduling late would be structurally ironic.
- `selvedge-disaster-response` external arc is not yet advanced (S001 has run; S002–S005 pending operator transport); retrieval-discipline adoption at engine-v9 would propagate to later external-arc sessions if adoption completes before arc end.
- §10.4-M5 activation-pending on arc-feedback-production resolves at S048 (see S048 close §10.4-M5 disposition); engine-feedback/ infrastructure is now exercised operationally, and extending its discipline layer to retrieval is the natural next increment.

## Bundled scope at S049 per operator ratification

Per S048 Halt 1 Q4 = (b) bundle with S049 MAD: **EF-047-brief-slot-template-hidden-arc-leakage** (friction; two options minor) and **EF-047-session-input-files-redundant-with-verbatim-capture** (observation; minor documentary) are bundled with the S049 retrieval-discipline MAD. Both are minor-documentary scope; they compose with the retrieval-discipline territory at the engine-feedback / external-application-workspace boundary. Bundled-minor adoption expected at S049 close alongside level (A) substantive.

## Forward observations

- **EF-047-retrieval-discipline is self-referential evidence of its own concern.** The source record names "agents cannot be told to look where indices don't point" as a failure mode; S048 triage reads preserved-minority status largely via SESSION-LOG.md summaries + INDEX.md (not via the minorities' original full activation-warrant text). The S049 MAD is itself a data point on whether the Case Steward at S049 can reliably load the EF-047-retrieval source record's claims against the full set of preserved minorities without a retrieval affordance beyond the current text-substrate — the MAD's own preparation is a meta-exercise.
- **OI-019 sub-question (f)** "extended-baseline visibility mechanism periodic-vs-triggered-vs-narrow" was opened at S043 as seed territory; EF-047-retrieval-discipline's level (B) and level (C) directions are concrete candidate mechanisms for sub-question (f). OI-019 is cross-referenced but not closed by this triage (OI closure would require the MAD to produce a specific mechanism).
- **Trajectory-level concern**: operator observation about the engine applied to "multi-year software-engineering project with 100+ sessions" is forward-looking; S049 adoption at level (A) addresses the concern at policy level but does not resolve the substrate question. That question remains open through S049 and likely beyond.

## OI impact

No OI opened by this triage. OI-019 cross-referenced; no state change. If S049 MAD closes with level (C) direction-of-travel decision, a new OI may be opened for the multi-session structured-retrieval design process; deferred to the S049 MAD.
