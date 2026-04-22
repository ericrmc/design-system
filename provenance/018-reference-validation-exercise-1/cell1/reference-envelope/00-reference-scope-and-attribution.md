---
session: 018
title: Reference Scope & Attribution — Kerth Prime Directive + Safety Poll (Retrospective Opening)
date: 2026-04-22
status: drafted-not-sealed
draft_rejected_at_c3_gate: true
see_also: ../03-c3-test-result.md
---

> **NOT SEALED.** D2 rejected at C3 pre-seal gate per `../03-c3-test-result.md`. This envelope was drafted during Cell 1 sourcing but the case pack was never sealed (no anti-drift-witness commit for a sealed case). Files preserved as provenance of what was drafted before rejection. The `status: sealed` fields in per-component files below are also rewritten to `drafted-not-sealed`.


# Reference Scope & Attribution

## Reference case identity

**Kerth's retrospective opening protocol**, consisting of two canonical components:

1. **The Prime Directive** — a 40-word statement read aloud at the start of a retrospective.
2. **The Safety Poll** — the anonymous 1-to-5 safety rating procedure Kerth specifies as part of his broader "safety check."

## Attribution

- **Author:** Norman L. Kerth
- **Primary source:** *Project Retrospectives: A Handbook for Team Reviews*, Dorset House, 2001. ISBN 0-932633-44-7.
- **Derivative and citing sources** (anti-drift witnesses — see `99-anti-drift-witnesses.md` for URLs + fetch dates):
  - Retrospective Wiki (reference for Prime Directive verbatim text)
  - TeamRetro (reference for Prime Directive verbatim text + opening usage)
  - FunRetrospectives (reference for Prime Directive verbatim text)
  - Joshua Kerievsky, Medium (reference for Safety Poll procedure)

## Scope boundary (what is IN the reference for this exercise)

- The exact Prime Directive text (40 words).
- The Prime Directive's stated purpose: pre-retrospective blame-deflection framing from individuals to system-level conditions.
- The Safety Poll's structure: anonymous 1-to-5 rating where 5 = "no problem talking about anything" and 1 = "I won't speak / I'll go along with managers", collected before the retrospective begins, tallied and visualised.

## Scope boundary (what is OUT of scope for this exercise)

- The full content of Kerth's 2001 book (not sourceable online; not commit-eligible as anti-drift witness).
- Kerth's other three safety-check steps beyond the Safety Poll (Steps 1, 3, 4 of the 4-step safety check are referenced in Kerievsky's blog post but not documented in detail anywhere publicly accessible).
- Any subsequent retrospective body structure (the "Original Four" questions, the "Events timeline" exercise, etc.). The exercise is scoped to **the opening** only.
- Translations or linguistic variants of the Prime Directive.

## Reference type per §1 C7 (representativeness)

Structured procedure / read-aloud script with embedded measurement step. Matches the methodology's external-artefact claim type (see Session 010 "House Decision in Five Moves" precedent: procedural script with embedded step structure).

## Author-uncertainty-declared (C8c) — best-reproducible summary

Kerth's own uncertainty, as documented in secondary sources citing his book:

- **Scale-dependence uncertainty.** Kerth notes the procedure was designed for end-of-project retrospectives and may not transfer cleanly to shorter iteration retrospectives or single-team contexts (paraphrased from Kerievsky's commentary on Kerth's context).
- **Manager-presence uncertainty.** Kerth explicitly acknowledges that the safety poll's utility depends on whether managers are in the room; the procedure assumes the possibility of managerial presence producing speech suppression.
- **Cultural-context uncertainty.** Kerth's facilitation register (West Coast U.S. software engineering culture, circa 2000) may not transfer across cultures without adaptation.

The author-uncertainty commentary reproduced here is derivative (secondary sources paraphrasing Kerth) rather than verbatim-from-book. Flagged as a C8c completeness limitation — full verbatim author-uncertainty would require the book.

## Sealing status

This reference envelope is **sealed** at Cell 1 close. The Case Steward does not read it further during Cell 2 execution; Produce agents do not see any of the files in `reference-envelope/` during Cell 2. At Cell 3 open, validators may unseal and read the envelope for comparison work.
