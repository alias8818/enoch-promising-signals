# CPU speculative decoding with suffix-LM draft

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-speculative-decoding-with-suffix-lm-draft-2d748ff2872c`
Run ID: `cpu-speculative-decoding-with-suffix-lm-draft-2d748ff2872c-20260628T034705741889+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/426e03455cca

## What looked useful

Suffix-LM drafts can exploit repeated structured suffixes to create accepted multi-token proposals, but the benefit is workload-dependent and disappeared in the out-of-domain control.

## Boundaries and scale limits

Synthetic corpus only; target is not a transformer; no real CPU transformer latency, KV-cache, model-quality, or natural-corpus serving measurements were produced. Out-of-domain control had no target-batch reduction.

## Claim scope

In a synthetic structured-token proxy with an interpolated 5-gram target and variable-order suffix-LM draft, greedy speculative decoding preserved target output and reduced target verification batches by 2.933x at gamma=4; gamma sweep showed 1.693x to 3.016x structured reduction.

## Why it stopped

Current result is a bounded synthetic proxy useful signal, not direct transformer evidence or a paper-ready validation.

## Recommended next action

Run a bounded direct CPU transformer follow-up using a small open model, real tokenizer, suffix/prompt-lookup draft baseline, and measured latency plus acceptance on natural and structured corpora.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU transformer suffix-draft speculative decoding probe
- Success threshold: At least 1.3x measured wall-clock tokens/sec improvement on structured in-domain prompts with identical greedy target output and no improvement claim for controls that fail acceptance.
- Stop condition: Stop if suffix draft acceptance is below 0.4 or measured latency improvement is below 1.1x on the structured split after a smoke plus one bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-speculative-decoding-with-suffix-lm-draft-2d748ff2872c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
