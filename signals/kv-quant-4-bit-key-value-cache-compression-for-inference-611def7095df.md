# KV-quant: 4-bit key-value cache compression for inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-quant-4-bit-key-value-cache-compression-for-inference-611def7095df`
Run ID: `kv-quant-4-bit-key-value-cache-compression-for-inference-611def7095df-20260611T002721831007+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d8ae7b0184f5

## What looked useful

4-bit KV quantization delivered 3.20x-3.56x theoretical KV-cache compression after group metadata, but caused meaningful decode-attention drift: relative output L2 was 0.112 on normal tensors and 0.267-0.326 under 1% outlier stress; top-1 attention agreement fell to 0.75 in the outlier group-32 case. 8-bit controls stayed much closer to fp16. Naive dequantization was about 10.3x-10.9x slower than fp16 attention, so memory compression alone does not imply latency improvement.

## Boundaries and scale limits

No pretrained model traces, perplexity, generation quality, fused packed int4 kernel, long-context serving, or multi-model validation were run. Runtime numbers are naive PyTorch dequantize-plus-attention, not optimized int4 inference.

## Claim scope

Synthetic GPU decode-attention probe for per-vector affine groupwise 4-bit K/V cache quantization at batch 4, 16 heads, sequence length 2048, head dimension 128 on NVIDIA GB10.

## Why it stopped

Synthetic/proxy evidence supports an early cautionary result but not a full validation or publication-grade positive claim.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should use real KV traces from a small pretrained transformer and include an outlier-aware 4-bit variant plus fp16 and 8-bit controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace outlier-aware 4-bit KV cache quantization
- Success threshold: At least 2.5x effective KV-cache compression with less than 1% perplexity or NLL degradation versus fp16 and no worse than 0.02 mean attention KL on real traces.
- Stop condition: Stop if naive or outlier-aware 4-bit quantization exceeds 3% perplexity or NLL degradation, loses more than 25% top-1 attention agreement on real traces, or cannot exceed 2.0x effective compression after metadata and residual windows.

## Evidence references

- Artifact root: `<local-path>/projects/kv-quant-4-bit-key-value-cache-compression-for-inference-611def7095df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
