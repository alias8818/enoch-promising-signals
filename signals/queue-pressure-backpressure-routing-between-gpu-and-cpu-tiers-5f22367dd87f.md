# Queue-Pressure Backpressure Routing Between GPU and CPU Tiers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-pressure-backpressure-routing-between-gpu-and-cpu-tiers-5f22367dd87f`
Run ID: `queue-pressure-backpressure-routing-between-gpu-and-cpu-tiers-5f22367dd87f-20260610T070257296262+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/01fe695f76d4

## What looked useful

Backpressure routing cut p99 latency versus static overflow by 42.7% to 59.7% across tested scenarios. SLO miss-rate reductions were 93.3% to 99.4% in adequate-capacity scenarios, but only 11.0% in the thin CPU tier case, showing the mechanism depends on overflow capacity.

## Boundaries and scale limits

Synthetic service times only; no real GPU kernels, batching, prefill/decode split, memory pressure, network overhead, autoscaler behavior, or production traffic traces. The sweep used 4 toy scenarios, 20 seeds each, and 600 simulated seconds per scenario.

## Claim scope

In a deterministic synthetic queueing simulation with bursty arrivals, a fast constrained GPU tier, and a slower parallel CPU overflow tier, queue-pressure backpressure routing reduced p99 latency and SLO miss rate versus GPU-only and static overflow policies when overflow capacity was adequate; it remained capacity-sensitive when the CPU tier was thin.

## Why it stopped

No-paper closure: this run produced useful synthetic evidence, but direct serving evidence is required for publication-grade validation.

## Recommended next action

Run a bounded trace-replay or local live-serving experiment with measured GPU and CPU service distributions before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Replay Validation of Queue-Pressure GPU-to-CPU Backpressure Routing
- Success threshold: Queue-pressure routing reduces p99 latency by at least 20% and SLO miss rate by at least 50% versus static overflow while keeping CPU utilization below saturation and preserving throughput.
- Stop condition: Stop if trace replay shows less than 10% p99 improvement versus static overflow, higher SLO miss rate, or sustained CPU saturation under the tested burst load.

## Evidence references

- Artifact root: `<local-path>/projects/queue-pressure-backpressure-routing-between-gpu-and-cpu-tiers-5f22367dd87f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
