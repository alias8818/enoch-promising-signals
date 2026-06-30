# Adaptive KV eviction plus 4-bit KV on GB10 for long-context local inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adaptive-kv-eviction-plus-4-bit-kv-on-gb10-for-long-context-local-inference-6e14a6021d10`
Run ID: `adaptive-kv-eviction-plus-4-bit-kv-on-gb10-for-long-context-local-inference-6e14a6021d10-20260619T195326950123+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/970da9f66e8b

## What looked useful

Across three medium seeds at seq_len=32768 and dim=value_dim=256, adaptive fp16 improved output cosine over recent-only fp16 by about 0.18 to 0.21 absolute across tested budgets. Adaptive int4 closely tracked adaptive fp16 while estimating 15.5x to 124x cache compression versus full fp16 cache.

## Boundaries and scale limits

Proxy-only synthetic attention workload; no real decoder integration, no perplexity or generation-quality measurement, no production fused int4 kernel, and no validation across real model layers/heads or natural prompt distributions.

## Claim scope

In a GB10 CUDA synthetic long-context attention probe with recurring long-range hot tokens, adaptive retention based on prior attention plus sparse anchors preserved substantially more full-cache attention-output fidelity than recent-only retention at 3.125% to 25% cache budgets; 4-bit K/V quantize-dequantize added only about 0.0013 to 0.0025 absolute cosine loss versus adaptive fp16.

## Why it stopped

Proxy mechanism evidence supports a bounded adaptive-retention plus 4-bit KV signal, but it is not a full validation of long-context local LLM inference.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate adaptive eviction plus 4-bit KV into a small real decoder cache path and compare perplexity or retrieval-task accuracy, latency, and memory against full-cache, recent-only, and quant-only controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real decoder validation of adaptive KV eviction plus 4-bit KV
- Success threshold: Adaptive 4-bit cache should retain at least 95% of full-cache task accuracy or keep perplexity increase below 5% while using at least 4x less KV memory than full fp16 and outperforming recent-only at the same retained-token budget.
- Stop condition: Stop as negative if adaptive 4-bit is not better than recent-only at matched memory on real decoder metrics, or if quantization/eviction overhead erases practical memory or latency benefits.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-kv-eviction-plus-4-bit-kv-on-gb10-for-long-context-local-inference-6e14a6021d10`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
