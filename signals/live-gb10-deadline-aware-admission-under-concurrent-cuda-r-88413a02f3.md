# Live GB10 deadline-aware admission under concurrent CUDA request dispatch

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-gb10-deadline-aware-admission-under-concurrent-cuda-r-88413a02f3`
Run ID: `live-gb10-deadline-aware-admission-under-concurrent-cuda-r-88413a02f3-20260613T112945130777+0000`

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

- Parent run decision: Queue admission policy under near-capacity gb10 lane: enoch://control-plane/projects/queue-admission-policy-under-near-capacity-gb10-lane-527f13858bd1/runs/queue-admission-policy-under-near-capacity-gb10-lane-527f13858bd1-20260613T105911856467+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/10a2893af618

## What looked useful

A small direct GB10 CUDA test supports the mechanism that deadline-aware admission can reject impossible concurrent GPU requests and preserve deadline-satisfying completions under overload, but the predictor must be conservatively calibrated because concurrent launch overhead can otherwise cause admitted misses.

## Boundaries and scale limits

Synthetic burn kernels only; one GPU; one overloaded arrival/deadline/work distribution; no real inference runtime, batching, stream priority scheduling, preemption, multi-tenant workload, or long-duration robustness test.

## Claim scope

On one GB10, for a deterministic 96-request synthetic CUDA-kernel workload launched by concurrent host request threads into nonblocking streams, conservative calibrated deadline-aware admission improved accepted deadline hit rate from 5.2% to 100% and deadline-met goodput from 12.68/s to 141.23/s compared with admitting all requests.

## Why it stopped

Tier 1 controlled direct test completed and produced useful mechanism evidence, but the evidence is small/synthetic and not publication-grade.

## Recommended next action

Run a bounded deepen follow-up with a real inference/CUDA runtime or a workload sweep over arrival rates, deadline slack, and predictor safety factors before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Deadline-aware admission under real CUDA inference workload sweeps
- Success threshold: Deadline-aware admission achieves at least 90% accepted deadline hit rate and at least 2x deadline-met goodput over admit-all in a majority of tested overload conditions without relying on contaminated concurrent benchmark runs.
- Stop condition: Stop if deadline-aware admission fails to beat admit-all deadline-met goodput by 2x or cannot maintain at least 90% accepted deadline hit rate after conservative calibration on two representative overload settings.

## Evidence references

- Artifact root: `<local-path>/projects/live-gb10-deadline-aware-admission-under-concurrent-cuda-r-88413a02f3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
