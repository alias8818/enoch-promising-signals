# CPU Log Replay Oracle for KV Eviction Policies

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-log-replay-oracle-for-kv-eviction-policies-77a9c3abc698`
Run ID: `cpu-log-replay-oracle-for-kv-eviction-policies-77a9c3abc698-20260522T074254487027+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8b8a45c3f053

## What looked useful

Medium synthetic replay completed in 100.245 s with 482.5 MB max RSS. Oracle throughput ranged from 180,586 to 565,356 accesses/s, median 396,583. Best online miss rate was 1.022x to 2.051x the oracle miss rate, median 1.213x, showing the offline oracle is practical enough for local policy-gap studies and exposes non-trivial headroom.

## Boundaries and scale limits

Evidence is synthetic and page-level only: no production LLM-serving logs, real scheduler traces, tensor transfer costs, prefix-sharing metadata costs, batching interactions, or end-to-end latency/token-throughput measurements. Medium run covered up to 3.24M accesses in one trace and 15 workload/capacity cases.

## Claim scope

A single-process CPU Python replay harness can compute a Belady-style offline page-cache oracle for bounded synthetic KV-shaped traces and reveal measurable oracle gaps versus LRU, FIFO, LFU, and random baselines.

## Why it stopped

Synthetic proxy evidence supports the mechanism but does not directly validate production KV eviction behavior or paper-grade claims.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next action is to replay real or high-fidelity serving-simulator KV block logs through the same oracle and require consistent oracle gaps plus latency/token-throughput impact.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Serving Trace Replay for KV Eviction Oracle Gaps
- Success threshold: At least two real or faithful trace workloads show best-online miss rate at least 1.10x the oracle miss rate at production-relevant capacities, and miss-rate differences correlate with a measurable serving cost metric.
- Stop condition: Stop if real/fidelity traces show less than 1.05x oracle gap across relevant capacities or if miss-rate differences do not move any serving cost metric.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-log-replay-oracle-for-kv-eviction-policies-77a9c3abc698`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
