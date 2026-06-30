# INT8 KV Cache with H2O Eviction on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-kv-cache-with-h2o-eviction-on-cpu-f54a785c07d4`
Run ID: `int8-kv-cache-with-h2o-eviction-on-cpu-f54a785c07d4-20260523T235043257381+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12311a2acc01

## What looked useful

H2O INT8 matched H2O FP32 mean relative L2 error within 0.00056 absolute, reduced error versus recent-only by 10.12%, and cut theoretical KV memory 3.76x versus an equal-budget FP32 cache and 15.06x versus full FP16 KV at seq_len=4096; naive dequantized INT8 was 1.76x slower than H2O FP32.

## Boundaries and scale limits

Synthetic trace only; no real LLM KV activations, no perplexity/task quality, no end-to-end generation, and no optimized INT8 CPU attention kernel. Python/NumPy timing showed INT8 dequantization overhead, not serving-grade performance.

## Claim scope

In a five-seed synthetic single-head CPU decode benchmark, H2O-style heavy-hitter plus recent-token eviction preserved full-cache attention outputs better than a recent-only cache at the same token budget, and per-token INT8 KV storage added negligible output error while reducing theoretical KV memory.

## Why it stopped

Proxy/local synthetic evidence supports the memory-error mechanism but does not provide full validation or CPU speedup; the naive Python INT8 path is slower due to dequantization overhead.

## Recommended next action

Stop this run as no-paper useful signal; the next concrete step is a bounded real-trace CPU test with an optimized or library-backed INT8 attention path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real KV Trace Test for INT8 H2O CPU Cache
- Success threshold: At a 4x or greater KV memory reduction versus full FP16, H2O INT8 should keep logit/perplexity degradation within 5% of H2O FP16/FP32 and be no slower than H2O FP16/FP32 by more than 10% on CPU replay.
- Stop condition: Stop if real-trace H2O INT8 increases quality degradation by more than 5% relative to H2O FP16/FP32 or remains slower than FP16/FP32 after using an optimized INT8/fused CPU path.

## Evidence references

- Artifact root: `<local-path>/projects/int8-kv-cache-with-h2o-eviction-on-cpu-f54a785c07d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
