"""`selvedge subtract-eligibility` — deterministic subtract-rule report.

Per 078 D-6: the report is rule-based; the human reviewer-subtractor reads it
and acts. 079 ships the rule scaffold; numbers are operator-tunable in 080+.
"""

from __future__ import annotations

import json
import sqlite3

from .paths import db_path


def cmd_subtract_eligibility(args) -> int:
    K_UNCITED = args.uncited_threshold
    M_STALE = args.stale_threshold
    P_TRIAGE = args.untriaged_threshold

    conn = sqlite3.connect(str(db_path()))
    conn.row_factory = sqlite3.Row

    last_session_no = conn.execute(
        "SELECT COALESCE(MAX(session_no),0) AS n FROM sessions"
    ).fetchone()["n"]

    uncited = conn.execute(
        """
        SELECT sv.spec_id, sv.version,
               (SELECT MAX(s.session_no) FROM refs r
                  JOIN objects o_target ON o_target.object_id = r.target_object_id
                  JOIN spec_versions sv2 ON sv2.object_id = o_target.object_id
                  JOIN objects o_source ON o_source.object_id = r.source_object_id
                  JOIN sessions s ON s.session_id = (
                    SELECT CASE o_source.object_kind
                        WHEN 'decision' THEN (SELECT session_id FROM decisions WHERE decision_id = o_source.typed_row_id)
                        ELSE NULL END
                  )
                WHERE sv2.spec_version_id = sv.spec_version_id) AS last_cite_session_no
          FROM spec_versions sv
         WHERE sv.status='active'
        """
    ).fetchall()
    uncited_eligible = []
    for r in uncited:
        last = r["last_cite_session_no"]
        gap = last_session_no - (last or 0)
        if last is None or gap >= K_UNCITED:
            uncited_eligible.append(
                {"spec": f"{r['spec_id']}-v{r['version']}", "last_cite_session_no": last, "gap": gap}
            )

    stale = conn.execute(
        """
        SELECT c.commitment_id, c.summary_md, s.session_no AS opened_in
          FROM commitments c
          JOIN decisions d ON d.decision_id = c.decision_id
          JOIN sessions s ON s.session_id = d.session_id
         WHERE c.status='open'
        """
    ).fetchall()
    stale_eligible = [
        {
            "commitment_id": r["commitment_id"],
            "summary": r["summary_md"],
            "opened_in": r["opened_in"],
            "gap": last_session_no - r["opened_in"],
        }
        for r in stale
        if last_session_no - r["opened_in"] >= M_STALE
    ]

    untri = conn.execute(
        """
        SELECT ef.feedback_id, ef.flag, ef.body_md, s.session_no AS opened_in
          FROM engine_feedback ef
          JOIN sessions s ON s.session_id = ef.session_id
         WHERE ef.disposition IS NULL
        """
    ).fetchall()
    untri_eligible = [
        {
            "feedback_id": r["feedback_id"],
            "flag": r["flag"],
            "summary": (r["body_md"] or "")[:80],
            "opened_in": r["opened_in"],
            "gap": last_session_no - r["opened_in"],
        }
        for r in untri
        if last_session_no - r["opened_in"] >= P_TRIAGE
    ]

    conn.close()
    report = {
        "last_session_no": last_session_no,
        "thresholds": {"uncited": K_UNCITED, "stale": M_STALE, "untriaged": P_TRIAGE},
        "uncited_active_specs": uncited_eligible,
        "stale_open_commitments": stale_eligible,
        "untriaged_engine_feedback": untri_eligible,
    }
    print(json.dumps(report, indent=2))
    return 0
