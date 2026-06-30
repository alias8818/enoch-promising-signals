# Anchor-Indexed KV State Compression for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-indexed-kv-state-compression-for-cpu-inference-39d6c91775ff`
Run ID: `anchor-indexed-kv-state-compression-for-cpu-inference-39d6c91775ff-20260531T191740944363+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1c64bc485425

## What looked useful

Anchor-indexed int8 residuals reduced attention-output error on locally correlated synthetic KV versus plain int8, but the reconstruct-then-attend CPU path was much slower than full-cache attention, with median anchor speedup only 0.187x overall and 0.147x on correlated KV.

## Boundaries and scale limits

Synthetic KV only; no real LLM KV traces, perplexity/task quality, end-to-end generation, or fused dequantize-attention CPU kernel. Contexts were limited to 8192 tokens with 8 heads and head dimension 64.

## Claim scope

CPU NumPy microbenchmark of single-token attention over synthetic KV caches, comparing full float32 K/V attention with anchor-plus-int8-residual K/V reconstructed before attention.

## Why it stopped

Bounded synthetic cache/attention evidence falsifies the naive reconstruct-before-attention CPU latency path; this is not a full validation of all possible fused implementations.

## Recommended next action

Stop this run as no-paper evidence; the next bounded test should implement a fused CPU dequantize-attention kernel on small real-model KV traces and require latency parity plus acceptable attention or perplexity error.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused CPU dequantize-attention test for anchor-indexed KV compression
- Success threshold: At least 1.0x latency versus the full-KV baseline, at least 1.5x KV memory reduction versus fp16-equivalent KV, and no more than 0.5% relative perplexity degradation or an attention-output relative L2 error below 0.001 on real-model traces.
- Stop condition: Stop if the fused implementation remains below 0.9x baseline latency at context length 2048 or larger, or if real-model KV traces lose the anchor error advantage over plain int8.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-kv-state-compression-for-cpu-inference-39d6c91775ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
