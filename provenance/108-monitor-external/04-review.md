---
session: 108
title: monitor-external — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: _me_open_external_ro builds the SQLite URI by string interpolation; paths with spaces or URI-special chars (?, #, &) will fail to open silently.
  - **fixed.** URL-encode SQLite URI path via urllib.parse.quote in _me_open_external_ro; safe set is / so absolute path components survive.
- **critical**: harvest-ef calls Conn.open() with no path; if cwd is inside the external workspace, db_path resolves to external and writes land in the wrong substrate.
  - **fixed.** harvest-ef now resolves self_db via workspace_root() at the top of the handler and passes it explicitly to Conn.open(self_db); pinning bypasses both cwd-based MODE.md search and SELVEDGE_DB_PATH override.
- **high**: harvest-ef per-file write_tx commits eagerly so partial failures are committed; non-SelvedgeError exceptions bypass the catch and skip the final JSON summary.
  - **fixed.** harvest-ef catches Exception alongside SelvedgeError per file; result entry records status=error with type and detail; final JSON summary always prints. Per-file commits retained per DV-S106-3 cli_surface refusal-report contract.
- **high**: _EF_FLAG_RE matches mid-paragraph text via MULTILINE; an EF body containing a sentence starting flag: observation will be misclassified.
  - **fixed.** _me_parse_ef_file now scans only the first 8 non-empty non-marker lines for the flag annotation; mid-paragraph flag mentions cannot override the default. Verified by test_harvest_ef_ignores_flag_buried_in_prose.
- **medium**: Self-vs-peer guard uses path equality; on case-insensitive macOS filesystems samefile semantics are required to prevent guard bypass.
  - **fixed.** Self-vs-peer guard in _me_validate_external now uses Path.samefile so case-insensitive macOS filesystems and symlinks resolve correctly to the same inode.
- **medium**: harvest-ef result entries have inconsistent shape across success/error/skip outcomes; no uniform status field complicates operator scripting.
  - **fixed.** harvest-ef result shape unified: every entry now has path, external_session_no, flag, status (success or error or skipped), and outcome-specific fields. Tests updated accordingly.
- **low**: Module docstring at the top of cli.py lists subcommands but does not mention monitor-external; reference is stale.
  - **fixed.** Module docstring now lists monitor-external alongside the other top-level subcommands with engine-v31 / DV-S106-3 reference.
## Iteration 2

- **high**: F-84 fix is incomplete: harvest-ef remains vulnerable when cwd is inside a third peer workspace and SELVEDGE_WORKSPACE is unset; workspace_root resolves to that third peer.
  - **fixed.** harvest-ef now refuses E_REFUSAL_SELF when Path.cwd().resolve is inside the resolved peer root; covers the residual cwd-confusion scenario without requiring SELVEDGE_WORKSPACE.
- **high**: test_harvest_ef_pins_writes_to_workspace_root claims to set SELVEDGE_DB_PATH but the harness does not pass extra_env, so the test does not exercise the regression.
  - **fixed.** rewritten as test_harvest_ef_ignores_selvedge_db_path_override using _run_external_cli with SELVEDGE_DB_PATH=peer_db extra_env, plus new test_harvest_ef_refuses_when_cwd_inside_peer for the F-90 cwd guard.
## Iteration 3

- **high**: F-90 cwd guard is incomplete: cwd inside peer1 plus workspace=peer2 plus SELVEDGE_WORKSPACE unset still routes writes to peer1 because workspace_root walks cwd upward.
  - **fixed.** harvest-ef refuses if SELVEDGE_WORKSPACE is unset; explicit env makes self-dev unambiguous. New test_harvest_ef_refuses_without_explicit_self_workspace_env covers F-92.

## Terminal passes

- **iteration 1** — findings @ `62b52cf86f82`
  - Iter 1 surfaced 7 findings (F-83 to F-89): URI escape, harvest-ef cwd hazard, exception coverage, flag regex, samefile guard, shape inconsistency, docstring.
- **iteration 2** — findings @ `62b52cf86f82`
  - Iter 2 surfaced F-90 (cwd guard incomplete for residual third-workspace scenario) and F-91 (test did not exercise SELVEDGE_DB_PATH bypass).
- **iteration 3** — findings @ `62b52cf86f82`
  - Iter 3 surfaced F-92: cwd guard still incomplete because workspace_root walks cwd upward when SELVEDGE_WORKSPACE is unset.
- **iteration 4** — clean @ `62b52cf86f82`
  - Iter 4 reviewer verdict clean: SELVEDGE_WORKSPACE-required guard plus cwd-inside-peer guard plus samefile root check make all multi-peer scenarios safe.
