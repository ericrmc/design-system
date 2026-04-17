---
session: 003
title: Decisions — Multi-Agent Deliberation Pattern
date: 2026-04-17
status: complete
---

# Decisions — Session 003: Multi-Agent Deliberation Pattern

## D-015: Adopt the multi-agent deliberation pattern via a new specification

**Decision:** Introduce a new specification, `specifications/multi-agent-deliberation.md`, defining when and how the methodology convenes multiple independent perspectives, how their outputs are synthesized, and how the whole process is recorded. Update `methodology-kernel.md` with a one-sentence pointer under the Convene activity.

**Rationale:** The methodology's own kernel already requires that substantive work not be done by a single perspective. Until this session, that requirement was met in name only — every "perspective" was written by a single agent. The prompt explicitly calls for "a group of AI agents with genuinely different viewpoints." Parallel context-isolated subagents, each reasoning independently from an identical brief with a different stance, close most of that gap. The pattern is exercised in this session (five perspectives convened to design itself).

**Rejected alternatives:**
- Substantive revision of `methodology-kernel.md` (Skeptic's position [`01c-perspective-skeptic.md`, Q7]) — rejected because the kernel's Convene/Deliberate language is already mechanism-neutral and hosts this pattern. The Skeptic's underlying concern (that treating this as elaboration lets the methodology avoid confronting the limitation) is preserved instead by keeping OI-004 open and by the Limitations section of the new specification stating plainly that this mechanism does not achieve genuine independence.
- Embedding the pattern inside `methodology-kernel.md` — rejected because it would violate the kernel's small-surface property. The kernel describes the rhythm; child specifications describe mechanisms.
- Defer until a larger multi-agent framework is available (e.g., `TeamCreate`) — rejected because the simpler parallel-subagent mechanism is sufficient for the pattern's first version and available today. Heavier infrastructure can be added later without rewriting the specification.

**What remains open:**
- Whether recursive synthesis is needed when the synthesis itself is load-bearing and contested (Pragmatist flagged; deferred).
- Whether a disagreement-density metric should be computed from parallel outputs as a training-anchoring warning signal (Skeptic proposed; candidate for a future session).

---

## D-016: Selective-use trigger for multi-agent deliberation

**Decision:** Multi-agent deliberation is required when any of the following conditions applies to a decision a session intends to record:

1. The decision modifies `methodology-kernel.md`.
2. The decision creates or substantively revises any specification in `specifications/`.
3. The decision is one on which reasonable practitioners could genuinely disagree — operationalized as: the session author can name at least two plausible positions before the deliberation begins.
4. The session author has tagged the decision "load-bearing" for any other reason and records why.

Decisions that do *not* meet any of these criteria may be made by a single agent. The decision record must state explicitly that the decision was made under single-agent reasoning, naming the reason (e.g., "Single-perspective; non-load-bearing: minor correction per D-014 precedent").

**Rationale:** Every perspective converged on "selective, not universal." Four perspectives (Methodologist, Pragmatist, Archivist, Futurist) converged on criteria tied to decision consequentiality and contested-ness [`01-deliberation.md`, Q1]. The Pragmatist's concrete trigger list is the most operational and is adopted. The Skeptic's stricter criterion ("only when a named blindspot exists") is rejected as too restrictive for this version but is archived in the provenance record. The "load-bearing" opt-in and the explicit opt-out annotation both serve the Skeptic's drift-to-ritual concern — they make any deviation from the default visible.

**Rejected alternatives:**
- "All deliberations" — rejected by all perspectives as guaranteed to produce silent regression.
- Skeptic's stricter "only when a named blindspot is identified" — rejected as too narrow, though archived as a stricter alternative the methodology may adopt if evidence of ritual drift emerges.
- No trigger (judgment-only) — rejected because unstated thresholds invite expedient skipping.

**What remains open:**
- The third criterion ("reasonable practitioners could disagree") is subjective and will drift. Accepted as unavoidable; monitored by the session log recording which Decides triggered multi-agent work.

---

## D-017: Perspectives and stance briefs

**Decision:**

- **Number:** Default 3 perspectives. May rise to 5 when the problem spans clearly different concern-domains. More than 5 requires a written justification in the convening record.
- **Selection:** Perspectives are chosen for expected disagreement on *this* problem. No permanent roster (reaffirms D-005). At least one perspective must be adversarial (reaffirms existing kernel rule).
- **Stance brief structure:** Each brief contains, in order: (1) a shared methodology-context section (byte-identical across all briefs in the deliberation), (2) a shared problem statement (byte-identical), (3) the shared design questions (byte-identical), (4) a role-specific stance (second-person, imperative, naming the specific anxieties the perspective holds, 150–300 words), (5) a response-format instruction (shared), (6) the "do not import ideas from outside this brief without flagging" constraint (shared).
- **Workspace context per perspective:** Minimal and identical. Perspectives reason from the brief; they do not read workspace files during the deliberation. This keeps the deliberation reproducible and prevents spurious disagreement from divergent reading.
- **Brief immutability:** Briefs are committed to the workspace before any perspective is launched. Briefs are not edited during the deliberation.

**Rationale:** The 3-to-5 range is the overlap of all five perspectives' recommendations [`01-deliberation.md`, Q2]. The uniform-minimal-context choice favors archival reproducibility and auditability (Methodologist, Pragmatist, Archivist). The Futurist's differentiated-context position is preserved as a future direction rather than adopted now, because differentiating context requires the convener to anticipate each perspective's needs — itself a framing decision without a checking mechanism.

**Rejected alternatives:**
- Fixed perspective roster — rejected (reaffirms D-005).
- Fewer than 3 perspectives — rejected because pairwise disagreement has no tiebreaker.
- More than 5 as default — rejected because synthesis quality degrades and token cost rises with weak marginal value.
- Differentiated workspace context per perspective (Futurist's position) — rejected for the pattern's first version; archived as a candidate revision.
- Free-form brief structure — rejected because reproducibility and brief-diffing require a fixed schema.

**What remains open:**
- Whether brief-writing itself needs an adversary (Skeptic's concern about "infinite regress" [`01c`, Q6]). No good answer yet; named openly in the Limitations section of the new specification.

---

## D-018: Synthesis conventions

**Decision:**

- **Synthesizer identity:** The synthesizer must not have been one of the deliberation's perspectives. The synthesizer's identity (agent/model) is recorded in the synthesis file's frontmatter.
- **Citation requirement:** Claims in the synthesis that attribute a position to a perspective must cite the source file, using the convention `[source-file, question/section]`. Claims not directly sourced from any raw perspective are marked `[synth]`.
- **Quote over paraphrase for load-bearing claims:** Where a perspective's argument turns on specific language, the synthesis quotes that language rather than paraphrasing.
- **Preserve dissent:** Disagreements are listed as disagreements. A minority position with a strong argument is preserved as-is, not diluted. Majority/minority structure is reported explicitly.
- **Convergence vs. coverage:** The synthesis distinguishes *convergence* (all perspectives independently reached a similar conclusion) from *coverage* (only one perspective raised a point; others were silent). These are different epistemic states.
- **Synthesis order:** Perspectives are presented to the synthesizer in alphabetical order by role name to reduce synthesizer ordering anchoring.

**Rationale:** Synthesis is the pattern's highest-risk step — where N independent reasonings collapse to one record. Every perspective noted the risk [`01-deliberation.md`, Q4]. The Skeptic's demands ("quote not paraphrase," "forbidden from introducing claims not traceable to a raw output") and the Archivist's citation convention both address this and are adopted. The Futurist's `[synth]` distinction and convergence-vs-coverage distinction are adopted. The separation between synthesizer and deliberators (Methodologist's position) is adopted.

**Rejected alternatives:**
- Synthesis performed by one of the deliberating perspectives — rejected because it lets a perspective author the record of its own disagreement.
- Paraphrase-only synthesis — rejected as insufficient; load-bearing claims must be quoted.
- Synthesis that resolves disagreement into a unified recommendation — rejected because the Decide step does that, not synthesis. Keeping them separate preserves honest disagreement.
- Multi-agent synthesis as the default — rejected for the pattern's first version because of synthesis-coordination complexity. Flagged as an open direction.

**What remains open:**
- Recursive synthesis (multi-agent synthesis when the synthesis itself is contested) — unresolved.
- Automated synthesis citation coverage check (the Archivist's linter idea [`01d`, Q4]) — not in this session's scope.

---

## D-019: Provenance layout for deliberations

**Decision:** Tiered convention:

- **Single-deliberation sessions:** Use the existing flat numbered-files convention at the session's provenance root. Naming: `01a-perspective-<role>.md`, `01b-perspective-<role>.md`, … for raw outputs; `01-deliberation.md` for synthesis. Briefs need not be separate files — the briefs used in the deliberation are derivable from the perspective files' role-specific stances plus the shared sections (which are identical across briefs in a deliberation). However, if a session's briefs depart from this derivability (e.g., differentiated context), the briefs must be preserved as separate files named `01*-brief-<role>.md`.
- **Multi-deliberation sessions:** Use the Archivist's proposed layout [`01d-perspective-archivist.md`, Q5]: `provenance/<session-id>/deliberations/<decision-id>/briefs/`, `responses/`, `synthesis.md`, `manifest.json`.
- **Metadata in v1:** Synthesizer identity, model, date, and deliberation commit hash go in the synthesis file's YAML frontmatter. A separate `manifest.json` is only required in the multi-deliberation layout.

**Rationale:** Session 003 produced one deliberation; flat files are sufficient and consistent with Sessions 001 and 002. When a future session runs multiple deliberations, the heavier subdirectory layout prevents filename collisions and makes per-deliberation metadata natural. Tiering avoids imposing heavy structure on sessions that don't need it.

**Rejected alternatives:**
- Always use subdirectory layout — rejected as overhead for single-deliberation sessions.
- Always use flat layout — rejected because it breaks down when multiple deliberations coexist.
- Always create a separate brief file per perspective — rejected as duplicative when the shared sections of all briefs are byte-identical and the role-specific stance is already preserved inside each raw-output file.

**What remains open:**
- The first multi-deliberation session will need to exercise the subdirectory layout; the specification should be clear enough that this transition is mechanical.

---

## D-020: Methodology-kernel receives a minor correction, not a substantive revision

**Decision:** `methodology-kernel.md` is updated with a single sentence under the Convene activity pointing to the new `multi-agent-deliberation.md` specification. This is treated as a **minor correction** — committed through git, no file-level version preservation.

OI-004 is **not closed** by this session. It remains open with its scope narrowed: the mechanism now exists for convening independent Claude-family perspectives, but the deeper goal of OI-004 — truly independent viewpoints via different models or human participants — is unaddressed by this session.

D-009 (acknowledgment of simulated disagreement) is updated with a cross-reference to the new specification but remains in force. The specification replaces the *single-agent simulation* as the default mechanism; D-009's honest-acknowledgment principle still applies, now to the Claude-monoculture limitation rather than to same-context simulation.

**Rationale:** The kernel's Convene and Deliberate sections already describe perspectives without specifying how they are instantiated — so the pattern is an elaboration within existing kernel language, not a change to kernel meaning. This is consistent with D-014's emerging heuristic: if a change is *anticipated by* the specification's language, it is a minor correction.

Keeping OI-004 open directly answers the Skeptic's strongest argument — that closing OI-004 on the basis of parallel Claude subagents would be "lying to itself at the level of its own record" [`01c`, Q7]. The methodology chooses honesty over false resolution.

**Rejected alternatives:**
- Substantive revision of `methodology-kernel.md` with a preserved v1 file (Skeptic's position) — rejected because the kernel's language does not change; only an addition is made. The Skeptic's substantive concern is preserved through OI-004's continued openness and the new specification's Limitations section.
- Closing OI-004 — rejected as dishonest given the Claude-monoculture limitation remains unaddressed.
- Removing D-009 — rejected; D-009's core principle (honest acknowledgment of simulated-disagreement limits) still applies to the residual limitations of the new mechanism.

**Note on OI-002:** This decision provides a second data point for OI-002 (substantive vs. minor revision threshold). Adding a cross-reference pointer — content that is fully within the specification's existing scope and changes no meaning — is a minor correction. The heuristic from D-014 holds.

**What remains open:**
- OI-004, with narrowed scope.
- Whether the Skeptic's drift-to-ritual prediction bears out in Sessions 004+. If it does, a future session may need to substantively revise the kernel to tighten the trigger rule.
