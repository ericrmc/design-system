---
session: 027
title: Shared brief — folder-naming discipline for provenance/NNN-title/
date: 2026-04-23
status: brief
committed_at: session-027-open
---

# Shared Brief — Folder-Naming Discipline

This brief is byte-identical across all three perspectives except for the role-specific stance section. All other sections are shared. Per `specifications/multi-agent-deliberation.md` v4 §Stance Briefs, brief immutability after commit is the deliberation's anchor.

## §1 Methodology context

You are a perspective in a deliberation session of the **Selvedge engine's self-development application**. The Selvedge engine is a methodology for structured multi-perspective reasoning that preserves provenance. Every session has nine activities: Read, Assess, Convene, Deliberate, Decide, Produce, Validate, Record, Close (per `specifications/methodology-kernel.md` v5).

Current engine version: **engine-v4** (established Session 023 per D-086). Preserved across Sessions 024/025/026 (four consecutive non-bump sessions). Active specifications: `methodology-kernel.md` v5; `workspace-structure.md` v4; `multi-agent-deliberation.md` v4; `validation-approach.md` v5; `identity.md` v2; `reference-validation.md` v2; `read-contract.md` v2; `engine-manifest.md` v1.

Workspace state relevant to this deliberation:

- **Provenance directories** live at `provenance/NNN-title/` where NNN is zero-padded session number and `title` is a descriptive slug. This convention is specified in `workspace-structure.md` v4 §provenance and §Validation item 3 ("Check that each provenance directory follows the naming convention `NNN-title/`").
- **Provenance immutability**: Per D-017 and `workspace-structure.md` v4 §provenance, "Provenance records are immutable once the session closes. Errors or retractions are recorded in subsequent sessions, not by editing past records."
- **OI-002** governs the substantive-vs-minor spec-revision heuristic. Substantive revisions trigger an engine-v bump per `engine-manifest.md` §5; minor corrections do not.
- **OI-007** tracks scaling pressure on workspace surfaces — the general discipline of not adding new surface when it can be avoided.
- **Session 015 precedent**: a single-perspective planning session that kept its opening-default folder name (`015-session-assessment`) because no substantive output warranted a rename. The close framed this as "Session 002 precedent for minimal no-deliberation sessions."
- **Session 022 precedent**: a substantive workspace-scaling session that was renamed at open from default to `022-workspace-scaling-trajectory` to reflect the session's work.

## §2 Problem statement

The operator, at Session 027 open, observed that the last four provenance folders are all named `session-assessment`:

| Session | Folder name | Content | SESSION-LOG title (abbrev.) |
|---|---|---|---|
| 023 | `023-session-assessment` | Substantive (engine-v4 bump; read-contract.md v1→v2) | "Read-Contract Budget Recalibration; engine-v3 → engine-v4" |
| 024 | `024-session-assessment` | Substantive (D-088 A.4 carry-the-warning; R6 cleanup) | "MAD 6K-Soft-Warn Response — A.4 Carry-the-Warning" |
| 025 | `025-session-assessment` | Path A execution; D-090/D-091 both `[none]` | "Path A Executed — Carry-the-Warning Continues" |
| 026 | `026-session-assessment` | Path A execution; D-092/D-093 both `[none]` | "Path A Executed — D-086 R9 Cadence-Escalation Window Ages Out" |

Historical practice (not specified, informally observed):

- Sessions 017–022 received meaningful folder names reflecting content: `017-oi017-reframing-deliberation`, `018-reference-validation-exercise-1`, `019-reference-validation-revision`, `020-workspace-scaling-deliberation`, `021-oi004-criterion4-articulation`, `022-workspace-scaling-trajectory`.
- Session 015 kept the placeholder (`015-session-assessment`) — no spec revision, single-perspective.
- Sessions 023 and 024 produced substantive work but kept the placeholder. This is the drift the operator surfaced.
- Sessions 025 and 026 produced no substantive work (two `[none]` decisions each) and match Session 015's placeholder pattern.

**The drift**: the rename-at-close-when-substantive practice is informally observed but not specified in `workspace-structure.md` or `prompts/development.md`. It broke at Session 023 and has remained broken for four sessions. The operator's observation is the first flag.

**Physical constraints on retroactive action**: a `grep` over the workspace shows 30 files contain path-string references to `023-session-assessment`, `024-session-assessment`, `025-session-assessment`, and `026-session-assessment`. The references are almost entirely self-references inside the four folders (assessment files citing their own paths; manifest.yaml files naming their originating paths; archive-pack chunks referencing their container folder; close files naming commits that landed under the old path). A retroactive rename requires either:

- (a) leaving these text references stale (workspace becomes internally inconsistent), or
- (b) editing the text references inside the closed-session folders (D-017 immutability violation unless explicitly dispensed), or
- (c) a narrower dispensation: permit path-string updates for folder rename but forbid content changes, with the dispensation explicitly enumerated in a decision record.

Git history points into the old paths regardless of any rename — retroactive workspace state cannot be hidden.

## §3 Design questions

Each perspective is asked to address the following. Number your responses Q1-Q6.

**Q1.** Should the engine formalise a folder-naming discipline? If yes, what does the rule say? If no, what is the cost of leaving it informal? Be specific about what goes wrong if nothing changes.

**Q2.** When (in the session cycle — open, close, mid-session) should the folder name be chosen or revised? Who has authority to revise it — the current session, the next session, never after close? How does this interact with D-017 immutability?

**Q3.** Should there be a retroactive rename of Sessions 023/024/025/026's folders? If yes, how is D-017 reconciled — a dispensation narrower than "edit closed session content" (e.g., "path-string updates only, no content mutation, enumerated in a decision record")? If no, what is the cost of the four folders remaining as historical witnesses to the drift?

**Q4.** Should the **opening default** name change from `NNN-session-assessment` to something else (e.g., `NNN-opening`, `NNN-<date-stamp>`, `NNN-pending-title`)? Is the current default a design bug (sessions that don't rename inherit an uninformative placeholder) or a useful placeholder (placeholder accurately labels a session-shape that ended up as assessment-only)?

**Q5.** Where should the rule live? `workspace-structure.md` §provenance (the spec that governs the `NNN-title/` convention), `prompts/development.md` §How to operate (the executable prompt), or elsewhere? What are the tradeoffs?

**Q6.** The operator's observation is data about the engine's self-observability — the drift went unflagged across four self-audits (Sessions 024/025/026 each ran their own Session N-1 synthesis-fidelity audit; none surfaced this drift). Is this class of drift governable by the mechanism you propose, or does it surface a deeper limitation of single-session self-audits?

## §4 Role-specific stance

[Role-specific stance is the only section that varies between briefs. Each perspective's brief substitutes its own §4 here.]

## §5 Response format

Each perspective produces a single file named `01<letter>-perspective-<role>.md` at the session's provenance root, where `<letter>` is a, b, or c in the order Archivist, Discoverer, Minimalist (alphabetical-ish by role stance):

- `01a-perspective-archivist.md`
- `01b-perspective-discoverer.md`
- `01c-perspective-minimalist.md`

Each file carries the standard Layer 1 frontmatter per `multi-agent-deliberation.md` v4 §Heterogeneous-Participant Recording Schema:

```yaml
---
session: 027
title: Perspective — <Role>
date: 2026-04-23
status: complete
perspective: <role>
committed_at: <session-phase>
---
```

Response body organised as six numbered sections Q1-Q6 matching the design questions. Target length: 300-700 words per question (so 1,800-4,200 words total per perspective). Conciseness is welcome; padding is not. State positions directly; cite specific files or sessions when relevant using either a path reference (e.g., `provenance/022-workspace-scaling-trajectory/03-close.md`) or a SESSION-LOG row reference.

Include at the end of your response a **Concluding summary** section: one to three sentences naming your top-line recommendation.

## §6 Constraint on external imports

Reason primarily from this brief and from the workspace state it describes. If you are tempted to cite an idea from pretraining (a software-engineering convention, a project-management practice, a workflow pattern from another tool), flag it explicitly as `[pretrained-external]` in the response and describe how it would be adopted into the Selvedge engine's specification process — do not commit it directly as a recommendation. Per `prompts/development.md` §Rules that hold across applications: "Do not import ideas from outside the process. If an insight arrived through reading something unrelated, a conversation with a human, or your own pretraining, introduce it as an input to an explicit surveying or hypothesising step rather than committing it directly."
