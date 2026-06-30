# Per-Head 4-bit KV Cache Quantization on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-4-bit-kv-cache-quantization-on-cpu-93776f362fba`
Run ID: `per-head-4-bit-kv-cache-quantization-on-cpu-93776f362fba-20260604T111115045852+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4f69b55a54be

## What looked useful

Per-head int4 KV reduced K+V memory by about 8x versus fp32 and was 1.34x-1.74x faster than fp32 on 2048-token synthetic decode shapes, but one scale per head caused high output error: 0.256-0.303 relative RMSE on uniform heads and 0.340-0.671 on heterogeneous heads. Per-head scaling sometimes beat global scaling but remained too inaccurate for a positive claim.

## Boundaries and scale limits

No real transformer perplexity or generation quality, no batching, no multithreading, no NUMA tuning, no hand-written AVX512 int4 kernel, and only sequence lengths up to 2048 with H<=16 and D<=128.

## Claim scope

Synthetic single-process CPU decode-attention microbenchmark for packed symmetric int4 K/V caches with one scale per head, compared against fp32 attention and a global-scale int4 control.

## Why it stopped

Early synthetic CPU falsification: the memory and longer-context latency mechanism works, but one-scale-per-head int4 KV has high attention-output error and weak top-1 agreement, so this is not a full validation or paper-ready result.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded follow-up using real small-model KV traces to compare per-head-only scales with per-head-per-block or per-token group scales.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace blockwise int4 KV scaling versus per-head-only scaling
- Success threshold: Blockwise or groupwise int4 must cut relative attention-output RMSE by at least 2x versus per-head-only int4 on real traces while keeping KV memory at least 3x smaller than fp16 and not slowing single-token CPU decode by more than 20% versus fp32 for 2048-token context.
- Stop condition: Stop if real-trace relative output RMSE remains above 0.15 or top-1 attention agreement remains below 0.80 for all tested scale granularities that preserve at least 3x fp16 memory reduction.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-4-bit-kv-cache-quantization-on-cpu-93776f362fba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
