---
session: 077
perspective: cross-family-devops
family: OpenAI
date: 2026-04-27
---

# cross-family-devops — blind position

## Frame

I read this as a data-integrity and operating-surface problem, not primarily as an agent-design problem. `constraints.md` says models default to prose, treat failure as cheap, lose foundational instructions under context pressure, and cannot internalise lessons across sessions; the successor should therefore move the parts that require precision out of model discretion. The database is not a convenience layer. It is the enforcement boundary. The multi-agent shape only helps if each agent writes through that boundary and cannot smuggle state back into Markdown, memory, or unmanaged chat messages.

## Position

### Substrate

Use SQLite first, with a clear promotion path to Postgres. SQLite is the right default because Selvedge is workspace-local, git-backed, and operator-run. It gives transactions, foreign keys, `STRICT` tables, indexes, triggers, and zero server operations. Postgres becomes justified only when agents run across multiple machines, write concurrency regularly exceeds one active writer, or the human review surface needs web-native multi-user access. A document store, graph store, triple store, or JSON files with schema validation should be rejected for v1 because the failure mode in `constraints.md` property 1 is precisely prose-shaped state with weak reference refusal.

The state bundle should be:

- `state/selvedge.db` — source of truth for structured state.
- `state/migrations/NNN-name.sql` — schema history.
- `state/exports/` — generated close artefacts for human reading, never source of truth.
- git — tamper-evident outer substrate, as `methodology.md` already requires at close.

The database is committed at close. Before commit, `selvedge validate --precommit S077` runs `PRAGMA integrity_check`, foreign-key checks, lifecycle checks, and generated-artifact consistency checks. Recovery from a bad change is git restore of the database plus Markdown artefacts. Recovery from runtime crash is SQLite rollback plus lease expiry, not manual Markdown repair.

### Identifiers

Identifiers should be allocated by the substrate, not proposed by agents.

- Sessions: `S%03d`, display path still `provenance/077-<slug>/`.
- Decisions: `D-S%03d-%03d`; display alias may render as `S077:D1` for continuity with `workspace.md`.
- Specifications: `SPEC-<slug>` plus versions `SPEC-<slug>-v%03d`.
- Agent runs: `AR-S%03d-<role>-%02d`.
- Deliberations: `DEL-S%03d-%03d`.
- References: `REF-S%03d-%05d`.
- Work items: `WI-S%03d-%05d`.

Agents ask the CLI for the next object; they do not type these IDs into prose and hope they are right.

### Core schema

The minimum schema should have an object registry so references can be checked generically without polymorphic foreign-key gaps:

| table | key columns |
|---|---|
| `workspaces` | `workspace_id text primary key`, `mode check`, `engine_version_at_creation`, `created_at` |
| `objects` | `object_id text primary key`, `object_type check`, `lifecycle_state check`, `created_session_id references sessions`, `created_at`, `closed_at` |
| `sessions` | `session_id text primary key references objects`, `session_no integer unique`, `slug`, `mode`, `application_id`, `status check(planned,active,closing,closed,aborted)`, `engine_version_start`, `engine_version_close`, `started_at`, `closed_at` |
| `session_activity` | `session_id`, `activity check(read,assess,convene,deliberate,decide,produce,validate,record,close)`, `status`, `started_at`, `completed_at`, unique `(session_id, activity)` |
| `read_log` | `session_id`, `source_type check(file,db_query,tool,operator)`, `locator`, `content_sha256`, `loaded_bytes`, `purpose`, `agent_run_id` |
| `agent_runs` | `agent_run_id text primary key`, `session_id`, `role check(reader,specifier,decider,deliberator,reviewer,validator,assembler,subtractor,orchestrator)`, `family`, `model`, `status`, `context_budget_tokens`, `started_at`, `ended_at` |
| `work_items` | `work_item_id`, `session_id`, `role`, `input_json check(json_valid(input_json))`, `status check(queued,leased,done,failed,cancelled)`, `leased_by`, `lease_expires_at`, `output_object_id` |
| `decisions` | `decision_id text primary key references objects`, `session_id`, `local_no`, `title`, `body_md`, `rationale_md`, `status check(draft,proposed,accepted,rejected,deferred,superseded)`, `decided_at`, unique `(session_id, local_no)` |
| `decision_alternatives` | `decision_id`, `alternative_no`, `alternative_md`, `rejection_reason_md`, unique `(decision_id, alternative_no)` |
| `specs` | `spec_id text primary key references objects`, `slug unique`, `canonical_path`, `current_version_id`, `status check(active,retired)` |
| `spec_versions` | `spec_version_id text primary key references objects`, `spec_id`, `version_no`, `path`, `body_sha256`, `status check(draft,active,superseded,retired)`, `created_session_id`, `supersedes_version_id`, unique `(spec_id, version_no)` |
| `refs` | `ref_id text primary key`, `source_object_id references objects`, `relation check(cites,supersedes,amends,implements,rejects,opens,closes,validates)`, `target_object_id references objects`, `target_version_id references objects null`, `created_session_id`, `allow_superseded integer default 0`, `reason_md null` |
| `reviews` | `review_id text primary key references objects`, `session_id`, `reviewer_agent_run_id`, `close_correctness_md`, `mechanism_adequacy_md`, `trajectory_discipline_md`, `finding_count generated or derived` |
| `issues` | `issue_id text primary key references objects`, `status check(open,resolved,deferred,withdrawn,superseded)`, `title`, `body_md`, `opened_session_id`, `closed_session_id` |
| `engine_feedback` | `feedback_id text primary key references objects`, `origin_session_id`, `status check(new,triaged,resolved,rejected,deferred)`, `body_md`, `disposition_md` |

Counters are derived with queries. The only stored sequence-like values are local ordinals assigned inside transactions for stable display. A validator should refuse any Markdown decision file whose declared decision IDs do not match database rows.

### Lifecycle and refusal

Closed sessions are immutable. SQLite triggers should reject updates to `decisions`, `refs`, `spec_versions`, `read_log`, and `reviews` where the owning session is `closed`. Later correction happens by new rows in a later session, matching `methodology.md` preservation rules.

Reference insertion should refuse missing targets. Reference insertion to a superseded spec version should fail unless `allow_superseded=1` and `reason_md` is non-empty. This implements `constraints.md` properties 2 and 5: failure must be structural, and lessons must become prevention rather than repeated review findings.

Specification versioning should be explicit: a new substantive spec edit creates `SPEC-workspace-v002`, marks v001 `superseded`, updates `specs.current_version_id`, and records a `refs` row from the deciding decision to both versions with `supersedes`.

### Agent boundary

Do not make every named role a long-running agent. That would recreate ceremony as infrastructure.

- Deterministic tools: reader query facade, validator, assembler, ID allocator, migration runner.
- LLM agents: deliberator perspectives, specifier, reviewer, subtractor, sometimes decider.
- Orchestrator: one process that opens a session, creates work items, launches agents, and closes.

Coordination should be through the substrate. A work item is UTF-8 JSON, capped at 32 KiB, containing object IDs and requested output shape, not copied workspace context. Large outputs become `objects` plus Markdown body columns or file paths with SHA-256. A deliberator receives something like:

```json
{"session_id":"S077","work_item_id":"WI-S077-00012","role":"deliberator","inputs":[{"object_id":"SPEC-constraints-v001"},{"object_id":"DEL-S077-001"}],"output_contract":"blind_position_v1"}
```

Agents write outputs by calling `selvedge submit --work-item WI-S077-00012 --file position.md`. The CLI validates shape, inserts rows, and marks the item done in one transaction. Agents do not message each other directly.

### Failure and recovery

If two agents write conflicting state, SQLite serializes writers and unique constraints decide. One insert succeeds; the other receives a refusal that must be handled as a new work item or operator intervention.

If the orchestrator crashes, `sessions.status='active'` remains. Recovery runs `selvedge recover S077`: expired leases return to `queued`, completed outputs remain, and no partially inserted decision exists because writes are transactional.

If the database is corrupt, restore the last committed `state/selvedge.db` from git. If corruption appears after a migration, roll back the migration branch and re-run from the prior close. Do not build an elaborate second state system until empirical evidence demands it; `constraints.md` explicitly warns that database-protection ceremony can become the same failure in another form.

### Scale and operations

This design should tolerate far beyond the prior 75 sessions and roughly 3000 active spec lines noted in `engine-manifest.md`: 10,000 sessions, 100,000 decisions, 1,000,000 references, and tens of thousands of agent runs are ordinary SQLite territory with indexes on `refs(source_object_id)`, `refs(target_object_id)`, `decisions(session_id)`, and `work_items(status, lease_expires_at)`. The cliff is not row count; it is write concurrency and operational distribution. More than one workspace-local orchestrator or more than five frequent concurrent writers is the Postgres trigger.

A session should look like:

```sh
selvedge session start --slug design-space --application 075
selvedge deliberate create --session S077 --question "next-generation engine design space"
selvedge run --session S077 --agents agents.yml
selvedge validate --precommit S077
selvedge assemble --session S077 --out provenance/077-design-space
git add state/selvedge.db state/migrations provenance specifications
git commit
```

The human reviewer should interact with a compact terminal or web dashboard showing failed checks, changed active specs, unresolved references, repeated warning classes, and generated close text. The subtractor should interact with derived weight reports: active spec bytes, role count, open issue age, repeated validation failures, and artefacts unused by any session in N sessions. Its authority is not advisory; it can propose removal decisions that the normal decision mechanism must accept, reject, or defer with reasons.

## Where you would not commit

I would not commit permanently to SQLite without a concurrency trial. If session 078’s prototype actually launches remote cross-family agents that write independently from different machines, Postgres may be simpler than fighting SQLite locking and file sync semantics.

I would not commit to the object registry if a prototype shows it becoming a universal abstraction swamp. The evidence that would change my mind is a simpler schema that still enforces references across decisions, specs, issues, reviews, and feedback without application-side hand-checking.

I would not commit to generated Markdown exports as sufficient review surface. Binary database state in git is recoverable but not naturally reviewable. If human reviewers cannot audit changes from generated diffs alone, the system may need a canonical SQL dump or NDJSON export, but that should be added only after the pain is observed.

I would not commit to pure substrate coordination for all agents. For short local runs it is enough. Long-running hosted agents may require a real queue, but the queue should carry work-item IDs and leases, not become a second source of state.

## What you think the other perspectives will miss

I expect some perspectives will treat “database” as storage rather than refusal. That misses the central engineering point from `constraints.md`: the model’s defaults only change when malformed work cannot be accepted.

I expect the multi-agent discussion to overvalue role taxonomy and undervalue write-path discipline. Seven roles are manageable if four are deterministic tools; seven chatty LLM agents are an operations problem disguised as methodology.

I expect the subtraction role to be framed culturally rather than mechanically. A subtractor without delete authority, derived weight reports, and a decision path for removals will become another reviewer.

I expect human-review advocates to ask the reviewer to read more. The stronger design asks the reviewer to read less but see sharper exceptions: refused references, superseded targets, repeated validation classes, and generated diffs against active specifications.
