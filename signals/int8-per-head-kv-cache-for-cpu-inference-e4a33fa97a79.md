# Int8 per-head KV cache for CPU inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `int8-per-head-kv-cache-for-cpu-inference-e4a33fa97a79`
Run ID: `int8-per-head-kv-cache-for-cpu-inference-e4a33fa97a79-20260530T004503528887+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6d56167698b4

## What looked useful

Per-head INT8 K/V cache gave 1.5x-2.1x speedup on larger 8-thread synthetic decode shapes and 2.1x-2.9x speedup on long-context 1-thread shapes, with nearly 4x K/V memory reduction and mean absolute output error below 0.001. Small 8-thread shapes were neutral to slightly slower.

## Boundaries and scale limits

No real model integration, no perplexity/generation-quality measurement, no production inference-engine overhead, no batching/prefill/cache-update measurement, and no optimized architecture-specific INT8 dot kernel beyond native compiler optimization.

## Claim scope

Synthetic CPU one-token decode-attention benchmark on an Intel Xeon Silver 4114-class worker: per-head symmetric INT8 K/V cache reduced K/V storage by about 4x and improved latency for larger tested shapes, while preserving small absolute attention-output error versus FP32 K/V.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic proxy benchmark, not full validation in a real CPU LLM serving stack.

## Recommended next action

Run a bounded real-model CPU inference follow-up that integrates per-head INT8 K/V cache into a decode path and measures tokens/sec, memory, and perplexity/generation quality against FP32/BF16/FP16 cache baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU decode validation for per-head INT8 K/V cache
- Success threshold: At least 1.25x long-context decode throughput improvement or equivalent memory-pressure win versus the best floating-point cache baseline, with perplexity degradation under 1% relative or a clearly bounded generation-quality difference.
- Stop condition: Stop if real-model quality degrades beyond the threshold, if decode throughput is not improved for long contexts, or if integration overhead erases the synthetic memory-bandwidth benefit.

## Evidence references

- Artifact root: `<local-path>/projects/int8-per-head-kv-cache-for-cpu-inference-e4a33fa97a79`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
