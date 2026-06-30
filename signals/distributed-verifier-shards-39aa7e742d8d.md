# Distributed Verifier Shards

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `distributed-verifier-shards-39aa7e742d8d`
Run ID: `distributed-verifier-shards-39aa7e742d8d-20260521T223852892600+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2eeb37ddb77e

## What looked useful

All sharded strategies detected the expected invalid proofs. On the bounded 192000-constraint workload, 8-worker static intra-proof sharding reached 0.5889 s versus 4.5405 s serial, a 7.71x speedup; tiny smoke workloads remained overhead dominated.

## Boundaries and scale limits

No real proof system, model verifier trace, networked distributed execution, adversarial shard behavior, GPU kernel, or heterogeneous constraint graph was tested.

## Claim scope

On a single 20-CPU host with synthetic independent SHA-256 verifier constraints, process-local verifier shards preserved invalid-proof detection and improved throughput once per-shard work was large enough to amortize dispatch overhead.

## Why it stopped

No-paper useful signal only: local synthetic evidence supports the mechanism but does not directly validate real distributed verifier shards.

## Recommended next action

Stop paper path for this run; run a bounded deepen test using a real verifier trace or heterogeneous constraint-cost distribution before considering larger distributed validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Heterogeneous Real-Trace Verifier Shard Scheduling
- Success threshold: Dynamic sharding preserves all invalid detections and improves p95 latency or throughput by at least 20% over static sharding on heterogeneous verifier workloads.
- Stop condition: Stop if dynamic sharding fails correctness parity or remains within 5% of static sharding across all seeds while adding scheduling overhead.

## Evidence references

- Artifact root: `<local-path>/projects/distributed-verifier-shards-39aa7e742d8d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
