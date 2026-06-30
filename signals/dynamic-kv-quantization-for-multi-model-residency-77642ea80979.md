# Dynamic KV Quantization for Multi-Model Residency

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-kv-quantization-for-multi-model-residency-77642ea80979`
Run ID: `dynamic-kv-quantization-for-multi-model-residency-77642ea80979-20260528T053553283672+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b47b93fd62bd

## What looked useful

Dynamic idle-only KV quantization is mechanically plausible for increasing idle-context residency, but only if the scheduler dequantizes once when a model becomes active and keeps active KV in fp16. Naive per-token dequantization is a latency regression.

## Boundaries and scale limits

This run did not use real model weights, real request traces, fused low-precision attention kernels, a paged KV cache, quality/perplexity evaluation, or simultaneous multi-model serving. Model-weight residency was excluded from the capacity calculation.

## Claim scope

On a GB10 with synthetic KV tensors up to heads=32, sequence=8192, head_dim=128, storing inactive KV cache as symmetric int8 with block scales roughly halves KV bytes and a one-time fp16 dequantization on reactivation amortizes after about 3.6-6.4 fp16 decode-token equivalents. Dequantizing every decode step is 4.4-7.5x slower than fp16 attention in the naive PyTorch implementation.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a synthetic GPU probe and analytical capacity estimate, not an end-to-end serving validation.

## Recommended next action

Run a bounded real-model deepen test with a tiny or GPT-2-small-class transformer, two resident model instances, an idle-KV int8 policy, and measured p50/p95 switch latency, decode throughput, memory, and perplexity/quality deltas.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model idle KV quantization scheduler probe
- Success threshold: At least 1.8x idle KV residency improvement, less than 10% steady-state decode throughput loss after reactivation, p95 switch latency below 25 ms, and no more than 1% relative perplexity degradation on the selected bounded workload.
- Stop condition: Stop as negative if real-model quality degradation exceeds 1% relative perplexity, p95 switch latency exceeds 25 ms, or steady-state throughput loss exceeds 10% after reactivation.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-kv-quantization-for-multi-model-residency-77642ea80979`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
