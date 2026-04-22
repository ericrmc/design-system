---
session: 022
title: Decisions — Read-Contract Adoption, Engine-v3 Bump, Retroactive Migrations
date: 2026-04-22
status: complete
---

# Decisions — Session 022

## D-084: Adopt R1–R11 read-contract minimum-coherent set; engine-v2 → engine-v3

**Triggers met:** [d016_1, d016_2, d016_3, d023_1, d023_2, d023_3]

**Triggers rationale:** d016_1 fires — R4 substantively revises `methodology-kernel.md` v4 → v5 (§1 Read revision). d016_2 fires — R5 creates `specifications/read-contract.md` v1 (new spec) and R6 revises `workspace-structure.md` v3 → v4 substantively. d016_3 fires — R9 revises `validation-approach.md` v4 → v5 (new Tier 1 checks 20/21/22 + new Tier 2 Q9). d023_1 fires — kernel modification requires non-Claude participation (Outsider Shape A satisfies). d023_2 fires — specifications/multi-agent-deliberation.md itself unchanged this session BUT R5's read-contract.md creates new engine-definition content governing how raw perspective files are preserved at close (i.e., cross-cutting onto multi-agent-deliberation.md's §Provenance Layout via a pointer-only cross-reference in R6 workspace-structure.md). Conservative over-declaration per Session 021 d016_1 precedent: declare d023_2 to honor honest-limit-aligned disclosure. d023_3 fires — validation-approach.md is revised in ways that touch Tier 2 semantic validation (new Q9).

**Decision:** Adopt R1 through R11 as a minimum-coherent set addressing the workspace-scaling trajectory:

- **R1.** Remove the R3 mempalace paragraph from `CLAUDE.md` (E.1). §5.4 warrant ratified per 4-of-4 cross-family.
- **R2.** Adopt the bounded-read-contract frame with vocabulary refinement per 3-of-4 cross-family. Default-read surface vs archive surface distinction cuts across existing engine-definition/development-provenance/application-scope file classes as a separate access-discipline dimension.
- **R3.** Revise `prompts/development.md` lines 19, 25, 43 per synthesis text (Architect + Conservator + Outsider convergence).
- **R4.** Revise `methodology-kernel.md` v4 → v5 §1 Read. v4 preserved as `methodology-kernel-v4.md` status: superseded.
- **R5.** Create `specifications/read-contract.md` v1 as new narrow-single-purpose specification housing read-contract normative content (Outsider frame-completion contribution). Fourth narrow-purpose spec in OI-002 n=3→n=4 pattern.
- **R6.** Revise `workspace-structure.md` v3 → v4 substantive (adds cross-references; pairs with open-issues directory creation). v3 preserved as `workspace-structure-v3.md`.
- **R7.** Revise `prompts/application.md` analogously to R3 for external-application consistency.
- **R8.** Retroactive migrations this session: R8a SESSION-LOG thin-index restoration; R8b open-issues/ directory split; R8c Session 014 Outsider archive-pack migration; R8d enumerated queue for remaining over-threshold raws (via check 20); R8e/R8f defer.
- **R9.** `tools/validate.sh` new Tier 1 checks 20 (default-read budget), 21 (archive-pack manifest integrity), 22 (archive-pack citation consistency). New constants `DEFAULT_READ_HARD_WORD_CEILING=15000`, `DEFAULT_READ_SOFT_WORD_CEILING=10000`, `READ_CONTRACT_ADOPTION_SESSION=22`. Pair with new Tier 2 Q9 in `validation-approach.md` v5.
- **R10.** Declare `engine-v3` in `engine-manifest.md` §2 + §7. Add `specifications/read-contract.md` to §3.
- **R11.** OI housekeeping per synthesis §5.

**Rationale:**

The synthesis §2 cross-family analysis established 3-of-4 or 4-of-4 cross-family warrant for C1 through C9. The adoption set is the minimum-coherent response to the scaling trajectory — each R-item addresses a specific observation (R1 addresses §5.4; R2-R5 address the read-contract; R8 addresses the current ceiling breaches; R9 prevents future drift).

Engine-v3 is warranted per `engine-manifest.md` §5 (substantive revision to multiple engine-definition files). The Skeptic's adjacent-bump cadence concern (§5.4 minority) is preserved with activation warrants.

**Rejected alternatives:**

1. **Skeptic total rejection (minimum-set: E.1 + SESSION-LOG-restoration only).** Rejected because it does not address the kernel §1 Read unexecutability (Skeptic's falsifier-burden test (b)) — the operator explicitly argued paginated-Read is the laundering pattern; restoring SESSION-LOG alone returns that one file to executability but does not repair the kernel sentence itself nor address the Session 014 outlier. Skeptic's minimum-set is preserved as §5.1 with activation warrants.

2. **Top-level `archives/` directory for archive-packs** (Outsider §5.2). Rejected in favor of session-local location for locality-plus-new-top-level-scaling-concern reasons. Preserved as §5.2 minority.

3. **8,000-word per-file hard budget** (Outsider §5.3). Rejected in favor of 15,000-word ceiling (compromise with Architect's 20K-token ≈ 15K-word and Conservator's 25K-token values). Preserved as §5.3 minority.

4. **Superseded-spec reclassification immediately** (Outsider §5.5). Rejected in favor of deferring; existing `-vN.md` suffix convention adequate. Preserved as §5.5 minority.

5. **Epoch-index consolidation of Sessions 001–010** (operator candidate #4). Rejected unanimously (Conservator: forbidden summarisation unless redefined as purely navigational; Architect/Outsider/Skeptic: defer or no). Unanimous non-adoption.

6. **Full superseded-spec migration to archive surface.** Rejected (3-of-4 Claude; preserved as Outsider §5.5).

7. **Bulk retroactive migration of all over-threshold raws in Session 022.** Rejected — migration via enumerated-queue-plus-follow-on-sessions (R8d) preserves session-scope rigor.

**Load-bearing minority positions preserved:** §5.1 (Skeptic reject-frame); §5.2 (Outsider top-level archives); §5.3 (Outsider 8K-word budget); §5.4 (Skeptic engine-version cadence); §5.5 (Outsider superseded-spec reclassification). See `01-deliberation.md` §5 for operational warrants.

---

## D-085: OI state housekeeping

**Triggers met:** [none]

**Triggers rationale:** Records OI consequences of D-084 without adding new normative content. OI-004 tally advancement is asserted in this decision but the tally is a consequence of D-084's required-trigger status, not itself a new normative rule. No kernel/spec/MAD/validation-approach revision in D-085 itself. Not operator-marked load-bearing. `[none]` consistent per D-073/D-077/D-079/D-081/D-083 housekeeping precedent.

**Decision:**

1. **OI-002:** tenth data point (R3/R4/R6/R7 all substantive; R5 creation extends narrow-single-purpose-spec pattern to n=4; R9 check additions substantive; multi-spec revision in a single session). The five-point heuristic continues to hold stable. No formal heuristic update this session.

2. **OI-004:** tally advances **7-of-3 → 8-of-3** (D-084 fires d023_1 + d023_2 + d023_3 — eighth required-trigger deliberation with non-Claude participation after Sessions 005, 006, 009, 011, 014, 017, 021). Voluntary:required ratio rebalances **7:7 → 7:8** (required overtakes voluntary for second time in history, after Session 017's 5:6). Criterion-3 cumulative **55 → 60** (five new Outsider contributions this session per §6 synthesis).

   OI-004 **state unchanged at state 3 "Articulated; awaiting closure-retrospective"** per `multi-agent-deliberation.md` v4 §Closure Procedure for OI-004. No closure-retrospective artefact attempted this session; state 3 → state 4 requires separate deliberation.

3. **OI-007:** count **12 → 12** (no OI opened or resolved). Five new first-class minorities (§5.1-§5.5) held at `01-deliberation.md` §5 rather than as new OIs per Session 015/019/020/021 precedent.

4. **OI-015:** Session 022 is a **positive exercise** — the laundering-gap reconciliation clause operated as intended (operator input surfaced verbatim in brief §3; perspectives treated as input; R4 kernel revision is the response to the laundering-at-harness-layer finding). Session 022 adds to OI-015's positive-example column (after Sessions 013, 020, 021). Monitor continues.

5. **Session 022 watchpoints:** WX-22-1 (laundering-as-codification), WX-22-2 (threshold-adjustment discipline), WX-22-3 (engine-version cadence), WX-22-4 (archive-pack location stress test), WX-22-5 (aggregate default-read surface growth) recorded per §7 synthesis.

**Rejected alternatives:**

- Opening a new OI for the read-contract adoption itself (e.g., "OI-018 read-contract adequacy"). Rejected per Session 015/019/020/021 precedent of holding first-class minorities in deliberation §5 with operational warrants rather than creating new OIs.

- Declaring OI-004 advanceable to state 4 this session because criterion-4 now has a richer corroborating example (frame-completion contribution from Outsider). Rejected because OI-004 state advance requires a closure-retrospective artefact per `multi-agent-deliberation.md` v4 §Closure Procedure for OI-004 — Session 022 does not produce that artefact.
