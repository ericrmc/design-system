"""`selvedge export` — materialise markdown projections from substrate rows.

Three modes:
  --session <N>             — per-session provenance directory
  --issues                  — open-issues/ regeneration
  --provenance --anchor X   — cross-session anchor trace (DV-S116-1)
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..paths import ANCHOR_TRACE_DEFAULT_DEPTH, db_path
from .anchor import _export_provenance_anchor
from .issues import _export_issues
from .session import _export_session_provenance
from .spec_versions import _export_spec_versions


def cmd_export(args) -> int:
    print_stdout = getattr(args, "print_stdout", False)
    if print_stdout and not args.provenance:
        print("export --print: only valid with --provenance --anchor (FR-S173-1)", file=sys.stderr)
        return 2
    if print_stdout and args.write:
        print("export --print and --write are mutually exclusive", file=sys.stderr)
        return 2
    conn = sqlite3.connect(str(db_path()))
    conn.row_factory = sqlite3.Row
    try:
        if args.provenance:
            if not args.anchor:
                print("export --provenance: pass --anchor <alias>", file=sys.stderr)
                return 2
            depth = args.max_depth if args.max_depth is not None else ANCHOR_TRACE_DEFAULT_DEPTH
            result = _export_provenance_anchor(conn, args.anchor, max_depth=depth, write=args.write)
            if print_stdout:
                sys.stdout.write(result["preview"])
            else:
                print(json.dumps({k: v for k, v in result.items() if k != "preview"}, indent=2))
                if result.get("dry_run") and result.get("preview"):
                    print("\n--- preview ---\n")
                    print(result["preview"])
        elif args.issues:
            result = _export_issues(conn, write=args.write)
            print(json.dumps(result, indent=2))
        elif args.session is not None:
            result = _export_session_provenance(conn, args.session, write=args.write)
            # L5 close-time export expansion (OI-S081-6 / DV-S081-1): the close-
            # ceremony command (`selvedge export --session N --write`) is the
            # single entry point at session-close, so trigger the workspace-
            # wide regen of the open-issues index and the spec_versions index
            # in the same invocation. Both are deterministic re-renders of
            # current substrate state; no-op safe under --dry-run.
            issues_result = _export_issues(conn, write=args.write)
            spec_versions_result = _export_spec_versions(conn, write=args.write)
            result["issues_export"] = issues_result
            result["spec_versions_export"] = spec_versions_result
            print(json.dumps(result, indent=2))
        else:
            print("export: pass --session <N>, --issues, or --provenance --anchor <alias>", file=sys.stderr)
            return 2
    finally:
        conn.close()
    return 0
