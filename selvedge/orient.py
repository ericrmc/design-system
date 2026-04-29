"""`selvedge orient` — live read of substrate state for session orientation."""

from __future__ import annotations

import json
import sqlite3

from .paths import FR_ANY_ALIAS_RE, FR_ISSUE_CITE_RE, FR_NULL_STATE_RE, db_path


def _orient_sections(conn: sqlite3.Connection) -> dict:
    """Gather the orientation packet as a dict of named sections.

    Used by cmd_orient. Each section is a list of dicts (or scalar) so the
    output can be rendered as either markdown or JSON without losing structure.
    """
    out: dict = {}
    out["workspace"] = {
        r["key"]: r["value"]
        for r in conn.execute("SELECT key, value FROM workspace_metadata").fetchall()
    }
    out["recent_close_records"] = [
        dict(r) for r in conn.execute(
            "SELECT s.workspace_session_no, s.slug, s.engine_version_at_close, s.closed_at, "
            "       cr.close_record_id "
            "FROM close_records cr JOIN sessions s ON s.session_id=cr.session_id "
            "ORDER BY s.session_no DESC LIMIT 3"
        ).fetchall()
    ]
    # Forward references: every undisposed close_state_item with
    # facet='next_session_should' across the full history. Disposition rows
    # in forward_reference_dispositions remove the item from the queue.
    fr_rows = conn.execute(
        "SELECT csi.seq, csi.state_item_id, ta.text AS text, "
        "       COALESCE(s.workspace_session_no, s.session_no) AS wno "
        "FROM close_state_items csi "
        "JOIN text_atoms ta ON ta.atom_id=csi.item_atom_id "
        "JOIN close_records cr ON cr.close_record_id=csi.close_record_id "
        "JOIN sessions s ON s.session_id=cr.session_id "
        "WHERE csi.facet='next_session_should' "
        "  AND NOT EXISTS (SELECT 1 FROM forward_reference_dispositions frd "
        "                  WHERE frd.state_item_id=csi.state_item_id) "
        "ORDER BY s.session_no DESC, csi.seq"
    ).fetchall()
    out["next_session_should_total"] = len(fr_rows)
    out["next_session_should"] = [
        {
            "from_session": f"S{r['wno']:03d}",
            "seq": r["seq"],
            "ref": f"FR-S{r['wno']:03d}-{r['seq']}",
            "text": r["text"],
        }
        for r in fr_rows[:30]
    ]
    out["next_session_should_truncated"] = len(fr_rows) > 30
    # Rot annotation per DV-S101-1: each FR text is scanned for OI- issue
    # aliases via regex; cites whose target issue is resolved/superseded or
    # absent become a `rot` list on the FR.
    fr_cite_aliases: list[str] = []
    fr_cites: list[list[str]] = []
    for item in out["next_session_should"]:
        item["rot"] = []
        seen: list[str] = []
        for m in FR_ISSUE_CITE_RE.findall(item["text"]):
            if m not in seen:
                seen.append(m)
            if m not in fr_cite_aliases:
                fr_cite_aliases.append(m)
        fr_cites.append(seen)
    if fr_cite_aliases:
        placeholders = ",".join("?" * len(fr_cite_aliases))
        status_rows = conn.execute(
            f"SELECT alias, status FROM issues WHERE alias IN ({placeholders})",
            tuple(fr_cite_aliases),
        ).fetchall()
        status_by_alias = {r["alias"]: r["status"] for r in status_rows}
        LIVE_STATUSES = {"open", "in_progress", "blocked"}
        for item, cites in zip(out["next_session_should"], fr_cites):
            for alias in cites:
                status = status_by_alias.get(alias)
                if status is None:
                    item["rot"].append({"alias": alias, "status": "absent"})
                elif status not in LIVE_STATUSES:
                    item["rot"].append({"alias": alias, "status": status})
    # Null-state annotation (DV-S128-1, closes OI-S126-4): flag FR items
    # whose text matches a queue-selector phrase pattern AND carries no
    # citable alias of any form. Pure-placeholder items accumulate in the
    # queue indefinitely because they never name a concrete referent to
    # dispose against; the flag surfaces them for §8.5 disposition.
    for item in out["next_session_should"]:
        text = item["text"]
        item["null_state"] = bool(
            FR_NULL_STATE_RE.search(text) and not FR_ANY_ALIAS_RE.search(text)
        )
    open_issues_rows = conn.execute(
        "SELECT i.alias, i.priority, i.status, ta.text AS title "
        "FROM issues i JOIN text_atoms ta ON ta.atom_id=i.title_atom_id "
        "WHERE i.status IN ('open','in_progress','blocked') "
        "ORDER BY CASE i.priority WHEN 'HIGH' THEN 0 WHEN 'MEDIUM' THEN 1 ELSE 2 END, "
        "         i.surfaced_session_id"
    ).fetchall()
    out["open_issues_total"] = len(open_issues_rows)
    out["open_issues"] = [dict(r) for r in open_issues_rows[:30]]
    out["open_issues_truncated"] = len(open_issues_rows) > 30
    out["in_flight_work_items"] = [
        dict(r) for r in conn.execute(
            "SELECT work_item_id, kind, status, leased_by, lease_expires_at "
            "FROM work_items WHERE status IN ('queued','leased','failed') ORDER BY work_item_id"
        ).fetchall()
    ]
    out["active_specs"] = [
        dict(r) for r in conn.execute(
            "SELECT spec_id, version, body_canonical_in_substrate FROM spec_versions "
            "WHERE status='active' ORDER BY spec_id"
        ).fetchall()
    ]
    # Recent supersessions: surface the rationale for spec_version status
    # transitions to superseded (OI-S110-1). Joins decision_effects whose
    # target_object_id resolves to a spec_version object. Effects without
    # object linkage are not reachable here; the count is reported so
    # OI-S110-3's backfill scope stays visible from orient.
    out["recent_supersessions"] = [
        dict(r) for r in conn.execute(
            "SELECT COALESCE(s.workspace_session_no, s.session_no) AS wno, "
            "       dv.decision_no, "
            "       ta.text AS decision_title, sv.spec_id, sv.version "
            "FROM decision_effects de "
            "JOIN decisions_v2 dv ON dv.decision_v2_id=de.decision_v2_id "
            "JOIN sessions s ON s.session_id=dv.session_id "
            "JOIN text_atoms ta ON ta.atom_id=dv.title_atom_id "
            "JOIN objects o ON o.object_id=de.target_object_id "
            "JOIN spec_versions sv ON sv.spec_version_id=o.typed_row_id "
            "WHERE de.effect_kind='supersedes' AND o.object_kind='spec_version' "
            "ORDER BY de.effect_id DESC LIMIT 10"
        ).fetchall()
    ]
    out["unlinked_supersedes_count"] = conn.execute(
        "SELECT COUNT(*) FROM decision_effects "
        "WHERE effect_kind='supersedes' AND target_object_id IS NULL"
    ).fetchone()[0]
    backfill_row = conn.execute(
        "SELECT alias, status FROM issues WHERE alias='OI-S110-3'"
    ).fetchone()
    if backfill_row and backfill_row["status"] in ("open", "in_progress", "blocked"):
        out["unlinked_supersedes_pointer"] = backfill_row["alias"]
    else:
        out["unlinked_supersedes_pointer"] = None
    out["deferred_decisions"] = [
        dict(r) for r in conn.execute(
            "SELECT s.workspace_session_no, dv.decision_no, ta.text AS title "
            "FROM decisions_v2 dv JOIN sessions s ON s.session_id=dv.session_id "
            "JOIN text_atoms ta ON ta.atom_id=dv.title_atom_id "
            "WHERE dv.outcome_type='defer' ORDER BY dv.decision_v2_id DESC LIMIT 10"
        ).fetchall()
    ]
    out["open_findings"] = [
        dict(r) for r in conn.execute(
            "SELECT review_finding_id, severity, ta.text AS finding "
            "FROM review_findings rf JOIN text_atoms ta ON ta.atom_id=rf.finding_atom_id "
            "WHERE rf.disposition='open' AND rf.severity IN ('critical','high','medium') "
            "ORDER BY review_finding_id"
        ).fetchall()
    ]
    feedback_rows = conn.execute(
        "SELECT ef.feedback_id, ef.flag, ef.body_md, "
        "       o.alias, "
        "       s.workspace_session_no AS surfaced_in "
        "FROM engine_feedback ef "
        "LEFT JOIN objects o ON o.object_id=ef.object_id "
        "JOIN sessions s ON s.session_id=ef.session_id "
        "WHERE ef.disposition IS NULL "
        "ORDER BY ef.feedback_id DESC"
    ).fetchall()
    out["untriaged_feedback_total"] = len(feedback_rows)

    def _first_nonempty_line(text: str) -> str:
        for line in (text or "").splitlines():
            stripped = line.strip()
            if stripped:
                return stripped[:120]
        return ""

    out["untriaged_feedback"] = [
        {
            "alias": r["alias"] or f"feedback_id={r['feedback_id']}",
            "flag": r["flag"],
            "surfaced_in": r["surfaced_in"],
            "head": _first_nonempty_line(r["body_md"]),
        }
        for r in feedback_rows[:20]
    ]
    out["untriaged_feedback_truncated"] = len(feedback_rows) > 20
    out["unapplied_migrations"] = []
    return out


def _orient_markdown(packet: dict) -> str:
    lines = [
        "# Workspace orientation",
        "",
        "Generated by `bin/selvedge orient`. Substrate is canonical; this packet is a live read.",
        "",
    ]
    ws = packet["workspace"]
    lines.append("## Workspace")
    lines.append("")
    for k, v in ws.items():
        lines.append(f"- **{k}**: {v}")
    lines.append("")

    lines.append("## Recent sessions (last 3)")
    lines.append("")
    if packet["recent_close_records"]:
        lines.append("| Session | Slug | Engine | Closed at |")
        lines.append("|---------|------|--------|-----------|")
        for r in packet["recent_close_records"]:
            lines.append(
                f"| S{r['workspace_session_no']:03d} | {r['slug']} | "
                f"{r['engine_version_at_close']} | {r['closed_at']} |"
            )
        lines.append("")
    else:
        lines.append("(no closed sessions)")
        lines.append("")

    fr_total = packet.get("next_session_should_total", len(packet["next_session_should"]))
    lines.append(f"## Forward references ({len(packet['next_session_should'])} of {fr_total} undisposed)")
    lines.append("")
    if packet["next_session_should"]:
        for item in packet["next_session_should"]:
            suffix = ""
            if item.get("rot"):
                parts = [f"{r['alias']}: {r['status']}" for r in item["rot"]]
                suffix += f" [rot: {', '.join(parts)}]"
            if item.get("null_state"):
                suffix += " [null-state]"
            lines.append(f"- {item['ref']} {item['text']}{suffix}")
        if packet.get("next_session_should_truncated"):
            lines.append("")
            lines.append(
                f"_{fr_total - len(packet['next_session_should'])} more elided. "
                "Dispose via `bin/selvedge submit forward-reference-disposition --payload "
                "'{{\"target_session\": <wno>, \"seq\": <n>, \"note\": \"...\"}}'`._"
            )
    else:
        lines.append("(none)")
    lines.append("")

    total = packet.get("open_issues_total", len(packet["open_issues"]))
    lines.append(f"## Open issues ({len(packet['open_issues'])} of {total})")
    lines.append("")
    if packet["open_issues"]:
        lines.append("| Alias | Priority | Status | Title |")
        lines.append("|-------|----------|--------|-------|")
        for r in packet["open_issues"]:
            lines.append(f"| {r['alias']} | {r['priority']} | {r['status']} | {r['title']} |")
        if packet.get("open_issues_truncated"):
            lines.append("")
            lines.append(
                f"_{total - len(packet['open_issues'])} more issues elided. "
                "Run `bin/selvedge query \"SELECT alias, priority, status FROM issues "
                "WHERE status IN ('open','in_progress','blocked')\"` for the full list._"
            )
    else:
        lines.append("(none)")
    lines.append("")

    lines.append(f"## In-flight work_items ({len(packet['in_flight_work_items'])})")
    lines.append("")
    if packet["in_flight_work_items"]:
        lines.append("| ID | Kind | Status | Leased by | Lease expires |")
        lines.append("|----|------|--------|-----------|---------------|")
        for r in packet["in_flight_work_items"]:
            lines.append(
                f"| {r['work_item_id']} | {r['kind']} | {r['status']} | "
                f"{r['leased_by'] or ''} | {r['lease_expires_at'] or ''} |"
            )
    else:
        lines.append("(none)")
    lines.append("")

    lines.append("## Active specs")
    lines.append("")
    lines.append("| Spec | Version | Canonical-in-substrate |")
    lines.append("|------|---------|------------------------|")
    for r in packet["active_specs"]:
        lines.append(f"| {r['spec_id']} | {r['version']} | {r['body_canonical_in_substrate']} |")
    lines.append("")

    sup = packet.get("recent_supersessions", [])
    unlinked = packet.get("unlinked_supersedes_count", 0)
    pointer = packet.get("unlinked_supersedes_pointer")
    lines.append(f"## Recent supersessions ({len(sup)})")
    lines.append("")
    if sup:
        lines.append("| Decision | Spec | Version | Title |")
        lines.append("|----------|------|---------|-------|")
        for r in sup:
            alias = f"DV-S{r['wno']:03d}-{r['decision_no']}"
            title = (r["decision_title"] or "").replace("|", "\\|")
            spec_id = (r["spec_id"] or "").replace("|", "\\|")
            lines.append(f"| {alias} | {spec_id} | {r['version']} | {title} |")
    else:
        lines.append("(none)")
    if unlinked:
        lines.append("")
        if pointer:
            lines.append(
                f"_{unlinked} supersedes effect(s) lack target_object_id and are not reachable here; "
                f"see {pointer} for backfill scope._"
            )
        else:
            lines.append(
                f"_{unlinked} supersedes effect(s) lack target_object_id and are not reachable here; "
                "raw SQL on decision_effects required for those._"
            )
    lines.append("")

    lines.append(f"## Deferred decisions ({len(packet['deferred_decisions'])})")
    lines.append("")
    if packet["deferred_decisions"]:
        for r in packet["deferred_decisions"]:
            lines.append(f"- DV-S{r['workspace_session_no']:03d}-{r['decision_no']}: {r['title']}")
    else:
        lines.append("(none)")
    lines.append("")

    lines.append(f"## Open review findings ({len(packet['open_findings'])})")
    lines.append("")
    if packet["open_findings"]:
        for r in packet["open_findings"]:
            lines.append(f"- [{r['severity']}] {r['finding']}")
    else:
        lines.append("(none)")
    lines.append("")

    fb_total = packet.get("untriaged_feedback_total", len(packet.get("untriaged_feedback", [])))
    fb = packet.get("untriaged_feedback", [])
    lines.append(f"## Untriaged engine feedback ({len(fb)} of {fb_total})")
    lines.append("")
    if fb:
        lines.append("| Alias | Flag | Surfaced | Head |")
        lines.append("|-------|------|----------|------|")
        for r in fb:
            surfaced = f"S{r['surfaced_in']:03d}" if r["surfaced_in"] is not None else ""
            head = (r["head"] or "").replace("|", "\\|")
            lines.append(f"| {r['alias']} | {r['flag']} | {surfaced} | {head} |")
        if packet.get("untriaged_feedback_truncated"):
            lines.append("")
            lines.append(
                f"_{fb_total - len(fb)} more untriaged feedback rows elided. "
                "Run `bin/selvedge query \"SELECT feedback_id, flag, body_md FROM engine_feedback "
                "WHERE disposition IS NULL\"` for the full list._"
            )
        lines.append("")
        lines.append(
            "_Triage via `bin/selvedge submit engine-feedback-disposition --payload "
            "'{\"alias\": \"EF-...\", \"disposition\": \"...\"}'`._"
        )
    else:
        lines.append("(none)")
    lines.append("")
    return "\n".join(lines)


def cmd_orient(args) -> int:
    conn = sqlite3.connect(str(db_path()))
    conn.row_factory = sqlite3.Row
    try:
        packet = _orient_sections(conn)
    finally:
        conn.close()
    if args.as_json:
        print(json.dumps(packet, indent=2, default=str))
    else:
        print(_orient_markdown(packet))
    return 0
