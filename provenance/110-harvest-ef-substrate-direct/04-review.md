---
session: 110
title: harvest-ef-substrate-direct — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: _me_read_peer_ef catches sqlite3.OperationalError on connection open and maps unconditionally to E_PEER_BUSY; corrupt DB or wrong path also gets that label.
  - **fixed.** Pattern matches _refusal_from_sqlite: locked/busy maps to E_PEER_BUSY; other OperationalError now maps to new E_PEER_OPEN_FAILED.
- **high**: Query execution path has same OperationalError ambiguity; SQL/schema errors mislabeled as E_PEER_BUSY.
  - **fixed.** New E_PEER_QUERY_FAILED separates non-busy query failures from transient lock contention.
- **medium**: Module docstring lists structured error codes but omits new E_PEER_BUSY and E_PEER_SCHEMA_UNSUPPORTED.
  - **fixed.** Docstring updated with E_PEER_BUSY, E_PEER_OPEN_FAILED, E_PEER_QUERY_FAILED, E_PEER_SCHEMA_UNSUPPORTED.
- **medium**: Race-window UNIQUE collision on harvested_engine_feedback ledger surfaces as generic IntegrityError without context for the operator.
  - **fixed.** Catch block recognises E_REFUSAL_UNIQUE on harvested_engine_feedback and labels result as skipped with reason concurrent harvest already imported this peer row.
- **medium**: Empty peer_rows path silently returns empty results; operator may miss that peer has no rows to harvest.
  - **fixed.** Both dry-run and live output now include note peer substrate has no engine_feedback rows when applicable.
- **medium**: _do_harvest closure captures fid/peer_ws_id/peer_alias as default args but role from enclosing scope; inconsistent style.
  - **fixed.** Added role default-arg capture for consistency; rules out late-binding surprises if the loop changes shape later.
## Iteration 2

- **medium**: Schema validation queries (sqlite_master, workspace_metadata, pragma_table_info) lack OperationalError categorisation; raw exception would propagate.
  - **fixed.** Added _peer_exec inner helper that wraps every peer query with the same E_PEER_BUSY/E_PEER_QUERY_FAILED categorisation.
- **medium**: _me_read_peer_ef docstring Raises section listed only 2 of 4 actual error codes.
  - **fixed.** Docstring Raises section now lists all 4: E_PEER_OPEN_FAILED, E_PEER_BUSY, E_PEER_QUERY_FAILED, E_PEER_SCHEMA_UNSUPPORTED.

## Terminal passes

- **iteration 1** — findings @ `c3404d9aec52`
  - Iter-1: 2 high + 4 medium findings (OpError ambiguity x2, docstring, race-UNIQUE label, empty-rows note, closure style). All fixed in-iteration.
- **iteration 2** — findings @ `c3404d9aec52`
  - Iter-2: 2 medium findings (schema-query OpError gap, docstring Raises incomplete). Both fixed in-iteration via _peer_exec helper + Raises list update.
- **iteration 3** — clean @ `c3404d9aec52`
  - Iter-3: clean. _peer_exec helper correctly wraps schema-validation queries; docstring Raises section matches all 4 raised codes; no new medium+ findings.
