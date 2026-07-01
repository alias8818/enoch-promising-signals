# Exact-Anchor Hierarchical KV Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-hierarchical-kv-compression-3d45507dd100`
Run ID: `exact-anchor-hierarchical-kv-compression-3d45507dd100-20260524T183733410541+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5dad48f191a0

## What looked useful

Exact-anchor hierarchical summaries approximate full attention extremely well for smooth redundant spans at about 8x compression, but they cannot preserve arbitrary exact non-anchor retrieval: measured exact target retention was 0.0 for non-anchor targets and relative L2 error remained above 0.62 even with four summaries per interval.

## Boundaries and scale limits

No pretrained transformer, real language modeling, multi-head cache trace, throughput, or long-context benchmark was run. Results are proxy evidence for the compression mechanism, not full LLM-serving validation.

## Claim scope

Synthetic attention-only evaluation of exact anchor retention plus mean-summary hierarchical pseudo-KV entries on 4096-item, 64-dimensional caches across smooth, anchor-retrieval, and non-anchor-retrieval regimes.

## Why it stopped

Proxy evidence is mixed: mechanism is supported for smooth redundant spans but early-falsified for exact non-anchor retrieval, so broad exact-anchor hierarchical KV compression is not validated by this run.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same compressor on a small pretrained transformer cache with perplexity and needle-style retrieval metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-Transformer Exact-Anchor HKV Cache Benchmark
- Success threshold: At least 2x KV entry reduction with less than 5% relative perplexity/loss degradation on normal text and no more than 10 percentage-point retrieval accuracy loss versus full cache on a bounded needle task.
- Stop condition: Stop if exact-anchor HKV exceeds 10% relative loss degradation or loses more than 10 percentage points of retrieval accuracy at 2x compression on the small-transformer benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-hierarchical-kv-compression-3d45507dd100`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
