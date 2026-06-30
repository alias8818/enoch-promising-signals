# 4-Bit KV Cache for CPU Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-kv-cache-for-cpu-long-context-f0056313ab85`
Run ID: `4-bit-kv-cache-for-cpu-long-context-f0056313ab85-20260608T233033199920+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/32e06eb072fe

## What looked useful

4-bit KV cache is primarily a memory-capacity win for CPU long context. A naive on-the-fly dequant kernel showed long-context speedups of 1.07x-1.29x at 65k-262k sequence lengths, but short contexts were 0.35x-0.84x as fast as float32 and relative L2 attention-output error was about 0.14-0.20.

## Boundaries and scale limits

Tested only one synthetic attention head with random K/V/query tensors on an 8-online-CPU Xeon worker. No real transformer, perplexity, generated quality, multi-layer cache behavior, batching, GQA/MQA, int8 baseline, or SIMD-optimized production kernel was evaluated.

## Claim scope

A single-threaded native CPU synthetic decode-attention benchmark found that packed per-row symmetric 4-bit KV cache reduces KV memory by about 7.1x-7.8x including scales and can modestly improve long-context kernel time once the float32 working set is large, but it is slower at shorter contexts and introduces non-trivial attention-output error.

## Why it stopped

Synthetic kernel-local evidence is insufficient for publication and shows mixed performance: useful memory reduction and modest long-context speedups, but slower short contexts and unvalidated model-level quality.

## Recommended next action

Stop this run as a no-paper useful signal; deepen with a real CPU inference-stack test comparing float KV, int8 KV, and 4-bit KV on tokens/s, peak RSS, and perplexity or quality drift at 32k-128k context.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU decode validation for 4-bit KV cache
- Success threshold: At 64k or 128k context, 4-bit KV achieves at least 4x peak memory reduction and at least 1.15x sustained decode tokens/s over float KV, while quality/perplexity degradation remains within a predeclared acceptable bound and int8 does not dominate the tradeoff.
- Stop condition: Stop if 4-bit KV is slower than float KV at 64k context in the real stack, if quality degradation is clearly unacceptable, or if int8 KV provides comparable memory relief with better speed-quality tradeoff.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-kv-cache-for-cpu-long-context-f0056313ab85`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
