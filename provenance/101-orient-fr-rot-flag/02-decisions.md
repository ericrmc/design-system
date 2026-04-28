---
session: 101
title: orient-fr-rot-flag — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Adopt regex-only always-on inline rot annotation in orient for FRs citing resolved or absent issue aliases

**Kind:** substantive.  **Outcome:** adopt process_rule `orient-fr-rot-annotation`.

**Why.**

- (engine_feedback) EF-S100-1 named recurring friction in cleanup sessions: each undisposed FR requires mental cross-reference of cited aliases against current issue state. [EF-S100-1]
- (deliberation) Three perspectives converged on scope (cited-issue resolved or absent only) and on leaving historical FRs as text-only with no backfill. [P-7-P-1]
- (deliberation) P-3 argued opt-in cleanup tooling produced the 30-FR backlog; a flag operators must remember does not address recurring friction. [P-7-P-3]
- (constraint) Persisting regex-derived citations in a new table would be persisting a derivation of FR text; irreversible schema should follow evidence not precede it.

**Effects.**

- modifies _compute_orient_packet and _orient_markdown gain rot extraction and annotation
- opens_issue Rename objects.citable_alias to objects.alias for query ergonomics

**Rejected alternatives.**

- **R-1.1.** Hybrid mechanism: add close_state_item_cites table for structured citations going forward, regex fallback for legacy FRs (P-2 position).
  - (inferior_tradeoff) Permanent submit-path tax on every close-record for value that arrives only at next orient; schema is irreversible and should follow evidence.
  - (redundant_with_existing) FR text already canonicalises the citation; persisting parser output duplicates information already in close_state_items.
- **R-1.2.** Opt-in --fr-rot flag with inline annotation gated behind it (P-1 position).
  - (inferior_tradeoff) Opt-in cleanup signals reproduce original failure mode: operators forget the flag exists and rot accumulates as it does without the feature.
- **R-1.3.** Opt-in --fr-rot flag emitting a separate Rotting forward-references section after the FR queue (P-2 CLI position).
  - (inferior_tradeoff) Splits operator attention across two FR sections and still fails the opt-in problem; aggregation gives no value over inline.
- **R-1.4.** Do nothing; treat the friction as small enough to leave alone (P-3 minority view).
  - (inferior_tradeoff) EF-S100-1 explicitly proposed the remedy; recurring mental-cross-reference cost is real and inline annotation is cheap to add.
