# Tiered KV eviction to DRAM for 2x local context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiered-kv-eviction-to-dram-for-2x-local-context-6a63193073a2`
Run ID: `tiered-kv-eviction-to-dram-for-2x-local-context-6a63193073a2-20260523T061644565520+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/01c8b93e0fc7

## What looked useful

Exact DRAM-tiered KV can preserve 2W attention outputs, but only by reading the evicted half every decode step. Ignoring evicted KV is not equivalent to 2W context, and rereading it naively is bandwidth-dominated.

## Boundaries and scale limits

No real transformer serving stack, fused attention kernel, batching, asynchronous overlap, real prompt quality, or 7B+ model run was tested. The evidence falsifies the naive exact reread mechanism as a practical standalone method, but not sparse retrieval or carefully overlapped tiered KV systems.

## Claim scope

Synthetic GB10 PyTorch microbenchmarks of fp16 decoder KV attention show that exact tiering of a 2W local window by keeping W recent KV on GPU and rereading W old KV from DRAM is numerically exact and halves GPU-resident KV bytes, but naive per-token reread adds 1.98x-4.35x latency versus GPU-only 2W attention at tested sizes and extrapolates to about 8 GiB of DRAM reads, or about 148.6 ms copy time, per generated token for a Llama-7B-like 16k-token evicted half.

## Why it stopped

Proxy microbenchmark early-falsified the naive exact tiered-KV design for practical 2x local context: exactness requires old-half DRAM traffic every token, while the no-reread variant is not 2W attention.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test sparse or overlapped retrieval rather than naive full old-half reread.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sparse or overlapped tiered KV retrieval for bounded long-context decode
- Success threshold: For at least a GPT-2-small-class or comparable toy decoder, achieve exact or quality-matched access to useful evicted KV with less than 25% tokens/sec overhead versus GPU-only 2W attention when the GPU-only cache fits, and at least 1.8x reduction in GPU-resident KV bytes.
- Stop condition: Stop if old-KV transfer remains above 50% of per-token latency after overlap/sparsity, or if quality matches W-only recent attention rather than the 2W baseline.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-kv-eviction-to-dram-for-2x-local-context-6a63193073a2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
