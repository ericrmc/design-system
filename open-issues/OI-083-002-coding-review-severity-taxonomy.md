---
id: OI-083-002
title: Worked rubric for the coding review loop's severity taxonomy
surfaced-in-session: 083
status: open
priority: LOW
---

# OI-083-002 — Worked rubric for the coding review loop's severity taxonomy

## Surfaced

The S083 reviewer pass surfaced ambiguity at the medium/low boundary of the four-level severity taxonomy (critical / high / medium / low) introduced in `specifications/methodology.md` v3 §When to review §Coding review loop. Two reviewers reading the same finding could classify it differently — in particular, a missing test assertion (medium per spec: "correctness, safety, or coverage gap") versus a clarity nit (low). The methodology spec records the deferral and notes that genuinely-borderline findings are treated as medium for the loop's termination condition until calibrated.

## Why it matters

The loop's termination condition is "no medium-or-higher findings remain." If two reviewers disagree on classification, the loop can either stall (the implementer treats every nit as medium) or be gamed (the implementer demotes findings to low). Neither is a stable equilibrium for sustained discipline.

## What's needed

After two or three code-producing sessions have exercised the loop, collect:

- The findings each reviewer raised, with their classification.
- Cases where the implementer disagreed with the classification and what was decided.
- Cases where a finding crossed the medium/low boundary in either direction.

From that empirical base, write a 1-page rubric to `specifications/methodology.md` (or a sibling spec) with three to five worked examples per severity level. The goal is consistency across reviewers and across sessions, not classifier perfection.

## Disposition path

Open until at least three real code-producing sessions have exercised the loop. The first such session will be the next S08X session that touches `selvedge/`, `state/migrations/`, or `bin/`/`tools/` logic; the cadence-read S083 deferred is unlikely to qualify, but a return to T-03/T-07/T-09/T-16 pytest coverage extension would.
