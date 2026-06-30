# 4-bit Memory-Mapped KV for 64k

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-memory-mapped-kv-for-64k-333c9be48ca8`
Run ID: `4-bit-memory-mapped-kv-for-64k-333c9be48ca8-20260523T223913960510+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/032903e20ec6

## What looked useful

The storage mechanism is viable and reproducible at 64k, but naive int4 mmap decode is 1.39x slower than fp16 at 65,536 context despite 3.76x lower storage, with synthetic attention output relative RMSE around 9-11%.

## Boundaries and scale limits

Test used synthetic KV tensors only: 4 layers, 8 heads, head_dim 64, 65,536 tokens, single-process CPU NumPy on GB10 host. It did not test real model KV distributions, perplexity, generation quality, fused GPU kernels, batch serving, or cold page-cache behavior.

## Claim scope

In a local synthetic NumPy mechanism probe, a 4-layer 64k-token KV-like cache can be stored in memory-mapped int4 format with fp16 per-vector scales at 3.76x smaller size than fp16 and reopened for decode-style attention reads, but the naive CPU int4 decode path is slower than fp16.

## Why it stopped

Synthetic mechanism evidence is insufficient for a paper and shows a naive CPU implementation is slower than fp16; this is not a full validation of 4-bit memory-mapped KV for real 64k LLM serving.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should integrate the mmap int4 cache into a real small transformer decode loop with fp16 and 8-bit baselines before any larger serving claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model 64k decode quality and fused-kernel feasibility for int4 mmap KV
- Success threshold: Int4 mmap KV stays within 5% perplexity/loss of fp16, beats fp16 KV storage by at least 3x including metadata, and matches or improves fp16 decode latency at 64k in the optimized path.
- Stop condition: Stop if real-model loss degrades by more than 10% versus fp16 or optimized int4 decode remains slower than fp16 by more than 10% at 64k.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-memory-mapped-kv-for-64k-333c9be48ca8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
