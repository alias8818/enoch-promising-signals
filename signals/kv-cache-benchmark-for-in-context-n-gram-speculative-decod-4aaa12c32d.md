# KV-cache benchmark for in-context n-gram speculative decoding

Status: `useful_signal`
Project ID: `kv-cache-benchmark-for-in-context-n-gram-speculative-decod-4aaa12c32d`
Run ID: `kv-cache-benchmark-for-in-context-n-gram-speculative-decod-4aaa12c32d-20260515T094016761816+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/08bd9c0b18ff

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier-1 direct evidence supports the mechanism in controlled repeated-context prompts, but this is not publication-grade evidence and only covers one small model with greedy decoding.

## Recommended next action

Run a bounded medium confirmation on at least two model sizes and a real repeated-context prompt suite with identical-output checks and production-relevant KV-cache timing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium KV-cache benchmark for prompt n-gram speculative decoding
- Success threshold: For at least two repeated-context workload families and two model sizes, outputs remain identical to the target greedy baseline, median decode speedup is >= 1.25x, target forward-call reduction is >= 40%, and sparse-match controls do not claim speedup beyond measurement noise.
- Stop condition: Stop as negative if repeated-context workloads fail to reach 1.10x median speedup or if cache repair/rejection overhead erases target-call reductions on the larger model.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-benchmark-for-in-context-n-gram-speculative-decod-4aaa12c32d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
