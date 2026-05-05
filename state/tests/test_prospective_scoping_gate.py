"""Tests for T-41 prospective-scoping close-record gate (S199 DV-S199-1).

Coverage:
- Pure-meta session (no substantive DV/migration/spec_version) admits close-record
  without prospective-scoping receipt.
- Session with substantive DV refused close-record without receipt.
- Receipt path (a): assumption_ledger row with origin_decision pointing to a
  session DV satisfies the gate.
- Receipt path (b): engine_feedback row with body_md prefix 'scoping-pass:'
  satisfies the gate.
- Cheap-exit nil_attestation 'scoping-pass: 0' must contain 'exclusions applied:'.
- Substantive-DV nil_attestation must mention ≥1 of three implication patterns.
- Body_md case-insensitivity: 'Scoping-Pass:' admits same as 'scoping-pass:'.
- Prefix detection trims leading whitespace.
"""
from __future__ import annotations

import json
import sqlite3

from conftest import _run_cli, WORKSPACE


def _open_session_alias(db_path) -> str:
    """Look up the alias of the conftest-opened session (init_session_offset
    varies; session_no=1 may map to S001, S180, S199, etc. depending on the
    substrate's offset setting at init time)."""
    conn = sqlite3.connect(str(db_path))
    try:
        row = conn.execute(
            "SELECT alias FROM objects WHERE object_kind='session' ORDER BY object_id DESC LIMIT 1"
        ).fetchone()
    finally:
        conn.close()
    assert row is not None, "no open session in clean_substrate"
    return row[0]


def _seed_substantive_dv(db_path) -> str:
    """Submit a kind=substantive decision-record to make the session substantive.

    Uses target_kind='process_rule' (not 'decision_v2') so the precheck and the
    decision-record agree per T-33. Cites the conftest session alias so T-34
    admits the operator_directive basis with a non-NULL cited_object_id.
    """
    import re
    pre = _run_cli(["precheck", "--target-kind", "process_rule", "--target-key", "test-substantive-rule"])
    raw = pre["out"]["_raw"] if isinstance(pre["out"], dict) and "_raw" in pre["out"] else (pre["out"] or "")
    if not isinstance(raw, str):
        raw = str(raw)
    m = re.search(r"nonce=(\S+)", raw)
    assert m, f"could not parse nonce from precheck output: {raw!r}"
    nonce = m.group(1)
    sess_alias = _open_session_alias(db_path)
    res = _run_cli([
        "submit", "decision-record", "--payload", json.dumps({
            "title": "Seed substantive decision-record so the close-record gate fires for tests.",
            "kind": "substantive",
            "precheck_nonce": nonce,
            "outcome_type": "adopt",
            "target_kind": "process_rule",
            "target_key": "test-substantive-rule",
            "supports": [{"basis": "operator_directive", "claim": "Test-only seeded support claim citing the session for cited_object_id resolution.", "cite": sess_alias}],
            "effects": [{"effect_kind": "creates", "target_descriptor": "test fixture rule"}],
            "alternatives": [{"label": "R-1.1", "option": "Alternative the test rejects so T-19 admits.", "rejections": [{"basis": "inferior_tradeoff", "reason": "test-only rejection reason"}]}],
        }),
    ])
    return res["out"]["result"]["alias"]


def _seed_procedural_dv() -> str:
    """A procedural kind decision does NOT make the session substantive."""
    res = _run_cli([
        "submit", "decision-record", "--payload", json.dumps({
            "title": "Seed procedural decision-record (kind=procedural; not substantive).",
            "kind": "procedural",
            "outcome_type": "adopt",
            "target_kind": "process_rule",
            "target_key": "test-procedural-rule",
            "supports": [],
            "effects": [],
            "alternatives": [],
        }),
    ])
    return res["out"]["result"]["alias"]


def _close_record_attempt(scoping_body: str | None = None, lift_ar_for_dv: str | None = None) -> dict:
    """Submit a close-record. Optionally pre-submit a scoping-pass EF or lift an
    AR row tied to a session DV to satisfy the gate."""
    if scoping_body is not None:
        ef = _run_cli([
            "submit", "engine-feedback", "--payload",
            json.dumps({"flag": "observation", "body_md": scoping_body}),
        ])
        assert ef["rc"] == 0
    if lift_ar_for_dv is not None:
        ar = _run_cli([
            "submit", "assumption", "--payload",
            json.dumps({
                "statement": "Test lift attached to DV; satisfies T-41 path (a) without scoping-pass body.",
                "origin_decision": lift_ar_for_dv,
            }),
        ])
        assert ar["rc"] == 0
    res = _run_cli([
        "submit", "close-record", "--payload", json.dumps({
            "summary": "Test close-record summary atom for T-41 gate test fixtures.",
            "items": [{"facet": "what_was_done", "text": "Test close item required by T-19 (non-empty items)."}],
        }),
    ], expect_ok=False)
    if res["out"] is None and res["err"]:
        try:
            res["out"] = json.loads(res["err"])
        except json.JSONDecodeError:
            pass
    return res


def test_pure_meta_session_admits_without_receipt(clean_substrate):
    """A session with NO substantive DV / spec_version admits close-record."""
    _seed_procedural_dv()  # not substantive — kind=procedural
    res = _close_record_attempt()
    assert res["rc"] == 0, res


def test_substantive_session_refused_without_receipt(clean_substrate, db_path):
    """A session with a substantive DV but no scoping receipt is refused."""
    _seed_substantive_dv(db_path)
    res = _close_record_attempt()
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_REFUSAL_T41"
    assert "prospective-scoping receipt" in res["out"]["detail"]


def test_receipt_path_a_ar_row_with_session_dv(clean_substrate, db_path):
    """Receipt path (a): AR row with origin_decision pointing to a session DV
    satisfies the gate without any scoping-pass: prose."""
    dv = _seed_substantive_dv(db_path)
    res = _close_record_attempt(lift_ar_for_dv=dv)
    assert res["rc"] == 0, res


def test_receipt_path_b_scoping_pass_efbody(clean_substrate, db_path):
    """Receipt path (b): engine_feedback row with prefix 'scoping-pass:'
    satisfies the gate (full body, not nil_attestation)."""
    _seed_substantive_dv(db_path)
    body = (
        "scoping-pass: 1 — patterns considered: schema-adjacency, caller-implications; "
        "lifts: AR-S199-1; reviewed engine_feedback substrate writes for caller-implication seams."
    )
    res = _close_record_attempt(scoping_body=body)
    assert res["rc"] == 0, res


def test_nil_attestation_requires_exclusions_applied(clean_substrate, db_path):
    """scoping-pass: 0 nil_attestation must contain 'exclusions applied:' substring
    per codex guard #1."""
    _seed_substantive_dv(db_path)
    body = "scoping-pass: 0 — no implications surfaced this round; closure attestation."
    res = _close_record_attempt(scoping_body=body)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_REFUSAL_T41"
    assert "exclusions applied" in res["out"]["detail"]


def test_substantive_nil_must_name_implication_pattern(clean_substrate, db_path):
    """Per codex guard #2: when session produced a substantive DV, the nil
    body must mention ≥1 of {schema-adjacency, caller-implications,
    migration-implications}."""
    _seed_substantive_dv(db_path)
    body = (
        "scoping-pass: 0 — exclusions applied: no executable artefacts produced this round; "
        "spec-only changes covered by §8.5 audit-step prose."
    )
    res = _close_record_attempt(scoping_body=body)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_REFUSAL_T41"
    assert "implication patterns" in res["out"]["detail"]


def test_substantive_nil_with_implication_pattern_admits(clean_substrate, db_path):
    """Substantive-DV nil naming an implication pattern admits."""
    _seed_substantive_dv(db_path)
    body = (
        "scoping-pass: 0 — exclusions applied: no caller-implications surface for this DV "
        "since no API change shipped; schema-adjacency reviewed and out-of-scope."
    )
    res = _close_record_attempt(scoping_body=body)
    assert res["rc"] == 0, res


def test_prefix_case_insensitive(clean_substrate, db_path):
    """Body_md prefix detection is case-insensitive ('Scoping-Pass:' admits)."""
    _seed_substantive_dv(db_path)
    body = (
        "Scoping-Pass: 1 — patterns considered: caller-implications; "
        "lift AR placeholder; capitalisation should not block detection."
    )
    res = _close_record_attempt(scoping_body=body)
    assert res["rc"] == 0, res


def test_prefix_with_leading_whitespace(clean_substrate, db_path):
    """Body_md prefix detection trims leading whitespace before testing prefix."""
    _seed_substantive_dv(db_path)
    body = (
        "   scoping-pass: 1 — patterns considered: schema-adjacency; "
        "lift AR placeholder; leading whitespace should not block detection."
    )
    res = _close_record_attempt(scoping_body=body)
    assert res["rc"] == 0, res


def test_spec_version_makes_session_substantive(clean_substrate):
    """RF-3 fix: a session producing a spec_versions row (no DV) is substantive
    per _session_produced_substantive_artefact() and triggers T-41."""
    # Submit a spec-version v1 (initial; no supersedes); use SELVEDGE_EXPORT_CONTEXT
    # to bypass the refuse-substrate-md hook for the body file write.
    import os, subprocess, sys
    payload = {
        "session_no": 1,
        "spec_id": "test-spec-for-prospective-scoping",
        "version": 1,
        "body_path": "specifications/test-spec-fixture.md",
        "body_md": "# Test spec v1\n\nFixture for T-41 spec_version path tests; not committed to git.",
    }
    env = os.environ.copy()
    env["SELVEDGE_EXPORT_CONTEXT"] = "1"
    env["SELVEDGE_WORKSPACE"] = str(WORKSPACE)
    res = subprocess.run(
        ["bin/selvedge", "submit", "spec-version", "--payload", "-"],
        input=json.dumps(payload), text=True, capture_output=True, env=env,
    )
    assert res.returncode == 0, res.stderr
    # Now attempt close-record without scoping-pass receipt: should refuse.
    cr = _close_record_attempt()
    assert cr["rc"] != 0
    assert cr["out"]["code"] == "E_REFUSAL_T41"
    # Cleanup: remove the test-spec body file so it doesn't pollute git.
    spec_file = WORKSPACE / "specifications" / "test-spec-fixture.md"
    if spec_file.exists():
        spec_file.unlink()


def test_non_nil_body_bypasses_nil_guards(clean_substrate, db_path):
    """RF-4 fix: non-nil scoping-pass: bodies (e.g. 'scoping-pass: 1 ...')
    bypass nil_attestation guards. Even if the body lacks 'exclusions applied:'
    or implication-pattern names, a non-nil count admits."""
    _seed_substantive_dv(db_path)
    body = "scoping-pass: 2 — lifted AR-S001-1 and AR-S001-2; review of generated artefacts found two real implications."
    res = _close_record_attempt(scoping_body=body)
    assert res["rc"] == 0, res


def test_multi_row_first_fails_second_passes(clean_substrate, db_path):
    """RF-2 fix: when multiple scoping-pass: rows exist, the gate admits if any
    row passes all applicable guards. First-row-fails-short-circuit was a bug."""
    _seed_substantive_dv(db_path)
    # Submit a failing row first (nil without exclusions)
    failing = _run_cli([
        "submit", "engine-feedback", "--payload",
        json.dumps({"flag": "observation", "body_md": "scoping-pass: 0 — no exclusions named here; this row should fail guards."}),
    ])
    assert failing["rc"] == 0
    # Submit a passing row second
    passing = _run_cli([
        "submit", "engine-feedback", "--payload",
        json.dumps({"flag": "observation", "body_md": "scoping-pass: 0 — exclusions applied: schema-adjacency reviewed; no implications surfaced for this fixture session."}),
    ])
    assert passing["rc"] == 0
    # close-record should admit because a valid row exists
    res = _run_cli([
        "submit", "close-record", "--payload", json.dumps({
            "summary": "Test close-record summary atom for T-41 multi-row gate test.",
            "items": [{"facet": "what_was_done", "text": "Test close item required by T-19 (non-empty items)."}],
        }),
    ], expect_ok=False)
    if res["out"] is None and res["err"]:
        try:
            res["out"] = json.loads(res["err"])
        except json.JSONDecodeError:
            pass
    assert res["rc"] == 0, res


def test_prefix_with_markdown_bold(clean_substrate, db_path):
    """S200 fix: body_md beginning with markdown-bold (**scoping-pass: ...**)
    is admitted as the §8.6 spec example uses markdown-bold formatting and
    the gate should tolerate the bold prefix."""
    _seed_substantive_dv(db_path)
    body = (
        "**scoping-pass: 1** — patterns considered: schema-adjacency; "
        "lift AR placeholder; markdown-bold prefix should be tolerated by gate."
    )
    res = _close_record_attempt(scoping_body=body)
    assert res["rc"] == 0, res


def test_unrelated_ef_does_not_satisfy_gate(clean_substrate, db_path):
    """An unrelated engine_feedback row (not starting 'scoping-pass:') does not
    satisfy the gate; refusal still fires."""
    _seed_substantive_dv(db_path)
    body = "audit-step: ordinary close-time audit body; this is the §8.5 row, not the scoping-pass row."
    res = _close_record_attempt(scoping_body=body)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_REFUSAL_T41"
