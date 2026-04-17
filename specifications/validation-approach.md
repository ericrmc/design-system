---
title: Validation Approach
version: 1
status: active
created: 2026-04-17
last-updated: 2026-04-17
supersedes: none
---

# Validation Approach

## Purpose

This specification defines how the methodology validates itself: what is checked, how checks are organized, and what the checks can and cannot assure. It serves the methodology's self-hosting principle — a methodology that cannot verify its own specifications cannot evolve reliably.

## Specification

### Two-Tier Model

Validation has two tiers, reflecting the distinction between properties that can be checked mechanically and those that require judgment.

**Tier 1: Structural Checks** are automated checks run by `tools/validate.sh`. They verify that the workspace's files conform to the formats and conventions defined in other specifications. Structural checks are necessary but not sufficient for methodology health — a workspace can pass all structural checks while its specifications are semantically wrong or its provenance is misleading.

**Tier 2: Guided Assessment** is a set of questions printed by the validation tool for the agent or human conducting the session to consider. These questions address properties that cannot be checked mechanically: semantic consistency, provenance usefulness, and whether the methodology is making genuine progress.

### Tier 1: Structural Checks

The following checks are automated:

| # | Check | Source Spec | Severity |
|---|-------|-------------|----------|
| 1 | Required top-level files exist (PROMPT.md, SESSION-LOG.md, open-issues.md) | workspace-structure | Fail |
| 2 | Required directories exist (specifications/, provenance/) | workspace-structure | Fail |
| 3 | Each specification has YAML frontmatter with required fields (title, version, status, created, last-updated, supersedes) | workspace-structure | Fail |
| 4 | Each specification has three required section headings (Purpose, Specification, Validation) | workspace-structure | Fail |
| 5 | Provenance directories follow NNN-title naming convention | workspace-structure | Fail |
| 6 | Session log has an entry for each provenance directory | workspace-structure | Fail |
| 7 | Each provenance directory contains at least one .md file | methodology-kernel | Fail |
| 8 | Provenance files have YAML frontmatter with required fields (session, title, date, status) | workspace-structure | Fail |
| 9 | Decision records include rejected alternatives sections | methodology-kernel | Warning |
| 10 | No uncommitted changes to provenance files (basic immutability heuristic) | workspace-structure | Warning |

Checks marked **Fail** cause the tool to exit with a non-zero code. Checks marked **Warning** are reported but do not cause failure.

### Tier 2: Guided Assessment

The following questions are printed for the assessor to consider:

1. **Provenance continuity:** Did this session's Read activity use prior provenance to understand past decisions? Were any past decisions re-proposed without acknowledgment?
2. **Specification consistency:** Are the current specifications semantically consistent with each other? Do any contradict or make assumptions that conflict?
3. **Adversarial quality:** In deliberative work, did the adversarial perspective provide genuine challenge, or did it concede too easily?
4. **Meaningful progress:** Is the methodology producing meaningful progress, or is it accumulating ceremony without advancing?
5. **Specification-reality alignment:** Are there specifications that describe things that no longer exist, or things that exist without being specified?

### Tool Location and Behavior

The validation tool is located at `tools/validate.sh`. It:
- Is **read-only**: it never modifies any workspace file
- Produces a **structured report** with pass/fail/warning counts for Tier 1
- Prints the **Tier 2 questions** after the Tier 1 report
- Exits with **code 0** if no Tier 1 failures, **code 1** otherwise
- Has **no dependencies** beyond standard Unix tools (bash, grep, sed, awk) and git

### When to Run

Validation should be run:
- At the **start** of each session, during or immediately after the Read activity
- After the **Produce** activity, to check that new artifacts meet structural requirements
- Before the **Close** activity, as a final coherence check

### Limitations

Automated structural checks verify form, not meaning. Passing all structural checks does not mean:
- Specifications are correct about what they describe
- Provenance captures the actual reasoning (it may be post-hoc rationalization)
- Decisions were well-considered
- The methodology is serving its purpose

These deeper questions are the purpose of Tier 2, which depends on honest assessment by the agent or human conducting the session. The methodology acknowledges that when a single AI agent both does the work and assesses it, Tier 2 is self-assessment rather than independent validation. This is a known limitation (see D-009), mitigated by making the questions explicit and recording the assessment in provenance.

The immutability check (Check 10) is a basic heuristic — it detects uncommitted changes to provenance files but does not verify full immutability across git history. Comprehensive immutability verification is a potential future improvement.

## Validation

To validate this specification:

1. Run `tools/validate.sh` and verify it performs the ten structural checks listed in the table above
2. Verify the tool prints the five guided questions listed above
3. Compare the tool's actual checks against the table in this specification — they should match
4. Verify the tool is read-only (it makes no changes to any file)
5. Verify the tool exits with code 0 when all fail-severity checks pass, and code 1 otherwise
