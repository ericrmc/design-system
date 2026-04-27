---
session: 083
title: Coding review loop — decisions
date: 2026-04-27
engine_version_at_close: engine-v19
mode: self-development
substrate_session_no: 4
substrate_aliases:
  D-1: D-S004-1
  D-2: D-S004-2
---

# Decisions

Markdown D-numbering aligns with substrate aliases (T-01 forced D-S004-1 to be written before D-S004-2 because D-S004-2 cites D-S004-1; this file follows the substrate ordering).

## D-1. No multi-agent deliberation convened (operator-directed) — D-S004-1

**What.** The kernel revision shipped in this session (recorded as D-2 below) would normally require multi-agent deliberation including at least one cross-family perspective per `specifications/methodology.md` §When to convene multiple agents — the change touches how the methodology works (a new reviewer mechanism with a defined termination condition, sequenced into the kernel between §When to convene and §Validation senses). No such deliberation was convened.

**Why.** The decision is operator-directed and the directive is unambiguous ("if there is any coding, a subagent reviewer must be called to check it, repeatedly until all medium+ issues are fixed"). Per §When to convene multiple agents: "If a multi-agent deliberation would otherwise be triggered but is not performed (because the workspace lacks a non-Claude provider, because the decision is operator-directed, because the cost is unwarranted for this scope), the reason is recorded in the session's decision record." This entry is that record.

**Rejected alternatives.**

- **R-2.1. Convene cross-family deliberation anyway, given the change touches the kernel.** Rejected: would not change the outcome (the operator has stated the requirement) and would consume capacity without affecting the artefact. The kernel-touching property triggers the deliberation rule, but the operator-directed property triggers the explicit-record exception, and the exception applies. The cross-family check on whether the loop's design details generalise well is a proper future session — see §Open.
- **R-2.2. Treat the operator directive as itself the cross-family perspective and record no further deliberation note.** Rejected: conflates two distinct mechanisms. Cross-family deliberation produces a written perspective that surfaces assumptions a single training-distribution shares (constraints §3); an operator directive produces a normative requirement that shapes what the deliberation is for. The methodology spec distinguishes them. Recording the deliberation-skipped exception explicitly is the discipline.

**Open.** A future session may convene cross-family perspectives on the loop's design details (severity classification, adjudication pathway, termination condition, scope boundary between executable logic and out-of-scope metadata) once the mechanism has been exercised against real code-producing sessions and there is empirical signal to deliberate over. The severity-rubric piece is tracked under `OI-083-002`; the broader cross-family review is admitted under the release gate as "mechanism-implementing-existing-methodology".

## D-2. Introduce the coding review loop as a methodology mechanism; bump engine-v18 → engine-v19 (operator-directed override of 078 D-5 release gate) — D-S004-2

**What.** `specifications/methodology.md` v3 adds §When to review with two subsections: §Coding review loop (new) and §Engine-definition close review (retained). The coding review loop requires that any session producing, modifying, or deleting executable logic (Python under `selvedge/`, SQL under `state/migrations/`, shell logic under `bin/` or `tools/`, or any other artefact whose execution behaviour the change alters) invoke a reviewer subagent — distinct from the implementer — to audit the change, address every medium-or-higher finding (fix or explicitly adjudicate with a substantive reason in `04-review.md`), and re-invoke the reviewer. The loop terminates when the reviewer reports no medium-or-higher findings remain, or halts at the four-iteration deadlock threshold. The session does not close until that condition is met. `prompts/development.md` and `prompts/application.md` invoke the mechanism. `specifications/workspace.md` v3 expands the `04-review.md` description to cover loop iterations. `engine-manifest.md` v19 records the engine bump v18 → v19. `tools/validate.sh` banner updates to engine-v19.

**Why.** Operator directive: "if there is any coding, a subagent reviewer must be called to check it, repeatedly until all medium+ issues are fixed." The directive responds to the pattern visible at S082's close: an adversarial Explore pass after the initial commit found three critical issues and several coverage gaps that the implementer's self-review missed; the close was amended in-place (post-close reviewer pass section in `provenance/082-migrate-runner/03-close.md`, substrate decision D-S003-1). Promoting that ad-hoc pattern to a structural pre-close requirement aligns with constraints §2 (prevention must be structural, not exhortative) and §5 (detection without a feedback loop into prevention does not correct anything). The loop's termination condition is the structural feedback path: a medium-or-higher finding either gets addressed or recorded as an explicit adjudication; no finding is silently dropped.

**Cite.** `specifications/methodology.md` v3 §When to review §Coding review loop; `prompts/development.md` §Operate (revised); `prompts/application.md` §Review (added); `provenance/082-migrate-runner/03-close.md` §Post-close reviewer pass; D-1 above (substrate D-S004-1) for the procedural exception.

**Rejected alternatives.**

- **R-1.1. Reuse the engine-definition close review (single-pass) for code changes too, without introducing a loop.** Rejected: a single pass does not have a termination condition tied to defect severity, so a finding is "noted" rather than addressed. This is the failure mode constraints §5 names. The loop is the substantive difference.
- **R-1.2. Make the loop optional (advisory) for "small" code changes, with implementer discretion to skip.** Rejected: the operator's directive carved out no small-change exemption, and prior sessions show "small change" is a category implementers self-grant before the bug ships. A blanket rule with explicit adjudication for false-positives is more honest than a rule with a fuzzy size threshold.
- **R-1.3. Defer the change as methodology-expanding active-spec content under the 078 D-5 release gate.** Rejected: the operator override is explicit. The release gate is a self-imposed constraint that the operator can lift, and per `specifications/methodology.md` §When to convene multiple agents, when a deliberation is otherwise triggered but not performed because the decision is operator-directed, the reason is recorded. This decision body and D-1 above (substrate D-S004-1) are that record.
- **R-1.4. Encode the loop in the substrate (a precommit gate on `04-review.md` content) at this session, not as a deferred open issue.** Rejected: a substrate gate is the right long-term home, but designing it correctly (structured "reviewer reports clean" representation, severity-classification consistency, interaction with the engine-definition close review) is its own session's worth of work and should not ride along under an already-exceptional gate override. Operator-policed enforcement plus `OI-083-001` tracking the substrate-encoding deferral is the sound first step.

**Self-hosting note.** This session edits `tools/validate.sh` (banner string only) plus engine-definition spec files. Per the final reading of the rule (executable *logic* — explicitly enumerated out-of-scope items include version strings, banner text, comments, and shell-script changes that touch only documentation lines), the banner edit does not trigger the coding review loop. The implementer ran the loop anyway as a self-hosting safety margin; iterations and findings are recorded in `04-review.md`. The engine-definition close review (single-pass) was triggered by the spec-file changes and is recorded in the same file. Both completed clean.

**Open.** The mechanism is operator-policed; the substrate does not yet refuse a coding session that closes without a clean reviewer pass. Recorded as `open-issues/OI-083-001-coding-review-substrate-enforcement.md` for a future session to design. The severity taxonomy admits classifier disagreement at its boundaries; a worked rubric is deferred until two or three code-producing sessions have exercised the loop. Recorded as `open-issues/OI-083-002-coding-review-severity-taxonomy.md`.

## D-3. Engine version bump v18 → v19 (bundled into D-2 in the substrate)

**What.** `engine-manifest.md` frontmatter version 18 → 19, supersedes line updated, §Current engine version rewritten, §Engine-version history appended. `tools/validate.sh` banner updated to engine-v19.

**Why.** Per §Versioning in the manifest: "the engine version increments when any file in the active set above changes substantively." `methodology.md` (v2 → v3), `prompts/development.md`, `prompts/application.md`, and `specifications/workspace.md` (v2 → v3) all changed substantively. The bump is mandatory, not optional. Per the S082 precedent (D-S003-1 bundles the v17 → v18 bump into the substantive ship decision in the substrate), this entry exists in markdown only; D-S004-2's body records the same fact in the substrate.

**Rejected alternatives.**

- **Defer the bump to a later session.** Rejected: would break the §Versioning rule. The bump tracks the spec change, not when downstream consumers notice.
