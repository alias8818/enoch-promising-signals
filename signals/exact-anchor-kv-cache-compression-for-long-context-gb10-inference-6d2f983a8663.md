# Exact-Anchor KV Cache Compression for Long-Context GB10 Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-cache-compression-for-long-context-gb10-inference-6d2f983a8663`
Run ID: `exact-anchor-kv-cache-compression-for-long-context-gb10-inference-6d2f983a8663-20260605T151805373583+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/ffc50c4ab94f

## What looked useful

4-bit non-anchor quantization reached about 3.6x KV memory reduction with low error on correlated synthetic KV, but exact anchors added only marginal protection over all-token quantization and 2-bit compression produced large attention-output error.

## Boundaries and scale limits

No trained long-context model, no real KV traces, no downstream quality metrics, and no fused mixed-precision attention kernel were tested. Runtime measurements are for a naive dequantize-then-attend PyTorch implementation.

## Claim scope

GB10 proxy attention-primitive benchmark at sequence length 16384, 8 heads, head dimension 64, with synthetic iid and locally correlated KV tensors; exact FP16 anchors every 64 tokens and per-vector quantized non-anchor KV.

## Why it stopped

Proxy attention-primitive evidence does not support the stronger exact-anchor mechanism as a paper-ready result; anchor-specific gains were small and naive runtime was slower than FP16.

## Recommended next action

Stop this run as no-paper useful evidence; test a bounded real-model follow-up using actual transformer KV traces and compare exact anchors against all-token and content-aware quantization at equal memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Exact-Anchor KV Quantization Ablation
- Success threshold: At matched memory near 3.5x compression, anchor-based compression improves retrieval accuracy or logit drift by at least 20% relative over all-token 4-bit quantization without increasing decode latency by more than 10% in a serving-relevant implementation.
- Stop condition: Stop if real KV traces show less than 5% relative improvement over all-token quantization at matched memory or if latency remains slower without a credible fused-kernel path.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-cache-compression-for-long-context-gb10-inference-6d2f983a8663`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
