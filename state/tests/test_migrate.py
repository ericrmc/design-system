"""Tests for the `selvedge migrate` runner (engine-v18, S082 ships).

Coverage:
  - T-15 parse-level refusals (DROP TABLE, DROP COLUMN, ALTER ... DROP)
  - T-15 admits non-destructive drops (DROP TRIGGER, DROP INDEX)
  - SQL comments don't trip T-15
  - --status lists applied + pending
  - --dry-run reports pending without writing
  - --apply is idempotent (second call is a no-op)
  - drift detection (recorded sha256 ≠ file sha256 ⇒ E_MIGRATION_DRIFT)
  - end-to-end: a tmp-workspace migration file is applied and then refused
    on second call after the file is mutated (E_MIGRATION_DRIFT)
"""
from __future__ import annotations

import json
import os
import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

from conftest import BIN, WORKSPACE


# ---------------------------------------------------------------------------
# Direct unit tests on the T-15 parser
# ---------------------------------------------------------------------------


def test_t15_refuses_drop_table():
    from selvedge.cli import _t15_violations

    assert _t15_violations("DROP TABLE foo;") == ["DROP TABLE"]
    assert _t15_violations("drop table foo;") == ["DROP TABLE"]


def test_t15_refuses_drop_column():
    from selvedge.cli import _t15_violations

    assert _t15_violations("ALTER TABLE foo DROP COLUMN bar;") == ["DROP COLUMN", "ALTER TABLE … DROP"]


def test_t15_refuses_alter_drop():
    from selvedge.cli import _t15_violations

    # The DROP keyword inside ALTER TABLE … DROP CONSTRAINT (forbidden form).
    sql = "ALTER TABLE foo\n  DROP CONSTRAINT bar;"
    violations = _t15_violations(sql)
    assert "ALTER TABLE … DROP" in violations


def test_t15_admits_drop_trigger():
    from selvedge.cli import _t15_violations

    assert _t15_violations("DROP TRIGGER IF EXISTS t13_old;") == []


def test_t15_admits_drop_index():
    from selvedge.cli import _t15_violations

    assert _t15_violations("DROP INDEX idx_foo;") == []


def test_t15_admits_create_trigger():
    from selvedge.cli import _t15_violations

    assert _t15_violations("CREATE TRIGGER tx BEFORE UPDATE OF c ON t BEGIN SELECT 1; END;") == []


def test_t15_strips_comments_before_match():
    from selvedge.cli import _t15_violations

    # The keyword DROP TABLE appears only inside comments — must not trip.
    sql = """
        -- prose mentions DROP TABLE in passing
        /* a block comment naming DROP COLUMN as something we don't do */
        CREATE TRIGGER tx BEFORE UPDATE OF c ON t BEGIN SELECT 1; END;
    """
    assert _t15_violations(sql) == []


# ---------------------------------------------------------------------------
# Subcommand integration tests against an isolated tmp workspace
# ---------------------------------------------------------------------------


def _run_in(env: dict, args: list[str]) -> dict:
    proc = subprocess.run(
        [str(BIN), *args],
        capture_output=True,
        text=True,
        env={**os.environ, **env},
    )
    out = (proc.stdout or "").strip()
    err = (proc.stderr or "").strip()
    payload = None
    if out:
        try:
            payload = json.loads(out)
        except json.JSONDecodeError:
            payload = {"_raw": out}
    return {"rc": proc.returncode, "out": payload, "err": err}


@pytest.fixture
def tmp_substrate(tmp_path):
    """A throwaway substrate + migrations dir for runner tests.

    Copies migration 001 into the tmp migrations dir (so init succeeds) and
    points the CLI at both via env. The MODE.md file is required by
    workspace_root(); we create one in tmp_path.
    """
    (tmp_path / "MODE.md").write_text("---\nmode: self-development\nworkspace_id: tmp\n---\n")
    mig_dir = tmp_path / "migrations"
    mig_dir.mkdir()
    shutil.copy(WORKSPACE / "state" / "migrations" / "001-initial.sql", mig_dir / "001-initial.sql")
    db = tmp_path / "selvedge.sqlite"
    env = {
        "SELVEDGE_WORKSPACE": str(tmp_path),
        "SELVEDGE_DB_PATH": str(db),
        "SELVEDGE_MIGRATIONS_DIR": str(mig_dir),
    }
    init = _run_in(env, ["init", "--force"])
    assert init["rc"] == 0, init
    return {"env": env, "db": db, "mig_dir": mig_dir, "root": tmp_path}


def test_status_lists_applied_after_init(tmp_substrate):
    res = _run_in(tmp_substrate["env"], ["migrate", "--status"])
    assert res["rc"] == 0, res
    assert res["out"]["ok"]
    names = [a["name"] for a in res["out"]["applied"]]
    assert "001-initial.sql" in names
    assert res["out"]["pending"] == []


def test_dry_run_reports_pending_without_writing(tmp_substrate):
    mig = tmp_substrate["mig_dir"] / "002-add-trigger.sql"
    mig.write_text(
        "BEGIN;\n"
        "CREATE TRIGGER tmp_test BEFORE INSERT ON sessions\n"
        "FOR EACH ROW WHEN 0 BEGIN SELECT 1; END;\n"
        "INSERT INTO schema_migrations (name, sha256) VALUES ('002-add-trigger.sql', 'COMPUTED-AT-APPLY-TIME');\n"
        "COMMIT;\n"
    )
    res = _run_in(tmp_substrate["env"], ["migrate", "--dry-run"])
    assert res["rc"] == 0, res
    assert res["out"]["dry_run"] is True
    assert [m["name"] for m in res["out"]["would_apply"]] == ["002-add-trigger.sql"]
    # Confirm no row was written.
    conn = sqlite3.connect(str(tmp_substrate["db"]))
    n = conn.execute("SELECT COUNT(*) FROM schema_migrations WHERE name='002-add-trigger.sql'").fetchone()[0]
    conn.close()
    assert n == 0


def test_apply_then_idempotent(tmp_substrate):
    mig = tmp_substrate["mig_dir"] / "002-add-trigger.sql"
    mig.write_text(
        "BEGIN;\n"
        "CREATE TRIGGER tmp_test BEFORE INSERT ON sessions\n"
        "FOR EACH ROW WHEN 0 BEGIN SELECT 1; END;\n"
        "INSERT INTO schema_migrations (name, sha256) VALUES ('002-add-trigger.sql', 'COMPUTED-AT-APPLY-TIME');\n"
        "COMMIT;\n"
    )
    res = _run_in(tmp_substrate["env"], ["migrate", "--apply"])
    assert res["rc"] == 0, res
    assert [a["name"] for a in res["out"]["applied"]] == ["002-add-trigger.sql"]

    # Second apply — no-op.
    res2 = _run_in(tmp_substrate["env"], ["migrate", "--apply"])
    assert res2["rc"] == 0, res2
    assert res2["out"]["applied"] == []

    # Status reflects both applied.
    status = _run_in(tmp_substrate["env"], ["migrate", "--status"])
    names = [a["name"] for a in status["out"]["applied"]]
    assert names == ["001-initial.sql", "002-add-trigger.sql"]
    assert status["out"]["pending"] == []


def test_drift_detection_refuses(tmp_substrate):
    mig = tmp_substrate["mig_dir"] / "002-add-trigger.sql"
    mig.write_text(
        "BEGIN;\n"
        "CREATE TRIGGER tmp_drift BEFORE INSERT ON sessions\n"
        "FOR EACH ROW WHEN 0 BEGIN SELECT 1; END;\n"
        "INSERT INTO schema_migrations (name, sha256) VALUES ('002-add-trigger.sql', 'COMPUTED-AT-APPLY-TIME');\n"
        "COMMIT;\n"
    )
    apply = _run_in(tmp_substrate["env"], ["migrate", "--apply"])
    assert apply["rc"] == 0

    # Mutate the migration file post-apply — schema_migrations now records the
    # original sha256; the file's new sha256 should produce E_MIGRATION_DRIFT.
    mig.write_text(mig.read_text() + "\n-- drift\n")
    drift = _run_in(tmp_substrate["env"], ["migrate", "--status"])
    assert drift["rc"] == 3
    assert "E_MIGRATION_DRIFT" in drift["err"]


def test_t15_refuses_destructive_migration_in_dry_run(tmp_substrate):
    mig = tmp_substrate["mig_dir"] / "002-destructive.sql"
    mig.write_text(
        "BEGIN;\n"
        "DROP TABLE work_items;\n"
        "INSERT INTO schema_migrations (name, sha256) VALUES ('002-destructive.sql', 'COMPUTED-AT-APPLY-TIME');\n"
        "COMMIT;\n"
    )
    res = _run_in(tmp_substrate["env"], ["migrate", "--dry-run"])
    assert res["rc"] == 3
    assert "E_REFUSAL_T15" in res["err"]
    # And the apply path also refuses, leaving the substrate unchanged.
    res2 = _run_in(tmp_substrate["env"], ["migrate", "--apply"])
    assert res2["rc"] == 3
    assert "E_REFUSAL_T15" in res2["err"]
    conn = sqlite3.connect(str(tmp_substrate["db"]))
    n = conn.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='work_items'").fetchone()[0]
    conn.close()
    assert n == 1, "work_items must still exist; T-15 must have refused before any execution"


def test_t15_refuses_alter_drop_column(tmp_substrate):
    mig = tmp_substrate["mig_dir"] / "002-drop-column.sql"
    mig.write_text(
        "BEGIN;\n"
        "ALTER TABLE work_items DROP COLUMN payload_json;\n"
        "INSERT INTO schema_migrations (name, sha256) VALUES ('002-drop-column.sql', 'COMPUTED-AT-APPLY-TIME');\n"
        "COMMIT;\n"
    )
    res = _run_in(tmp_substrate["env"], ["migrate", "--apply"])
    assert res["rc"] == 3
    assert "E_REFUSAL_T15" in res["err"]


def test_failure_mid_apply_restores_from_backup(tmp_substrate):
    # A migration that parses past T-15 but fails at execute time (references a
    # nonexistent table). The runner should restore from the pre-migrate backup
    # and leave schema_migrations unchanged.
    mig = tmp_substrate["mig_dir"] / "002-broken.sql"
    mig.write_text(
        "BEGIN;\n"
        "CREATE TRIGGER bad_trigger BEFORE UPDATE ON does_not_exist\n"
        "FOR EACH ROW BEGIN SELECT 1; END;\n"
        "INSERT INTO schema_migrations (name, sha256) VALUES ('002-broken.sql', 'COMPUTED-AT-APPLY-TIME');\n"
        "COMMIT;\n"
    )

    # Capture pre-apply state for restore verification.
    db_path = tmp_substrate["db"]
    pre_table_count = sqlite3.connect(str(db_path)).execute(
        "SELECT COUNT(*) FROM sqlite_master WHERE type='table'"
    ).fetchone()[0]

    res = _run_in(tmp_substrate["env"], ["migrate", "--apply"])
    assert res["rc"] == 3
    assert "E_MIGRATION_FAILED" in res["err"]

    # schema_migrations should not have a row for the broken migration.
    conn = sqlite3.connect(str(db_path))
    try:
        n = conn.execute("SELECT COUNT(*) FROM schema_migrations WHERE name='002-broken.sql'").fetchone()[0]
        assert n == 0
        # The substrate must be functionally identical to its pre-apply state.
        post_table_count = conn.execute(
            "SELECT COUNT(*) FROM sqlite_master WHERE type='table'"
        ).fetchone()[0]
        assert post_table_count == pre_table_count
        # The bad trigger must not exist on the post-restore substrate.
        bad = conn.execute(
            "SELECT COUNT(*) FROM sqlite_master WHERE type='trigger' AND name='bad_trigger'"
        ).fetchone()[0]
        assert bad == 0
    finally:
        conn.close()

    # The .pre-migrate-backup file must remain on disk (operator can inspect it
    # post-mortem; runner does not auto-delete on failure).
    backup = db_path.with_suffix(".sqlite.pre-migrate-backup")
    assert backup.exists(), "post-failure: backup file should remain for operator inspection"


def test_apply_replaces_placeholder_sha_with_real_hash(tmp_substrate):
    """Defensive test against drift-detection bypass: if the runner stored the
    placeholder string `COMPUTED-AT-APPLY-TIME` indefinitely, the drift check
    would silently treat every applied migration as 'never drifts' (the
    placeholder branch in `_migration_state` short-circuits the sha compare).
    Verify the real sha256 lands in `schema_migrations` post-apply."""
    import hashlib as _h

    mig = tmp_substrate["mig_dir"] / "002-placeholder.sql"
    mig_body = (
        "BEGIN;\n"
        "CREATE TRIGGER tmp_placeholder BEFORE INSERT ON sessions\n"
        "FOR EACH ROW WHEN 0 BEGIN SELECT 1; END;\n"
        "INSERT INTO schema_migrations (name, sha256) VALUES ('002-placeholder.sql', 'COMPUTED-AT-APPLY-TIME');\n"
        "COMMIT;\n"
    )
    mig.write_text(mig_body)
    expected_sha = _h.sha256(mig_body.encode()).hexdigest()

    res = _run_in(tmp_substrate["env"], ["migrate", "--apply"])
    assert res["rc"] == 0, res

    conn = sqlite3.connect(str(tmp_substrate["db"]))
    try:
        recorded = conn.execute(
            "SELECT sha256 FROM schema_migrations WHERE name='002-placeholder.sql'"
        ).fetchone()[0]
    finally:
        conn.close()
    assert recorded != "COMPUTED-AT-APPLY-TIME", (
        "post-apply: runner must replace the placeholder with the real sha256; "
        "leaving the placeholder would silently disable drift detection"
    )
    assert recorded == expected_sha


def test_apply_with_no_pending_is_a_clean_noop(tmp_substrate):
    """After `init` (which auto-applies migrations), a fresh `--apply` must
    return ok with `applied: []` and not error on the empty-pending path."""
    res = _run_in(tmp_substrate["env"], ["migrate", "--apply"])
    assert res["rc"] == 0, res
    assert res["out"]["ok"] is True
    assert res["out"]["applied"] == []


def test_migrate_against_nonexistent_substrate_returns_rc2(tmp_path):
    """Running migrate before init should fail cleanly with rc=2 and a clear
    operator-readable message, not crash with an unhandled exception."""
    (tmp_path / "MODE.md").write_text("---\nmode: self-development\nworkspace_id: tmp\n---\n")
    mig_dir = tmp_path / "migrations"
    mig_dir.mkdir()
    shutil.copy(WORKSPACE / "state" / "migrations" / "001-initial.sql", mig_dir / "001-initial.sql")
    db = tmp_path / "absent.sqlite"
    assert not db.exists()
    env = {
        "SELVEDGE_WORKSPACE": str(tmp_path),
        "SELVEDGE_DB_PATH": str(db),
        "SELVEDGE_MIGRATIONS_DIR": str(mig_dir),
    }
    for sub in (["migrate", "--status"], ["migrate", "--dry-run"], ["migrate", "--apply"]):
        res = _run_in(env, sub)
        assert res["rc"] == 2, f"{sub}: expected rc=2, got rc={res['rc']}: {res}"
        assert "no substrate" in res["err"].lower() or "selvedge init" in res["err"].lower()
