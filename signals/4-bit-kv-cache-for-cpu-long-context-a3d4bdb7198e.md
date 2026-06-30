# 4-bit KV-Cache for CPU Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-kv-cache-for-cpu-long-context-a3d4bdb7198e`
Run ID: `4-bit-kv-cache-for-cpu-long-context-a3d4bdb7198e-20260614T053852085288+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a505c71cd74a

## What looked useful

The memory mechanism is real but the naive CPU implementation loses the latency tradeoff. Future work should skip materialize-then-attend dequantization and test fused/tiled int4 attention before model-level validation.

## Boundaries and scale limits

Proxy-only NumPy benchmark; no real language model, no perplexity or generation metric, no serving trace, no RoPE/GQA coverage, and no fused AVX512/VNNI int4 attention kernel.

## Claim scope

On synthetic CPU attention tensors up to 32k context with 8 heads and head_dim 64, packed int4 KV-cache storage with fp32 per-block scales reduces cache bytes by 3.2x to 3.56x versus fp16 and preserves output direction reasonably well, but a naive full-cache dequantize-every-token path is substantially slower than fp32/fp16 baselines.

## Why it stopped

Bounded proxy evidence shows useful cache compression and moderate synthetic output error, but the tested naive CPU path is 5.16x to 15.64x slower than the best baseline at 32k context, so the idea is not paper-ready or viable as implemented.

## Recommended next action

Stop this no-paper run; next useful bounded action is to implement a fused or tiled CPU int4 attention kernel and compare it against fp16/fp32 baselines at 32k to 128k context.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused CPU int4 KV-cache attention benchmark
- Success threshold: At 64k context, achieve at least 3x fp16 KV memory reduction, int4 decode latency no worse than 1.5x the fp16 baseline, and no more than 5% degradation on the selected model/trace quality metric.
- Stop condition: Stop if the fused/tiled implementation remains more than 2x slower than fp16 at 32k context or if model quality degradation exceeds 10% before reaching 64k.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-kv-cache-for-cpu-long-context-a3d4bdb7198e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
