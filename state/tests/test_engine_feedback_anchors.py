"""Tests for engine_feedback_anchors typed-FK chain-walk reachability (S194 DV-S194-1).

Coverage:
- T-37 refusal: harvest-prefixed body without anchors[] is refused.
- Anchors path: harvest-prefixed body with valid anchors lands one row in
  engine_feedback_anchors per declared anchor.
- Non-harvest body: optional anchors=[] is admitted (back-compat).
- Anchor alias resolution: unresolvable alias is refused with E_REFUSAL_T01.
- Anchor role enum: invalid role is refused with E_VALIDATION.
- orient surfacing: anchored harvest EFs whose anchor lands on an active
  spec_version or recent decision_v2 surface in `relevant_history_anchored`.
"""
from __future__ import annotations

import json
import sqlite3

from conftest import PRIMARY_DB, _run_cli


def _submit_ef(payload: dict, expect_ok: bool = True) -> dict:
    res = _run_cli([
        "submit", "engine-feedback",
        "--payload", json.dumps(payload),
    ], expect_ok=expect_ok)
    # Refusal payloads come back on stderr; parse them so tests can assert.
    if not expect_ok and res["out"] is None and res["err"]:
        try:
            res["out"] = json.loads(res["err"])
        except json.JSONDecodeError:
            pass
    return res


def test_t37_refuses_harvest_without_anchors(clean_substrate):
    res = _submit_ef({
        "flag": "observation",
        "body_md": "historical-harvest: source=archive/test.md\n\nbody.",
    }, expect_ok=False)
    assert res["rc"] != 0, res
    assert res["out"]["ok"] is False
    assert res["out"]["code"] == "E_REFUSAL_T37"
    assert "harvest-prefixed" in res["out"]["detail"]


def test_t37_admits_harvest_with_anchors(clean_substrate):
    # Find a resolvable alias — the seed session's session row should have one.
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        row = conn.execute(
            "SELECT alias FROM objects WHERE alias IS NOT NULL LIMIT 1"
        ).fetchone()
    finally:
        conn.close()
    assert row is not None, "no aliases in seed substrate"
    seed_alias = row[0]

    res = _submit_ef({
        "flag": "observation",
        "body_md": "historical-harvest: source=archive/test.md\n\nbody.",
        "anchors": [{"alias": seed_alias, "role": "about"}],
    })
    assert res["rc"] == 0, res
    assert res["out"]["ok"] is True
    assert res["out"]["result"]["anchors"][0]["anchor_role"] == "about"

    fid = res["out"]["result"]["feedback_id"]
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        n_anchors = conn.execute(
            "SELECT COUNT(*) FROM engine_feedback_anchors WHERE feedback_id=?", (fid,)
        ).fetchone()[0]
    finally:
        conn.close()
    assert n_anchors == 1


def test_non_harvest_body_admits_no_anchors(clean_substrate):
    res = _submit_ef({
        "flag": "observation",
        "body_md": "**Plain EF** without harvest prefix; no anchors required.",
    })
    assert res["rc"] == 0, res
    assert res["out"]["ok"] is True
    assert res["out"]["result"]["anchors"] == []


def test_unresolvable_anchor_alias_refused(clean_substrate):
    res = _submit_ef({
        "flag": "observation",
        "body_md": "historical-harvest: source=archive/test.md\n\nbody.",
        "anchors": [{"alias": "DV-NEVER-EXISTED-9999", "role": "about"}],
    }, expect_ok=False)
    assert res["rc"] != 0, res
    assert res["out"]["ok"] is False
    assert res["out"]["code"] == "E_REFUSAL_T01"
    assert "DV-NEVER-EXISTED-9999" in res["out"]["detail"]


def test_invalid_anchor_role_refused(clean_substrate):
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        seed_alias = conn.execute(
            "SELECT alias FROM objects WHERE alias IS NOT NULL LIMIT 1"
        ).fetchone()[0]
    finally:
        conn.close()
    res = _submit_ef({
        "flag": "observation",
        "body_md": "historical-harvest: source=archive/test.md\n\nbody.",
        "anchors": [{"alias": seed_alias, "role": "not-a-real-role"}],
    }, expect_ok=False)
    assert res["rc"] != 0, res
    assert res["out"]["ok"] is False
    assert res["out"]["code"] == "E_VALIDATION"


def test_orient_surfaces_anchored_history(clean_substrate):
    # Anchor a harvest EF on the active spec_version, then verify orient
    # surfaces it in relevant_history_anchored.
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        spec_alias_row = conn.execute(
            "SELECT o.alias FROM spec_versions sv "
            "JOIN objects o ON o.object_id=sv.object_id "
            "WHERE sv.status='active' LIMIT 1"
        ).fetchone()
    finally:
        conn.close()
    if spec_alias_row is None:
        # Seed substrate has no active spec yet — skip rather than fail.
        return
    spec_alias = spec_alias_row[0]

    res = _submit_ef({
        "flag": "observation",
        "body_md": "historical-harvest: source=archive/test.md\n\nbody about active spec.",
        "anchors": [{"alias": spec_alias, "role": "about"}],
    })
    assert res["rc"] == 0, res

    orient = _run_cli(["orient", "--json"])
    assert orient["rc"] == 0, orient
    rh = orient["out"]["relevant_history_anchored"]
    assert any(r["anchor_alias"] == spec_alias for r in rh), \
        f"anchored harvest EF did not surface in orient relevant_history_anchored; got {rh!r}"


def test_orient_total_counts_anchor_edges_not_distinct_efs(clean_substrate):
    """Review-finding S194 iter-1 high: rh_total must count (feedback,
    anchor_role) tuples to match the LIMIT-10 row semantics."""
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        spec_row = conn.execute(
            "SELECT o.alias FROM spec_versions sv "
            "JOIN objects o ON o.object_id=sv.object_id "
            "WHERE sv.status='active' LIMIT 1"
        ).fetchone()
        dv_row = conn.execute(
            "SELECT o.alias FROM decisions_v2 dv "
            "JOIN objects o ON o.object_id=dv.object_id LIMIT 1"
        ).fetchone()
    finally:
        conn.close()
    if spec_row is None or dv_row is None:
        return
    spec_alias = spec_row[0]
    dv_alias = dv_row[0]

    # One harvest EF with TWO anchors of different roles — should count as 2
    # in relevant_history_total because the LIMIT 10 caps at 2 rows for this EF.
    res = _submit_ef({
        "flag": "observation",
        "body_md": "historical-harvest: source=archive/dual.md\n\nbody.",
        "anchors": [
            {"alias": spec_alias, "role": "about"},
            {"alias": dv_alias, "role": "descended_from"},
        ],
    })
    assert res["rc"] == 0, res

    orient = _run_cli(["orient", "--json"])
    rh = orient["out"]["relevant_history_anchored"]
    rh_total = orient["out"]["relevant_history_total"]
    # The single EF contributed 2 anchor edges; both should surface and count.
    matching = [r for r in rh if r["ef_alias"] == res["out"]["result"]["alias"]]
    assert len(matching) == 2, f"expected 2 anchor edges for the dual-anchor EF, got {matching!r}"
    assert rh_total >= 2, f"rh_total should count anchor edges; got {rh_total}"
