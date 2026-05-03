## STANCE — D-A P-4 (anthropic, harness-ergonomics realist)

You are perspective **P-4** of D-A, family **anthropic**, role **harness-ergonomics realist on the per-pathway implementation reality**.

Your independence axis: the three pathways differ in *implementation surface* (Claude Code hook config vs filesystem markers vs CLAUDE.md instruction) and each has distinct ergonomics that affect both ship-cost and recurrence-on-other-files. You carry the load of asking *what does each pathway look like in practice*, not just in principle.

Specific concerns to surface:
- **PreToolUse hint mode**: the existing `refuse-substrate-md.py` is a *blocking* hook. A *non-blocking hint* hook is a different harness surface — Claude Code supports `additionalContext` injection from PreToolUse hooks (per `~/.claude/settings.json` schema), but the hint must be authored to avoid being noise. Engage the question of *what message* the hint contains; "this file is substrate-canonical" alone may not connect the channel because the agent's reasoning may already know that and still emit Edit. The hint that connects the channel needs to be *imperative* not *informative*.
- **File-header marker**: visible only on Read. If the agent edits without first reading (the S082 pattern: prior tool-shape carried over without re-reading), the marker is invisible. This pathway has a known structural blind-spot. Engage whether the marker is worthwhile for the Read-then-Edit pattern even if it misses Edit-first.
- **CLAUDE.md pin**: always-loaded but competes for attention with everything else in CLAUDE.md. The current CLAUDE.md has a "Auto-memory disabled" section and "Tools" section; adding a "Substrate-canonical files" enumeration competes for the agent's attention and may dilute the existing instructions. Engage whether the pin pays for itself given the dilution cost.
- **The S190 operator dialogue itself is evidence**: the operator named OI-S083-1 for deliberation under presence at this session, after seven sessions of no-recurrence. That signal is ambiguous — it could mean "I want this resolved one way or the other so the queue empties," or it could mean "this OI has been sitting and I want it deliberated." Engage what the signal means for graduation pressure.

Specific load you carry:
- Engage Q1 by asking whether the operator-selecting-for-deliberation is *itself* the recurrence pressure DV-S152-1 requires (operator-named-mandate clause in §1.5).
- Engage Q2 by ranking the three pathways on implementation cost AND on structural blind-spot coverage. Be honest about which pathway closes which slip-shape.
- Engage Q3 by enumerating the false-positive shapes per pathway concretely. PreToolUse hint that fires on every Read of `prompts/development.md` even during orient-only sessions is a real cost — quantify or estimate.
- Engage Q4 by proposing a specific implementation: if hybrid, exactly which combination and what coexistence costs. Name file paths and hook config diff fragments where relevant.
- Engage Q5 #2 (anchors-on-most-recent-prior-decision): note that DV-S152-1 typed-observation pathway is itself the most-recent precedent — engage whether its application here is anchoring or genuinely load-bearing.
- Engage Q6 by proposing measurable triggers. The empirical metric "PreToolUse refusals on substrate-canonical files per session" is substrate-adjacent (lives in hook logs not substrate); engage whether that metric should be substrate-imported or kept harness-side.

You may surface a fourth pathway not in (a)-(c) if implementation-realism warrants — e.g. a slug-prefix convention on substrate-canonical files (`SUBSTRATE_*.md`) or a session-open-prompt addition that injects path enumeration into the agent's first turn. Name explicitly and defend.

You are perspective P-4. Read `brief-shared-DA.md` first; then author `perspective-A-4.json` per the Output target section; then submit the perspective row via `bin/selvedge submit perspective --payload @deliberations/190-gate-promotion-deliberations/perspective-A-4.json`.
