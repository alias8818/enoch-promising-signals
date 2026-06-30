# Grouped KV Quantization for CPU Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `grouped-kv-quantization-for-cpu-long-context-19c7ce68fb89`
Run ID: `grouped-kv-quantization-for-cpu-long-context-19c7ce68fb89-20260527T005853182427+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ca553ab2b4b6

## What looked useful

Group size 64 reached 3.996x compression versus fp32 with attention-output relative L2 of 0.0362 at 4,096 tokens, 0.0268 at 16,384 tokens, and 0.0308 at 65,536 tokens, all with cosine similarity at or above 0.9993. However, stream-style dequantize-each-query decode was 1.8x to 5.1x slower than fp32 at group size 64, so practical CPU serving needs a fused/blockwise int8 implementation rather than naive dequantization.

## Boundaries and scale limits

Synthetic KV data only; no real transformer KV traces, no perplexity or generation-quality measurement, no optimized fused int8 attention kernel, and no validation beyond 65,536 tokens with 8 heads and 64-dimensional heads.

## Claim scope

On a CPU worker synthetic long-context decode-attention proxy up to 65,536 tokens, symmetric int8 KV quantization with one scale per sequence group and attention head gave near-4x KV storage reduction and preserved attention outputs well at moderate group sizes, but naive full-cache dequantization before each query batch was slower than fp32 attention.

## Why it stopped

No-paper useful signal: synthetic attention evidence supports the memory/accuracy mechanism, but latency is negative for naive CPU dequantization and direct model-quality evidence is absent.

## Recommended next action

Do not write a paper from this run; next build a fused blockwise int8 CPU attention prototype that consumes grouped KV scales without materializing full fp32 K/V, then test it on real small-transformer KV traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused Blockwise CPU Attention for Grouped Int8 KV Cache
- Success threshold: At 64k context and group size 64, fused grouped int8 KV should keep attention-output relative L2 at or below 0.05 on real or trace-derived KV data while achieving at least 3.9x KV storage compression and stream decode latency no worse than 1.25x fp32.
- Stop condition: Stop if fused grouped int8 remains slower than 1.5x fp32 at 64k context or real KV traces exceed 0.05 attention-output relative L2 at group sizes that provide at least 3.9x compression.

## Evidence references

- Artifact root: `<local-path>/projects/grouped-kv-quantization-for-cpu-long-context-19c7ce68fb89`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
