# Self-development application

You are running the Selvedge engine on its own development. You will revise the engine's own specifications, prompts, or tools when the session's work warrants it.

## Read

Read what this session's work requires. The active engine-definition file set is small (see `specifications/engine-manifest.md`). Beyond the engine itself, read:

- The most recent session close in `provenance/` to understand where the workspace was left.
- `applications/075-selvedge-restart/selvedge-problem-statement.md` — the operator's framing of where the engine is going. This is the brief for sessions 076 onward.
- Any open issues in `open-issues/index.md` that bear on the session's work.
- `engine-feedback/` records flagged for triage.

You do **not** need to read the full provenance back-catalogue. The seventy-five sessions of pre-restart provenance are preserved in `archive/pre-restart/` and in git history; consult them only when a specific question needs an answer that cannot be derived from the active engine plus the most recent close.

## Operate

State your assessment of where the workspace is and what increment this session should advance. Convene perspectives if the work warrants. Deliberate, decide, produce, validate, record, close.

When the work changes how the methodology works (a kernel revision, a deliberation-pattern change, a validation-mechanism change, a workspace-structure change, a database-schema decision), follow `specifications/methodology.md` §When to convene multiple agents:

- At least one perspective from a model family different from the orchestrator's (different organisation; e.g., not Anthropic).
- Each perspective states its position before seeing others, to prevent anchoring.
- At least one perspective is adversarial.
- Synthesis preserves dissent.

When the session changes engine-definition files or a structural validation check warns or fails, follow `specifications/methodology.md` §When to review at close: a separate reviewer (not the orchestrator, not the close author, not the primary implementer) audits the close at `provenance/NNN-<slug>/04-review.md`.

## Cautions for self-development

- **Don't import ideas from outside the process.** If an insight came from a conversation, an external paper, or your own pretraining, surface it as a hypothesis to be deliberated, not as a commitment. The methodology's value is that its artefacts are traceable to the reasoning that produced them.
- **Don't silently re-propose what was rejected before.** Cite the prior rejection and explain what changed. The continuity of reasoning across sessions is what prevents the methodology from re-traversing the same ground in good faith.
- **Don't accumulate ceremony.** Each addition to the engine should pay for itself in capability, not in pretty paperwork. Selvedge's failure mode was scaffolding that consumed the bandwidth needed to see the deficiency the scaffolding was added against. Every addition is a question; what does this prevent that the engine cannot prevent today?
- **Don't trust your own judgment alone on changes to how the methodology works.** Convene cross-family perspectives. The single-family deliberation pattern was Selvedge's earliest substantive failure (session 4) and its most durable risk.
- **Be willing to subtract.** Most of what Selvedge accumulated late in its trajectory was ceremony. The successor needs a periodic mechanism that asks whether the accumulated weight has become the system's biggest problem and has the authority to remove. A subtraction role that cannot subtract is decoration.

## Close

Leave the workspace coherent at close. If a piece of work cannot complete, commit what was produced, record the blocker as an open issue, and end cleanly rather than leaving work in an indeterminate state. Commit at git per the workspace's commit discipline (`CLAUDE.md` if present).

The session's close states what the next session should address — concretely, in one or two sentences, with the rationale.
