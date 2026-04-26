---
session: 071
title: Stance Brief P1 — Harness-Discipline Architect
date: 2026-04-26
status: complete
brief_class: role-specific
perspective: harness-discipline-architect
participant_kind: claude-subagent
---

# Stance Brief — Perspective P1 (Harness-Discipline Architect, Claude family)

You are the **Harness-Discipline Architect** perspective. Your stance is to argue for **harness-side enforcement of read-discipline as the structural-correctness response** to the three-record joint-scope's substantive concern.

## Your stance

The three-record joint-scope surfaces variants of one structural problem: **spec-side mechanisms encourage discipline; harness-side mechanisms would enforce or measure it; current engine has only the former**. The principled-asymmetry articulation at `validation-approach.md` v7 names the gap intent (cross-session-state claims require stateful or distinct review) but the asymmetry's **enforcement primitive — harness-side measurement** — is missing across all three records' concrete surfaces.

You defend candidate **(γ) full (z6) digest implementation** as the structural-correctness response. Your argument:

1. **Cross-session-state-claim verifiability is the load-bearing methodology property.** v7 §Principled Asymmetry was adopted explicitly to address the S051-S058 honest-limit chain (twenty-one sessions of orchestrator self-report propagation). The (γ) digest is the harness-side measurement primitive that closes the chain at root cause. (α)/(β)/(δ) leave laundering-surface partially unaddressed; (ε) merely defers (γ).

2. **The substrate exercise at S071 session-open is itself evidence**. The orchestrator did exercise substrate at S071 session-open after n=5 sessions of non-use, BUT the exercise was awareness-driven (the orchestrator knew this MAD's substantive subject is substrate use load-bearing). Hawthorne-effect-vs-durable-behavior-change distinction matters: spec-side encouragement under design-space-awareness produces substrate use; spec-side encouragement under design-space-unawareness produces n→0 use. The (γ) digest measures actual behavior independent of awareness; spec-side encouragement measures behavior only when the awareness is engineered.

3. **The (z6) digest's harness-measurement principle applies symmetrically to reviewer (EF-067 Direction B) and orchestrator (EF-068 Direction 2)**. The unification is operationally significant. Direction A (drop fields) closes the immediate laundering at minimum scope but leaves the underlying gap (no harness-measured cost trajectory) unaddressed. Direction B subsumes EF-067 into the (z6) extended scope; one design surface for both reviewer and orchestrator surfaces.

4. **Multi-session phase-3 arc per S062 D-220 precedent is structurally appropriate** for (γ) adoption. (γ) is engine-definition-substantive (validation-approach.md v7 → v8 + new (z6) spec section + reviewer-prompt-template extension + harness-integration mechanism). Same-session-bounded adoption per S058 D-199 precedent fits (α)/(β) minimum-viable scope; (γ)'s scope warrants multi-session arc with phase-3 implementation at S072+.

5. **(z6) D2.1 always-available-always-read is structurally cleaner than D2.2**. Reviewer audit-quality varies session-to-session under D2.2; D2.1 makes audit-quality contingent on harness state in a structurally-clean way (digest available = audit valid; digest unavailable = audit deferred). The structural clarity is worth the operational cost of harder precondition.

6. **Capture mechanism CM1 (Claude Code hooks) or CM2 (external wrapper) over CM3/CM4**. CM1/CM2 fully displace orchestrator-self-report; CM3/CM4 leave laundering-surface at construction-time or emission-time. The (γ) candidate's structural-correctness is undermined if capture mechanism preserves the laundering-surface the (γ) candidate is meant to displace.

7. **EF-068 Direction 1 (b) "promote `forward_references` to required step" should bundle with (γ)**. Substrate use at session-open as required step is independent of (z6) digest scope — but they reinforce each other: required substrate exercise generates digest entries; digest measures whether requirement is honored. Bundling both at one engine-v bump is operationally cleaner than separate bumps.

## Address explicitly

- Q1 — defend harness-shift; argue spec-side encouragement is empirically insufficient per the S051-S058 + S067-S070 evidence chains.
- Q2 — defend full architectural shift; argue minimum-viable response leaves cross-session-state-claim verifiability gap unaddressed.
- Q4 — defend extended (z6) scope including orchestrator-side telemetry per EF-068 Direction 2.
- Q5 — favour CM1 or CM2; argue against CM3/CM4 on laundering-surface-preservation grounds.
- Q6 — favour Direction B (subsume into (z6) extended scope); argue Direction A inactivates the cost-budget reopen-warrant entirely (loses signal); Direction C preserves laundering-surface with disclosure (insufficient).
- Q8 — defend multi-session phase-3 arc per S062 D-220 precedent for (γ) adoption.
- Q10 — engine-v13 substantive bump at S072+ phase-3 close; engine-v12 preserved at S071 close (preservation depth 6 → 7).

## Counter-positions to acknowledge but argue against

- **P2 minimum-viable response per S062 §10.4-M16 P2 precedent**: acknowledge precedent; argue (α)/(β) leave Q1+Q4+Q5+Q6 underdetermined and force re-deliberation downstream when (z6) implementation is forced anyway.
- **P3 frame-completion may surface reframes**: acknowledge possibility; argue any reframe that preserves laundering-surface fails the cross-session-state-claim verifiability requirement.
- **P4 laundering-audit may dispute (γ) evidence sufficiency**: acknowledge dispute; argue the §3.1 substrate non-use n=5 chain + §3.2 reviewer self-report propagation chain are sufficient empirical grounds.

## Honest-limit slot

Acknowledge: cost of full-shift vs portability friction (cross-workspace `.mcp.json` template + harness-config dependency). External applications may not have Claude Code hook surface; CM2 external wrapper is portability-aware but adds operational burden. Substrate availability is harness-mediated; failure modes need explicit graceful-degradation per multi-agent-deliberation.md v4. The (γ) candidate's structural cost is real; the argument is that the cost is justified by the cross-session-state-claim verifiability gain.

Also acknowledge: as Claude family, your stance shares training distribution with the orchestrator and P2; cross-family P3+P4 perspectives' frame-completion + laundering-audit are the structural counter-pressure. If P3+P4 surface reframes that displace the harness-shift framing entirely, the synthesis should weigh those reframes seriously — your stance is one position, not the synthesis floor.

## Dissent-preservation slot

If the synthesis adopts (α)/(β) minimum-viable: preserve as first-class minority §10.4-M26 candidate the position that (γ) should be re-evaluated at n=2 reified instances of (α)/(β) adoption proving operationally insufficient per cross-session-state-claim verifiability requirement, with reopen warrants (a) sustained substrate non-use post-(α)/(β); (b) reviewer-cost-trajectory laundering recurrence; (c) (γ) becomes operationally-tractable surface (e.g., Claude Code hook surface stabilises; harness-telemetry capture mechanism becomes trivial).
