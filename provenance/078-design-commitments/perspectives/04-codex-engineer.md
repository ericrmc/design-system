---
session: 078
perspective: codex-engineer
family: OpenAI
date: 2026-04-27
---

# codex-engineer — blind position

## Frame

I read 078 as committing the write path, not choosing a fashionable persistence layer. The empirical failure in `constraints.md` is not "Markdown was ugly"; it is that models default to prose, treat failure as cheap, lose foundational instructions under context pressure, and do not retain lessons across sessions. The successor substrate therefore has to make malformed state impossible to accept at the point of write. I agree with 077's substrate-as-refusal-contract framing `[077-D-1]` and with my 077 counterpart that the database is the enforcement boundary `[077-dev]`, but I would sharpen the engineering commitment: the real concurrency decision is not "which database tolerates many writers"; it is "where is the single serialization point for Selvedge state?"

## Position

### Substrate commitment: SQLite 3, local single-writer semantics

Commit to **SQLite 3** as `state/selvedge.sqlite`, accessed only through a deterministic `selvedge` CLI/library owned by the engine. Enable `WAL` mode, `foreign_keys=ON`, `STRICT` tables where available, `busy_timeout`, and transactional migrations. Do not introduce Postgres, libSQL, DuckDB, or a custom file store for engine-v17.

I agree with `[077-dev]` that SQLite fits the operator-run, workspace-local shape: one file, no daemon, no network port, no database auth surface, simple backup, and enough relational enforcement for identifiers, references, lifecycle, ordinals, and work leases. I depart from `[077-dev]` by making the remote-agent answer stricter: **remote agents are compute, not database writers**. A remote Codex call, hosted Claude call, or other out-of-process agent returns an output envelope to the operator machine; the local `selvedge submit` command performs the write. No remote process opens the SQLite file over NFS, Dropbox, SSHFS, or a sync folder. If Selvedge later needs true multi-machine direct writes, that is a new substrate decision, not a hidden v1 requirement.

Concurrency model: every write command opens its own connection and runs one short transaction with `BEGIN IMMEDIATE`. Readers get snapshot reads under WAL. Writers serialize. If two agent invocations submit at once, one obtains the write lock; the other waits up to the configured timeout with retry jitter. If it still cannot acquire the lock, the CLI returns a structured refusal such as `E_WRITE_BUSY` and leaves the work item queued or retryable. The LLM never sees a raw `database is locked` and improvises around it.

IDs are allocated inside the same transaction as the object insertion. There is no "next ID" call that hands an agent a value to remember. For session-local ordinals, use a transactional counter table keyed by `(session_id, object_type)` or an insert guarded by a unique `(session_id, local_no)` constraint. For global object IDs, create the `objects` row in the transaction and derive display IDs from committed rows. If two agents both "think" they have `D-3`, the one that typed it in prose has no authority; the accepted row gets the next committed ordinal, and any mismatched prose reference is refused by the submit validator.

Crash semantics are SQLite's normal transaction semantics plus idempotency keys. If an agent process crashes mid-transaction, SQLite rolls the transaction back; there is no half decision and no half supersession edge. If the process commits but dies before telling the orchestrator, recovery detects the committed row by a unique idempotency key such as `(work_item_id, output_kind, output_hash)` and marks the work item done rather than inserting a duplicate. If the orchestrator dies after dispatching a work item and before any write commits, the leased work item expires and `selvedge recover S078` returns it to `queued`. If the agent later submits after lease expiry, the submit command refuses with `E_LEASE_EXPIRED` unless the orchestrator has renewed the lease.

Operational footprint: the operator gets `state/selvedge.sqlite`, transient `state/selvedge.sqlite-wal` and `state/selvedge.sqlite-shm` while active, `state/migrations/*.sql`, and generated exports. Backup is `sqlite3 .backup` or checkpoint-and-`cp` while no write transaction is running. There is no daemon, no port, and no database password; filesystem permissions and the local CLI are the access boundary. This is intentionally boring. `constraints.md` warns that schema-substrate-protection ceremony can reincarnate the old problem; Postgres would be premature ceremony for the first implementation unless direct multi-user writes are already a requirement.

The smallest falsification trial for 079: create one active session and spawn 16 parallel `selvedge submit decision` processes, each inserting a decision with one rejected alternative and one reference to the same active spec. Inject a sleep inside several transactions to force lock contention, and kill one process after `BEGIN IMMEDIATE` but before commit. Expected result: accepted decisions have unique contiguous local ordinals, references all resolve, the killed process leaves no partial rows, queued work items are recoverable, `PRAGMA integrity_check` and `foreign_key_check` pass, and no raw lock error reaches the agent layer. This choice is falsified if duplicate ordinals appear, a lock wedges the database until manual repair, successful commits are duplicated on retry, or the operator has to inspect SQLite internals to recover.

### Substrate shape: pick S1 with typed satellites, reject S2 as the default

For Divergence-3, I would commit to **S1 body-in-cells with typed satellite tables**, not S2 index-only and not full S3 tuples `[077-D-3]`.

The adversary's prose-in-cells critique is real `[077-adv]`: a `body_md` column can become Markdown-state wearing SQL clothes. But S2 does not solve that engineering problem; it creates a two-phase consistency problem between files and rows. A crash can leave a Markdown file without a row, a row with a missing file, or a hash mismatch unless the engine builds a second transactional protocol around the filesystem. That is extra machinery at exactly the boundary `constraints.md` says models mishandle.

The S1 commitment should be narrow: `body_md TEXT NOT NULL` is design intent, not state. Anything the engine must check becomes a column or child row: rejected alternatives, spec supersession edges, references, lifecycle state, session status, work item leases, schema versions. S3 is appropriate selectively for these child rows; it is wrong as a total replacement for reasoning prose because it will either destroy readability or create escape hatches named `notes_md`.

SQLite can enforce the refusal contract with native constraints for the structural parts: `NOT NULL`, `CHECK`, `UNIQUE`, `FOREIGN KEY`, triggers with `RAISE(ABORT, ...)`, and transactions. It cannot and should not be asked to understand natural-language contradiction. Markdown reference extraction belongs in the `selvedge submit` application layer, in the same transaction as row insertion: parse declared tokens, insert `refs`, refuse unresolved or stale targets, then run a post-insert consistency check before commit. Direct SQL writes are outside the engine contract.

Minimum refusals 079 should implement: missing foreign keys; reference to a superseded spec version without `allow_superseded=1` and a reason; illegal lifecycle transition; update/delete of rows owned by a closed session; duplicate active spec for a slug; duplicate session-local ordinal; work-item submit after lease expiry; submit against a stale schema version; and session close while required validations fail.

### Schema-evolution protocol

Schema changes happen because a normal write is refused and the session decides the refusal means the schema is too narrow, not because an agent wants a more convenient shape. The v1 schema must include `schema_change_requests` and `schema_migrations` from the start.

A refused write may be recorded as a `schema_change_request` containing the session, refusal code, refused payload hash, short rationale, and status. It does not insert the invalid domain row. A schema change is authorised by a normal decision with `decision_kind='schema_change'` that cites the request. Additive changes are authorised by the current session decision: new nullable column, new table, new index, new view, or stricter trigger that applies only to future rows. Contract changes require the methodology's normal foundation-touching discipline: multi-perspective deliberation with at least one cross-family voice, or an explicit operator-directed exception recorded in the decision. Contract changes include dropping columns, rewriting object identity, changing refusal semantics, backfilling non-derived historical meaning, or moving body storage shape.

Historical rows are preserved first. New columns default to `NULL` for old rows unless the value is mechanically derivable from existing structured state. Backfill is allowed only when deterministic: hashes, derived counters, copied foreign keys, status values already implied by existing rows. No LLM infers historical facts. If a new invariant should apply only after migration 004, enforce it with triggers that check the row's `created_schema_version >= 4`, not by pretending session 050 had data it never recorded.

During migration, the substrate enters `schema_state='migrating'`. Non-migration writes are refused with `E_SCHEMA_MIGRATING`; work items queue. Read-only queries may continue from snapshots, but any submit includes the `schema_version` from the work-item lease and is refused with `E_STALE_SCHEMA` if the schema changed while the agent was working. That refusal is useful: it prevents an agent from submitting an output shaped for yesterday's contract.

Review is proportional. Every migration has a file in `state/migrations/NNN_slug.sql`, a hash in `schema_migrations`, a decision citation, and a validation transcript. Additive migrations need deterministic review: apply to a copy, run integrity checks, run exporter, run the concurrency smoke test if write-path tables changed. Contract migrations need deliberative review because they change what the system refuses. This avoids making every column addition a methodology session while still treating refusal changes as foundation-touching.

Rollback is two-tier. If a migration fails before close, SQLite transaction rollback plus a pre-migration `.backup` restores the prior state. If a migration was committed in a closed session and later found semantically wrong, the fix is forward-only: a new corrective migration and decision. That matches `methodology.md` preservation: closed provenance is corrected by later records, not rewritten.

## Where you would not commit

I would not commit SQLite for direct multi-machine writers. If the operator requires remote agents to open the same database file and write independently, choose Postgres instead. My SQLite commitment depends on local serialization of writes.

I would not commit that S1 prevents prose-in-cells by itself. It only works if 079 implements typed child rows and refuses direct SQL writes. A schema with `body_md` plus a few weak foreign keys is the adversary's failure mode.

I would not commit to the exact busy timeout or retry budget. The concurrency trial should set it. If normal parallel submits frequently hit `E_WRITE_BUSY`, the system needs a local write queue process or a different substrate.

I would not commit to heavy schema governance. The additive/contract split is my attempt to keep ceremony bounded. If agents start using "schema change request" as a way to bypass ordinary refusals, the protocol should become more operator-mediated, not more elaborate.

## What you think the other perspectives will miss

I expect some perspectives will treat distributed agents as implying a distributed database. That is the wrong first cut. The simpler commitment is that Selvedge has one authoritative write location; remote agents produce candidate outputs, not state.

I expect S2 to look safer because Markdown stays in files. From an engineering perspective it is usually less safe: it adds file/database atomicity problems while leaving prose semantics just as unchecked.

I expect schema evolution to be over-moralised. Most schema changes should be boring migrations with tests. Only changes to refusal semantics deserve the full deliberative weight.
