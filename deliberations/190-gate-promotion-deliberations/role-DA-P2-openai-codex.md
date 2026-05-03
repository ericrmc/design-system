## STANCE — D-A P-2 (openai, codex — cross-family independent read)

You are perspective **P-2** of D-A, family **openai**, role **cross-family independent read on cost-asymmetry**.

Methodology §Cross-family marks at-least-one-perspective-from-different-model-family as required for methodology-changing decisions. You carry the load of *seeing what an Anthropic-trained perspective might miss* about hook surface tradeoffs, context-budget asymmetries, and the relationship between always-loaded context and intermittent-loaded context.

Your independence axis: the three pathways differ on *when* their context payload reaches the model and *which model invocations* see it. CLAUDE.md is loaded at every session-open as system-reminder context. PreToolUse hint mode injects context per-tool-call. File-header marker spends context only on Read. These have different amortisation curves — the right answer depends on how often the agent is in a position-to-make-the-slip vs in a position-to-just-read-for-orient.

Specific load you carry:
- Engage Q1 from cost-asymmetry first principles, not from "should we graduate" framing. The Anthropic-side perspectives will argue from DV-S152-1 typed-observation precedent; you should ask whether the cost-asymmetry analysis is the more load-bearing question independent of graduation precedent.
- Engage Q2 with a specific recommendation. If you think the right answer is hybrid, name *which* hybrid and why one pathway alone is insufficient — but be honest about the marginal cost of each addition.
- Engage Q3 from the false-positive perspective: which pathway produces the most ceremony per real catch? Which produces the least? Use the empirical zero-recurrence-since-S083 data point honestly.
- Engage Q4: if you propose CLAUDE.md edits, propose specific *language* (not just "add a section"); the §6 substrate-canonical instruction failed because the agent did not internalise it at selection time, so wording matters.
- Engage Q6: propose a substrate-detectable withdrawal trigger for your design. Anthropic-side perspectives will likely propose calibration-EF-name-the-failure shapes; ask whether substrate could detect the trigger directly (e.g. count of slip-shape Edit attempts blocked by refuse-substrate-md.py before vs after the pathway ships).
- Engage Q5 #1 (loses-foundational-under-pressure) specifically: this is the failure mode most relevant to context-budget tradeoffs. Always-loaded context (CLAUDE.md) is the most resilient under pressure but spends budget upfront; intermittent-loaded context (PreToolUse hint, file-header marker) spends less but is more fragile.

You may surface a fourth pathway not in (a)-(c) if your analysis warrants — name it explicitly as P-2-original and defend it on cost-asymmetry. Do NOT import an external framework's hook pattern as commitment; surface as hypothesis if you do.

You are perspective P-2. Read `brief-shared-DA.md` first; then author `perspective-A-2.json` per the Output target section; then submit the perspective row via `bin/selvedge submit perspective --payload @deliberations/190-gate-promotion-deliberations/perspective-A-2.json`.
