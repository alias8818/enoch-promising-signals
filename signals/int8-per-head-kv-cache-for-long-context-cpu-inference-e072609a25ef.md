# INT8 per-head KV cache for long-context CPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-per-head-kv-cache-for-long-context-cpu-inference-e072609a25ef`
Run ID: `int8-per-head-kv-cache-for-long-context-cpu-inference-e072609a25ef-20260527T213933366411+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/72faf9de0682

## What looked useful

Per-head INT8 KV storage reduced cache bytes to about 25% of FP32 and kept normal synthetic output relative L2 near 1.5%-1.7%, but the storage-only CPU path was 3.4x-5.1x slower than FP32 because it dequantized K/V before attention. Rare synthetic outliers made one-scale-per-head error rise sharply, reaching 8.5% output relative L2 at 0.1% magnitude-30 outliers and 23.2% at magnitude 100.

## Boundaries and scale limits

No real LLM traces, perplexity, generation quality, fused INT8 kernel, multi-layer serving loop, batching, grouped-query attention, or production allocator behavior were tested.

## Claim scope

Synthetic one-token CPU decode attention with 8 heads, 64 dimensions per head, 1k-16k context, using storage-only symmetric INT8 KV cache with one scale per head and FP32 compute after dequantization.

## Why it stopped

Bounded proxy evidence shows storage-only per-head INT8 KV cache is not CPU-latency viable despite memory savings; this is not a full validation of all possible fused-kernel designs.

## Recommended next action

Stop this storage-only version as no-paper useful evidence; the concrete next test is a fused CPU INT8 attention kernel that avoids materializing full FP32 K/V and compares against FP32 on synthetic and real-model KV traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused CPU INT8 KV attention kernel for long-context decode
- Success threshold: At 16k context, fused INT8 median decode latency is no worse than FP32 while using no more than 30% of FP32 KV bytes and keeping output relative L2 below 0.02 on normal traces and below 0.05 under mild outlier stress.
- Stop condition: Stop if the fused kernel remains slower than FP32 by more than 20% at 8k and 16k context or if real-trace output/perplexity error exceeds the success threshold.

## Evidence references

- Artifact root: `<local-path>/projects/int8-per-head-kv-cache-for-long-context-cpu-inference-e072609a25ef`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
