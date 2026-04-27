---
session: 083
title: Coding review loop — assessment
date: 2026-04-27
engine_version_at_open: engine-v18
mode: self-development
---

# Assessment

## State at open

The S082 close left three S083 candidates in priority order: (1) human reviewer-subtractor cadence read, (2) numbering-convention text resolution, (3) pytest coverage extension to T-03/T-07a/b/T-09/T-16. All three are admitted under the 078 D-5 release gate.

The operator overrides this priority with an explicit directive: update the engine definition so that any session that produces code must invoke a reviewer subagent that is re-invoked until no medium-or-higher findings remain. This is methodology-expanding active-spec content — the kind of change the 078 D-5 gate was written to forbid. The override is operator-directed and is recorded as such in §Decisions; per `specifications/methodology.md` (when a deliberation is otherwise triggered but not performed because the decision is operator-directed, the reason is recorded), no multi-agent deliberation is convened.

The S082 close itself motivates the change: an adversarial reviewer pass after the initial close commit found three critical issues and several coverage gaps that the implementer's self-review missed, and the close had to be amended. The operator's directive promotes that informal post-hoc pattern into a structural pre-close requirement, with a termination condition (no medium-or-higher findings).

## Agenda

1. Add §When to review to `specifications/methodology.md`, with two subsections: §Coding review loop (the new loop) and §Engine-definition close review (a clarified retention of the prior close-review rule for engine-definition-file changes).
2. Update `prompts/development.md` and `prompts/application.md` to invoke both mechanisms.
3. Expand `04-review.md` description in `specifications/workspace.md` to cover loop iterations.
4. Bump engine version v18 → v19; update `engine-manifest.md` and `tools/validate.sh` banner.
5. Run a reviewer subagent against the changeset (the new mechanism applied to its own introduction) and address medium+ findings until clean. The changeset is mostly markdown spec edits plus a banner string update in `validate.sh`; this exercises the engine-definition close review path and is a useful self-hosting demonstration of the loop on a near-trivial code change (the banner).
6. Commit and push.

## What is not in scope

- The four other engine-feedback inbox items.
- The S083 candidates from the S082 close (cadence read, numbering convention, T-03/T-07/T-09/T-16 coverage).
- Any substrate migration. The new mechanism is operator-policed for now; structural enforcement (e.g., a `04-review.md` precommit gate) is deferred and recorded as an open issue at close if warranted.
