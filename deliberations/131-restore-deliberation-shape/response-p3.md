**Position.** Multi-agent deliberation has drifted to a 2-perspective default because the post-restart engine lost its deliberation shape machinery without losing the conditions that made that machinery necessary. Restoring deliberation requires not importing MAD v4 whole but rather disciplining it through the lens of constraints.md, which teaches that LLM agents need structural friction at their decision points. My position: deliberation shape should be minimal, substrate-enforced at the floor (3 perspectives, cross-family, one adversarial), brief-immutable with role-specific stances, and synthesis-transparent—but the restoration path should use only three additions to the engine: a 3-perspective floor in `prompt-development.md` v9, a deliberation substrate record to prevent re-defaults, and a deliberation-open CLI gating that enforces cross-family. Restore the *discipline* MAD v4 encoded, not the *prose* it generated. This addresses constraints.md properties 1, 2, and 5 (models default away from friction, need structural enforcement, cannot carry lessons across sessions) without the accretion cost of the full spec.

**Q1 (number).** Floor of 3 perspectives, target of 4 for decisions that change methodology. When the problem spans more than two genuinely independent concern-domains (e.g., substrate, interface, validation), add a perspective. No 5+ without written justification at convene time. Rationale: constraints.md §3 shows that cross-family disagreement surfaces blind spots; property 5 says consensus within a family is weak. Two perspectives allow consensus-within-family to masquerade as convergence (S124 evidence shows the four-perspective shape revealed this masquerade). Three is the minimal threshold. Four handles deliberations that require both depth and breadth.

**Q2 (role discipline).** Close the enum to five role kinds: Anthropic-Pragmatist, Anthropic-Skeptic, OpenAI-Skeptic, OpenAI-Dreamer, and one free-form role named for the deliberation's actual disagreement axis (e.g., "Substrate-Minimalist," "Retention-Maximalist"). This avoids re-describing roles each deliberation while allowing operator-driven specialization to a real axis. Operator names the free-form role at convene time; fixed roles rotate across families. Names are used consistently in briefs, synthesis, and decision records.

**Q3 (required role).** Yes, one adversarial perspective is required. Substrate-enforce: `deliberation-open` refuses if adversarial-family is not named. The refusal is structural (constraints.md property 1: models avoid friction unless it is external). Prose discipline alone fails; property 5 shows it is forgotten across sessions.

**Q4 (stance-brief structure).** Re-codify the shared/role-specific split: briefs are stored in the workspace, generated at convene time, immutable after commit. Structure: methodology context (shared), problem statement (shared), design questions (shared), role-specific stance (150–300 words, role-naming the specific concerns), response format (shared), constraint on external imports (shared). Briefs remain workspace files, not substrate records—they are working documents, not the engine's state. Brief immutability is enforced by git: all briefs are committed before any perspective is launched.

**Q5 (synthesis discipline).** Restore citation requirements and `[synth]` markers for synthesizer-original claims. Synthesizer cannot have been a perspective. Dissent preservation and majority/minority structure are required; coverage vs convergence distinction is required. These are prose rules, enforced by review at session-close; they should not live in the substrate (constraints.md property 2: external friction is more reliable than internal discipline). Synthesis order: alphabetical by role name.

**Q6 (graceful degradation).** Minimum viable quorum: 3 valid outputs, at least one from outside the perspective's primary family. Fewer than 3, or fewer than 2 families represented, triggers re-run or question reformulation. This avoids both the pure-democracy trap (majority vote within family) and the brittleness of strict cross-family requirement (if one family fails, the deliberation collapses).

**Q7 (smallest shape).** Three additions to the engine: (1) Add "minimum 3 perspectives, at least 2 families, one adversarial" as a hard gate in `prompt-development.md` v9 §4, with `deliberation-open` CLI enforcing it before the briefing phase. (2) Add a deliberations table record per convene (date, topic, expected role count, families) to prevent the re-default: when a developer reaches for a 2-perspective deliberation, the substrate already has a record that it should be 3. (3) Restore brief-immutability: briefs are committed together before perspectives are launched; a perspective that later claims the brief was unclear has a reproducible artefact. This is ~50 lines of prompt and ~10 lines of CLI gating, not 482 lines of spec.

**schema_sketch.**
- Extend `deliberations` table: add `minimum_perspectives` INT (default 3), `expected_families` TEXT (comma-separated, e.g. "anthropic,openai"), `adversarial_perspective_label` TEXT.
- Add deliberation-brief table: `deliberation_id`, `role_label`, `family`, `stance_md_hash` (content-addressable reference to immutable brief text, committed to git before launch).

**cli_surface.**
- `deliberation-open --perspectives 3 --families anthropic,openai --adversarial skeptic` gates convene at the CLI level; refuses if requirements not met.
- `brief-lock` verb to commit briefs and prevent mutation until deliberation-seal.

**migration_path.**
- Add gating to existing `deliberation-open` verb at S132: enforce minimum-perspectives rule before briefing phase launches.
- Brief immutability enforced by existing git workflow: briefs are committed before perspective-launch, and commit history is the provenance record.
- No retroactive changes needed to S076–S131; the 2-perspective default is a historical record, not a system error requiring cleanup.

**what_not.**
- Not re-importing MAD v4 prose verbatim; not creating a 482-line spec; not mandating substrate-recorded role names (enumeration in code is enough).
- Not changing synthesis mechanics beyond re-adopting citation and convergence-vs-coverage discipline (prose-enforced).
- Not creating a rotating-quorum or past-self perspective (external: this is a pre-training pattern I recognize; treating as hypothesis not warrant).
- Not mandating 5+ perspectives, even for methodology changes (4 is the target, 5 requires justification; let accretion decide whether 5 is needed).

**open_question.**
- When operator-named axes do not cleanly map to model families (e.g., "crypto-skeptic" could be either family), how is the free-form role slot assigned? Operator pre-declares, or consensus rule?
- If a deliberation starts with 3 and one perspective returns a refusal, is re-run required, or is a replacement perspective acceptable? (constraints.md property 5 suggests re-run preserves the intent; replacement inherits unknown framing.)
- Should the stance-brief generation itself be formalized as a verb with a template, or remain operator-written-and-reviewed?

**risk.**
- If the 3-perspective floor is enforced at the CLI level, an operator can bypass it only by hand-editing the database, which creates a silent failure mode (a deliberation that looks valid but lacks required structure).
- Adversarial requirement can be satisfied formally (a role named "skeptic") without being substantive; prose discipline is necessary but not sufficient.
- Brief immutability enforced by git-review-before-launch works only if the review step is not skipped; no code-level enforcement possible without a pre-commit hook, which is out-of-scope for this decision.

**what_lost.**
- The full MAD v4 spec's schema-lifecycle machinery (4-state perspective lifecycle, Layer 2 manifest, validate.sh checks 16–19) is not restored. These were optimizations for a larger engine; the post-restart engine can absorb deliberation discipline without them.
- Rotating-quorum perspectives (constraint-property-5 hedge) are not adopted; they are speculative and could be revisited if future deliberations show the same lessons-loss pattern.
- The constraints.md properties (now archived) are not restored as working documents; they remain in this brief's §4.1 as historical warrant, not as an engine-loadable spec.
