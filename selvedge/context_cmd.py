"""bin/selvedge context — assessment-precheck context-pack CLI (T-38 substrate-gate, S195 DV-S195-1).

Mirrors the T-33 decision-record precheck pattern (engine-v49, DV-S179-1)
but at assessment-submit time. Operator-named-mandate at S194-close
relocated context-surfacing from orient (where agents skim under context
pressure) to assessment-time as a substrate-enforced refusal: the agent
cannot submit an assessment without first running this CLI to render the
substrate-presented context-pack into their context window.

Substrate-presented (not operator-curated): the substrate auto-generates
the pack from active deliberation surfaces (undisposed FRs + open HIGH
OIs as the floor; named --target narrows or adds). Operator quote:
"the substrate is not frictionless and agents tend to avoid using it" —
forcing the auto-generated pack to print at run-time means the agent
sees relevant typed-graph context regardless of whether they would have
sought it. Single-use atomic-consume + sha256-over-rendered-pack-content
shape per codex shape-consult (EF-S195-1) caution against substrate-drift
invalidating receipts.

Read/write separation (DV-S176-1 D-27): the CLI walks substrate read-only
to gather sources, computes context_sha256 over the rendered markdown, and
INSERTs one assessment_prechecks row + emits nonce. The substrate refuses
the assessment-submit at T-38 unless the nonce verifies inside same
write_tx.
"""

from __future__ import annotations

import hashlib
import json
import secrets
import sqlite3
from typing import List, Optional

from .errors import SelvedgeError
from .paths import db_path

CONTEXT_WALKER_VERSION = "v1"
CONTEXT_DEFAULT_TTL = 1800  # 30 minutes; matches T-33 default


def _open_session_id(conn: sqlite3.Connection) -> int:
    row = conn.execute(
        "SELECT session_id FROM sessions WHERE status='open' LIMIT 1"
    ).fetchone()
    if row is None:
        raise SelvedgeError(
            "E_VALIDATION",
            "no open session; bin/selvedge context requires an active session "
            "(run `bin/selvedge submit session-open --payload ...` first)",
        )
    return row["session_id"]


def _resolve_target_alias(conn: sqlite3.Connection, alias: str) -> Optional[int]:
    row = conn.execute("SELECT object_id FROM objects WHERE alias=?", (alias,)).fetchone()
    return row["object_id"] if row else None


def _gather_substrate_floor(conn: sqlite3.Connection) -> List[str]:
    """Substrate-presented floor: undisposed FRs + open HIGH OIs.

    Per operator-named-mandate at S194-close: agents avoid the substrate;
    auto-generation mandatory. Returns the alias-set the pack will walk
    when --target is not provided. Named --target narrows or adds; this
    floor is the always-included baseline.
    """
    floor: List[str] = []
    fr_rows = conn.execute(
        "SELECT csi.seq, COALESCE(s.workspace_session_no, s.session_no) AS wno "
        "FROM close_state_items csi "
        "JOIN close_records cr ON cr.close_record_id=csi.close_record_id "
        "JOIN sessions s ON s.session_id=cr.session_id "
        "WHERE csi.facet='next_session_should' "
        "  AND NOT EXISTS (SELECT 1 FROM forward_reference_dispositions frd "
        "                  WHERE frd.state_item_id=csi.state_item_id) "
        "ORDER BY s.session_no DESC, csi.seq"
    ).fetchall()
    for r in fr_rows:
        floor.append(f"FR-S{r['wno']:03d}-{r['seq']}")
    oi_rows = conn.execute(
        "SELECT alias FROM issues WHERE status='open' AND priority='HIGH' "
        "ORDER BY created_at DESC"
    ).fetchall()
    for r in oi_rows:
        floor.append(r["alias"])
    return floor


def _gather_target_context(
    conn: sqlite3.Connection, target_alias: str, target_oid: Optional[int]
) -> List[dict]:
    """For one target: chain-walked predecessors + anchored harvest EFs +
    recent supersessions + active spec clauses citing it. Each returned
    entry is a dict with `kind`, `body`, `source_alias`."""
    sources: List[dict] = []

    if target_oid is None:
        sources.append(
            {
                "kind": "unresolved_target",
                "body": f"target {target_alias} does not resolve in objects.alias; "
                f"chain-walks unavailable. (Issues + FRs do not register in objects; "
                f"acceptable per DV-S189-1 markdown-only-recovery.)",
                "source_alias": None,
            }
        )
        return sources

    # 1. Anchored harvest EFs whose anchor lands on target_oid.
    rows = conn.execute(
        "SELECT o_ef.alias AS ef_alias, efa.anchor_role, "
        "       SUBSTR(ef.body_md, 1, 200) AS head "
        "FROM engine_feedback_anchors efa "
        "JOIN engine_feedback ef ON ef.feedback_id=efa.feedback_id "
        "JOIN objects o_ef ON o_ef.object_id=ef.object_id "
        "WHERE efa.anchor_object_id=? AND ef.disposition IS NULL "
        "ORDER BY efa.feedback_id DESC LIMIT 8",
        (target_oid,),
    ).fetchall()
    for r in rows:
        head_first_line = (r["head"] or "").split("\n", 1)[0][:160]
        sources.append(
            {
                "kind": "anchored_harvest",
                "body": f"{r['ef_alias']} [{r['anchor_role']} {target_alias}] {head_first_line}",
                "source_alias": r["ef_alias"],
            }
        )

    # 2. Decisions citing target via decision_supports.cited_object_id.
    rows = conn.execute(
        "SELECT o_dv.alias AS dv_alias, ds.basis, "
        "       SUBSTR(ta.text, 1, 160) AS claim "
        "FROM decision_supports ds "
        "JOIN decisions_v2 dv ON dv.decision_v2_id=ds.decision_v2_id "
        "JOIN objects o_dv ON o_dv.object_id=dv.object_id "
        "JOIN text_atoms ta ON ta.atom_id=ds.claim_atom_id "
        "WHERE ds.cited_object_id=? "
        "ORDER BY dv.decision_v2_id DESC LIMIT 5",
        (target_oid,),
    ).fetchall()
    for r in rows:
        sources.append(
            {
                "kind": "decision_citing",
                "body": f"{r['dv_alias']} basis={r['basis']} claim={r['claim']}",
                "source_alias": r["dv_alias"],
            }
        )

    # 3. Active spec_versions where a decision_effects row links the target
    # decision to the spec_version (i.e., the spec is descended-from a
    # decision the agent is acting on). Review-finding S195 iter-1 medium
    # fix: the prior query had a self-equality bug that reduced to
    # sv.object_id=? and only matched specs that ARE the target.
    rows = conn.execute(
        "SELECT sv.spec_id, sv.version, sv.body_path "
        "FROM spec_versions sv "
        "JOIN decision_effects de ON de.target_object_id=sv.object_id "
        "JOIN decisions_v2 dv ON dv.decision_v2_id=de.decision_v2_id "
        "WHERE sv.status='active' "
        "  AND dv.object_id=? "
        "ORDER BY sv.spec_id",
        (target_oid,),
    ).fetchall()
    for r in rows:
        sources.append(
            {
                "kind": "active_spec",
                "body": f"SPEC-{r['spec_id']}-v{r['version']} body_path={r['body_path']}",
                "source_alias": f"SPEC-{r['spec_id']}-v{r['version']}",
            }
        )

    # 4. Recent supersessions where target is a superseded or successor.
    rows = conn.execute(
        "SELECT o_succ.alias AS succ_alias, o_sup.alias AS sup_alias "
        "FROM decision_effects de "
        "JOIN decisions_v2 dv ON dv.decision_v2_id=de.decision_v2_id "
        "JOIN objects o_succ ON o_succ.object_id=dv.object_id "
        "LEFT JOIN objects o_sup ON o_sup.object_id=de.target_object_id "
        "WHERE de.effect_kind='supersedes' "
        "  AND (de.target_object_id=? OR dv.object_id=?) "
        "ORDER BY dv.decision_v2_id DESC LIMIT 3",
        (target_oid, target_oid),
    ).fetchall()
    for r in rows:
        sources.append(
            {
                "kind": "supersession",
                "body": f"{r['succ_alias']} supersedes {r['sup_alias']}",
                "source_alias": r["succ_alias"],
            }
        )

    return sources


def _render_pack(
    target_aliases: List[str], floor_aliases: List[str], per_target: dict
) -> str:
    lines = [
        "# Assessment context pack (S195 DV-S195-1, T-38)",
        "",
        "Substrate-presented context for the open session; agents must read this "
        "before submitting the assessment. The receipt nonce binds this packet "
        "to the assessment-submit (single-use atomic-consume).",
        "",
        f"## Substrate-presented floor",
        "",
    ]
    if floor_aliases:
        lines.append("Undisposed forward-references + open HIGH-priority issues:")
        for a in floor_aliases:
            lines.append(f"- {a}")
    else:
        lines.append("(no undisposed FRs or open HIGH OIs at this time)")
    lines.append("")

    lines.append(f"## Targets ({len(target_aliases)})")
    lines.append("")
    if not target_aliases:
        lines.append("(no --target provided; pack scoped to the floor only)")
        lines.append("")
        return "\n".join(lines).rstrip() + "\n"

    for ta in target_aliases:
        lines.append(f"### {ta}")
        lines.append("")
        srcs = per_target.get(ta, [])
        if not srcs:
            lines.append(
                f"(no anchored harvest, citing decisions, active specs, or "
                f"supersessions found for {ta}; if alias is an issue or FR it "
                f"does not register in objects.alias per DV-S189-1)"
            )
            lines.append("")
            continue
        by_kind: dict[str, list[dict]] = {}
        for s in srcs:
            by_kind.setdefault(s["kind"], []).append(s)
        for kind in (
            "anchored_harvest",
            "decision_citing",
            "active_spec",
            "supersession",
            "unresolved_target",
        ):
            if not by_kind.get(kind):
                continue
            lines.append(f"**{kind}**")
            for s in by_kind[kind]:
                lines.append(f"- {s['body']}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def cmd_context(args) -> int:
    """bin/selvedge context [--target <alias>]* [--print]

    Renders the assessment-precheck context pack, computes context_sha256,
    inserts one assessment_prechecks row for the open session, and prints
    the pack body + nonce to stdout. The agent embeds the nonce in the
    subsequent `bin/selvedge submit assessment --payload {... "precheck_nonce":
    "..."}` call. T-38 in the assessment handler refuses without nonce or on
    nonce/sha256/freshness/single-use mismatch.

    Substrate-presented floor: undisposed FRs + open HIGH OIs (always
    included). Named --target narrows or adds; the floor is mandatory.
    """
    targets: List[str] = list(args.target or [])
    conn = sqlite3.connect(str(db_path()))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")

    try:
        session_id = _open_session_id(conn)
        floor_aliases = _gather_substrate_floor(conn)

        per_target: dict[str, List[dict]] = {}
        for ta in targets:
            oid = _resolve_target_alias(conn, ta)
            per_target[ta] = _gather_target_context(conn, ta, oid)

        body = _render_pack(targets, floor_aliases, per_target)
        context_sha = hashlib.sha256(body.encode("utf-8")).hexdigest()
        nonce = secrets.token_hex(16)
        targets_json = json.dumps({"targets": targets, "floor": floor_aliases})

        conn.execute("BEGIN")
        cur = conn.execute(
            "INSERT INTO assessment_prechecks "
            "(session_id, targets_json, context_sha256, context_md, nonce, "
            " ttl_seconds, walker_version) VALUES (?,?,?,?,?,?,?)",
            (
                session_id,
                targets_json,
                context_sha,
                body,
                nonce,
                CONTEXT_DEFAULT_TTL,
                CONTEXT_WALKER_VERSION,
            ),
        )
        precheck_id = cur.lastrowid
        conn.commit()
    except SelvedgeError:
        conn.rollback()
        raise
    finally:
        conn.close()

    if getattr(args, "print_stdout", False):
        print(body)
    print(
        f"precheck_id={precheck_id} nonce={nonce} "
        f"context_sha256={context_sha} ttl_seconds={CONTEXT_DEFAULT_TTL} "
        f"targets={len(targets)} floor={len(floor_aliases)}"
    )
    return 0
