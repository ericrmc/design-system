---
session: 032
title: L1a Thin-Prompt Canary Verdict — PD-A (Rule of St. Benedict Ch 58)
date: 2026-04-23
status: complete
cell: 1
step: l1a-canary
candidate: PD-A
verdict: PASS
---

# L1a Thin-Prompt Canary Verdict

## §1 Test inputs

- **Thin prompt** (`cell1/l1a-thin-prompt.txt`): "A community wants to admit a new permanent member. The admission decision will be irreversible. The community already has established members and a hierarchical structure. Design the admission procedure, from first approach to final acceptance. Output is the procedure itself, as a structured text. Approximately 400-500 words."
- **Non-Claude family**: codex exec v0.121.0; model `gpt-5.4`; provider `openai`; reasoning `xhigh`; sandbox read-only; session id `019db900-4dcc-7322-a5d1-2e89bfd254ae`. Raw output at `cell1/l1a-codex-raw.txt`.
- **Claude family**: Agent tool `general-purpose` subagent; isolated context. Raw output at `cell1/l1a-claude-raw.md`.

## §2 Reference-distinctive markers checked (mechanical grep audit)

Per `reference-validation.md` v2 §4 L1a: "reject on spontaneous emission of reference's idiosyncratic structure, labels, or sequence." Distinctive markers for PD-A (Rule of St. Benedict Ch 58):

| Marker | Codex | Claude | Status |
|---|---|---|---|
| "Benedict" | absent | absent | clean |
| "Rule" (proper noun referring to RSB) | absent | absent | clean |
| "Suscipe" / "Suscipe me, Domine" | absent | absent | clean |
| "novice" / "novitiate" | absent | absent | clean |
| "abbot" / "abbess" | absent | absent | clean |
| "monastery" / "monastic" / "monk" | absent | absent | clean |
| "convent" / "cloister" | absent | absent | clean |
| "oratory" | absent | absent | clean |
| "altar" | absent | absent | clean |
| "stability" + "conversion of life" + "obedience" three-vow formula | absent | absent | clean |
| "Rule" reading at intervals (2/6/4 month or 12-month divided) | absent | absent | clean |
| 4-day gate-knocking pattern | absent | absent | clean |
| Prostration before assembly | absent | absent | clean |
| Petition placed on altar | absent | absent | clean |
| "ora et labora" | absent | absent | clean |
| "religious", "vow", "consecration", "ordination" | absent | absent | clean |

**Verdict: clean on all distinctive markers in both model families.**

## §3 Structural-genre observation

Both outputs converge on a similar generic-civic-bureaucratic admission structure:
- Sponsor / sponsorship requirement (codex stage 2; Claude stage 1)
- Multi-month probationary observation (codex 6 months; Claude 12 months)
- Senior council review (codex stage 6; Claude stage 4)
- Public objection period of 30 days (codex stage 7; Claude stage 5)
- Supermajority vote (codex stage 8 with head-confirmation; Claude stage 6 with 4/5 + 2/3 quorum)
- Final ratification + permanent record (codex stage 9; Claude stage 7+8)

This convergence is **constraint-derivable** (the constraints request graduated commitment, multiple exit points, asymmetric authority, public ceremony, and resolve-testing — all present in both outputs). The convergence does NOT match RoSB's specific structure:

- RoSB has 4 distinct phases: (1) repeated rejection at gate to test resolve over ~4 days; (2) brief guesthouse stay; (3) novitiate of 12 months under senior monk's tutelage with three formal Rule-readings at 2-month / 6-month / 4-month intervals each followed by explicit "leave or stay" offer; (4) final profession in oratory with three vows + altar petition + prostration + threefold "Suscipe me, Domine" sung by novice and community.
- Codex has 9 stages including modern bureaucratic markers (Membership Steward; Eligibility Review; Disclosure Statement; Membership Council; supermajority + head ratification; covenant signing; official register).
- Claude has 8 stages including modern civic markers (3-year-tenure sponsor with reputational liability; Council of Elders; written examination in camera; 4/5 supermajority + 2/3 quorum; binding oath with sponsor co-signature; sponsor's 3-year continuing guarantee).

The shared genre features (sponsor; probation; council review; objection period; supermajority; public ceremony) are present across many real-world admission procedures (professional bodies, fraternal societies, citizenship procedures, cooperative memberships). They do not constitute RoSB-distinctive emission.

## §4 §1 C3 Stage (a) verdict

**PASS for both model families.** No spontaneous emission of RoSB's idiosyncratic structure, labels, or sequence under thin-prompt conditions.

Per v2 §4 L1a, **L1a survival is necessary but not sufficient**: the WX-18-2 finding (Session 018) showed thin prompts under-detect saturation when triggering content is distributed across requirements rather than concentrated in problem-shape. The L1b full-constraint test (next step) is the discriminating gate.

## §5 Honest limits

- **Mechanical grep is exhaustive on the listed markers.** Other RoSB-distinctive features the survey did not enumerate could in principle slip through. Manual structural review (above §3) confirms no qualitative match to RoSB's 4-phase structure either.
- **Both outputs default to "modern committee governance" priors** — neither attempts traditional/religious/historical framings even without explicit modern-context constraint. This may indicate that the thin prompt's "hierarchical structure" + "irreversible" + "permanent member" combination triggers HR/civic templates more strongly than religious-formation templates. The L1b full constraint statement (with constraint 10's "no specialised modern infrastructure" tip-toward-pre-modern) tests whether RoSB-shaped output emerges when the modern-context defaults are blocked.

## §6 Next step

Proceed to L1b full-constraint saturation test with the full constraint statement from `cell1/01-constraint-statement.md` §3 / `cell1/constraint-prompt.txt`.
