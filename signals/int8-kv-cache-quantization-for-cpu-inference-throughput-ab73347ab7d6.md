# Int8 KV-cache quantization for CPU inference throughput

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-kv-cache-quantization-for-cpu-inference-throughput-ab73347ab7d6`
Run ID: `int8-kv-cache-quantization-for-cpu-inference-throughput-ab73347ab7d6-20260608T173917488155+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/1d3749dd7343

## What looked useful

INT8 KV cache reduces estimated KV bytes per generated token by about 3.7x-3.8x, but CPU throughput gains appear only once the FP32 KV footprint is large enough for memory/cache pressure to dominate the dequantization overhead.

## Boundaries and scale limits

Synthetic single-head, single-threaded decode attention only; no full model serving, batching, optimized production INT8 kernel, tokenizer/model overhead, perplexity, or task-quality evaluation.

## Claim scope

On this CPU worker, a naive C++ per-token symmetric INT8 KV decode attention path is slower or break-even for smaller tested synthetic KV footprints, but 2.4x-3.5x faster than FP32 for the largest tested dim=128 long-context cases, with about 0.9%-1.0% relative L2 output error versus FP32.

## Why it stopped

Bounded direct microbenchmark completed; result is useful but mixed and not end-to-end or publication-grade.

## Recommended next action

Run a bounded real-model CPU serving benchmark using an optimized INT8 KV implementation and fixed prompts at 8k-16k context before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU serving validation for INT8 KV-cache crossover
- Success threshold: At least 1.5x decode tokens/s improvement at 8k or 16k context with no more than 1% perplexity regression or a predeclared small logit-divergence threshold, while not regressing more than 10% at 2k context.
- Stop condition: Stop if the optimized INT8 KV path is slower than FP32 at both 8k and 16k contexts or quality regression exceeds the predeclared threshold.

## Evidence references

- Artifact root: `<local-path>/projects/int8-kv-cache-quantization-for-cpu-inference-throughput-ab73347ab7d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
