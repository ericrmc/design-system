"""`selvedge feedback` — record an engine-feedback row without operator-orchestrated session ceremony.

If a session is already open, the EF lands in that session (same as
`submit engine-feedback`). If no session is open, this command opens a
`kind=meta` intake session, submits the EF, writes a minimal close
record, and closes the session — all in one write_tx, so the operator
no longer pays the 4-step ceremony cost for a single feedback signal.

Decided in S122 deliberation 13 (P-1 anthropic + P-2 codex converged
on operator-tooling over schema relaxation; engine_feedback.session_id
remains NOT NULL). Surfaced friction: peer disaster-recovery hit this
3 times (S005, S006, S007 — all "session opened solely to record
operator-directed feedback") without ever raising it as an EF, and
this self-dev session nearly repeated the under-exploration pattern.
"""

from __future__ import annotations

import json
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

# Slug must be kebab-case ASCII (1+ chars, lowercase letters/digits/hyphens,
# starts with a letter, no double-hyphen, no path separators). Tightly bound
# because the slug becomes a path segment in `provenance/<wno>-<slug>/` at
# export time — operator-supplied slugs without this guard would admit
# `../` traversal. `_intake_slug()` always produces a string matching
# this pattern.
_SLUG_RE = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")

from .connection import Conn
from .errors import SelvedgeError
from .submit._helpers import _dry_run_var
from .submit.close import _submit_close_record
from .submit.feedback import _submit_engine_feedback
from .submit.session import _submit_session_close, _submit_session_open


def _read_body(arg: str) -> str:
    if arg == "-":
        return sys.stdin.read()
    if arg.startswith("@"):
        return Path(arg[1:]).read_text()
    return arg


def _has_open_session(conn: sqlite3.Connection) -> bool:
    row = conn.execute(
        "SELECT 1 FROM sessions WHERE status='open' LIMIT 1"
    ).fetchone()
    return row is not None


def _intake_slug() -> str:
    # Microsecond resolution + lowercase pads guarantee uniqueness under bursty
    # concurrent calls; %f is microsecond. Reviewer iter-1 H-1: seconds-only
    # resolution would collide under same-second invocations.
    return (
        "feedback-intake-"
        + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-%f")
    )


def _validate_slug(slug: str) -> None:
    # fullmatch (not match) — re.match's $ accepts a single trailing newline,
    # which would survive into the substrate and break provenance/<wno>-<slug>/
    # at export. Reviewer iter-2 H-1.
    if not _SLUG_RE.fullmatch(slug):
        raise SelvedgeError(
            "E_VALIDATION",
            (
                f"slug {slug!r} must be kebab-case ASCII matching "
                f"{_SLUG_RE.pattern} (no path separators, no traversal, "
                f"no embedded newlines)"
            ),
        )


def _wrapped_submit(
    conn: sqlite3.Connection, body: str, flag: str, role: str, slug: str | None
) -> dict:
    if _has_open_session(conn):
        ef = _submit_engine_feedback(
            conn, {"flag": flag, "body_md": body}, role
        )
        return {"intake_session": False, "engine_feedback": ef}

    sopen = _submit_session_open(
        conn, {"slug": slug or _intake_slug(), "kind": "meta"}, role
    )
    ef = _submit_engine_feedback(
        conn, {"flag": flag, "body_md": body}, role
    )
    summary = (
        f"Intake session opened solely to record {ef['alias']} ({flag}) via "
        f"bin/selvedge feedback wrapper."
    )
    close = _submit_close_record(
        conn,
        {
            "summary": summary,
            "items": [
                {
                    "facet": "engine_version",
                    "text": (
                        f"{sopen['engine_version_at_open']} unchanged; "
                        f"intake-only meta session has no executable change."
                    ),
                },
                {
                    "facet": "what_was_done",
                    "text": (
                        f"Recorded {ef['alias']} ({flag}) via bin/selvedge "
                        f"feedback wrapper (DV-S122-1)."
                    ),
                },
                {
                    "facet": "state_at_close",
                    "text": (
                        "Session opened solely to record operator-directed "
                        "engine-feedback; no other substrate writes."
                    ),
                },
                {
                    "facet": "next_session_should",
                    "text": (
                        f"No mandatory follow-up; {ef['alias']} sits in the "
                        f"engine-feedback triage queue for the next session."
                    ),
                },
                {
                    "facet": "validator_summary",
                    "text": (
                        "Validator not exercised mid-wrapper; operator runs "
                        "tools/validate.sh post-commit per workflow."
                    ),
                },
            ],
        },
        role,
    )
    sclose = _submit_session_close(conn, {}, role)
    return {
        "intake_session": True,
        "session": {
            "workspace_session_no": sopen["workspace_session_no"],
            "session_id": sopen["session_id"],
            "slug": sopen["slug"],
        },
        "engine_feedback": ef,
        "close_record": close,
        "session_close": sclose,
    }


def cmd_feedback(args) -> int:
    body = _read_body(args.body).strip()
    if not body:
        print(
            json.dumps(
                {
                    "ok": False,
                    "code": "E_VALIDATION",
                    "detail": "feedback body is empty after read+strip",
                }
            ),
            file=sys.stderr,
        )
        return 3
    flag = args.flag
    role = args.role or "__cli__"
    slug = args.slug
    if slug is not None:
        try:
            _validate_slug(slug)
        except SelvedgeError as e:
            print(
                json.dumps({"ok": False, "code": e.code, "detail": e.detail}),
                file=sys.stderr,
            )
            return 3
    dry_run = bool(getattr(args, "dry_run", False))

    c = Conn.open()
    token = _dry_run_var.set(dry_run)
    try:
        result = c.write_tx(
            lambda conn: _wrapped_submit(conn, body, flag, role, slug),
            dry_run=dry_run,
        )
    except SelvedgeError as e:
        envelope = {"ok": False, "code": e.code, "detail": e.detail}
        if dry_run:
            envelope["dry_run"] = True
        print(json.dumps(envelope), file=sys.stderr)
        return 3
    finally:
        _dry_run_var.reset(token)
        c.close()
    envelope = {"ok": True, "result": result}
    if dry_run:
        envelope["dry_run"] = True
    print(json.dumps(envelope))
    return 0
