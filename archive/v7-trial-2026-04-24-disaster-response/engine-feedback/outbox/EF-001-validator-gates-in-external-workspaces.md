---
feedback_id: EF-001-validator-gates-in-external-workspaces
source_workspace_id: selvedge-disaster-response
source_session: 001
created_at: 2026-04-24T15:00:00+10:00
reported_by: application-agent
target: engine
target_files:
  - tools/validate.sh
  - specifications/validation-approach.md
  - specifications/engine-manifest.md
severity: friction
status: outbound
---

# EF-001 — validator session-number gates do not fire in early external-workspace sessions

## Observation

`tools/validate.sh` at engine-v7 carries several session-number-gated
checks whose adoption-session constants are historical to the
self-development source workspace's chronology:

- `TRIGGERS_MET_ADOPTION_SESSION=6` gates checks 14 and 15
  (`triggers_met:` coverage + non-Claude participation coverage).
- `CRITERION4_ARTICULATION_SESSION=21` gates checks 16, 17, 19
  (OI-004 criterion-4 schema fields).
- `READ_CONTRACT_ADOPTION_SESSION=22` gates check 20 (default-read
  per-file budget).
- `AGGREGATE_BUDGET_ADOPTION_SESSION=28` gates check 20 aggregate
  enforcement + check 22 rotated-close citation form.
- `MODE_MD_ADOPTION_SESSION=36` gates check 23 (MODE.md presence)
  with a bootstrap-state override that does fire for external
  workspaces.

In an external-problem application workspace initialised at engine-
v7 (this workspace), Session 001 numbers at 1. The four
session-number gates above evaluate to "pre-adoption" for any
session with number < adoption-constant. In this workspace, **all
sessions 1 through 5 will be pre-adoption for checks 14/15, all
sessions 1 through 20 for checks 16/17/19, all sessions 1 through
21 for check 20, all sessions 1 through 27 for check 20 aggregate
and check 22 rotated-close form**. The validator reports no output
for these checks in those sessions; discipline held in Session 001
only by independent orchestrator attention.

The specific failure mode this session observed: Session 001's
`02-decisions.md` contains ten decisions, all declaring
`**Triggers met:** [d016_3]` or `[d016_3, d016_4]` per MAD v4
§Trigger-Coverage Annotation Schema. The validator produced no
output under `[14] Multi-agent trigger coverage (triggers_met)` or
`[15] Non-Claude trigger coverage (triggers_met)` because the gate
filtered Session 001 as pre-adoption. A session that had simply
forgotten the `**Triggers met:**` line would have produced the same
silent pass.

The Outsider manifest carries the v4 fields
`participant_organisation: openai`, `claude_output_in_training:
unknown`, `training_lineage_evidence_pointer: unknown-but-asserted`,
`independence_basis: organization-distinct` — the validator did not
check any of these because check 16/17/19 is gated ≥ 021.

## Why it matters

The session-number gates were calibrated to the self-development
source workspace's chronology to preserve immutability of pre-
adoption sessions per D-017 and per the stated rationale in
`validation-approach.md` v5 §Gating Conventions. That rationale is
correct for the self-development workspace: pre-adoption sessions
there exist and cannot be retroactively rewritten.

It is **not correct for an external workspace bootstrapped at
engine-v7**. There are no pre-adoption sessions in such a workspace
— Session 001 is the first session and it is, by the bootstrap
contract (`engine-manifest.md` §6), executing under the current
engine's discipline. The same-numbered session in an external
workspace and in the self-development workspace are not
equivalent: self-dev Session 001 predates the rules being checked;
external-workspace Session 001 is subject to them from the start.

Concretely, this means:

- External workspaces get no validator enforcement of
  `triggers_met:` coverage for their first 5 sessions.
- External workspaces get no validator enforcement of OI-004
  criterion-4 schema for their first 20 sessions.
- External workspaces get no default-read per-file budget enforcement
  for their first 21 sessions.
- External workspaces get no aggregate-budget or close-rotation
  citation enforcement for their first 27 sessions.

Any external-application session that drops these disciplines
silently passes Tier 1 validation. The discipline would hold only
by operator/orchestrator attention, not by tooling.

## Evidence

- `provenance/001-session/03-close.md` §3 notes this session passed
  Tier 1 (42 passed / 0 failed / 0 warnings) but observes that
  checks 14/15/16/17/19/20 were silent under the session-number
  gates.
- `provenance/001-session/02-decisions.md` contains compliant
  `**Triggers met:**` annotations on every decision; the validator
  produced no output reflecting this.
- `provenance/001-session/manifests/outsider.manifest.yaml` contains
  compliant v4 criterion-4 fields; the validator produced no output
  reflecting this.
- `tools/validate.sh` lines 11, 17, 35, 36, 1040 carry the four
  relevant session-number constants.

## Suggested change

Several directions are available; the triage session should
deliberate among them. Not ranking here — each has trade-offs.

**Direction A — dual gating on session-number OR MODE.** Gate each
affected check by `(session_num >= adoption_session) OR (mode ==
"external-problem")`. In external workspaces, the check fires from
Session 001 because the workspace itself was created under the
engine version that already includes the rule. In the self-
development workspace, the check fires from its adoption session as
today. Trade-off: requires reading `MODE.md` in `validate.sh`;
requires a convention for external-workspace engine-version
checkpointing (e.g., if a workspace was bootstrapped at engine-v5,
checks added at engine-v6 should still gate).

**Direction B — engine-version gating instead of session-number
gating.** Record `engine_version_at_creation` in `MODE.md` (already
present at engine-v7). Each check gates on "is this check part of
the engine version this workspace was initialised under, or a later
version the workspace has adopted?" Trade-off: requires per-check
"introduced-at-engine-version" metadata; requires a workspace-level
engine-version-adoption log if workspaces can roll forward.

**Direction C — explicit pre-adoption-session override.** Change the
gate to `session_num >= max(adoption_session, workspace_first_session)`.
The self-development workspace's `workspace_first_session = 1`
keeps current behaviour; an external workspace's
`workspace_first_session = 1` but is co-paired with an
`engine_version_at_creation` that is beyond all adoption-session
constants, so the gate should not apply. Trade-off: essentially
reduces to Direction B.

**Direction D — document-only remediation.** Document that external-
workspace orchestrators must independently apply the discipline; do
not change the validator. Trade-off: trades engine-level guarantee
for operator discipline; inconsistent with the stated purpose of
Tier 1 being machine-verifiable.

A combined D + (A or B) may be the right near-term: update
`prompts/application.md` to warn external orchestrators about the
gate, while opening an OI or adopting Direction A/B as the engineered
remediation.

## Application-scope disposition

Session 001 of `selvedge-disaster-response` workspace held the
discipline independently: wrote `**Triggers met:**` annotations on
every decision; populated criterion-4 fields in the Outsider
manifest; checked per-file sizes manually (the two v1 artefacts in
`applications/` are out of default-read scope; the two new default-
read candidates — the application brief and Session 001's `03-
close.md` — are both under any plausible ceiling). No further
application-scope action taken; this feedback is for engine
improvement.

The finding was surfaced at Tier 1 run time (not by Tier 2 review),
which is itself informative: the silence was visible because
checks 14/15/16/17/19/20 emitted only their section headers with no
item output. A future check-output convention that emits
`(out-of-scope by session-number gate)` explicitly (as check 18 and
check 20 already do) would at least make the silence legible.
