"""Selvedge CLI — argparse setup and main dispatch.

Subcommand implementations live in dedicated modules (see imports below).
This file is intentionally argparse-only: it owns no business logic.

Subcommands:
  init                 Initialise a fresh substrate.
  migrate              Apply pending migrations against an existing substrate.
  id-allocate          Allocate an object_id in-transaction.
  submit               Write a row to the substrate; refuses on T-01..T-31.
  validate --precommit Run substrate integrity + spec hashes + ref resolution.
  subtract-eligibility Deterministic eligibility report.
  recover              Reset expired work_item leases to 'queued'.
  query                Read-only convenience query.
  export               Materialise markdown views (sessions, issues, anchor traces).
  orient               Print the workspace orientation packet.
  schema               Print substrate schema (live read).
  monitor-external     Read a peer Selvedge workspace; harvest engine_feedback.

Single-writer discipline, structured errors, and substrate-only writes for
session state remain unchanged from the engine-v34 surface — only the
internal layout has moved.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Optional

from .errors import SelvedgeError
from .export import cmd_export
from .precheck import cmd_precheck
from .feedback_cmd import cmd_feedback
from .id_allocate import cmd_id_allocate
from .init_cmd import cmd_init
from .migrations import cmd_migrate
from .monitor_external import cmd_monitor_external
from .orient import cmd_orient
from .paths import ANCHOR_TRACE_DEFAULT_DEPTH, ANCHOR_TRACE_HARD_CAP_DEPTH
from .query import cmd_query
from .recover import cmd_recover
from .schema import cmd_schema
from .submit import SUBMIT_HANDLERS, cmd_submit
from .submit_help import cmd_submit_help
from .subtract import cmd_subtract_eligibility
from .validate import cmd_validate


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="selvedge", description="Selvedge substrate CLI (engine-v20)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init", help="Initialise a fresh substrate (apply 001 + any later migrations).")
    p_init.add_argument("--force", action="store_true", help="Overwrite existing substrate.")
    p_init.set_defaults(fn=cmd_init)

    p_mig = sub.add_parser("migrate", help="Apply pending migrations against an existing substrate.")
    mode = p_mig.add_mutually_exclusive_group(required=True)
    mode.add_argument("--status", action="store_true", help="List applied + pending migrations.")
    mode.add_argument("--dry-run", action="store_true", help="Parse migrations + T-15 check, no writes.")
    mode.add_argument("--apply", dest="apply_", action="store_true", help="Apply pending migrations in lex order.")
    p_mig.set_defaults(fn=cmd_migrate)

    p_idalloc = sub.add_parser("id-allocate", help="Allocate an objects row.")
    p_idalloc.add_argument("--kind", required=True)
    p_idalloc.add_argument("--typed-row-id", type=int, required=True)
    p_idalloc.add_argument("--alias", default=None)
    p_idalloc.set_defaults(fn=cmd_id_allocate)

    p_submit = sub.add_parser("submit", help="Write a row to the substrate.")
    p_submit.add_argument("kind", help=f"one of: {sorted(SUBMIT_HANDLERS)}")
    p_submit.add_argument("--payload", required=True, help="JSON payload, '@file', or '-' for stdin.")
    p_submit.add_argument("--role", default="__cli__")
    p_submit.add_argument(
        "--dry-run",
        dest="dry_run",
        action="store_true",
        help=(
            "Run the handler inside a transaction that always rolls back. "
            "Triggers and constraint refusals propagate as normal; no rows "
            "(or spec body files) persist. EF-S118-1."
        ),
    )
    p_submit.set_defaults(fn=cmd_submit)

    p_submit_help = sub.add_parser(
        "submit-help",
        help="Print payload schemas from the submit registry (documentation; handlers own validation).",
    )
    p_submit_help.add_argument(
        "kind",
        nargs="?",
        default=None,
        help=f"submit kind to describe; omit for the full index. one of: {sorted(SUBMIT_HANDLERS)}",
    )
    p_submit_help.set_defaults(fn=cmd_submit_help)

    p_validate = sub.add_parser("validate", help="Validate substrate integrity.")
    p_validate.add_argument("--precommit", action="store_true")
    p_validate.set_defaults(fn=cmd_validate)

    p_elig = sub.add_parser("subtract-eligibility", help="Eligibility report for human reviewer-subtractor.")
    p_elig.add_argument("--uncited-threshold", type=int, default=10)
    p_elig.add_argument("--stale-threshold", type=int, default=5)
    p_elig.add_argument("--untriaged-threshold", type=int, default=3)
    p_elig.set_defaults(fn=cmd_subtract_eligibility)

    p_rec = sub.add_parser("recover", help="Reclaim expired work_item leases.")
    p_rec.set_defaults(fn=cmd_recover)

    p_q = sub.add_parser("query", help="Read-only SQL query (debugging).")
    p_q.add_argument("sql")
    p_q.add_argument("--pretty", action="store_true")
    p_q.set_defaults(fn=cmd_query)

    p_exp = sub.add_parser("export", help="Materialise markdown views from substrate rows (engine-v20+).")
    p_exp.add_argument("--session", type=int, help="Session number to export.")
    p_exp.add_argument("--issues", action="store_true", help="Export the issues table to open-issues/<alias>.md (engine-v22+).")
    p_exp.add_argument("--provenance", action="store_true", help="Cross-session anchor-trace export (OI-S114-1, DV-S116-1).")
    p_exp.add_argument("--anchor", type=str, default=None, help="Alias to root the anchor-trace at (use with --provenance).")
    p_exp.add_argument(
        "--max-depth",
        dest="max_depth",
        type=int,
        default=None,
        help=f"Chain-walk depth for anchor-trace (default {ANCHOR_TRACE_DEFAULT_DEPTH}, hard cap {ANCHOR_TRACE_HARD_CAP_DEPTH}).",
    )
    p_exp.add_argument("--write", action="store_true", help="Write files to disk (default: dry-run, print plan).")
    p_exp.add_argument(
        "--print",
        dest="print_stdout",
        action="store_true",
        help="Anchor-trace only: emit the markdown body to stdout (no JSON wrapper, no disk write). FR-S173-1.",
    )
    p_exp.set_defaults(fn=cmd_export)

    p_orient = sub.add_parser("orient", help="Print the workspace orientation packet (engine-v23+).")
    p_orient.add_argument("--json", dest="as_json", action="store_true", help="Emit JSON instead of markdown.")
    p_orient.set_defaults(fn=cmd_orient)

    p_pre = sub.add_parser(
        "precheck",
        help="Render decision-record context pack and write a single-use precheck receipt (T-33, engine-v49, DV-S179-1).",
    )
    p_pre.add_argument(
        "--target-kind",
        dest="target_kind",
        required=True,
        choices=["decision_v2"],
        help="Target kind (decision_v2 only at engine-v49).",
    )
    p_pre.add_argument(
        "--target-key",
        dest="target_key",
        required=True,
        help="Target key (typically the decision_v2 target_key the agent will submit).",
    )
    p_pre.add_argument(
        "--print",
        dest="print_stdout",
        action="store_true",
        help="Emit the rendered context body to stdout in addition to the receipt summary.",
    )
    p_pre.set_defaults(fn=cmd_precheck)

    p_schema = sub.add_parser("schema", help="Print substrate schema (live read from sqlite_master).")
    p_schema.add_argument("table", nargs="?", default=None, help="Optional table name to focus on.")
    p_schema.add_argument("--raw", action="store_true", help="Emit raw .schema DDL instead of formatted view.")
    p_schema.set_defaults(fn=cmd_schema)

    p_me = sub.add_parser(
        "monitor-external",
        help="Read a peer Selvedge workspace and harvest its engine-feedback (engine-v31, DV-S106-3).",
    )
    me_sub = p_me.add_subparsers(dest="monitor_sub", required=True)

    p_me_st = me_sub.add_parser("status", help="Print external workspace status (read-only).")
    p_me_st.add_argument("--workspace", required=True, help="Path to peer workspace root (must contain MODE.md and state/selvedge.sqlite).")
    p_me_st.add_argument("--json", dest="as_json", action="store_true", help="Emit JSON instead of markdown.")
    p_me_st.add_argument("--sessions-per-phase", type=int, default=3, help="Heuristic phase divisor (default 3).")
    p_me_st.set_defaults(fn=cmd_monitor_external)

    p_me_ni = me_sub.add_parser("next-input", help="Emit a JSON draft of the next session-input file.")
    p_me_ni.add_argument("--workspace", required=True, help="Path to peer workspace root.")
    p_me_ni.add_argument("--arc-plan", default=None, help="Path to the arc-plan markdown (optional, embedded in output).")
    p_me_ni.add_argument("--assumption-ledger", default=None, help="Path to assumption-ledger markdown (optional, embedded in output).")
    p_me_ni.add_argument("--phase", default=None, help="Phase identifier (operator-supplied).")
    p_me_ni.add_argument("--out", default=None, help="Write JSON to file path instead of stdout.")
    p_me_ni.set_defaults(fn=cmd_monitor_external)

    p_me_he = me_sub.add_parser(
        "harvest-ef",
        help="Read peer engine_feedback rows substrate-direct and copy into THIS workspace's engine_feedback rows (idempotent via harvested_engine_feedback ledger).",
    )
    p_me_he.add_argument("--workspace", required=True, help="Path to peer workspace root.")
    p_me_he.add_argument("--since-session", type=int, default=None, help="Optional coarse filter: skip rows whose peer workspace_session_no is <= N.")
    p_me_he.add_argument("--dry-run", action="store_true", help="Print harvest plan without writing rows.")
    p_me_he.add_argument("--role", default="__cli__")
    p_me_he.set_defaults(fn=cmd_monitor_external)

    p_fb = sub.add_parser(
        "feedback",
        help=(
            "Record an engine-feedback row; if no session is open, "
            "wrap the EF in a meta intake session (DV-S122-1)."
        ),
        description=(
            "Records an engine-feedback row. If a session is already "
            "open, the EF is submitted into that session as a passthrough "
            "(intake_session=false) — appropriate when the EF arises from "
            "the work-in-progress. If no session is open, the wrapper "
            "opens a kind=meta intake session, submits the EF, writes a "
            "minimal close-record, and closes the session in one "
            "write_tx (intake_session=true)."
        ),
    )
    p_fb.add_argument(
        "body",
        help="EF body markdown; '@file' to read from a file, '-' for stdin.",
    )
    p_fb.add_argument(
        "--flag",
        default="observation",
        choices=["observation", "reframe", "calibration", "blocker", "triage"],
        help="EF flag (default observation).",
    )
    p_fb.add_argument(
        "--slug",
        default=None,
        help=(
            "Override the auto-generated intake-session slug "
            "(default feedback-intake-<UTC-timestamp>); ignored if a "
            "session is already open."
        ),
    )
    p_fb.add_argument("--role", default="__cli__")
    p_fb.add_argument(
        "--dry-run",
        dest="dry_run",
        action="store_true",
        help=(
            "Run the wrapper inside a transaction that always rolls back "
            "(mirrors `submit --dry-run` semantics from DV-S120-1)."
        ),
    )
    p_fb.set_defaults(fn=cmd_feedback)

    args = parser.parse_args(argv)
    try:
        return args.fn(args)
    except SelvedgeError as e:
        print(json.dumps({"ok": False, "code": e.code, "detail": e.detail}), file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
