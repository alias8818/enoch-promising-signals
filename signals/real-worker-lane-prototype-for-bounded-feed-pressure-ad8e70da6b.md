# Real Worker-Lane Prototype for Bounded Feed Pressure

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-worker-lane-prototype-for-bounded-feed-pressure-ad8e70da6b`
Run ID: `real-worker-lane-prototype-for-bounded-feed-pressure-ad8e70da6b-20260601T022410824110+0000`

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

- Parent run decision: Bounded Work Lane Feed Pressure Control: enoch://control-plane/projects/bounded-work-lane-feed-pressure-control-05973c7044cc/runs/bounded-work-lane-feed-pressure-control-05973c7044cc-20260531T194810907752+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8d9d476b9342

## What looked useful

Bounded per-worker lanes reduced peak outstanding work from 4967 to 28 tasks (177.4x), reduced peak parent RSS from 343088 KiB to 27624 KiB (91.9%), and completed all tasks at 109.2% of unbounded throughput while increasing producer submit time from 0.395 s to 4.225 s, demonstrating real backpressure.

## Boundaries and scale limits

Single-host CPU-only prototype; one worker count, one lane depth, fixed service time, fixed payload size, no network queues, no distributed workers, no failure/retry path, and no heterogeneous or bursty production traffic.

## Claim scope

In a local Python multiprocessing prototype with 4 workers, 5000 distinct 64 KiB payload tasks, fixed 3 ms worker service time, and per-worker lane depth 8, bounded worker lanes imposed producer backpressure, capped outstanding work, and avoided parent-side queue memory growth while preserving worker-limited throughput.

## Why it stopped

Tier 1 controlled direct test supports the mechanism but is not publication-grade evidence; closing as no-paper useful signal.

## Recommended next action

Run a medium confirmation with heterogeneous service times, bursty arrivals, multiple lane depths, and latency/backlog percentiles against unbounded shared and bounded shared-queue baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Worker-Lane Confirmation Under Bursty Heterogeneous Load
- Success threshold: Bounded lanes reduce peak outstanding work and peak parent RSS by at least 5x versus unbounded shared queue, retain at least 90% throughput versus the best baseline, and do not worsen p99 latency by more than 10% in at least two of three seeds.
- Stop condition: Stop if bounded lanes fail the throughput-retention threshold or worsen p99 latency by more than 25% in two seeds, or if the added controls show the observed effect is explained entirely by generic bounded shared queues.

## Evidence references

- Artifact root: `<local-path>/projects/real-worker-lane-prototype-for-bounded-feed-pressure-ad8e70da6b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
