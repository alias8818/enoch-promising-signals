# Grouped INT4 KV-cache compression with direct memory+throughput evidence

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `grouped-int4-kv-cache-compression-with-direct-memory-throughput-evidence-4a97fd3e449c`
Run ID: `grouped-int4-kv-cache-compression-with-direct-memory-throughput-evidence-4a97fd3e449c-20260613T192111951959+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fee21034b133

## What looked useful

Grouped INT4 reliably reduces KV-cache bytes in the tested layout, but naive dequantize-on-demand throughput does not consistently beat FP16; the mechanism may become useful when memory traffic dominates, as suggested by parity/slight speedup at 4K context.

## Boundaries and scale limits

No real transformer, quality/perplexity measurement, CUDA/fused kernel, GPU memory telemetry, paged attention, batching, serving trace, or 7B+ model evidence was produced.

## Claim scope

Synthetic NumPy CPU attention decode shows grouped symmetric INT4 KV-cache storage with FP16 per-token/head/group scales reduces cache bytes by 3.56x versus FP16 storage, while throughput is mixed: slower at 1K and 2K context and roughly parity at 4K context in the longer sequential run.

## Why it stopped

Local CPU synthetic evidence is useful but insufficient for a paper-positive claim about model-serving KV-cache compression.

## Recommended next action

Run a bounded fused CUDA or Triton grouped-INT4 KV-cache decode benchmark against a strong FP16/BF16 paged-attention baseline with real model memory and throughput telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused GPU grouped-INT4 KV-cache decode benchmark
- Success threshold: At context lengths where KV-cache memory is material, INT4 must show at least 3x measured KV-cache memory reduction and at least 95% of baseline decode throughput without unacceptable quality drift.
- Stop condition: Stop if fused INT4 remains below 90% of baseline throughput at long context or if real-model quality drift is unacceptable under the tested quantization layout.

## Evidence references

- Artifact root: `<local-path>/projects/grouped-int4-kv-cache-compression-with-direct-memory-throughput-evidence-4a97fd3e449c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
