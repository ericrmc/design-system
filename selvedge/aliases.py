"""Alias resolution and reference recording shared by submit handlers."""

from __future__ import annotations

import re
import sqlite3
from typing import Iterable, Optional

from .errors import SelvedgeError
from .paths import ALIAS_RE


def _resolve_alias(conn: sqlite3.Connection, alias: str) -> Optional[int]:
    row = conn.execute(
        "SELECT object_id FROM objects WHERE alias = ?",
        (alias,),
    ).fetchone()
    return row["object_id"] if row else None


_ISSUE_ALIAS_RE = re.compile(r"^OI-(?:S\d{3}-\d+|\d{3}(?:-\d{3})?)$")
_FR_ALIAS_RE = re.compile(r"^FR-S\d{3}-\d+$")


def _resolve_alias_to_object_id(conn: sqlite3.Connection, alias: str) -> int:
    row = conn.execute("SELECT object_id FROM objects WHERE alias=?", (alias,)).fetchone()
    if row is None:
        # DV-S158-1: detect issue-shape and forward-reference-shape aliases and
        # emit a basis-aware hint. Issues live in `issues`, forward-references
        # live in `forward_reference_dispositions` close-state items; neither
        # registers in `objects`, so cite slots backed by FK to objects cannot
        # carry them. Fold into claim text or cite the surfacing EF / opening DV.
        if _ISSUE_ALIAS_RE.match(alias):
            raise SelvedgeError(
                "E_REFUSAL_T01",
                f"alias [{alias}] is an issue alias (issues are not objects); "
                f"cite the surfacing EF-... or opening DV-... instead, or fold "
                f"the OI reference into claim text",
            )
        if _FR_ALIAS_RE.match(alias):
            raise SelvedgeError(
                "E_REFUSAL_T01",
                f"alias [{alias}] is a forward-reference alias (FRs live in "
                f"forward_reference_dispositions, not objects); cite the "
                f"prior-session DV-... that emitted the FR or fold the FR "
                f"reference into claim text",
            )
        raise SelvedgeError("E_REFUSAL_T01", f"unresolved alias [{alias}]")
    return row["object_id"]


def _resolve_issue_alias(conn: sqlite3.Connection, alias: str) -> int:
    row = conn.execute(
        "SELECT issue_id FROM issues WHERE alias=?", (alias,)
    ).fetchone()
    if row is None:
        raise SelvedgeError("E_NOT_FOUND", f"issue alias [{alias}] not registered")
    return row["issue_id"]


def _alias_for_decision(session_no: int, decision_no: int) -> str:
    return f"D-S{session_no:03d}-{decision_no}"


def _alias_for_spec(spec_id: str, version: int) -> str:
    return f"SPEC-{spec_id}-v{version}"


def _alias_for_commitment(session_no: int, idx: int) -> str:
    return f"C-S{session_no:03d}-{idx}"


def _alias_for_engine_feedback(session_no: int, idx: int) -> str:
    return f"EF-S{session_no:03d}-{idx}"


def _parse_refs(body_md: str) -> list[str]:
    return [m.group(1) for m in ALIAS_RE.finditer(body_md or "")]


def _record_refs(
    conn: sqlite3.Connection,
    *,
    source_object_id: int,
    body_md: str,
    extra_refs: Iterable[dict] = (),
) -> int:
    """T-01: parse aliases out of body_md; insert refs rows; refuse if any alias unresolved."""
    aliases = _parse_refs(body_md)
    n = 0
    for alias in aliases:
        target_oid = _resolve_alias(conn, alias)
        if target_oid is None:
            raise SelvedgeError("E_REFUSAL_T01", f"unresolved alias [{alias}] in body_md")
        conn.execute(
            "INSERT INTO refs (source_object_id, target_object_id, relation, allow_superseded, reason_md) "
            "VALUES (?,?,?,?,?)",
            (source_object_id, target_oid, "cites", 0, None),
        )
        n += 1
    for r in extra_refs:
        target_alias = r.get("target_alias")
        target_oid = r.get("target_object_id") or (
            _resolve_alias(conn, target_alias) if target_alias else None
        )
        if target_oid is None:
            raise SelvedgeError("E_REFUSAL_T01", f"unresolved ref target {r!r}")
        conn.execute(
            "INSERT INTO refs (source_object_id, target_object_id, relation, allow_superseded, reason_md) "
            "VALUES (?,?,?,?,?)",
            (
                source_object_id,
                target_oid,
                r.get("relation", "cites"),
                int(r.get("allow_superseded", 0)),
                r.get("reason_md"),
            ),
        )
        n += 1
    return n
