# N-Gram Suffix Local Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-suffix-local-speculative-decoding-1f49fabb16e8`
Run ID: `n-gram-suffix-local-speculative-decoding-1f49fabb16e8-20260529T145743409808+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f20cb0e4924a

## What looked useful

Ordered traces substantially outperform shuffled-token controls. Best word-token result was Python stdlib at 1.90 tokens per target call and 47.4% target-call reduction. Best byte-token result was Python stdlib at 3.38 tokens per target call and 70.4% target-call reduction. Word-level prose was weaker at 1.11-1.24 tokens per call.

## Boundaries and scale limits

Proxy-only trace evidence on Gutenberg prose and Python standard-library code; no real causal LM, no model tokenizer, no GPU serving latency, no KV-cache measurement, and no stochastic generation quality evaluation.

## Claim scope

A CPU trace-oracle benchmark found that online local n-gram suffix copying can reduce target verification calls on ordered text/code streams, especially code and byte-token traces, before accounting for real model-serving overhead.

## Why it stopped

Closed as no-paper useful signal because this run supports the mechanism only in a trace oracle; it is not direct model-serving validation.

## Recommended next action

Run a bounded direct speculative decoding implementation on a small causal LM using the model tokenizer and report wall-clock tokens/s, target calls, acceptance, draft overhead, and KV-cache behavior on prose and code prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Small-LM Test of N-Gram Suffix Speculative Decoding
- Success threshold: At least 15% wall-clock tokens/s improvement on code prompts with no more than 5% regression on prose prompts, over at least 100 prompts per domain on a small locally runnable causal LM.
- Stop condition: Stop if accepted tokens per target call is below 1.10 or draft overhead erases wall-clock gains on both prose and code prompt sets.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-local-speculative-decoding-1f49fabb16e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
