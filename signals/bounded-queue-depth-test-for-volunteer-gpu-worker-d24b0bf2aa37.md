# Bounded Queue Depth Test for Volunteer GPU Worker

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-queue-depth-test-for-volunteer-gpu-worker-d24b0bf2aa37`
Run ID: `bounded-queue-depth-test-for-volunteer-gpu-worker-d24b0bf2aa37-20260614T030621938367+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b55635fe84fe

## What looked useful

Bounded queue depth appears practically useful for a volunteer GPU worker because it caps admitted work and memory exposure with a modest throughput penalty on the tested GB10 workload.

## Boundaries and scale limits

Synthetic local workload only; no real volunteer-worker arrival traces, network ingestion, production reject/backpressure semantics, multi-tenant load, heterogeneous GPUs, or sustained hours-long overload were tested.

## Claim scope

On a single NVIDIA GB10 worker running 64 synthetic CUDA FP16 matrix-multiply jobs with 128 MiB host payloads per job, bounded admission depths 2/4/8 capped admitted jobs at the configured depth and reduced peak process RSS versus unbounded eager admission; depth 8 retained 91.6% of unbounded throughput while reducing peak RSS by about 79.0%.

## Why it stopped

Local synthetic evidence supports the mechanism but is not direct volunteer-fleet evidence or a publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next concrete step is a trace-replay worker test with explicit reject/backpressure semantics and real or calibrated volunteer arrival distributions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Replay Bounded Queue Depth Test for Volunteer GPU Worker
- Success threshold: At least one bounded depth reduces peak RSS by 50% or more and p99 admitted queue wait by 50% or more while retaining at least 85% of unbounded completed-job throughput with no increase in job errors.
- Stop condition: Stop if all bounded depths either lose more than 15% throughput or fail to reduce peak RSS by at least 50% under the replayed workload.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-queue-depth-test-for-volunteer-gpu-worker-d24b0bf2aa37`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
