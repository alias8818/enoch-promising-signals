# Small-Model KV-Cache Suffix Drafting Latency Test

Status: `useful_signal`
Project ID: `small-model-kv-cache-suffix-drafting-latency-test-2316475335`
Run ID: `small-model-kv-cache-suffix-drafting-latency-test-2316475335-20260515T210223330089+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f8aa642cf3d5

## What looked useful

Measured warm suffix KV reuse was 0.376x to 0.754x the latency of no-cache recomputation for 16-512 token suffixes, but 0.990x to 1.005x the latency of standard full-prompt cached decode, so the optimization only matters when suffix state would otherwise be recomputed.

## Boundaries and scale limits

Random-weight small model only; no pretrained drafter, target-model verification, acceptance-rate measurement, batched serving, paged attention, scheduler effects, or production cache-eviction behavior.

## Claim scope

On a single-batch 8-layer GPT-style CUDA benchmark, warm suffix KV-cache reuse reduces repeated 8-token draft-attempt latency versus recomputing the suffix/context each token, but does not improve over ordinary full-prompt KV-cached decode.

## Why it stopped

Controlled Tier 1 result supports the mechanism only against a weak recomputation baseline and fails to show advantage over the standard KV-cached serving baseline.

## Recommended next action

Stop as no-paper evidence unless a concrete speculative decoding stack is known to recompute drafter suffix KV; then run the proposed end-to-end cached-baseline follow-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-End Suffix KV Reuse In A Real Speculative Decoding Loop
- Success threshold: At least 15% lower mean accepted-token latency than the best standard cached baseline at one suffix length, with no worse than 5% acceptance-rate regression and p90 latency also improved.
- Stop condition: Stop if suffix reuse is within +/-5% of standard cached baseline for all suffix lengths or if memory/cache-copy overhead erases the latency gain.

## Evidence references

- Artifact root: `<local-path>/projects/small-model-kv-cache-suffix-drafting-latency-test-2316475335`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
