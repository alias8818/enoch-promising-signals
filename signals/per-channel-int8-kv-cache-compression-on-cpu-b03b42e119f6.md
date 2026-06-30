# Per-Channel INT8 KV Cache Compression on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-channel-int8-kv-cache-compression-on-cpu-b03b42e119f6`
Run ID: `per-channel-int8-kv-cache-compression-on-cpu-b03b42e119f6-20260603T145001079256+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6d97d8ae3df8

## What looked useful

The compression mechanism is plausible for memory footprint, but a simple CPU vectorized implementation does not produce latency wins. Longer sequence lengths narrow but do not remove the INT8 latency penalty.

## Boundaries and scale limits

Synthetic activations only; no real transformer KV traces, perplexity, generation quality, FP16/BF16 serving baseline, batching, NUMA tuning, or optimized int8 kernel. Compression versus FP16/BF16 would be about 2x rather than 4x.

## Claim scope

On a one-thread NumPy CPU decode-step simulation with synthetic K/V tensors up to 8 heads, sequence length 8192, and head dimension 64, per-channel INT8 KV cache compression reduces cache bytes by about 4x versus FP32 and preserves normal-distribution attention outputs with about 1.0-1.3% relative RMSE, but the naive INT8 path is slower than FP32.

## Why it stopped

Proxy/local CPU evidence supports memory reduction but falsifies the naive latency-benefit version of the hypothesis; this is not full model validation.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should implement or reuse an optimized CPU int8 attention kernel and compare against FP16/BF16 KV cache on real model KV traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized CPU kernel test for per-channel INT8 KV cache attention
- Success threshold: At seq length 8192, INT8 compressed KV cache uses at least 1.8x less memory than FP16/BF16 and median decode-step attention latency is no worse than 1.05x the FP16/BF16 baseline with output relative RMSE below 0.02 on non-heavy-tail traces.
- Stop condition: Stop if the optimized kernel remains more than 1.2x slower than FP16/BF16 at seq length 8192 or if real-trace output relative RMSE exceeds 0.05.

## Evidence references

- Artifact root: `<local-path>/projects/per-channel-int8-kv-cache-compression-on-cpu-b03b42e119f6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
