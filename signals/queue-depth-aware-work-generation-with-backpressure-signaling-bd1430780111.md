# Queue-depth-aware work generation with backpressure signaling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-depth-aware-work-generation-with-backpressure-signaling-bd1430780111`
Run ID: `queue-depth-aware-work-generation-with-backpressure-signaling-bd1430780111-20260608T023738491215+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e4978c02a2ea

## What looked useful

Across three 20-replicate simulated scenarios, feedback policies eliminated drops versus open-loop. Queue-depth gating preserved throughput within about 0.1% while cutting wasted generation 98.1-99.1%. Explicit backpressure cut p95 latency 55.8-81.0% and mean queue depth 54.2-93.4% versus queue-depth gating, but lost 0.0-5.9% throughput depending on scenario.

## Boundaries and scale limits

Synthetic simulation only; not validated on a real worker pool, RPC/control-plane implementation, multi-producer scheduler, GPU workload, distributed system, or production trace.

## Claim scope

In a deterministic discrete-event bounded-queue simulator with one generator and noisy periodic downstream capacity shocks, queue-depth-aware generation eliminated drops and sharply reduced wasted generated work; explicit delayed backpressure further reduced p95 latency and backlog but sometimes traded away throughput.

## Why it stopped

Closed as no-paper useful signal because the evidence is simulation-only and the throughput-preservation part of the hypothesis is mixed rather than fully supported.

## Recommended next action

Run a bounded real worker-pool microbenchmark with open-loop, queue-depth-only, and explicit delayed-backpressure controllers before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real worker-pool backpressure microbenchmark with delayed signals
- Success threshold: Explicit backpressure reduces p95 latency by at least 40% and wasted generated work by at least 80% versus queue-depth-only gating while completed jobs/sec is within 3% and fairness does not degrade by more than 5%.
- Stop condition: Stop if explicit backpressure loses more than 8% completed jobs/sec in two or more scenarios, adds controller overhead that dominates saved work, or fails to improve p95 latency by at least 20% versus queue-depth-only gating.

## Evidence references

- Artifact root: `<local-path>/projects/queue-depth-aware-work-generation-with-backpressure-signaling-bd1430780111`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
