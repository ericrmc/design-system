---
title: Validation Approach (historical v2)
version: 2
status: superseded
superseded-by: validation-approach.md (v3)
created: 2026-04-17
last-updated: 2026-04-18
updated-by-session: 005
supersedes: validation-approach-v1.md
---

# Validation Approach

## Purpose

This specification defines how the methodology validates itself: what is checked, how checks are organized, and what the checks can and cannot assure. It serves the methodology's self-hosting principle — a methodology that cannot verify its own specifications cannot evolve reliably.

Version 2 adds three new Tier 1 checks (11, 12, 13) that enforce the D-024 heterogeneous-participant schema introduced by `multi-agent-deliberation.md` v2, and one new Tier 2 question paired with check 13's honest limit. It specifies gating, severity, and sequencing rules for the new checks. It supersedes v1 (`validation-approach-v1.md`).

## Specification

### Two-Tier Model

Validation has two tiers, reflecting the distinction between properties that can be checked mechanically and those that require judgment.

**Tier 1: Structural Checks** are automated checks run by `tools/validate.sh`. They verify that the workspace's files conform to the formats and conventions defined in other specifications. Structural checks are necessary but not sufficient for methodology health — a workspace can pass all structural checks while its specifications are semantically wrong or its provenance is misleading.

**Tier 2: Guided Assessment** is a set of questions printed by the validation tool for the agent or human conducting the session to consider. These questions address properties that cannot be checked mechanically: semantic consistency, provenance usefulness, and whether the methodology is making genuine progress.

### Tier 1: Structural Checks

The following checks are automated:

| # | Check | Source Spec | Severity | Gate |
|---|-------|-------------|----------|------|
| 1 | Required top-level files exist (PROMPT.md, SESSION-LOG.md, open-issues.md) | workspace-structure | Fail | unconditional |
| 2 | Required directories exist (specifications/, provenance/) | workspace-structure | Fail | unconditional |
| 3 | Each specification has YAML frontmatter with required fields (title, version, status, created, last-updated, supersedes) | workspace-structure | Fail | unconditional |
| 4 | Each specification has three required section headings (Purpose, Specification, Validation) | workspace-structure | Fail | unconditional |
| 5 | Provenance directories follow NNN-title naming convention | workspace-structure | Fail | unconditional |
| 6 | Session log has an entry for each provenance directory | workspace-structure | Fail | unconditional |
| 7 | Each provenance directory contains at least one .md file | methodology-kernel | Fail | unconditional |
| 8 | Provenance files have YAML frontmatter with required fields (session, title, date, status) | workspace-structure | Fail | unconditional |
| 9 | Decision records include rejected alternatives sections | methodology-kernel | Warning | unconditional |
| 10 | No uncommitted changes to provenance files (basic immutability heuristic) | workspace-structure | Warning | unconditional |
| 11 | Multi-agent three-raw-output floor: ≥3 files matching `*-perspective-*.md` | multi-agent-deliberation (v2 Validation #3) | Fail | session has ≥1 `*-perspective-*.md` file |
| 12 | Heterogeneous-participant schema well-formedness: each `manifests/*.manifest.yaml` has all D-024 required fields as literal keys | multi-agent-deliberation (v2 Validation #8) | Fail | session has `manifests/` subdirectory |
| 13 | Cross-model-claim honesty: `cross_model: true` implies ≥1 manifest with `training_lineage_overlap_with_claude` other than `known-overlap` OR `participant_kind: human` | multi-agent-deliberation (v2 Validation #9) | Fail | session declares `cross_model: true` AND check 12 passed for that session |

Checks marked **Fail** cause the tool to exit with a non-zero code. Checks marked **Warning** are reported but do not cause failure.

### Gating Conventions (checks 11, 12, 13)

**Presence-gating.** Checks 11, 12, and 13 apply only to sessions whose provenance exhibits the relevant artefact. A session without any `*-perspective-*.md` files is not a multi-agent session and is out-of-scope for check 11. A session without a `manifests/` subdirectory has not adopted the D-024 schema and is out-of-scope for check 12 (and by extension, check 13). Out-of-scope sessions produce no output from the gated check — no warning, no failure.

**Consequence for prior sessions.** Sessions 001 (Genesis) and 002 (Self-Validation) are not multi-agent; they are out-of-scope for all three new checks. Session 003 and Session 004 are multi-agent (have perspective files) but did not produce a `manifests/` subdirectory; they are in-scope for check 11 and out-of-scope for checks 12 and 13. Session 005 and later sessions that adopt the full schema are in-scope for all three.

**Rationale for the gate granularity.** Gating at `manifests/` subdirectory presence — rather than at `participants.yaml` presence or at session-number — was chosen to (a) keep Session 004's bootstrap-exempt minimal `participants.yaml` naturally out-of-scope without requiring an inline exemption list, (b) avoid encoding a numeric session cutoff that must be maintained in the tool, and (c) produce the same outcome in practice as session-number gating (Session 005 is the first session to have a `manifests/` subdirectory). This decision is recorded in D-030 (Session 005) along with the genuine cross-model disagreement that preceded it.

### Sequencing (check 13 after check 12)

Check 13 depends on well-formed manifests. If check 12 fails for a given session, check 13 reports `BLOCKED: check 12 failed for this session; cannot evaluate check 13` for that session and does not itself fail or warn. This prevents double-reporting of a single underlying problem and keeps the tool honest about what it actually evaluated.

### Check 13's Honest Limit (mandatory inline documentation)

Check 13 enforces **consistency of self-report**, not **truthfulness of self-report**. This limit is mandatory content in three locations:

1. A comment block in `tools/validate.sh` directly above check 13's implementation.
2. Check 13's failure message (as an inline NOTE).
3. This specification (above).

The language to preserve verbatim:

> This check verifies the session's claim is internally consistent with its manifests. It does not and cannot verify that the manifests' lineage claims are themselves true. Manifest truth relies on operator integrity and the `participant_selected_by` field's accountability.

**Known gaming modes** (recorded in D-029 and preserved for future maintainers):

- **Value-flipping.** An operator edits `training_lineage_overlap_with_claude` in the manifest of a Claude subagent from `known-overlap` to `independent-claim`; the check passes.
- **`unknown` laundering.** An operator sets one participant's lineage field to `unknown` (a valid value) when the true value is `known-overlap`; the check passes.
- **Paper-human classification.** An operator records a nominal human participant who did not substantively participate; the check passes because `participant_kind: human` bypasses the lineage-value check.
- **Wrapper impersonation.** An operator routes a Claude call through a wrapper that looks like a non-Claude CLI and lies in the `provider` field; the check cannot distinguish this from a genuine non-Claude invocation.

These gaming modes are not fixed by check 13 alone. The Tier 2 question paired with check 13 (see below) is the methodology's designed counter-pressure to laundering by self-report.

### Tier 2: Guided Assessment

The following questions are printed for the assessor to consider:

1. **Provenance continuity:** Did this session's Read activity use prior provenance to understand past decisions? Were any past decisions re-proposed without acknowledgment?
2. **Specification consistency:** Are the current specifications semantically consistent with each other? Do any contradict or make assumptions that conflict?
3. **Adversarial quality:** In deliberative work, did the adversarial perspective provide genuine challenge, or did it concede too easily?
4. **Meaningful progress:** Is the methodology producing meaningful progress, or is it accumulating ceremony without advancing?
5. **Specification-reality alignment:** Are there specifications that describe things that no longer exist, or things that exist without being specified?
6. **Cross-model-honesty evidence (new; paired with check 13):** This session records `cross_model: true`. Name the concrete evidence — invocation transcript, CLI command, wall-clock gap, human presence — that distinguishes a genuine non-Claude participant from a Claude subagent with an edited manifest. If you cannot, flip `cross_model` to false. (Skip if this session does not claim cross-model participation.)

### Tool Location and Behavior

The validation tool is located at `tools/validate.sh`. It:
- Is **read-only**: it never modifies any workspace file.
- Produces a **structured report** with pass/fail/warning counts for Tier 1.
- Prints the **Tier 2 questions** after the Tier 1 report.
- Exits with **code 0** if no Tier 1 failures, **code 1** otherwise.
- Has **no dependencies** beyond standard Unix tools (bash 3.2+, grep, sed, awk) and git.

### When to Run

Validation should be run:

- At the **start** of each session, during or immediately after the Read activity.
- After the **Produce** activity, to check that new artifacts meet structural requirements.
- Before the **Close** activity, as a final coherence check.

### Limitations

Automated structural checks verify form, not meaning. Passing all structural checks does not mean:

- Specifications are correct about what they describe.
- Provenance captures the actual reasoning (it may be post-hoc rationalization).
- Decisions were well-considered.
- The methodology is serving its purpose.
- Cross-model participation is genuine rather than theatrical (see check 13's honest limit).

These deeper questions are the purpose of Tier 2, which depends on honest assessment by the agent or human conducting the session. The methodology acknowledges that when a single AI agent both does the work and assesses it, Tier 2 is self-assessment rather than independent validation. This is a known limitation (see D-009), mitigated by making the questions explicit and recording the assessment in provenance, and further mitigated since Session 005 by the D-023 non-Claude-participation rule for meta-deliberations on self-assessment mechanisms.

The immutability check (Check 10) is a basic heuristic — it detects uncommitted changes to provenance files but does not verify full immutability across git history. Comprehensive immutability verification is a potential future improvement.

Check 12 verifies the presence of D-024 required keys but does not verify that the values are correct. A manifest may have all required keys while containing nonsense values; check 12 passes. The boundary between key-presence and value-correctness is a deliberate archival choice (the Archivist's Q3 position in Session 005: "the check succeeds if a field literally contains the string `unknown`, because D-024 explicitly admits `unknown` as a truthful value").

Check 13 is **consistency-of-self-report**, not **truthfulness-of-self-report**, as documented above. The Tier 2 Q6 is the methodology's designed complement. Passing check 13 *and* the operator answering Q6 with concrete evidence is stronger than either alone; neither is a truth certificate.

## Validation

To validate this specification:

1. Run `tools/validate.sh` and verify it performs the thirteen structural checks listed in the table above.
2. Verify the tool prints the six guided questions listed above.
3. Compare the tool's actual checks against the table in this specification — they should match.
4. Verify the tool is read-only (it makes no changes to any file).
5. Verify the tool exits with code 0 when all fail-severity checks pass, and code 1 otherwise.
6. Verify that check 13's honest-limit language appears in `tools/validate.sh` (comment block above check 13), in check 13's failure message, and in this specification's "Check 13's Honest Limit" subsection. Any divergence is a specification violation.
7. Verify that check 13 reports `BLOCKED` (not `FAIL` and not `PASS`) for sessions where check 12 failed.
8. Verify that check 11 applies only to sessions with at least one `*-perspective-*.md` file, check 12 applies only to sessions with a `manifests/` subdirectory, and check 13 applies only to sessions that declare `cross_model: true`.
