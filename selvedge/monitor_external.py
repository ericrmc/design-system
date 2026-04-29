"""`selvedge monitor-external` — read peer Selvedge workspace, harvest engine_feedback.

Three subcommands operate against a peer Selvedge workspace given by
--workspace <path>. `status` and `next-input` read the peer's substrate
read-only via SQLite URI. `harvest-ef` reads engine_feedback rows directly
from the peer's substrate (engine-v26+ substrate-only-writes) and copies
them into THIS workspace's substrate via the existing `submit
engine-feedback` handler, recording per-row provenance in a
harvested_engine_feedback ledger so re-runs are idempotent at row precision.
"""

from __future__ import annotations

import json
import os
import sqlite3
import sys
import time
import urllib.parse
from pathlib import Path

from .connection import Conn
from .errors import SelvedgeError
from .paths import WORKSPACE_ROOT_ENV, workspace_root
from .submit import SUBMIT_HANDLERS
from .submit._helpers import _atom_session_id, _check_role_capability


def _me_validate_external(workspace_arg: str) -> tuple[Path, Path]:
    """Resolve and validate an external workspace path. Refuse if it points at
    THIS workspace (so harvest-ef cannot accidentally write to its source).

    Per S108 review F-87, the self-vs-peer guard uses inode equality
    (`Path.samefile`) so it survives macOS case-insensitive filesystems and
    symlinks where two distinct path strings refer to the same directory.
    """
    if not workspace_arg:
        raise SelvedgeError("E_BAD_ARG", "--workspace is required")
    root = Path(workspace_arg).expanduser().resolve()
    if not root.exists():
        raise SelvedgeError("E_NO_WORKSPACE", f"path does not exist: {root}")
    if not root.is_dir():
        raise SelvedgeError("E_NO_WORKSPACE", f"not a directory: {root}")
    if not (root / "MODE.md").exists():
        raise SelvedgeError("E_NO_WORKSPACE", f"missing MODE.md: {root}")
    db = root / "state" / "selvedge.sqlite"
    if not db.exists():
        raise SelvedgeError("E_NO_WORKSPACE", f"missing substrate: {db}")
    try:
        self_root = workspace_root()
    except SelvedgeError:
        self_root = None
    if self_root is not None and self_root.exists() and root.samefile(self_root):
        raise SelvedgeError(
            "E_REFUSAL_SELF",
            f"--workspace points at this workspace ({root}); "
            "monitor-external requires a peer workspace",
        )
    return root, db


def _me_open_external_ro(db: Path) -> sqlite3.Connection:
    """Open the external substrate read-only via a SQLite URI.

    Per S108 review F-83, the path component is URL-quoted because SQLite's
    URI parser treats `?`, `#`, and `&` as URI delimiters; a peer workspace
    whose absolute path contains those characters would otherwise fail to
    open with a misleading "no such table" error.
    """
    quoted = urllib.parse.quote(str(db), safe="/")
    conn = sqlite3.connect(f"file:{quoted}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA busy_timeout = 1000")
    conn.execute("PRAGMA query_only = 1")
    return conn


def _me_iso_utc(ts: float) -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(ts))


def _me_collect_close(conn: sqlite3.Connection) -> dict:
    """Read the latest close_record's summary + next_session_should atoms."""
    row = conn.execute(
        "SELECT cr.close_record_id, "
        "       COALESCE(s.workspace_session_no, s.session_no) AS wno, "
        "       ta_sum.text AS summary "
        "FROM close_records cr "
        "JOIN sessions s ON s.session_id=cr.session_id "
        "JOIN text_atoms ta_sum ON ta_sum.atom_id=cr.summary_atom_id "
        "ORDER BY s.session_no DESC LIMIT 1"
    ).fetchone()
    if row is None:
        return {"workspace_session_no": None, "summary": None, "next_session_should": []}
    next_should = [
        r["text"] for r in conn.execute(
            "SELECT ta.text FROM close_state_items csi "
            "JOIN text_atoms ta ON ta.atom_id=csi.item_atom_id "
            "WHERE csi.close_record_id=? AND csi.facet='next_session_should' "
            "ORDER BY csi.seq",
            (row["close_record_id"],),
        ).fetchall()
    ]
    return {
        "workspace_session_no": row["wno"],
        "summary": row["summary"],
        "next_session_should": next_should,
    }


def _me_status(args) -> int:
    root, db = _me_validate_external(args.workspace)
    conn = _me_open_external_ro(db)
    try:
        meta = {r["key"]: r["value"] for r in conn.execute(
            "SELECT key, value FROM workspace_metadata"
        ).fetchall()}
        sessions = [dict(r) for r in conn.execute(
            "SELECT session_no, workspace_session_no, slug, kind, status, "
            "engine_version_at_open, engine_version_at_close, opened_at, closed_at "
            "FROM sessions ORDER BY session_no DESC LIMIT 5"
        ).fetchall()]
        oi_counts = {r["priority"]: r["n"] for r in conn.execute(
            "SELECT priority, COUNT(*) AS n FROM issues "
            "WHERE status='open' GROUP BY priority"
        ).fetchall()}
        latest_close = _me_collect_close(conn)
        ef_rows: list[dict] | None
        if conn.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='engine_feedback'"
        ).fetchone():
            ef_rows = [dict(r) for r in conn.execute(
                "SELECT ef.feedback_id, ef.flag, ef.disposition, "
                "       COALESCE(s.workspace_session_no, s.session_no) AS wno "
                "FROM engine_feedback ef "
                "JOIN sessions s ON s.session_id = ef.session_id "
                "ORDER BY ef.feedback_id DESC LIMIT 10"
            ).fetchall()]
        else:
            ef_rows = None
    finally:
        conn.close()

    spp = max(1, args.sessions_per_phase)
    latest_local_no = sessions[0]["session_no"] if sessions else 0
    phase_idx = max(0, latest_local_no - 1) // spp if latest_local_no else 0

    pkt = {
        "workspace_path": str(root),
        "workspace_metadata": meta,
        "recent_sessions": sessions,
        "open_issues_total": sum(oi_counts.values()),
        "open_issues_by_priority": oi_counts,
        "ef_rows": ef_rows,
        "latest_close": latest_close,
        "phase_heuristic": {
            "value": f"P{phase_idx}",
            "sessions_per_phase": spp,
            "method": (
                "floor((latest_substrate_session_no - 1) / sessions_per_phase); "
                "uses local session_no so init_session_offset does not skew arc-phase"
            ),
        },
    }
    if args.as_json:
        print(json.dumps(pkt, indent=2, default=str))
    else:
        print(_me_render_status_md(pkt))
    return 0


def _me_render_status_md(pkt: dict) -> str:
    lines: list[str] = []
    lines.append("# monitor-external status")
    lines.append("")
    lines.append(f"- **workspace_path**: {pkt['workspace_path']}")
    for k in ("workspace_id", "mode", "current_engine_version"):
        if k in pkt["workspace_metadata"]:
            lines.append(f"- **{k}**: {pkt['workspace_metadata'][k]}")
    lines.append("")
    lines.append(f"## Recent sessions ({len(pkt['recent_sessions'])})")
    lines.append("")
    if pkt["recent_sessions"]:
        lines.append("| Session | Slug | Kind | Status | Engine open | Engine close | Closed at |")
        lines.append("|---------|------|------|--------|-------------|--------------|-----------|")
        for s in pkt["recent_sessions"]:
            wno = s.get("workspace_session_no") or s["session_no"]
            lines.append(
                f"| S{wno:03d} | {s['slug']} | {s['kind']} | {s['status']} | "
                f"{s['engine_version_at_open']} | {s.get('engine_version_at_close') or ''} | "
                f"{s.get('closed_at') or ''} |"
            )
    else:
        lines.append("(no sessions yet)")
    lines.append("")
    lines.append(f"## Open issues ({pkt['open_issues_total']})")
    lines.append("")
    if pkt["open_issues_by_priority"]:
        for prio in ("HIGH", "MEDIUM", "LOW"):
            n = pkt["open_issues_by_priority"].get(prio)
            if n:
                lines.append(f"- {prio}: {n}")
    else:
        lines.append("(none)")
    lines.append("")
    lines.append("## Engine-feedback (peer substrate, last 10)")
    lines.append("")
    rows = pkt.get("ef_rows")
    if rows is None:
        lines.append("(peer schema does not expose engine_feedback table)")
    elif rows:
        for r in rows:
            disp = f" — disposed: {r['disposition']}" if r.get("disposition") else ""
            lines.append(
                f"- feedback_id={r['feedback_id']} S{r['wno']:03d} "
                f"flag={r['flag']}{disp}"
            )
    else:
        lines.append("(no engine_feedback rows in peer substrate)")
    lines.append("")
    lines.append("## Latest close-record next_session_should")
    lines.append("")
    lc = pkt["latest_close"]
    if lc["next_session_should"]:
        lines.append(f"- close from S{lc['workspace_session_no']:03d}")
        for item in lc["next_session_should"]:
            lines.append(f"  - {item}")
    else:
        lines.append("(no closed session with next_session_should yet)")
    lines.append("")
    lines.append("## Phase heuristic")
    lines.append("")
    ph = pkt["phase_heuristic"]
    lines.append(f"- **value**: {ph['value']} (sessions_per_phase={ph['sessions_per_phase']})")
    lines.append(f"- method: {ph['method']}")
    lines.append("")
    return "\n".join(lines)


def _me_next_input(args) -> int:
    root, db = _me_validate_external(args.workspace)

    def _read_optional(path_arg: str | None, label: str) -> tuple[str | None, str | None]:
        if not path_arg:
            return None, None
        p = Path(path_arg).expanduser().resolve()
        if not p.exists():
            raise SelvedgeError("E_NO_FILE", f"{label} not found: {p}")
        return str(p), p.read_text()

    arc_plan_path, arc_plan_excerpt = _read_optional(args.arc_plan, "arc-plan")
    ledger_path, ledger_excerpt = _read_optional(args.assumption_ledger, "assumption-ledger")

    conn = _me_open_external_ro(db)
    try:
        latest_session = conn.execute(
            "SELECT session_no, workspace_session_no, slug, kind, status, closed_at "
            "FROM sessions ORDER BY session_no DESC LIMIT 1"
        ).fetchone()
        latest_close = _me_collect_close(conn)
        open_oi = [r["alias"] for r in conn.execute(
            "SELECT alias FROM issues WHERE status='open' "
            "ORDER BY CASE priority WHEN 'HIGH' THEN 0 WHEN 'MEDIUM' THEN 1 ELSE 2 END, alias"
        ).fetchall()]
    finally:
        conn.close()

    if latest_session is None:
        next_session_no = 1
        next_workspace_session_no = 1
    else:
        next_session_no = latest_session["session_no"] + 1
        next_workspace_session_no = (
            latest_session["workspace_session_no"] or latest_session["session_no"]
        ) + 1

    out = {
        "external_workspace": str(root),
        "phase": args.phase,
        "next_external_session_no": next_session_no,
        "next_external_workspace_session_no": next_workspace_session_no,
        "latest_close": latest_close,
        "open_issue_aliases": open_oi,
        "arc_plan_path": arc_plan_path,
        "arc_plan_excerpt": arc_plan_excerpt,
        "assumption_ledger_path": ledger_path,
        "assumption_ledger_excerpt": ledger_excerpt,
        "draft_session_input": {
            "phase": args.phase,
            "carry_forward_from_close": latest_close["next_session_should"],
            "operator_must_fill": [
                "reveal_axis",
                "domain_facts",
                "specific_assumption_ids_to_revise",
                "session_input_md_body",
            ],
            "note": (
                "This is a JSON drafting buffer per DV-S106-3. The operator reviews and "
                "edits before placing the final session-input markdown in the external "
                "workspace's applications/<slug>/session-inputs/ directory."
            ),
        },
    }
    payload = json.dumps(out, indent=2, default=str)
    if args.out:
        out_path = Path(args.out).expanduser().resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(payload)
        print(json.dumps({"ok": True, "wrote": str(out_path), "bytes": len(payload)}))
    else:
        print(payload)
    return 0


def _me_read_peer_ef(peer_db: Path) -> tuple[str, list[dict]]:
    """Read the peer's engine_feedback rows substrate-direct.

    Returns (peer_workspace_id, rows). Each row dict has feedback_id, peer_wno,
    peer_slug, flag, body_md, peer_alias (or None if peer schema lacks objects
    or the row has no object_id).
    """
    try:
        conn = _me_open_external_ro(peer_db)
    except sqlite3.OperationalError as e:
        msg = str(e)
        if "database is locked" in msg or "database is busy" in msg:
            raise SelvedgeError("E_PEER_BUSY", f"peer substrate busy: {e}")
        raise SelvedgeError("E_PEER_OPEN_FAILED", f"could not open peer substrate: {e}")

    def _peer_exec(sql: str, params: tuple = ()):
        try:
            return conn.execute(sql, params).fetchall()
        except sqlite3.OperationalError as e:
            msg = str(e)
            if "database is locked" in msg or "database is busy" in msg:
                raise SelvedgeError("E_PEER_BUSY", f"peer substrate query busy: {e}")
            raise SelvedgeError("E_PEER_QUERY_FAILED", f"peer substrate query failed: {e}")

    try:
        if not _peer_exec(
            "SELECT 1 FROM sqlite_master "
            "WHERE type='table' AND name='engine_feedback'"
        ):
            raise SelvedgeError(
                "E_PEER_SCHEMA_UNSUPPORTED",
                "peer substrate has no engine_feedback table; harvest-ef requires "
                "engine-v17+ with the engine_feedback table present",
            )
        meta_rows = _peer_exec(
            "SELECT value FROM workspace_metadata WHERE key='workspace_id'"
        )
        if not meta_rows or not meta_rows[0]["value"]:
            raise SelvedgeError(
                "E_PEER_SCHEMA_UNSUPPORTED",
                "peer workspace_metadata.workspace_id is missing; required to key "
                "the harvested_engine_feedback ledger uniquely",
            )
        peer_ws_id = str(meta_rows[0]["value"])
        has_objects_alias = bool(_peer_exec(
            "SELECT 1 FROM pragma_table_info('objects') WHERE name='alias'"
        ))
        has_objects_citable = bool(_peer_exec(
            "SELECT 1 FROM pragma_table_info('objects') WHERE name='citable_alias'"
        ))
        alias_col_sql: str | None
        if has_objects_alias:
            alias_col_sql = "o.alias"
        elif has_objects_citable:
            alias_col_sql = "o.citable_alias"
        else:
            alias_col_sql = None

        if alias_col_sql:
            sql = (
                "SELECT ef.feedback_id, "
                "       COALESCE(s.workspace_session_no, s.session_no) AS peer_wno, "
                "       s.slug AS peer_slug, "
                "       ef.flag, ef.body_md, "
                f"       {alias_col_sql} AS peer_alias "
                "FROM engine_feedback ef "
                "JOIN sessions s ON s.session_id = ef.session_id "
                "LEFT JOIN objects o ON o.object_id = ef.object_id "
                "ORDER BY ef.feedback_id"
            )
        else:
            sql = (
                "SELECT ef.feedback_id, "
                "       COALESCE(s.workspace_session_no, s.session_no) AS peer_wno, "
                "       s.slug AS peer_slug, "
                "       ef.flag, ef.body_md, "
                "       NULL AS peer_alias "
                "FROM engine_feedback ef "
                "JOIN sessions s ON s.session_id = ef.session_id "
                "ORDER BY ef.feedback_id"
            )
        rows = [dict(r) for r in _peer_exec(sql)]
    finally:
        conn.close()
    return peer_ws_id, rows


def _me_harvest_ef(args) -> int:
    if WORKSPACE_ROOT_ENV not in os.environ:
        raise SelvedgeError(
            "E_REFUSAL_SELF",
            f"harvest-ef requires {WORKSPACE_ROOT_ENV} to be set so the self-dev "
            "write target is unambiguous; cwd-based workspace inference is too "
            "ambiguous for write operations across peer workspaces",
        )
    self_root = workspace_root()
    self_db = self_root / "state" / "selvedge.sqlite"
    if not self_db.exists():
        raise SelvedgeError("E_NO_WORKSPACE", f"missing self-dev substrate: {self_db}")
    root, peer_db = _me_validate_external(args.workspace)
    cwd_resolved = Path.cwd().resolve()
    if cwd_resolved == root or cwd_resolved.is_relative_to(root):
        raise SelvedgeError(
            "E_REFUSAL_SELF",
            f"refusing harvest-ef: current directory {cwd_resolved} is inside the peer "
            f"workspace {root}; run from the self-dev workspace so the write target is "
            "unambiguous",
        )

    peer_ws_id, peer_rows = _me_read_peer_ef(peer_db)

    self_conn = sqlite3.connect(str(self_db))
    self_conn.row_factory = sqlite3.Row
    try:
        ledger_existing: set[int] = {
            int(r["peer_feedback_id"])
            for r in self_conn.execute(
                "SELECT peer_feedback_id FROM harvested_engine_feedback "
                "WHERE peer_workspace_id=?",
                (peer_ws_id,),
            ).fetchall()
        }
    finally:
        self_conn.close()

    plan: list[dict] = []
    for r in peer_rows:
        fid = int(r["feedback_id"])
        wno = int(r["peer_wno"]) if r.get("peer_wno") is not None else None
        flag = r["flag"]
        entry: dict = {
            "peer_feedback_id": fid,
            "peer_wno": wno,
            "peer_slug": r.get("peer_slug"),
            "peer_alias": r.get("peer_alias"),
            "flag": flag,
        }
        if fid in ledger_existing:
            entry["action"] = "skip"
            entry["reason"] = "already-harvested (per peer_workspace_id, peer_feedback_id)"
            plan.append(entry)
            continue
        if (
            args.since_session is not None
            and wno is not None
            and wno <= args.since_session
        ):
            entry["action"] = "skip"
            entry["reason"] = f"session {wno} <= --since-session {args.since_session}"
            plan.append(entry)
            continue
        entry["action"] = "harvest"
        plan.append(entry)

    if args.dry_run:
        out = {
            "ok": True, "dry_run": True,
            "peer_workspace_id": peer_ws_id,
            "peer_rows_total": len(peer_rows),
            "plan": plan,
        }
        if not peer_rows:
            out["note"] = "peer substrate has no engine_feedback rows"
        print(json.dumps(out, indent=2))
        return 0

    bodies: dict[int, str] = {int(r["feedback_id"]): r["body_md"] for r in peer_rows}

    role = args.role or "__cli__"
    results: list[dict] = []
    c = Conn.open(self_db)
    try:
        for entry in plan:
            if entry["action"] != "harvest":
                results.append({**entry, "status": "skipped"})
                continue
            fid = entry["peer_feedback_id"]
            body = bodies[fid]
            wno = entry["peer_wno"]
            peer_alias = entry.get("peer_alias")
            preface_alias = f"alias `{peer_alias}`, " if peer_alias else ""
            preface = (
                f"_Harvested from peer substrate `{peer_ws_id}` "
                f"(peer feedback_id {fid}, {preface_alias}"
                f"external session S{wno:03d})._\n\n"
                if wno is not None
                else f"_Harvested from peer substrate `{peer_ws_id}` "
                f"(peer feedback_id {fid}, {preface_alias}external session unknown)._\n\n"
            )
            payload = {"flag": entry["flag"], "body_md": preface + body}
            try:
                def _do_harvest(conn, p=payload, fid=fid, peer_ws_id=peer_ws_id,
                                 peer_alias=peer_alias, role=role):
                    res = SUBMIT_HANDLERS["engine-feedback"](conn, p, role)
                    sess_id = _atom_session_id(conn, None)
                    _check_role_capability(
                        conn, role, "harvested_engine_feedback", "insert"
                    )
                    conn.execute(
                        "INSERT INTO harvested_engine_feedback "
                        "(peer_workspace_id, peer_feedback_id, peer_alias, "
                        " imported_object_id, session_id) "
                        "VALUES (?,?,?,?,?)",
                        (peer_ws_id, fid, peer_alias, res["object_id"], sess_id),
                    )
                    return res
                result = c.write_tx(_do_harvest)
                results.append({
                    **entry,
                    "status": "success",
                    "self_alias": result["alias"],
                    "self_object_id": result["object_id"],
                })
            except SelvedgeError as e:
                if e.code == "E_REFUSAL_UNIQUE" and "harvested_engine_feedback" in e.detail:
                    results.append({
                        **entry,
                        "status": "skipped",
                        "reason": "concurrent harvest already imported this peer row",
                    })
                else:
                    results.append({
                        **entry,
                        "status": "error",
                        "error": e.code,
                        "detail": e.detail,
                    })
            except Exception as e:  # noqa: BLE001 — surface to operator, never silent
                results.append({
                    **entry,
                    "status": "error",
                    "error": type(e).__name__,
                    "detail": str(e),
                })
    finally:
        c.close()
    out = {
        "ok": True, "dry_run": False,
        "peer_workspace_id": peer_ws_id,
        "peer_rows_total": len(peer_rows),
        "results": results,
    }
    if not peer_rows:
        out["note"] = "peer substrate has no engine_feedback rows"
    print(json.dumps(out, indent=2))
    return 0


def cmd_monitor_external(args) -> int:
    sub = args.monitor_sub
    if sub == "status":
        return _me_status(args)
    if sub == "next-input":
        return _me_next_input(args)
    if sub == "harvest-ef":
        return _me_harvest_ef(args)
    print(f"unknown monitor-external subcommand: {sub}", file=sys.stderr)
    return 2
