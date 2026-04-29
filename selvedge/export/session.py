"""Per-session provenance export: 00-assessment / 01-deliberation / 02-decisions / 03-close / 04-review."""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Optional

from ..errors import SelvedgeError


def _atom_text(conn: sqlite3.Connection, atom_id: Optional[int]) -> str:
    if atom_id is None:
        return ""
    row = conn.execute("SELECT text FROM text_atoms WHERE atom_id=?", (atom_id,)).fetchone()
    return row["text"] if row else ""


def _export_session_provenance(conn: sqlite3.Connection, session_ref: int, write: bool = False) -> dict:
    """Export a session by EITHER substrate session_no OR workspace_session_no.

    Looks up the session row via either column; uses workspace_session_no for
    the provenance directory name (e.g. provenance/084-<slug>/) so the file
    layout matches workspace conventions, not substrate counters.
    """
    sess = conn.execute(
        "SELECT session_id, session_no, workspace_session_no, slug, mode, "
        "       engine_version_at_open, engine_version_at_close, "
        "       opened_at, closed_at, status FROM sessions "
        "WHERE workspace_session_no=? OR session_no=? LIMIT 1",
        (session_ref, session_ref),
    ).fetchone()
    if sess is None:
        raise SelvedgeError("E_NOT_FOUND", f"session ref={session_ref} (tried workspace_session_no and session_no)")
    sid = sess["session_id"]
    workspace_no = sess["workspace_session_no"] or sess["session_no"]
    session_no = sess["session_no"]
    out_dir = Path("provenance") / f"{workspace_no:03d}-{sess['slug']}"
    files: dict[str, str] = {}

    # 00-assessment.md
    asm = conn.execute(
        "SELECT assessment_id, state_atom_id FROM assessments WHERE session_id=?",
        (sid,),
    ).fetchone()
    if asm:
        items = conn.execute(
            "SELECT ord, item_atom_id FROM assessment_agenda_items WHERE assessment_id=? ORDER BY ord",
            (asm["assessment_id"],),
        ).fetchall()
        lines = [
            "---",
            f"session: {workspace_no:03d}",
            f"title: {sess['slug']} — assessment",
            f"engine_version_at_open: {sess['engine_version_at_open']}",
            f"mode: {sess['mode']}",
            "generated_by: selvedge export",
            "---",
            "",
            "# Assessment",
            "",
            "## State at open",
            "",
            _atom_text(conn, asm["state_atom_id"]),
            "",
            "## Agenda",
            "",
        ]
        for it in items:
            lines.append(f"{it['ord']}. {_atom_text(conn, it['item_atom_id'])}")
        lines.append("")
        files["00-assessment.md"] = "\n".join(lines)

    # 01-deliberation.md
    delibs = conn.execute(
        "SELECT deliberation_id, topic, sealed_at, synthesis_md FROM deliberations WHERE session_id=? ORDER BY deliberation_id",
        (sid,),
    ).fetchall()
    if delibs:
        lines = [
            "---",
            f"session: {workspace_no:03d}",
            f"title: {sess['slug']} — deliberation",
            "generated_by: selvedge export",
            "---",
            "",
            "# Deliberation",
            "",
        ]
        for d in delibs:
            lines.append(f"## D-{d['deliberation_id']} — {d['topic']}")
            lines.append("")
            lines.append(f"sealed_at: {d['sealed_at']}")
            lines.append("")
            persp = conn.execute(
                "SELECT perspective_id, label, family FROM perspectives WHERE deliberation_id=? ORDER BY perspective_id",
                (d["deliberation_id"],),
            ).fetchall()
            for pe in persp:
                lines.append(f"### {pe['label']} ({pe['family']})")
                lines.append("")
                pos = conn.execute(
                    "SELECT position_atom_id FROM perspective_positions WHERE perspective_id=?",
                    (pe["perspective_id"],),
                ).fetchone()
                if pos:
                    lines.append(f"**Position.** {_atom_text(conn, pos['position_atom_id'])}")
                    lines.append("")
                claims = conn.execute(
                    "SELECT seq, section_kind, claim_atom_id FROM perspective_claims WHERE perspective_id=? ORDER BY seq",
                    (pe["perspective_id"],),
                ).fetchall()
                if claims:
                    cur_section = None
                    for c in claims:
                        if c["section_kind"] != cur_section:
                            cur_section = c["section_kind"]
                            lines.append(f"**{cur_section}.**")
                        lines.append(f"- {_atom_text(conn, c['claim_atom_id'])}")
                    lines.append("")
            if d["synthesis_md"]:
                lines.append("### Synthesis")
                lines.append("")
                lines.append(d["synthesis_md"])
                lines.append("")
            sps = conn.execute(
                "SELECT kind, label, summary FROM synthesis_points WHERE deliberation_id=? ORDER BY synthesis_point_id",
                (d["deliberation_id"],),
            ).fetchall()
            if sps:
                lines.append("### Synthesis points")
                lines.append("")
                for sp in sps:
                    lines.append(f"- **{sp['kind']} {sp['label']}.** {sp['summary']}")
                lines.append("")
        files["01-deliberation.md"] = "\n".join(lines)

    # 02-decisions.md
    dvs = conn.execute(
        "SELECT decision_v2_id, decision_no, kind, title_atom_id, outcome_type, target_kind, target_key "
        "FROM decisions_v2 WHERE session_id=? ORDER BY decision_no",
        (sid,),
    ).fetchall()
    legacy_ds = conn.execute(
        "SELECT decision_no, kind, title, body_md FROM decisions WHERE session_id=? ORDER BY decision_no",
        (sid,),
    ).fetchall()
    if dvs or legacy_ds:
        lines = [
            "---",
            f"session: {workspace_no:03d}",
            f"title: {sess['slug']} — decisions",
            "generated_by: selvedge export",
            "---",
            "",
            "# Decisions",
            "",
        ]
        for d in dvs:
            lines.append(f"## D-{d['decision_no']}. {_atom_text(conn, d['title_atom_id'])}")
            lines.append("")
            lines.append(
                f"**Kind:** {d['kind']}.  **Outcome:** {d['outcome_type']} {d['target_kind']} `{d['target_key']}`."
            )
            lines.append("")
            sups = conn.execute(
                "SELECT seq, basis, claim_atom_id, cited_object_id FROM decision_supports WHERE decision_v2_id=? ORDER BY seq",
                (d["decision_v2_id"],),
            ).fetchall()
            if sups:
                lines.append("**Why.**")
                lines.append("")
                for s in sups:
                    cite = ""
                    if s["cited_object_id"]:
                        c = conn.execute(
                            "SELECT alias FROM objects WHERE object_id=?", (s["cited_object_id"],)
                        ).fetchone()
                        if c and c["alias"]:
                            cite = f" [{c['alias']}]"
                    lines.append(f"- ({s['basis']}) {_atom_text(conn, s['claim_atom_id'])}{cite}")
                lines.append("")
            effs = conn.execute(
                "SELECT effect_kind, target_object_id, target_issue_id, target_descriptor FROM decision_effects WHERE decision_v2_id=? "
                "ORDER BY effect_id",
                (d["decision_v2_id"],),
            ).fetchall()
            if effs:
                lines.append("**Effects.**")
                lines.append("")
                for e in effs:
                    descriptor = e["target_descriptor"] or ""
                    alias = ""
                    if e["target_object_id"]:
                        c = conn.execute(
                            "SELECT alias FROM objects WHERE object_id=?", (e["target_object_id"],)
                        ).fetchone()
                        if c and c["alias"]:
                            alias = c["alias"]
                    elif e["target_issue_id"]:
                        c = conn.execute(
                            "SELECT alias FROM issues WHERE issue_id=?", (e["target_issue_id"],)
                        ).fetchone()
                        if c and c["alias"]:
                            alias = c["alias"]
                    if alias and descriptor:
                        lines.append(f"- {e['effect_kind']} {alias} — {descriptor}")
                    elif alias:
                        lines.append(f"- {e['effect_kind']} {alias}")
                    else:
                        lines.append(f"- {e['effect_kind']} {descriptor}")
                lines.append("")
            alts = conn.execute(
                "SELECT alternative_v2_id, label, option_atom_id FROM alternatives_v2 WHERE decision_v2_id=? ORDER BY alternative_v2_id",
                (d["decision_v2_id"],),
            ).fetchall()
            if alts:
                lines.append("**Rejected alternatives.**")
                lines.append("")
                for a in alts:
                    lines.append(f"- **{a['label']}.** {_atom_text(conn, a['option_atom_id'])}")
                    rejs = conn.execute(
                        "SELECT seq, basis, rejection_atom_id FROM alternative_rejections WHERE alternative_v2_id=? ORDER BY seq",
                        (a["alternative_v2_id"],),
                    ).fetchall()
                    for r in rejs:
                        lines.append(f"  - ({r['basis']}) {_atom_text(conn, r['rejection_atom_id'])}")
                lines.append("")
        if legacy_ds:
            lines.append("## Legacy decisions (pre-v20)")
            lines.append("")
            for d in legacy_ds:
                lines.append(f"### D-{d['decision_no']}. {d['title']}")
                lines.append("")
                lines.append(d["body_md"])
                lines.append("")
        files["02-decisions.md"] = "\n".join(lines)

    # 04-review.md
    rfs = conn.execute(
        "SELECT iteration, severity, finding_atom_id, target_object_id, disposition, disposition_atom_id "
        "FROM review_findings WHERE session_id=? ORDER BY iteration, review_finding_id",
        (sid,),
    ).fetchall()
    rps = conn.execute(
        "SELECT iteration, outcome, head_sha, summary_atom_id, halt_issue_id "
        "FROM review_passes WHERE session_id=? ORDER BY iteration",
        (sid,),
    ).fetchall()
    if rfs or rps:
        lines = [
            "---",
            f"session: {workspace_no:03d}",
            f"title: {sess['slug']} — review",
            "generated_by: selvedge export",
            "---",
            "",
            "# Reviewer audit",
            "",
        ]
        cur_iter = None
        for rf in rfs:
            if rf["iteration"] != cur_iter:
                cur_iter = rf["iteration"]
                lines.append(f"## Iteration {cur_iter}")
                lines.append("")
            cite = ""
            if rf["target_object_id"]:
                c = conn.execute(
                    "SELECT alias FROM objects WHERE object_id=?", (rf["target_object_id"],)
                ).fetchone()
                if c and c["alias"]:
                    cite = f" against `{c['alias']}`"
            lines.append(f"- **{rf['severity']}**{cite}: {_atom_text(conn, rf['finding_atom_id'])}")
            disp_text = (
                _atom_text(conn, rf["disposition_atom_id"])
                if rf["disposition_atom_id"] is not None
                else "(no disposition recorded)"
            )
            lines.append(f"  - **{rf['disposition']}.** {disp_text}")
        if rps:
            lines.append("")
            lines.append("## Terminal passes")
            lines.append("")
            for rp in rps:
                halt = ""
                if rp["halt_issue_id"]:
                    h = conn.execute(
                        "SELECT alias FROM issues WHERE issue_id=?", (rp["halt_issue_id"],)
                    ).fetchone()
                    if h and h["alias"]:
                        halt = f" (halt issue `{h['alias']}`)"
                lines.append(
                    f"- **iteration {rp['iteration']}** — {rp['outcome']}{halt} @ `{rp['head_sha'][:12]}`"
                )
                lines.append(f"  - {_atom_text(conn, rp['summary_atom_id'])}")
        lines.append("")
        files["04-review.md"] = "\n".join(lines)

    # 03-close.md
    cr = conn.execute(
        "SELECT close_record_id, summary_atom_id FROM close_records WHERE session_id=?",
        (sid,),
    ).fetchone()
    if cr:
        items = conn.execute(
            "SELECT seq, facet, item_atom_id FROM close_state_items WHERE close_record_id=? ORDER BY seq",
            (cr["close_record_id"],),
        ).fetchall()
        lines = [
            "---",
            f"session: {workspace_no:03d}",
            f"title: {sess['slug']} — close",
            f"engine_version_at_close: {sess['engine_version_at_close']}",
            f"mode: {sess['mode']}",
            "generated_by: selvedge export",
            "---",
            "",
            "# Close",
            "",
            "## Summary",
            "",
            _atom_text(conn, cr["summary_atom_id"]),
            "",
        ]
        cur_facet = None
        facet_titles = {
            "what_was_done": "What was done",
            "state_at_close": "State at close",
            "open_issues": "Open issues",
            "next_session_should": "What the next session should address",
            "engine_version": "Engine version",
            "validator_summary": "Validator at close",
        }
        for it in items:
            if it["facet"] != cur_facet:
                cur_facet = it["facet"]
                lines.append(f"## {facet_titles.get(cur_facet, cur_facet)}")
                lines.append("")
            lines.append(f"- {_atom_text(conn, it['item_atom_id'])}")
        lines.append("")
        files["03-close.md"] = "\n".join(lines)

    if write:
        out_dir.mkdir(parents=True, exist_ok=True)
        for name, content in files.items():
            (out_dir / name).write_text(content)
        return {
            "dry_run": False,
            "session_no": session_no,
            "workspace_session_no": workspace_no,
            "out_dir": str(out_dir),
            "files_written": list(files.keys()),
        }
    return {
        "dry_run": True,
        "session_no": session_no,
        "workspace_session_no": workspace_no,
        "out_dir": str(out_dir),
        "files_planned": list(files.keys()),
    }
