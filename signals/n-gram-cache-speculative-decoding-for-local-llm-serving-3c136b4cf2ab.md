# N-gram Cache Speculative Decoding for Local LLM Serving

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-cache-speculative-decoding-for-local-llm-serving-3c136b4cf2ab`
Run ID: `n-gram-cache-speculative-decoding-for-local-llm-serving-3c136b4cf2ab-20260523T153634546655+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d616f470598f

## What looked useful

A self-contained benchmark showed exact greedy-output matches in all tested cases. Distilgpt2 prompt-only cache reduced target forwards by 76.6% on repeated prompts and 60.4% on code-like prompts, but gave 0.0% reduction on short non-repetitive mixed prompts. Full-history cache improved aggregate reductions further but partly exploited generated newline loops.

## Boundaries and scale limits

Evidence is limited to synthetic prompts, isolated single-process CUDA inference, greedy decoding, and tiny/distilgpt2 models. It does not validate 7B+ models, production request traces, sampling, batching, paged KV cache integration, or multi-user serving throughput.

## Claim scope

On small GPT-2-class causal LMs running locally on GB10, exact greedy n-gram cache speculative decoding can reduce target-model verification calls and latency for repeated prompt/code-like contexts while preserving exact greedy output.

## Why it stopped

Bounded local evidence supports the mechanism but remains synthetic/small-model and not publication-grade for broad local LLM serving claims.

## Recommended next action

Stop this run as no-paper useful signal; next direct evidence should integrate the prompt-only n-gram proposer into a real local serving stack and test a 7B-class model on real request traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Server-level prompt n-gram speculative decoding on 7B local traces
- Success threshold: At least 15% p50 latency reduction and 10% p95 latency reduction on repeated/code-heavy trace slices, no output mismatches in greedy mode, and no more than 3% latency regression on non-repetitive slices.
- Stop condition: Stop if prompt-only acceptance stays below 20% or end-to-end latency improves by less than 5% on repeated/code-heavy traces after KV-cache-aware integration.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cache-speculative-decoding-for-local-llm-serving-3c136b4cf2ab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
