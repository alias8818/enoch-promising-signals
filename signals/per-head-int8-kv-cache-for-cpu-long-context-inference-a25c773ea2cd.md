# Per-head INT8 KV cache for CPU long-context inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-int8-kv-cache-for-cpu-long-context-inference-a25c773ea2cd`
Run ID: `per-head-int8-kv-cache-for-cpu-long-context-inference-a25c773ea2cd-20260528T141841071626+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0b5705bd13e5

## What looked useful

Per-head INT8 KV cache is mechanically plausible for CPU long-context decode because it reliably gives about 4x KV memory reduction and sometimes materially improves decode latency, but the speed benefit is shape-dependent and was only 1.09x in the largest heads=32 dim=128 check.

## Boundaries and scale limits

This run did not test full transformer inference, real LLM KV activation distributions, perplexity or generation quality, production CPU kernels, batching, RoPE effects, MQA/GQA variants, or comparisons against established KV quantization baselines. The result is a bounded kernel-level signal, not publication-grade evidence.

## Claim scope

On this CPU worker, a direct C++ single-token attention-decode proxy shows that per-head symmetric INT8 K/V storage can reduce KV-cache memory by about 4x and preserve synthetic attention outputs with relative L2 error near 1.0-1.25%; measured latency speedups ranged from 1.03x to 2.26x for heads=8 dim=64 and from 1.09x to 1.69x for heads=32 dim=128.

## Why it stopped

No-paper closure: bounded local kernel evidence is useful but mixed and incomplete; it does not support a publication claim without real-model quality and production-kernel validation.

## Recommended next action

Run a bounded deepen follow-up in a small real CPU inference stack, comparing FP16/FP32 KV, per-head INT8 KV, and an existing KV quantization baseline on perplexity drift plus decode tokens/s at 8k-64k context.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU validation of per-head INT8 KV cache
- Success threshold: At 16k-32k context, achieve at least 1.25x decode tokens/s improvement or equivalent memory-enabled context extension versus the best non-INT8 baseline, with perplexity drift under 1% relative or an explicitly justified task-quality tolerance.
- Stop condition: Stop if per-head INT8 is slower than the existing KV quantization baseline at 16k context or exceeds the quality-drift tolerance in two independent evaluation slices.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-int8-kv-cache-for-cpu-long-context-inference-a25c773ea2cd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
