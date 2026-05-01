"""Reference-harness export: per-harness markdown under provenance/<open_wno>-<open_slug>/harnesses/<alias>.md.

Called from `_export_session_provenance` for each session N: emits any
non-open harness whose lifecycle touches N (opened, sealed, or reopened
in N). Open harnesses are skipped — the export materialises sealed
reference data, not in-flight scratch.

Files land in the OPENING session's directory regardless of which
session is being exported, so the alias-based filename matches the
opening session number and a harness sealed cross-session reconciles
into a single canonical path. A reopen overwrites the same path with
updated frontmatter (status flips to `reopened`, fired triggers shown).
"""

from __future__ import annotations

import sqlite3
from typing import Optional


def _atom_text(conn: sqlite3.Connection, atom_id: Optional[int]) -> str:
    if atom_id is None:
        return ""
    row = conn.execute("SELECT text FROM text_atoms WHERE atom_id=?", (atom_id,)).fetchone()
    return row["text"] if row else ""


def _session_wno_slug(conn: sqlite3.Connection, session_id: Optional[int]) -> tuple[Optional[int], Optional[str]]:
    if session_id is None:
        return (None, None)
    row = conn.execute(
        "SELECT workspace_session_no, session_no, slug FROM sessions WHERE session_id=?",
        (session_id,),
    ).fetchone()
    if row is None:
        return (None, None)
    return (row["workspace_session_no"] or row["session_no"], row["slug"])


def _export_reference_harnesses_for_session(
    conn: sqlite3.Connection, session_id: int
) -> dict[str, str]:
    """Return workspace-relative path -> markdown for every non-open harness
    whose lifecycle touches `session_id` (opened, sealed, or reopened here).

    Caller (session exporter) merges these files into its write set.
    """
    rows = conn.execute(
        "SELECT harness_id, alias, session_id, arc_slug, stage_n, "
        "       absence_declaration_atom_id, expiry_sessions, status, "
        "       sealed_at, sealed_session_id, expired_at, reopened_session_id, created_at "
        "FROM reference_harnesses "
        "WHERE status != 'open' "
        "  AND (session_id = ? OR sealed_session_id = ? OR reopened_session_id = ?) "
        "ORDER BY harness_id",
        (session_id, session_id, session_id),
    ).fetchall()

    files: dict[str, str] = {}
    for h in rows:
        open_wno, open_slug = _session_wno_slug(conn, h["session_id"])
        sealed_wno, _ = _session_wno_slug(conn, h["sealed_session_id"])
        reopened_wno, _ = _session_wno_slug(conn, h["reopened_session_id"])
        if open_wno is None or open_slug is None:
            continue  # defensive; session_id is NOT NULL per schema
        rel_path = f"provenance/{open_wno:03d}-{open_slug}/harnesses/{h['alias']}.md"

        lines: list[str] = ["---", f"id: {h['alias']}", f"status: {h['status']}",
                            f"arc_slug: {h['arc_slug']}", f"stage: {h['stage_n']}",
                            f"opened-in-session: {open_wno}"]
        if sealed_wno is not None:
            lines.append(f"sealed-in-session: {sealed_wno}")
        if h["sealed_at"]:
            lines.append(f"sealed-at: {h['sealed_at']}")
        if reopened_wno is not None:
            lines.append(f"reopened-in-session: {reopened_wno}")
        if h["expired_at"]:
            lines.append(f"expired-at: {h['expired_at']}")
        lines.append(f"expiry-sessions: {h['expiry_sessions']}")
        lines.append("generated_by: selvedge export --session")
        lines.append("---")
        lines.append("")
        lines.append(f"# {h['alias']} — Reference harness")
        lines.append("")

        lines.append("## Lifecycle")
        lines.append("")
        lines.append(f"- opened in session {open_wno} ({open_slug}); created at {h['created_at']}")
        if sealed_wno is not None:
            lines.append(f"- sealed in session {sealed_wno} at {h['sealed_at']}")
        if h["expired_at"]:
            lines.append(f"- expired at {h['expired_at']}")
        if reopened_wno is not None:
            lines.append(f"- reopened in session {reopened_wno}")
        lines.append("")

        lines.append("## Absence declaration")
        lines.append("")
        lines.append(_atom_text(conn, h["absence_declaration_atom_id"]))
        lines.append("")

        targets = conn.execute(
            "SELECT ord, descriptor_atom_id, artifact_path, artifact_sha256 "
            "FROM reference_harness_targets WHERE harness_id=? ORDER BY ord",
            (h["harness_id"],),
        ).fetchall()
        if targets:
            lines.append("## Targets")
            lines.append("")
            for t in targets:
                desc = _atom_text(conn, t["descriptor_atom_id"])
                lines.append(f"- **#{t['ord']}** — {desc}")
                if t["artifact_path"]:
                    lines.append(f"  - path: `{t['artifact_path']}`")
                if t["artifact_sha256"]:
                    lines.append(f"  - sha256: `{t['artifact_sha256']}`")
            lines.append("")

        assumptions = conn.execute(
            "SELECT ord, assumption_atom_id, origin_session_id, status "
            "FROM reference_harness_assumptions WHERE harness_id=? ORDER BY ord",
            (h["harness_id"],),
        ).fetchall()
        if assumptions:
            lines.append("## Assumptions")
            lines.append("")
            for a in assumptions:
                origin_wno, _ = _session_wno_slug(conn, a["origin_session_id"])
                origin = f" (origin: S{origin_wno:03d})" if origin_wno is not None else ""
                lines.append(
                    f"- **#{a['ord']}** [{a['status']}]{origin} — {_atom_text(conn, a['assumption_atom_id'])}"
                )
            lines.append("")

        claims = conn.execute(
            "SELECT claim_id, ord, claim_atom_id, world_constraint_atom_id, "
            "       surrogate_frame_atom_id, load_bearing "
            "FROM reference_harness_claims WHERE harness_id=? ORDER BY ord",
            (h["harness_id"],),
        ).fetchall()
        claim_ord_by_id = {c["claim_id"]: c["ord"] for c in claims}
        if claims:
            lines.append("## Claims")
            lines.append("")
            for c in claims:
                lb = " **load-bearing**" if c["load_bearing"] else ""
                lines.append(f"- **#{c['ord']}**{lb} — {_atom_text(conn, c['claim_atom_id'])}")
                if c["world_constraint_atom_id"]:
                    lines.append(
                        f"  - world constraint: {_atom_text(conn, c['world_constraint_atom_id'])}"
                    )
                if c["surrogate_frame_atom_id"]:
                    lines.append(
                        f"  - surrogate frame: {_atom_text(conn, c['surrogate_frame_atom_id'])}"
                    )
            lines.append("")

        stresses = conn.execute(
            "SELECT ord, protocol_kind, description_atom_id "
            "FROM reference_harness_stresses WHERE harness_id=? ORDER BY ord",
            (h["harness_id"],),
        ).fetchall()
        if stresses:
            lines.append("## Stress protocols")
            lines.append("")
            for s in stresses:
                lines.append(
                    f"- **#{s['ord']}** ({s['protocol_kind']}) — "
                    f"{_atom_text(conn, s['description_atom_id'])}"
                )
            lines.append("")

        results = conn.execute(
            "SELECT result_id, claim_id, result, evidence_atom_id "
            "FROM reference_harness_results "
            "WHERE claim_id IN (SELECT claim_id FROM reference_harness_claims WHERE harness_id=?) "
            "ORDER BY result_id",
            (h["harness_id"],),
        ).fetchall()
        if results:
            lines.append("## Results")
            lines.append("")
            for r in results:
                claim_ord = claim_ord_by_id.get(r["claim_id"], "?")
                lines.append(
                    f"- claim **#{claim_ord}** → **{r['result']}** — "
                    f"{_atom_text(conn, r['evidence_atom_id'])}"
                )
            lines.append("")

        dissents = conn.execute(
            "SELECT ord, dissent_atom_id, source_claim_id "
            "FROM reference_harness_dissent WHERE harness_id=? ORDER BY ord",
            (h["harness_id"],),
        ).fetchall()
        if dissents:
            lines.append("## Dissent")
            lines.append("")
            for d in dissents:
                src = (
                    f" (re #{claim_ord_by_id[d['source_claim_id']]})"
                    if d["source_claim_id"] in claim_ord_by_id
                    else ""
                )
                lines.append(
                    f"- **#{d['ord']}**{src} — {_atom_text(conn, d['dissent_atom_id'])}"
                )
            lines.append("")

        triggers = conn.execute(
            "SELECT ord, trigger_atom_id, fired_at, reopened_session_id "
            "FROM reference_harness_triggers WHERE harness_id=? ORDER BY ord",
            (h["harness_id"],),
        ).fetchall()
        if triggers:
            lines.append("## Falsification triggers")
            lines.append("")
            for t in triggers:
                fired = ""
                if t["fired_at"]:
                    fired_wno, _ = _session_wno_slug(conn, t["reopened_session_id"])
                    fired = f" — **FIRED** at {t['fired_at']}"
                    if fired_wno is not None:
                        fired += f" (session {fired_wno})"
                lines.append(
                    f"- **#{t['ord']}** — {_atom_text(conn, t['trigger_atom_id'])}{fired}"
                )
            lines.append("")

        lines.append("---")
        lines.append(
            "*Substrate-canonical: regenerated from `reference_harnesses` row by "
            "`selvedge export --session`. Atom text preserved verbatim from substrate.*"
        )
        files[rel_path] = "\n".join(lines).rstrip() + "\n"

    return files
