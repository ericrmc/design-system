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
                                    json.dumps({"slug": "export-fixture", "kind": "spec_only"})])
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
    # workspace_session_no = 1 + 179 = 180 in the fresh workspace.
    res = _run_cli_in(isolated_workspace, ["export", "--session", "180"])
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
    res = _run_cli_in(isolated_workspace, ["export", "--session", "180", "--write"])
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
    # T-36 (DV-S180-1, engine-v50, migration 040) refuses seal without a
    # deliberation_counterfactuals row; submit one nil_attestation cheap-exit.
    _run_cli_in(isolated_workspace, [
        "submit", "deliberation-counterfactual", "--payload",
        json.dumps({"deliberation_id": did,
                    "position": "export-fixture cheap-exit nil_attestation: no counterfactuals.",
                    "why": "tactical fixture seal; stance-space exhaustion not load-bearing.",
                    "disposition": "nilled-by-exclusion",
                    "exclusion_kind": "out-of-scope",
                    "nil_attestation": 1}),
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

    # decision-record (Path A). T-33 (engine-v49) requires a precheck for
    # kind=substantive; obtain a single-use nonce first.
    pre = _run_cli_in(isolated_workspace, [
        "precheck", "--target-kind", "process_rule", "--target-key", "export-fixture",
    ])
    nonce = None
    raw = (pre["out"].get("_raw") if isinstance(pre["out"], dict) else "") or ""
    for tok in raw.split():
        if tok.startswith("nonce="):
            nonce = tok.split("=", 1)[1]
            break
    assert nonce, f"precheck did not return a nonce: {pre}"
    _run_cli_in(isolated_workspace, [
        "submit", "decision-record", "--payload",
        json.dumps({
            "session_no": 1,
            "title": "fixture decision for export coverage", "kind": "substantive",
            "outcome_type": "adopt", "target_kind": "process_rule", "target_key": "export-fixture",
            "precheck_nonce": nonce,
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
    """The exporter accepts EITHER workspace_session_no (e.g. 180) OR the
    substrate session_no (1). Both should resolve to the same session."""
    _run_cli_in(isolated_workspace, [
        "submit", "assessment", "--payload",
        json.dumps({"state": "alt-ref state", "agenda": ["one"]}),
    ])
    res = _run_cli_in(isolated_workspace, ["export", "--session", "1"])
    assert res["rc"] == 0
    assert res["out"]["dry_run"] is True


# ---------------------------------------------------------------------------
# _export_provenance_anchor --print (FR-S173-1)
# ---------------------------------------------------------------------------


def test_export_anchor_print_emits_markdown_to_stdout(isolated_workspace):
    """--print rooted on the fixture session alias must emit the anchor-trace
    markdown body to stdout (frontmatter + headline) and create no
    provenance/anchor-traces/ files on disk."""
    res = _run_cli_in(isolated_workspace, [
        "export", "--provenance", "--anchor", "S180", "--print",
    ])
    assert res["rc"] == 0, res
    raw = res["out"]["_raw"] if isinstance(res["out"], dict) else res["out"]
    assert "anchor: S180" in raw
    assert "# Anchor trace: `S180`" in raw
    # No JSON wrapper keys in stdout.
    assert "nodes_visited" not in raw.split("---", 2)[-1]
    # --print must not write to disk.
    assert not (isolated_workspace / "provenance" / "anchor-traces").exists()


def test_export_print_without_provenance_refused(isolated_workspace):
    res = _run_cli_in(isolated_workspace, ["export", "--session", "180", "--print"])
    assert res["rc"] == 2
    assert "only valid with --provenance --anchor" in res["err"]


def test_export_print_with_write_refused(isolated_workspace):
    res = _run_cli_in(isolated_workspace, [
        "export", "--provenance", "--anchor", "S180", "--print", "--write",
    ])
    assert res["rc"] == 2
    assert "mutually exclusive" in res["err"]


# ---------------------------------------------------------------------------
# _export_issues
# ---------------------------------------------------------------------------


def test_export_issues_dry_run_plans_index_and_open_files(isolated_workspace):
    """Seed two issues — one open, one resolved — and confirm the dry-run plan
    routes them to the right paths and includes open-issues/index.md."""
    _run_cli_in(isolated_workspace, [
        "submit", "issue", "--payload",
        json.dumps({"alias": "OI-S180-1", "title": "open pytest issue", "priority": "MEDIUM"}),
    ])
    _run_cli_in(isolated_workspace, [
        "submit", "issue", "--payload",
        json.dumps({"alias": "OI-S180-2", "title": "to-be-resolved pytest issue", "priority": "LOW"}),
    ])
    _run_cli_in(isolated_workspace, [
        "submit", "issue-disposition", "--payload",
        json.dumps({
            "alias": "OI-S180-2",
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
    assert "open-issues/OI-S180-1.md" in planned
    assert "open-issues/resolved/OI-S180-2.md" in planned


def test_export_issues_write_creates_files_and_index(isolated_workspace):
    _run_cli_in(isolated_workspace, [
        "submit", "issue", "--payload",
        json.dumps({
            "alias": "OI-S180-3",
            "title": "issue with summary and body for export-write fixture",
            "summary": "summary text recorded under the issue's summary atom",
            "body": "body text recorded under the issue's body atom",
            "priority": "HIGH",
        }),
    ])
    res = _run_cli_in(isolated_workspace, ["export", "--issues", "--write"])
    assert res["rc"] == 0, res
    assert res["out"]["dry_run"] is False
    issue_md = isolated_workspace / "open-issues" / "OI-S180-3.md"
    assert issue_md.exists()
    text = issue_md.read_text()
    assert "OI-S180-3" in text
    assert "priority: HIGH" in text
    assert "summary text recorded" in text
    assert "body text recorded" in text
    index = (isolated_workspace / "open-issues" / "index.md").read_text()
    assert "OI-S180-3" in index


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


# ---------------------------------------------------------------------------
# reference-harness export
# ---------------------------------------------------------------------------


def _seed_sealed_harness(workspace: Path, alias: str = "RH-S180-1") -> dict:
    """Open + populate + seal a harness in the fresh test workspace's session 1
    (workspace_session_no=180). Returns the seal CLI response payload."""
    open_res = _run_cli_in(workspace, [
        "submit", "harness-open", "--payload",
        json.dumps({
            "alias": alias,
            "arc_slug": "pytest-arc",
            "stage_n": 1,
            "absence_declaration": f"absence declaration for {alias} export-pipeline test",
            "expiry_sessions": 4,
        }),
    ])
    assert open_res["rc"] == 0, open_res
    hid = open_res["out"]["result"]["harness_id"]
    _run_cli_in(workspace, [
        "submit", "harness-target", "--payload",
        json.dumps({
            "harness_id": hid, "ord": 1,
            "descriptor": "pytest target descriptor for harness export",
            "artifact_path": "tests/fixture-target.md",
            "artifact_sha256": "deadbeef" * 8,
        }),
    ])
    _run_cli_in(workspace, [
        "submit", "harness-assumption", "--payload",
        json.dumps({"harness_id": hid, "ord": 1,
                    "assumption": "fixture assumption for harness export pytest"}),
    ])
    claim_res = _run_cli_in(workspace, [
        "submit", "harness-claim", "--payload",
        json.dumps({"harness_id": hid, "ord": 1,
                    "claim": "fixture claim for harness export pytest",
                    "load_bearing": True}),
    ])
    cid = claim_res["out"]["result"]["claim_id"]
    _run_cli_in(workspace, [
        "submit", "harness-stress", "--payload",
        json.dumps({"harness_id": hid, "ord": 1, "protocol_kind": "constraint_replay",
                    "description": "fixture stress description for harness export"}),
    ])
    _run_cli_in(workspace, [
        "submit", "harness-result", "--payload",
        json.dumps({"claim_id": cid, "result": "survived",
                    "evidence": "fixture evidence text for harness result export"}),
    ])
    _run_cli_in(workspace, [
        "submit", "harness-dissent", "--payload",
        json.dumps({"harness_id": hid, "ord": 1,
                    "dissent": "fixture dissent text for harness export"}),
    ])
    seal_res = _run_cli_in(workspace, [
        "submit", "harness-seal", "--payload", json.dumps({"harness_id": hid}),
    ])
    assert seal_res["rc"] == 0, seal_res
    return {"harness_id": hid, "alias": alias}


def test_export_session_skips_open_harness(isolated_workspace):
    """An open harness must not appear in the export plan; it has no
    sealed reference value yet."""
    _run_cli_in(isolated_workspace, [
        "submit", "harness-open", "--payload",
        json.dumps({
            "alias": "RH-S180-1", "arc_slug": "pytest-arc", "stage_n": 1,
            "absence_declaration": "open-only harness for skip-open pytest",
            "expiry_sessions": 4,
        }),
    ])
    _run_cli_in(isolated_workspace, [
        "submit", "close-record", "--payload",
        json.dumps({"summary": "fixture close-record so the export plan is non-empty",
                    "items": []}),
    ])
    res = _run_cli_in(isolated_workspace, ["export", "--session", "180"])
    assert res["rc"] == 0, res
    assert res["out"]["harness_files_planned"] == []


def test_export_session_emits_sealed_harness_dry_run(isolated_workspace):
    seeded = _seed_sealed_harness(isolated_workspace)
    _run_cli_in(isolated_workspace, [
        "submit", "close-record", "--payload",
        json.dumps({"summary": "close-record for sealed-harness dry-run export",
                    "items": []}),
    ])
    res = _run_cli_in(isolated_workspace, ["export", "--session", "180"])
    assert res["rc"] == 0, res
    planned = res["out"]["harness_files_planned"]
    assert len(planned) == 1
    assert planned[0].endswith(f"/harnesses/{seeded['alias']}.md")
    # Dry-run must not have written anything.
    assert not (isolated_workspace / planned[0]).exists()


def test_export_session_writes_sealed_harness(isolated_workspace):
    seeded = _seed_sealed_harness(isolated_workspace)
    _run_cli_in(isolated_workspace, [
        "submit", "close-record", "--payload",
        json.dumps({"summary": "close-record for sealed-harness write export",
                    "items": []}),
    ])
    res = _run_cli_in(isolated_workspace, ["export", "--session", "180", "--write"])
    assert res["rc"] == 0, res
    written = res["out"]["harness_files_written"]
    assert len(written) == 1
    path = isolated_workspace / written[0]
    assert path.exists()
    text = path.read_text()
    assert f"id: {seeded['alias']}" in text
    assert "status: sealed" in text
    assert "## Targets" in text
    assert "## Claims" in text
    assert "## Results" in text
    assert "## Dissent" in text
    assert "load-bearing" in text
    assert "fixture claim for harness export pytest" in text
    assert "→ **survived**" in text


# ---------------------------------------------------------------------------
# L5 close-time export expansion (OI-S081-6 / DV-S187-1)
# ---------------------------------------------------------------------------


def _seed_decision_with_alias_cite(workspace: Path) -> str:
    """Seed a substantive decision_v2 row whose precheck nonce is captured and
    whose supports.cite resolves against an existing alias (the EF row we
    submit below). Return the EF alias so callers can assert chain-walk anchor
    presence.

    The fixture also exercises decision_chain_walks (T-32 receipt) and
    decision_prechecks (T-33 receipt) population paths.
    """
    # Seed an EF first so we have a citable alias for supports.cite.
    ef = _run_cli_in(workspace, [
        "submit", "engine-feedback", "--payload",
        json.dumps({"flag": "observation",
                    "body_md": "**l5-fixture:** EF body for L5 export pytest fixture."}),
    ])
    ef_alias = ef["out"]["result"]["alias"]
    # Precheck the substantive decision.
    pre = _run_cli_in(workspace, [
        "precheck", "--target-kind", "process_rule", "--target-key", "l5-fixture-target",
    ])
    nonce = None
    raw = (pre["out"].get("_raw") if isinstance(pre["out"], dict) else "") or ""
    for tok in raw.split():
        if tok.startswith("nonce="):
            nonce = tok.split("=", 1)[1]
            break
    assert nonce, f"precheck did not return a nonce: {pre}"
    _run_cli_in(workspace, [
        "submit", "decision-record", "--payload",
        json.dumps({
            "title": "L5 fixture decision exercising chain-walks plus precheck receipts.",
            "kind": "substantive",
            "outcome_type": "adopt",
            "target_kind": "process_rule",
            "target_key": "l5-fixture-target",
            "precheck_nonce": nonce,
            "supports": [{
                "basis": "engine_feedback",
                "claim": "L5 fixture support claim citing the seeded EF row.",
                "cite": ef_alias,
            }],
            "alternatives": [{
                "label": "R-1.1",
                "option": "L5 fixture rejected alternative path",
                "rejections": [{
                    "basis": "inferior_tradeoff",
                    "reason": "rejected for the L5 export fixture coverage path",
                }],
            }],
        }),
    ])
    return ef_alias


def test_l5_session_export_emits_engine_feedback_file(isolated_workspace):
    """An engine_feedback row in the session must surface as 05-engine-feedback.md
    with the EF alias, flag, and body content."""
    _run_cli_in(isolated_workspace, [
        "submit", "engine-feedback", "--payload",
        json.dumps({"flag": "calibration",
                    "body_md": "**l5-fixture-ef:** body content for L5 export fixture."}),
    ])
    _run_cli_in(isolated_workspace, [
        "submit", "close-record", "--payload",
        json.dumps({"summary": "fixture close-record so 05-engine-feedback emits",
                    "items": []}),
    ])
    res = _run_cli_in(isolated_workspace, ["export", "--session", "180", "--write"])
    assert res["rc"] == 0, res
    out_dir = isolated_workspace / res["out"]["out_dir"]
    ef_md = out_dir / "05-engine-feedback.md"
    assert ef_md.exists(), res
    text = ef_md.read_text()
    assert "EF-S180-1" in text
    assert "**flag.** calibration" in text
    assert "l5-fixture-ef" in text


def test_l5_session_export_emits_chain_walks_and_prechecks(isolated_workspace):
    """A substantive decision-record fires T-32 chain-walks per cited alias
    and T-33 precheck receipt; both must surface as 09-chain-walks.md and
    08-prechecks.md respectively under the per-session dir."""
    _seed_decision_with_alias_cite(isolated_workspace)
    _run_cli_in(isolated_workspace, [
        "submit", "close-record", "--payload",
        json.dumps({"summary": "fixture close-record for L5 chain-walk + precheck export",
                    "items": []}),
    ])
    res = _run_cli_in(isolated_workspace, ["export", "--session", "180", "--write"])
    assert res["rc"] == 0, res
    out_dir = isolated_workspace / res["out"]["out_dir"]
    walks = out_dir / "09-chain-walks.md"
    pre = out_dir / "08-prechecks.md"
    assert walks.exists(), res
    assert pre.exists(), res
    walks_text = walks.read_text()
    pre_text = pre.read_text()
    assert "Decision chain-walks" in walks_text
    assert "**walker_version.**" in walks_text
    assert "**result_sha256.**" in walks_text
    assert "Decision prechecks" in pre_text
    assert "l5-fixture-target" in pre_text


def test_l5_session_export_emits_counterfactuals_and_fr_dispositions(isolated_workspace):
    """A sealed deliberation with a counterfactual row, plus a FR-disposition
    that resolves a prior session's `next_session_should` atom, both surface
    as their L5 files."""
    # Seed an FR-bearing close-record (state-item with facet=next_session_should).
    _run_cli_in(isolated_workspace, [
        "submit", "close-record", "--payload",
        json.dumps({"summary": "fixture close authoring an FR for L5 disposition test",
                    "items": [{"facet": "next_session_should",
                                "text": "fixture next-session-should atom for FR-disposition export"}]}),
    ])
    # Close + open a second session so we can dispose the prior FR from S181.
    _run_cli_in(isolated_workspace, ["submit", "session-close", "--payload", "{}"])
    _run_cli_in(isolated_workspace, [
        "submit", "session-open", "--payload",
        json.dumps({"slug": "l5-fr-disposer", "kind": "spec_only"}),
    ])
    # Now dispose FR-S180-1 (target_session=180, seq=1) from S181.
    _run_cli_in(isolated_workspace, [
        "submit", "forward-reference-disposition", "--payload",
        json.dumps({"target_session": 180, "seq": 1,
                    "note": "addressed by L5 fixture path for FR-disposition export"}),
    ])
    # Seed a deliberation with a counterfactual nil-attestation row.
    # The second session opened above has substrate session_no=2.
    delib = _run_cli_in(isolated_workspace, [
        "submit", "deliberation-open", "--payload",
        json.dumps({"session_no": 2,
                    "topic": "L5 fixture deliberation for counterfactual export"}),
    ])
    did = delib["out"]["result"]["deliberation_id"]
    _run_cli_in(isolated_workspace, [
        "submit", "perspective", "--payload",
        json.dumps({"session_no": 2, "deliberation_id": did, "label": "p1",
                    "family": "anthropic",
                    "body_md": "L5 fixture perspective body for counterfactual export"}),
    ])
    _run_cli_in(isolated_workspace, [
        "submit", "deliberation-counterfactual", "--payload",
        json.dumps({"deliberation_id": did,
                    "position": "L5 fixture cheap-exit nil_attestation: stance-space exhausted.",
                    "why": "tactical fixture seal for L5 counterfactual export coverage.",
                    "disposition": "nilled-by-exclusion",
                    "exclusion_kind": "out-of-scope",
                    "nil_attestation": 1}),
    ])
    _run_cli_in(isolated_workspace, [
        "submit", "deliberation-seal", "--payload",
        json.dumps({"session_no": 2, "deliberation_id": did,
                    "synthesis_md": "L5 fixture synthesis text"}),
    ])
    _run_cli_in(isolated_workspace, [
        "submit", "close-record", "--payload",
        json.dumps({"summary": "fixture close for L5 counterfactual + FR-disposition export",
                    "items": []}),
    ])
    res = _run_cli_in(isolated_workspace, ["export", "--session", "181", "--write"])
    assert res["rc"] == 0, res
    out_dir = isolated_workspace / res["out"]["out_dir"]
    cf = out_dir / "06-counterfactuals.md"
    fr = out_dir / "07-fr-dispositions.md"
    assert cf.exists(), res
    assert fr.exists(), res
    cf_text = cf.read_text()
    fr_text = fr.read_text()
    assert "Deliberation counterfactuals" in cf_text
    assert "nil_attestation" in cf_text
    assert "FR-S180-1" in fr_text
    assert "addressed by L5 fixture path" in fr_text


def test_l5_session_export_omits_files_when_no_rows(isolated_workspace):
    """A session with only an assessment + close-record (no EF/precheck/walks/
    deliberation/FR-disp) produces no L5 files at all."""
    _run_cli_in(isolated_workspace, [
        "submit", "assessment", "--payload",
        json.dumps({"state": "L5 absence-fixture state", "agenda": ["L5 absence agenda"]}),
    ])
    _run_cli_in(isolated_workspace, [
        "submit", "close-record", "--payload",
        json.dumps({"summary": "L5 absence close-record", "items": []}),
    ])
    res = _run_cli_in(isolated_workspace, ["export", "--session", "180", "--write"])
    assert res["rc"] == 0, res
    out_dir = isolated_workspace / res["out"]["out_dir"]
    for name in ("05-engine-feedback.md", "06-counterfactuals.md",
                 "07-fr-dispositions.md", "08-prechecks.md", "09-chain-walks.md"):
        assert not (out_dir / name).exists(), f"unexpected L5 file {name} on absence-fixture"


def test_l5_session_export_reconciles_stale_files(isolated_workspace):
    """If a prior export wrote 05-engine-feedback.md and the substrate row was
    deleted before the next export, the rerun must remove the stale file."""
    out_dir = isolated_workspace / "provenance" / "180-export-fixture"
    out_dir.mkdir(parents=True, exist_ok=True)
    stale = out_dir / "05-engine-feedback.md"
    stale.write_text("# stale L5 file from prior export — substrate row no longer exists\n")
    _run_cli_in(isolated_workspace, [
        "submit", "close-record", "--payload",
        json.dumps({"summary": "L5 reconciliation fixture close-record", "items": []}),
    ])
    res = _run_cli_in(isolated_workspace, ["export", "--session", "180", "--write"])
    assert res["rc"] == 0, res
    assert not stale.exists()
    deleted = res["out"]["l5_files_deleted"]
    assert any(d.endswith("05-engine-feedback.md") for d in deleted), res


def test_l5_session_write_triggers_issues_and_spec_versions_regen(isolated_workspace):
    """`selvedge export --session N --write` must regenerate workspace-wide
    open-issues/index.md and specifications/_versions.md as part of the close-
    ceremony command, so close commits everything in one shot."""
    _run_cli_in(isolated_workspace, [
        "submit", "issue", "--payload",
        json.dumps({"alias": "OI-S180-9", "title": "L5 trigger fixture issue", "priority": "MEDIUM"}),
    ])
    _run_cli_in(isolated_workspace, [
        "submit", "close-record", "--payload",
        json.dumps({"summary": "L5 trigger fixture close", "items": []}),
    ])
    res = _run_cli_in(isolated_workspace, ["export", "--session", "180", "--write"])
    assert res["rc"] == 0, res
    issues_index = isolated_workspace / "open-issues" / "index.md"
    spec_index = isolated_workspace / "specifications" / "_versions.md"
    assert issues_index.exists(), "issues regen did not run alongside --session N --write"
    assert spec_index.exists(), "spec_versions regen did not run alongside --session N --write"
    assert "OI-S180-9" in issues_index.read_text()
    spec_text = spec_index.read_text()
    assert "Spec versions" in spec_text
    assert "| Spec |" in spec_text
    assert res["out"]["issues_export"]["dry_run"] is False
    assert res["out"]["spec_versions_export"]["dry_run"] is False


def test_l5_session_dry_run_does_not_write_workspace_indexes(isolated_workspace):
    """Dry-run --session must not land issues/index.md or specifications/_versions.md."""
    _run_cli_in(isolated_workspace, [
        "submit", "close-record", "--payload",
        json.dumps({"summary": "L5 dry-run fixture close", "items": []}),
    ])
    res = _run_cli_in(isolated_workspace, ["export", "--session", "180"])
    assert res["rc"] == 0, res
    assert not (isolated_workspace / "open-issues").exists()
    assert not (isolated_workspace / "specifications" / "_versions.md").exists()
    assert res["out"]["issues_export"]["dry_run"] is True
    assert res["out"]["spec_versions_export"]["dry_run"] is True


def test_l5_session_export_idempotent(isolated_workspace):
    """Running export --session N --write twice must produce identical files
    on the second run (deterministic ordering, no live timestamps in body)."""
    _run_cli_in(isolated_workspace, [
        "submit", "engine-feedback", "--payload",
        json.dumps({"flag": "observation",
                    "body_md": "**l5-idempotence:** body content for idempotence test."}),
    ])
    _run_cli_in(isolated_workspace, [
        "submit", "close-record", "--payload",
        json.dumps({"summary": "L5 idempotence fixture close", "items": []}),
    ])
    r1 = _run_cli_in(isolated_workspace, ["export", "--session", "180", "--write"])
    assert r1["rc"] == 0, r1
    out_dir = isolated_workspace / r1["out"]["out_dir"]
    snapshot = {p.name: p.read_text() for p in out_dir.glob("*.md")}
    issues_index = isolated_workspace / "open-issues" / "index.md"
    spec_index = isolated_workspace / "specifications" / "_versions.md"
    snapshot["__issues_index"] = issues_index.read_text() if issues_index.exists() else ""
    snapshot["__spec_index"] = spec_index.read_text() if spec_index.exists() else ""
    r2 = _run_cli_in(isolated_workspace, ["export", "--session", "180", "--write"])
    assert r2["rc"] == 0, r2
    rerun = {p.name: p.read_text() for p in out_dir.glob("*.md")}
    rerun["__issues_index"] = issues_index.read_text() if issues_index.exists() else ""
    rerun["__spec_index"] = spec_index.read_text() if spec_index.exists() else ""
    assert snapshot == rerun, "L5 export was not idempotent across reruns (per-session or workspace-wide indexes)"
