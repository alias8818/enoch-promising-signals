# Per-Head Int8 KV Cache for Long Context on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-int8-kv-cache-for-long-context-on-cpu-da557e62e639`
Run ID: `per-head-int8-kv-cache-for-long-context-on-cpu-da557e62e639-20260602T184721062409+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b67010670af1

## What looked useful

Per-head int8 K/V reduced cache memory by about 4x and preserved synthetic attention outputs with roughly 0.012 to 0.015 relative RMSE at 32768 context. Corrected long-context latency was faster than fp32 by 1.54x for uniform head ranges and 1.30x for 8x head-range spread, but speedups were noisy and not universal. Per-head scaling reduced average relative RMSE versus one global scale by about 1.40x under 8x head range spread.

## Boundaries and scale limits

No real transformer model, no perplexity/task-quality measurement, no production fused kernel, no llama.cpp/vLLM-style integration, no real prompt distribution, and no validation beyond 32768 synthetic context on this CPU worker.

## Claim scope

Standalone CPU single-token decode attention microbenchmark with synthetic K/Q/V, H=16, D=64, contexts 512 to 32768, comparing fp32 K/V against per-head symmetric int8 K/V and a global-scale int8 control.

## Why it stopped

Microbenchmark evidence supports the mechanism but is not full validation; real model integration and quality measurements are required before any paper-positive claim.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded action is to integrate per-head int8 KV into a real CPU inference path for a small open model and measure long-context latency, memory, and perplexity/task quality against the engine baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU inference validation of per-head int8 KV cache
- Success threshold: At 16k or longer context, achieve at least 3.5x measured KV memory reduction, no more than 2% relative degradation on the selected quality metric, and at least 1.2x median decode-latency speedup versus the engine baseline.
- Stop condition: Stop as negative if real-model quality degrades by more than 2% after reasonable calibration or if median decode latency is not improved at 16k+ context despite confirmed KV memory reduction.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-int8-kv-cache-for-long-context-on-cpu-da557e62e639`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
