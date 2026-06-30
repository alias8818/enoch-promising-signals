# Bounded Serving Runtime Replay of Mooncake KV Oracle Gaps

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-serving-runtime-replay-of-mooncake-kv-oracle-gaps-0d6e056fb8`
Run ID: `bounded-serving-runtime-replay-of-mooncake-kv-oracle-gaps-0d6e056fb8-20260522T080904576473+0000`

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

- Parent run decision: CPU Log Replay Oracle for KV Eviction Policies: enoch://control-plane/projects/cpu-log-replay-oracle-for-kv-eviction-policies-77a9c3abc698/runs/cpu-log-replay-oracle-for-kv-eviction-policies-77a9c3abc698-20260522T074254487027+0000
- Parent run decision: Real Serving Trace Replay for KV Eviction Oracle Gaps: enoch://control-plane/projects/real-serving-trace-replay-for-kv-eviction-oracle-gaps-b144aaac34/runs/real-serving-trace-replay-for-kv-eviction-oracle-gaps-b144aaac34-20260522T075854715194+0000

## What looked useful

Across 252 fixed-seed runs on four Mooncake trace files, runtime cache improved goodput over no-cache by 5.66% mean, while oracle over runtime improved goodput by only 1.05% mean, 0.78% median, and 3.34% max. This supports KV reuse as useful but weakens a broad claim that large oracle gaps are available in bounded trace replay.

## Boundaries and scale limits

No GPU kernels, RDMA transport, vLLM/Mooncake runtime integration, or datacenter-scale serving was measured. Service time is a linear prefill/decode/transfer proxy, so claims are limited to trace-level scheduling/cache mechanics.

## Claim scope

Public Mooncake FAST'25 trace replay with a calibrated CPU queueing/cache simulator: KV reuse improves overloaded SLO goodput versus no-cache, but a future-aware oracle eviction policy adds only a small goodput gain over an online runtime LRU policy.

## Why it stopped

Tier 2 replay produced a useful mechanism signal but not a paper-positive positive result: oracle-vs-runtime goodput gains were consistently small and remain simulator-bound.

## Recommended next action

Stop paper escalation for this claim; if continuing, run one bounded deepen test that replaces online LRU with frequency/recency-aware cache admission or eviction and requires at least 5% goodput gain over runtime LRU on the same traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Frequency-aware KV cache admission to close Mooncake trace oracle gaps
- Success threshold: At least 5% mean SLO-goodput improvement over runtime LRU on conversation_trace and synthetic_trace, while staying within 50% of the Belady oracle hit-rate gap and not worsening P99 latency beyond the 2500 ms SLO.
- Stop condition: Stop if the frequency-aware policy improves mean goodput by less than 2% over runtime LRU on both conversation_trace and synthetic_trace, or if gains only appear when using future information.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-serving-runtime-replay-of-mooncake-kv-oracle-gaps-0d6e056fb8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
