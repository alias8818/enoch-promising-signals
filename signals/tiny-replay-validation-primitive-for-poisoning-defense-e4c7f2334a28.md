# Tiny Replay-Validation Primitive for Poisoning Defense

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-replay-validation-primitive-for-poisoning-defense-e4c7f2334a28`
Run ID: `tiny-replay-validation-primitive-for-poisoning-defense-e4c7f2334a28-20260613T172201524361+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6380573564f9

## What looked useful

A tiny replay-validation primitive dominated accept-all and keyword-only baselines in the scoped test: replay_validation poison_accept_rate=0.000, benign_accept_rate=1.000, downstream_compromise_rate=0.000; keyword_blocklist poison_accept_rate=0.750 and downstream_compromise_rate=1.000; accept_all poison_accept_rate=1.000 and downstream_compromise_rate=1.000.

## Boundaries and scale limits

Evidence is synthetic and structured: 1,000 generated tasks, 6,000 memory candidates, three deterministic policies, no LLM extraction, no paraphrase entailment, no real user transcripts, no adaptive attacker against the validator, and no production agent integration.

## Claim scope

In a deterministic synthetic repeated-agent memory setting with trusted/untrusted source events, exact key/value fact replay, and instruction-pollution attacks, source-bound replay validation blocked all generated poison candidates while retaining all benign candidates.

## Why it stopped

No-paper closure: this run produced a useful bounded synthetic signal, but the evidence is not direct enough for paper-positive claims about real LLM-agent poisoning defense.

## Recommended next action

Run a bounded deepen follow-up that replaces structured facts with LLM-generated memory candidates from natural-language transcripts and measures replay-validation precision/recall against adaptive poison prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language replay validation against adaptive memory poisoning prompts
- Success threshold: Poison acceptance <= 5%, downstream compromise <= 5%, and benign acceptance >= 90% across at least 300 labeled natural-language candidates.
- Stop condition: Stop early as unsupported if replay validation rejects more than 20% benign candidates or accepts more than 20% poison candidates after the first 100 labeled candidates.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-replay-validation-primitive-for-poisoning-defense-e4c7f2334a28`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
