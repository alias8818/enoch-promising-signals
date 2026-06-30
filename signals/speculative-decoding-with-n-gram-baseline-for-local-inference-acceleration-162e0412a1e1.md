# Speculative Decoding with N-gram Baseline for Local Inference Acceleration

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `speculative-decoding-with-n-gram-baseline-for-local-inference-acceleration-162e0412a1e1`
Run ID: `speculative-decoding-with-n-gram-baseline-for-local-inference-acceleration-162e0412a1e1-20260607T112605187406+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a400e038d654

## What looked useful

Exact n-gram prompt-lookup speculation produced 2.68x-3.57x median speedups on repeated GPT-2 prompts by cutting target forwards from 64 to 17-23; tiny-gpt2 was slower, showing fixed overhead can erase the benefit on very small models.

## Boundaries and scale limits

Evidence is limited to one small GPU-resident GPT-2-class model, short 64-token generations, three synthetic prompt classes, single-request timing, no production KV-cache serving stack, no batching, no sampling, and no real prompt trace distribution.

## Claim scope

On a local NVIDIA GB10 running Hugging Face gpt2 greedy decoding, an exact n-gram prompt-lookup speculative decoder reduced target forwards and wall-clock latency for 64-token generations on synthetic repeated log/code prompts while preserving byte-for-byte greedy output.

## Why it stopped

Evidence supports the local mechanism but is synthetic and small-scale, so it is insufficient for a publication-grade broad inference-acceleration claim.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next test is a bounded production-style benchmark on a 1B-7B local model with KV caching and real prompt traces bucketed by repetition rate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache n-gram speculation on real prompt traces
- Success threshold: High-repetition bucket p50 latency speedup >= 1.3x, p95 speedup >= 1.1x, exact output match on all deterministic requests, and low-repetition bucket slowdown <= 5%.
- Stop condition: Stop if KV-cache-aware verification cannot preserve exact greedy output, or if high-repetition p50 speedup is below 1.1x while low-repetition prompts slow down by more than 5%.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-n-gram-baseline-for-local-inference-acceleration-162e0412a1e1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
