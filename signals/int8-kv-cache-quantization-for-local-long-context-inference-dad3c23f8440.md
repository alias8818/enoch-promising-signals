# INT8 KV cache quantization for local long-context inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-kv-cache-quantization-for-local-long-context-inference-dad3c23f8440`
Run ID: `int8-kv-cache-quantization-for-local-long-context-inference-dad3c23f8440-20260529T063011363821+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2ce92ee43bde

## What looked useful

INT8 KV plus fp16 per-token scales used 50.78% of FP16 storage and kept cosine similarity around 0.999956, but decode latency was 2.5x to 4.4x slower than FP16 as context increased from 2K to 32K. The mechanism is memory-useful but not practical locally without fused dequantization inside attention.

## Boundaries and scale limits

Synthetic random tensors only; no real LLM perplexity or generation evaluation; no fused INT8 attention kernel; single-batch one-token decode only; not a full serving benchmark or publication-grade validation.

## Claim scope

On NVIDIA GB10 using a synthetic one-token grouped-query attention microbenchmark with 32 query heads, 8 KV heads, head_dim 128, and 2K-32K context, per-token symmetric INT8 KV storage roughly halves cache bytes and preserves attention outputs, but an unfused PyTorch dequantize-before-attention path is substantially slower than FP16.

## Why it stopped

Closed as no-paper useful signal because the direct local proxy showed strong memory savings and low synthetic error, but the unfused implementation was 2.5x-4.4x slower; this is an early bounded falsification of naive INT8 KV cache quantization as a practical latency improvement, not a full validation.

## Recommended next action

Run a bounded fused-kernel deepen test: implement or use a CUDA/Triton INT8 KV attention path and require near-FP16 decode latency plus a real-model quality check before considering further scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused INT8 KV decode attention on GB10
- Success threshold: INT8 KV storage at <=55% of FP16, fused INT8 decode median latency <=1.15x FP16 at both 16K and 32K, attention cosine similarity >=0.9999, and real-model perplexity drift <=1%.
- Stop condition: Stop if fused INT8 decode remains >1.5x FP16 at 16K context or if real-model quality drift exceeds 1% under the same quantization policy.

## Evidence references

- Artifact root: `<local-path>/projects/int8-kv-cache-quantization-for-local-long-context-inference-dad3c23f8440`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
