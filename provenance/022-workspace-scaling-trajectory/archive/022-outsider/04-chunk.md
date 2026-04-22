 session-open read workaround proves that operationally [§3, §6].

The risk of information loss is low for `SESSION-LOG.md` and moderate for `open-issues.md`.

- `SESSION-LOG.md`: low risk, because the detailed content already has a canonical home in `03-close.md`.
- `open-issues.md`: moderate risk, because annotations often carry live reasoning, cross-links, and conditional states. The mitigation is mechanical relocation with stable OI ids and exact-text preservation, not summary-only rewriting.

## Q6. `tools/validate.sh` hard-gate check

I support candidate #8, but not exactly as written.

It should hard-fail when any default-read file exceeds the configured per-file budget. I would set that budget in words, not tokens, because the current validator is bash-only and already uses standard Unix tooling [validation-approach §Tool Location and Behavior]. My recommendation is `8,000` words per default-read file.

I would also add an aggregate report, and likely a warning threshold, for the total development-provenance default-read surface. Per-file control alone is not sufficient if the default-read set keeps growing by accretion.

Canonical/default-read versus archive/witness must be detected by explicit classification, not filename heuristics. The normative list should live in a dedicated read-contract spec. The validator can mirror that list as constants or globs, as it already mirrors other spec rules [validation-approach §Tier 1: Structural Checks]. Without explicit classification, the validator will become a maze of accidental path rules.

## Q7. Session 020 minority activations

- §5.1: do not declare the old warrant vindicated as written. The literal 50,000-token condition is not met [§5.1]. Revise the warrant downward to the actual failure mode, or better, subsume the whole question into the new read-contract adoption. I prefer subsumption.
- §5.2: yes, adopt the rollback/restoration direction. Its warrant is satisfied [§5.2], and the fix belongs inside the new bounded default-read model.
- §5.3: yes, adopt. Its warrant is also satisfied [§5.3], and again the right framing is that `SESSION-LOG.md` returns to being an index, not a dossier.

So my pattern is: literal no on §5.1’s old trigger, yes on revising the underlying rule, yes on subsuming all three into the broader read-contract repair.

## Q8. Close shape for this session’s own raws

I accept “no grandfather clause” only in the thresholded sense. If this session adopts witness-packs, then any raw output from this session that exceeds the archive-pack threshold should be packed before close. Small raw outputs should remain ordinary provenance files; packing everything by default would add ceremony without solving a real problem.

Practically, that means this session’s provenance may close with ordinary raw perspective files plus zero or more witness-pack references if any response runs over budget. The `SESSION-LOG` entry should stay thin and simply record that the session adopted the bounded-read/archive model and, if applicable, created witness packs for over-threshold raws.

## Q9. Engine-version implication and triggers

Engine-v3 is warranted if the session adopts the substantive repair rather than E.1 alone.

E.1 by itself is only a `CLAUDE.md` cleanup. I verified the current mempalace paragraph is still there, and removing it does not touch engine-definition files. No engine bump is warranted for that alone.

The full repair, by contrast, changes engine behavior in substance. At minimum it touches:

- `specifications/methodology-kernel.md`
- `prompts/development.md`
- `prompts/application.md`
- `specifications/workspace-structure.md`
- `specifications/multi-agent-deliberation.md`
- `specifications/validation-approach.md`
- `tools/validate.sh`
- `specifications/engine-manifest.md`

If a dedicated read-contract spec is added, that is another engine-definition change. On that package, `engine-v3` is plainly correct [engine-manifest §5].

On triggers: I agree with the operator’s anticipated trigger declaration if the session takes the full adoption set. My confidence is highest on the non-Claude/engine-governance side because the proposed set revises the kernel, revises `multi-agent-deliberation.md`, and revises validation semantics. I am less certain on the exact D-016 numbering because I did not independently re-open the originating trigger-definition record, so that portion of my agreement is inferential rather than text-verified.

## Honest Limits

I verified the live current text of `prompts/development.md`, `prompts/application.md`, `specifications/methodology-kernel.md`, `specifications/workspace-structure.md`, `specifications/engine-manifest.md`, `specifications/validation-approach.md`, `specifications/multi-agent-deliberation.md` §Provenance Layout, `tools/validate.sh`, and `CLAUDE.md`.

I did not read other perspectives’ responses. I did not inspect raw provenance records beyond the one named extreme outlier path and did not inventory all over-threshold raw files across the workspace. I also did not reproduce the brief’s token counts with the same tokenizer, so where I discuss thresholds I am reasoning from the brief’s stated ceilings plus live file inspection, not from an independently matched token audit.
tokens used
46,382
I accept the direction of the operator’s concern, but not the operator’s ontology as stated. The failure here is a broken read contract: the engine still normatively requires exhaustive reading while actual sessions already rely on paging, grepping, and routing around oversized surfaces [§2.2, §3, §6; methodology-kernel §1 Read; §4.2]. A canonical-vs-witness distinction is the right repair only if it is treated as a bounded access rule layered on top of the existing file classes, not as a claim that every historically important file remains default-read forever [workspace-structure §File classes].

## Q1. Frame acceptance

Partially yes. I accept the need for a bounded default-read surface and a preserved reference/archive surface. I do not accept “two artefact kinds” as the deepest diagnosis. The deeper diagnosis is that the workspace’s normative read obligation and its operational reading mechanism have diverged [§3, §6]. “Canonical surfaces” and “witnesses” are a repair for that divergence, not the root conceptual model.

That distinction matters because the workspace already has a load-bearing ontology: engine-definition, development-provenance, and application-scope [workspace-structure §File classes; engine-manifest §1, §4]. The new distinction should cut across those classes as an access discipline:

- `default-read surface`: what every session must read in full before acting.
- `reference/archive surface`: what must be preserved exactly and read when relied on, cited, or challenged.

My main disagreement with the operator’s examples is that putting all per-session `03-close.md` files on the canonical/default-read surface would recreate the same growth problem in a slower form. That controls per-file size but not aggregate session-open burden. A bounded surface must be bounded in total, not only in its largest member. So I accept the direction, but I would define the repair as a “bounded working-set contract,” not simply “two artefact kinds.”

## Q2. `prompts/development.md` revisions

Yes, line 19 must change. Yes, line 25 must change with it. Yes, line 43 should explicitly authorize archive/witness packing. And no, prompt-only revision is not sufficient; the kernel must change too, because the kernel currently makes the prompt-level relaxation semantically illegal [methodology-kernel §1 Read; §4.1, §4.2].

My proposed text is:

- Line 19: “Begin by reading the workspace’s default-read surface completely: the active engine-definition files, the workspace’s bounded orientation records, and the current session’s explicit inputs. Then read any archived records you will rely on, cite, challenge, or revise.”
- Line 25: “Before substantive work, read the bounded decision-orientation records the workspace designates for continuity, then read any archived prior records needed to understand relevant rejections, unresolved disputes, or dependency chains.”
- Line 43: “Preserve all provenance. Do not delete or silently compress historical records. When a preserved record exceeds default-read bounds, retain it as an immutable archived witness with a stable manifest, chunk references, and integrity metadata.”

I would also revise `methodology-kernel.md` §1 Read in the same direction. The current text says “every file, every specification, every provenance record” [methodology-kernel §1 Read]. That is the contradiction. If the session changes only `prompts/development.md`, the kernel and executable prompt diverge.

I would further align `prompts/application.md`, because its current Read section still says the full current state of the application workspace. If that text is left untouched, the engine exports the same contradiction to external applications.

## Q3. Witness-pack specification

I will use “witness-pack” because the brief uses it, but the load-bearing idea is archived exact-text packaging.

- Format: directory, not zip, and not a single monolith. Use `manifest.md` plus numbered raw chunks such as `0001.raw.md`, `0002.raw.md`, etc. Zip-like archives are wrong here because they break grep/diff/referenceability.
- Location: a top-level `witnesses/` or `archives/` directory, not retroactively inserted into closed provenance directories. That respects provenance immutability better than adding new files inside old session folders [workspace-structure §provenance/].
- Inclusion rule: any archived record that exceeds the default-read per-file budget must have a pack. Small archived records can remain single-file archived records without chunking. Superseded specs should become archive-surface by rule even if they do not need chunking [engine-manifest §4].
- Reference convention: canonical/default-read files cite a stable witness id and, when needed, a chunk id. Example: `witness:W-014-01d#0003` or equivalent path-plus-chunk reference.
- Resolution rule: the manifest states `source_path`, `reason_for_archiving`, `source_hash`, ordered chunk list, and reconstruction rule.
- Integrity: hash the source file and each chunk. The pack is append-only. If the source was copied from an existing immutable record, the manifest says so explicitly.
- Engine impact: yes, this is engine-v3 work. It changes read semantics, provenance handling, and validation.

I would put the normative classification rules in a new engine-definition spec, something like `specifications/read-contract.md`. This is cross-cutting enough that burying it in `workspace-structure.md` would make the rule hard to follow and easy to drift.

## Q4. Retroactive migration scope

- (a) Yes. `provenance/014-oi016-resolution/01d-perspective-outsider.md` is the clearest falsifier to the old read contract [§2.2]. If nothing else is migrated, this one should be.
- (b) Yes, in principle. If the methodology adopts a threshold, all over-threshold raw perspective files should eventually receive archive packs. Otherwise the rule is selective and arbitrary. If the set is too large to finish now, do not pretend the migration is complete.
- (c) Yes, but as reclassification first, chunking second. Superseded spec copies are already explicitly not part of engine load [engine-manifest §4]. They should move off the default-read surface immediately; only oversize ones need packing.
- (d) Yes. Long annotations in `open-issues.md` should move into issue-specific detail records or witness packs, with the index left thin [workspace-structure §open-issues.md].
- (e) Yes, but not via witness-packing by default. `SESSION-LOG.md` is mutable and already defined as an index over `03-close.md`, not a replacement for it [workspace-structure §SESSION-LOG.md]. Long entries should simply be shortened in place.
- (f) No, not this session. Epoch consolidation for Sessions 001–010 is plausible later, but it is not necessary to repair the broken read contract immediately. It adds synthesis risk and a lot of migration surface.

## Q5. Canonical-surface restoration this session

Yes on both.

`SESSION-LOG.md` should be restored to a true thin index this session. The specification already says it is “a running index” and that canonical detail lives in `03-close.md` [workspace-structure §SESSION-LOG.md]. The current state is type-drift, not just growth [§2.2, §5.3].

`open-issues.md` should also be restructured this session. I do not think §5.1’s original strict 50,000-token warrant has literally fired [§5.1]. I do think the file is already “unwieldy” under the structure spec’s own authorization clause [workspace-structure §open-issues.md], and the current session-open read workaround proves that operationally [§3, §6].

The risk of information loss is low for `SESSION-LOG.md` and moderate for `open-issues.md`.

- `SESSION-LOG.md`: low risk, because the detailed content already has a canonical home in `03-close.md`.
- `open-issues.md`: moderate risk, because annotations often carry live reasoning, cross-links, and conditional states. The mitigation is mechanical relocation with stable OI ids and exact-text preservation, not summary-only rewriting.

## Q6. `tools/validate.sh` hard-gate check

I support candidate #8, but not exactly as written.

It should hard-fail when any default-read file exceeds the configured per-file budget. I would set that budget in words, not tokens, because the current validator is bash-only and already uses standard Unix tooling [validation-approach §Tool Location and Behavior]. My recommendation is `8,000` words per default-read file.

I would also add an aggregate report, and likely a warning threshold, for the total development-provenance default-read surface. Per-file control alone is not sufficient if the default-read set keeps growing by accretion.

Canonical/default-read versus archive/witness must be detected by explicit classification, not filename heuristics. The normative list should live in a dedicated read-contract spec. The validator can mirror that list as constants or globs, as it already mirrors other spec rules [validation-approach §Tier 1: Structural Checks]. Without explicit classification, the validator will become a maze of accidental path rules.

## Q7. Session 020 minority activations

- §5.1: do not declare the old warrant vindicated as written. The literal 50,000-token condition is not met [§5.1]. Revise the warrant downward to the actual failure mode, or better, subsume the whole question into the new read-contract adoption. I prefer subsumption.
- §5.2: yes, adopt the rollback/restoration direction. Its warrant is satisfied [§5.2], and the fix belongs inside the new bounded default-read model.
- §5.3: yes, adopt. Its warrant is also satisfied [§5.3], and again the right framing is that `SESSION-LOG.md` returns to being an index, not a dossier.

So my pattern is: literal no on §5.1’s old trigger, yes on revising the underlying rule, yes on subsuming all three into the broader read-contract repair.

## Q8. Close shape for this session’s own raws

I accept “no grandfather clause” only in the thresholded sense. If this session adopts witness-packs, then any raw output from this session that exceeds the archive-pack threshold should be packed before close. Small raw outputs should remain ordinary provenance files; packing everything by default would add ceremony without solving a real problem.

Practically, that means this session’s provenance may close with ordinary raw perspective files plus zero or more witness-pack references if any response runs over budget. The `SESSION-LOG` entry should stay thin and simply record that the session adopted the bounded-read/archive model and, if applicable, created witness packs for over-threshold raws.

## Q9. Engine-version implication and triggers

Engine-v3 is warranted if the session adopts the substantive repair rather than E.1 alone.

E.1 by itself is only a `CLAUDE.md` cleanup. I verified the current mempalace paragraph is still there, and removing it does not touch engine-definition files. No engine bump is warranted for that alone.

The full repair, by contrast, changes engine behavior in substance. At minimum it touches:

- `specifications/methodology-kernel.md`
- `prompts/development.md`
- `prompts/application.md`
- `specifications/workspace-structure.md`
- `specifications/multi-agent-deliberation.md`
- `specifications/validation-approach.md`
- `tools/validate.sh`
- `specifications/engine-manifest.md`

If a dedicated read-contract spec is added, that is another engine-definition change. On that package, `engine-v3` is plainly correct [engine-manifest §5].

On triggers: I agree with the operator’s anticipated trigger declaration if the session takes the full adoption set. My confidence is highest on the non-Claude/engine-governance side because the proposed set revises the kernel, revises `multi-agent-deliberation.md`, and revises validation semantics. I am less certain on the exact D-016 numbering because I did not independently re-open the originating trigger-definition record, so that portion of my agreement is inferential rather than text-verified.

## Honest Limits

I verified the live current text of `prompts/development.md`, `prompts/application.md`, `specifications/methodology-kernel.md`, `specifications/workspace-structure.md`, `specifications/engine-manifest.md`, `specifications/validation-approach.md`, `specifications/multi-agent-deliberation.md` §Provenance Layout, `tools/validate.sh`, and `CLAUDE.md`.

I did not read other perspectives’ responses. I did not inspect raw provenance records beyond the one named extreme outlier path and did not inventory all over-threshold raw files across the workspace. I also did not reproduce the brief’s token counts with the same tokenizer, so where I discuss thresholds I am reasoning from the brief’s stated ceilings plus live file inspection, not from an independently matched token audit.
