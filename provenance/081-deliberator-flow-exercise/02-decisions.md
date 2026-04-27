---
session: 081
title: First real deliberator-N flow — decisions
date: 2026-04-27
substrate_session_no: 2
---

# Decisions

Three decisions, all written to the substrate as rows in `decisions` (substrate `decision_id` 6, 7, 8; aliases `D-S002-1`, `D-S002-2`, `D-S002-3`). One is a calibration; two are dispositions. The calibration carries three rejected alternatives in `decision_alternatives`; the dispositions carry none (per T-02, only substantive decisions require alternatives at session-close).

## D-1 — Ratify 17-table substrate count for engine-v17 via D-10 breach clause; align manifest enumeration

**Substrate alias:** `D-S002-1`. **Kind:** `calibration`.

**What.** Ratify the actual schema count in `state/migrations/001-initial.sql` of 17 tables for engine-v17. Record the +1 over 078 D-10's ≤16-table budget as a calibrated breach with cause; the cause is `synthesis_points`, which carries T-14 (convergence requires ≥2 source_perspectives, enforced as a CHECK constraint) and has no other structural home that does not re-introduce the prose-state failure mode the substrate exists to refuse.

Manifest enumeration in `specifications/engine-manifest.md` §Substrate is updated from 15 names to 17 names: both `objects` (which 078 D-10's enumeration always included but the manifest's prose omitted) and `synthesis_points` (the calibrated breach). The manifest annotation calls out that `objects` is the citable_alias indirection table powering T-01.

This ratification is **narrow**: it does not relax D-10's budget mechanism for future additions. Each future table proposal continues to be evaluated against the 16-table budget plus a per-addition cause check.

**Why.** Sources from substrate deliberation 2 (sealed `2026-04-27T06:14:18.722Z`):

- [P-2-claude] (anthropic) proposed disposition C (recategorise `objects` as substrate-infrastructure exempt). Rejected here because 078 D-10's enumeration explicitly included `objects` in its 16-table list (verified at `provenance/078-design-commitments/02-decisions.md` line 354), so reclassifying `objects` would substantively rewrite D-10 and is gate-blocked.
- [P-2-codex] (openai) proposed disposition A (ratify-17 with narrow cause). Adopted with the narrowness discipline P-2-codex named ("the recorded cause should be concrete enough that future additions cannot cite this as generic permission").
- [P-2-adversarial] (anthropic) proposed disposition D (replace D-10's budget mechanism). Not acted on here because rewriting D-10 substantively is gate-blocked; preserved as a minority and carried forward as OI-081-001 for post-gate review.

The convergence on rejecting B (synthesis_point 2) and on aligning the manifest with the schema (synthesis_point 3) is recorded in the substrate.

**Rejected alternatives.**

- **B — Subtract `synthesis_points`.** Absorb T-14 elsewhere (deliberations.synthesis_md JSON, or generalised notes table with a kind discriminator). **Rejected**: structurally blocked on the absent `selvedge migrate` runner (OI-080-001 / EF-079-002). Substantively wrong even if unblocked — moving T-14 from a CHECK constraint to application-layer JSON-parse is the prose-state failure mode `constraints.md` property 1 names as the failure the substrate exists to eliminate.
- **C — Recategorise `objects` as substrate-infrastructure exempt.** Treat `objects` as plumbing exempt from the 16-table budget; raise budget to 17 only for synthesis_points. **Rejected**: 078 D-10's enumeration explicitly included `objects` in its 16-table list, so reclassifying `objects` would substantively revise D-10 (gate-blocked) rather than recategorise within it. Also adds a category distinction (domain vs infrastructure) the methodology has not formally drawn before, increasing surface that future authors must maintain.
- **D — Replace D-10's budget mechanism.** Substantively rewrite the budget rule itself; dissolve OI-079-001 rather than answer it. **Rejected** under 078 D-5 release gate; carried forward as OI-081-001 for post-gate reconsideration.

**Open.** Whether the table-count budget remains the right mechanism after the release gate lifts — see OI-081-001. Manifest enumeration alignment for `state/migrations/002-*.sql` (when migration 002 lands) follows the same discipline this decision sets.

---

## D-2 — Backfill OI-079-001 + record numbering-convention inconsistency

**Substrate alias:** `D-S002-2`. **Kind:** `disposition`.

**What.** OI-079-001 was named in `provenance/079-substrate-vertical-slice/02-decisions.md` (final §"Open issues raised by this session"), in `provenance/080-cli-deliberator-extension/00-assessment.md` §Discrepancy noted at open, and in `provenance/080-cli-deliberator-extension/03-close.md` §What S081 should address — but the issue file `open-issues/OI-079-001.md` was never written and the index was never updated. S081 backfills the file (with status: Resolved, resolved-in-session: 081), and adds a row to both the active and resolved tables in `open-issues/index.md`. The file is kept in the active issues directory (not moved to `open-issues/resolved/`) for OI-081-001 follow-up linkage; recorded as hybrid-state, parallel to OI-016's existing pattern.

The numbering-convention text in `open-issues/index.md` ("strictly append-only: OI-001 was first, OI-002 second, etc.") does not anticipate the session-prefixed scheme that OI-080-001 and OI-079-001 (now backfilled) and OI-081-001 (now opened) all use. The convention text is **not** edited in S081 — that resolution belongs to a future session, which can either backfill the convention text to admit the session-prefixed scheme or normalise the existing session-prefixed IDs to the legacy sequential scheme. The inconsistency is recorded here so the next reader has it in front of them.

**Why.** Provenance integrity. An issue cited in three provenance files but absent as a file in `open-issues/` is exactly the prose-state drift the substrate plus index discipline are meant to refuse; backfilling the file and the index closes the surface inconsistency. The convention-text deferral is itself a small instance of the same drift, recorded here rather than silently corrected so a future session has authority to choose between the two normalisation directions.

**Open.** The numbering-convention text resolution. Future session decides.

---

## D-3 — Open OI-081-001 carrying P-2-adversarial minority for post-gate review

**Substrate alias:** `D-S002-3`. **Kind:** `disposition`.

**What.** Open `open-issues/OI-081-001.md` (status: Open — deferred to post-release-gate review; priority: LOW post-gate; blocked-on: 078 D-5 release gate). The issue carries forward the [P-2-adversarial] minority position from S081 deliberation 2 (substrate `synthesis_point_id=5`, kind = 'minority'): that 078 D-10's table-count budget is a derived quantity masquerading as a constraint, and the protective mechanism (count) is structurally available to the substrate while the narrative-discipline mechanism (prose enumeration matching the count across two documents) demonstrably failed twice across three sessions in exactly the prose-state pattern `specifications/constraints.md` property 1 names.

The post-gate session that takes up OI-081-001 should convene cross-family perspectives fresh — the original minority came from an Anthropic-family adversarial agent, and a non-Anthropic perspective on whether the budget *as a mechanism* still earns its keep would be load-bearing.

Index updated: active count moves 14 → 15.

**Why.** Methodology preservation. The kernel says (§When to convene multiple agents) "Synthesis preserves dissent: a minority position is recorded as a minority, not erased." The substrate carries this as `synthesis_point_id=5`; the workspace's open-issues surface carries it as OI-081-001. Both pathways together make the position re-discoverable from either direction (substrate query for minority points, or open-issues directory traversal).

**Open.** All of OI-081-001 by definition. The release gate is the dependency.

---

## Engine-version impact

`engine-v17` unchanged. The manifest enumeration edit is a correction-of-omission in prose (adding two table names that should always have been present), not a substantive content addition. Per `engine-manifest.md` §Versioning ("Typo corrections and formatting do not bump"), the engine version is not bumped. The manifest's frontmatter `updated-by-session` is updated from 079 to 081 to record the touch.

The release gate (078 D-5) is not breached: D-1 is a calibration permitted under the existing breach clause; D-2 and D-3 are dispositions (workspace-bookkeeping). No new active-spec content is added to `methodology.md`, `constraints.md`, `workspace.md`, the prompts, or `validate.sh`.

## Substrate state at decisions-write

- `deliberations` rows: 2 (rows 1 from S080 smoke; 2 from S081, sealed).
- `perspectives` rows: 5 (rows 1–2 from S080 smoke; 3–5 from S081 — claude/codex/adversarial).
- `synthesis_points` rows: 5 (row 1 from S080 smoke; 2–5 from S081 — two convergence, one divergence, one minority).
- `decisions` rows: 8 (rows 1–5 from S080; 6–8 from S081).
- `decision_alternatives` rows: 12 total (9 from S080 D-1..D-4 substantive + 3 from S081 D-1 calibration; S081 D-2 and D-3 are dispositions and T-02 does not require alternatives).
- `refs` rows: 4 total in substrate at S081 close (S080 added none; S081 D-1 wrote 3 to the perspectives, D-3 wrote 1 to P-2-adversarial).

## Open issues raised by this session

- **OI-081-001** — Open, LOW post-gate. Replace table-count budget with derived-only check? Carries P-2-adversarial minority.

## Open issues resolved by this session

- **OI-079-001** — Resolved by D-1 (file backfilled by D-2). Hybrid-state (in active and resolved tables) for OI-081-001 follow-up linkage.

## Engine-feedback raised by this session

None.
