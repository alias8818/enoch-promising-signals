# Bounded Work Lane Feed Pressure Control

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-work-lane-feed-pressure-control-05973c7044cc`
Run ID: `bounded-work-lane-feed-pressure-control-05973c7044cc-20260531T194810907752+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8d9d476b9342

## What looked useful

Across 40 paired seeds, lane-pressure admission improved p95 wait and throughput in 40/40 seeds versus both baselines. Mean p95 wait fell 63.4% versus unbounded greedy and 57.1% versus global cap; mean job throughput rose 53.5% and 23.0%, respectively.

## Boundaries and scale limits

Synthetic CPU-only simulation only; no production worker runtime, no real memory allocator/queue pressure, no network or GPU effects, and no trace replay from an operational system.

## Claim scope

In a deterministic synthetic discrete-event simulation with bursty arrivals, heavy-tailed service costs, and heterogeneous worker lanes, per-lane bounded feed pressure improved throughput and tail wait versus unbounded greedy feed and a shared global cap baseline.

## Why it stopped

Simulation-proxy evidence supports the mechanism but is not direct production/runtime evidence, so this run should close as no-paper useful signal.

## Recommended next action

Run a bounded deepen test by implementing the policy in a real local async/threaded worker-lane prototype and measuring RSS, queue depth, lane utilization, throughput, and tail latency under replayed bursty/heavy-tail traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Worker-Lane Prototype for Bounded Feed Pressure
- Success threshold: Lane-pressure policy improves p95 latency by at least 25% versus both baselines without reducing completed throughput by more than 3% and without increasing peak RSS versus global cap.
- Stop condition: Stop if lane-pressure fails the latency threshold in more than half of paired traces or introduces more than 10% throughput loss in the median run.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-work-lane-feed-pressure-control-05973c7044cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
