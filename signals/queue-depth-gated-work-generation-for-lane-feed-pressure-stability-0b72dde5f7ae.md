# Queue-depth-gated work generation for lane feed pressure stability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-depth-gated-work-generation-for-lane-feed-pressure-stability-0b72dde5f7ae`
Run ID: `queue-depth-gated-work-generation-for-lane-feed-pressure-stability-0b72dde5f7ae-20260525T074150938866+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/48e5caa5378f

## What looked useful

Queue-depth gating reduced p95 queue depth by at least 75.8%, reduced mean queue depth by at least 74.1%, and eliminated overflow across 24 paired robustness comparisons, while worst throughput loss was 0.61%.

## Boundaries and scale limits

Synthetic CPU-only simulation; no real production traces, live dataloader, GPU serving pipeline, model-training loop, quality metric, multi-tenant fairness test, or datacenter-scale validation.

## Claim scope

In a deterministic synthetic multi-lane queueing model with heterogeneous service rates, bursts, stalls, finite queue capacity, and 8-seed robustness checks, per-lane queue-depth-gated work generation stabilized lane feed pressure versus open-loop generation.

## Why it stopped

Synthetic evidence supports the mechanism but is not direct enough for a paper or production claim.

## Recommended next action

Stop this worker run as no-paper useful-signal evidence; next run should replay queue-depth gating against real lane feed traces or a live dataloader/serving feeder with direct utilization, latency, overflow, and quality metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace replay validation of queue-depth-gated lane work generation
- Success threshold: At least 50% p95 queue occupancy reduction and 90% overflow/drop reduction, with throughput or utilization within 2% of baseline and p95 latency increase no greater than 5%.
- Stop condition: Stop as unsupported if gating fails to reduce p95 occupancy by 25%, causes more than 2% throughput/utilization loss, or increases p95 latency by more than 5% in matched direct runs.

## Evidence references

- Artifact root: `<local-path>/projects/queue-depth-gated-work-generation-for-lane-feed-pressure-stability-0b72dde5f7ae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
