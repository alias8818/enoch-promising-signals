# Queue-depth-aware cascade controller

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-depth-aware-cascade-controller-7379c2c4837b`
Run ID: `queue-depth-aware-cascade-controller-7379c2c4837b-20260620T234011136506+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b5f990dbbbaa

## What looked useful

Queue depth is a plausible control signal, but the simple tested heuristic is not robust: p95 latency improved by 2.63% in low_load and 0.59% in bursty_overload, while near_capacity p95 latency worsened by 0.44% and utility fell by 0.0066.

## Boundaries and scale limits

CPU-only discrete-event proxy with synthetic confidence, correctness, service-time, and arrival distributions; no real LLM serving stack, batching scheduler, production trace, or GPU contention was tested.

## Claim scope

In a deterministic synthetic two-tier cascade simulation, queue-depth-aware routing produced small improvements in low-load and bursty-overload scenarios but regressed near-capacity latency and utility versus a cheap-first confidence cascade.

## Why it stopped

Mixed proxy result: useful scheduling signal, but the tested controller regressed near-capacity utility and does not support publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up using held-out synthetic or captured traces and a controller that jointly estimates cheap and expensive queue occupancy before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out trace evaluation of joint-queue cascade routing
- Success threshold: Across all held-out regimes, improve p95 latency by at least 5% or utility by at least 0.02 versus cheap_first with no scenario showing more than 1% p95 latency regression or negative utility delta.
- Stop condition: Stop if the joint-queue controller still shows any held-out near-capacity p95 latency regression above 1% or negative utility delta after one bounded tuning pass.

## Evidence references

- Artifact root: `<local-path>/projects/queue-depth-aware-cascade-controller-7379c2c4837b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
