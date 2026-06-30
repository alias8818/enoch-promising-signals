# Prompt-Anchored N-gram Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-anchored-n-gram-speculative-decoding-on-cpu-755be5b2c60e`
Run ID: `prompt-anchored-n-gram-speculative-decoding-on-cpu-755be5b2c60e-20260524T002540948921+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7818fde4346a

## What looked useful

On copy-heavy prompts, prompt-anchored n-gram drafts were often accepted and reduced target model calls by 35.9-40.1% with 1.39-1.48x mean speedup while preserving exact greedy output. Controls without repeated suffixes produced no drafts and stayed near baseline. Long drafts can hurt when partial acceptance forces cache repair.

## Boundaries and scale limits

Only distilgpt2 plus a tiny smoke model; only greedy decoding; six hand-authored prompts; no production traces, larger quantized models, optimized KV-cache slicing, sampling, or long-context serving benchmark.

## Claim scope

Small CPU benchmark with distilgpt2 on six hand-authored prompts: exact greedy prompt-anchored n-gram speculative decoding helps copy-heavy repeated-prompt continuations but not broad non-repetition controls.

## Why it stopped

No-paper useful signal: direct small-model evidence supports the mechanism only in a narrow copy-heavy setting and is insufficient for a broad CPU speculative decoding claim.

## Recommended next action

Run a bounded deepen follow-up on real RAG/chat prompt traces with an adaptive max-draft policy and an inference backend that supports cheap KV-cache cropping.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive prompt-lookup speculative decoding on real CPU prompt traces
- Success threshold: Median speedup >= 1.2x overall, copy-heavy subset speedup >= 1.5x, p10 slowdown no worse than 0.95x, and exact greedy token equivalence on every prompt.
- Stop condition: Stop if acceptance on real traces is below 20% or if non-copy prompts slow down by more than 10% after adaptive gating.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-anchored-n-gram-speculative-decoding-on-cpu-755be5b2c60e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
