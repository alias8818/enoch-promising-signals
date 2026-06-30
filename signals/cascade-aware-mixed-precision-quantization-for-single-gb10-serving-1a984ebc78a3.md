# Cascade-Aware Mixed-Precision Quantization for Single-GB10 Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cascade-aware-mixed-precision-quantization-for-single-gb10-serving-1a984ebc78a3`
Run ID: `cascade-aware-mixed-precision-quantization-for-single-gb10-serving-1a984ebc78a3-20260619T085234354291+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/905ab151f450

## What looked useful

Traffic-weighted allocation avoided a clear sensitivity-only failure mode: at 6 bits, cascade-aware top-1 agreement was 0.892212 versus 0.805420 for sensitivity-only and route agreement was 0.953613 versus 0.900513. However, uniform 6-bit remained better at 0.927734 top-1 and 0.966553 route agreement.

## Boundaries and scale limits

Synthetic MLP cascade only; fake quantize/dequantize around fp16 matmul; no real LLM perplexity, KV-cache quantization, fused low-bit kernel, vLLM/llama.cpp serving, production trace, or long-context workload evidence.

## Claim scope

In a deterministic synthetic three-stage cascade run on a single GB10 with PyTorch CUDA, cascade-aware traffic weighting improved mixed-precision allocation versus sensitivity-only allocation at matched 5-bit and 6-bit average budgets, but did not outperform uniform quantization on MSE, top-1 agreement, or route agreement.

## Why it stopped

Proxy medium confirmation did not beat the uniform quantization baseline, so the original idea is not validated for paper writing; result is a bounded synthetic mechanism signal only.

## Recommended next action

Stop this run as no-paper useful signal; next run should test a real small LLM cascade with matched-memory uniform, sensitivity-only, and cascade-aware quantization plus actual perplexity/task metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-LLM Cascade-Aware Quantization Check
- Success threshold: Cascade-aware allocation must improve held-out perplexity or task agreement by at least 2 percentage points over uniform at the same memory budget, without more than 5% serving throughput regression on GB10.
- Stop condition: Stop if uniform quantization matches or beats cascade-aware on both accuracy and route stability at two memory budgets, or if real low-bit kernel support is unavailable and only fake-quantized timing can be measured.

## Evidence references

- Artifact root: `<local-path>/projects/cascade-aware-mixed-precision-quantization-for-single-gb10-serving-1a984ebc78a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
