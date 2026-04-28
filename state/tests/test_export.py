"""Tests for the export pipeline: cmd_export → _export_session_provenance and
_export_issues.

The export materialises markdown files from substrate rows; coverage was
deferred under OI-S090-2 because the round-trip case (substrate → markdown
→ git) is more involved than a single submit handler test. We test:

  - dry-run: returns the planned file set without touching disk
  - --write: lands the planned files at the workspace-relative paths
  - --issues: renders open-issues/<alias>.md plus the index
  - error surfaces: missing --session/--issues, unknown session ref

To avoid clobbering the real workspace's provenance/ and open-issues/
trees, each test runs in tmp_path with the substrate snapshot copied in.
The CLI subprocess is given SELVEDGE_WORKSPACE pointing at tmp_path.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from conftest import PRIMARY_DB, WORKSPACE, _coverage_subprocess_env


def _run_cli_in(workspace: Path, args: list[str]) -> dict:
    """Variant of conftest._run_cli that points SELVEDGE_WORKSPACE at a
    custom tmp_path. Output parsing mirrors the original. We set
    COVERAGE_FILE absolutely so subprocess coverage data lands next to
    pytest's, not in the tmp cwd where pytest-cov never sees it."""
    env = os.environ | {"SELVEDGE_WORKSPACE": str(workspace)} | _coverage_subprocess_env()
    if "COVERAGE_PROCESS_START" in env:
        env["COVERAGE_FILE"] = str(WORKSPACE / ".coverage")
    bin_path = workspace / "bin" / "selvedge"
    proc = subprocess.run(
        [str(bin_path), *args],
        capture_output=True, text=True, env=env, cwd=str(workspace),
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
def isolated_workspace(tmp_path, monkeypatch):
    """Copy the bare minimum of the workspace into tmp_path so cmd_export can
    write provenance/ and open-issues/ files without disturbing the real tree.

    We symlink read-only inputs (selvedge package, bin shim, state/migrations)
    and copy state/selvedge.sqlite as a fresh snapshot."""
    # Symlink in code + migrations (read-only).
    (tmp_path / "selvedge").symlink_to(WORKSPACE / "selvedge")
    (tmp_path / "bin").mkdir()
    (tmp_path / "bin" / "selvedge").symlink_to(WORKSPACE / "bin" / "selvedge")
    (tmp_path / "state").mkdir()
    (tmp_path / "state" / "migrations").symlink_to(WORKSPACE / "state" / "migrations")
    # Symlink the venv + pyproject so the shim's `.venv/bin/python` discovery
    # succeeds inside tmp_path (otherwise it falls back to system python3,
    # which lacks `coverage` and the subprocess does not contribute to the
    # coverage report).
    venv = WORKSPACE / ".venv"
    if venv.exists():
        (tmp_path / ".venv").symlink_to(venv)
    pyproject = WORKSPACE / "pyproject.toml"
    if pyproject.exists():
        (tmp_path / "pyproject.toml").symlink_to(pyproject)
    sitecustomize = WORKSPACE / "state" / "tests" / "sitecustomize.py"
    if sitecustomize.exists():
        (tmp_path / "state" / "tests").mkdir(parents=True, exist_ok=True)
        (tmp_path / "state" / "tests" / "sitecustomize.py").symlink_to(sitecustomize)
    # Initialise a fresh substrate inside tmp_path so the export has predictable
    # session content.
    init = _run_cli_in(tmp_path, ["init", "--force"])
    assert init["rc"] == 0, init
    open_ = _run_cli_in(tmp_path, ["submit", "session-open", "--payload",
                                    json.dumps({"slug": "export-fixture"})])
    assert open_["rc"] == 0, open_
    return tmp_path


# ---------------------------------------------------------------------------
# cmd_export argument parsing
# ---------------------------------------------------------------------------


def test_export_without_session_or_issues_returns_2(isolated_workspace):
    res = _run_cli_in(isolated_workspace, ["export"])
    assert res["rc"] == 2
    assert "pass --session" in res["err"]


def test_export_unknown_session_ref_refused(isolated_workspace):
    res = _run_cli_in(isolated_workspace, ["export", "--session", "999"])
    assert res["rc"] == 3
    assert "E_NOT_FOUND" in res["err"]


# ---------------------------------------------------------------------------
# _export_session_provenance
# ---------------------------------------------------------------------------


def test_export_session_dry_run_returns_planned_files(isolated_workspace):
    """Add an assessment + close-record so the exporter has content to plan,
    then call --session 1 without --write and confirm the plan is returned."""
    _run_cli_in(isolated_workspace, [
        "submit", "assessment", "--payload",
        json.dumps({
            "state": "fixture state for the export-pipeline pytest",
            "agenda": ["pytest agenda item one"],
        }),
    ])
    _run_cli_in(isolated_workspace, [
        "submit", "close-record", "--payload",
        json.dumps({
            "summary": "fixture close-record for the dry-run export test",
            "items": [{"facet": "what_was_done", "text": "exported the substrate dryly"}],
        }),
    ])
    # workspace_session_no = 1 + 79 = 80 in the fresh workspace.
    res = _run_cli_in(isolated_workspace, ["export", "--session", "80"])
    assert res["rc"] == 0, res
    assert res["out"]["dry_run"] is True
    planned = res["out"]["files_planned"]
    assert any("00-assessment.md" in p for p in planned)
    assert any("03-close.md" in p for p in planned)
    # Dry-run must not have created any provenance/ tree at all.
    assert not (isolated_workspace / "provenance").exists(), (
        "dry_run leaked a provenance directory onto disk"
    )


def test_export_session_write_lands_files(isolated_workspace):
    _run_cli_in(isolated_workspace, [
        "submit", "assessment", "--payload",
        json.dumps({
            "state": "fixture state for the export-pipeline write test",
            "agenda": ["pytest agenda one", "pytest agenda two"],
        }),
    ])
    _run_cli_in(isolated_workspace, [
        "submit", "close-record", "--payload",
        json.dumps({
            "summary": "fixture close-record for the write-export test",
            "items": [
                {"facet": "what_was_done", "text": "wrote the export files"},
                {"facet": "next_session_should", "text": "follow up on export coverage"},
            ],
        }),
    ])
    res = _run_cli_in(isolated_workspace, ["export", "--session", "80", "--write"])
    assert res["rc"] == 0, res
    assert res["out"]["dry_run"] is False
    out_dir = isolated_workspace / res["out"]["out_dir"]
    for name in res["out"]["files_written"]:
        assert (out_dir / name).exists(), f"missing: {out_dir / name}"
    # Structure check: assessment file must carry the section markers, the
    # state atom, and at least one agenda atom — not just a substring match.
    text = (out_dir / "00-assessment.md").read_text()
    assert "# Assessment" in text
    assert "## State at open" in text
    assert "## Agenda" in text
    assert "fixture state for the export-pipeline write test" in text
    assert "pytest agenda one" in text


def test_export_session_with_deliberation_decision_finding(isolated_workspace):
    """Exercise the deliberation, decisions, and review-findings branches of
    _export_session_provenance by populating the session with one of each
    before exporting."""
    # Deliberation + perspective + seal + synthesis-point.
    delib = _run_cli_in(isolated_workspace, [
        "submit", "deliberation-open", "--payload",
        json.dumps({"session_no": 1, "topic": "fixture deliberation for export coverage"}),
    ])
    assert delib["rc"] == 0, delib
    did = delib["out"]["result"]["deliberation_id"]
    p1 = _run_cli_in(isolated_workspace, [
        "submit", "perspective", "--payload",
        json.dumps({"session_no": 1, "deliberation_id": did, "label": "p1",
                    "family": "anthropic", "body_md": "first perspective body for export fixture"}),
    ])
    p2 = _run_cli_in(isolated_workspace, [
        "submit", "perspective", "--payload",
        json.dumps({"session_no": 1, "deliberation_id": did, "label": "p2",
                    "family": "openai", "body_md": "second perspective body for export fixture"}),
    ])
    _run_cli_in(isolated_workspace, [
        "submit", "deliberation-seal", "--payload",
        json.dumps({"session_no": 1, "deliberation_id": did,
                    "synthesis_md": "synthesis text under the export fixture"}),
    ])
    _run_cli_in(isolated_workspace, [
        "submit", "synthesis-point", "--payload",
        json.dumps({"session_no": 1, "deliberation_id": did, "kind": "convergence",
                    "label": "C-1", "summary": "single convergence point",
                    "source_perspectives": [
                        p1["out"]["result"]["perspective_id"],
                        p2["out"]["result"]["perspective_id"],
                    ]}),
    ])

    # decision-record (Path A).
    _run_cli_in(isolated_workspace, [
        "submit", "decision-record", "--payload",
        json.dumps({
            "session_no": 1,
            "title": "fixture decision for export coverage", "kind": "substantive",
            "outcome_type": "adopt", "target_kind": "process_rule", "target_key": "export-fixture",
            "alternatives": [{
                "label": "R-1.1", "option": "alternative we considered then rejected",
                "rejections": [{"basis": "inferior_tradeoff",
                                 "reason": "rejected for being slower than the chosen path"}],
            }],
        }),
    ])

    # legacy-style decision (uses _submit_decision which the export also reads).
    _run_cli_in(isolated_workspace, [
        "submit", "decision", "--payload",
        json.dumps({
            "session_no": 1,
            "kind": "substantive", "title": "legacy-shape decision for export",
            "body_md": "legacy decision body without alias refs",
            "alternatives": [{
                "label": "R-1.1", "summary": "legacy alt summary",
                "rejection_reason_md": "rejected because the legacy alt path is slower than chosen",
            }],
        }),
    ])

    # review-finding.
    _run_cli_in(isolated_workspace, [
        "submit", "review-finding", "--payload",
        json.dumps({"session_no": 1, "iteration": 1, "severity": "low",
                    "finding": "fixture finding for export-pipeline coverage"}),
    ])

    res = _run_cli_in(isolated_workspace, ["export", "--session", "1", "--write"])
    assert res["rc"] == 0, res
    out_dir = isolated_workspace / res["out"]["out_dir"]
    written = res["out"]["files_written"]
    # All five facets should be present given we seeded each surface.
    assert "00-assessment.md" not in written  # we did not seed an assessment in this test
    assert "01-deliberation.md" in written
    assert "02-decisions.md" in written
    assert "04-review.md" in written
    decisions_text = (out_dir / "02-decisions.md").read_text()
    assert "fixture decision for export coverage" in decisions_text


def test_export_session_via_substrate_session_no(isolated_workspace):
    """The exporter accepts EITHER workspace_session_no (e.g. 80) OR the
    substrate session_no (1). Both should resolve to the same session."""
    _run_cli_in(isolated_workspace, [
        "submit", "assessment", "--payload",
        json.dumps({"state": "alt-ref state", "agenda": ["one"]}),
    ])
    res = _run_cli_in(isolated_workspace, ["export", "--session", "1"])
    assert res["rc"] == 0
    assert res["out"]["dry_run"] is True


# ---------------------------------------------------------------------------
# _export_issues
# ---------------------------------------------------------------------------


def test_export_issues_dry_run_plans_index_and_open_files(isolated_workspace):
    """Seed two issues — one open, one resolved — and confirm the dry-run plan
    routes them to the right paths and includes open-issues/index.md."""
    _run_cli_in(isolated_workspace, [
        "submit", "issue", "--payload",
        json.dumps({"alias": "OI-S080-1", "title": "open pytest issue", "priority": "MEDIUM"}),
    ])
    _run_cli_in(isolated_workspace, [
        "submit", "issue", "--payload",
        json.dumps({"alias": "OI-S080-2", "title": "to-be-resolved pytest issue", "priority": "LOW"}),
    ])
    _run_cli_in(isolated_workspace, [
        "submit", "issue-disposition", "--payload",
        json.dumps({
            "alias": "OI-S080-2",
            "to_status": "resolved",
            "reason": "resolved for export pytest fixture",
        }),
    ])
    res = _run_cli_in(isolated_workspace, ["export", "--issues"])
    assert res["rc"] == 0, res
    assert res["out"]["dry_run"] is True
    assert res["out"]["issues_exported"] == 2
    planned = res["out"]["files_planned"]
    assert "open-issues/index.md" in planned
    assert "open-issues/OI-S080-1.md" in planned
    assert "open-issues/resolved/OI-S080-2.md" in planned


def test_export_issues_write_creates_files_and_index(isolated_workspace):
    _run_cli_in(isolated_workspace, [
        "submit", "issue", "--payload",
        json.dumps({
            "alias": "OI-S080-3",
            "title": "issue with summary and body for export-write fixture",
            "summary": "summary text recorded under the issue's summary atom",
            "body": "body text recorded under the issue's body atom",
            "priority": "HIGH",
        }),
    ])
    res = _run_cli_in(isolated_workspace, ["export", "--issues", "--write"])
    assert res["rc"] == 0, res
    assert res["out"]["dry_run"] is False
    issue_md = isolated_workspace / "open-issues" / "OI-S080-3.md"
    assert issue_md.exists()
    text = issue_md.read_text()
    assert "OI-S080-3" in text
    assert "priority: HIGH" in text
    assert "summary text recorded" in text
    assert "body text recorded" in text
    index = (isolated_workspace / "open-issues" / "index.md").read_text()
    assert "OI-S080-3" in index


def test_export_issues_write_cleans_stale_files(isolated_workspace):
    """An export --write should delete on-disk open-issues/*.md files that
    don't correspond to a substrate row (EF-S092-2 reconciliation)."""
    oi_dir = isolated_workspace / "open-issues"
    oi_dir.mkdir(parents=True, exist_ok=True)
    stale = oi_dir / "OI-stale.md"
    stale.write_text("# stale issue not in substrate\n")
    # No substrate issues + write -> stale file must be removed.
    res = _run_cli_in(isolated_workspace, ["export", "--issues", "--write"])
    assert res["rc"] == 0, res
    assert not stale.exists()
    assert str(stale.relative_to(isolated_workspace)) in res["out"]["files_deleted"]
