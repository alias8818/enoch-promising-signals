# INT4 KV-cache compression for CPU long-context inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-kv-cache-compression-for-cpu-long-context-inference-496b177b7142`
Run ID: `int4-kv-cache-compression-for-cpu-long-context-inference-496b177b7142-20260620T044601046325+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ae97c47b70d8

## What looked useful

INT4 KV compression is mechanically effective for memory reduction and preserves synthetic attention outputs with cosine about 0.989-0.991, but the simple CPU path loses latency at long contexts: 1.23x slower at 4k, 1.47x slower at 16k, and 1.39x slower at 32k.

## Boundaries and scale limits

Synthetic K/V and query tensors only; NumPy vectorized dequantization rather than an optimized fused CPU kernel; no real transformer perplexity/task evaluation; max tested context 32768 with heads=8 and dim=64.

## Claim scope

Bounded CPU synthetic one-token attention proxy: groupwise packed INT4 KV cache reduces storage bytes by 3.56x versus fp16 K/V including scales, but naive full-cache dequantization is slower than fp16-stored K/V attention at 4k-32k contexts.

## Why it stopped

Bounded proxy, not full validation: naive INT4 full-cache dequantization saved memory but was slower than fp16-stored K/V attention for 4k-32k long-context cases.

## Recommended next action

Stop this run as no-paper useful signal; only continue via a bounded fused/blockwise CPU INT4 attention kernel test that avoids materializing full fp32 K/V.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused blockwise CPU INT4 KV attention without full-cache dequantization
- Success threshold: At 16k-64k contexts, fused INT4 path must use at least 3.0x less KV memory including scales, have median decode latency no worse than 0.95x of fp16-stored K/V baseline, and keep output cosine at or above 0.99 on synthetic or trace-derived attention outputs.
- Stop condition: Stop if the fused/blockwise path remains slower than fp16-stored K/V by more than 10% at 16k and 32k, or if output cosine falls below 0.98 before any real-model evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/int4-kv-cache-compression-for-cpu-long-context-inference-496b177b7142`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
