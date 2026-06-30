# KV-cache and batching controls for n-gram speculative GPT-2 decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-and-batching-controls-for-n-gram-speculative-gpt-6bebb401ea`
Run ID: `kv-cache-and-batching-controls-for-n-gram-speculative-gpt-6bebb401ea-20260603T223303950374+0000`

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

- Parent run decision: N-Gram Speculative Draft for GPT-2 Inference on Home GPUs: enoch://control-plane/projects/n-gram-speculative-draft-for-gpt-2-inference-on-home-gpus-4e0d400ec304/runs/n-gram-speculative-draft-for-gpt-2-inference-on-home-gpus-4e0d400ec304-20260603T184345347360+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/810c7576d010

## What looked useful

KV-cache reuse matters for n-gram speculative GPT-2 decoding: full-prefix recompute had similar acceptance and forward-count behavior but was slower than greedy KV, while KV speculative decoding was faster and preserved greedy outputs. Batched verifier calls also showed near batch-size row-throughput improvement in the controlled equal-length case.

## Boundaries and scale limits

Only 4 hand-built repeated prompts, 64 generated tokens per prompt, greedy decoding only, equal-length batch verifier microbench, no realistic prompt distribution, no heterogeneous batch scheduler, no larger-model validation, and no serving latency distribution.

## Claim scope

On four short repeated prompts with GPT-2-small greedy decoding on GB10, n-gram speculative decoding with KV-cache verifier reuse matched greedy output, reduced target forwards per generated token from about 1.02 to 0.66, improved mean throughput from 321.90 to 415.38 tokens/s, and an equal-length 8-row verifier microbench showed 7.95x row-throughput speedup from batching.

## Why it stopped

Tier 1 direct test completed and supports the mechanism, but the evidence is too narrow and synthetic/repetitive for paper readiness.

## Recommended next action

Run a bounded deepen benchmark on a real-text GPT-2 prompt suite with heterogeneous batch lengths, acceptance histograms, padding waste, tokens/s, and p50/p95 latency versus greedy KV and recompute controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text heterogeneous batching benchmark for n-gram speculative GPT-2 decoding
- Success threshold: Speculative KV matches greedy outputs on all prompts, improves mean tokens/s by at least 15% over greedy KV at one heterogeneous batch setting, and does not regress p95 per-token latency by more than 10%; recompute control remains slower than KV speculative decoding.
- Stop condition: Stop if acceptance falls below 40% on real-text prompts or if heterogeneous batching overhead removes the throughput advantage in all tested batch settings.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-and-batching-controls-for-n-gram-speculative-gpt-6bebb401ea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
