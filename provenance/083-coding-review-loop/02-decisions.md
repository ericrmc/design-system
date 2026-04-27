---
session: 083
title: Coding review loop — decisions
date: 2026-04-27
engine_version_at_close: engine-v19
mode: self-development
---

# Decisions

## D-1. Introduce the coding review loop as a methodology mechanism (operator-directed)

**What.** `specifications/methodology.md` v3 adds §When to review with two subsections: §Coding review loop (new) and §Engine-definition close review (retained). The coding review loop requires that any session producing, modifying, or deleting executable code (Python under `selvedge/`, SQL under `state/migrations/`, shell under `bin/` or `tools/`, or any other artefact intended to execute) invoke a reviewer subagent — distinct from the implementer — to audit the change, address every medium-or-higher finding (fix or explicitly adjudicate with a reason in `04-review.md`), and re-invoke the reviewer. The loop terminates when the reviewer reports no medium-or-higher findings remain. The session does not close until that condition is met. `prompts/development.md` and `prompts/application.md` invoke the mechanism. `specifications/workspace.md` v3 expands the `04-review.md` description to cover loop iterations. `engine-manifest.md` v19 records the engine bump v18 → v19. `tools/validate.sh` banner updates to engine-v19.

**Why.** Operator directive: "if there is any coding, a subagent reviewer must be called to check it, repeatedly until all medium+ issues are fixed." The directive responds to the pattern visible at S082's close: an adversarial Explore pass after the initial commit found three critical issues and several coverage gaps that the implementer's self-review missed; the close was amended in-place (post-close reviewer pass section in `provenance/082-migrate-runner/03-close.md`). Promoting that ad-hoc pattern to a structural pre-close requirement aligns with constraints §2 (prevention must be structural, not exhortative) and §5 (detection without a feedback loop into prevention does not correct anything). The loop's termination condition is the structural feedback path: a medium-or-higher finding either gets addressed or recorded as an explicit adjudication; no finding is silently dropped.

**Cite.** `specifications/methodology.md` v3 §When to review §Coding review loop; `prompts/development.md` §Operate (revised); `prompts/application.md` §Review (added); `provenance/082-migrate-runner/03-close.md` §Post-close reviewer pass.

**Rejected alternatives.**

- **Close-time single-pass review only (the existing engine-definition rule, reused for code).** Rejected: a single pass does not have a termination condition tied to defect severity, so a finding is "noted" rather than addressed. This is exactly the failure mode constraints §5 names. The loop is the substantive difference.
- **Make the loop optional (advisory) for "small" code changes.** Rejected: the operator's directive does not carve out a small-change exemption, and prior sessions show that "small change" is a category implementers self-grant before the bug ships. A blanket rule with explicit adjudication for false-positives is more honest than a rule with a fuzzy size threshold.
- **Defer the change as methodology-expanding active-spec content under the 078 D-5 release gate.** Rejected: the operator override is explicit. The release gate is a self-imposed constraint that the operator can lift, and per `specifications/methodology.md` (when a deliberation is otherwise triggered but not performed because the decision is operator-directed, the reason is recorded), the gate's "no new active-spec content" clause yields to operator direction with the reason recorded — which this entry is.
- **Encode the loop in the substrate (a precommit gate on `04-review.md` content).** Rejected for now: a substrate gate is the right long-term home, but designing it correctly (what does "reviewer reports clean" look like as a structured row? how is severity classified consistently?) is its own session. Operator-policed enforcement plus an open issue tracking the substrate-encoding deferral is the sound first step. See §Open.

**Self-hosting note.** This session edits `tools/validate.sh` (banner string only) plus engine-definition spec files. Per the final reading of the rule (executable *logic* — explicitly enumerated out-of-scope items include version strings, banner text, comments, and shell-script changes that touch only documentation lines), the banner edit does not trigger the coding review loop. The implementer ran the loop anyway as a self-hosting safety margin; iterations and findings are recorded in `04-review.md`. The engine-definition close review (single-pass) was triggered by the spec-file changes and is recorded in the same file. Both completed clean.

**Open.** The mechanism is operator-policed; the substrate does not yet refuse a coding session that closes without a clean reviewer pass. Recorded as `open-issues/OI-083-001-coding-review-substrate-enforcement.md` for a future session to design. The severity taxonomy admits classifier disagreement at its boundaries; a worked rubric is deferred until two or three code-producing sessions have exercised the loop. Recorded as `open-issues/OI-083-002-coding-review-severity-taxonomy.md`.

## D-2. No multi-agent deliberation convened (operator-directed)

**What.** The kernel revision in D-1 would normally require a multi-agent deliberation including at least one cross-family perspective per `specifications/methodology.md` §When to convene multiple agents (the change touches how the methodology works). No such deliberation was convened.

**Why.** The decision is operator-directed and the directive is unambiguous. Per §When to convene multiple agents: "If a multi-agent deliberation would otherwise be triggered but is not performed (because the workspace lacks a non-Claude provider, because the decision is operator-directed, because the cost is unwarranted for this scope), the reason is recorded in the session's decision record." This entry is that record.

**Rejected alternatives.**

- **Convene cross-family deliberation anyway.** Rejected: would not change the outcome (the operator has stated the requirement) and would consume capacity without affecting the artefact. The cross-family check on whether the loop's *design details* (severity classification, adjudication pathway, termination condition) generalise well is a proper future session — recorded under §Open in D-1 alongside the substrate-enforcement deferral.

**Open.** A future session may convene cross-family perspectives on the loop's design details once the mechanism has been exercised against real code-producing sessions and there is empirical signal to deliberate over.

## D-3. Engine version bump v18 → v19

**What.** `engine-manifest.md` frontmatter version 18 → 19, supersedes line updated, §Current engine version rewritten, §Engine-version history appended. `tools/validate.sh` banner updated to engine-v19.

**Why.** Per §Versioning in the manifest: "the engine version increments when any file in the active set above changes substantively." `methodology.md` (v2 → v3), `prompts/development.md`, `prompts/application.md`, and `specifications/workspace.md` (v2 → v3) all changed substantively. The bump is mandatory, not optional.

**Rejected alternatives.**

- **Defer the bump to a later session.** Rejected: would break the §Versioning rule. The bump tracks the spec change, not when downstream consumers notice.
