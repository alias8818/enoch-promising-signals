# Multi-Codebook Residual Vector Quantization for KV Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-codebook-residual-vector-quantization-for-kv-cache-57743870fd44`
Run ID: `multi-codebook-residual-vector-quantization-for-kv-cache-57743870fd44-20260602T182213718009+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/878afbbb9b2b

## What looked useful

On correlated KV-like synthetic vectors, 8x256 RVQ reached attention relative MSE 6.03e-05 and cosine 0.999987, better than per-channel int4 attention MSE 2.56e-04, but at 5.0 effective bits/dim including per-run codebook overhead at 8192 vectors. On Gaussian vectors, 8x256 RVQ attention MSE was 0.363 versus int4 at 0.0561, an early warning that the method relies on exploitable activation structure.

## Boundaries and scale limits

No real transformer KV traces, no end-to-end perplexity/token-agreement test, no fused serving kernel, and no long-context production workload. Codebook overhead was counted for a single 8192-vector sequence and would need offline/shared amortization to make the code-only bit rate meaningful.

## Claim scope

Synthetic GPU benchmark of residual vector quantization for KV-cache-shaped tensors: RVQ preserves attention output on low-rank correlated KV-like vectors when using enough residual codebooks, but fails on unstructured Gaussian vectors and depends on codebook amortization.

## Why it stopped

No-paper closure: the result is a reproducible synthetic/proxy useful signal, not direct model or serving evidence.

## Recommended next action

Run a bounded direct-evidence follow-up on real GPT-2-small or distilgpt2 KV traces, with held-out prompts and equal-effective-bit comparisons against int4/groupwise baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: RVQ KV Cache on Real GPT-2-Class Activations
- Success threshold: At equal effective bits, RVQ must reduce held-out attention-output relative MSE by at least 2x versus int4 or maintain perplexity delta within 5% of int4 while using at least 25% fewer amortized cache bits.
- Stop condition: Stop if real held-out KV traces show RVQ attention-output error worse than int4 at equal effective bits in two model layers or if decode overhead exceeds the memory-bandwidth savings in a GPU microbenchmark.

## Evidence references

- Artifact root: `<local-path>/projects/multi-codebook-residual-vector-quantization-for-kv-cache-57743870fd44`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
