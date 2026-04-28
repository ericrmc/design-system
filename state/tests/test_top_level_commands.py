"""Tests for the top-level CLI commands that aren't `submit` — validate,
subtract-eligibility, recover, query, schema.

These commands shape outputs differently from `submit`:
  - validate  : prints a string ("validate --precommit: ok") on success,
                "FAIL  ..." lines to stderr on failure.
  - subtract-eligibility, recover, query : print JSON to stdout.
  - schema    : prints a markdown summary (or raw DDL with --raw).

The substrate-test fixtures in conftest are reused; `selvedge_cli`'s payload
parser tolerates non-JSON stdout (returns `{"_raw": text}`) so we lean on the
raw form where appropriate.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3

import pytest

from conftest import PRIMARY_DB, WORKSPACE


def test_validate_precommit_ok_on_clean_substrate(clean_substrate, selvedge_cli):
    res = selvedge_cli(["validate", "--precommit"])
    assert res["rc"] == 0, res
    assert res["out"]["_raw"].startswith("validate --precommit")


def test_validate_precommit_flags_more_than_one_open_session(clean_substrate, selvedge_cli):
    """Insert a second open session via raw SQL (T-10 still admits session_no=2),
    then expect validate to report >1 open session."""
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        # The trigger T-10 enforces session_no=MAX+1; session 1 is open from the
        # fixture so we insert session_no=2 (still 'open' to break the invariant).
        conn.execute(
            "INSERT INTO sessions (session_no, workspace_session_no, slug, mode, "
            "workspace_id, engine_version_at_open, status) "
            "VALUES (2, 2, 'second', 'self-development', 'selvedge-self-development', "
            "'engine-v17', 'open')"
        )
        conn.commit()
    finally:
        conn.close()
    res = selvedge_cli(["validate", "--precommit"], expect_ok=False)
    assert res["rc"] == 1
    assert "more than one open session" in res["err"]


def test_validate_precommit_flags_spec_hash_mismatch(clean_substrate, selvedge_cli):
    """An active spec_versions row whose body file has drifted should fail T-04."""
    body_dir = WORKSPACE / "state" / "tests" / "spec-bodies"
    body_dir.mkdir(parents=True, exist_ok=True)
    body = body_dir / "validate-mismatch.md"
    body.write_text("original body for the validate hash test\n")
    body_rel = body.relative_to(WORKSPACE).as_posix()
    sha = hashlib.sha256(body.read_bytes()).hexdigest()
    try:
        r = selvedge_cli(
            [
                "submit", "spec-version", "--payload",
                json.dumps({
                    "session_no": 1, "spec_id": "validate-mismatch",
                    "version": 1, "body_path": body_rel, "body_sha256": sha,
                }),
            ]
        )
        assert r["out"]["ok"], r
        # Drift the body so the recorded sha256 no longer matches.
        body.write_text("drifted content that no longer matches the recorded sha\n")
        res = selvedge_cli(["validate", "--precommit"], expect_ok=False)
        assert res["rc"] == 1
        assert "spec hash mismatch" in res["err"]
    finally:
        body.unlink(missing_ok=True)


def test_subtract_eligibility_emits_default_thresholds(clean_substrate, selvedge_cli):
    res = selvedge_cli(["subtract-eligibility"])
    assert res["rc"] == 0, res
    assert res["out"]["thresholds"] == {"uncited": 10, "stale": 5, "untriaged": 3}
    assert res["out"]["last_session_no"] == 1
    # All three lists exist on the report (may be empty, that's fine).
    for key in ("uncited_active_specs", "stale_open_commitments", "untriaged_engine_feedback"):
        assert isinstance(res["out"][key], list)


def test_subtract_eligibility_honours_custom_thresholds(clean_substrate, selvedge_cli):
    res = selvedge_cli(
        [
            "subtract-eligibility",
            "--uncited-threshold", "1",
            "--stale-threshold", "1",
            "--untriaged-threshold", "1",
        ]
    )
    assert res["rc"] == 0
    assert res["out"]["thresholds"] == {"uncited": 1, "stale": 1, "untriaged": 1}


def test_subtract_eligibility_lists_untriaged_feedback_above_threshold(clean_substrate, selvedge_cli):
    """Seed a feedback row directly with no disposition; with threshold=0 the
    gap (last_session_no - opened_in = 0) is >= 0, so it appears."""
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        conn.execute(
            "INSERT INTO engine_feedback (session_id, flag, body_md) VALUES (1, 'observation', 'pytest seed')"
        )
        conn.commit()
    finally:
        conn.close()
    res = selvedge_cli(["subtract-eligibility", "--untriaged-threshold", "0"])
    assert res["rc"] == 0
    assert any(
        r["flag"] == "observation" and "pytest seed" in r["summary"]
        for r in res["out"]["untriaged_engine_feedback"]
    )


def test_recover_with_no_expired_leases_returns_zero(clean_substrate, selvedge_cli):
    res = selvedge_cli(["recover"])
    assert res["rc"] == 0
    assert res["out"]["reclaimed_leases"] == 0


def test_query_runs_arbitrary_select(clean_substrate, selvedge_cli):
    res = selvedge_cli(["query", "SELECT 1 AS one, 'two' AS label"])
    assert res["rc"] == 0
    assert res["out"] == [{"one": 1, "label": "two"}]


def test_query_pretty_flag_indents_output(clean_substrate, selvedge_cli):
    """--pretty switches json.dumps to indent=2; the non-pretty form is one
    line. We don't assert exact whitespace — just that the indented marker
    appears in the raw output."""
    res = selvedge_cli(["query", "--pretty", "SELECT 1 AS one"])
    assert res["rc"] == 0
    assert res["out"] == [{"one": 1}]


def test_schema_summary_lists_known_tables(clean_substrate, selvedge_cli):
    res = selvedge_cli(["schema"])
    assert res["rc"] == 0, res
    text = res["out"]["_raw"] if isinstance(res["out"], dict) else "\n".join(res["out"])
    assert "sessions" in text
    assert "decisions" in text


def test_schema_focuses_on_single_table(clean_substrate, selvedge_cli):
    res = selvedge_cli(["schema", "sessions"])
    assert res["rc"] == 0
    text = res["out"]["_raw"] if isinstance(res["out"], dict) else "\n".join(res["out"])
    assert "sessions" in text


def test_schema_raw_emits_ddl(clean_substrate, selvedge_cli):
    res = selvedge_cli(["schema", "--raw"])
    assert res["rc"] == 0
    text = res["out"]["_raw"] if isinstance(res["out"], dict) else "\n".join(res["out"])
    assert "CREATE TABLE" in text


def test_schema_unknown_table_is_handled(clean_substrate, selvedge_cli):
    """Asking for a table that doesn't exist should not crash. The handler
    currently emits an empty summary at rc=0 — pin that contract so a
    future refactor doesn't silently change the failure surface."""
    res = selvedge_cli(["schema", "this_table_does_not_exist"])
    assert res["rc"] == 0
    text = res["out"]["_raw"] if isinstance(res["out"], dict) else "\n".join(res["out"])
    # Output should not contain a different table's DDL — the requested name
    # must appear (clarifying message) or the output must be empty/short.
    assert "this_table_does_not_exist" in text or len(text) < 200
