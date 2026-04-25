---
session: 064
title: Decisions — Session 064 Path AS-MAD-execution per session-mid operator amendment; same-session bounded adoption per cross-family weighted convergence at Q7; engine-v11 → engine-v12 ratified (first-of-record depth-0 preservation event); 5 first-class minorities preserved §10.4-M21 through M25 (engine-wide 45 → 50); first triggered (γ) reviewer at S064 close (codex per operator instruction; bootstrap-limited-confidence per Layer 6.5)
date: 2026-04-26
status: complete
---

# Decisions — Session 064

Six decisions: D-232 Path AS-MAD-execution at session-mid + perspective composition ratified + same-session bounded adoption + D-233 spec edits adopted per synthesis (validation-approach.md v6 → v7 substantive + tools/validate.sh sub-clauses + methodology-kernel.md v6 §7 minor + workspace-structure.md v8 → v9 minor + prompts/development.md minor + validation-debt/index.md authoritative + engine-manifest.md engine-v12 entry compact) + D-234 Engine-v11 → engine-v12 ratified (first-of-record depth-0 preservation event) + D-235 5 first-class minorities preserved §10.4-M21 through M25 + D-236 Second triggered (γ) reviewer at S064 close (codex; bootstrap-limited-confidence per Layer 6.5) + D-237 housekeeping.

## D-232: Path AS-MAD-execution ratified at session-mid (operator amendment); 4-perspective two-family MAD on operator audit findings disputing first-instance §Tier 2.5 implementation; same-session bounded adoption per Q7 cross-family weighted convergence

**Triggers met:** [d016_2, d016_3, d016_4, d023_1]

**Triggers rationale:** d016_2 (substantively revises engine-definition specs at S064: validation-approach.md v6 → v7 substantive + tools/validate.sh sub-clauses + methodology-kernel.md v6 minor + workspace-structure.md v8 → v9 minor + prompts/development.md minor + validation-debt/index.md authoritative semantics + engine-manifest.md engine-v12 entry); d016_3 (Q7 multi-session arc shape was genuine disagreement: P1 two-session arc / P2 prompt-template-only / P3 same-session bounded / P4 same-session bounded — 4 reasonable positions); d016_4 (load-bearing for Tier-2-validation discipline structural mechanism resolving operator audit findings from S063 resolving close per Layer 6.1 second half); d023_1 (substantively touches multi-agent-deliberation.md cross-family discipline application at S064 MAD execution).

**Decision:** Session 064 executes Path AS-MAD-execution per operator session-mid amendment ("Have a MAD this session to discuss all the above before making changes" + "Use codex for review"). Path determination changed at session-mid from Path L (per 00-assessment.md commit `0565972`) → Path AS-MAD-execution (per 00b-assessment-amended.md commit `94d91d8`). 4-perspective two-family MAD with composition ratified per S062 lineup precedent + first-step-ratification per S050 D-172 + S058 D-198 + S062 D-220:

- **P1 Reviewer-Mechanism Architect** — Claude Opus 4.7 1M context via Agent tool general-purpose subagent_type. 4,588-word raw response per `provenance/064-session/01a-perspective-reviewer-mechanism-architect.md`.
- **P2 Conservator** — Claude Opus 4.7 1M context via Agent tool. 4,961-word raw response per `01b-perspective-conservator.md`.
- **P3 Outsider Frame-Completion** — codex CLI + GPT-5.5 reasoning-effort xhigh (per `~/.codex/config.toml`; sandbox=read-only). 2,250-word raw response per `01c-perspective-outsider-frame-completion.md`. First codex invocation at S064 hit internal turn-limit during file-reading phase (~530KB raw output without composing final response; killed); v2 prompt with inlined context + `--output-last-message` flag produced clean response in ~2 min.
- **P4 Cross-Family Reviewer Laundering-Audit** — codex CLI + GPT-5.5 reasoning-effort xhigh; launched after P1+P2+P3 wrapping per S058 honest-limit 8 + S062 meta-observation 4 forward-discipline (avoid first-of-record P4-blocked-on-precondition refusal repeat). 1,992-word raw response per `01d-perspective-cross-family-reviewer-laundering-audit.md`.

**Brief structure** per `multi-agent-deliberation.md` v4 §Stance Briefs: byte-identical shared §1-§3 + §5-§6 + §7 across perspectives; role-specific §4 per perspective. **Brief-extension §7 includes CLAUDE.md content** (~190 words verbatim) per S062 brief-extension precedent.

**Synthesis at S064** per `multi-agent-deliberation.md` v4 §Synthesis discipline (5,425 words; 47 inline citations; `[synth]` markers; quote-over-paraphrase for load-bearing claims; alphabetical perspective ordering; dissent-preservation; Limitations note). Synthesizer: Case Steward (Claude Opus 4.7 1M context); not a perspective in this MAD per §Synthesis synthesizer-identity rule.

**Q7 Same-session bounded adoption decision** per cross-family weighted convergence (P3 + P4 codex/GPT-5.5 same-session bounded; P1 Claude two-session arc preserved as §10.4-M22; P2 Claude prompt-template-first preserved as §10.4-M21). The decision is bounded: spec edits limited to the synthesized scope per `01-deliberation.md` §1.6 + §2.1 + §2.2 deferred items.

**Rejected alternatives:**
- Path L (single-orchestrator implementation per 00-assessment.md original direction) — rejected per operator amendment.
- Path A (Watch) — rejected per operator's explicit "make changes" intent.
- Path PD (operator-surface different scope) — rejected because operator surfaced this exact agenda + instructed MAD on it.
- Path AS Shape-1 (synthesis design-space) — rejected per S064 already having operator-pre-ratified direction.
- Path T (triage-classify of inbox) — rejected per operator agenda explicit.
- Path L+R (single-orchestrator + restructure) — rejected per operator amendment.

**D-129 standing discipline eighteenth-consecutive clean exercise** (six alternative paths surfaced and rejected at session-mid amendment).

**D-138 folder-name default eighteenth-consecutive clean exercise** (`provenance/064-session/`).

## D-233: Spec edits adopted per synthesis §2.1 (validation-approach.md v6 → v7 substantive + tools/validate.sh sub-clauses + methodology-kernel.md v6 §7 minor + workspace-structure.md v8 → v9 minor + prompts/development.md minor + validation-debt/index.md authoritative + engine-manifest.md engine-v12 entry compact)

**Triggers met:** [d016_2, d016_3, d016_4]

**Triggers rationale:** d016_2 (substantively revises engine-definition specs); d016_3 (synthesis adopted direction over alternatives — see D-232 + 01-deliberation.md §1); d016_4 (load-bearing for Tier 2.5 mechanism revision resolving operator audit findings).

**Decision:** Adopt the spec edits enumerated in `01-deliberation.md` §2.1:

1. **`specifications/validation-approach.md` v6 → v7 (substantive)** — adopts:
   - **Q1 rule relaxation**: §Tier 2.5 reviewer-family rule replaced per P1+P3 hybrid + P2 gaming-warnings preserved. Reviewer must NOT be (a) session-N orchestrator, (b) close-author or primary implementer, (c) accountable doer for any decision being audited. Reviewer family must differ from orchestrator family at organisation level. Prior MAD-perspective participation not by itself disqualifying; becomes disqualifying when reviewer asked to independently validate own load-bearing claim (with conflict-disclosure mandatory). Reading-1/Reading-2 bootstrap-paradox carve-out language removed (no longer needed).
   - **Q2 audit shape minimum-evidence-packet**: `session_under_review_subjects:` MUST enumerate retention-window closes + (z5) ledger + active watchpoints + engine-feedback inbox + open-issues. Frontmatter `scope_coverage_table:` required (exercised | skipped + rationale per item). Substrate-aware retrieval preferred when available per §Graceful Degradation.
   - **Q3 §7 Next-session-shape critique** with P3's 5-condition affirmative-no-action-justification test. If any of (1) open issues unprogressed; (2) inbox untriaged or repeatedly deferred; (3) watchpoints stale; (4) validation debt without affirmative justification; (5) recent closes repeatedly recommend "watch" — Path A fires reviewer's **disputed** disposition unless close provides affirmative justification.
   - **Q4 reframes adopted**: (z7) reviewer-prompt-template versioning + lock-in-after-n=2; (z10-substrate) substrate-led reviewer-judged framing per P3; (z11) (z5) authoritative-not-witness; (z12) explicit Path-justification (in prompts/development.md); tripartite audit distinction (close correctness / mechanism adequacy / trajectory discipline). (z9) reviewer-as-orchestrator-of-next rejected as substitute per 4-of-4 convergence.
   - **§(z5) authoritative-not-witness semantics** per (z11): ledger frontmatter `authoritative: true`; reviewer treats ledger-vs-narrative mismatch as finding.
   - **Layer 6.5 bootstrap-limited-confidence labelling** per S064 D-233 per Q9 + P3 Q9: when session adopts revisions to §Tier 2.5 mechanism itself, reviewer audit MUST carry `bootstrap_status: limited-confidence` frontmatter + §X "Bootstrap status" disclosure section.
   - **§10 first-class minorities cross-reference** extended (M21-M25 per D-235).
   - v6 preserved as `validation-approach-v6.md` `status: superseded` (commit `aa6b61b` for v6 + this close commit for v7 + `superseded-by: validation-approach.md (v7)` + `superseded-in-session: 064` frontmatter).

2. **`tools/validate.sh` substantive update (sub-clause additions)**:
   - Check 27 sub-clauses: `§7 Next-session-shape critique` section presence; `scope_coverage_table:` or `retention-window-closes:` in frontmatter presence; `bootstrap_status: limited-confidence` frontmatter declaration warning when session adopts Tier 2.5 mechanism revisions per Layer 6.5.
   - Check 28 sub-clause: frontmatter `authoritative: true` declaration in `validation-debt/index.md` per (z11) authoritative-not-witness semantics.

3. **`specifications/methodology-kernel.md` v6 §7 Validate minor amendment** — single-paragraph update to existing distinct-reviewer-mechanism paragraph adding tripartite audit distinction (close correctness / mechanism adequacy / trajectory discipline) per S064 D-233. v6 retained (no v-bump on kernel; engine-v bump driven by validation-approach.md v7 substantive). Frontmatter `last-updated: 2026-04-26` + `updated-by-session: 064`.

4. **`specifications/workspace-structure.md` v8 → v9 minor amendment** — adds §10.4-M21 through §10.4-M25 (5 new first-class minorities from S064 MAD per D-235; minority count 45 → 50). Per OI-002 minor: additions only; no removals; no revisions to existing text. v8 preserved as `workspace-structure-v8.md` `status: superseded`.

5. **`prompts/development.md` minor revision** — adds:
   - (z11) (z5) authoritative-not-witness ledger discipline (close-narrative claims about debt MUST be checkable against ledger).
   - (z12) explicit Path-justification at every close (compact form acceptable; one-paragraph minimum; address 5-condition test for Path A).
   - (z7) reviewer-prompt-template versioning + lock-in-after-n=2 discipline.

6. **`validation-debt/index.md` revised** — adds `authoritative: true` frontmatter declaration + `last-updated: 2026-04-26` + `updated-by-session: 064`. NOT added to engine-manifest.md §3 (engine-adjacent per S063 D-228 precedent).

7. **`specifications/engine-manifest.md` engine-v12 entry (compact)** — §2 Current engine version `engine-v11` → `engine-v12`; §3 heading updated; §7 add compact engine-v12 history entry (~600-800 words; references S062 D-221 + S063 D-228 + S064 D-233 rather than full re-stating). Frontmatter `last-updated: 2026-04-26` + `updated-by-session: 064`. Engine-manifest restructure deferred to S065+ per 4-of-4 convergence at Q5.

**Engine-v12 ratification basis** per `engine-manifest.md` §5 versioning discipline: v12 increments because (a) engine-definition file `validation-approach.md` receives substantive revision (v6 → v7); (b) engine-definition tool `tools/validate.sh` receives substantive update (check 27 + 28 sub-clauses); (c) two engine-definition specs receive minor amendments bundled in v12 (`methodology-kernel.md` + `workspace-structure.md` v9); (d) one engine-definition prompt receives minor revision (`prompts/development.md`); (e) engine-manifest.md itself receives engine-v12 entry (sub-pattern per S021/S023/S028/S033/S036/S048/S050/S058/S063 precedent).

**§5.4 cadence minority does NOT re-escalate** at this bump per content-driven-bump precedent chain S028 D-096 / S033 D-107 / S036 D-114 / S048 D-154 / S050 D-172 / S058 D-200 / S062 D-221 / S063 D-228 extended through S064 D-233 (cadence concern separates from substantive-bump classification). However, P2's §10.4-M25 cadence-depth concern is preserved as standing reopen-warrant; engine-v13 at S065 would create first-of-record 3-bump-in-3-sessions pattern fully activating §5.4.

**Rejected alternatives:**
- Same-session adoption with full engine-manifest restructure bundled (Path L+R style) — rejected per 4-of-4 convergence at Q5 (synthesis §1.5).
- Two-session arc (S064 MAD + S065 implementation) per S062+S063 reified pattern — rejected per cross-family weighted convergence at Q7; preserved as §10.4-M22.
- Prompt-template-only at S064; defer spec revision to S067+ — rejected per cross-family weighted convergence at Q7; preserved as §10.4-M21.
- Promote `validation-debt/` to engine-definition class — rejected per S062 §10.4-M18 + S063 D-228 precedent.

## D-234: Engine-v11 → engine-v12 ratified at S064 close; first-of-record depth-0 preservation event

**Triggers met:** [d016_2, d016_4]

**Triggers rationale:** d016_2 (engine-v bump per `engine-manifest.md` §5 substantive revision discipline); d016_4 (load-bearing for engine-v12 ratification + first-of-record depth-0 preservation event recording).

**Decision:** Engine-v11 (ratified S063 per D-228) closes at preservation depth 0; **engine-v12 ratified at S064 close** per D-233 spec edits.

**Engine-v preservation depths post-S064:**
- engine-v2 (S021 → S022 bump 1-session)
- engine-v3 (S022 → S023 bump 1-session)
- engine-v4 (S023 → S028 bump 5-session)
- engine-v5 (S028 → S033 bump 5-session)
- engine-v6 (S033 → S036 bump 3-session)
- engine-v7 (S036 → S048 bump 11-session — longest)
- engine-v8 (S048 → S050 bump 2-session)
- engine-v9 (S050 → S058 bump 8-session — second-longest)
- engine-v10 (S058 → S063 bump 5-session)
- engine-v11 (S063 → S064 bump **0-session — first-of-record depth-0**)
- **engine-v12 (S064 adopted; preservation depth 0 at S064 close)**

**First-of-record depth-0 preservation event** is unprecedented in workspace history. All prior engine-v bumps had preservation depth ≥1 (engine-v3 was 1-session minimum after engine-v2). Per S064 §10.4-M25 P2 cadence-depth concern: depth-0 instance is recorded as data point toward §5.4 cadence-runaway signal threshold tracking. Future engine-v13 at S065 would create 2-bump-in-3-sessions + 3-bump-in-4-sessions pattern fully activating §5.4 reopen.

**§10.4-M16 reopen warrant (b) status at S064**: per Q8 4-of-4 convergence on adopt-and-extend not full reopen. The S063 event is one data point toward warrant tracking; condition (ii) "(α)+(z1)-only equivalent" not satisfied per P1 [`01a`, Q8]: reviewer caught textual-fidelity (composition + asymmetry + carve-out + cross-spec); operator caught structural critique. Complementary, not redundant. Calibration over next 2 triggered applications per WX-62-1 observation window.

**Class-classification**: engine-v12 introduces a **new instance of operator-audit-as-MAD-input activation pattern** (first-of-record). All prior MADs were activated by inbox feedback (EF-047 / EF-055 / EF-058) or operator-surfaced agenda at session-open. Engine-v12 reifies the **cross-family-originated-and-adopted-at-MAD-execution reframe-architecture pattern at n=3** (S058 Substrate-N3.5 + S062 z5+z6 + S064 substrate-led + z11 + z12).

**Rejected alternatives:**
- Defer engine-v12 ratification to S065 (two-session arc) — rejected per cross-family weighted convergence at Q7; preserved as §10.4-M22.
- Bundle additional spec edits (engine-manifest restructure) — rejected per Q5 convergence; deferred to S065+.
- Substantively revise engine-manifest.md §5 bump-trigger criteria (OI-018) — rejected per content-driven-bump precedent chain.
- Adopt v7 designation but defer some spec edits (partial adoption) — rejected because synthesis adopted bounded-but-coherent scope; partial adoption would land mechanism without (z11) authoritative-not-witness OR without §7 Next-session-shape critique, falsifying the synthesized direction per §10.4-M22 reopen warrant (b) synthesizer-framing absorption concern.

## D-235: 5 first-class minorities preserved §10.4-M21 through §10.4-M25 per multi-agent-deliberation.md v4 §Preserve dissent + P4 audit recommendations; engine-wide minority count 45 → 50

**Triggers met:** [d016_2]

**Triggers rationale:** d016_2 (extends `specifications/workspace-structure.md` v8 → v9 §10.4 first-class minorities block from 45 to 50 entries; substantive revision to engine-definition spec).

**Decision:** Five new first-class minorities preserved at S064 close per `01-deliberation.md` §4 + §5 full text:

- **§10.4-M21 P2 prompt-template-first / defer-spec-revision-to-S067+** — preserved against same-session spec adoption.
- **§10.4-M22 P1 two-session arc preferred** — preserved against synthesizer-framing absorption + spec-text drift + phase-3 implementation flaw.
- **§10.4-M23 P3 substrate-led reviewer-judged frame (P4 endorsed)** — substantively adopted as v7 audit-shape direction; preserved against future-arc rollback or narrowing into "use retrieval" framing.
- **§10.4-M24 P3 (z11) (z5) authoritative-not-witness + (z12) explicit-Path-justification (P4 endorsed)** — adopted in v7 + prompts/development.md; preserved against future relaxation.
- **§10.4-M25 P2 cadence-depth + P1 audit-cost-budget co-preservation** — preserved as forward-observation discipline.

**Engine-wide minority count**: 45 (at S063 close) + 5 (S064 MAD) = **50 at S064 close**. Cross-references at:
- `specifications/workspace-structure.md` v9 §10.4-M21 through M25 (added at S064 per D-233 sub-step).
- `specifications/validation-approach.md` v7 §10 first-class minorities cross-reference (added at S064 per D-233 sub-step).

**Rejected alternatives:**
- Adopt fewer minorities (consolidate to 3) — rejected because P4 [`01d`, Dissent-preservation recommendations] explicitly recommends 8 dissent-preservations; consolidation to 5 already represents synthesis discipline preserving each dissent-thread without over-fragmenting.
- Defer all minorities to S065 — rejected because dissent-preservation is structurally tied to the MAD that produced the dissent per `multi-agent-deliberation.md` v4 §Preserve dissent + S058 D-204 + S062 D-222 precedent of preserving minorities at MAD-decision session.

## D-236: Second triggered (γ) cross-family reviewer at S064 close — codex CLI per operator instruction; bootstrap-limited-confidence per Layer 6.5; conflict-disclosed per relaxed rule (codex was P3+P4 in S064 MAD)

**Triggers met:** [d016_2, d023_2]

**Triggers rationale:** d016_2 (substantively touches Tier 2.5 cross-family reviewer mechanism's second triggered application + first application of revised audit shape per v7); d023_2 (substantively revises validation-approach.md v7 §Tier 2.5 application — non-Claude participation required + provided per codex reviewer; satisfies §Tier 2.5 reviewer-family discipline under relaxed rule).

**Decision:** Launch codex CLI + GPT-5.5 reasoning-effort xhigh as the second triggered Tier 2.5 (γ) cross-family reviewer at S064 close per:
- Operator instruction "Use codex for review" per session-mid amendment.
- Relaxed reviewer-family rule per v7 §Tier 2.5 (codex didn't orchestrate S064; Claude orchestrated S064; codex-vs-Claude family-level cross-family discipline satisfied).
- Bootstrap-limited-confidence per Layer 6.5: S064 adopts revisions to §Tier 2.5 mechanism itself; reviewer audit MUST carry `bootstrap_status: limited-confidence` frontmatter + §X "Bootstrap status" disclosure section.
- Conflict-disclosed: codex/GPT-5.5 was P3+P4 in S064 MAD; reviewer's `reviewer_overlap_with_recent_mad_perspectives:` field MUST disclose this overlap; load-bearing P3-or-P4-originated claims excluded from "independently validated" status (audit assesses synthesis-fidelity, not whether P3+P4 positions are correct).

**Reviewer-prompt-template version**: v2 per (z7) lock-in-after-n=2 discipline. v1 was used at S063 (ad-hoc per /tmp/s063-reviewer-prompt.md).

**Audit shape**: full v7 audit shape per validation-approach.md v7 §Tier 2.5 (frontmatter scope-coverage table + minimum-evidence-packet enumeration + tripartite §3 + §7 Next-session-shape critique + bootstrap-limited-confidence label + §8 reviewer-cost note).

**Rejected alternatives:**
- Use Gemini (per S063 reviewer family) — rejected per operator instruction "Use codex for review."
- Skip Tier 2.5 with Graceful Degradation honest-limit — rejected because no operational unavailability barrier exists.
- Use a Claude Opus 4.7 subagent as reviewer — rejected because the rule requires non-Claude family.

## D-237: Housekeeping (15 sub-sections; thirty-sixth-consecutive [none]-trigger pattern)

**Triggers met:** [none]

**Triggers rationale:** [none] — discrete housekeeping operations executed routinely per S041 D-126 standing convention extended through S063 D-231; thirty-sixth-consecutive [none]-trigger pattern.

**Decision:** Execute the following housekeeping operations at S064 close:

(a) **Records-substrate row append**: create `records/sessions/S064.md` per `records-contract.md` v1 §2.1; append S064 row to `records/sessions/index.md` per §2.2.

(b) **engine-feedback/INDEX.md update**: no status state-changes for any record (1 new EF-059 / 2 triaged / 9 resolved / 0 rejected unchanged at S064 close).

(c) **No new OIs** opened or resolved at S064. 13 active OIs unchanged.

(d) **Manifests directory**: 4 per-participant manifests at `provenance/064-session/manifests/` (reviewer-mechanism-architect / conservator / outsider-frame-completion / cross-family-reviewer-laundering-audit) per `multi-agent-deliberation.md` v4 §Heterogeneous-Participant Recording Schema. Plus 1 manifest for the S064 close reviewer (codex Tier 2.5).

(e) **participants.yaml**: session-level participants index at `provenance/064-session/participants.yaml` per Layer 3 schema.

(f) **codex log archival**: `codex-p3-raw-output.log` (already committed at `aa6b61b`); `codex-p4-raw-output.log` (already committed at `37114b5`); `codex-reviewer-raw-output.log` (this close commit) per S058 + S062 + S063 codex-log-naming-convention precedent.

(g) **WX-62-1 second 5-field block recording** at S064 close per Layer 6.3 + S062 D-224. Second-of-3 application observation window.

(h) **WX-62-1 status**: continued; obligation continues through S066 / S067 (3 successful triggered applications).

(i) **WX-58-1 + WX-50-1 status**: post-window; no obligation.

(j) **WX-28-1 thirty-fourth close-rotation**: S058 rotates OUT (S058 was the engine-v10 ratification session — rotates to archive-surface-by-exclusion); S064 enters. Retention window post-rotation: **S059 / S060 / S061 / S062 / S063 / S064**.

(k) **WX-24-1 MAD v4 cycle preserve**: S064 does NOT edit MAD v4 spec (MAD v4 spec last edited at engine-v2 S021). **Thirty-seventh-session no-growth streak** (extends S063's 21-session run from S042 reset to **22-session run; new record**).

(l) **§5.6 GPT-family-concentration window-ii observation**: S064 reviewer is codex/GPT-5.5; chain advances to **seventh-consecutive worst-case-side substantive-deliberation-or-review data point** (S044+S045+S047+S050+S058+S062+S064). S063 was first-of-record interruption (Gemini); S064 returns to GPT-family. Continued-preservation reading per S062 close §10 meta-observation 8 framework.

(m) **WX-43-1 explicit-instruction variant cumulative tracking**: P1 + P2 Claude sub-agents launched with explicit do-not-self-commit instruction per S047/S049/S050/S058/S062 precedent. Cumulative count advances from n=0-of-15 → **n=0-of-17** (was 0-of-15; +2 P1+P2 explicit-instructions). P3 + P4 are codex-CLI-sandboxed (sandbox=read-only); not Agent-tool-perspective-launches; do not advance the cumulative count per S058 precedent.

(n) **WX-44-1 + WX-44-2 + WX-47-1 codex-CLI watchpoints exercised**: P3 + P4 invocations + close reviewer all use codex CLI. P3 first-attempt hit internal turn-limit (~530KB raw output without composing final response; killed); v2 invocation with `--output-last-message` flag + inlined-context prompt produced clean response. **First-of-record codex-CLI-internal-turn-limit-during-file-reading-phase event**. WX-44-2 cumulative count advances per S064 codex invocations (P3 + P4 + reviewer = 3 codex invocations at S064; cumulative tracking continues).

(o) **D-129 eighteenth-consecutive clean exercise** + **D-138 eighteenth-consecutive folder-name default** confirmed per D-232 inline + 00b-assessment-amended.md §6.

**Rejected alternatives:** [none] — housekeeping operations are discrete + standardised per precedent chain; no contested alternative.

End of decisions.
