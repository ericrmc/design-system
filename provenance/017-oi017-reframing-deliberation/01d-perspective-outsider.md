---
session: 017
title: Perspective — Outsider (independent, non-Claude; proposes H4 layered model)
date: 2026-04-22
status: complete
perspective: outsider
committed_at: 2026-04-22
model_identity: OpenAI GPT-5.4 via codex exec
codex_session_id: 019db36d-14a0-7d10-863e-179677eef35b
reasoning_effort: xhigh
tokens_used: 19120
---

## Q1 — Adopt the reframing, but as a layered model rather than a replacement

I would adopt the reframing, but not in the H2 form as stated. I think the H1/H2/H3 frame entangles two different decisions that should be separated: what Selvedge is, and what must be loaded to run it. The brief already shows that "methodology" is doing double duty, and that is not just a wording problem. It affects the executable boundary, provenance portability, and prompt shape. So I reject H1.

I also think H2 overcorrects. If the workspace renames the core thing from methodology to engine, it risks erasing a distinction that the brief itself says is real: there is an abstract, domain-general mechanic, and there is a concrete workspace implementation of that mechanic. My position is a fourth hypothesis: make the stack explicit as methodology -> engine -> application. Selvedge remains the methodology; the Selvedge engine is the current loadable implementation; each run against self-development or an external problem is an application of that engine.

The strongest reason for this is that it resolves the actual ambiguity without collapsing levels. It gives a clean answer to the operator's two observations: yes, the loadable engine should be separable from its development provenance; yes, self-development and external application need different entry prompts. But it does not force a premature claim that the nine-activity kernel is only an engine concern.

The main cost is conceptual and editorial overhead. The workspace would now have to be disciplined about which statements are methodology-level, which are engine-level, and which are workspace-state. That is real cost. But I think it is the right cost, because the ambiguity is already operational.

## Q2 — Change the scope-bearing files, not every file indiscriminately

The files that materially need change are `PROMPT.md`, `specifications/methodology-kernel.md`, `specifications/workspace-structure.md`, and `specifications/identity.md`. I would also make smaller terminology updates in `specifications/multi-agent-deliberation.md` and `specifications/validation-approach.md`. I would leave `specifications/reference-validation.md` unchanged unless a concrete inconsistency appears.

In `specifications/methodology-kernel.md`, I would keep the filename and add an opening scope clarification. The key sentence should be something like: "This specification defines the Selvedge methodology kernel: the abstract execution semantics that a conforming engine must realise." I would then add one sentence pointing to `engine-manifest.md` as the place that defines the current engine packaging.

In `specifications/workspace-structure.md`, I would add an explicit file-class distinction: engine-definition files, development-provenance files, and application-scope files. Concretely, engine-definition would include `PROMPT.md`, the prompt files, `specifications/`, and `tools/validate.sh`; development-provenance would include `SESSION-LOG.md`, `open-issues.md`, and `provenance/`; application-scope would include `applications/`. The important normative change is that an external application workspace may load the engine-definition set without inheriting development-provenance.

In `specifications/identity.md`, I would add explicit denotation language: "Selvedge names the methodology. 'Selvedge engine' denotes the current executable implementation defined by `engine-manifest.md`." That preserves the name while resolving scope.

In `specifications/multi-agent-deliberation.md` and `specifications/validation-approach.md`, I would make only light edits so they state that their rules apply both in self-development runs and external-application runs.

## Q3 — Split the executable prompts, keep a thin top-level entry point

I would reorganise `PROMPT.md` into a thin dispatcher and split the executable content into two files. I would not keep one large prompt with internal branches. A branched monolith is exactly where silent import happens: self-development assumptions bleed into external application runs because both modes share too much narrative scaffolding.

Concretely, I would make `PROMPT.md` short. Its job would be to define the three layers, state that Selvedge has two operating modes, and point to two entry prompts: one for self-development and one for external application. The actual executable instructions would move to something like `prompts/development.md` and `prompts/application.md`.

The development prompt would preserve today's behaviour: the workspace is allowed to modify its own engine-definition files, deliberate over open issues, and treat its own specifications as the design object. The application prompt would do the opposite: it would load the engine manifest plus the target application's local context, and it would explicitly state that the development history is not part of the application context unless imported on purpose.

I prefer this over H3's "no split" because the brief already gives enough evidence that the two prompt roles are different in kind, not just in wording.

## Q4 — Create `engine-manifest.md`, and keep it strictly minimal

Yes, I would create `specifications/engine-manifest.md`. I think it is necessary because the load boundary is the practical core of the reframing. Without an authoritative manifest, the workspace still depends on tacit knowledge about which files "count."

At minimum, the manifest should contain five things. First, a definition of the engine: the current loadable implementation of the Selvedge methodology. Second, the canonical file set that constitutes the engine-definition. Third, the entry points for each application kind: self-development and external application. Fourth, an explicit exclusion list stating that `SESSION-LOG.md`, `open-issues.md`, existing `provenance/`, and prior `applications/` content are not part of the engine load by default. Fifth, a minimal initialisation contract for a fresh external application workspace.

I would keep it out of the business of restating every other spec. Its purpose is not to become a new kernel. Its purpose is to answer a narrow operational question: "What do I need to load to run Selvedge here, and what do I explicitly not need?"

## Q5 — Selvedge should name the methodology; the engine gets the qualified name

I would keep "Selvedge" as the name of the methodology. I would use "Selvedge engine" as the qualified name of the current executable implementation. That is the cleanest way to preserve identity continuity while acknowledging the reframing.

I would not say that Selvedge equally names both without qualification. That invites the same ambiguity back in. The unqualified name should point to the broader thing. The qualified phrase should point to the concrete, loadable thing.

On the Reopening conditions, I can only be partial because the brief discloses only condition 1. Condition 1 is clearly not triggered; the external adoption threshold remains unmet. [uncertain] For conditions 2-4, I do not know their text. My judgment is that H2 as stated might prudently justify reopening identity even if it does not mechanically trigger a listed condition, because it changes what the name denotes. Under my position, I would not reopen `identity.md` in the strong sense; I would amend it for clarification. If one of the undisclosed conditions concerns denotation change or scope reclassification, H2 is more exposed than H3 or my layered alternative.

## Q6 — External application should start from the engine manifest, not from the development history

Under my position, someone else should initialise a fresh application workspace by copying the engine-definition set named in `engine-manifest.md`, not by cloning the full self-development workspace state. That means they take the prompt entry points, the relevant specifications, and the validation tooling, but not the originating `SESSION-LOG.md`, accumulated `provenance/`, or legacy `applications/` outputs.

The initial workspace should contain `PROMPT.md`, the mode-specific prompt files, `specifications/`, `tools/validate.sh`, a fresh `SESSION-LOG.md`, a fresh `open-issues.md`, an empty `provenance/`, and an `applications/001-<slug>/` directory for the local problem. Inside that application directory, I would require at minimum a `brief.md` stating the problem, constraints, stakeholders, and success condition. If there are source materials, they should live alongside it in that same application folder.

Session 001 in that new workspace would use the application prompt plus `applications/001-<slug>/brief.md` as the local context. The session log should record which engine manifest version or revision was loaded. The produced artefact would live under the same application folder, and provenance would start fresh from that workspace's own run history.

The critical rule is this: external application workspaces inherit the engine, not the engine's autobiography.

## Q7 — The strongest case against this is that it may be premature architecture

The strongest argument against my position is that I may be solving a conceptual neatness problem before there is enough operational evidence. There are only two external artefacts and no independent adopter past the threshold named in `identity.md`. On that view, H3 is better: define the engine boundary with a manifest, add a few clarifying sentences, and wait for one or two genuine external application workspaces to expose whether prompt separation and layered naming are really needed. My proposal could create duplicated prompts, extra terminology, and maintenance burden before the system has earned that complexity.

I would abandon my position in favour of H3 if two conditions were observed. First, when drafting `prompts/application.md`, it turns out to be almost the same as the self-development prompt, with only small variable substitutions and no meaningful behavioural divergence. Second, a pilot external application workspace can be initialised from a manifest-only clarification with no confusion about whether development provenance is in scope. If that happens, then a prompt split is premature and the lighter H3 path is superior.

I would even move toward H1 if a simpler clarification inside the existing `PROMPT.md` eliminated the ambiguity in practice across multiple sessions. But I do not think the brief points that way today. The load boundary problem already looks structural, not merely editorial.
