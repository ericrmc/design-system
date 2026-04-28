---
session: 101
title: orient-fr-rot-flag — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **medium**: rot key is conditionally present on next_session_should items; breaks the previously-fixed item shape and any JSON consumer expecting stable schema.
  - **fixed.** rot key now always present on next_session_should items as a list, empty when no rot detected.
- **medium**: fr_cite_aliases set iteration non-determinism could affect IN-clause order across runs; verify output remains byte-identical across operators.
  - **adjudicated.** Replaced set with append-dedup list; placeholder order is now deterministic. Per-FR rot list was already deterministic since built from text-order cites.
- **high**: Regex extracts OI-089 prefix from malformed OI-089- text; reviewer marked acceptable since extracted alias is valid prefix.
  - **adjudicated.** Reviewer self-corrected to acceptable. Extracting valid prefix from malformed trailing-hyphen text is correct behavior; operators do not write malformed FR aliases in practice.
