---
session: 089
title: issues-export-and-orient-mad — deliberation
generated_by: selvedge export
---

# Deliberation

## D-5 — Issue↔work_item linkage and selvedge orient/schema CLI tooling

sealed_at: 2026-04-27T19:23:21.436Z

### P-1 (anthropic)

**Position.** Ship the smallest schema that closes the loop: widen work_items.kind, attach issue_id directly, retire dead enum members; no join table, no mirror columns.

**schema_sketch.**
- A1: Single column on work_items: issue_id INTEGER REFERENCES issues(issue_id), nullable. 2-3 work_items per issue is many-to-one; join tables are for M:N or edge metadata.
- A1 cont: Refuse work_item_count cache column on issues; dispatcher answers needs work_items via LEFT JOIN where w.work_item_id IS NULL. One query, no triggers, no cache.
- A2: Issue without work_items is a real, useful state — documented but not yet decomposed. Discriminator is the LEFT JOIN; in flight is EXISTS work_item with issue_id and status in (queued,leased).
- A2 cont: Do not model a fourth status on issues; it is derivable. Avoid redundant denormalised state.
- A3: Coordinate via a derived view, not triggers. Triggers auto-flipping issues.status from work_item leases create cross-table state machines fighting T-09-style invariants.
- A3 cont: Closing the last open work_item must NOT auto-resolve the issue. Resolution is a deliberate act with an issue_dispositions row. Refuse silent state change.
- A4: Widen the kind enum. Add issue_resolution as a kind value. The original specify/decide/deliberate/review/other taxonomy was speculative engine-v17 vocabulary that never carried traffic.
- A5: Keep work_items.session_id NOT NULL; rename semantics in spec to creating session. Cross-session leasing already supported via leased_by/leased_at/completed_at separate from session_id.
- A5 cont: Do not add leased_in_session_id column until a query needs it; agent_runs.work_item_id already records who-ran-what-when.
**cli_surface.**
- B1: orient prints Markdown to stdout by default. Consumer is an LLM context window; Markdown is native. JSON is a --format json flag for the day a non-LLM tool needs it.
- B2: orient sections in order: workspace metadata, current engine version, last 3 close_records with full next_session_should lists, open issues by priority with linkage status.
- B2 cont: also in-flight work_items, active spec_versions, deferred decisions (decisions_v2 with outcome_type=defer), and open review_findings at medium severity or higher.
- B2 final: Drop recent sessions as its own section — redundant with close_records.
- B3: Stdout only. Refuse .orient.md materialisation. A materialised file drifts the moment substrate changes; redirect is the operators call, not the tools.
- B4: Truncate with hard caps and --full escape hatch. Last 3 close_records, top 30 open issues by priority then recency, all in-flight work_items, all deferred decisions.
- B5: Replace the First, orient via the substrate section in PROMPT.md with a single line: Run bin/selvedge orient. Lands as the prompt-development.md engine-v23 manifest entry.
- C1: schema is live derivation from sqlite_master, formatted table-by-table with columns, types, CHECK enums broken out as bullets, triggers grouped under their table. --raw flag for DDL.
- C2: selvedge schema issues returns the formatted view including a status admits line extracted from the CHECK constraint via regex over sqlite_master.sql. Refuse hand-curated enum registry that drifts.
- C3: Live introspection always; zero snapshot. Migrations are source of truth; sqlite_master reflects them after selvedge migrate. Versioned snapshots are exactly the drift hazard that killed markdown OIs.
**what_not.**
- Cut: (1) join table issue_work_items — cardinality does not justify it. (2) .orient.md materialisation — drift hazard with no upside. (3) auto-flipping issues.status from work_item state changes.
**risk.**
- Risk: widened kind enum becomes a dumping ground. Mitigation: migration adds NOT NULL CHECK that kind=issue_resolution IFF issue_id IS NOT NULL. Bidirectional invariant; refuse drift.
- Risk: orient output exceeds context budget on busy workspaces. Mitigation: hard truncation caps in code with N more issues elided footer per truncated section. Never silently drop.
- Risk: schema regex parser misreads multi-line CHECK constraints. Mitigation: parser is best-effort; on parse failure falls through to raw CHECK text rather than asserting an enum list.

### P-2 (openai)

**Position.** JSON-first execution linkage over precedent: many-to-many issue_work_items join table, JSON-default orient, formatted JSON schema CLI, session_id rename to creating session.

**schema_sketch.**
- A1: Use issue_work_items, a many-to-many join table. One work item can resolve several issues; one issue can require several work items. Migration-bundling is the realistic case.
- A1 cont: Columns: issue_id, work_item_id, relation, created_session_id, created_at, with unique (issue_id, work_item_id) constraint. Do not add work_items.issue_id; it fails realistic migration-bundling case.
- A2: Issue-without-work-items is a real state — documented but not yet operationalised. Dispatcher rollup: no linked nonterminal items means needs_work_item; queued/leased means in_flight.
- A2 cont: All linked items completed while issue still open means needs_disposition. State derived from rollup, not stored on issues table.
- A3: Do not auto-flip issues.status from work_items.status. Issue status is editorial lifecycle; work item status is execution state. Keep issue transitions explicit through issue_dispositions.
- A3 cont: orient should expose derived execution state, but triggers must not silently mark issues in_progress or resolved.
- A4: Widen work_items.kind with issue_resolution. Reusing specify/decide/deliberate/review/other would preserve precedent while destroying meaning. Detailed type belongs in payload_json.
- A5: work_items.session_id becomes creating session, effectively created_session_id. Add nullable leased_session_id, completed_session_id, and maybe failed_session_id.
- A5 cont: Rewrite T-11 so a session can close after creating queued future work. Block only work actively leased or failed by the closing session, not future queue carry.
**cli_surface.**
- B1: selvedge orient returns JSON by default. Agents parse keys and arrays better than Markdown headers. Add --format markdown later for humans, but default must be deterministic JSON with stable section names.
- B2: Include workspace metadata, current engine version, current/open session, last five close summaries, prior session next_session_should, active specs, open issues with linkage rollups.
- B2 cont: also queued/leased/failed work items, deferred decisions, open validation debt, unresolved medium-plus review findings, unapplied migrations.
- B2 final: Drop full issue bodies and full spec prose; orient is a navigation and dispatch packet, not an archive.
- B3: Print to stdout only by default. Add --write path for reproducible packets, preferably .orient.json, but never auto-materialise a tracked file.
- B3 cont: Generated orientation files go stale fast; reproducibility should come from rerunning a deterministic command against a named database state.
- B4: Bound output. Defaults: last five sessions, top thirty open issues by priority/status/age, all in-flight work items up to one hundred, all prior-session next_session_should, active spec metadata only.
- B4 cont: Every truncated section must include total_count, returned_count, and the SQL/query hint needed to fetch the rest.
- B5: Replace current PROMPT orientation instructions with run bin/selvedge orient --pretty first. Keep short fallback saying agents may query directly only when orient is missing or insufficient.
- C1: selvedge schema returns a formatted JSON schema summary, table by table: columns, types, nullability, primary keys, foreign keys, indexes, triggers, parsed CHECK enums, atom-type length tiers.
- C2: selvedge schema issues must answer enum questions directly and include the raw constraint for audit. For issues.status emit open, in_progress, blocked, resolved, superseded plus source SQL fragment.
- C3: Must introspect the live SQLite database, so new migrations appear automatically. Versioned dump is an export mode, not source of truth. Schema CLI should report migration head and database path.
**what_not.**
- Cut: issues.work_item_count, issues.has_work_items, and work_items.issue_id; all are lossy caches or wrong cardinality.
- Cut Markdown-first orient; that repeats the old agents-parse-prose failure mode. Cut automatic issue status transitions from work item events; they erase the human disposition record.
**risk.**
- Risk: join table can become ceremonial if the CLI does not make linking easy at work-item creation time.
- Risk: T-11 can keep blocking queue carry if session_id semantics are not changed decisively.
- Risk: orient can become another giant context dump unless every section has caps, counts, and follow-up query handles.

### P-3 (anthropic)

**Position.** Schema-strict, state-machine-enforced linkage: join table with lifecycle metadata, widened kind enum, trigger-level refusal of orphans and silent state coupling.

**schema_sketch.**
- A1: Join table issue_work_items with columns issue_id, work_item_id, created_at, completed_at, ordinal is the only defensible shape. A simple FK on work_items.issue_id loses per-linkage lifecycle events.
- A1 cont: Operators pattern of one issue bundled into 2-3 work_items maps directly to N:M relationships that close-records and reuse scenarios will require.
- A2: Issue without work_items is a real state — documented, filed, acknowledged, but not yet decomposed. Three states: pending decomposition, decomposed in flight, decomposed complete.
- A2 cont: Add column decomposition_status on issues (enum: not_decomposed, decomposed_in_flight, decomposed_complete) with a CHECK constraint enforcing the invariant.
- A3: No auto-flip; explicit disposition. issues.status and work_items.status are orthogonal. Issue does not auto-flip to in_progress when a work_item leases — operator dispatch logic drives the flip.
- A3 cont: Store explicit dispositions in issue_dispositions making the causal chain auditable. Refusal of silent state-machine coupling is substrate-canonical discipline.
- A4: work_items.kind enum must widen. Existing enum (specify/decide/deliberate/review/other) describes session phases not issue-resolution work.
- A4 cont: Add new enum work_item_resolution_kind with issue-specific values like diagnose, patch_skeleton, implement_core, test_integration, documentation, review_for_merge.
- A5: Rename session_id to created_in_session_id. Add first_leased_in_session_id, completed_in_session_id to the issue_work_items join table.
- A5 cont: A work_item can be created in S091, leased in S092, completed in S093, with each sessions context preserved in the linkage.
**cli_surface.**
- B1: Markdown by default, JSON on flag. Default to concatenated Markdown — agent-readable, git-diff-able for debugging, requires no parsing. Support --json for downstream tooling.
- B2: Sections: workspace metadata, current session summary, open issues by priority, in-flight work_items, work_items with expired leases (bold separate section, error state requiring triage).
- B2 cont: also next-session directives from prior close_record, deferred decisions, recent mutations to issues and work_items.
- B3: Stdout only. Never materialise .orient.md. Always query live. Cost of fresh query is negligible; cost of stale snapshot drifting is unbounded.
- B4: Truncate at dispatch boundary, not volume. If >20 open issues, include all open issues. In-flight work_items: all of them, non-negotiable. Sessions: last 4 closed sessions.
- B5: Replace the Orient step in PROMPT.md with: Run bin/selvedge orient before starting any task. Your task starts after you have read that output.
- C1: Live introspection with formatted breakout. For each table: column name, type, constraints, enums broken out from CHECK constraints. Include a live enum reference section (atom_type, kind, status enums).
- C2: Both raw and parsed. selvedge schema issues extracts the CHECK constraint and parses it into a formatted list. Provide both raw SQL (for verification) and human-readable list.
- C3: Live read, no snapshot. Every invocation queries sqlite_master + pragma table_info() at runtime. Migrations add columns? Next schema invocation reflects the new state.
**what_not.**
- Cut: any auto-flip of issue.status on work_item state changes. Explicit disposition records are cheaper and auditable. Silent state machines have killed a thousand systems.
- Cut: reuse of existing work_items.kind enum for issue-resolution work. The conflation cost exceeds the table cost. Split the enum.
- Cut: snapshot schema or orient files in the repo. Every artifact is a drift surface.
**risk.**
- Risk: orphan work_items — parent issue resolves while children still leased. Mitigation: trigger t24_issue_work_items_orphan_on_resolve blocks status transition if any in-flight leases exist.
- Risk: expired leases silently printed in orient output. Mitigation: CLI must query work_items WHERE lease_expires_at < now() and emit non-zero exit code if any exist. Fail loudly.
- Risk: session leased_by field becomes stale. Mitigation: trigger t25_work_items_lease_renewal_explicit requires re-leasing in-flight work_item to explicitly set leased_by and advance leased_at.

### Synthesis

Three perspectives converge: issue↔work_item linkage exists; issues.status does NOT auto-flip from work_items.status; widen work_items.kind to admit issue_resolution; work_items.session_id semantics rename to creating-session; selvedge orient prints to stdout (no materialized file); selvedge schema is live from sqlite_master with parsed CHECK enums; PROMPT.md orient section replaced by a single run-selvedge-orient instruction. Diverge: linkage shape (P-1 single column on work_items vs P-2/P-3 join table), output format (P-1/P-3 markdown default vs P-2 JSON default), issue state representation (P-2/P-3 explicit column or rollup vs P-1 derived via LEFT JOIN), kind enum values (P-1 minimal add issue_resolution vs P-3 many fix-shaped values), trigger discipline (P-3 mandatory T-24 orphan-on-resolve and T-25 lease-renewal vs P-1/P-2 admit-without-trigger). Synthesis adopts: join table issue_work_items per P-2/P-3 (M:N admits the migration-bundling case where one work_item closes multiple issues, e.g. one migration could close OI-086-001..004); markdown default with --json flag per P-1/P-3 (LLM context windows are the primary consumer); derive state via join, no decomposition_status column per P-1; minimal kind enum widening (add issue_resolution only, defer richer taxonomy until empirical signal); add T-24 orphan-on-resolve trigger per P-3 (orphan work_items on issue resolve is a real failure mode); defer T-25 lease-renewal trigger to a future session.

### Synthesis points

- **convergence C-1.** All perspectives: issue↔work_item linkage exists; issues.status does NOT auto-flip from work_items.status; explicit issue_dispositions row required.
- **convergence C-2.** work_items.kind enum widens to admit issue_resolution; existing session-phase taxonomy retained but no longer load-bearing for issue work.
- **convergence C-3.** work_items.session_id semantics rename to creating-session; lease/completion sessions tracked elsewhere or via existing leased_by.
- **convergence C-4.** selvedge orient prints to stdout; no materialized .orient file (drift hazard); selvedge schema is live read from sqlite_master with parsed CHECK enums.
- **convergence C-5.** PROMPT.md orient section replaced by a single instruction: run bin/selvedge orient. Stops every agent rediscovering the substrate queries.
- **divergence D-1.** Linkage shape: P-1 column work_items.issue_id (M:1); P-2/P-3 join table issue_work_items (M:N). Synthesis adopts join table per P-2/P-3 since one migration may close multiple issues (e.g. OI-086-001..004 could share a fix).
- **divergence D-2.** orient output format: P-1/P-3 markdown default with --json flag; P-2 JSON default with --format markdown. Synthesis adopts markdown default per P-1/P-3 since LLM context windows are the primary consumer.
- **divergence D-3.** Issue decomposition state: P-2/P-3 want explicit decomposition_status column or rollup view; P-1 says derivable via LEFT JOIN. Synthesis adopts P-1 derived approach; ship the LEFT JOIN as a documented dispatch query.
- **divergence D-4.** kind enum widening: P-1 minimal (just issue_resolution); P-3 multiple fix-shaped values. Synthesis adopts minimal per P-1; richer taxonomy deferred until empirical signal.
- **divergence D-5.** Trigger strictness: P-3 mandates T-24 orphan-on-resolve refusal and T-25 explicit lease renewal; P-1/P-2 admit without triggers. Synthesis adopts T-24 (real failure mode) and defers T-25 to a future session.
- **minority M-1.** P-2 minority: JSON-first orient default; future tooling consumers will be non-LLM. Synthesis preserves intent via --json flag; minority forward if downstream tooling materialises before LLM consumers complain.
- **minority M-2.** P-3 minority: explicit decomposition_status column to make needs-work-item state structurally first-class. Synthesis defers; if LEFT JOIN dispatch query proves awkward in practice, schema add is admitted later.
