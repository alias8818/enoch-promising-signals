# INT8 KV-Cache for Long-Context CPU Inference with Quality Gates

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-kv-cache-for-long-context-cpu-inference-with-quality-gates-a2ebef0462c9`
Run ID: `int8-kv-cache-for-long-context-cpu-inference-with-quality-gates-a2ebef0462c9-20260610T164301888869+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bc2847f32b96

## What looked useful

Per-tensor INT8 is compact and sometimes faster but fails quality gates under outliers. Per-token INT8 passes Gaussian cases but fails outlier gates at all tested lengths. Per-token group-16 scaling passes all outlier cases, including 8192 tokens with min cosine 0.999712 and relative L2 0.02040, at 3.2x compression, but is 3.43x slower than FP32 in the 8192-token outlier case.

## Boundaries and scale limits

No real transformer model, perplexity, task quality, fused INT8 CPU kernel, multi-layer serving loop, or context beyond 8192 tokens was tested. Timing reflects NumPy dequantization plus FP32 attention rather than production optimized INT8 kernels.

## Claim scope

Synthetic CPU decode-attention benchmark shows that INT8 KV caches can reduce KV storage by 3.2x to 4.0x, and group-of-16 per-token scaling preserves attention-output quality under a 1% outlier stress test through 8192 tokens, but the unfused NumPy dequantize-then-attend path is slower than FP32 for the robust variants.

## Why it stopped

Closed as no-paper useful signal: local synthetic evidence supports the scale-granularity quality mechanism but does not validate an end-to-end long-context CPU inference system or a production latency win.

## Recommended next action

Run a bounded real-model CPU decode experiment with FP32, per-token INT8, and group-16 INT8 KV caches, measuring perplexity/generation quality plus the same attention-output gates and using a model-integrated or optimized dequantization path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU decode validation for grouped INT8 KV-cache gates
- Success threshold: Group-16 INT8 achieves at least 3.0x KV-cache compression, passes cosine/KL/relative-L2 gates, keeps real-model perplexity or logit divergence within a predeclared tolerance, and avoids more than 20% decode throughput regression after integration or kernel optimization.
- Stop condition: Stop if real-model quality gates fail for group-16 INT8 at 2048 or 8192 tokens, or if integrated CPU decode remains more than 50% slower than FP32 after straightforward batching/dequantization optimization.

## Evidence references

- Artifact root: `<local-path>/projects/int8-kv-cache-for-long-context-cpu-inference-with-quality-gates-a2ebef0462c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
