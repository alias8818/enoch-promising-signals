# Anchor-Preserved KV Cache Compression for CPU RAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-preserved-kv-cache-compression-for-cpu-ram-446cdcbdea10`
Run ID: `anchor-preserved-kv-cache-compression-for-cpu-ram-446cdcbdea10-20260620T065332353846+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/8326b63f3b9a

## What looked useful

Anchor preservation gave consistent modest error reductions: middle int8 reduced relative L2 output error by 9.36% versus all-token int8 while reducing compression ratio by 7.84%; middle int4 reduced error by 9.76% versus all-token int4 while reducing compression ratio by 34.19%. Dropping middle tokens while keeping anchors/recent tokens failed badly with 3.54 mean relative L2 error.

## Boundaries and scale limits

Synthetic NumPy proxy only; no real transformer KV distributions, perplexity, natural-text decode quality, layer/head heterogeneity, or inference-server throughput were tested. Sequence lengths were 1024-4096 with dimensions 64-128 and 64 queries per scenario.

## Claim scope

In deterministic synthetic decoder-attention traces with anchor/sink and recency-biased attention mass, preserving small fp16 anchor/recent KV subsets while quantizing the remaining cache reduces attention-output approximation error versus uniform quantization, but the tested budgets do not improve RAM efficiency at comparable quality.

## Why it stopped

Closed as a bounded proxy useful signal: mechanism partially supported, but no RAM-efficiency win or direct model-quality evidence was produced.

## Recommended next action

Run a direct small-transformer KV-cache compression test at matched RAM budgets, measuring perplexity or decode-quality plus CPU latency/memory telemetry; do not write a paper from this proxy alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-Transformer Matched-Budget Anchor-Preserved KV Compression
- Success threshold: At equal measured KV-cache RAM, anchor-preserved compression improves perplexity or decode-quality degradation by at least 5% relative to uniform quantization without increasing mean decode latency by more than 10%.
- Stop condition: Stop if matched-budget anchor-preserved variants fail to improve model-quality degradation by 5% or if CPU decode latency increases by more than 10%.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserved-kv-cache-compression-for-cpu-ram-446cdcbdea10`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
