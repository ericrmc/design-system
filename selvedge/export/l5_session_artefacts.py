"""L5 close-time export expansion (OI-S081-6 / DV-S081-1 / DV-S187-1).

Five session-bounded artefact files, written alongside the existing 00–04
provenance dir for each session:

  - 05-engine-feedback.md       — engine_feedback rows surfaced this session
  - 06-counterfactuals.md       — deliberation_counterfactuals for this session's deliberations
  - 07-fr-dispositions.md       — forward_reference_dispositions resolved by this session
  - 08-prechecks.md             — decision_prechecks rows authored this session
  - 09-chain-walks.md           — decision_chain_walks receipts for this session's decisions

These tables are not session-state per se but they are the receipts that prove
gates ran (T-32 chain-walks, T-33 prechecks, T-36 counterfactuals) plus the
substrate's own learning ledger (engine_feedback) and the session's explicit
ask-resolution record (forward_reference_dispositions). Per S081 C-8 they are
mandatory close-time exports so substrate-loss leaves them recoverable from
the markdown surface.

The exporter is deterministic: stable ordering by primary key, no live
timestamps in body content beyond what's already on the substrate row, and
empty rowsets produce no file (caller reconciles stale files).
"""

from __future__ import annotations

import sqlite3
from typing import Optional


def _atom_text(conn: sqlite3.Connection, atom_id: Optional[int]) -> str:
    if atom_id is None:
        return ""
    row = conn.execute("SELECT text FROM text_atoms WHERE atom_id=?", (atom_id,)).fetchone()
    return row["text"] if row else ""


def _frontmatter(workspace_no: int, slug: str, title: str) -> list[str]:
    return [
        "---",
        f"session: {workspace_no:03d}",
        f"title: {slug} — {title}",
        "generated_by: selvedge export --session",
        "---",
        "",
    ]


def _engine_feedback_md(conn: sqlite3.Connection, session_id: int, workspace_no: int, slug: str) -> Optional[str]:
    rows = conn.execute(
        "SELECT ef.feedback_id, o.alias, ef.flag, ef.body_md, ef.disposition "
        "FROM engine_feedback ef "
        "LEFT JOIN objects o ON o.object_id=ef.object_id "
        "WHERE ef.session_id=? "
        "ORDER BY ef.feedback_id",
        (session_id,),
    ).fetchall()
    if not rows:
        return None
    lines = _frontmatter(workspace_no, slug, "engine-feedback") + ["# Engine feedback", ""]
    for r in rows:
        lines.append(f"## {r['alias']}")
        lines.append("")
        lines.append(f"- **flag.** {r['flag']}")
        lines.append(f"- **disposition.** {r['disposition'] or '(none)'}")
        lines.append("")
        lines.append(r["body_md"])
        lines.append("")
    return "\n".join(lines)


def _counterfactuals_md(conn: sqlite3.Connection, session_id: int, workspace_no: int, slug: str) -> Optional[str]:
    rows = conn.execute(
        "SELECT cf.counterfactual_id, cf.deliberation_id, cf.seq, "
        "       cf.position, cf.why, cf.disposition, cf.disposition_note, "
        "       cf.exclusion_kind, cf.nil_attestation, d.topic "
        "FROM deliberation_counterfactuals cf "
        "JOIN deliberations d ON d.deliberation_id=cf.deliberation_id "
        "WHERE cf.session_id=? "
        "ORDER BY cf.deliberation_id, cf.seq",
        (session_id,),
    ).fetchall()
    if not rows:
        return None
    lines = _frontmatter(workspace_no, slug, "counterfactuals") + ["# Deliberation counterfactuals", ""]
    cur_delib: Optional[int] = None
    for r in rows:
        if r["deliberation_id"] != cur_delib:
            cur_delib = r["deliberation_id"]
            lines.append(f"## D-{cur_delib} — {r['topic']}")
            lines.append("")
        nil = " (nil_attestation)" if r["nil_attestation"] else ""
        lines.append(f"### Counterfactual {r['seq']}{nil}")
        lines.append("")
        lines.append(f"- **position.** {r['position']}")
        lines.append(f"- **why.** {r['why']}")
        if r["disposition_note"]:
            lines.append(f"- **disposition.** {r['disposition']} — {r['disposition_note']}")
        elif r["exclusion_kind"]:
            lines.append(f"- **disposition.** {r['disposition']} (exclusion_kind={r['exclusion_kind']})")
        else:
            lines.append(f"- **disposition.** {r['disposition']}")
        lines.append("")
    return "\n".join(lines)


def _fr_dispositions_md(conn: sqlite3.Connection, session_id: int, workspace_no: int, slug: str) -> Optional[str]:
    rows = conn.execute(
        "SELECT frd.disposition_id, frd.resolved_at, "
        "       csi.seq AS csi_seq, csi.facet, "
        "       s_orig.workspace_session_no AS orig_wno, "
        "       ta_orig.text AS orig_text, "
        "       ta_note.text AS note_text "
        "FROM forward_reference_dispositions frd "
        "JOIN close_state_items csi ON csi.state_item_id=frd.state_item_id "
        "JOIN close_records cr ON cr.close_record_id=csi.close_record_id "
        "JOIN sessions s_orig ON s_orig.session_id=cr.session_id "
        "JOIN text_atoms ta_orig ON ta_orig.atom_id=csi.item_atom_id "
        "LEFT JOIN text_atoms ta_note ON ta_note.atom_id=frd.note_atom_id "
        "WHERE frd.resolved_session_id=? "
        "ORDER BY frd.disposition_id",
        (session_id,),
    ).fetchall()
    if not rows:
        return None
    lines = _frontmatter(workspace_no, slug, "forward-reference-dispositions") + [
        "# Forward-reference dispositions", "",
    ]
    for r in rows:
        lines.append(f"## FR-S{r['orig_wno']:03d}-{r['csi_seq']}")
        lines.append("")
        lines.append(f"- **Originating session.** S{r['orig_wno']:03d} (`{r['facet']}` state-item seq {r['csi_seq']}).")
        lines.append(f"- **Original ask.** {r['orig_text']}")
        note = r["note_text"] or "(no note)"
        lines.append(f"- **Resolved.** {note}")
        lines.append(f"- **Resolved-at.** {r['resolved_at']}")
        lines.append("")
    return "\n".join(lines)


def _prechecks_md(conn: sqlite3.Connection, session_id: int, workspace_no: int, slug: str) -> Optional[str]:
    rows = conn.execute(
        "SELECT precheck_id, target_kind, target_key, context_sha256, "
        "       walker_version, ttl_seconds, created_at, consumed_at, "
        "       consumed_by_decision_v2_id "
        "FROM decision_prechecks "
        "WHERE session_id=? "
        "ORDER BY precheck_id",
        (session_id,),
    ).fetchall()
    if not rows:
        return None
    lines = _frontmatter(workspace_no, slug, "decision-prechecks") + ["# Decision prechecks (T-33 receipts)", ""]
    for r in rows:
        lines.append(f"## Precheck #{r['precheck_id']} — {r['target_kind']} `{r['target_key']}`")
        lines.append("")
        lines.append(f"- **walker_version.** {r['walker_version']}")
        lines.append(f"- **ttl_seconds.** {r['ttl_seconds']}")
        lines.append(f"- **context_sha256.** `{r['context_sha256'][:16]}…`")
        lines.append(f"- **created_at.** {r['created_at']}")
        if r["consumed_at"]:
            lines.append(f"- **consumed_at.** {r['consumed_at']} (by decision_v2_id={r['consumed_by_decision_v2_id']})")
        else:
            lines.append("- **consumed_at.** (unconsumed)")
        lines.append("")
    return "\n".join(lines)


def _chain_walks_md(conn: sqlite3.Connection, session_id: int, workspace_no: int, slug: str) -> Optional[str]:
    rows = conn.execute(
        "SELECT cw.chain_walk_id, cw.decision_v2_id, cw.anchor_alias, "
        "       cw.max_depth, cw.walker_version, cw.nodes_visited, "
        "       cw.edges_traversed, cw.truncation_status, cw.result_sha256, "
        "       cw.created_at, dv.decision_no, ta.text AS title_text "
        "FROM decision_chain_walks cw "
        "JOIN decisions_v2 dv ON dv.decision_v2_id=cw.decision_v2_id "
        "LEFT JOIN text_atoms ta ON ta.atom_id=dv.title_atom_id "
        "WHERE dv.session_id=? "
        "ORDER BY cw.decision_v2_id, cw.chain_walk_id",
        (session_id,),
    ).fetchall()
    if not rows:
        return None
    lines = _frontmatter(workspace_no, slug, "decision-chain-walks") + [
        "# Decision chain-walks (T-32 receipts)",
        "",
        "Receipts only. The full walker output (`result_text`) is preserved in",
        "the `decision_chain_walks` substrate row and regenerable via",
        "`bin/selvedge export --provenance --anchor <alias> --print`.",
        "",
    ]
    cur_decision: Optional[int] = None
    for r in rows:
        if r["decision_v2_id"] != cur_decision:
            cur_decision = r["decision_v2_id"]
            title = r["title_text"] or "(untitled decision)"
            lines.append(f"## D-{r['decision_no']}. {title}")
            lines.append("")
        lines.append(f"### Anchor `{r['anchor_alias']}`")
        lines.append("")
        lines.append(f"- **walker_version.** {r['walker_version']}")
        lines.append(f"- **max_depth.** {r['max_depth']}")
        lines.append(f"- **nodes_visited.** {r['nodes_visited']}")
        lines.append(f"- **edges_traversed.** {r['edges_traversed']}")
        lines.append(f"- **truncation_status.** {r['truncation_status']}")
        lines.append(f"- **result_sha256.** `{r['result_sha256'][:16]}…`")
        lines.append(f"- **created_at.** {r['created_at']}")
        lines.append("")
    return "\n".join(lines)


# Public dispatcher: filename -> markdown body (when rows present).
L5_FILENAMES = (
    "05-engine-feedback.md",
    "06-counterfactuals.md",
    "07-fr-dispositions.md",
    "08-prechecks.md",
    "09-chain-walks.md",
)


def export_l5_session_artefacts(
    conn: sqlite3.Connection, session_id: int, workspace_no: int, slug: str
) -> dict[str, str]:
    """Return {filename: body} for any of the 5 L5 artefacts that have rows.

    Empty rowsets produce no entry; the caller reconciles on-disk stale files
    against the keys returned here.
    """
    plan = (
        ("05-engine-feedback.md", _engine_feedback_md),
        ("06-counterfactuals.md", _counterfactuals_md),
        ("07-fr-dispositions.md", _fr_dispositions_md),
        ("08-prechecks.md", _prechecks_md),
        ("09-chain-walks.md", _chain_walks_md),
    )
    out: dict[str, str] = {}
    for name, fn in plan:
        body = fn(conn, session_id, workspace_no, slug)
        if body is not None:
            out[name] = body
    return out
