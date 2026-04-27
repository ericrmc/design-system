---
id: OI-083-001
title: Substrate enforcement of the coding review loop
surfaced-in-session: 083
status: open
priority: MEDIUM
---

# OI-083-001 — Substrate enforcement of the coding review loop

## Surfaced

S083 D-1 introduces the coding review loop (`specifications/methodology.md` v3 §When to review §Coding review loop): any session producing, modifying, or deleting executable logic must invoke a reviewer subagent, address every medium-or-higher finding, and repeat until clean. The mechanism is currently operator-policed; the substrate does not yet refuse a coding session that closes without a clean reviewer pass or an explicit halted-state record.

## Why it matters

Constraints §2 (prevention must be structural) and §5 (detection without a feedback loop into prevention does not correct anything) argue that the loop will degrade over time if its enforcement is exhortative rather than structural. The S082 close already shows that an implementer's self-review misses load-bearing findings; an operator-policed rule depends on the implementer remembering to invoke the reviewer at all.

## What's needed

A substrate gate that refuses commit (or refuses session-close attestation) when:

- The session's commits include changes to files matching the "executable logic" pattern (Python under `selvedge/`, SQL under `state/migrations/`, shell logic under `bin/` or `tools/`, plus future-defined extensions);
- AND `provenance/NNN-<slug>/04-review.md` is absent, or its final-pass record does not assert that the reviewer reported clean of medium-or-higher findings (or that the loop halted at the four-iteration deadlock threshold).

Open design questions:

- What is the structured representation of "reviewer reported clean"? A `04-review.md` row in the substrate (a new table) or a parsed marker in the markdown file?
- How is "executable logic" classified at commit time? A path regex is mechanical but loses the methodology spec's "execution behaviour" test. A change that flips a boolean default in a comment-out region is logic; a rename that preserves behaviour is admittedly out of scope but is hard to distinguish at the file level.
- How does the gate interact with the engine-definition close review (single-pass)? Both can trigger; the substrate must record both completions.

## Disposition path

Defer to a future session that has capacity for substrate work. The 078 D-5 release gate's bug-fix and validator-tightening admittance covers this kind of change. Closing OI-080-001 in S082 proved the migration runner can ship under the gate.
