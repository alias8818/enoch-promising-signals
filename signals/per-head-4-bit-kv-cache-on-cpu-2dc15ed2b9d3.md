# Per-head 4-bit KV cache on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-4-bit-kv-cache-on-cpu-2dc15ed2b9d3`
Run ID: `per-head-4-bit-kv-cache-on-cpu-2dc15ed2b9d3-20260527T115731068043+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/904c3dfc2ffb

## What looked useful

Packed int4 per-head KV compressed K+V storage 8x and reached 1.60x to 4.16x speedup for 2048-32768 token cases, but relative L2 output error stayed high at 0.229-0.290, making one-scale-per-head KV compression unsupported as a practical standalone method.

## Boundaries and scale limits

Synthetic random KV/query tensors only; float32 baseline only; scalar compact C++ kernel rather than a production AVX-512/fused backend; no real LLM activation trace, perplexity, downstream accuracy, or multi-request serving test.

## Claim scope

On this CPU worker, a single-query synthetic decode-attention microbenchmark with float32 KV baseline showed that packed signed 4-bit KV using one K scale and one V scale per head can speed up long-context attention once memory traffic dominates, but the same coarse quantization produced high relative L2 output error.

## Why it stopped

Bounded direct CPU microbenchmark found a speed mechanism but also early falsification of practical quality for one-scale-per-head 4-bit KV due to 23%-29% relative L2 output error; this is not a full model validation.

## Recommended next action

Stop this one-scale-per-head variant as no-paper evidence; the concrete next bounded test is blockwise or per-token scaled int4 KV in the same decode-attention harness plus a small real-transformer activation trace.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blockwise scaled 4-bit KV cache on CPU decode attention
- Success threshold: At 8192 tokens, maintain at least 1.5x speedup versus float32 KV while reducing relative L2 output error below 0.10 on synthetic tensors and avoiding severe degradation on a real-model trace.
- Stop condition: Stop if blockwise/per-token scaling either falls below 1.2x speedup at 8192 tokens or still exceeds 0.15 relative L2 output error after reasonable block-size tuning.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-4-bit-kv-cache-on-cpu-2dc15ed2b9d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
