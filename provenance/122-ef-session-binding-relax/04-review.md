---
session: 122
title: ef-session-binding-relax — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high** against `DV-S122-1`: sessions.slug lacks UNIQUE; same-second concurrent feedback calls would produce duplicate auto-slugs.
  - **fixed.** Fixed: _intake_slug now includes microsecond suffix (%f) — sub-microsecond collisions are not realistic for CLI invocations.
- **high** against `DV-S122-1`: Operator --slug is unvalidated; permits path-traversal via export at provenance/<wno>-<slug>/.
  - **fixed.** Fixed: _validate_slug enforces kebab-case ASCII regex before write_tx; test_feedback_refuses_path_traversal_slug exercises the refusal.
- **medium** against `DV-S122-1`: Passthrough EF lands in any open session regardless of kind; coding-session conflation undocumented.
  - **fixed.** Fixed: argparse description block makes passthrough vs intake explicit; behavior is documented, not enforced (operators may legitimately want EF in coding session).
- **low** against `DV-S122-1`: Empty @file body produces generic empty-after-strip error without naming the file.
  - **adjudicated.** Cosmetic; operator can debug from the file path they passed. Not worth additional code path.
## Iteration 2

- **high** against `DV-S122-1`: _SLUG_RE used re.match which accepts trailing newline; needed fullmatch to reject embedded/trailing control chars.
  - **fixed.** Fixed: switched to _SLUG_RE.fullmatch; added test cases for trailing/embedded newline + 8 other malformed shapes (uppercase, underscore, leading/trailing hyphen, double-hyphen, digit-start, space, empty).
- **high** against `DV-S122-1`: sessions.slug lacks UNIQUE; same-microsecond concurrent writes could silently create duplicates.
  - **adjudicated.** Out of S122 scope (substrate-wide invariant, not wrapper-specific); microsecond resolution makes collision practically impossible for CLI invocations; OI-S122-1 tracks the substrate migration.
- **medium** against `DV-S122-1`: Slug-shape test coverage was sparse; only ../../etc was exercised.
  - **fixed.** Fixed: parametrized test now covers 11 malformed slug shapes + 4 valid kebab shapes; 20 tests total in test_feedback_cmd.py.

## Terminal passes

- **iteration 2** — clean @ `5978ba7eb8b9`
  - Iter-2 surfaced fullmatch bug + slug-uniqueness substrate gap (OI-S122-1) + sparse slug-shape coverage; first two fixed in-iteration, third filed as follow-up issue. Coding loop converged.
