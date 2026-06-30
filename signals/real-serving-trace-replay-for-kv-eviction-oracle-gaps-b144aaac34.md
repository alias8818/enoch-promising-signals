# Real Serving Trace Replay for KV Eviction Oracle Gaps

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-serving-trace-replay-for-kv-eviction-oracle-gaps-b144aaac34`
Run ID: `real-serving-trace-replay-for-kv-eviction-oracle-gaps-b144aaac34-20260522T075854715194+0000`

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

- Parent run decision: CPU Log Replay Oracle for KV Eviction Policies: enoch://control-plane/projects/cpu-log-replay-oracle-for-kv-eviction-policies-77a9c3abc698/runs/cpu-log-replay-oracle-for-kv-eviction-policies-77a9c3abc698-20260522T074254487027+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8b8a45c3f053

## What looked useful

LRU exceeded the 10% relative excess miss threshold at five of six cache capacities, with a maximum gap of 35.03% and median gap of 20.19%; LFU/FIFO/random also left meaningful oracle headroom over most capacities.

## Boundaries and scale limits

Single public trace, one-hour metadata replay, unit block sizing, no live model/server latency, no GPU memory pressure, no multi-node validation.

## Claim scope

On the public Mooncake arxiv trace, a deterministic block-level replay over 23,608 real requests shows common online eviction policies can incur more than 10% excess KV block misses relative to a Belady next-use oracle at bounded cache capacities.

## Why it stopped

Tier 1 direct trace replay met the threshold for a useful mechanism signal, but this remains no-paper evidence because it does not measure live serving latency or GPU memory behavior.

## Recommended next action

Run a bounded vLLM/LMCache or Mooncake-compatible replay using the same trace and a small model/server configuration, comparing LRU-like eviction to an oracle-informed/admission baseline on recomputed prefill tokens and p95 request latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded Serving Runtime Replay of Mooncake KV Oracle Gaps
- Success threshold: At least 10% fewer recomputed prefill tokens or at least 5% lower p95 latency versus the online baseline at one bounded cache size, with no throughput regression above 5%.
- Stop condition: Stop if the runtime replay shows less than 3% improvement in both recomputed tokens and p95 latency proxy at all tested cache sizes, or if the serving stack cannot consume the trace without substantial new infrastructure.

## Evidence references

- Artifact root: `<local-path>/projects/real-serving-trace-replay-for-kv-eviction-oracle-gaps-b144aaac34`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
