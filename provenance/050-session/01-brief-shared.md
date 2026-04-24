---
session: 050
title: Shared brief — 4-perspective two-family MAD on EF-047-retrieval-discipline-and-text-system-scaling-ceiling; retrieval substrate adoption decision for the Selvedge methodology (self-development + external-application workspaces) under S050 00-assessment §2a correction-overlay + Halt-1 Q6 external-application-portability scope expansion
date: 2026-04-24
status: brief-immutable-at-commit
---

# Shared brief — Session 050

## §0 Operator ratifications (verbatim)

S048 Halt 1 Q3 = (i) "S049 dedicated MAD" on EF-047-retrieval-discipline. S048 Halt 1 Q4 = (b) "bundle with S049 MAD" for the two minor EF-047 records.

S049 Halt 1 operator scope revision (verbatim):

> "recommendations should include data structure changes rather than discipline only … real scalable technical solutions … not constrained by 'watching' growth or summarising or archiving … it demands real engineering rigour"

S049 D-159 pre-ratified S050 as the 4-perspective two-family MAD with 8-question agenda. Design-space document at `provenance/049-session/design-space.md` produced at S049 as this MAD's input.

S050 Halt 1 operator pre-session corrections (verbatim):

> "Additional data points surfaced since S049: DuckDB FTS is current/stable and not experimental. P1 SQLite FTS5 is not 'the operator-named default', it was just an option presented to spur more research. The deliberation should not weight any operator-mentioned options more than others, nor is the operator's default 'load-bearing'."

S050 Halt 1 ratifications (operator response to 00-assessment §8):
- **Q1 (i)** — proceed with pre-scheduled MAD.
- **Q2 (a)** — canonicalise corrections in S050 00-assessment + edit triage record + fresh shared-brief; S049 design-space preserved as-is.
- **Q3 (ii)** — rename options neutrally: Substrate-1 SQLite-FTS5 / Substrate-2 DuckDB+FTS / Substrate-3 tantivy-py / Substrate-4 Whoosh-Reloaded / Substrate-N P3-surfaced-option.
- **Q4 (ii)** — P1 is neutral surveyor; advocacy emerges from technical evaluation, not operator-mention prior. P1 surveys the full candidate set including P3-surfaced additions.
- **Q5 (a)** — SESSION-LOG thin-row discipline at close (≤180 words).
- **Q6 — additional operator agenda** (verbatim):

> "include in consideration any externally run engine applications such as described in S046 and S047. These contain dense application artefacts and provenance that should also be able to benefit from the underlying mechanics, e.g. a bootstrapped database stored relative to that workspace."

The Q6 ratification is a **scope expansion**: external-application inheritance (Q7 in the 8-question agenda) is load-bearing, not deferrable. The substrate MUST work portably across the self-development workspace and any external-application workspace (starting with `selvedge-disaster-response` bootstrapped at S046 per D-142). Each workspace carries its own workspace-relative bootstrapped index. Q7 is no longer a yes/no question; it is a question about portability shape.

## §0b §5.6 GPT-family-concentration worst-case-side disclosure

Zero non-GPT non-Claude participants this session per operator S044 R2 standing preference. §5.6 joint minority worst-case-side data point continues (fourth-consecutive-substantive-deliberation data point; evaluation at S050 close).

## §0c Commit-discipline standing instruction (per WX-43-1 explicit-instruction variant)

Each perspective: **do not self-commit any files**. Your output goes to the Case Steward (orchestrator) who commits verbatim. You may propose file edits in your output as markdown code blocks or as explicit "proposed edit" sections, but do not execute `git commit` yourself.

## §0d WX-44-1 codex-CLI discipline (applies to P3 + P4 codex invocations)

No repo-wide search operations (no `find`, `grep -r`, `rg` over the workspace) from inside codex. Case Steward provides all necessary context in the stance brief + attached files. If you need additional context, request it in your output rather than searching.

## §1 What this deliberation is

You are one of four perspectives in a multi-agent deliberation for Session 050 of the Selvedge engine's self-development workspace. The Selvedge methodology is realised as a loadable file set (the specifications enumerated in `engine-manifest.md` §3); the self-development workspace at `/Users/ericmccowan/Development/complex-systems-engine/` is where the methodology evolves its own specifications by running on its own outputs; one external-application workspace exists at `/Users/ericmccowan/Development/selvedge-disaster-response/` (bootstrapped S046 per D-142; executed S047 arc-plan design session + S001 application session).

The engine-feedback/ inbox record `EF-047-retrieval-discipline-and-text-system-scaling-ceiling.md` raised that the write-side discipline (preserve + archive + shrink) is strong but the read-side substrate for Case-Steward retrieval under growing corpus scale is ad-hoc (prose scan over default-read + manifest walks). The operator reframed this at S049 from "discipline" to "substrate": the question is not "more rules for retrieval" but "what structured substrate sits under the text files and answers queries efficiently at agent-context scale". The S049 design-space document at `provenance/049-session/design-space.md` synthesised candidates, rejected alternatives, and an 8-question agenda for this S050 MAD.

**Your deliberation makes the substantive adoption decision.**

You have four perspectives:

- **P1 — Substrate Architect** (Claude subagent, neutral surveyor per Halt-1 Q4). Survey the full candidate set; propose specific architecture (tables, tokenizer, MCP tool surface, indexer shape) for whichever candidate evaluates strongest on technical merits. Advocacy emerges from the evaluation; there is no operator-preferred starting point.
- **P2 — Incrementalist / Maintenance Sceptic** (Claude subagent). Challenge the adoption scope. Smallest useful substrate first; when does each subsequent addition (edges table; aliases; warrants_currently_met; validator check 24) pay back? Is a partial adoption the honest increment; is defer-and-stay-lexical-tools-only a respectable option?
- **P3 — Outsider / Frame-Completion** (Codex/GPT-5.5 via `codex exec --sandbox read-only`). Frame-completion. Is the problem framed correctly as a substrate question? Sixth / seventh / Nth alternative not on the design-space menu? Is the Q6 external-application-portability expansion changing the structural trade-offs in ways the Claude perspectives would under-weight? Propose Substrate-N options not on §2 list.
- **P4 — Cross-Family Reviewer** (Codex/GPT-5.5 via `codex exec --sandbox read-only`). Laundering audit per S047 P4 convention. Examine P1+P2 proposals for Claude-lineage reasoning patterns. Apply anti-laundering guards: failed/strained criteria explicitly listed; revision traceability; cross-session touch; concrete measurable adoption criteria. Convergence-check: name counter-frames for any proposed substrate choice; record 4-of-4 convergence if it arises as shared-frame-blindness data point.

Your outputs will be committed verbatim and synthesised by the Case Steward (Claude orchestrator). Minority positions that do not converge will be preserved per MAD v4 §Preserve Dissent.

## §2 Problem statement under S050 00-assessment §2a correction-overlay

**Decide the retrieval substrate for the Selvedge methodology, portable across the self-development workspace and external-application workspaces, with decisions on adoption scope + kernel amendment + alias discipline + rebuild trigger + cross-spec sync + external-application inheritance + validator-check extension.**

### §2a Correction overlay to the S049 design-space

The S049 design-space document remains the substantive prior synthesis. Load it as the primary context. Apply two corrections over the design-space text:

**Correction 1 (factual)** — The DuckDB FTS extension is **current/stable**, not experimental. The design-space §5.3 first bullet ("DuckDB FTS extension is flagged experimental upstream … This is the biggest stability concern") is retracted. Evaluate DuckDB as a mature option. §11 honest-limit "pre-S050 spot-check of current DuckDB release notes is recommended" is resolved in favour of "stable".

**Correction 2 (framing)** — No weighting privilege attaches to operator-mentioned options. The following design-space framings are retracted:
- §3.1 P1 annotation "This is the operator-named default" (for SQLite FTS5).
- §4 header "Option A: SQLite FTS5 + structured tables + MCP (operator's named direction)".
- §4.2 / §5.4 any phrasing implying SQLite has an edge on "operator alignment".
- §5.4 closing: "But the operator named FTS5 specifically; Option A has the edge on operator alignment + zero install + ecosystem maturity".
- §6.4 bullet 4: "Operator did not name embeddings. This is a signal worth respecting." (The other three §6.4 bullets — ID-lookup failure, Anthropic-contextual-retrieval-at-<200K-tokens, semantic drift — stand.)

Evaluate every candidate on technical merits alone. Operator-surfaced candidates carry no deliberation weight distinct from research-surfaced candidates. The design-space's menu is **input, not ranked preference**.

### §2b Halt-1 Q6 scope expansion — external-application portability is load-bearing

The Selvedge methodology is domain-general. External-application workspaces (selvedge-disaster-response; any future ones) produce dense application artefacts and provenance in their own domains. The substrate MUST benefit these workspaces, not only the self-development workspace. Each workspace carries its own workspace-relative bootstrapped index.

This has specific design implications you must address:

- **Portability of the substrate code**: the indexer + MCP server need to live somewhere that external-application workspaces inherit or bootstrap from. Candidate mechanisms: engine-definition file set (per `engine-manifest.md` §3) that external workspaces inherit byte-identically at bootstrap; engine-adjacent tooling in a shared `tools/` directory that external workspaces copy at bootstrap; ancillary-local (per S046 D-142 precedent for `tools/bootstrap-external-workspace.sh`).
- **Workspace-relative index location**: the index file (`.cache/retrieval.db` or `.cache/retrieval.duckdb` or equivalent) must be workspace-local. A self-dev index does not query external-workspace content; an external-workspace index does not query self-dev content. Cross-workspace queries are out of scope at S050 (operator did not request; design-space §10 did not foreclose but S050 does not solve it).
- **Bootstrap integration**: `tools/bootstrap-external-workspace.sh` (S046 D-142 ancillary tooling at `/Users/ericmccowan/Development/complex-systems-engine/tools/bootstrap-external-workspace.sh`) should install the retrieval substrate in the new external workspace at bootstrap time, with a workspace-appropriate `.mcp.json` registration.
- **Dependency floor**: whatever substrate gets picked, its dependency floor is paid by every external-application workspace. A Python stdlib-only substrate (SQLite FTS5 on macOS default Python) has a floor of "Python 3.x + macOS default"; a DuckDB substrate adds a `duckdb` Python wheel install. Consider this when weighing candidates.
- **Bootstrap-time indexer run**: whether the bootstrapped substrate ships with a pre-built index or builds on first use affects the bootstrap UX. The external workspace's `tools/bootstrap-external-workspace.sh` is the place to choose.

## §3 Workspace state (measured at S050 open)

- **Self-development workspace**: 457 markdown files / 1.4M words / aggregate default-read 67,805 words across 19 files / 49 sessions of provenance / 15 MiB provenance directory / 31 preserved minorities in active specs.
- **External-application workspace (selvedge-disaster-response)**: bootstrapped S046 D-142; S047 produced `applications/001-disaster-response/arc-plan.md`; S001 (disaster-response application's own session 001) executed S047 close per operator transport. Actual current scale at that workspace is smaller than self-dev but growing with each arc session.
- **Identifier density, self-dev corpus**: D-NNN ~4,362 grep hits; OI-NNN ~4,243; Session-NNN ~10,286; WX-NN-N high hundreds; engine-vN ~1,458; EF-* ~60; `[archive: path]` low dozens; d016_N / d023_N dense per-decision.
- **`tools/validate.sh` is already a retrieval substrate**: 1,129 assertions across 23 checks are effectively SELECT-JOIN-AGGREGATE queries over the filesystem, bash-implemented.
- **Git history as implicit retrieval**: commit messages are 800–1,070 words recently; `git log -S` is the only substrate surfacing historical prose removed from active files.
- **`specifications/engine-manifest.md` §3 — engine-definition files** (current):

  ```
  PROMPT.md
  MODE.md (workspace-identity; distinct from engine-definition per §3)
  prompts/development.md
  prompts/application.md
  specifications/engine-manifest.md
  specifications/identity.md
  specifications/methodology-kernel.md
  specifications/multi-agent-deliberation.md
  specifications/validation-approach.md
  specifications/read-contract.md
  specifications/reference-validation.md
  specifications/workspace-structure.md
  tools/validate.sh
  ```

- **Ancillary** per S046 D-142: `tools/bootstrap-external-workspace.sh` (local-only; external workspaces build their own).

## §4 Eight questions for the MAD to resolve

Question numbers preserved from S049 design-space §8.2 for traceability. Framings updated per S050 00-assessment §2a + Halt-1 Q6 scope expansion.

**Q1 — Primary substrate choice.** Substrate-1 SQLite FTS5 / Substrate-2 DuckDB+FTS / Substrate-3 tantivy-py / Substrate-4 Whoosh-Reloaded / Substrate-N (P3-surfaced). Evaluate every candidate on technical merits. Defer-and-stay-lexical-tools-only is a respectable option P2 should argue.

**Q2 — Adoption scope.** Full-kit (all five tables + FTS + aliases + MCP server + validator check 24 + kernel §1 amendment) vs incremental (phase 1: FTS + `search` + `resolve_id` MCP tools; phase 2: edges + traversal + warrants_currently_met; phase 3: validator extension) vs minimal (FTS + search only) vs defer.

**Q3 — Kernel §1 amendment shape.** If the substrate ships, does the kernel §1 Read activity gain a "Warrant evaluation" sub-activity that calls a substrate tool? What happens when the substrate is unavailable (index not rebuilt, MCP server not running, bootstrap incomplete)?

**Q4 — Alias vocabulary.** SKOS three-label (prefLabel / altLabel / hiddenLabel) vs simpler two-label (canonical + aliases) vs defer alias discipline to a later session once substrate is operational.

**Q5 — Rebuild trigger.** Git post-commit hook (auto) vs session-open mtime check (lazy) vs both (belt-and-braces). Honest-limit if index is stale?

**Q6 — Cross-spec `syncs_with:` frontmatter field (EF-047 original level B).** Redundant with an `edges` table that extracts cross-spec references automatically? Or load-bearing at the spec layer as declaration-of-intent distinct from extracted-references?

**Q7 — External-application inheritance (LOAD-BEARING per Halt-1 Q6).** Shape of portability. Candidate mechanisms:
- (a) Engine-definition — substrate code files (`tools/build_retrieval_index.*`, `tools/retrieval_server.*`, `.mcp.json` template) enumerated in `engine-manifest.md` §3; external workspaces inherit byte-identically at bootstrap.
- (b) Engine-adjacent tooling — files live in shared `tools/` directory; external workspaces copy at bootstrap per `tools/bootstrap-external-workspace.sh`; not engine-definition (not required byte-identical) but always installed.
- (c) Ancillary-local — files stay local to self-dev; external workspaces re-implement independently (rejected by operator Q6).
- Integration with `tools/bootstrap-external-workspace.sh` is required regardless of (a) or (b).

**Q8 — Validator check 24 scope.** Preserved-minority pointer verification (baseline); OR extended to verify every `[archive: path]` citation resolves through the substrate; OR extended further to verify every ID reference in prose resolves to a known canonical form. Also: should check 24 run in external-application workspaces where preserved-minority-inheritance status is different (minorities-of-the-engine-are-present-as-inherited; minorities-of-the-application-accumulate-fresh)?

## §5 Perspective stance briefs

Each perspective reads §0–§4 above. Additionally, each has a stance-specific instruction set below. Other perspectives' stances are visible to you — reading adversarially is encouraged.

### §5.1 P1 — Substrate Architect (Claude subagent)

**Role** (post-Halt-1-Q4 amendment): neutral surveyor. Survey the full candidate set including any P3-surfaced additions (you will not see P3's output at launch; you may speculate about candidates P3 is likely to surface and pre-address them). Evaluate every candidate on technical merits alone. There is no operator-preferred starting point. Advocacy emerges from the evaluation.

**Your output** (`01a-perspective-substrate-architect.md`):
1. **Candidate evaluation** — for each of Substrate-1 through Substrate-4 (and any Substrate-N you surface), evaluate on: ID-crisp query performance; full-text BM25 quality; frontmatter-filter ergonomics; graph traversal ergonomics; dependency floor (self-dev + external-workspace); MCP integration effort; rebuild cost; index size; ecosystem maturity; API stability over 2–5 year horizon.
2. **Recommendation** — pick one (or hybrid). State why.
3. **Architecture proposal** — table schema / tokenizer config / MCP tool surface / indexer shape / rebuild trigger / file plan.
4. **External-application portability design** — how does the substrate bootstrap into a new external-workspace? What does the bootstrap script do? Where does the index file live (workspace-relative path)? What `.mcp.json` shape registers it in the external workspace? Is there a per-workspace config file?
5. **Answers to Q1–Q8** — one substantive paragraph per question.
6. **Counter-frames** — name the strongest argument against your recommendation that P4 might raise; pre-empt where possible.
7. **Measurable adoption criteria** — what metric, at what threshold, at what session, triggers revisit of this decision? (P4 laundering-audit guard.)

**Length target**: 3,000–4,500 words.

### §5.2 P2 — Incrementalist / Maintenance Sceptic (Claude subagent)

**Role**: challenge adoption scope. Smallest useful substrate first. Argue for minimal / defer / incremental options. Maintenance cost sustained over years. External-workspace portability adds a dependency surface for every future external application — is that acceptable tax, or a feature?

**Your output** (`01b-perspective-incrementalist-skeptic.md`):
1. **Baseline case for "defer"** — what is wrong with continuing ripgrep + grep + git-log + validate.sh as the substrate? What scale threshold would force adoption?
2. **Baseline case for "minimal adoption"** — if we must adopt something, what is the smallest possible useful substrate (single-table FTS + 1 MCP tool + nothing else)? What does it fail to do, and is that OK for the next 6–12 months?
3. **Cost surface per candidate** — each Substrate option's cost in: dependency floor; rebuild time; index size; code LOC; docs burden; debugging surface; external-workspace dependency propagation.
4. **Bootstrap cost for external applications** — what does Q6 Q7 portability cost every new external application? Is it OK tax on a "methodology-for-domain-projects" pitch?
5. **Phased-adoption plan** — if adoption proceeds, stage it: phase 1 (ship X; demonstrate value Y; revisit); phase 2 (add Z iff criterion W met); phase 3+ (open-ended). Name the go/no-go gates.
6. **Answers to Q1–Q8** — one substantive paragraph per question.
7. **Counter-frames** — name the strongest argument against your skeptic position that P1 might raise; concede what is conceded.
8. **Measurable adoption criteria** — what would have to be true to vindicate (or falsify) the incremental path?

**Length target**: 2,500–4,000 words.

### §5.3 P3 — Outsider / Frame-Completion (Codex/GPT-5.5 via `codex exec --sandbox read-only`)

**Role**: frame-completion. Is the problem framed correctly as a substrate question? Is there a sixth/seventh/Nth alternative not on the design-space menu? Is the Q6 external-application-portability expansion changing the structural trade-offs in ways the Claude perspectives would under-weight? Propose Substrate-N options not on §2 list.

**Your output** (`01c-perspective-outsider-frame-completion.md`):
1. **Frame critique** — what is the problem *actually*? Are the Claude perspectives framing it correctly? Is there a dissolving reframe that makes the substrate question moot, or less important?
2. **Candidate additions** — propose 1–3 Substrate-N options not on the design-space menu. Evaluate them on the same criteria P1 used. Include at least one option that fundamentally differs from "text-file + index" (e.g., "agent memory"; "structured artefacts replacing unstructured markdown"; "convention-over-tooling"; "query-log as substrate"; or something else that counts as alternative-shape).
3. **External-application portability reframe** — is engine-definition vs ancillary the right axis, or is there a better mechanism (bootstrap-template repo; adjacent-but-copied library; etc.)?
4. **Answers to Q1–Q8** — one substantive paragraph per question, with explicit distinct framing where the Claude perspectives may converge.
5. **Counter-frames for the dominant Claude position** — if P1+P2 converge on any specific substrate, what is the strongest case that this convergence is shared-frame blindness? Name the specific shared assumptions.

**Length target**: 2,000–3,500 words. Err toward compact and sharp; frame-completion under-length is better than frame-completion over-length.

**Standing instructions**: do NOT self-commit files. Do NOT search the workspace (`find`/`grep`/`rg`); Case Steward provides context. No repo-wide operations. Write your output to stdout in markdown; Case Steward captures and commits.

### §5.4 P4 — Cross-Family Reviewer / Laundering Audit (Codex/GPT-5.5 via `codex exec --sandbox read-only`)

**Role**: laundering audit of P1+P2 proposals for Claude-lineage reasoning patterns. Apply anti-laundering guards. Convergence-check: name counter-frames for any proposed substrate choice; if 4-of-4 convergence arises, flag as shared-frame-blindness data point per EF-047-session-inputs forward observation.

**Your output** (`01d-perspective-cross-family-reviewer.md`):
1. **Laundering-audit of P1** — does P1 list failed/strained criteria (not only wins) for its recommendation? Does P1 show revision traceability (what did P1 reconsider mid-draft)? Does P1 name cross-session precedents (S046 D-142 ancillary-tooling precedent; S048 D-153 read-contract carve-out precedent; S049 design-space prior synthesis)? Does P1 propose concrete measurable adoption criteria (not aspirational)?
2. **Laundering-audit of P2** — does P2 list positive-path criteria, not only critique? Does P2 engage with P1's architecture on its merits? Does P2's defer case identify the falsifying condition (what evidence would force adoption)?
3. **Convergence-check** — compare P1 and P2 on substrate choice, adoption scope, portability shape, alias discipline. Identify convergence and divergence. For each convergence, name the strongest counter-frame the pair did not consider.
4. **Shared-frame-blindness assessment** — are the Claude perspectives operating within a shared frame (e.g., "text-file substrate with add-on index" vs "restructure-the-artefacts")? If so, name it.
5. **Answers to Q1–Q8** — one substantive paragraph per question, with explicit attention to laundering-risk framings.
6. **Measurable adoption criteria recommendation** — which of P1's (or P2's) criteria meets the concrete-measurable bar? Which is aspirational?
7. **Dissent-preservation recommendation** — if your review produces distinct positions from P1+P2+P3, name which deserve first-class-minority preservation.

**Length target**: 2,000–3,500 words. Forensic; specific references to P1/P2 text preferred.

**Standing instructions**: do NOT self-commit files. Do NOT search the workspace. Write to stdout; Case Steward commits.

## §6 Deliberation rules

Per `specifications/multi-agent-deliberation.md` v4:

1. **Brief immutability at commit**: this brief is committed before P1–P4 launch; you read this verbatim, not a revised version.
2. **Do not import ideas from outside the process**: if you bring in an idea, introduce it as an explicit source-of-idea annotation (e.g., "I recall from pretraining that …") rather than asserting it as consensus knowledge.
3. **Do not overwrite prior specifications silently**: your proposals touch `methodology-kernel.md`, `validation-approach.md`, `engine-manifest.md`, `workspace-structure.md`, `read-contract.md`. Propose versioned successors (v6 → v7) with the prior version preserved.
4. **Preserve all provenance**: minority positions that do not converge will be recorded.
5. **Cite the design-space**: where you agree with the design-space, cite the section. Where you disagree, cite and rebut.
6. **Cite the operator corrections**: where a correction eliminates an option or rebalances a trade-off, say so explicitly.

## §7 Output format

Each perspective produces one markdown file at `provenance/050-session/01X-perspective-<name>.md` (where X = a, b, c, d). Frontmatter:

```yaml
---
session: 050
perspective: <short-name>
perspective_family: <claude | codex-gpt-5.5>
perspective_role: <substrate-architect | incrementalist-skeptic | outsider-frame-completion | cross-family-reviewer>
date: 2026-04-24
status: immutable-at-commit
---
```

Body sections per the stance brief. Answer Q1–Q8. No tool calls, no web fetches — reason from the shared-brief + the design-space. The Case Steward synthesises into `01-deliberation.md` and `02-decisions.md` at close.

## §8 Honest limits of this brief

- **Operator Q6 scope-expansion is concrete but under-specified**: the operator said "bootstrapped database stored relative to that workspace" but did not specify the exact bootstrap mechanism. Perspectives must propose one.
- **DuckDB stability claim is taken on operator's authority (2026-04-24 data point)**. Perspectives may re-verify from their own knowledge base but should not treat the original design-space §5.3 "experimental" characterisation as standing.
- **Brief written by Case Steward after reading S049 design-space**. Case-Steward framing is visible in §2 problem statement. P3 frame-completion and P4 laundering-audit should watch for this.
- **External-application current state**: selvedge-disaster-response arc is 1-of-4-or-5 sessions executed. Portability design must be provisional for external-applications that don't yet exist.
- **MCP API stability**: FastMCP and the Anthropic Python SDK are under active development in 2026. Perspectives should weigh API-stability-over-years in their recommendations.

End of shared brief.
