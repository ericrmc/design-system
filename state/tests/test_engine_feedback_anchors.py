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


# Note: orient surfacing tests removed in S195 per DV-S195-1 — the
# relevant_history_anchored section was relocated to assessment-time
# (T-38 substrate-gate) per operator-named-mandate at S194-close. The
# engine_feedback_anchors typed-FK graph is now consumed by the
# bin/selvedge context CLI; tests for that flow live in
# test_assessment_precheck.py.
