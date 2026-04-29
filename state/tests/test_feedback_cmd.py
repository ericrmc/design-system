"""Tests for `bin/selvedge feedback` (DV-S122-1).

Two paths to cover:
- Open-session passthrough: a session is already open; the wrapper just
  submits an engine_feedback row in that session.
- Intake-session wrapping: no session is open; the wrapper opens a
  kind=meta intake session, submits the EF, writes a close-record, and
  closes the session — all in one write_tx.
"""
from __future__ import annotations

import json
import sqlite3

from conftest import PRIMARY_DB, _run_cli


def _close_open_session() -> None:
    """Close whatever session clean_substrate left open so we can exercise
    the no-session intake path."""
    cr = _run_cli(
        [
            "submit",
            "close-record",
            "--payload",
            json.dumps(
                {
                    "summary": "test fixture close to clear the open session before exercising the feedback wrapper.",
                    "items": [
                        {"facet": "engine_version", "text": "engine-v17 unchanged in fixture close-record."},
                        {"facet": "what_was_done", "text": "fixture-only: closed pytest seed session before feedback wrapper test."},
                        {"facet": "state_at_close", "text": "no substrate writes in fixture close-record."},
                        {"facet": "next_session_should", "text": "fixture-only: feedback wrapper test will open the next session."},
                        {"facet": "validator_summary", "text": "fixture not exercised by validator."},
                    ],
                }
            ),
        ]
    )
    assert cr["rc"] == 0, cr
    sc = _run_cli(["submit", "session-close", "--payload", "{}"])
    assert sc["rc"] == 0, sc


def test_feedback_passthrough_uses_open_session(clean_substrate):
    res = _run_cli([
        "feedback",
        "passthrough body for the engine-feedback wrapper test fixture.",
        "--flag", "observation",
    ])
    assert res["rc"] == 0, res
    assert res["out"]["ok"] is True
    assert res["out"]["result"]["intake_session"] is False
    assert res["out"]["result"]["engine_feedback"]["flag"] == "observation"
    # No new session opened — only one open session in the substrate (the fixture).
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        n_open = conn.execute(
            "SELECT COUNT(*) FROM sessions WHERE status='open'"
        ).fetchone()[0]
        n_ef = conn.execute("SELECT COUNT(*) FROM engine_feedback").fetchone()[0]
    finally:
        conn.close()
    assert n_open == 1
    assert n_ef == 1


def test_feedback_intake_wraps_meta_session(clean_substrate):
    _close_open_session()
    res = _run_cli([
        "feedback",
        "intake body for the engine-feedback wrapper test fixture.",
        "--flag", "blocker",
    ])
    assert res["rc"] == 0, res
    assert res["out"]["ok"] is True
    assert res["out"]["result"]["intake_session"] is True
    sess_info = res["out"]["result"]["session"]
    assert sess_info["slug"].startswith("feedback-intake-")
    ef_alias = res["out"]["result"]["engine_feedback"]["alias"]
    # All four substrate rows landed atomically in one write_tx.
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        n_open = conn.execute(
            "SELECT COUNT(*) FROM sessions WHERE status='open'"
        ).fetchone()[0]
        slug = conn.execute(
            "SELECT slug FROM sessions WHERE session_id=?",
            (sess_info["session_id"],),
        ).fetchone()[0]
        flag = conn.execute(
            "SELECT flag FROM engine_feedback ORDER BY feedback_id DESC LIMIT 1"
        ).fetchone()[0]
        n_close = conn.execute(
            "SELECT COUNT(*) FROM close_records WHERE session_id=?",
            (sess_info["session_id"],),
        ).fetchone()[0]
    finally:
        conn.close()
    # The intake session must be closed by the wrapper — no lingering open.
    assert n_open == 0
    assert slug == sess_info["slug"]
    assert flag == "blocker"
    assert n_close == 1
    assert ef_alias.startswith("EF-S")


def test_feedback_dry_run_persists_nothing(clean_substrate):
    _close_open_session()
    res = _run_cli([
        "feedback",
        "dry-run body for the engine-feedback wrapper test fixture.",
        "--flag", "observation",
        "--dry-run",
    ])
    assert res["rc"] == 0, res
    assert res["out"]["ok"] is True
    assert res["out"].get("dry_run") is True
    # Nothing should have persisted: no engine_feedback row, no new session.
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        n_ef = conn.execute("SELECT COUNT(*) FROM engine_feedback").fetchone()[0]
        n_open = conn.execute(
            "SELECT COUNT(*) FROM sessions WHERE status='open'"
        ).fetchone()[0]
    finally:
        conn.close()
    assert n_ef == 0
    assert n_open == 0


def test_feedback_refuses_empty_body(clean_substrate):
    res = _run_cli(
        ["feedback", "   ", "--flag", "observation"],
        expect_ok=False,
    )
    assert res["rc"] == 3
    err = json.loads(res["err"])
    assert err["code"] == "E_VALIDATION"
    assert "empty" in err["detail"].lower()


import pytest


@pytest.mark.parametrize(
    "bad_slug",
    [
        "../../etc",       # path traversal
        "Feedback",        # uppercase
        "feed_back",       # underscore
        "-leading",        # leading hyphen
        "trailing-",       # trailing hyphen
        "double--hyphen",  # double hyphen
        "1leading-digit",  # digit-start
        "with space",      # space
        "trailing\n",      # trailing newline (reviewer iter-2 H-1)
        "embed\nnewline",  # embedded newline
        "",                # empty
    ],
)
def test_feedback_refuses_malformed_slug(clean_substrate, bad_slug):
    """Reviewer iter-1 H-2 + iter-2 H-1: --slug must reject everything that
    is not strict kebab-case ASCII, including embedded/trailing newlines that
    re.match would accept under $-anchoring (fullmatch closes the gap)."""
    _close_open_session()
    # `--slug=<value>` form (not `--slug <value>`) so argparse does not
    # interpret a leading-hyphen slug as a separate flag.
    res = _run_cli(
        [
            "feedback",
            "body for the slug-validation test fixture.",
            f"--slug={bad_slug}",
        ],
        expect_ok=False,
    )
    assert res["rc"] == 3, (bad_slug, res)
    err = json.loads(res["err"])
    assert err["code"] == "E_VALIDATION"


@pytest.mark.parametrize(
    "good_slug",
    [
        "feedback-intake-test",
        "f",                            # single letter
        "a-1",                          # alpha-digit
        "valid-kebab-with-many-parts",
    ],
)
def test_feedback_accepts_valid_kebab_slug(clean_substrate, good_slug):
    _close_open_session()
    res = _run_cli([
        "feedback",
        "body for the kebab-acceptance test fixture.",
        "--slug",
        good_slug,
    ])
    assert res["rc"] == 0, (good_slug, res)
    assert res["out"]["result"]["session"]["slug"] == good_slug


def test_feedback_intake_slug_includes_microseconds(clean_substrate):
    """Reviewer iter-1 H-1: bursty concurrent calls must not collide on the
    same-second slug. Microsecond precision is in the auto-slug shape."""
    _close_open_session()
    res = _run_cli([
        "feedback",
        "intake body for the microsecond-slug test fixture.",
    ])
    assert res["rc"] == 0, res
    slug = res["out"]["result"]["session"]["slug"]
    # Format: feedback-intake-YYYYMMDD-HHMMSS-ffffff (last block is 6 digits).
    parts = slug.split("-")
    assert parts[0] == "feedback" and parts[1] == "intake"
    assert len(parts[-1]) == 6, f"expected 6-digit microsecond suffix, got {slug!r}"
    assert parts[-1].isdigit(), f"microsecond suffix not digits: {slug!r}"
