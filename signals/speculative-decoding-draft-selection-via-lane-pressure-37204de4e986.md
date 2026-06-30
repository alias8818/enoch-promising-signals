# Speculative Decoding Draft Selection via Lane Pressure

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `speculative-decoding-draft-selection-via-lane-pressure-37204de4e986`
Run ID: `speculative-decoding-draft-selection-via-lane-pressure-37204de4e986-20260523T162204411828+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/72c532193db4

## What looked useful

Per-request adaptive draft lengths improved accepted/drafted ratio but created padded verification waste and under-drafting, producing lower throughput and worse p95 latency than fixed k=4 in all tested traffic profiles.

## Boundaries and scale limits

Synthetic CPU-only scheduler model; no real draft or target model kernels, no GPU lane traces, no KV-cache effects, and no production serving runtime. Results are mechanism-level early falsification, not full deployment validation.

## Claim scope

In a deterministic padded-batch synthetic speculative-decoding scheduler, naive per-request lane-pressure draft selection failed to beat a fixed k=4 baseline across bimodal, mostly-high, mostly-low, and flat acceptance profiles; a batch-uniform pressure control only tied fixed k=4 in mostly-high traffic and underperformed elsewhere.

## Why it stopped

Proxy simulator evidence does not support the tested lane-pressure draft-selection policy; this is not a full validation, but it is sufficient to reject the naive per-lane form before spending larger serving-system effort.

## Recommended next action

Stop this run as a proxy early falsification; the next bounded test should implement k-bucketing or batch-homogeneous pressure selection in a real small-model speculative decoding runtime and require direct GPU lane-utilization evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bucketed Lane-Pressure Speculative Decoding in a Real Small-Model Runtime
- Success threshold: At least 5% higher tokens/second than fixed k=4 with no p95 latency regression greater than 2% on at least two mixed-acceptance workloads, plus lower measured wasted verification work.
- Stop condition: Stop if bucketed or homogeneous pressure selection fails to beat fixed k=4 on throughput or worsens p95 latency by more than 2% in two independent workloads.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-draft-selection-via-lane-pressure-37204de4e986`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
