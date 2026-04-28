# Engine-feedback outbox

Per `specifications/workspace-structure.md` v5 §engine-feedback, this
directory is the **outbox** for methodology-level feedback observed during this
external application's execution. Non-engine operator-managed content; not
copied when the engine is cloned.

## When to write a feedback file

During any session in this workspace, if an engine-level concern surfaces — an
unclear specification, a kernel §7 activity ambiguity, a `multi-agent-deliberation.md`
field that is awkward in this domain's practice, a reference-validation exercise
gap, a dispatcher edge case, or any equivalent methodology-level friction —
record the observation as a feedback file here.

Feedback files are **out-of-scope for this application's own deliberation**
(whose work is the domain artefact) but **in-scope for engine/methodology
improvement** by the self-development source workspace's triage process.

## File naming

`EF-<session-number>-<short-slug>.md` — for example, `EF-002-dispatch-edge-case.md`.

## Frontmatter schema (copy into each feedback file)

```yaml
---
feedback_id: EF-NNN-<slug>
source_workspace_id: selvedge-disaster-response
source_session: NNN
created_at: <ISO-8601 timestamp>
reported_by: operator | application-agent
target: engine | methodology | other
target_files: [<paths-to-affected-engine-files>]
severity: blocker | friction | observation
status: outbound
---
```

## Body sections

`## Observation` — what happened in this application.
`## Why It Matters` — what engine/methodology behaviour was implicated.
`## Suggested Change` — optional; concrete change proposal if the feedback
                       author has one.
`## Evidence` — links, copied snippets, or file-and-line references.
`## Application-Scope Disposition` — why this application did or did not
                                    resolve locally.

## Return flow

Between sessions, the operator copies each completed feedback file verbatim
from this outbox to the self-development source workspace at:

    <source-workspace>/engine-feedback/inbox/EF-<same-name>.md

The file in this outbox is preserved as the originating witness; the inbox copy
in the source workspace is the triage target. The engine does not specify
automated cross-workspace transport — the operator is the transport per
workspace-structure.md v5 §engine-feedback return semantics.

The self-development workspace's `engine-feedback/INDEX.md` tracks intake /
triage / resolution status across all mediated feedback records.
