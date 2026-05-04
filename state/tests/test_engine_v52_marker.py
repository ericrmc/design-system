"""engine-v52 marker — OI-S081-7 coverage:

- snapshot_catalog.trigger CHECK admits 'deliberation_seal' (migration 044).
- export_manifest table exists with the expected columns + UNIQUE(path).
- workspace_metadata.current_engine_version == 'engine-v52' after migrate.
- take_snapshot('deliberation_seal') succeeds against the widened CHECK.
- take_snapshot accepts keep_reason override; init_refused/init_forced rows
  carry keep_reason='pre_destructive_anchor'.
- The submit dispatcher fires take_snapshot('deliberation_seal') after a
  deliberation-seal commit, with workspace_session_no surfaced.
- export --session N --write writes export_manifest rows for each emitted
  file and re-export replaces (not appends) via UNIQUE(path).
- Stale-file reconciliation removes the corresponding manifest row.

Tests run against an isolated substrate under tmp_path; production state is
never touched.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import sqlite3
import subprocess
from pathlib import Path

import pytest

WORKSPACE = Path(__file__).resolve().parents[2]
BIN = WORKSPACE / "bin" / "selvedge"


def _sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def _run_raw(env: dict, args: list[str], cwd: Path | None = None) -> dict:
    proc = subprocess.run(
        [str(BIN), *args],
        capture_output=True,
        text=True,
        env=env,
        cwd=str(cwd) if cwd else None,
    )
    out = (proc.stdout or "").strip()
    err = (proc.stderr or "").strip()
    parsed = None
    if out:
        try:
            parsed = json.loads(out)
        except json.JSONDecodeError:
            parsed = {"_raw": out}
    return {"rc": proc.returncode, "out": parsed, "err": err}


def _run(env: dict, args: list[str], cwd: Path | None = None) -> dict:
    """S195 DV-S195-1 T-38: auto-inject precheck_nonce when args look like
    `submit assessment --payload <json>` and payload lacks the nonce."""
    if (
        len(args) >= 4 and args[0] == "submit" and args[1] == "assessment"
        and args[2] == "--payload"
    ):
        try:
            payload = json.loads(args[3])
        except json.JSONDecodeError:
            payload = None
        if isinstance(payload, dict) and "precheck_nonce" not in payload:
            ctx = _run_raw(env, ["context", "--print"], cwd=cwd)
            # Review-finding S195 iter-1 high fix: loud-fail on context CLI
            # failure (silent skip would mask real bugs in fixtures).
            assert ctx["rc"] == 0, (
                f"_run: context CLI required for assessment-submit injection "
                f"but failed: rc={ctx['rc']} err={ctx['err']!r}"
            )
            raw_out = ""
            if isinstance(ctx["out"], dict) and "_raw" in ctx["out"]:
                raw_out = ctx["out"]["_raw"]
            import re as _re
            m = _re.search(r"nonce=(\S+)", raw_out)
            assert m, (
                f"_run: context CLI succeeded but no nonce parsed: "
                f"raw_out={raw_out!r}"
            )
            payload["precheck_nonce"] = m.group(1)
            args = ["submit", "assessment", "--payload", json.dumps(payload)]
    return _run_raw(env, args, cwd=cwd)


@pytest.fixture
def isolated(tmp_path):
    """Tmp workspace + tmp snapshots + tmp DB so a full migrate stack lands
    without touching production paths."""
    (tmp_path / "MODE.md").write_text(
        "---\nmode: self-development\nworkspace_id: tmp-engine-v52\n---\n"
    )
    mig_dir = tmp_path / "migrations"
    mig_dir.mkdir()
    for src in (WORKSPACE / "state" / "migrations").iterdir():
        if src.suffix == ".sql":
            shutil.copy(src, mig_dir / src.name)
    db = tmp_path / "selvedge.sqlite"
    snaps = tmp_path / "snapshots"
    existing_pp = os.environ.get("PYTHONPATH", "")
    pp = f"{WORKSPACE}:{existing_pp}" if existing_pp else str(WORKSPACE)
    env = os.environ | {
        "SELVEDGE_WORKSPACE": str(tmp_path),
        "SELVEDGE_DB_PATH": str(db),
        "SELVEDGE_MIGRATIONS_DIR": str(mig_dir),
        "SELVEDGE_SNAPSHOTS_DIR": str(snaps),
        "PYTHONPATH": pp,
    }
    return {"env": env, "db": db, "snaps": snaps, "root": tmp_path}


def _open_session(env: dict, slug: str = "engine-v52-test", kind: str = "spec_only") -> dict:
    return _run(
        env,
        [
            "submit",
            "session-open",
            "--payload",
            json.dumps({"slug": slug, "kind": kind}),
        ],
    )


def test_migration_044_bumps_engine_version_and_creates_export_manifest(isolated):
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    conn = sqlite3.connect(f"file:{isolated['db']}?mode=ro", uri=True)
    try:
        version = conn.execute(
            "SELECT value FROM workspace_metadata WHERE key='current_engine_version'"
        ).fetchone()[0]
        assert version == "engine-v58", version

        # export_manifest table exists with expected columns + UNIQUE(path).
        cols = {
            row[1]: row[2]
            for row in conn.execute("PRAGMA table_info('export_manifest')").fetchall()
        }
        assert {"manifest_id", "session_no", "kind", "path", "sha256",
                "size_bytes", "row_count", "generated_at"}.issubset(cols.keys())
        # UNIQUE(path) is inline in the CREATE TABLE; SQLite auto-creates
        # sqlite_autoindex_export_manifest_<n>. Verify the constraint by
        # attempting a duplicate insert.
        wconn = sqlite3.connect(str(isolated["db"]))
        try:
            wconn.execute(
                "INSERT INTO export_manifest (kind, path, sha256, size_bytes) "
                "VALUES ('assessment', 'fixtures/dup.md', "
                "'0000000000000000000000000000000000000000000000000000000000000000', 0)"
            )
            wconn.commit()
            with pytest.raises(sqlite3.IntegrityError):
                wconn.execute(
                    "INSERT INTO export_manifest (kind, path, sha256, size_bytes) "
                    "VALUES ('assessment', 'fixtures/dup.md', "
                    "'1111111111111111111111111111111111111111111111111111111111111111', 0)"
                )
        finally:
            wconn.close()

        # snapshot_catalog.trigger CHECK admits deliberation_seal.
        sql = conn.execute(
            "SELECT sql FROM sqlite_master WHERE type='table' AND name='snapshot_catalog'"
        ).fetchone()[0]
        assert "deliberation_seal" in sql, sql
    finally:
        conn.close()


def test_take_snapshot_accepts_deliberation_seal(isolated):
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    open_res = _open_session(isolated["env"])
    assert open_res["rc"] == 0, open_res
    wno = open_res["out"]["result"]["workspace_session_no"]

    # Direct call into take_snapshot to confirm the trigger landed.
    import sys
    sys.path.insert(0, str(WORKSPACE))
    from selvedge.snapshots import take_snapshot, VALID_TRIGGERS

    assert "deliberation_seal" in VALID_TRIGGERS

    result = take_snapshot(
        "deliberation_seal",
        source_path=isolated["db"],
        source_session_no=wno,
    )
    assert result is not None
    assert result.exists()

    conn = sqlite3.connect(f"file:{isolated['db']}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute(
            "SELECT * FROM snapshot_catalog WHERE trigger='deliberation_seal'"
        ).fetchone()
    finally:
        conn.close()
    assert row is not None
    assert row["source_session_no"] == wno


def test_take_snapshot_keep_reason_override(isolated):
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    open_res = _open_session(isolated["env"])
    assert open_res["rc"] == 0, open_res

    import sys
    sys.path.insert(0, str(WORKSPACE))
    from selvedge.snapshots import take_snapshot

    result = take_snapshot(
        "manual",
        source_path=isolated["db"],
        keep_reason="pre_destructive_anchor",
    )
    assert result is not None

    conn = sqlite3.connect(f"file:{isolated['db']}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute(
            "SELECT * FROM snapshot_catalog WHERE trigger='manual' "
            "ORDER BY snapshot_id DESC LIMIT 1"
        ).fetchone()
    finally:
        conn.close()
    assert row is not None
    assert row["keep_reason"] == "pre_destructive_anchor"

    # Bad keep_reason returns None and writes nothing.
    bad = take_snapshot(
        "manual",
        source_path=isolated["db"],
        keep_reason="not_a_real_band",
    )
    assert bad is None


def test_init_refused_tags_pre_destructive_anchor(isolated):
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    open_res = _open_session(isolated["env"])
    assert open_res["rc"] == 0, open_res

    refused = _run(isolated["env"], ["init", "--force"])
    assert refused["rc"] == 2, refused
    assert "E_LIVE_SUBSTRATE" in refused["err"]

    conn = sqlite3.connect(f"file:{isolated['db']}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute(
            "SELECT * FROM snapshot_catalog WHERE trigger='init_refused' "
            "ORDER BY snapshot_id DESC LIMIT 1"
        ).fetchone()
    finally:
        conn.close()
    assert row is not None
    assert row["keep_reason"] == "pre_destructive_anchor"


def test_init_forced_emits_snapshot_file(isolated):
    """init --really-force is the second pre-destructive anchor path. The
    catalog row is written into the about-to-be-unlinked substrate so it is
    not readable post-unlink; this test confirms the snapshot FILE lands on
    disk (the recovery anchor) and the new substrate carries no init_forced
    row (mirrors test_snapshots_and_restore.py). The keep_reason override is
    covered in test_take_snapshot_keep_reason_override by direct API call."""
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    open_res = _open_session(isolated["env"])
    assert open_res["rc"] == 0, open_res

    forced = _run(isolated["env"], ["init", "--really-force"])
    assert forced["rc"] == 0, forced

    snap_files = sorted(isolated["snaps"].glob("*-init_forced*.sqlite"))
    assert len(snap_files) >= 1, list(isolated["snaps"].iterdir())

    conn = sqlite3.connect(f"file:{isolated['db']}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            "SELECT * FROM snapshot_catalog WHERE trigger='init_forced'"
        ).fetchall()
    finally:
        conn.close()
    assert rows == [], "new substrate (post-unlink) should carry no init_forced row"


def test_deliberation_seal_dispatch_fires_snapshot(isolated):
    """End-to-end: open session, open deliberation, add perspective +
    counterfactual, seal — confirm snapshot row lands with correct trigger
    and source_session_no."""
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    open_res = _open_session(isolated["env"])
    assert open_res["rc"] == 0, open_res
    wno = open_res["out"]["result"]["workspace_session_no"]
    sno = open_res["out"]["result"]["session_no"]

    do = _run(
        isolated["env"],
        [
            "submit",
            "deliberation-open",
            "--payload",
            json.dumps({"session_no": sno, "topic": "engine-v52 dispatch test"}),
        ],
    )
    assert do["rc"] == 0, do
    did = do["out"]["result"]["deliberation_id"]

    pe = _run(
        isolated["env"],
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({
                "deliberation_id": did,
                "label": "P-1",
                "family": "anthropic",
                "name_or_role": "test-perspective",
                "stance_brief_md": "stance brief atom for the dispatch test fixture",
                "body_md": "**Position.** position atom for dispatch test fixture",
            }),
        ],
    )
    assert pe["rc"] == 0, pe

    cf = _run(
        isolated["env"],
        [
            "submit",
            "deliberation-counterfactual",
            "--payload",
            json.dumps({
                "deliberation_id": did,
                "nil_attestation": 1,
                "position": "stance space exhausted by perspectives present (cheap-exit)",
                "why": "single-axis dispatch test; no alternative reading remains",
                "disposition": "nilled-by-exclusion",
                "exclusion_kind": "out-of-scope",
            }),
        ],
    )
    assert cf["rc"] == 0, cf

    seal = _run(
        isolated["env"],
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did, "synthesis_md": "synthesis text"}),
        ],
    )
    assert seal["rc"] == 0, seal

    conn = sqlite3.connect(f"file:{isolated['db']}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            "SELECT * FROM snapshot_catalog WHERE trigger='deliberation_seal'"
        ).fetchall()
    finally:
        conn.close()
    assert len(rows) == 1, [dict(r) for r in rows]
    assert rows[0]["source_session_no"] == wno
    assert _sha256(Path(rows[0]["path"])) == rows[0]["sha256"]


def test_export_manifest_records_session_files(isolated):
    """Open + close a session, export it, confirm export_manifest rows
    appear for the per-session files. Re-export replaces rather than
    appends (UNIQUE(path) + INSERT OR REPLACE)."""
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    open_res = _open_session(isolated["env"], slug="manifest-test")
    assert open_res["rc"] == 0, open_res
    wno = open_res["out"]["result"]["workspace_session_no"]

    asm = _run(
        isolated["env"],
        [
            "submit",
            "assessment",
            "--payload",
            json.dumps({
                "state": "isolated tmp workspace for export_manifest coverage",
                "agenda": ["confirm export_manifest rows land for per-session artefacts"],
            }),
        ],
    )
    assert asm["rc"] == 0, asm

    cr = _run(
        isolated["env"],
        [
            "submit",
            "close-record",
            "--payload",
            json.dumps({
                "summary": "manifest test minimal close-record fixture row",
                "items": [
                    {"facet": "what_was_done", "text": "manifest fixture session for export_manifest pytest"},
                ],
            }),
        ],
    )
    assert cr["rc"] == 0, cr
    sc = _run(isolated["env"], ["submit", "session-close", "--payload", "{}"])
    assert sc["rc"] == 0, sc

    exp = _run(
        isolated["env"],
        ["export", "--session", str(wno), "--write"],
        cwd=isolated["root"],
    )
    assert exp["rc"] == 0, exp

    conn = sqlite3.connect(f"file:{isolated['db']}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            "SELECT * FROM export_manifest WHERE session_no=? ORDER BY path",
            (wno,),
        ).fetchall()
    finally:
        conn.close()
    kinds = {r["kind"] for r in rows}
    # 00-assessment, 03-close are the minimum we authored; 04-review absent
    # since no review_findings were written.
    assert "assessment" in kinds, kinds
    assert "close" in kinds, kinds
    # Workspace-wide indices land too because export --session also fires
    # issues + spec_versions regen via the L5 close-time hook.
    conn = sqlite3.connect(f"file:{isolated['db']}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        ww = conn.execute(
            "SELECT * FROM export_manifest WHERE session_no IS NULL ORDER BY path"
        ).fetchall()
    finally:
        conn.close()
    ww_kinds = {r["kind"] for r in ww}
    assert "spec_versions_index" in ww_kinds, ww_kinds
    assert "open_issues_index" in ww_kinds, ww_kinds

    # sha256 on each row matches the file bytes that landed.
    for r in rows:
        on_disk = isolated["root"] / r["path"]
        assert on_disk.exists(), f"manifest path missing on disk: {on_disk}"
        assert _sha256(on_disk) == r["sha256"], r["path"]

    # Re-export: row count for session_no=wno is unchanged (REPLACE, not append).
    pre_count = len(rows)
    exp2 = _run(
        isolated["env"],
        ["export", "--session", str(wno), "--write"],
        cwd=isolated["root"],
    )
    assert exp2["rc"] == 0, exp2
    conn = sqlite3.connect(f"file:{isolated['db']}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        post_rows = conn.execute(
            "SELECT * FROM export_manifest WHERE session_no=?",
            (wno,),
        ).fetchall()
    finally:
        conn.close()
    assert len(post_rows) == pre_count, (
        f"REPLACE semantics broken: pre={pre_count} post={len(post_rows)}"
    )


def test_export_manifest_stale_reconciliation_drops_row_and_file(isolated):
    """When a per-session L5 file becomes stale (substrate rows removed),
    the export pipeline must delete BOTH the on-disk file AND the
    corresponding export_manifest row, with manifest DELETE preceding
    file unlink so a DELETE failure leaves both recoverable."""
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    open_res = _open_session(isolated["env"], slug="reconcile-test")
    assert open_res["rc"] == 0, open_res
    wno = open_res["out"]["result"]["workspace_session_no"]

    # Plant a fake stale L5 file at the expected per-session path AFTER an
    # export has run, so the next export sees it as stale (substrate rows
    # don't produce it) and reconciles. Use 06-counterfactuals.md as the
    # stale file: no deliberation_counterfactuals rows in this session, so
    # the substrate produces no body for it.
    asm = _run(
        isolated["env"],
        [
            "submit",
            "assessment",
            "--payload",
            json.dumps({"state": "stale-file fixture", "agenda": ["stale L5 reconciliation pytest"]}),
        ],
    )
    assert asm["rc"] == 0, asm

    # First export creates the per-session dir without 06-counterfactuals.md.
    exp = _run(
        isolated["env"], ["export", "--session", str(wno), "--write"], cwd=isolated["root"]
    )
    assert exp["rc"] == 0, exp

    out_dir = isolated["root"] / "provenance" / f"{wno:03d}-reconcile-test"
    stale_file = out_dir / "06-counterfactuals.md"
    stale_file.write_text("---\nstale-fixture: yes\n---\n# stale\n")
    # Plant a manifest row pointing at the stale file path.
    rel = str(stale_file.resolve().relative_to(isolated["root"].resolve()))
    wconn = sqlite3.connect(str(isolated["db"]))
    try:
        wconn.execute(
            "INSERT INTO export_manifest (session_no, kind, path, sha256, size_bytes, row_count) "
            "VALUES (?, 'counterfactuals', ?, "
            "'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', "
            "?, 0)",
            (wno, rel, stale_file.stat().st_size),
        )
        wconn.commit()
    finally:
        wconn.close()

    # Second export should reconcile: stale file unlinked AND manifest row dropped.
    exp2 = _run(
        isolated["env"], ["export", "--session", str(wno), "--write"], cwd=isolated["root"]
    )
    assert exp2["rc"] == 0, exp2
    assert not stale_file.exists(), "stale file should be unlinked by reconciliation"

    rconn = sqlite3.connect(f"file:{isolated['db']}?mode=ro", uri=True)
    try:
        rows = rconn.execute(
            "SELECT * FROM export_manifest WHERE path=?", (rel,)
        ).fetchall()
    finally:
        rconn.close()
    assert rows == [], f"manifest row for stale path should be deleted; found {rows}"


def test_export_manifest_dry_run_writes_no_rows(isolated):
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    open_res = _open_session(isolated["env"], slug="dry-run-test")
    assert open_res["rc"] == 0, open_res
    wno = open_res["out"]["result"]["workspace_session_no"]
    asm = _run(
        isolated["env"],
        [
            "submit",
            "assessment",
            "--payload",
            json.dumps({"state": "dry-run fixture", "agenda": ["dry-run pytest fixture"]}),
        ],
    )
    assert asm["rc"] == 0, asm

    # No --write flag → dry run; no manifest rows.
    exp = _run(
        isolated["env"],
        ["export", "--session", str(wno)],
        cwd=isolated["root"],
    )
    assert exp["rc"] == 0, exp

    conn = sqlite3.connect(f"file:{isolated['db']}?mode=ro", uri=True)
    try:
        n = conn.execute("SELECT COUNT(*) FROM export_manifest").fetchone()[0]
    finally:
        conn.close()
    assert n == 0, "dry-run must not write export_manifest rows"
