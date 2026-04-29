"""Submit-handler dispatch.

`SUBMIT_HANDLERS` maps each `submit <kind>` string to its handler function.
`cmd_submit` parses the payload, opens a write_tx, and dispatches.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from ..connection import Conn
from ..errors import SelvedgeError
from ._helpers import _dry_run_var
from .assessment import _submit_assessment, _submit_legacy_import
from .close import _submit_close_record
from .decision_v2 import _submit_decision_v2
from .deliberation import (
    _submit_deliberation_open,
    _submit_deliberation_seal,
    _submit_perspective,
    _submit_perspective_claim,
    _submit_perspective_position,
    _submit_synthesis_point,
)
from .feedback import (
    _submit_engine_feedback,
    _submit_engine_feedback_disposition,
    _submit_forward_reference_disposition,
)
from .harness import (
    _submit_harness_assumption,
    _submit_harness_claim,
    _submit_harness_dissent,
    _submit_harness_open,
    _submit_harness_result,
    _submit_harness_seal,
    _submit_harness_stress,
    _submit_harness_target,
    _submit_harness_trigger,
    _submit_harness_trigger_fire,
)
from .issue import (
    _submit_issue,
    _submit_issue_disposition,
    _submit_issue_link,
    _submit_issue_note,
    _submit_issue_work_item,
)
from .legacy_decision import _submit_decision
from .review import (
    _submit_finding_disposition,
    _submit_review_finding,
    _submit_review_pass,
)
from .session import _submit_session_close, _submit_session_open
from .spec import _submit_spec_clause, _submit_spec_section, _submit_spec_version


SUBMIT_HANDLERS = {
    "session-open": _submit_session_open,
    "session-close": _submit_session_close,
    "decision": _submit_decision,
    "spec-version": _submit_spec_version,
    "deliberation-open": _submit_deliberation_open,
    "perspective": _submit_perspective,
    "deliberation-seal": _submit_deliberation_seal,
    "synthesis-point": _submit_synthesis_point,
    # Path A (engine-v20+):
    "assessment": _submit_assessment,
    "decision-record": _submit_decision_v2,
    "perspective-position": _submit_perspective_position,
    "perspective-claim": _submit_perspective_claim,
    "review-finding": _submit_review_finding,
    "review-pass": _submit_review_pass,
    "finding-disposition": _submit_finding_disposition,
    "close-record": _submit_close_record,
    "legacy-import": _submit_legacy_import,
    "spec-section": _submit_spec_section,
    "spec-clause": _submit_spec_clause,
    # Issues (engine-v22+):
    "issue": _submit_issue,
    "issue-disposition": _submit_issue_disposition,
    "issue-link": _submit_issue_link,
    "issue-note": _submit_issue_note,
    "issue-work-item": _submit_issue_work_item,
    "engine-feedback": _submit_engine_feedback,
    "engine-feedback-disposition": _submit_engine_feedback_disposition,
    "forward-reference-disposition": _submit_forward_reference_disposition,
    # reference_harness (engine-v35+, S125 closing OI-S124-2):
    "harness-open": _submit_harness_open,
    "harness-target": _submit_harness_target,
    "harness-assumption": _submit_harness_assumption,
    "harness-claim": _submit_harness_claim,
    "harness-stress": _submit_harness_stress,
    "harness-result": _submit_harness_result,
    "harness-dissent": _submit_harness_dissent,
    "harness-trigger": _submit_harness_trigger,
    "harness-trigger-fire": _submit_harness_trigger_fire,
    "harness-seal": _submit_harness_seal,
}


def cmd_submit(args) -> int:
    if args.kind not in SUBMIT_HANDLERS:
        print(f"unknown kind: {args.kind}; known: {sorted(SUBMIT_HANDLERS)}", file=sys.stderr)
        return 2
    if args.payload == "-":
        payload = json.load(sys.stdin)
    elif args.payload.startswith("@"):
        payload = json.loads(Path(args.payload[1:]).read_text())
    else:
        payload = json.loads(args.payload)
    role = args.role or "__cli__"
    dry_run = bool(getattr(args, "dry_run", False))
    c = Conn.open()
    token = _dry_run_var.set(dry_run)
    try:
        result = c.write_tx(
            lambda conn: SUBMIT_HANDLERS[args.kind](conn, payload, role),
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
