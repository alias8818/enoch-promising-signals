# Tiered CPU-GPU Anchor Pinning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiered-cpu-gpu-anchor-pinning-2b8a8da09ef3`
Run ID: `tiered-cpu-gpu-anchor-pinning-2b8a8da09ef3-20260604T223122746591+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a52a6c210eec

## What looked useful

Exact tiered anchor pinning reached median parity with CPU offload and won 8/16 shapes, max 1.23x; naive exact tiering lost in 14/16 shapes. Anchor-only was 1.7-21.5x faster than CPU offload but had high relative output error on random attention, so speed alone is not evidence of viable model behavior.

## Boundaries and scale limits

Tested synthetic KV/query tensors only, sequence lengths 1024-16384, 8 heads, head dim 64, single decode query, PyTorch eager kernels. Did not test real transformer quality, serving batches, paged KV caches, fused attention kernels, or long memory-pressure runs.

## Claim scope

On NVIDIA GB10 with PyTorch fp16 synthetic single-query attention, exact tiered CPU-GPU anchor pinning is not a general latency win over pinned CPU KV offload; an optimized exact chunked implementation gives only shape-dependent gains up to 1.23x, while full GPU residency remains much faster.

## Why it stopped

Proxy microbenchmarks falsified the broad claim as paper-ready: exact tiering is only modest and shape-dependent, and anchor-only is inaccurate on synthetic random attention. This is not full validation of real-model anchor policies.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test real GPT-2-small attention traces with attention-sink or learned-anchor selection before any larger serving work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model trace test for anchor-only and selective-cold-fetch KV policies
- Success threshold: At least one bounded anchor policy preserves validation loss or perplexity within 2% of full attention and improves median decode-step latency by >=1.5x over pinned CPU offload for two sequence lengths >=8192.
- Stop condition: Stop if anchor policies require fetching more than 50% of cold KV on median steps, exceed 2% quality degradation, or fail to beat pinned CPU offload by 1.5x on the target shapes.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-cpu-gpu-anchor-pinning-2b8a8da09ef3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
