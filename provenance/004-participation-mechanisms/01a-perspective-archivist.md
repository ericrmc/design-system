---
session: 004
title: Raw Perspective — Archivist
date: 2026-04-18
status: complete
perspective: Archivist
agent-type: general-purpose subagent (parallel, context-isolated)
model: claude-opus-4-7
brief-commit: ab86605aaeea7b2bca88f89ecc2ab3b88dd2b378
---

*This file preserves the raw output from the Archivist perspective verbatim, without editorial change. See `01-deliberation.md` for synthesis.*

---

## Q1

The minimum viable mechanism is a **brief-drop pattern with verbatim response capture**: the convener commits the same brief used for Claude perspectives to `provenance/NNN/briefs/<perspective>.md`, then delivers it to one non-Claude participant (model or human) through whatever channel is available (web UI paste, CLI call, email), and commits the returned response verbatim as `provenance/NNN/raw/<perspective>.md` alongside a sibling manifest `<perspective>.manifest.yaml` recording how it was delivered and received.

I defend this choice on archival grounds: it requires zero new infrastructure, zero API keys, zero tools in the repo. The convener is the transport layer. The contract is not "the workspace can call the model" — it is "the workspace can record what the model said." That inversion is what keeps the mechanism specifiable today.

The concrete shape:
- Brief is committed **before** the participant sees it (preserves D-017's "briefs committed before launch" constraint).
- Raw response is committed **unedited**. If the participant is a chat UI, the convener pastes the full response including any preface. If the participant is a human, their reply text verbatim.
- The manifest records channel, timestamps, and identity fields (see Q4).
- The synthesizer treats the non-Claude response identically to Claude raw outputs under D-018 — cite by file, quote load-bearing claims.

What this deliberately does not do: attempt to automate the call, attempt to standardize the interface, attempt to ensure reproducibility of the model's output. It accepts that cross-model participation is **asynchronous and manual at first**, and that the reproducibility guarantee is over the *record*, not the *generation*. This matches what the workspace can actually guarantee — it controls the git history, not the remote model.

[external input: the pattern of "commit the brief, commit the response, commit the transport metadata separately" is analogous to archival practices for correspondence collections, where envelope metadata is kept distinct from letter contents. Flagging as external.]

## Q2

Mixing Opus, Sonnet, and Haiku is **training-distribution theatre for the purpose of OI-004, but operationally useful for other reasons**. It falls at "neither" on the OI-004 scale — not closure, not narrowing.

The argument: OI-004 is specifically about perspective independence *beyond the Claude family*. The Limitations section of `multi-agent-deliberation.md` is explicit that "all current perspectives share a model family" is the limit in question. Opus, Sonnet, and Haiku share the Claude family. They share training data distributions, RLHF preference models, constitutional inputs, and Anthropic's safety training. The size differences produce capability differences, not independence differences. A shared blind spot at the family level is still shared when the participants are Opus and Haiku.

That said, size-mixing has real utility that should not be confused with closure:
- Capability stratification (Haiku surfaces what a weaker reasoner notices; Opus surfaces what a stronger one does).
- Cost-scaled deliberation (cheap perspectives for exploratory rounds, expensive for load-bearing).
- Adversarial role assignment where the adversary is a different size and so has different failure modes within the family.

None of these narrow OI-004. They address orthogonal concerns — deliberation cost, capability floor, intra-family variance — that deserve their own tracking, perhaps as a separate open issue OI-011 ("intra-family model mixing as a deliberation-quality lever, distinct from cross-model independence").

For provenance honesty, the methodology should not let Opus+Sonnet+Haiku deliberations claim any progress on OI-004. The record should mark them as same-family. If the frontmatter permits a `participants_family` field with values like `claude-only` or `mixed`, an Opus+Sonnet+Haiku session is `claude-only`. Calling it mixed would be the provenance dishonesty the pattern warns about.

## Q3

**Recommended, not required, for substantive deliberations; required for any decision that modifies the multi-agent-deliberation specification itself or the kernel.**

The governing criterion is **self-referentiality**: when a deliberation's subject matter is the deliberation mechanism itself, the risk of monoculture blind spots contaminating the mechanism's own evolution is highest. A Claude-only deliberation about how Claude-only deliberations should work is precisely the failure mode OI-004 names.

Concrete trigger rule for the next session to adopt:

| Deliberation subject | Non-Claude participation |
|---|---|
| Kernel changes | Required |
| Changes to `multi-agent-deliberation.md` | Required |
| Changes to `validation-approach.md` when validation involves semantic judgment | Required |
| New specifications | Recommended |
| Load-bearing decisions tagged under D-016 | Recommended |
| Spec revisions not in above categories | Optional |

When required but skipped, the session must record an opt-out reason in the session's decision log (mirrors D-016's existing opt-out pattern). Acceptable opt-outs: "no non-Claude participant available within session timebox", "subject matter does not expose Claude-family blind spots" (must be argued, not asserted).

Why recommended rather than required for substantive-but-not-self-referential work: requiring it universally would either (a) block progress when no non-Claude participant is available, degrading the methodology to the speed of its slowest channel, or (b) produce pro-forma non-Claude participation — a human rubber-stamping the outcome, a second model called with a degraded brief — which is provenance theatre worse than honest acknowledgment of Claude-only reasoning.

The asymmetry is deliberate: the methodology evolving itself is where blind spots compound across sessions and become structural. External-domain deliberations using the methodology can tolerate more Claude-only sessions because errors there are caught by the domain, not internalized into the tool.

## Q4

A per-deliberation manifest is the clean boundary. Field names below are normative.

**File layout (single-deliberation session, per D-019):**
```
provenance/NNN/
  briefs/<perspective>.md
  raw/<perspective>.md
  manifests/<perspective>.manifest.yaml
  synthesis.md
  participants.yaml
```

**`participants.yaml` (session-level index):**
```yaml
session: "NNN"
participants:
  - perspective: archivist
    manifest: manifests/archivist.manifest.yaml
  - perspective: engineer
    manifest: manifests/engineer.manifest.yaml
```

**Per-participant manifest schema:**
```yaml
perspective: archivist
participant_kind: model | human | unknown
# For model participants:
model_family: claude | gpt | gemini | llama | other | unknown
model_id: "claude-opus-4-7"       # exact string as returned by API, or "unknown"
model_version: "20260115"          # or "unknown"
endpoint: "anthropic-api-v1"       # or "web-ui", "local", "unknown"
sampling:
  temperature: 1.0                 # or "unknown"
  top_p: "unknown"
  max_tokens: "unknown"
system_prompt_sha256: "a3f5..."    # hash of exact system prompt
system_prompt_file: "briefs/archivist.md"  # or separate file if system prompt differs from brief
# For human participants:
participant_id: "reviewer-01"      # pseudonym acceptable; must be stable across sessions
participant_role: "domain-expert-<domain>"
contact_channel: "email" | "in-person" | "async-written" | "unknown"
# Common fields:
delivered_at: "2026-04-18T14:00:00Z"
received_at: "2026-04-18T14:47:00Z"
raw_response_file: "raw/archivist.md"
raw_response_sha256: "7b2e..."     # computed from raw file at commit time
transport_notes: "Pasted from web UI; no edits."
edits_post_receipt: false          # MUST be false for raw files
```

**Unknown handling:** the literal string `"unknown"` is required, never blank, never omitted. A missing field is a schema violation caught by `validate.sh`. `"unknown"` is a signal that says "this session could not determine the value", which is itself auditable.

**Post-hoc editing:** the raw file is append-only from commit forward. Any correction lives in `raw/<perspective>.md.correction` with its own hash and a pointer from the manifest. The original raw file is never rewritten. `validate.sh` verifies that `raw_response_sha256` matches the committed file; mismatch is a hard failure.

**Boundary between frontmatter layers:**
- **Raw-output file frontmatter**: minimal — just `perspective` and `committed_at`. The response body is the payload.
- **Manifest**: all identity, version, transport, sampling, integrity fields.
- **Synthesis frontmatter**: cites manifest files, not model IDs directly. Synthesizer never reaches past the manifest into endpoint details.

This keeps the synthesis readable at the methodology layer and pushes all archival detail into the manifest, where a future auditor expects it.

## Q5

**Honestly closing OI-004 requires that a deliberation contain at least one perspective whose reasoning is generated by a system with substantively different training provenance from the Claude family, *and* that this condition holds structurally — not incidentally.**

The structural requirement is the hard part. A single session with one GPT response does not close OI-004 for the methodology; it narrows it for that session. Closure requires:

1. A specified trigger rule (Q3) that makes non-Claude participation a reliable property of the relevant deliberation classes, not a one-off.
2. A recording schema (Q4) that makes the participant heterogeneity auditable.
3. A demonstrated history — at least several sessions — where the non-Claude participant changed the outcome or surfaced a blind spot the Claude perspectives missed. Without demonstrated impact, the mechanism is present but inert.
4. An articulation of what "substantively different training provenance" means, and a named set of acceptable participant kinds.

**This session's mechanism is sufficient for narrowing OI-004, not for closure.**

It is sufficient for narrowing because: it specifies a concrete ingestion path for non-Claude outputs; it preserves auditability; it is adoptable in the next session without new infrastructure. If Session 004 actually includes a non-Claude participant using this mechanism, OI-004 narrows materially — the methodology has moved from "cannot incorporate external perspectives" to "has incorporated external perspectives at least once, with a reusable pattern."

It is not sufficient for closure because: (a) the mechanism does not guarantee non-Claude participation will occur; (b) one session's inclusion does not establish structural property; (c) "substantively different training provenance" remains undefined and will require its own deliberation.

I would recommend the session's decision log explicitly record: *OI-004 remains open; this mechanism is a narrowing tool, not a closure instrument. Closure requires sustained use and a separate decision defining training-provenance diversity thresholds.* Closing OI-004 prematurely would itself be the provenance dishonesty the methodology is designed to avoid.

## Q6

**Strongest objection:** the manifest-based brief-drop pattern outsources reproducibility to human diligence. If the convener pastes a response slightly wrong, edits a typo, strips a preface, or mis-records `delivered_at`, the archival guarantees collapse silently. The mechanism trusts a single human in the loop — the convener — to be perfectly faithful with no tooling support. This is precisely the failure mode archivists of physical correspondence spent centuries learning to distrust.

**Answer:**

I concede the objection partially and refuse it partially.

Concede: the mechanism does depend on convener fidelity, and there is no way to fully automate that dependency away when the participant is a human reviewer or a model accessed via a UI without an API. This is an inherent limit of the "zero new infrastructure" constraint. Any mechanism that claims otherwise is lying about its trust boundaries.

Refuse: the alternative is not "better provenance" but "no non-Claude participation at all until we build tooling." That trades a known, auditable, human-mediated risk for an indefinite delay that leaves OI-004 untouched. The honest position is to name the trust boundary in the provenance itself, not to pretend it doesn't exist.

Concrete mitigations that are cheap and should be part of the mechanism:

1. **Convener attestation field** in the manifest: `convener_attestation: "I confirm the raw_response_file is a verbatim copy of the received response, without edits beyond UTF-8 normalization."` Signed with convener's git identity via commit signature where available.
2. **Integrity hash**: `raw_response_sha256` committed in the manifest at the same commit as the raw file; `validate.sh` verifies on every run. Post-hoc edits become git-detectable.
3. **Separation of roles**: the convener of a deliberation with non-Claude participation is recorded as a named role in the session metadata. Future audits can see which human was the transport.
4. **Acknowledge the trust boundary in the specification itself**: add a Limitations subsection to whatever spec emerges from this session — "human-mediated transport is a trust dependency; the methodology does not automate faithfulness."

These do not eliminate the objection. They make the residual risk visible, bounded, and attributable. That is what archival provenance requires; it is not the same as what cryptographic non-repudiation requires, and the methodology should not claim to offer the latter.

## What I cannot answer from this perspective

I cannot adjudicate whether any specific non-Claude model's training provenance is "substantively different" enough to count toward narrowing OI-004 — that requires judgment about training corpora and methods I do not have authoritative access to, and any claim I made about e.g. GPT or Gemini training would be an external import. I also cannot evaluate the methodology's engineering trade-offs (CLI wrapper vs. manual paste, synchronous vs. asynchronous participation) from the archivist stance; those belong to the engineer perspective. Finally, I cannot determine whether the community of future readers this methodology serves will accept pseudonymous human reviewers as adequate identity, or demand stronger attestation — that is a governance question outside the archival frame.
