# Real-Trace Calibrated Verifier Cache-Cost Replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `100`
Project ID: `real-trace-calibrated-verifier-cache-cost-replay-68f6e85a94`
Run ID: `real-trace-calibrated-verifier-cache-cost-replay-68f6e85a94-20260522T081404903261+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `100`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Heterogeneous Real-Trace Verifier Shard Scheduling: enoch://control-plane/projects/heterogeneous-real-trace-verifier-shard-scheduling-6da291fae9/runs/heterogeneous-real-trace-verifier-shard-scheduling-6da291fae9-20260522T020904507296+0000
- Parent run decision: Calibrated Verifier Cache-Cost Scheduling Test: enoch://control-plane/projects/calibrated-verifier-cache-cost-scheduling-test-f3743cc2fb/runs/calibrated-verifier-cache-cost-scheduling-test-f3743cc2fb-20260522T065625951455+0000

## What looked useful

Full real-trace replay found substantial reusable prefix locality: 4.676B baseline input tokens, 3.424B net token-equivalent tokens saved, 26.77% residual cost, and break-even cache overhead of about 9.21 tokens per lookup/store op. The unordered-bucket upper-bound ablation reached 81.35% net savings, showing additional non-prefix locality that exact prefix caching cannot exploit.

## Boundaries and scale limits

Evidence is trace replay over anonymized 16-token bucket IDs, not raw prompts or a live verifier/KV-cache serving implementation. It covers one public Qwen3-32B serving trace and one 5M-entry LRU capacity point; it does not measure real GPU latency, KV memory bandwidth, allocator behavior, multi-tenant interference, or end-to-end verifier accuracy/correctness.

## Claim scope

On the public ETH EASL SwissAI Qwen3-32B bucketized serving trace, timestamp-sorted replay of 3,994,435 real requests shows that a strict exact-prefix verifier/prefill cache with a 5M-entry LRU cap reduces token-equivalent input cost by 73.23% net versus a no-cache baseline under the stated lookup/store overhead model.

## Why it stopped

The mechanism is supported by a full public trace replay, but publication-grade evidence would require a real serving implementation with measured latency and memory rather than token-equivalent cache-cost replay alone.

## Recommended next action

Stop this run as no-paper useful signal; next concrete step is a bounded implementation-level replay in a real verifier/prefill engine measuring wall-clock latency, KV memory, and cache overhead on this same trace.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Implementation-Level Verifier Prefix Cache Replay on SwissAI Trace
- Success threshold: At least 35% measured net latency or GPU-work reduction versus no-cache on the same real trace, with peak cache memory and eviction metrics documented and no correctness regressions.
- Stop condition: Stop as negative if measured net savings fall below 15% at practical cache capacities or if cache memory/lookup overhead erases the replay advantage.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-calibrated-verifier-cache-cost-replay-68f6e85a94`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
