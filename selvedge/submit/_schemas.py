"""Declarative payload schemas for every `bin/selvedge submit <kind>`.

This registry is operator-facing documentation, not validation. Handlers in
this package own validation; the entries here describe payload shape so
`bin/selvedge submit-help [kind]` can print expected fields without the
operator reading handler source. If a handler's payload reads diverge from
the registry, the handler is canonical and the registry entry is wrong.

Entry shape (each value is a dict):
    summary      one-sentence description of what the kind writes
    required     list of (name, description) tuples — every key MUST appear
    any_of       list of {"fields": [...], "description": "..."} — payload
                 must include exactly one of `fields`; used for `id|alias`
                 disjunctions where the handler accepts either form
    optional     list of (name, description) tuples — payload may contain
    example      example JSON payload (string; must parse as valid JSON)
    spec_ref     pointer to the prompt/spec section that frames the kind

Examples use realistic literal values (integers, short strings) so an
operator can copy-paste and adjust rather than substitute placeholders.
"""

from __future__ import annotations

# Common fields documented once and referenced by many handlers.
_SESSION_NO_OPTIONAL = (
    "session_no",
    "open session number; defaults to the unique open session if omitted",
)

SUBMIT_SCHEMAS: dict[str, dict] = {
    # ── Session lifecycle ─────────────────────────────────────────────
    "session-open": {
        "summary": "Open a new session; refused if another session is already open.",
        "required": [
            ("slug", "kebab-case session name (immutable post-open per T-23)"),
            ("kind", "one of: coding | spec_only | meta (immutable per T-29)"),
        ],
        "optional": [],
        "example": '{"slug": "my-session-slug", "kind": "coding"}',
        "spec_ref": "prompts/development.md §2",
    },
    "session-close": {
        "summary": "Close the open session; substrate auto-fills engine_version_at_close.",
        "required": [],
        "optional": [
            (
                "session_no",
                "target session by session_no or workspace_session_no; defaults to the unique open session",
            ),
            (
                "engine_version_at_close",
                "override metadata.current_engine_version (rare; usually omitted)",
            ),
        ],
        "example": "{}",
        "spec_ref": "prompts/development.md §9",
    },
    # ── Assessment + close-record ────────────────────────────────────
    "assessment": {
        "summary": "Submit the session assessment (state plus ordered agenda atoms).",
        "required": [
            ("state", "one-sentence read of where the workspace is (atom, 8-240 chars)"),
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            ("agenda", "list of one-sentence agenda atoms; ordered as given"),
        ],
        "example": '{"state": "Workspace is mid-arc and ready for FR-S161-15 implementation.", "agenda": ["item one", "item two"]}',
        "spec_ref": "prompts/development.md §3",
    },
    "close-record": {
        "summary": "Author the session close-record; prerequisite of session-close (T-39).",
        "required": [
            ("summary", "one-sentence summary of what shipped (atom)"),
            (
                "items",
                "non-empty list of {facet, text}; facet ∈ engine_version | what_was_done | state_at_close | open_issues | next_session_should | validator_summary",
            ),
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
        ],
        "example": (
            '{"summary": "Shipped submit-help and orient why-extension.", '
            '"items": ['
            '{"facet": "engine_version", "text": "engine-v47 unchanged."}, '
            '{"facet": "what_was_done", "text": "Added selvedge/submit/_schemas.py registry."}, '
            '{"facet": "next_session_should", "text": "Triage untriaged engine-feedback."}'
            ']}'
        ),
        "spec_ref": "prompts/development.md §9",
    },
    # ── Decisions (active + legacy) ──────────────────────────────────
    "decision-record": {
        "summary": "Record a decision with supports, effects, and rejected alternatives (decisions_v2 path).",
        "required": [
            ("title", "one-sentence decision title (atom, 8-240 chars)"),
            ("kind", "substantive | schema_migration | calibration | disposition | procedural"),
            ("outcome_type", "adopt | reject | defer | supersede | ratify"),
            (
                "target_kind",
                "process_rule | spec_version | migration | issue | review_rule | engine_version | open_question",
            ),
            ("target_key", "short identifier (2-120 chars)"),
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            (
                "supports",
                "list of {basis, claim, cite?}; basis ∈ constraint | operator_directive | prior_decision | review_finding | deliberation | spec_clause | engine_feedback",
            ),
            (
                "effects",
                "list of {effect_kind, target_descriptor, target?}; effect_kind ∈ creates | modifies | supersedes | opens_issue | bumps_engine | closes_issue | adds_migration",
            ),
            (
                "alternatives",
                "list of {label, option, rejections[{basis, reason, cite?}]}; label format R-N.N",
            ),
        ],
        "example": (
            '{"title": "Adopt registry shape for submit-help.", '
            '"kind": "substantive", "outcome_type": "adopt", '
            '"target_kind": "process_rule", "target_key": "submit-help-shape", '
            '"supports": [{"basis": "engine_feedback", "claim": "EF named the gap.", "cite": "EF-S161-1"}], '
            '"alternatives": [{"label": "R-1.1", "option": "Per-handler docstring scrape.", '
            '"rejections": [{"basis": "inferior_tradeoff", "reason": "Couples docs to source format."}]}]}'
        ),
        "spec_ref": "prompts/development.md §5",
    },
    "decision": {
        "summary": "Legacy decision handler (pre-engine-v20); use decision-record for new work.",
        "required": [
            ("session_no", "open session_no"),
            ("kind", "decision kind"),
            ("title", "decision title"),
            ("body_md", "decision body markdown"),
        ],
        "optional": [
            ("alternatives", "list of {label, summary, rejection_reason_md}"),
            ("refs", "extra refs to record"),
        ],
        "example": '{"session_no": 87, "kind": "substantive", "title": "Legacy title", "body_md": "Body text."}',
        "spec_ref": "(legacy) read-only path; use decision-record",
    },
    # ── Deliberation lifecycle ───────────────────────────────────────
    "deliberation-open": {
        "summary": "Open a deliberation under the current session; returns deliberation_id.",
        "required": [
            ("session_no", "open session_no"),
            ("topic", "short topic phrase"),
        ],
        "optional": [],
        "example": '{"session_no": 87, "topic": "Whether to adopt registry shape."}',
        "spec_ref": "prompts/development.md §4",
    },
    "perspective": {
        "summary": "Submit a perspective (legacy intake; capture subagent decomposes into position + claims).",
        "required": [
            ("deliberation_id", "deliberation_id from deliberation-open"),
            ("label", "P-1, P-2, ..."),
            ("family", "anthropic | openai | google | other-llm | human"),
            ("body_md", "perspective body markdown (preserved as legacy intake)"),
        ],
        "optional": [
            ("refs", "extra refs to record alongside body_md auto-detected aliases"),
        ],
        "example": '{"deliberation_id": 24, "label": "P-1", "family": "anthropic", "body_md": "**Position.** ..."}',
        "spec_ref": "prompts/development.md §4",
    },
    "deliberation-seal": {
        "summary": "Seal an open deliberation; refused if already sealed.",
        "required": [
            ("deliberation_id", "deliberation_id from deliberation-open"),
        ],
        "optional": [
            ("synthesis_md", "synthesis markdown text preserving dissent"),
        ],
        "example": '{"deliberation_id": 24, "synthesis_md": "Synthesis preserves M-1 dissent."}',
        "spec_ref": "prompts/development.md §4",
    },
    "deliberation-counterfactual": {
        "summary": "Author one counterfactual under an open deliberation (DV-S180-1, engine-v50, T-36).",
        "required": [
            ("deliberation_id", "open deliberation_id (T-13 refuses if sealed)"),
            ("position", "the position no perspective took (8-240 char atom)"),
            ("why", "why the position would change synthesis if adopted (8-240 char atom)"),
            ("disposition", "addressed-in-synthesis | deferred-to-FR | nilled-by-exclusion"),
        ],
        "optional": [
            ("disposition_note", "synthesis_md anchor (addressed-in-synthesis) or FR alias (deferred-to-FR); 8-240 char"),
            ("exclusion_kind", "preserved-as-divergence | barred-by-constraint | micro-decision | out-of-scope; required when disposition=nilled-by-exclusion"),
            ("nil_attestation", "0 or 1; 1 encodes 'seal-grade: 0' cheap-exit (requires seq=1, disposition=nilled-by-exclusion, exclusion_kind set)"),
        ],
        "example": '{"deliberation_id": 29, "position": "Hybrid clause: ship typed primitive AND retain prose-prefix as recommended-optional.", "why": "Foreclosed by Q1 framing graduate-or-subtract.", "disposition": "nilled-by-exclusion", "exclusion_kind": "out-of-scope"}',
        "spec_ref": "prompts/development.md §4",
    },
    "synthesis-point": {
        "summary": "Add a synthesis point to a sealed deliberation (convergence, divergence, minority).",
        "required": [
            ("deliberation_id", "sealed deliberation_id"),
            ("kind", "convergence | divergence | minority"),
            ("label", "C-1, D-2, M-1, ..."),
            ("summary", "one-line summary"),
        ],
        "optional": [
            ("source_perspectives", "list of perspective_ids contributing to the point"),
            ("body_md", "longer-form body (refs auto-recorded)"),
        ],
        "example": '{"deliberation_id": 24, "kind": "convergence", "label": "C-1", "summary": "Cross-family convergence on PILOT-FIRST.", "source_perspectives": [1, 2]}',
        "spec_ref": "prompts/development.md §4",
    },
    "perspective-position": {
        "summary": "Capture a perspective's distilled Position paragraph as one atom.",
        "required": [
            ("perspective_id", "perspective_id from submit perspective"),
            ("position", "one-paragraph distilled position (atom)"),
        ],
        "optional": [],
        "example": '{"perspective_id": 1, "position": "Adopt registry shape; reject docstring scrape."}',
        "spec_ref": "prompts/development.md §4",
    },
    "perspective-claim": {
        "summary": "Capture one bullet under a labeled section of a perspective body.",
        "required": [
            ("perspective_id", "perspective_id"),
            ("claim", "one-line claim atom"),
            (
                "section_kind",
                "position | schema_sketch | cli_surface | migration_path | what_not | open_question | risk | what_lost",
            ),
        ],
        "optional": [
            ("cite", "object alias to record as cited reference"),
        ],
        "example": '{"perspective_id": 1, "claim": "Registry should be a single dict.", "section_kind": "schema_sketch", "cite": "OI-S090-5"}',
        "spec_ref": "prompts/development.md §4",
    },
    # ── Spec authoring ───────────────────────────────────────────────
    "spec-version": {
        "summary": "Bump or seed a spec version; flips prior active to superseded in the same write_tx.",
        "required": [
            ("session_no", "open session_no"),
            ("spec_id", "spec id (e.g. methodology, prompt-development)"),
            ("version", "integer version number"),
            ("body_path", "path under workspace_root (e.g. specifications/methodology.md)"),
        ],
        "any_of": [
            {
                "fields": ["body_md", "body_sha256"],
                "description": "supply `body_md` (handler computes sha + writes file) OR pre-write the file and supply `body_sha256` (legacy two-step path verifies file on disk)",
            }
        ],
        "optional": [
            ("supersedes", "prior alias (SPEC-<spec>-v<n>); required for any non-initial version"),
            ("supersedes_reason_md", "one-sentence reason recorded on the supersedes ref"),
        ],
        "example": (
            '{"session_no": 87, "spec_id": "methodology", "version": 13, '
            '"body_path": "specifications/methodology.md", "body_md": "# Methodology v13\\n\\n...", '
            '"supersedes": "SPEC-methodology-v12", "supersedes_reason_md": "Add §Y."}'
        ),
        "spec_ref": "prompts/development.md §6",
    },
    "spec-section": {
        "summary": "Add a section row under a spec_version.",
        "required": [
            ("spec_version_id", "parent spec_version_id"),
            ("ord", "section order (integer)"),
            ("heading", "section heading atom"),
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            ("intent", "section intent atom"),
        ],
        "example": '{"spec_version_id": 42, "ord": 1, "heading": "Section heading"}',
        "spec_ref": "prompts/development.md §6",
    },
    "spec-clause": {
        "summary": "Add a clause row under a spec_section.",
        "required": [
            ("spec_section_id", "parent spec_section_id"),
            ("ord", "clause order (integer)"),
            ("clause_type", "clause type (per spec_clauses CHECK enum)"),
            ("normative_level", "normative level (per spec_clauses CHECK enum)"),
            ("clause", "clause text atom"),
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            ("source_decision_alias", "DV-S<wno>-<n> alias of the decision sourcing this clause"),
        ],
        "example": '{"spec_section_id": 99, "ord": 1, "clause_type": "rule", "normative_level": "MUST", "clause": "Clause text atom."}',
        "spec_ref": "prompts/development.md §6",
    },
    "legacy-import": {
        "summary": "Import a legacy decomposed atom (migration support; rare in modern sessions).",
        "required": [
            ("text", "atom text"),
            ("old_table", "originating table name"),
            ("old_pk", "originating primary key value"),
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            ("decomposition_status", "default: unratified"),
        ],
        "example": '{"text": "Imported atom text.", "old_table": "old_decisions", "old_pk": "123"}',
        "spec_ref": "(migration support)",
    },
    # ── Review loop (T-30) ───────────────────────────────────────────
    "review-finding": {
        "summary": "Record a reviewer-surfaced finding (T-20 refuses session-close on open medium+ findings).",
        "required": [
            ("iteration", "review iteration (1-4)"),
            ("severity", "critical | high | medium | low"),
            ("finding", "one-sentence problem statement (atom)"),
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            ("target", "object alias of the affected artefact"),
            ("disposition", "open | fixed | adjudicated (default open)"),
            ("disposition_text", "short disposition reason"),
        ],
        "example": '{"iteration": 1, "severity": "medium", "finding": "Schema example will not parse as JSON.", "target": "DV-S166-1"}',
        "spec_ref": "prompts/development.md §7",
    },
    "review-pass": {
        "summary": "Record a terminal review-pass row (one per iteration; outcome ∈ clean | findings | nonconverged).",
        "required": [
            ("iteration", "review iteration (1-4)"),
            ("outcome", "clean | findings | nonconverged"),
            ("head_sha", "git HEAD sha at the moment the reviewer ran (7-64 hex chars)"),
            ("summary", "one-line summary atom"),
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            (
                "halt_issue_alias",
                "OI-... tracking unresolved findings; required when outcome=nonconverged",
            ),
        ],
        "example": '{"iteration": 1, "outcome": "clean", "head_sha": "abc1234", "summary": "Reviewer found no issues."}',
        "spec_ref": "prompts/development.md §7",
    },
    "finding-disposition": {
        "summary": "Update a review-finding's disposition (open → fixed | adjudicated).",
        "required": [
            ("review_finding_id", "review_finding_id from submit review-finding"),
            ("disposition", "fixed | adjudicated"),
            ("disposition_text", "substantive reason or commit reference"),
        ],
        "optional": [],
        "example": '{"review_finding_id": 187, "disposition": "fixed", "disposition_text": "Replaced placeholder values with valid JSON literals."}',
        "spec_ref": "prompts/development.md §7",
    },
    # ── Issues ───────────────────────────────────────────────────────
    "issue": {
        "summary": "Open a new issue (status='open'; transitions go through issue-disposition).",
        "required": [
            ("alias", "issue alias (e.g. OI-S166-1)"),
            ("title", "one-line title atom"),
            ("priority", "HIGH | MEDIUM | LOW"),
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            ("summary", "optional summary atom"),
            ("body", "optional longer body"),
            ("surfaced_session_no", "session that surfaced the issue (defaults to current)"),
        ],
        "example": '{"alias": "OI-S166-1", "title": "Issue title atom.", "priority": "MEDIUM"}',
        "spec_ref": "prompts/development.md §5 (effects.opens_issue resolves to existing issue)",
    },
    "issue-disposition": {
        "summary": "Transition an issue's status (open ↔ in_progress | blocked | resolved | superseded).",
        "required": [
            ("to_status", "target status"),
            ("reason", "transition reason atom"),
        ],
        "any_of": [
            {
                "fields": ["issue_id", "alias"],
                "description": "identify the issue by integer `issue_id` OR string `alias` (e.g. OI-016)",
            }
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
        ],
        "example": '{"alias": "OI-S166-1", "to_status": "resolved", "reason": "Addressed by DV-S166-1."}',
        "spec_ref": "(closes_issue effect on decision-record dispatches this in-band)",
    },
    "issue-link": {
        "summary": "Link two issues with a typed relation.",
        "required": [
            ("relation", "link relation"),
        ],
        "any_of": [
            {
                "fields": ["source_issue_id", "source_alias"],
                "description": "identify the source issue by integer `source_issue_id` OR alias `source_alias`",
            },
            {
                "fields": ["target_issue_id", "target_alias"],
                "description": "identify the target issue by integer `target_issue_id` OR alias `target_alias`",
            },
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            ("reason", "link reason atom"),
        ],
        "example": '{"source_alias": "OI-S166-1", "target_alias": "OI-S151-3", "relation": "supersedes"}',
        "spec_ref": "issues §3 (links)",
    },
    "issue-note": {
        "summary": "Append a note to an issue.",
        "required": [
            ("note", "note text atom"),
        ],
        "any_of": [
            {
                "fields": ["issue_id", "alias"],
                "description": "identify the issue by integer `issue_id` OR string `alias`",
            }
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
        ],
        "example": '{"alias": "OI-S166-1", "note": "Note text atom."}',
        "spec_ref": "issues §3 (notes)",
    },
    "issue-work-item": {
        "summary": "Link an issue to a work_item with a typed relation.",
        "required": [
            ("work_item_id", "existing work_item_id"),
        ],
        "any_of": [
            {
                "fields": ["issue_id", "alias"],
                "description": "identify the issue by integer `issue_id` OR string `alias`",
            }
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            ("relation", "default: resolves"),
        ],
        "example": '{"alias": "OI-S166-1", "work_item_id": 42, "relation": "resolves"}',
        "spec_ref": "issues §3 (work-item linkage)",
    },
    # ── Engine-feedback + forward-references ─────────────────────────
    "engine-feedback": {
        "summary": "Record an engine-feedback row (use `bin/selvedge feedback` wrapper outside an open session).",
        "required": [
            ("flag", "observation | reframe | calibration | blocker"),
            ("body_md", "feedback body (free markdown; refs auto-recorded)"),
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            ("disposition", "optional disposition text (usually NULL at insert)"),
        ],
        "example": '{"flag": "observation", "body_md": "**S166 friction:** placeholder examples did not parse as JSON."}',
        "spec_ref": "prompts/development.md §8.5",
    },
    "engine-feedback-disposition": {
        "summary": "Update engine_feedback.disposition for a previously-submitted EF.",
        "required": [
            ("disposition", "disposition text"),
        ],
        "any_of": [
            {
                "fields": ["feedback_id", "alias"],
                "description": "identify the EF by integer `feedback_id` OR alias `alias` (e.g. EF-S166-1)",
            }
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
        ],
        "example": '{"alias": "EF-S166-1", "disposition": "addressed-by-DV-S166-1 (review-loop fixes)"}',
        "spec_ref": "prompts/development.md §8.5",
    },
    "forward-reference-disposition": {
        "summary": "Mark a prior session's next_session_should item as resolved.",
        "required": [
            ("target_session", "workspace_session_no of the close-record holding the FR"),
            ("seq", "close_state_items.seq of the FR"),
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            ("note", "disposition note atom"),
        ],
        "example": '{"target_session": 161, "seq": 15, "note": "addressed by DV-S166-1"}',
        "spec_ref": "prompts/development.md §8.5",
    },
    # ── Reference harness (workspace-experimental) ───────────────────
    "harness-open": {
        "summary": "Open a new reference_harness (status=open).",
        "required": [
            ("arc_slug", "arc slug naming the parent arc"),
            ("stage_n", "stage number (integer)"),
            ("expiry_sessions", "session-count window before expiry"),
            ("absence_declaration", "absence-of-domain declaration atom"),
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            ("alias", "override default alias RH-S<wno>-<n>"),
        ],
        "example": '{"arc_slug": "disaster-response", "stage_n": 1, "expiry_sessions": 5, "absence_declaration": "No domain expert present this session."}',
        "spec_ref": "(workspace-experimental; not kernel-promoted)",
    },
    "harness-target": {
        "summary": "Add a target_artifact entry to an open harness.",
        "required": [
            ("descriptor", "target descriptor atom"),
        ],
        "any_of": [
            {
                "fields": ["harness_id", "alias"],
                "description": "identify the harness by integer `harness_id` OR alias `alias`",
            }
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            ("artifact_path", "filesystem path to the target artifact"),
            ("artifact_sha256", "sha256 of artifact_path"),
        ],
        "example": '{"alias": "RH-S166-1", "descriptor": "Target descriptor atom.", "artifact_path": "specifications/methodology.md"}',
        "spec_ref": "(harness)",
    },
    "harness-claim": {
        "summary": "Add a claim_set entry to a harness.",
        "required": [
            ("claim", "claim atom"),
        ],
        "any_of": [
            {
                "fields": ["harness_id", "alias"],
                "description": "identify the harness by integer `harness_id` OR alias `alias`",
            }
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            ("world_constraint", "real-world constraint atom"),
            ("surrogate_frame", "surrogate-frame atom"),
            ("load_bearing", "boolean (default false)"),
        ],
        "example": '{"alias": "RH-S166-1", "claim": "Claim atom text.", "load_bearing": true}',
        "spec_ref": "(harness)",
    },
    "harness-stress": {
        "summary": "Add a stress_protocol entry to a harness.",
        "required": [
            ("protocol_kind", "stress protocol kind"),
            ("description", "stress description atom"),
        ],
        "any_of": [
            {
                "fields": ["harness_id", "alias"],
                "description": "identify the harness by integer `harness_id` OR alias `alias`",
            }
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
        ],
        "example": '{"alias": "RH-S166-1", "protocol_kind": "adversarial", "description": "Stress description atom."}',
        "spec_ref": "(harness)",
    },
    "harness-result": {
        "summary": "Record a claim-level harness result.",
        "required": [
            ("claim_id", "reference_harness_claims.claim_id"),
            ("result", "survived | strained | broken | untestable | deferred"),
            ("evidence", "evidence atom"),
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
        ],
        "example": '{"claim_id": 7, "result": "survived", "evidence": "Evidence atom from stress run."}',
        "spec_ref": "(harness; CHECK enum excludes domain_validated by design)",
    },
    "harness-dissent": {
        "summary": "Preserve a minority surrogate objection to a harness claim.",
        "required": [
            ("dissent", "dissent atom"),
        ],
        "any_of": [
            {
                "fields": ["harness_id", "alias"],
                "description": "identify the harness by integer `harness_id` OR alias `alias`",
            }
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            ("source_claim_id", "claim_id this dissent objects to (must belong to the same harness)"),
            ("conflict_kind", "typed-observation atom: free-text conflict-shape label (workspace-experimental, no enum); kernel methodology names no canonical values per DV-S152-1"),
        ],
        "example": '{"alias": "RH-S166-1", "dissent": "Dissent atom.", "source_claim_id": 7}',
        "spec_ref": "(harness; conflict_kind nullable opt-in atom per DV-S152-1)",
    },
    "harness-trigger": {
        "summary": "Register a falsification_trigger on a harness.",
        "required": [
            ("trigger", "trigger condition atom"),
        ],
        "any_of": [
            {
                "fields": ["harness_id", "alias"],
                "description": "identify the harness by integer `harness_id` OR alias `alias`",
            }
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
        ],
        "example": '{"alias": "RH-S166-1", "trigger": "Trigger condition atom."}',
        "spec_ref": "(harness)",
    },
    "harness-trigger-fire": {
        "summary": "Fire a falsification trigger on a sealed harness; cascades parent to status='reopened'.",
        "required": [
            ("trigger_id", "reference_harness_triggers.trigger_id"),
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
        ],
        "example": '{"trigger_id": 12}',
        "spec_ref": "(harness; one-shot per trigger row)",
    },
    "harness-assumption": {
        "summary": "Track a harness-level assumption with origin and status.",
        "required": [
            ("assumption", "assumption atom"),
        ],
        "any_of": [
            {
                "fields": ["harness_id", "alias"],
                "description": "identify the harness by integer `harness_id` OR alias `alias`",
            }
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            ("origin_session_no", "session that surfaced the assumption (defaults to current)"),
            ("status", "active | invalidated | deferred (default active)"),
        ],
        "example": '{"alias": "RH-S166-1", "assumption": "Assumption atom text.", "status": "active"}',
        "spec_ref": "(harness)",
    },
    "harness-seal": {
        "summary": "Transition a harness from open to sealed.",
        "required": [],
        "any_of": [
            {
                "fields": ["harness_id", "alias"],
                "description": "identify the harness by integer `harness_id` OR alias `alias`",
            }
        ],
        "optional": [
            _SESSION_NO_OPTIONAL,
            ("closure_kind", "typed-observation atom: free-text closure-shape label (workspace-experimental, no enum); kernel methodology names no canonical values per DV-S152-1"),
        ],
        "example": '{"alias": "RH-S166-1"}',
        "spec_ref": "(harness; closure_kind nullable opt-in atom per DV-S152-1)",
    },
}
