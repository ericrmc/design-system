"""Anchor-trace export (engine-v34 / OI-S114-1 v1, DV-S116-1).

`bin/selvedge export --provenance --anchor <alias>` walks the closed edge
family rooted at one alias and materialises a markdown projection.

Closed edge family per DV-S116-1:
  - decision_supports.cited_object_id
  - decision_effects.target_object_id, target_issue_id
  - alternatives_v2 → alternative_rejections.cited_object_id
  - perspectives ↔ deliberations
  - close_state_items (FR) ↔ forward_reference_dispositions
  - spec_versions superseded chain (via decision_effects.effect_kind=
    'supersedes' targeting spec_version objects)

Bounded chain-walk: default depth 3, hard cap 5, --max-depth flag,
visited-set cycles, deterministic enqueue order. Markdown only; --graph
HTML and workspace-mode are deferred per DV-S114-1.
"""

from __future__ import annotations

import re
import sqlite3
from pathlib import Path
from typing import Optional

from ..errors import SelvedgeError
from ..paths import (
    ANCHOR_CITE_RE,
    ANCHOR_DELIB_RE,
    ANCHOR_FR_RE,
    ANCHOR_TRACE_DEFAULT_DEPTH,
    ANCHOR_TRACE_HARD_CAP_DEPTH,
)
from .session import _atom_text

# Walker logic version. Bump when the BFS shape, edge family, or markdown
# rendering changes in ways that would invalidate older receipts. Stamped
# onto every decision_chain_walks row at S176 substrate-gate landing
# (DV-S176-1, migration 031).
WALKER_VERSION = "v1"


def _anchor_node_key(node: tuple) -> tuple:
    """Visited-set key. Unique per (kind, primary_id)."""
    kind, pk, _alias = node
    return (kind, int(pk))


def _anchor_synthetic_alias(node: tuple) -> str:
    """Display alias for the node, synthesised when the underlying row has none."""
    kind, pk, alias = node
    if alias:
        return alias
    if kind == "forward_reference":
        return f"FR:row{pk}"
    if kind == "deliberation":
        return f"DELIB-{pk}"
    return f"{kind}:{pk}"


def _node_from_object_id(conn: sqlite3.Connection, oid: Optional[int]) -> Optional[tuple]:
    if oid is None:
        return None
    row = conn.execute(
        "SELECT object_kind, typed_row_id, alias FROM objects WHERE object_id=?",
        (oid,),
    ).fetchone()
    if row is None:
        return None
    return (row["object_kind"], row["typed_row_id"], row["alias"])


def _node_from_issue_id(conn: sqlite3.Connection, issue_id: int) -> Optional[tuple]:
    row = conn.execute("SELECT alias FROM issues WHERE issue_id=?", (issue_id,)).fetchone()
    if row is None:
        return None
    return ("issue", issue_id, row["alias"])


def _node_from_session_id(conn: sqlite3.Connection, session_id: int) -> Optional[tuple]:
    row = conn.execute(
        "SELECT workspace_session_no, session_no FROM sessions WHERE session_id=?",
        (session_id,),
    ).fetchone()
    if row is None:
        return None
    wno = row["workspace_session_no"] or row["session_no"]
    return ("session", session_id, f"S{wno:03d}")


def _node_from_kind_pk(conn: sqlite3.Connection, kind: str, pk: int) -> Optional[tuple]:
    """Resolve (kind, pk) → node tuple with alias eagerly populated."""
    if kind == "session":
        return _node_from_session_id(conn, pk)
    if kind == "issue":
        return _node_from_issue_id(conn, pk)
    row = conn.execute(
        "SELECT alias FROM objects WHERE object_kind=? AND typed_row_id=?",
        (kind, pk),
    ).fetchone()
    alias = row["alias"] if row else None
    return (kind, pk, alias)


def _resolve_anchor(conn: sqlite3.Connection, alias: str) -> tuple:
    """Resolve an anchor alias → node tuple. Raises E_NOT_FOUND on miss.

    Tries (in order): derived FR alias, derived DELIB alias, issues table,
    objects table.
    """
    m = ANCHOR_FR_RE.match(alias)
    if m:
        wno = int(m.group(1))
        seq = int(m.group(2))
        row = conn.execute(
            "SELECT csi.state_item_id "
            "FROM close_state_items csi "
            "JOIN close_records cr ON cr.close_record_id=csi.close_record_id "
            "JOIN sessions s ON s.session_id=cr.session_id "
            "WHERE csi.facet='next_session_should' "
            "  AND COALESCE(s.workspace_session_no, s.session_no)=? AND csi.seq=?",
            (wno, seq),
        ).fetchone()
        if row is None:
            raise SelvedgeError("E_NOT_FOUND", f"forward-reference {alias!r} not found in close_state_items")
        return ("forward_reference", row["state_item_id"], alias)
    m = ANCHOR_DELIB_RE.match(alias)
    if m:
        did = int(m.group(1))
        row = conn.execute(
            "SELECT deliberation_id FROM deliberations WHERE deliberation_id=?", (did,)
        ).fetchone()
        if row is None:
            raise SelvedgeError("E_NOT_FOUND", f"deliberation {alias!r} not found")
        return ("deliberation", did, alias)
    if alias.startswith("OI-"):
        row = conn.execute("SELECT issue_id FROM issues WHERE alias=?", (alias,)).fetchone()
        if row is not None:
            return ("issue", row["issue_id"], alias)
    row = conn.execute(
        "SELECT object_kind, typed_row_id FROM objects WHERE alias=?",
        (alias,),
    ).fetchone()
    if row is None:
        raise SelvedgeError("E_NOT_FOUND", f"alias {alias!r} unresolved (objects, issues, derived FR/DELIB)")
    return (row["object_kind"], row["typed_row_id"], alias)


def _anchor_node_summary(conn: sqlite3.Connection, node: tuple) -> str:
    """One-line summary of a node for the trace listing."""
    kind, pk, _alias = node
    if kind == "decision_v2":
        r = conn.execute(
            "SELECT d.kind, d.outcome_type, d.target_kind, d.target_key, "
            "       ta.text AS title, "
            "       COALESCE(s.workspace_session_no, s.session_no) AS wno "
            "FROM decisions_v2 d "
            "JOIN text_atoms ta ON ta.atom_id=d.title_atom_id "
            "JOIN sessions s ON s.session_id=d.session_id "
            "WHERE d.decision_v2_id=?",
            (pk,),
        ).fetchone()
        if r:
            return (
                f"S{r['wno']:03d} {r['kind']} {r['outcome_type']} "
                f"{r['target_kind']}=`{r['target_key']}` — {r['title']}"
            )
    if kind == "decision":
        r = conn.execute("SELECT title FROM decisions WHERE decision_id=?", (pk,)).fetchone()
        if r:
            return f"legacy decision: {r['title']}"
    if kind == "engine_feedback":
        r = conn.execute(
            "SELECT ef.flag, ef.body_md, ef.disposition, "
            "       COALESCE(s.workspace_session_no, s.session_no) AS wno "
            "FROM engine_feedback ef JOIN sessions s ON s.session_id=ef.session_id "
            "WHERE ef.feedback_id=?",
            (pk,),
        ).fetchone()
        if r:
            head = (r["body_md"] or "").split("\n", 1)[0]
            head = head.lstrip("*_ ").rstrip().rstrip("*")
            if len(head) > 200:
                head = head[:197] + "…"
            disp = " (disposed)" if r["disposition"] else ""
            return f"S{r['wno']:03d} {r['flag']}{disp}: {head}"
    if kind == "issue":
        r = conn.execute(
            "SELECT i.priority, i.status, ta.text AS title, "
            "       COALESCE(sf.workspace_session_no, sf.session_no) AS surfaced "
            "FROM issues i "
            "JOIN text_atoms ta ON ta.atom_id=i.title_atom_id "
            "JOIN sessions sf ON sf.session_id=i.surfaced_session_id "
            "WHERE i.issue_id=?",
            (pk,),
        ).fetchone()
        if r:
            return f"surfaced S{r['surfaced']:03d} {r['priority']} {r['status']} — {r['title']}"
    if kind == "spec_version":
        r = conn.execute(
            "SELECT sv.spec_id, sv.version, sv.status, "
            "       COALESCE(s.workspace_session_no, s.session_no) AS wno "
            "FROM spec_versions sv JOIN sessions s ON s.session_id=sv.session_id "
            "WHERE sv.spec_version_id=?",
            (pk,),
        ).fetchone()
        if r:
            return f"S{r['wno']:03d} {r['spec_id']} v{r['version']} [{r['status']}]"
    if kind == "perspective":
        r = conn.execute(
            "SELECT p.label, p.family, d.topic, "
            "       COALESCE(s.workspace_session_no, s.session_no) AS wno "
            "FROM perspectives p "
            "JOIN deliberations d ON d.deliberation_id=p.deliberation_id "
            "JOIN sessions s ON s.session_id=d.session_id "
            "WHERE p.perspective_id=?",
            (pk,),
        ).fetchone()
        if r:
            return f"S{r['wno']:03d} {r['label']} ({r['family']}) on {r['topic']}"
    if kind == "deliberation":
        r = conn.execute(
            "SELECT d.topic, "
            "       COALESCE(s.workspace_session_no, s.session_no) AS wno "
            "FROM deliberations d JOIN sessions s ON s.session_id=d.session_id "
            "WHERE d.deliberation_id=?",
            (pk,),
        ).fetchone()
        if r:
            return f"S{r['wno']:03d} deliberation: {r['topic']}"
    if kind == "session":
        r = conn.execute(
            "SELECT slug, kind, mode, "
            "       COALESCE(workspace_session_no, session_no) AS wno "
            "FROM sessions WHERE session_id=?",
            (pk,),
        ).fetchone()
        if r:
            return f"S{r['wno']:03d} ({r['kind']}, {r['mode']}) {r['slug']}"
    if kind == "close_record":
        r = conn.execute(
            "SELECT ta.text AS summary, "
            "       COALESCE(s.workspace_session_no, s.session_no) AS wno "
            "FROM close_records cr "
            "JOIN sessions s ON s.session_id=cr.session_id "
            "JOIN text_atoms ta ON ta.atom_id=cr.summary_atom_id "
            "WHERE cr.close_record_id=?",
            (pk,),
        ).fetchone()
        if r:
            return f"S{r['wno']:03d} close: {r['summary']}"
    if kind == "forward_reference":
        r = conn.execute(
            "SELECT csi.seq, ta.text AS text, "
            "       COALESCE(s.workspace_session_no, s.session_no) AS wno "
            "FROM close_state_items csi "
            "JOIN close_records cr ON cr.close_record_id=csi.close_record_id "
            "JOIN sessions s ON s.session_id=cr.session_id "
            "JOIN text_atoms ta ON ta.atom_id=csi.item_atom_id "
            "WHERE csi.state_item_id=?",
            (pk,),
        ).fetchone()
        if r:
            text = r["text"]
            if len(text) > 200:
                text = text[:197] + "…"
            return f"S{r['wno']:03d} FR-{r['seq']}: {text}"
    if kind == "alternative_v2":
        r = conn.execute(
            "SELECT a.label, ta.text AS option_text, dv.decision_v2_id, "
            "       o.alias AS decision_alias, "
            "       COALESCE(s.workspace_session_no, s.session_no) AS wno "
            "FROM alternatives_v2 a "
            "JOIN decisions_v2 dv ON dv.decision_v2_id=a.decision_v2_id "
            "LEFT JOIN objects o ON o.object_id=dv.object_id "
            "JOIN sessions s ON s.session_id=dv.session_id "
            "JOIN text_atoms ta ON ta.atom_id=a.option_atom_id "
            "WHERE a.alternative_v2_id=?",
            (pk,),
        ).fetchone()
        if r:
            return f"S{r['wno']:03d} {r['label']} of {r['decision_alias']}: {r['option_text']}"
    if kind == "assessment":
        r = conn.execute(
            "SELECT ta.text AS state, "
            "       COALESCE(s.workspace_session_no, s.session_no) AS wno "
            "FROM assessments a "
            "JOIN sessions s ON s.session_id=a.session_id "
            "JOIN text_atoms ta ON ta.atom_id=a.state_atom_id "
            "WHERE a.assessment_id=?",
            (pk,),
        ).fetchone()
        if r:
            return f"S{r['wno']:03d} assessment: {r['state']}"
    return f"{kind} pk={pk}"


def _decisions_citing_object(conn: sqlite3.Connection, oid: int) -> list[tuple]:
    """Return [(edge_kind, decision_v2_id), ...] for every decision that
    references this object_id via the closed edge family."""
    out: list[tuple] = []
    for s in conn.execute(
        "SELECT decision_v2_id, seq FROM decision_supports "
        "WHERE cited_object_id=? ORDER BY decision_v2_id, seq",
        (oid,),
    ).fetchall():
        out.append(("supports", s["decision_v2_id"]))
    for e in conn.execute(
        "SELECT decision_v2_id, effect_kind, effect_id FROM decision_effects "
        "WHERE target_object_id=? ORDER BY decision_v2_id, effect_id",
        (oid,),
    ).fetchall():
        out.append((f"effect:{e['effect_kind']}", e["decision_v2_id"]))
    for r in conn.execute(
        "SELECT av.decision_v2_id, ar.seq "
        "FROM alternative_rejections ar "
        "JOIN alternatives_v2 av ON av.alternative_v2_id=ar.alternative_v2_id "
        "WHERE ar.cited_object_id=? ORDER BY av.decision_v2_id, ar.seq",
        (oid,),
    ).fetchall():
        out.append(("rejection_cite", r["decision_v2_id"]))
    return out


def _decisions_citing_issue(conn: sqlite3.Connection, issue_id: int) -> list[tuple]:
    """Inverse-resolve every decision that names this issue via decision_effects.

    Two paths: (a) target_issue_id FK (post engine-v28 / DV-S098-1 dispatch),
    and (b) target_descriptor substring match for legacy effects whose FK
    was never populated. Migration 021 backfilled most resolvable cases but
    `opens_issue` effects often carry descriptors that name a not-yet-created
    alias, so the FK can stay NULL.
    """
    seen: set[tuple] = set()
    out: list[tuple] = []
    for e in conn.execute(
        "SELECT decision_v2_id, effect_kind, effect_id FROM decision_effects "
        "WHERE target_issue_id=? ORDER BY decision_v2_id, effect_id",
        (issue_id,),
    ).fetchall():
        key = (e["effect_kind"], e["decision_v2_id"])
        if key not in seen:
            seen.add(key)
            out.append((f"effect:{e['effect_kind']}", e["decision_v2_id"]))
    alias_row = conn.execute("SELECT alias FROM issues WHERE issue_id=?", (issue_id,)).fetchone()
    if alias_row and alias_row["alias"]:
        alias = alias_row["alias"]
        alias_pat = f"%{alias}%"
        # SQL LIKE is a substring match; word-boundary regex narrows
        # to whole-alias matches before recording the edge.
        boundary_re = re.compile(rf"(?<![A-Za-z0-9\-]){re.escape(alias)}(?![0-9\-])")
        for e in conn.execute(
            "SELECT decision_v2_id, effect_kind, effect_id, target_descriptor "
            "FROM decision_effects "
            "WHERE target_issue_id IS NULL AND target_descriptor LIKE ? "
            "ORDER BY decision_v2_id, effect_id",
            (alias_pat,),
        ).fetchall():
            if not boundary_re.search(e["target_descriptor"] or ""):
                continue
            key = (e["effect_kind"], e["decision_v2_id"])
            if key not in seen:
                seen.add(key)
                out.append((f"effect:{e['effect_kind']}", e["decision_v2_id"]))
    return out


def _anchor_object_id(conn: sqlite3.Connection, kind: str, pk: int) -> Optional[int]:
    row = conn.execute(
        "SELECT object_id FROM objects WHERE object_kind=? AND typed_row_id=?",
        (kind, pk),
    ).fetchone()
    return row["object_id"] if row else None


def _anchor_neighbours(conn: sqlite3.Connection, node: tuple) -> list[tuple]:
    """Return [(edge_kind, direction, neighbour_node), ...] for one node."""
    kind, pk, _alias = node
    edges: list[tuple] = []

    if kind == "decision_v2":
        ses = conn.execute(
            "SELECT session_id FROM decisions_v2 WHERE decision_v2_id=?", (pk,)
        ).fetchone()
        if ses:
            n = _node_from_session_id(conn, ses["session_id"])
            if n:
                edges.append(("in_session", "out", n))
        for s in conn.execute(
            "SELECT cited_object_id FROM decision_supports "
            "WHERE decision_v2_id=? AND cited_object_id IS NOT NULL ORDER BY seq",
            (pk,),
        ).fetchall():
            n = _node_from_object_id(conn, s["cited_object_id"])
            if n:
                edges.append(("supports", "out", n))
        for e in conn.execute(
            "SELECT effect_kind, target_object_id, target_issue_id, effect_id "
            "FROM decision_effects WHERE decision_v2_id=? ORDER BY effect_id",
            (pk,),
        ).fetchall():
            if e["target_object_id"]:
                n = _node_from_object_id(conn, e["target_object_id"])
                if n:
                    edges.append((f"effect:{e['effect_kind']}", "out", n))
            elif e["target_issue_id"]:
                n = _node_from_issue_id(conn, e["target_issue_id"])
                if n:
                    edges.append((f"effect:{e['effect_kind']}", "out", n))
        for a in conn.execute(
            "SELECT alternative_v2_id FROM alternatives_v2 "
            "WHERE decision_v2_id=? ORDER BY alternative_v2_id",
            (pk,),
        ).fetchall():
            for r in conn.execute(
                "SELECT cited_object_id FROM alternative_rejections "
                "WHERE alternative_v2_id=? AND cited_object_id IS NOT NULL ORDER BY seq",
                (a["alternative_v2_id"],),
            ).fetchall():
                n = _node_from_object_id(conn, r["cited_object_id"])
                if n:
                    edges.append(("rejection_cite", "out", n))

    elif kind == "engine_feedback":
        ses = conn.execute(
            "SELECT session_id FROM engine_feedback WHERE feedback_id=?", (pk,)
        ).fetchone()
        if ses:
            n = _node_from_session_id(conn, ses["session_id"])
            if n:
                edges.append(("surfaced_in", "out", n))
        oid = _anchor_object_id(conn, "engine_feedback", pk)
        if oid is not None:
            for ek, did in _decisions_citing_object(conn, oid):
                edges.append((ek, "in", _node_from_kind_pk(conn, "decision_v2", did)))

    elif kind == "issue":
        i = conn.execute(
            "SELECT surfaced_session_id, resolved_session_id FROM issues WHERE issue_id=?",
            (pk,),
        ).fetchone()
        if i:
            n = _node_from_session_id(conn, i["surfaced_session_id"])
            if n:
                edges.append(("surfaced_in", "out", n))
            if i["resolved_session_id"]:
                n = _node_from_session_id(conn, i["resolved_session_id"])
                if n:
                    edges.append(("resolved_in", "out", n))
        for ek, did in _decisions_citing_issue(conn, pk):
            edges.append((ek, "in", _node_from_kind_pk(conn, "decision_v2", did)))

    elif kind == "spec_version":
        sv = conn.execute(
            "SELECT session_id FROM spec_versions WHERE spec_version_id=?", (pk,)
        ).fetchone()
        if sv:
            n = _node_from_session_id(conn, sv["session_id"])
            if n:
                edges.append(("created_in", "out", n))
        oid = _anchor_object_id(conn, "spec_version", pk)
        if oid is not None:
            for ek, did in _decisions_citing_object(conn, oid):
                edges.append((ek, "in", _node_from_kind_pk(conn, "decision_v2", did)))

    elif kind == "perspective":
        p = conn.execute(
            "SELECT deliberation_id FROM perspectives WHERE perspective_id=?", (pk,)
        ).fetchone()
        if p:
            edges.append(
                ("in_deliberation", "out", _node_from_kind_pk(conn, "deliberation", p["deliberation_id"]))
            )
        oid = _anchor_object_id(conn, "perspective", pk)
        if oid is not None:
            for ek, did in _decisions_citing_object(conn, oid):
                edges.append((ek, "in", _node_from_kind_pk(conn, "decision_v2", did)))

    elif kind == "deliberation":
        d = conn.execute(
            "SELECT session_id FROM deliberations WHERE deliberation_id=?", (pk,)
        ).fetchone()
        if d:
            n = _node_from_session_id(conn, d["session_id"])
            if n:
                edges.append(("in_session", "out", n))
            # decisions made in the same session whose support basis is
            # 'deliberation' link back here. Cited_object_id is NULL on the
            # deliberation basis row (current substrate convention), so the
            # join is via session + basis rather than object_id.
            for r in conn.execute(
                "SELECT DISTINCT s.decision_v2_id FROM decision_supports s "
                "JOIN decisions_v2 dv ON dv.decision_v2_id=s.decision_v2_id "
                "WHERE dv.session_id=? AND s.basis='deliberation' "
                "ORDER BY s.decision_v2_id",
                (d["session_id"],),
            ).fetchall():
                edges.append(
                    ("supports[deliberation]", "in", _node_from_kind_pk(conn, "decision_v2", r["decision_v2_id"]))
                )
        for r in conn.execute(
            "SELECT perspective_id FROM perspectives WHERE deliberation_id=? ORDER BY perspective_id",
            (pk,),
        ).fetchall():
            edges.append(
                ("has_perspective", "out", _node_from_kind_pk(conn, "perspective", r["perspective_id"]))
            )

    elif kind == "session":
        # Session is a leaf-ish node in the closed edge family per DV-S116-1.
        # Anchoring on a session is supported via session-root expansion in
        # _export_provenance_anchor; when a session is reached as a *neighbour*
        # we deliberately do NOT broadcast to every sibling decision/EF/spec —
        # that would dilute the causal trace.
        return edges

    elif kind == "close_record":
        cr = conn.execute(
            "SELECT session_id FROM close_records WHERE close_record_id=?", (pk,)
        ).fetchone()
        if cr:
            n = _node_from_session_id(conn, cr["session_id"])
            if n:
                edges.append(("of_session", "out", n))
        for r in conn.execute(
            "SELECT csi.state_item_id, csi.seq, "
            "       COALESCE(s.workspace_session_no, s.session_no) AS wno "
            "FROM close_state_items csi "
            "JOIN close_records cr ON cr.close_record_id=csi.close_record_id "
            "JOIN sessions s ON s.session_id=cr.session_id "
            "WHERE csi.close_record_id=? AND csi.facet='next_session_should' "
            "ORDER BY csi.seq",
            (pk,),
        ).fetchall():
            fr_alias = f"FR-S{r['wno']:03d}-{r['seq']}"
            edges.append(("forward_reference", "out", ("forward_reference", r["state_item_id"], fr_alias)))

    elif kind == "forward_reference":
        r = conn.execute(
            "SELECT csi.close_record_id, ta.text AS text "
            "FROM close_state_items csi "
            "JOIN text_atoms ta ON ta.atom_id=csi.item_atom_id "
            "WHERE csi.state_item_id=?",
            (pk,),
        ).fetchone()
        if r:
            edges.append((
                "from_close",
                "out",
                _node_from_kind_pk(conn, "close_record", r["close_record_id"]),
            ))
        d = conn.execute(
            "SELECT resolved_session_id, note_atom_id "
            "FROM forward_reference_dispositions WHERE state_item_id=?",
            (pk,),
        ).fetchone()
        if d:
            n = _node_from_session_id(conn, d["resolved_session_id"])
            if n:
                edges.append(("disposed_in", "out", n))
            note_text = _atom_text(conn, d["note_atom_id"]) if d["note_atom_id"] else ""
            for cited in _scan_anchor_cites(note_text):
                target = _resolve_optional(conn, cited)
                if target is not None:
                    edges.append(("disposition_cite", "out", target))

    elif kind == "alternative_v2":
        r = conn.execute(
            "SELECT decision_v2_id FROM alternatives_v2 WHERE alternative_v2_id=?",
            (pk,),
        ).fetchone()
        if r:
            edges.append(("alternative_of", "out", _node_from_kind_pk(conn, "decision_v2", r["decision_v2_id"])))
        for rr in conn.execute(
            "SELECT cited_object_id FROM alternative_rejections "
            "WHERE alternative_v2_id=? AND cited_object_id IS NOT NULL ORDER BY seq",
            (pk,),
        ).fetchall():
            n = _node_from_object_id(conn, rr["cited_object_id"])
            if n:
                edges.append(("rejection_cite", "out", n))

    return edges


def _scan_anchor_cites(text: str) -> list[str]:
    """Extract distinct alias citations from free-form text in seq-stable order."""
    seen: list[str] = []
    for m in ANCHOR_CITE_RE.finditer(text or ""):
        a = m.group(1)
        if a not in seen:
            seen.append(a)
    return seen


def _resolve_optional(conn: sqlite3.Connection, alias: str) -> Optional[tuple]:
    try:
        return _resolve_anchor(conn, alias)
    except SelvedgeError:
        return None


def _export_provenance_anchor(
    conn: sqlite3.Connection,
    alias: str,
    max_depth: int = ANCHOR_TRACE_DEFAULT_DEPTH,
    write: bool = False,
) -> dict:
    """BFS the closed edge family rooted at one alias; return a markdown projection.

    Visited-set keyed on (object_kind, primary_id) prevents cycles. Depth is
    bounded by max_depth (caller-supplied, refused above ANCHOR_TRACE_HARD_CAP_DEPTH=5).
    Edges out of the cap-1 frontier are listed but their neighbours are not
    expanded — this surfaces "this trace was bounded here" rather than
    silently truncating.
    """
    if not isinstance(max_depth, int) or max_depth < 1:
        raise SelvedgeError(
            "E_BAD_ARG",
            f"--max-depth must be 1..{ANCHOR_TRACE_HARD_CAP_DEPTH} (got {max_depth!r})",
        )
    if max_depth > ANCHOR_TRACE_HARD_CAP_DEPTH:
        raise SelvedgeError(
            "E_BAD_ARG",
            f"--max-depth {max_depth} exceeds hard cap {ANCHOR_TRACE_HARD_CAP_DEPTH} (DV-S116-1)",
        )

    root = _resolve_anchor(conn, alias)
    visited: dict[tuple, dict] = {}
    edges_out: list[dict] = []

    def display(node: tuple) -> str:
        return _anchor_synthetic_alias(node)

    def neighbours_for(node: tuple, is_root: bool) -> list[tuple]:
        # Session-as-anchor expansion: when the user roots the trace at a
        # session we surface its decisions/deliberations/close_record
        # explicitly (since the closed family treats sessions as leaves
        # otherwise). This keeps `--anchor S110` useful without broadcasting
        # session contents on every transit.
        if is_root and node[0] == "session":
            sid = node[1]
            edges: list[tuple] = []
            for r in conn.execute(
                "SELECT decision_v2_id FROM decisions_v2 WHERE session_id=? ORDER BY decision_no",
                (sid,),
            ).fetchall():
                edges.append(("decided_in", "out", _node_from_kind_pk(conn, "decision_v2", r["decision_v2_id"])))
            for r in conn.execute(
                "SELECT deliberation_id FROM deliberations WHERE session_id=? ORDER BY deliberation_id",
                (sid,),
            ).fetchall():
                edges.append(
                    ("deliberated_in", "out", _node_from_kind_pk(conn, "deliberation", r["deliberation_id"]))
                )
            for r in conn.execute(
                "SELECT feedback_id FROM engine_feedback WHERE session_id=? ORDER BY feedback_id",
                (sid,),
            ).fetchall():
                edges.append(("ef_surfaced", "out", _node_from_kind_pk(conn, "engine_feedback", r["feedback_id"])))
            for r in conn.execute(
                "SELECT spec_version_id FROM spec_versions WHERE session_id=? ORDER BY spec_version_id",
                (sid,),
            ).fetchall():
                edges.append(("spec_created", "out", _node_from_kind_pk(conn, "spec_version", r["spec_version_id"])))
            cr = conn.execute(
                "SELECT close_record_id FROM close_records WHERE session_id=?", (sid,)
            ).fetchone()
            if cr:
                edges.append(("closed_with", "out", _node_from_kind_pk(conn, "close_record", cr["close_record_id"])))
            return edges
        return _anchor_neighbours(conn, node)

    frontier: list[tuple[int, tuple]] = [(0, root)]
    visited[_anchor_node_key(root)] = {"depth": 0, "node": root}

    while frontier:
        next_frontier: list[tuple[int, tuple]] = []
        for depth, node in frontier:
            if depth >= max_depth:
                continue
            is_root = (depth == 0 and node == root)
            for edge_kind, direction, neighbour in neighbours_for(node, is_root):
                if neighbour is None:
                    continue
                edges_out.append({
                    "from_alias": display(node),
                    "from_kind": node[0],
                    "to_alias": display(neighbour),
                    "to_kind": neighbour[0],
                    "edge": edge_kind,
                    "direction": direction,
                    "depth_from": depth,
                })
                key = _anchor_node_key(neighbour)
                if key in visited:
                    continue
                visited[key] = {"depth": depth + 1, "node": neighbour}
                next_frontier.append((depth + 1, neighbour))
        next_frontier.sort(key=lambda dn: display(dn[1]))
        frontier = next_frontier

    for entry in visited.values():
        n = entry["node"]
        if n[2] is None:
            entry["display"] = display((n[0], n[1], None))
        else:
            entry["display"] = n[2]

    by_depth: dict[int, list[tuple]] = {}
    for key, entry in visited.items():
        by_depth.setdefault(entry["depth"], []).append((entry["display"], entry["node"]))
    for d in by_depth:
        by_depth[d].sort(key=lambda item: item[0])

    edges_at_depth: dict[int, list[dict]] = {}
    for e in edges_out:
        edges_at_depth.setdefault(e["depth_from"] + 1, []).append(e)

    root_summary = _anchor_node_summary(conn, root)
    out_path = Path("provenance") / "anchor-traces" / f"{alias}.md"
    lines: list[str] = [
        "---",
        f"anchor: {alias}",
        f"kind: {root[0]}",
        f"max_depth: {max_depth}",
        f"hard_cap_depth: {ANCHOR_TRACE_HARD_CAP_DEPTH}",
        f"nodes_visited: {len(visited)}",
        f"edges_traversed: {len(edges_out)}",
        "generated_by: selvedge export --provenance --anchor",
        "---",
        "",
        f"# Anchor trace: `{alias}`",
        "",
        f"**Anchor.** `{alias}` ({root[0]}) — {root_summary}",
        "",
        f"**Bounded chain-walk.** Default depth {ANCHOR_TRACE_DEFAULT_DEPTH}, "
        f"hard cap {ANCHOR_TRACE_HARD_CAP_DEPTH} (DV-S116-1). "
        f"This trace ran with `--max-depth {max_depth}`.",
        "",
        f"**Closed edge family.** decision_supports, decision_effects, "
        "alternatives_v2 → alternative_rejections, perspectives ↔ deliberations, "
        "close_state_items (FR) ↔ forward_reference_dispositions, spec_version "
        "supersession via decision_effects.",
        "",
        f"**Nodes visited.** {len(visited)}. **Edges traversed.** {len(edges_out)}.",
        "",
        "## Frontier by depth",
        "",
    ]
    for d in sorted(by_depth):
        lines.append(f"### Depth {d} ({len(by_depth[d])} node{'s' if len(by_depth[d])!=1 else ''})")
        lines.append("")
        for disp, node in by_depth[d]:
            summary = _anchor_node_summary(conn, node)
            lines.append(f"- `{disp}` ({node[0]}) — {summary}")
            for e in edges_at_depth.get(d, []):
                if e["to_alias"] == disp and e["to_kind"] == node[0]:
                    arrow = "←" if e["direction"] == "in" else "→"
                    lines.append(f"  - via `{e['edge']}` {arrow} `{e['from_alias']}`")
        lines.append("")

    cap_nodes = by_depth.get(max_depth, [])
    if cap_nodes:
        lines.append("## Boundary")
        lines.append("")
        lines.append(
            f"The trace reached `--max-depth {max_depth}` at "
            f"{len(cap_nodes)} node{'s' if len(cap_nodes)!=1 else ''}. "
            "Outbound edges from these nodes were not expanded. "
            f"Re-run with `--max-depth N` (1..{ANCHOR_TRACE_HARD_CAP_DEPTH}) to widen."
        )
        lines.append("")

    body = "\n".join(lines).rstrip() + "\n"
    files = {str(out_path): body}
    truncation_status = "depth_capped" if cap_nodes else "none"

    if write:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(body)
        return {
            "dry_run": False,
            "anchor": alias,
            "kind": root[0],
            "max_depth": max_depth,
            "nodes_visited": len(visited),
            "edges_traversed": len(edges_out),
            "out_path": str(out_path),
            "walker_version": WALKER_VERSION,
            "truncation_status": truncation_status,
            "body": body,
        }
    return {
        "dry_run": True,
        "anchor": alias,
        "kind": root[0],
        "max_depth": max_depth,
        "nodes_visited": len(visited),
        "edges_traversed": len(edges_out),
        "planned_path": str(out_path),
        "preview": body,
        "walker_version": WALKER_VERSION,
        "truncation_status": truncation_status,
    }
