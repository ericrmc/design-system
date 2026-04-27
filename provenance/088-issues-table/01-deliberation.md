---
session: 088
title: issues-table — deliberation
generated_by: selvedge export
---

# Deliberation

## D-4 — issues substrate table schema and backfill strategy

sealed_at: 2026-04-27T12:11:17.033Z

### P-1 (anthropic)

**Position.** Ship smallest issues schema that closes dispatch loop: one row per issue, single body atom, one links surface, three CLI kinds, one migration. Refuse elaboration until a session uses dispatch and complains.

**schema_sketch.**
- Identity: numeric issue_id PK plus citable_alias of shape OI-NNN[-NNN]. Drop the trailing slug from alias entirely; slugs belong in title atom not identifier.
- Aliases register in objects.citable_alias with object_kind=issue, added under a T-15 calibrated marker. OI-NNN-NNN form already encodes session-of-surfacing post-079; preserve it.
- Status enum: open or resolved. Two values, default open. Prose qualifiers (monitor, deferred, blocked-on) are notes about why an issue is open, not status values; they belong in note atoms or blocked_on links.
- in_progress is a leasing concept; if needed use existing work_items table, do not duplicate. superseded and wontfix collapse into resolved with a disposition enum (fixed, withdrawn, superseded, wontfix, deferred-permanently).
- Reopening admitted only via a new submit issue-disposition row that flips status to open with a reason atom; prior resolution row not edited (T-06 enforces this for closed-session rows).
- Priority enum closed: HIGH, MEDIUM, LOW. Three values matching what the 25 files use. Qualifiers like post-gate are not priorities; they are blocked_by edges to a gate object or another issue.
- Body storage: single body_md atom of atom_type=issue_body with the legacy_import 8-4000 char cap. Path A decomposition into issue_sections/issue_clauses is over-engineered; issues are not specs, not cited clause-by-clause.
- If an issue grows deliberation-style narrative (OI-002), split into multiple issues rather than introducing section/clause hierarchy. The 4000-char cap excludes OI-002 by design; OI-002 is a 16-session running annotation, not one issue.
- Relations: one issue_links surface with relation enum blocks, blocked_by, supersedes, duplicates. No folds_into (it is supersedes with a different label). blocks/blocked_by stored once canonical as blocks; dispatch reads both directions.
- Prefer reusing the existing refs table with object_kind=issue and widened relation enum (add blocks, duplicates under a calibrated marker) over creating a new issue_links table. Free-text references in body atoms are forbidden.
- Sessions: surfaced_in_session_id NOT NULL FK; resolved_in_session_id nullable, set only when status flips to resolved. Disposition row also carries resolving session; redundancy is cheap and lets dispatch filter without a join.
- Markdown coexistence: backfill then delete the 25 files. Path A says markdown is a generated export; parallel hand-maintained surface is the failure OI-085-002 names.
- Generate OI-NNN.md and index.md from substrate via selvedge export issues; refuse Write/Edit on those paths via the OI-085-002 harness hook. Parallel maintenance equals deletion with extra steps and drift.
**migration_path.**
- Backfill via in-migration SQL plus a small Python helper invoked by the migration runner. Not a subagent: subagents are non-deterministic and this is a one-shot import of 25 files into 25 rows.
- Helper reads each file, parses YAML frontmatter, writes one issues row plus one text_atoms row plus one objects row plus one legacy_imports row per file. Malformed files import as legacy_import atoms with decomposition_status=unratified.
- OI-002 specifically should be imported then split in the same session: its current shape is a 16-session log file, not an issue. Future session re-authors malformed atoms as proper issue_body atoms if warranted.
**cli_surface.**
- Three CLI submit kinds: submit issue, submit issue-disposition, submit issue-link. No submit issue-comment. Adding context after creation is a new disposition row (kind note) or a new linked issue.
- Comments are how trackers grow into Jira; refusing them is the substrate doing its job. Dispatch surface ships as bin/selvedge next, a single command, not a query the next session has to remember.
- Dispatch order: priority first then FIFO by surfaced session. Topological-blocks enforced as WHERE-NOT-EXISTS filter; at ~25 active issues this filter is exact and cheap, no full topological sort needed.
**what_not.**
- Cut spec_sections/spec_clauses analogue for issues. Path A is right for normative spec text; wrong for transient tracking prose. Refuse to ship it.
- Cut in_progress, blocked, wontfix, superseded as status values. Compress to two; encode the rest as disposition or links. Cut submit issue-comment on principle.
- Cut a separate issue_links table; reuse refs with widened relation enum. Cut a new identifier scheme: OI-NNN-NNN is fine, do not invent ISSUE-S088-1.
- Cut section/clause decomposition in the migration that creates issues; out of scope, defer to a future session if any issue actually needs it (none currently do).
**risk.**
- Risk: backfilling OI-002 hits the 4000-char cap and migration fails halfway. OI-002 is ~12K chars and will not fit legacy_import. Substrate should refuse the row, not silently truncate.
- Mitigation for OI-002 cap risk: pre-migration helper measures every file; any file over cap is logged as a backfill failure and migration aborts before any rows are written. Operator splits OI-002 by hand before re-running.
- Risk: drift between issues.status and disposition row effects. Two sources of truth produced manifest-vs-schema drift in the table-count saga (OI-079-001/OI-081-001).
- Drift mitigation: trigger refusing issue_dispositions inserts inconsistent with old plus transition (T-09 analogue); refuse direct UPDATE of issues.status, only movable via disposition row insert.
- Risk: dispatch returns issues blocked by something not yet modelled as a blocker. Most current blocked-on qualifiers are prose (OI-081-001 blocked-on 078 D-5 release gate); the gate is not an issue.
- Mitigation for gate risk: extend object_kind to admit gate (or release_gate) in the same migration, register the active gate as object, convert prose qualifier to refs row at backfill. Without this, dispatch surfaces blocked issues.

### P-2 (openai)

**Position.** Make issues a compact substrate queue, not a prose archive: one immutable identity row per issue, atomized title/summary/next-step, append-only notes and dispositions, explicit graph links, substrate-only dispatch.

**schema_sketch.**
- Identity: numeric issue_id PK and immutable objects.citable_alias. Backfilled rows keep historical alias exactly (OI-002, OI-085-002, OI-079-001); new rows use ISSUE-S088-1 form with session and ordinal, no slug.
- Slugs are mutable description, not identity, so they do not appear in alias. Status enum: open, in_progress, blocked, resolved, superseded, wontfix; default open.
- Reopening admitted only through submit issue-disposition with from-status, to-status, session FK, and reason atom. Terminal issue content remains immutable but queue state may transition.
- Priority closed enum: high, medium, low, default medium. post-gate, blocked-on, and similar qualifiers are not priority values; they belong in links, notes, or explicit disposition reasons.
- Body storage rejects body_md and full Path-A issue_sections/issue_clauses. Issues are queue objects, not specifications. Use title_atom_id, summary_atom_id, next_step_atom_id, optional resolution_atom_id, plus issue_notes rows.
- issue_notes rows hold 16-480 char atoms for history. Search runs over a view joining issue title, summary, next step, resolution, and notes.
- Relations: add issue_links with relation enum blocks, duplicates, supersedes, folds_into, related. Store only directed facts; blocked_by is derived from inverse blocks. Refuse self-links, duplicate links, and blocks cycles.
- Sessions: surfaced_session_id required. resolved_session_id nullable while non-terminal and required for resolved, superseded, or wontfix; terminal transitions require a disposition atom.
- This makes provenance structural without pretending every status mutation belongs to the original surfacing session.
- Markdown: after backfill, delete the active markdown issue surface. Preserve old files as a one-time archive/import witness with hashes, but do not maintain open-issues/index.md as a parallel dispatch surface.
**migration_path.**
- Do not put content import in schema migration SQL. Ship the schema and CLI kinds, then run a deterministic importer inside the session.
- Importer parses frontmatter, submits rows via the CLI, stores source path/hash, and emits import anomalies as issue notes. Hybrid files import per operational state.
- OI-079-001 imports as terminal with a link to OI-081-001; conditional reopen triggers become notes, not fake-open statuses.
**cli_surface.**
- Ship exactly four CLI kinds: submit issue, submit issue-disposition, submit issue-link, submit issue-note. Do not add issue-comment; comment invites chatty prose, while note can be typed and atom-bounded.
- Dispatch selects actionable, unblocked open issues then sorts by priority, unblocking value (count of issues this one blocks), and age. Returns issue_id, alias, title, priority, surfaced session, open_dependents, next_step.
- Dispatch joins issues to objects, title atom, sessions, optional next_step atom, and a dep subquery counting issues this one blocks (open, blocked, in_progress).
- Dispatch filters to status=open and NOT EXISTS unresolved blocker (relation=blocks targeting this issue with blocker status in open, blocked, in_progress).
- Dispatch ORDER BY: priority (high=1, medium=2, low=3), open_dependents DESC, surfaced session_no ASC, issue_id ASC; LIMIT 1.
**what_not.**
- Cut body_md, free-text status, free-text priority, duplicate blocked_by storage, markdown as an active surface, and full Path-A issue decomposition.
- Also cut in-migration content import: schema migrations define shape; importer sessions move historical data.
**risk.**
- Reopen laundering: terminal issues could be casually returned to open. Substrate must refuse terminal-to-open transitions unless an issue_disposition row has a current session FK and a 16-480 char reason atom.
- Graph deadlock: bad blocks links could cycle or make dispatch return nothing while open issues remain. Substrate should refuse self-links and cycles; dispatch should fail loudly with the unresolved blocker set.
- Import compression loss: long OI files could be over-summarized, erasing activation triggers. Importer must preserve source path/hash and create anomaly or note atoms for every unmapped paragraph before marking imported.

### P-3 (anthropic)

**Position.** Substrate-native issues require closed-schema dispatch and backwards-compatible hybrid states: closed enums, substrate-enforced state machines, and lossless preservation of the heterogeneous 25-file corpus.

**schema_sketch.**
- Identity: numeric issue_id PK with required, immutable, UNIQUE citable_alias TEXT capturing historical OI-NNN[-NNN[-slug]] format exactly. Parse and validate at INSERT time with a CHECK constraint.
- Backfill must read each markdown filename and frontmatter id field and demand exact match (failure triggers manual audit). Do not invent a new format like ISSUE-S088-1: that pattern belongs to decision/session aliasing.
- Status: five closed values open, in_progress, blocked, resolved, deferred. No free-text status. Enforce via CHECK constraint and T-trigger on session-close immutability.
- OI-016 and OI-079-001 are hybrid states (resolved-but-carrying-active-triggers; resolved-with-re-opening-conditions). Add nullable reopenable BOOLEAN and reopen_conditions_md TEXT (length-bounded, atom-style, no prose).
- A row with status=resolved and reopenable=1 means provisionally resolved, will auto-reopen if conditions fire. T-trigger: if reopenable=1 require non-NULL reopen_conditions_md; if 0 or NULL it must be NULL.
- Priority closed enum: CRITICAL, HIGH, MEDIUM, LOW, with optional blocking_issue_id INTEGER REFERENCES issues for explicit priority-chain representation. No free-text qualifiers like post-gate or blocked-on.
- Blockers belong in a separate issue_blockers table with rows (blocker_issue_id, blocked_issue_id, reason_atom_id REFERENCES text_atoms). Make every blockage a first-class row, not prose annotation.
- Body: single body_atom_id INTEGER REFERENCES text_atoms (NOT NULL, backfilled via legacy_import atom). Most issues are short; none merit full Path A decomposition. legacy_import 8-4000 char range covers the corpus.
- Future decomposition (claims/rejections) goes into a separate issue_clauses table created in a future migration. For now, one atom per issue.
- Mandatory issue_blockers table with closed relation enum: blocks, supersedes, duplicates, folds_into, depends_on. T-trigger: if A blocks B, B status cannot be resolved without explicit reason. Prevents silent orphaning of blocked issues.
- Sessions: surfaced_in_session NOT NULL REFERENCES sessions (immutable, set at INSERT). resolved_in_session nullable, set non-NULL only when status flips to resolved.
- T-trigger: when status flips to resolved, both resolved_in_session and a new resolved_at TEXT timestamp must be set in the same statement. T-trigger: resolved_in_session must not be updated or cleared after set (T-06 pattern).
- Markdown: delete the 25 files after backfill is validated. Substrate becomes single source of truth per engine-v20 Path A. Markdown becomes a generated export via selvedge export --session N --write.
- Audit history of pre-substrate issues lives in git via git show HEAD~50:open-issues/OI-016.md. Keeping files around just in case creates two sources of truth and drift (OI-079-001 manifest mismatch is exhibit A).
**migration_path.**
- Backfill via subagent through submit issue CLI kind, not raw SQL INSERT. Python script reads each .md file and parses heterogeneous frontmatter (id, status, surfaced-in-session, priority, blocked-on, etc.).
- For each file, calls selvedge submit issue with parsed alias, surfaced session, status, priority, body. CLI validates closed enums, enforces immutability, auto-generates legacy_import atom, records backfill session in decision record.
- Malformed files (e.g., OI-079-001 status Resolved (provisionally...)) halt the script with a detailed error naming file and field. Do not guess or coerce. Operator audits, corrects frontmatter in markdown, re-runs.
**cli_surface.**
- Require submit issue (creation), submit issue-disposition (status transitions mirroring finding-disposition), submit issue-relation (adds blockage/supersession edge to issue_blockers). Do not add submit issue-comment.
- If a session has context to add post-creation, it submits a new atom and updates the row body_atom_id; transitions trigger T-06 immutability on closed issues.
- resolved_in_session immutability means a resolved issue cannot be reopened by CLI; only an explicit submit issue-disposition with status=reopened (distinct from open) and a closed-enum reopen_reason CHECK. Prevents accidental re-opening.
- Dispatch query: SELECT issue_id, citable_alias, status, priority, session_no, slug from issues LEFT JOIN issue_blockers (only unresolved blockers) WHERE issue_blockers row IS NULL AND status IN open or in_progress.
- Dispatch JOINs sessions, ORDER BY priority DESC then surfaced_in_session ASC, LIMIT 10. Deterministic, fully indexable, refuses to surface blocked issues; no free-text priority, no substring search on status.
**what_not.**
- Cut free-text status or priority fields. The reopenable escape hatch is not optional; OI-016 and OI-079-001 prove real issues carry re-opening conditions and refusing them fails the dispatch mission.
- Cut any keep-the-markdown-as-parallel-surface compromise. Path A means substrate-only. Cut prose-based blocking relations: every blockage is a row in issue_blockers, queryable in O(log N), not substring search.
**risk.**
- Backfill halts on heterogeneous frontmatter. Operator parses OI-079-001 status Resolved (provisionally...) and the script rejects it because provisionally is not a closed enum value. This is working as designed.
- Alternative (coercing provisionally to resolved, losing re-opening-conditions nuance) leads to silent information loss. Fix is manual: operator audits the file, parses reopen_conditions_md from body if needed, re-runs.
- Dispatch over hybrid states: a future query for unresolved issues may not realize OI-016 (resolved-but-reopenable) is still active. Filter status IN open, in_progress, blocked, reopened unless query explicitly includes reopenable.
- Mitigation for hybrid query: provide a pre-built CLI kind selvedge query --next-issue that encodes the correct filter, so query authors do not forget the reopenable clause.
- Blockage cycles: operator could create issue_blockers rows forming a cycle (A blocks B, B blocks C, C blocks A). Dispatch returns empty; nothing unblocked.
- Mitigation for cycles: post-backfill validation query checks for cycles and fails backfill if one exists. T-trigger cycle detection in SQLite is expensive, so do it once at backfill-end rather than each insert.

### Synthesis

Three perspectives on issues-table design converge on substrate-only canonical surface, numeric PK + preserved historical citable_alias, closed enums for priority, dedicated link table for blocking relations, dispatch via WHERE-NOT-EXISTS filter, no submit-issue-comment kind, and reopening admitted only via disposition rows. Diverge on: status enum size (P-1 minimal two-value vs P-2 six-value vs P-3 five-value plus reopenable bool), body storage shape (P-1 single legacy_import atom vs P-2 atomized title/summary/next_step/resolution + notes vs P-3 single body_atom_id + future issue_clauses), backfill mechanism (P-1 deterministic in-migration Python helper vs P-2/P-3 subagent-via-CLI), CLI kind count (3 or 4), and identity scheme for new issues (preserve OI-NNN-NNN vs new ISSUE-S088-1). Synthesis adopts: closed five-value status enum (open/in_progress/blocked/resolved/superseded), reopening as disposition transition (no separate reopenable column), title+summary atoms with optional body_md atom for legacy_import backfill, four CLI kinds (issue, issue-disposition, issue-link, issue-note), dedicated issue_links table not refs reuse, subagent-via-CLI backfill with hard-fail on heterogeneity, preserve existing OI-NNN-NNN aliases verbatim and reserve new-issue alias format for a future decision.

### Synthesis points

- **convergence C-1.** All perspectives: substrate-only canonical, numeric issue_id PK plus citable_alias on objects, preserve historical OI-NNN aliases.
- **convergence C-2.** Closed priority enum HIGH/MEDIUM/LOW; free-text qualifiers go to links or notes, never priority.
- **convergence C-3.** Dedicated link-edge enforcement for blocks/supersedes/duplicates relations; dispatch via WHERE-NOT-EXISTS filter on open blockers.
- **convergence C-4.** Markdown files deleted after backfill; substrate becomes canonical; harness refuses Write/Edit on open-issues paths.
- **convergence C-5.** submit issue-comment refused; reopening admitted only via submit issue-disposition with reason atom.
- **divergence D-1.** Status enum size disagreement: P-1 wants two values open/resolved; P-2 wants six values; P-3 wants five plus reopenable bool. Synthesis adopts five values (open/in_progress/blocked/resolved/superseded) without reopenable column.
- **divergence D-2.** Body storage disagreement: P-1 single 4000-char issue_body atom; P-2 atomized title/summary/next_step/resolution + notes; P-3 single body_atom_id with future issue_clauses. Synthesis adopts title atom + summary atom + optional legacy_import body atom; notes via separate issue_notes table.
- **divergence D-3.** Link table disagreement: P-1 reuses refs with widened relation; P-2 dedicated issue_links; P-3 dedicated issue_blockers. Synthesis adopts dedicated issue_links table with relation enum blocks/supersedes/duplicates/folds_into.
- **divergence D-4.** Backfill mechanism disagreement: P-1 in-migration deterministic Python helper; P-2/P-3 subagent-via-CLI. Synthesis adopts subagent-via-CLI with hard-fail on heterogeneity per P-3.
- **divergence D-5.** CLI kinds count: P-1 wants three (issue, issue-disposition, issue-link); P-2 wants four (adds issue-note); P-3 wants three with issue-relation. Synthesis adopts four kinds per P-2 (notes typed and atom-bounded are useful).
- **minority M-1.** P-3 minority: explicit reopenable BOOLEAN + reopen_conditions_md columns to honestly represent OI-016 hybrid resolved-with-active-triggers state. Synthesis preserves intent via disposition history rather than schema columns; minority forward if disposition approach drifts.
- **minority M-2.** P-1 minority: refuse OI-002 import on size grounds and force operator to split it before backfill. Synthesis defers: import OI-002 as legacy_import atom (4000 char cap admits truncation; full body preserved in git); split deferred to a future session.
