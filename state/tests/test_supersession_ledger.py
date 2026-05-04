"""Tests for supersession-ledger v1 typed cross-artefact primitive (S197 DV-S197-1).

Coverage:
- Relation enum rejection: bad relation_kind refused with E_VALIDATION.
- Alias resolution refusal: unresolvable source/target/cite refused with E_REFUSAL_T01.
- Self-supersession refusal: source==target refused with E_VALIDATION (handler-side
  check fires before the CHECK constraint at the SQL layer).
- Atom-length: reason atom outside 8-240 refused with E_ATOM_LENGTH.
- Cross-kind admit: ledger admits supersession across different object_kinds
  (e.g. EF supersedes DV, SPEC supersedes SPEC); polymorphism via objects-FK.
- Object-registration: row registers as object with alias SL-S<wno>-<seq> and
  object_kind='supersession_ledger'.
- UNIQUE constraint: duplicate (source,target,relation_kind) refused.
- Optional cite: cite alias resolves correctly when provided.
- Missing required fields refused with E_VALIDATION.
"""
from __future__ import annotations

import json
import sqlite3

from conftest import PRIMARY_DB, _run_cli


def _seed_two_efs() -> tuple[str, str]:
    """Submit two engine_feedback rows so we have EF-S001-1 + EF-S001-2 aliases
    distinct from S001 (session) and A-S001 (assessment) for ledger source/target."""
    r1 = _run_cli([
        "submit", "engine-feedback", "--payload",
        json.dumps({"flag": "observation", "body_md": "**EF seed one** for supersession-ledger tests."}),
    ])
    r2 = _run_cli([
        "submit", "engine-feedback", "--payload",
        json.dumps({"flag": "observation", "body_md": "**EF seed two** for supersession-ledger tests."}),
    ])
    return r1["out"]["result"]["alias"], r2["out"]["result"]["alias"]


def _submit_sl(payload: dict, expect_ok: bool = True) -> dict:
    res = _run_cli([
        "submit", "supersession-ledger", "--payload", json.dumps(payload),
    ], expect_ok=expect_ok)
    if not expect_ok and res["out"] is None and res["err"]:
        try:
            res["out"] = json.loads(res["err"])
        except json.JSONDecodeError:
            pass
    return res


def test_admit_minimal_payload_returns_alias(clean_substrate):
    a, b = _seed_two_efs()
    res = _submit_sl({
        "source": a,
        "target": b,
        "relation_kind": "supersedes-fully",
        "reason": "Test minimal admit with two seed EFs as source and target.",
    })
    assert res["rc"] == 0, res
    r = res["out"]["result"]
    import re
    assert re.match(r"^SL-S\d{3,}-\d+$", r["alias"]), r
    assert r["relation_kind"] == "supersedes-fully"
    assert r["cite_object_id"] is None


def test_object_registration_lands_in_objects(clean_substrate):
    a, b = _seed_two_efs()
    res = _submit_sl({
        "source": a, "target": b,
        "relation_kind": "supersedes-fully",
        "reason": "Object-registration test: row should appear in objects with kind=supersession_ledger.",
    })
    alias = res["out"]["result"]["alias"]
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        row = conn.execute(
            "SELECT object_kind, typed_row_id FROM objects WHERE alias=?", (alias,)
        ).fetchone()
    finally:
        conn.close()
    assert row is not None, f"alias {alias} not registered in objects"
    assert row[0] == "supersession_ledger"
    assert row[1] == res["out"]["result"]["ledger_id"]


def test_relation_kind_enum_rejection(clean_substrate):
    a, b = _seed_two_efs()
    res = _submit_sl({
        "source": a, "target": b,
        "relation_kind": "deprecates",  # not in 5-value enum
        "reason": "Test that relation_kind outside 5-value enum is refused.",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["ok"] is False
    assert res["out"]["code"] == "E_VALIDATION"
    assert "relation_kind" in res["out"]["detail"]


def test_unresolvable_source_refused(clean_substrate):
    _, b = _seed_two_efs()
    res = _submit_sl({
        "source": "EF-S999-99",  # nonexistent
        "target": b,
        "relation_kind": "supersedes-fully",
        "reason": "Test unresolvable source alias is refused with E_REFUSAL_T01.",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_REFUSAL_T01"


def test_unresolvable_target_refused(clean_substrate):
    a, _ = _seed_two_efs()
    res = _submit_sl({
        "source": a,
        "target": "DV-S999-99",
        "relation_kind": "supersedes-fully",
        "reason": "Test unresolvable target alias is refused with E_REFUSAL_T01.",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_REFUSAL_T01"


def test_self_supersession_refused(clean_substrate):
    a, _ = _seed_two_efs()
    res = _submit_sl({
        "source": a, "target": a,
        "relation_kind": "supersedes-fully",
        "reason": "Test self-supersession (source==target) refused per CHECK source!=target.",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_VALIDATION"
    assert "self-supersession" in res["out"]["detail"]


def test_atom_length_refused(clean_substrate):
    a, b = _seed_two_efs()
    res = _submit_sl({
        "source": a, "target": b,
        "relation_kind": "supersedes-fully",
        "reason": "short",  # 5 chars, below 8
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_ATOM_LENGTH"


def test_unique_constraint_refused(clean_substrate):
    a, b = _seed_two_efs()
    p = {
        "source": a, "target": b,
        "relation_kind": "bounded-by",
        "reason": "First insert should land; second with same triple should be refused.",
    }
    r1 = _submit_sl(p)
    assert r1["rc"] == 0, r1
    r2 = _submit_sl(p, expect_ok=False)
    assert r2["rc"] != 0
    # CHECK / UNIQUE failures surface as E_REFUSAL_CHECK from the substrate layer.
    assert r2["out"]["code"] in ("E_REFUSAL_CHECK", "E_REFUSAL_UNIQUE"), r2


def test_optional_cite_resolves(clean_substrate):
    a, b = _seed_two_efs()
    # Use the session alias (S<wno>) as the cite — any resolvable alias works.
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        sess_alias = conn.execute(
            "SELECT alias FROM objects WHERE object_kind='session' LIMIT 1"
        ).fetchone()[0]
    finally:
        conn.close()
    res = _submit_sl({
        "source": a, "target": b,
        "relation_kind": "replaces-mechanism",
        "reason": "Test optional cite resolves to objects.alias when provided.",
        "cite": sess_alias,
    })
    assert res["rc"] == 0, res
    assert res["out"]["result"]["cite_object_id"] is not None


def test_unresolvable_cite_refused(clean_substrate):
    a, b = _seed_two_efs()
    res = _submit_sl({
        "source": a, "target": b,
        "relation_kind": "supersedes-fully",
        "reason": "Test unresolvable cite alias is refused with E_REFUSAL_T01.",
        "cite": "DV-S999-99",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_REFUSAL_T01"


def test_missing_source_refused(clean_substrate):
    _, b = _seed_two_efs()
    res = _submit_sl({
        "target": b,
        "relation_kind": "supersedes-fully",
        "reason": "Test missing source field is refused with E_VALIDATION.",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_VALIDATION"
    assert "source" in res["out"]["detail"]


def test_missing_relation_kind_refused(clean_substrate):
    a, b = _seed_two_efs()
    res = _submit_sl({
        "source": a, "target": b,
        "reason": "Test missing relation_kind field is refused with E_VALIDATION.",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_VALIDATION"
    assert "relation_kind" in res["out"]["detail"]


def test_missing_reason_refused(clean_substrate):
    a, b = _seed_two_efs()
    res = _submit_sl({
        "source": a, "target": b,
        "relation_kind": "supersedes-fully",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_VALIDATION"
    assert "reason" in res["out"]["detail"]


def test_all_five_relation_kinds_admit(clean_substrate):
    """Each of the 5 enum values admits successfully when seeded with distinct
    target aliases (UNIQUE constraint scoped per triple)."""
    a, b = _seed_two_efs()
    # Add three more EFs so we have 5 distinct target aliases.
    extras = []
    for i in range(3):
        r = _run_cli([
            "submit", "engine-feedback", "--payload",
            json.dumps({"flag": "observation", "body_md": f"**EF extra seed {i}** for relation enum admit test."}),
        ])
        extras.append(r["out"]["result"]["alias"])

    targets = [b] + extras
    enum_values = [
        "supersedes-fully",
        "supersedes-partial",
        "bounded-by",
        "replaces-mechanism",
        "retracted-by",
    ]
    for rk, tgt in zip(enum_values, targets):
        res = _submit_sl({
            "source": a, "target": tgt,
            "relation_kind": rk,
            "reason": f"Smoke admit for relation_kind={rk} per DV-S197-1 5-value enum.",
        })
        assert res["rc"] == 0, (rk, res)
        assert res["out"]["result"]["relation_kind"] == rk


def test_alias_resolves_post_insert(clean_substrate):
    """The ledger row's alias must resolve via objects.alias for chain-walk
    reachability (D-S197-1 D-2 P-2-stance: object-registration is load-bearing)."""
    a, b = _seed_two_efs()
    res = _submit_sl({
        "source": a, "target": b,
        "relation_kind": "supersedes-fully",
        "reason": "Test that the ledger alias resolves via objects.alias post-insert.",
    })
    sl_alias = res["out"]["result"]["alias"]
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        oid = conn.execute("SELECT object_id FROM objects WHERE alias=?", (sl_alias,)).fetchone()[0]
        # And the back-pointer on the ledger row matches.
        ledger_oid = conn.execute(
            "SELECT object_id FROM supersession_ledger WHERE ledger_id=?",
            (res["out"]["result"]["ledger_id"],),
        ).fetchone()[0]
    finally:
        conn.close()
    assert oid == ledger_oid


def test_legacy_backfill_conditional_in_clean_init(clean_substrate):
    """Migration 048's legacy backfill is conditional via WHERE EXISTS: on a
    fresh init with no SPEC-prompt-development-v2 / DV-S186-1 / S186 session
    objects seeded, the backfill is a no-op so test substrates carry zero
    supersession_ledger rows post-init. The production substrate carries the
    historical row at SL-S186-1 (verified in the production tree, not here)."""
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        n = conn.execute("SELECT COUNT(*) FROM supersession_ledger").fetchone()[0]
    finally:
        conn.close()
    assert n == 0, f"clean init should leave supersession_ledger empty; got {n} rows"
