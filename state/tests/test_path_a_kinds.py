"""Tests for engine-v20+ Path A submit kinds: decision-record, perspective-position,
perspective-claim, review-finding, finding-disposition, close-record, legacy-import,
spec-section, spec-clause.

These handlers were added in S080+ as the substrate-only-writes replacement for
the legacy markdown-shaped flow. Test coverage was deferred (OI-S090-2) and is
now landing here."""
from __future__ import annotations

import hashlib
import json

import pytest

from conftest import PRIMARY_DB, WORKSPACE


# ---------------------------------------------------------------------------
# decision-record (_submit_decision_v2)
# ---------------------------------------------------------------------------


def _minimal_decision_payload(**overrides) -> dict:
    """Smallest admissible decision-record payload. Override fields per test.

    Default kind is `procedural` (T-33 admitted-zero per DV-S179-1 / migration
    035) so most tests do not need to obtain a precheck nonce. Tests that
    specifically exercise kind=substantive must call `_run_precheck` first
    and pass the returned nonce as `precheck_nonce` in overrides.
    """
    base = {
        "title": "pytest decision-record happy path",
        "kind": "procedural",
        "outcome_type": "adopt",
        "target_kind": "process_rule",
        "target_key": "pytest-target",
    }
    base.update(overrides)
    return base


def _run_precheck(selvedge_cli, target_kind: str, target_key: str) -> str:
    """Run `bin/selvedge precheck --target-kind ... --target-key ...` and
    return the generated single-use nonce (T-33 enabling, engine-v49)."""
    import subprocess
    from conftest import BIN, WORKSPACE
    proc = subprocess.run(
        [str(BIN), "precheck", "--target-kind", target_kind, "--target-key", target_key],
        capture_output=True, text=True,
        env={"SELVEDGE_WORKSPACE": str(WORKSPACE), **__import__("os").environ},
    )
    assert proc.returncode == 0, f"precheck failed: rc={proc.returncode} stderr={proc.stderr}"
    # Output line: "precheck_id=N nonce=<hex> target_kind=... ..."
    for tok in proc.stdout.split():
        if tok.startswith("nonce="):
            return tok.split("=", 1)[1]
    raise AssertionError(f"no nonce in precheck output: {proc.stdout!r}")


def test_decision_record_minimal_creates_row_and_alias(clean_substrate, selvedge_cli, db):
    # Substantive kind requires a single-use precheck nonce per T-33 (DV-S179-1).
    nonce = _run_precheck(selvedge_cli, "process_rule", "pytest-target")
    payload = _minimal_decision_payload(kind="substantive", precheck_nonce=nonce)
    res = selvedge_cli(
        ["submit", "decision-record", "--payload", json.dumps(payload)]
    )
    assert res["out"]["ok"], res
    did = res["out"]["result"]["decision_v2_id"]
    decision_no = res["out"]["result"]["decision_no"]
    wno = db.execute(
        "SELECT s.workspace_session_no FROM decisions_v2 d "
        "JOIN sessions s ON s.session_id=d.session_id WHERE d.decision_v2_id=?",
        (did,),
    ).fetchone()["workspace_session_no"]
    assert res["out"]["result"]["alias"] == f"DV-S{wno:03d}-{decision_no}"
    row = db.execute(
        "SELECT decision_no, kind, outcome_type, target_kind, target_key "
        "FROM decisions_v2 WHERE decision_v2_id=?",
        (did,),
    ).fetchone()
    assert row["kind"] == "substantive"
    assert row["outcome_type"] == "adopt"
    assert row["target_key"] == "pytest-target"


def test_decision_record_supports_and_alternatives(clean_substrate, selvedge_cli, db):
    # T-34 (engine-v49, migration 036) refuses NULL cited_object_id on
    # cite-required bases; seed a prior procedural DV to cite.
    seed = selvedge_cli(
        ["submit", "decision-record", "--payload", json.dumps(
            _minimal_decision_payload(title="seed prior DV for cite")
        )]
    )
    seed_alias = seed["out"]["result"]["alias"]
    payload = _minimal_decision_payload(
        title="decision with supports + alternative",
        supports=[
            {"basis": "prior_decision", "claim": "cites seed DV via T-34", "cite": seed_alias},
        ],
        alternatives=[
            {
                "label": "R-1.1",
                "option": "alternative we considered and rejected",
                "rejections": [
                    {
                        "basis": "inferior_tradeoff",
                        "reason": "rejected for being slower with no countervailing gain",
                    }
                ],
            }
        ],
    )
    res = selvedge_cli(["submit", "decision-record", "--payload", json.dumps(payload)])
    assert res["out"]["ok"], res
    did = res["out"]["result"]["decision_v2_id"]
    assert len(res["out"]["result"]["alternatives"]) == 1
    n_supports = db.execute(
        "SELECT COUNT(*) AS n FROM decision_supports WHERE decision_v2_id=?", (did,)
    ).fetchone()["n"]
    n_alts = db.execute(
        "SELECT COUNT(*) AS n FROM alternatives_v2 WHERE decision_v2_id=?", (did,)
    ).fetchone()["n"]
    n_rej = db.execute(
        "SELECT COUNT(*) AS n FROM alternative_rejections ar "
        "JOIN alternatives_v2 a ON a.alternative_v2_id=ar.alternative_v2_id "
        "WHERE a.decision_v2_id=?",
        (did,),
    ).fetchone()["n"]
    assert (n_supports, n_alts, n_rej) == (1, 1, 1)


def test_decision_record_closes_issue_dispatches_disposition(clean_substrate, selvedge_cli, db):
    """closes_issue effect should atomically transition the target issue to
    resolved via _submit_issue_disposition (engine-v28 behaviour)."""
    seed = selvedge_cli(
        [
            "submit", "issue", "--payload",
            json.dumps({
                "session_no": 1,
                "alias": "OI-S001-7",
                "title": "issue to be closed by a decision",
                "priority": "MEDIUM",
            }),
        ]
    )
    assert seed["out"]["ok"], seed
    iid = seed["out"]["result"]["issue_id"]

    payload = _minimal_decision_payload(
        title="decision that closes an issue via closes_issue",
        outcome_type="adopt",
        target_kind="issue",
        target_key="OI-S001-7",
        effects=[
            {
                "effect_kind": "closes_issue",
                "target": "OI-S001-7",
                "target_descriptor": "resolved by the pytest closes_issue regression test",
            }
        ],
    )
    res = selvedge_cli(["submit", "decision-record", "--payload", json.dumps(payload)])
    assert res["out"]["ok"], res
    status = db.execute("SELECT status FROM issues WHERE issue_id=?", (iid,)).fetchone()["status"]
    assert status == "resolved"


def test_decision_record_closes_issue_without_descriptor_refused(clean_substrate, selvedge_cli):
    selvedge_cli(
        [
            "submit", "issue", "--payload",
            json.dumps({
                "session_no": 1, "alias": "OI-S001-8",
                "title": "issue for descriptor-required test", "priority": "LOW",
            }),
        ]
    )
    payload = _minimal_decision_payload(
        title="closes_issue missing target_descriptor — should refuse",
        target_kind="issue", target_key="OI-S001-8",
        effects=[{"effect_kind": "closes_issue", "target": "OI-S001-8"}],
    )
    res = selvedge_cli(
        ["submit", "decision-record", "--payload", json.dumps(payload)],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_VALIDATION" in res["err"]


def test_decision_record_closes_issue_short_descriptor_refused(clean_substrate, selvedge_cli):
    selvedge_cli(
        [
            "submit", "issue", "--payload",
            json.dumps({
                "session_no": 1, "alias": "OI-S001-9",
                "title": "issue for descriptor-length test", "priority": "LOW",
            }),
        ]
    )
    payload = _minimal_decision_payload(
        title="closes_issue with too-short target_descriptor",
        target_kind="issue", target_key="OI-S001-9",
        effects=[
            {
                "effect_kind": "closes_issue",
                "target": "OI-S001-9",
                "target_descriptor": "short",
            }
        ],
    )
    res = selvedge_cli(
        ["submit", "decision-record", "--payload", json.dumps(payload)],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_VALIDATION" in res["err"]


# ---------------------------------------------------------------------------
# T-32 substrate-gate: decision_chain_walks dispatched in-band per cited alias
# (engine-v48, DV-S176-1, migration 031).
# ---------------------------------------------------------------------------


def test_decision_record_no_cites_admits_zero_walks(clean_substrate, selvedge_cli, db):
    res = selvedge_cli(
        ["submit", "decision-record", "--payload", json.dumps(_minimal_decision_payload())]
    )
    assert res["out"]["ok"], res
    did = res["out"]["result"]["decision_v2_id"]
    assert res["out"]["result"]["chain_walks"] == []
    n = db.execute(
        "SELECT COUNT(*) AS n FROM decision_chain_walks WHERE decision_v2_id=?", (did,)
    ).fetchone()["n"]
    assert n == 0


def _seed_ef(selvedge_cli) -> str:
    """Submit one engine_feedback row in the open session; return its EF alias."""
    res = selvedge_cli(
        [
            "submit", "engine-feedback", "--payload",
            json.dumps({
                "flag": "observation",
                "body_md": "Seed EF for chain-walk test",
            }),
        ]
    )
    assert res["out"]["ok"], res
    return res["out"]["result"]["alias"]


def test_decision_record_cite_dispatches_chain_walk(clean_substrate, selvedge_cli, db):
    ef_alias = _seed_ef(selvedge_cli)
    payload = _minimal_decision_payload(
        title="decision-record citing EF alias triggers chain-walk receipt",
        supports=[{
            "basis": "engine_feedback",
            "claim": "T-32 happy-path: cited EF alias must materialise one chain_walks row.",
            "cite": ef_alias,
        }],
    )
    res = selvedge_cli(["submit", "decision-record", "--payload", json.dumps(payload)])
    assert res["out"]["ok"], res
    did = res["out"]["result"]["decision_v2_id"]
    walks = res["out"]["result"]["chain_walks"]
    assert len(walks) == 1
    assert walks[0]["anchor_alias"] == ef_alias
    row = db.execute(
        "SELECT anchor_alias, max_depth, walker_version, nodes_visited, "
        "edges_traversed, truncation_status, length(result_text) AS body_len, "
        "length(result_sha256) AS sha_len FROM decision_chain_walks WHERE decision_v2_id=?",
        (did,),
    ).fetchone()
    assert row["anchor_alias"] == ef_alias
    assert row["max_depth"] == 3
    assert row["walker_version"] == "v1"
    assert row["nodes_visited"] >= 1
    assert row["truncation_status"] in ("none", "depth_capped")
    assert row["body_len"] > 0
    assert row["sha_len"] == 64


def test_decision_record_effects_target_oi_dispatches_chain_walk(clean_substrate, selvedge_cli, db):
    """closes_issue effect target=OI-... is a citable anchor (walker resolves via issues table)."""
    seed = selvedge_cli(
        [
            "submit", "issue", "--payload",
            json.dumps({
                "session_no": 1, "alias": "OI-S001-99",
                "title": "issue closed by decision and walked via effects.target",
                "priority": "LOW",
            }),
        ]
    )
    assert seed["out"]["ok"], seed
    payload = _minimal_decision_payload(
        title="closes_issue effect target dispatches chain-walk on OI alias",
        target_kind="issue",
        target_key="OI-S001-99",
        effects=[{
            "effect_kind": "closes_issue",
            "target": "OI-S001-99",
            "target_descriptor": "resolved by closes_issue chain-walk regression test",
        }],
    )
    res = selvedge_cli(["submit", "decision-record", "--payload", json.dumps(payload)])
    assert res["out"]["ok"], res
    walks = res["out"]["result"]["chain_walks"]
    assert len(walks) == 1
    assert walks[0]["anchor_alias"] == "OI-S001-99"


def test_decision_record_unresolved_cite_refuses(clean_substrate, selvedge_cli):
    """Unresolved supports.cite is caught at T-01 alias-resolve before T-32 dispatch;
    either refusal is acceptable as long as the offending alias is named."""
    payload = _minimal_decision_payload(
        title="decision-record citing nonexistent alias must refuse",
        supports=[{
            "basis": "prior_decision",
            "claim": "Unresolved-alias path: this DV alias does not exist.",
            "cite": "DV-S999-9",
        }],
    )
    res = selvedge_cli(
        ["submit", "decision-record", "--payload", json.dumps(payload)],
        expect_ok=False,
    )
    assert res["rc"] != 0
    blob = (res.get("err", "") or "") + json.dumps(res.get("out") or {})
    assert "DV-S999-9" in blob
    assert "E_REFUSAL_T01" in blob or "E_REFUSAL_T32" in blob


def test_decision_record_walker_failure_on_effects_target_refuses_t32(clean_substrate, selvedge_cli):
    """effects.target bypasses supports.cite alias-resolution, so a target that
    fails the walker reaches the T-32 dispatch path. closes_issue refuses earlier
    via _resolve_issue_alias, but a creates/modifies effect.target that the
    walker cannot resolve hits the T-32 path."""
    payload = _minimal_decision_payload(
        title="decision-record creates effect with unresolvable target hits T-32",
        effects=[{
            "effect_kind": "creates",
            "target": "DV-S888-8",
            "target_descriptor": "ghost target",
        }],
    )
    res = selvedge_cli(
        ["submit", "decision-record", "--payload", json.dumps(payload)],
        expect_ok=False,
    )
    assert res["rc"] != 0
    blob = (res.get("err", "") or "") + json.dumps(res.get("out") or {})
    assert "DV-S888-8" in blob


def test_decision_record_dedupes_repeated_cites(clean_substrate, selvedge_cli, db):
    ef_alias = _seed_ef(selvedge_cli)
    payload = _minimal_decision_payload(
        title="decision-record citing same alias in support and rejection",
        supports=[{"basis": "engine_feedback", "claim": f"first cite to {ef_alias} alias for dedup test.", "cite": ef_alias}],
        alternatives=[{
            "label": "R-1.1",
            "option": f"alternative path rejected per {ef_alias} same alias.",
            "rejections": [{"basis": "redundant_with_existing", "reason": f"redundant per {ef_alias} same alias.", "cite": ef_alias}],
        }],
    )
    res = selvedge_cli(["submit", "decision-record", "--payload", json.dumps(payload)])
    assert res["out"]["ok"], res
    did = res["out"]["result"]["decision_v2_id"]
    walks = res["out"]["result"]["chain_walks"]
    assert len(walks) == 1
    n = db.execute(
        "SELECT COUNT(*) AS n FROM decision_chain_walks WHERE decision_v2_id=?", (did,)
    ).fetchone()["n"]
    assert n == 1


# ---------------------------------------------------------------------------
# perspective-position / perspective-claim
# ---------------------------------------------------------------------------


def _seed_perspective(selvedge_cli) -> int:
    """Open a deliberation + add one perspective; return perspective_id."""
    delib = selvedge_cli(
        [
            "submit", "deliberation-open", "--payload",
            json.dumps({"session_no": 1, "topic": "pytest deliberation"}),
        ]
    )
    did = delib["out"]["result"]["deliberation_id"]
    persp = selvedge_cli(
        [
            "submit", "perspective", "--payload",
            json.dumps({
                "deliberation_id": did, "label": "p1", "family": "anthropic",
                "body_md": "pytest perspective body",
            }),
        ]
    )
    return persp["out"]["result"]["perspective_id"]


def test_perspective_position_inserts_row(clean_substrate, selvedge_cli, db):
    pid = _seed_perspective(selvedge_cli)
    res = selvedge_cli(
        [
            "submit", "perspective-position", "--payload",
            json.dumps({"perspective_id": pid, "position": "the position statement, distilled"}),
        ]
    )
    assert res["out"]["ok"], res
    pos_id = res["out"]["result"]["position_id"]
    row = db.execute(
        "SELECT perspective_id, object_id FROM perspective_positions WHERE position_id=?", (pos_id,)
    ).fetchone()
    assert row["perspective_id"] == pid
    assert row["object_id"] is not None
    obj = db.execute(
        "SELECT object_kind, typed_row_id FROM objects WHERE object_id=?", (row["object_id"],)
    ).fetchone()
    assert obj["object_kind"] == "perspective_position"
    assert obj["typed_row_id"] == pos_id


def test_perspective_position_unknown_perspective_refused(clean_substrate, selvedge_cli):
    res = selvedge_cli(
        [
            "submit", "perspective-position", "--payload",
            json.dumps({"perspective_id": 999999, "position": "should fail"}),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_NOT_FOUND" in res["err"]


def test_perspective_claim_inserts_with_section_kind(clean_substrate, selvedge_cli, db):
    pid = _seed_perspective(selvedge_cli)
    res = selvedge_cli(
        [
            "submit", "perspective-claim", "--payload",
            json.dumps({
                "perspective_id": pid,
                "claim": "pytest claim under section_kind=position",
                "section_kind": "position",
            }),
        ]
    )
    assert res["out"]["ok"], res
    assert res["out"]["result"]["seq"] == 1


def test_perspective_claim_with_cite_resolves(clean_substrate, selvedge_cli, db):
    """A perspective_claim citing an existing object alias should resolve and
    record cited_object_id."""
    pid = _seed_perspective(selvedge_cli)
    # The perspective itself has an object alias we can cite.
    persp_alias_row = db.execute(
        "SELECT alias FROM objects WHERE object_kind='perspective' AND typed_row_id=?", (pid,)
    ).fetchone()
    persp_alias = persp_alias_row["alias"] if persp_alias_row else None
    if not persp_alias:
        pytest.skip("perspective has no alias to cite")
    res = selvedge_cli(
        [
            "submit", "perspective-claim", "--payload",
            json.dumps({
                "perspective_id": pid,
                "claim": f"this claim cites [{persp_alias}] as a known anchor",
                "section_kind": "position",
                "cite": persp_alias,
            }),
        ]
    )
    assert res["out"]["ok"], res
    cid = res["out"]["result"]["claim_id"]
    cited = db.execute(
        "SELECT cited_object_id FROM perspective_claims WHERE claim_id=?", (cid,)
    ).fetchone()
    assert cited["cited_object_id"] is not None


# ---------------------------------------------------------------------------
# review-finding / finding-disposition
# ---------------------------------------------------------------------------


def test_review_finding_inserts_with_alias(clean_substrate, selvedge_cli, db):
    res = selvedge_cli(
        [
            "submit", "review-finding", "--payload",
            json.dumps({
                "session_no": 1,
                "iteration": 1,
                "severity": "low",
                "finding": "pytest finding under iteration=1",
            }),
        ]
    )
    assert res["out"]["ok"], res
    rfid = res["out"]["result"]["review_finding_id"]
    row = db.execute(
        "SELECT severity, disposition, object_id FROM review_findings WHERE review_finding_id=?",
        (rfid,),
    ).fetchone()
    assert row["severity"] == "low"
    assert row["disposition"] == "open"
    wno = db.execute(
        "SELECT s.workspace_session_no FROM review_findings rf "
        "JOIN sessions s ON s.session_id=rf.session_id WHERE rf.review_finding_id=?",
        (rfid,),
    ).fetchone()["workspace_session_no"]
    obj = db.execute(
        "SELECT alias FROM objects WHERE object_id=?", (row["object_id"],)
    ).fetchone()
    assert obj["alias"] == f"RF-S{wno:03d}-1-{rfid}"


def test_finding_disposition_updates_status(clean_substrate, selvedge_cli, db):
    create = selvedge_cli(
        [
            "submit", "review-finding", "--payload",
            json.dumps({
                "session_no": 1, "iteration": 1, "severity": "medium",
                "finding": "finding to be dispositioned",
            }),
        ]
    )
    rfid = create["out"]["result"]["review_finding_id"]
    res = selvedge_cli(
        [
            "submit", "finding-disposition", "--payload",
            json.dumps({
                "review_finding_id": rfid,
                "disposition": "fixed",
                "disposition_text": "addressed by the disposition pytest",
            }),
        ]
    )
    assert res["out"]["ok"], res
    row = db.execute(
        "SELECT disposition FROM review_findings WHERE review_finding_id=?", (rfid,)
    ).fetchone()
    assert row["disposition"] == "fixed"


def test_finding_disposition_unknown_id_refused(clean_substrate, selvedge_cli):
    res = selvedge_cli(
        [
            "submit", "finding-disposition", "--payload",
            json.dumps({
                "review_finding_id": 999999,
                "disposition": "fixed",
                "disposition_text": "should fail",
            }),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_NOT_FOUND" in res["err"]


# ---------------------------------------------------------------------------
# close-record
# ---------------------------------------------------------------------------


def test_close_record_with_items_inserts_alias_and_state_items(clean_substrate, selvedge_cli, db):
    res = selvedge_cli(
        [
            "submit", "close-record", "--payload",
            json.dumps({
                "session_no": 1,
                "summary": "pytest close-record summary atom",
                "items": [
                    {"facet": "what_was_done", "text": "pytest exercised the close-record handler"},
                    {"facet": "next_session_should", "text": "pytest follow-up FR for the close-record fixture"},
                ],
            }),
        ]
    )
    assert res["out"]["ok"], res
    crid = res["out"]["result"]["close_record_id"]
    assert res["out"]["result"]["alias"].startswith("C-S")
    n_items = db.execute(
        "SELECT COUNT(*) AS n FROM close_state_items WHERE close_record_id=?", (crid,)
    ).fetchone()["n"]
    assert n_items == 2


# ---------------------------------------------------------------------------
# legacy-import
# ---------------------------------------------------------------------------


def test_legacy_import_inserts_row_and_atom(clean_substrate, selvedge_cli, db):
    res = selvedge_cli(
        [
            "submit", "legacy-import", "--payload",
            json.dumps({
                "session_no": 1,
                "old_table": "decisions",
                "old_pk": 1,
                "text": "legacy text body imported under pytest fixture",
            }),
        ]
    )
    assert res["out"]["ok"], res
    lid = res["out"]["result"]["legacy_import_id"]
    row = db.execute(
        "SELECT old_table, old_pk, decomposition_status FROM legacy_imports WHERE legacy_import_id=?",
        (lid,),
    ).fetchone()
    assert row["old_table"] == "decisions"
    assert row["old_pk"] == 1
    assert row["decomposition_status"] == "unratified"


# ---------------------------------------------------------------------------
# spec-section / spec-clause
# ---------------------------------------------------------------------------


def _seed_spec_version(selvedge_cli) -> int:
    body_dir = WORKSPACE / "state" / "tests" / "spec-bodies"
    body_dir.mkdir(parents=True, exist_ok=True)
    body = body_dir / "spec-section-fixture.md"
    body.write_text("fixture body for spec-section / spec-clause tests\n")
    body_rel = body.relative_to(WORKSPACE).as_posix()
    sha = hashlib.sha256(body.read_bytes()).hexdigest()
    res = selvedge_cli(
        [
            "submit", "spec-version", "--payload",
            json.dumps({
                "session_no": 1, "spec_id": "section-fixture", "version": 1,
                "body_path": body_rel, "body_sha256": sha,
            }),
        ]
    )
    assert res["out"]["ok"], res
    # The result returns alias; we want the spec_version_id.
    import sqlite3
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        row = conn.execute(
            "SELECT spec_version_id FROM spec_versions WHERE spec_id='section-fixture' AND version=1"
        ).fetchone()
    finally:
        conn.close()
    return row[0]


def test_spec_section_inserts_with_intent(clean_substrate, selvedge_cli, db):
    sv_id = _seed_spec_version(selvedge_cli)
    res = selvedge_cli(
        [
            "submit", "spec-section", "--payload",
            json.dumps({
                "session_no": 1,
                "spec_version_id": sv_id,
                "ord": 1,
                "heading": "Pytest spec-section heading atom",
                "intent": "intent atom for the pytest spec-section fixture body",
            }),
        ]
    )
    assert res["out"]["ok"], res
    ssid = res["out"]["result"]["spec_section_id"]
    row = db.execute(
        "SELECT ord, intent_atom_id FROM spec_sections WHERE spec_section_id=?", (ssid,)
    ).fetchone()
    assert row["ord"] == 1
    assert row["intent_atom_id"] is not None


def test_spec_clause_inserts_with_normative_level(clean_substrate, selvedge_cli, db):
    sv_id = _seed_spec_version(selvedge_cli)
    sec = selvedge_cli(
        [
            "submit", "spec-section", "--payload",
            json.dumps({
                "session_no": 1, "spec_version_id": sv_id, "ord": 1,
                "heading": "Section for clause pytest fixture",
            }),
        ]
    )
    ssid = sec["out"]["result"]["spec_section_id"]
    # T-35 (engine-v49, migration 038) refuses NULL source_decision_v2_id on
    # spec_clause INSERT; seed a procedural DV and cite it.
    src_dv = selvedge_cli(
        ["submit", "decision-record", "--payload", json.dumps(
            _minimal_decision_payload(title="seed source DV for spec_clause T-35")
        )]
    )
    src_alias = src_dv["out"]["result"]["alias"]
    res = selvedge_cli(
        [
            "submit", "spec-clause", "--payload",
            json.dumps({
                "session_no": 1,
                "spec_section_id": ssid, "ord": 1,
                "clause": "clause text exercised by the pytest fixture",
                "clause_type": "rule",
                "normative_level": "must",
                "source_decision_alias": src_alias,
            }),
        ]
    )
    assert res["out"]["ok"], res
    scid = res["out"]["result"]["spec_clause_id"]
    row = db.execute(
        "SELECT normative_level, clause_type FROM spec_clauses WHERE spec_clause_id=?", (scid,)
    ).fetchone()
    assert row["normative_level"] == "must"
    assert row["clause_type"] == "rule"


# ---------------------------------------------------------------------------
# T-33 / T-34 / T-35 / slug-UNIQUE / harness-alias registration tests
# (engine-v49, DV-S179-1, migrations 033-039)
# ---------------------------------------------------------------------------


def test_t33_substantive_decision_without_precheck_refused(clean_substrate, selvedge_cli):
    payload = _minimal_decision_payload(kind="substantive")
    res = selvedge_cli(
        ["submit", "decision-record", "--payload", json.dumps(payload)],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_T33" in res["err"]
    assert "precheck_nonce" in res["err"]


def test_t33_schema_migration_decision_without_precheck_refused(clean_substrate, selvedge_cli):
    payload = _minimal_decision_payload(kind="schema_migration")
    res = selvedge_cli(
        ["submit", "decision-record", "--payload", json.dumps(payload)],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_T33" in res["err"]


def test_t33_precheck_nonce_consumed_single_use(clean_substrate, selvedge_cli):
    nonce = _run_precheck(selvedge_cli, "process_rule", "single-use-key")
    payload = _minimal_decision_payload(
        kind="substantive", target_key="single-use-key", precheck_nonce=nonce
    )
    res1 = selvedge_cli(["submit", "decision-record", "--payload", json.dumps(payload)])
    assert res1["out"]["ok"]
    # Re-submit with same nonce -> consumed-error.
    payload2 = _minimal_decision_payload(
        kind="substantive", target_key="single-use-key", precheck_nonce=nonce,
        title="second decision attempting to reuse the same nonce",
    )
    res2 = selvedge_cli(
        ["submit", "decision-record", "--payload", json.dumps(payload2)], expect_ok=False
    )
    assert "already consumed" in res2["err"]


def test_t33_precheck_target_key_mismatch_refused(clean_substrate, selvedge_cli):
    nonce = _run_precheck(selvedge_cli, "process_rule", "key-A")
    payload = _minimal_decision_payload(
        kind="substantive", target_key="key-B-different", precheck_nonce=nonce
    )
    res = selvedge_cli(
        ["submit", "decision-record", "--payload", json.dumps(payload)], expect_ok=False
    )
    assert "target_key" in res["err"]
    assert "E_REFUSAL_T33" in res["err"]


def test_t33_procedural_kind_admits_zero_precheck(clean_substrate, selvedge_cli):
    """T-33 admit-zero predicate: kind in (procedural, calibration, disposition)
    submits without precheck like T-32 admits zero-cite."""
    for kind in ("procedural", "calibration", "disposition"):
        payload = _minimal_decision_payload(
            kind=kind, target_key=f"admit-zero-{kind}",
            title=f"kind-admitted-zero {kind} decision-record",
        )
        res = selvedge_cli(["submit", "decision-record", "--payload", json.dumps(payload)])
        assert res["out"]["ok"], f"kind={kind} failed: {res}"


def test_t34_decision_supports_null_cite_on_required_basis_refused(clean_substrate, selvedge_cli, db):
    nonce = _run_precheck(selvedge_cli, "process_rule", "t34-test-key")
    payload = _minimal_decision_payload(
        kind="substantive", target_key="t34-test-key", precheck_nonce=nonce,
        supports=[
            {"basis": "operator_directive", "claim": "operator directive without cite"},
        ],
    )
    res = selvedge_cli(
        ["submit", "decision-record", "--payload", json.dumps(payload)], expect_ok=False
    )
    assert "E_REFUSAL_T34" in res["err"], res


def test_t35_spec_clause_null_source_decision_refused(clean_substrate, selvedge_cli, db):
    sv_id = _seed_spec_version(selvedge_cli)
    sec = selvedge_cli(
        ["submit", "spec-section", "--payload", json.dumps({
            "session_no": 1, "spec_version_id": sv_id, "ord": 1,
            "heading": "Section for T-35 refusal test",
        })]
    )
    ssid = sec["out"]["result"]["spec_section_id"]
    res = selvedge_cli(
        ["submit", "spec-clause", "--payload", json.dumps({
            "session_no": 1, "spec_section_id": ssid, "ord": 1,
            "clause": "clause without source_decision_alias should refuse",
            "clause_type": "rule", "normative_level": "must",
        })], expect_ok=False
    )
    assert "E_REFUSAL_T35" in res["err"]


def test_sessions_slug_unique_index_refuses_duplicate(clean_substrate, db):
    """Migration 037 added UNIQUE index on sessions.slug."""
    import sqlite3
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                "INSERT INTO sessions (session_no, slug, mode, workspace_id, "
                "engine_version_at_open, status, kind) VALUES (?,?,?,?,?,?,?)",
                (999, "pytest", "self-development", "selvedge-self-development",
                 "engine-v17", "open", "spec_only"),
            )
            conn.commit()
    finally:
        conn.close()


def test_atom_length_support_claim_widened_to_480(clean_substrate, selvedge_cli):
    """Migration 039 widened text_atoms CHECK so atom_type IN (support_claim,finding)
    admits length 8-480. Verify 250-char support_claim succeeds (would have refused
    pre-039 as E_ATOM_LENGTH)."""
    nonce = _run_precheck(selvedge_cli, "process_rule", "atom-len-test")
    long_claim = "x" * 260
    payload = _minimal_decision_payload(
        kind="substantive", target_key="atom-len-test", precheck_nonce=nonce,
        supports=[
            {"basis": "operator_directive", "claim": long_claim, "cite": None},
        ],
    )
    # T-34 will block on missing cite, but the atom-length should not be the
    # gate. Test the atom-length directly via close_summary.
    # Use an alternative_rejection reason instead which uses rejection_reason
    # (still 240 cap) — actually use direct support with cite to a seed DV.
    seed = selvedge_cli(["submit", "decision-record", "--payload", json.dumps(
        _minimal_decision_payload(title="seed for atom-length test")
    )])
    seed_alias = seed["out"]["result"]["alias"]
    nonce2 = _run_precheck(selvedge_cli, "process_rule", "atom-len-test-2")
    payload = _minimal_decision_payload(
        kind="substantive", target_key="atom-len-test-2", precheck_nonce=nonce2,
        supports=[
            {"basis": "prior_decision", "claim": long_claim, "cite": seed_alias},
        ],
    )
    res = selvedge_cli(["submit", "decision-record", "--payload", json.dumps(payload)])
    assert res["out"]["ok"], res


def test_harness_alias_registered_in_objects_post_033(clean_substrate, db):
    """Migration 033 widened objects.object_kind CHECK to admit reference_harness
    and registered every existing reference_harnesses.alias. Verify that an
    INSERT of a reference_harness object_kind row succeeds (proves CHECK
    widening took effect)."""
    import sqlite3
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        conn.execute("PRAGMA foreign_keys=ON")
        conn.execute(
            "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES (?,?,?)",
            ("reference_harness", 99999, "RH-PYTEST-1"),
        )
        conn.commit()
        row = conn.execute(
            "SELECT alias FROM objects WHERE object_kind='reference_harness' AND alias='RH-PYTEST-1'"
        ).fetchone()
        assert row is not None
    finally:
        conn.close()
