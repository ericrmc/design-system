# Engine-feedback outbox index — selvedge-disaster-response

Feedback records written in this workspace (external-problem mode)
for operator-mediated transport back to the self-development source
workspace's `engine-feedback/inbox/` per `specifications/workspace-
structure.md` v5 §engine-feedback.

| Feedback ID | Created | Severity | Target | Status | Summary |
|---|---|---|---|---|---|
| `EF-001-validator-gates-in-external-workspaces.md` | 2026-04-24 | friction | engine | outbound | `tools/validate.sh` session-number gates calibrated to self-development chronology do not fire in external-workspace early sessions; checks 14/15/16/17/19/20 silent for Session 001 despite compliant artefacts. Four directions for remediation proposed. Reinforced by three consecutive sessions (001, 002, 003) of this workspace all hitting the same out-of-scope-gating. |
| `EF-003-claude-subagent-verbatim-capture-via-agent-tool.md` | 2026-04-24 | friction | engine | outbound | Agent-tool transport appends harness metadata (`agentId:` + `<usage>` blocks) to every Claude-subagent return; committing the full return verbatim pollutes the raw perspective file, but stripping it and claiming `output_edited_after_submission: false` is borderline because the committed file is byte-identical to model content but NOT byte-identical to the full Agent-tool return. MAD v4 §Mechanism is silent on transport-metadata handling for the Agent-tool pathway. Three remediation directions proposed (spec clarification / schema extension / transport-log sibling file). |
| `EF-003-archive-citation-convention-for-closed-session-files.md` | 2026-04-24 | observation | engine | outbound | `read-contract.md` v4 §6 archive-citation convention is archive-pack-directory-scoped; closed-session-file citations (the dominant archive-surface citation form in external-problem workspaces that have no archive-packs yet) are silent from spec and out-of-scope for validator check 22. Sessions 001/002/003 of this workspace all note the gap as honest-limits. Three remediation directions proposed (spec sub-section / check 22 extension / citation taxonomy refactor). |
