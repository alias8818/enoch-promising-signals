# Mixed-Precision KV Cache with Graceful Quality Degradation for Long Context Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `mixed-precision-kv-cache-with-graceful-quality-degradation-for-long-context-inference-b547c22437b0`
Run ID: `mixed-precision-kv-cache-with-graceful-quality-degradation-for-long-context-inference-b547c22437b0-20260607T001404757326+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/63bd8534a579

## What looked useful

Medium probe over contexts 4096, 8192, and 16384 with 5 seeds each found mixed_saliency at 67.75% estimated memory saving had output cosine 0.999995 and relative MSE 1.45e-05 versus FP16, while mixed_recent and uniform_int4 were around 0.993 cosine and 1.42e-02 relative MSE. A budget sweep showed 23% salient int8 with no FP16 already preserved high output fidelity in this proxy.

## Boundaries and scale limits

No end-to-end autoregressive model perplexity, task accuracy, generated text quality, packed int4/int8 KV kernels, decode throughput, learned saliency, or multi-layer/head real-model sensitivity was tested.

## Claim scope

In a synthetic long-context single-query attention retrieval proxy on GB10, oracle saliency allocation of 23% int8 tokens plus 0-5% FP16 tokens preserved FP16 attention-output fidelity far better than random or recency allocation at similar memory budgets, with about 65-69% estimated KV memory saving.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic/direct-attention proxy, not full validation of long-context inference quality or serving performance.

## Recommended next action

Run a bounded real-model follow-up that integrates non-oracle saliency KV quantization into a small cached autoregressive model and measures perplexity, long-context retrieval accuracy, memory, and decode throughput against FP16, uniform int8, and uniform int4.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-model non-oracle saliency KV quantization benchmark
- Success threshold: At similar estimated KV memory saving to uniform int4, non-oracle saliency mixed precision should reduce perplexity degradation or retrieval accuracy loss by at least 50% versus uniform int4 while staying within 10% decode throughput of the best quantized baseline.
- Stop condition: Stop if non-oracle saliency is no better than random or recency mixed allocation on both perplexity/retrieval quality and throughput at matched memory budgets.

## Evidence references

- Artifact root: `<local-path>/projects/mixed-precision-kv-cache-with-graceful-quality-degradation-for-long-context-inference-b547c22437`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
