---
feedback_id: EF-003-claude-subagent-verbatim-capture-via-agent-tool
source_workspace_id: selvedge-disaster-response
source_session: 003
created_at: 2026-04-24
reported_by: application-agent
target: engine
target_files:
  - specifications/multi-agent-deliberation.md
  - specifications/validation-approach.md
  - tools/validate.sh
severity: friction
status: outbound
---

# EF-003 — Claude-subagent verbatim-capture via Agent tool

## Observation

The Selvedge engine's multi-agent-deliberation specification (MAD v4)
requires raw perspective files to be committed **verbatim**. MAD v4
§Non-Claude Participation Mechanism specifies transport-guarantee
language in detail for non-Claude participants ("the **record**
(committed brief, verbatim response, attributable participant), not
the **generation**"). The Layer 2 manifest schema includes
`output_edited_after_submission: true | false` as a per-participant
field.

In practice, when Claude-subagent perspectives are launched via the
Claude Code `Agent` tool (the implementation mechanism MAD v4
§Mechanism names: *"The Claude-subagent implementation realises
this via parallel subagents launched through Claude Code's Agent
tool, each in an isolated context"*), the returned agent response
is not byte-identical to the model's content. Each Agent tool
return includes trailing tool-harness metadata of the form:

```
agentId: <hex-id> (use SendMessage with to: '<hex-id>' to continue this agent)
<usage>total_tokens: N
tool_uses: N
duration_ms: N</usage>
```

This metadata is transport-layer, not model-content. Committing it
verbatim into the raw perspective file would pollute the file with
non-content. Stripping it (treating it as transport-layer noise)
produces a file that is byte-identical to the model's content but
NOT byte-identical to the full Agent-tool return.

Session 003 in this workspace (Application 001, disaster-response)
encountered this three times (perspectives 01A, 01B, 01C) and
handled it by stripping the trailing metadata and disclosing the
strip in each manifest's `transport_notes` field:

> "Trailing agentId/usage metadata stripped from committed raw
> file (markdown-formatting-only edit permitted per MAD v4 §Stance
> Briefs brief-immutability clause; substantive content
> unchanged)."

Each manifest's `output_edited_after_submission: false` claim is
borderline: the committed file is byte-identical to model content
but NOT byte-identical to the full Agent-tool return. The "output"
token in the field name is semantically ambiguous between "model
content" and "Agent-tool return including transport metadata".

## Why it matters

Three concerns, each at increasing severity:

1. **Ambiguity in the verbatim guarantee for Claude-subagent
   transport.** MAD v4 §Non-Claude Participation Mechanism
   transport-guarantee language is scoped to non-Claude
   participants. The analogous guarantee for Claude-subagent
   transport via the Agent tool is implicit in §Mechanism but not
   operationalised. An operator faced with Agent-tool output must
   choose between (a) committing the full return (including
   non-content metadata) or (b) stripping the metadata and
   declaring the strip. MAD v4 doesn't prescribe either.

2. **`output_edited_after_submission` field semantic
   ambiguity.** As noted above. A future validator check (check
   13 is cross-model-claim honesty, not edit-detection; no
   current check inspects `output_edited_after_submission`) that
   relied on this field would face the definitional question. The
   honest answer at Session 003 is "content unchanged; transport
   metadata stripped" — a value this field cannot carry as-
   currently-specified.

3. **Per-session operational friction.** Every deliberation with
   Claude-subagent perspectives (which is every substantive
   deliberation in this workspace) requires the operator to
   manually strip trailing Agent-tool metadata before committing
   the raw perspective file. This is reliably-done-by-attention
   but not automated; a tired operator could commit the metadata
   accidentally. Conversely, a bad-faith operator could claim
   metadata-stripping as cover for actual content edits (the
   edits would be visible to an adversarial reviewer but not to
   `validate.sh`).

The friction compounds across sessions. Sessions 001 and 002 of
this workspace handled this silently (the committed raw files also
lack the trailing metadata; the operator made the same strip
without a `transport_notes` disclosure because the pattern wasn't
yet named). Session 003 elevated the disclosure to the manifest.
An external application's operator reading the MAD v4 spec fresh
would not know to make the strip or to disclose it.

## Suggested change

Three candidate directions, each operable independently:

**Direction 1 (narrow; lowest engine-change cost).** Add a sentence
to MAD v4 §Mechanism (after the "parallel subagents launched
through Claude Code's Agent tool" sentence) acknowledging that
Agent-tool transport appends harness metadata to the returned
content, and specifying that:

- "Output" for verbatim-preservation purposes means model-content
  only.
- Transport metadata (trailing `agentId` / `<usage>` blocks from
  the Agent tool, or equivalent from other transports) is
  transport-layer and MAY be stripped.
- The strip MUST be disclosed in the participant's Layer 2
  manifest `transport_notes` field.
- `output_edited_after_submission: false` remains valid after a
  disclosed transport-metadata strip.

**Direction 2 (medium; operational discipline).** Extend the Layer
2 manifest schema with an explicit field:

```yaml
transport_metadata_stripped: true | false
transport_metadata_disposition: <short description or "n/a">
```

This field would be `true` by default for Agent-tool transport
(given current Claude Code behaviour); `false` for transports that
return byte-identical model content (e.g., `codex exec` post-
`tokens used` copy). The field disambiguates the existing
`output_edited_after_submission` from transport-metadata-handling.

**Direction 3 (broadest; transport-log convention).** Adopt a
convention that the full Agent-tool return is preserved verbatim
as a sibling file (e.g., `01<letter>-perspective-<role>.transport-
log`) while the `.md` file carries only model-content. This
preserves the full record per MAD v4 §Transport guarantee without
polluting the human-readable perspective file, and makes any
subsequent content-edit distinguishable from transport-metadata-
handling.

Any of the three directions would clarify the friction. Direction
1 is cheapest (one sentence); Direction 2 is schema-level with
corresponding `validate.sh` field-presence check; Direction 3 is
structural and has operator-workflow cost.

## Evidence

Session 003 in this workspace. See:

- `provenance/003-session/manifests/system-model-reviser.manifest.yaml`
  (`transport_notes` field disclosing the strip for 01A).
- `provenance/003-session/manifests/vulnerability-advocate.manifest.yaml`
  (same for 01B).
- `provenance/003-session/manifests/adversarial-skeptic.manifest.yaml`
  (same for 01C).
- `provenance/003-session/01A-perspective-system-model-reviser.md`
  (the committed file, with metadata stripped; compare to the
  Agent-tool return in the conversation transcript, which would
  have carried the trailing block).

Sessions 001 and 002 in this workspace followed the same strip
convention but did not disclose it in `transport_notes` (the
pattern wasn't yet named).

## Application-scope disposition

The application handled this locally via per-manifest disclosure.
The disposition does not block this application's work; a fresh
external application starting from MAD v4 without inherited
operator knowledge might commit the metadata silently or strip it
without disclosure, producing a less-auditable provenance record
than the engine otherwise supports.

This feedback is written in outbox role per `specifications/
workspace-structure.md` v5 §engine-feedback and is pending
operator-mediated transport to the self-development source
workspace's `engine-feedback/inbox/` for triage.
