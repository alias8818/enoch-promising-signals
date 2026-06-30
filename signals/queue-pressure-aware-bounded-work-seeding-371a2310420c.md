# Queue-Pressure Aware Bounded Work Seeding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-pressure-aware-bounded-work-seeding-371a2310420c`
Run ID: `queue-pressure-aware-bounded-work-seeding-371a2310420c-20260620T151822434630+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8478ec7cb8b7

## What looked useful

Pressure-aware bounded seeding was useful under pressure: versus static bounded, it reduced saturated p95 root latency by 18.26%, mean queue length by 51.66%, and increased total value by 1.28%; versus eager unbounded, it reduced saturated p95 latency by 65.92%, mean queue length by 91.45%, and avoided 31.63 dropped roots on average. It was not uniformly better: versus eager unbounded it lost 20.31% total value in light load and 22.49% in bursty load by suppressing speculative follow-ups.

## Boundaries and scale limits

Synthetic discrete-event simulation only; no production Enoch scheduler integration, live traces, operator workflows, multi-worker controller traffic, or end-to-end agent quality measurement. The result is a mechanism probe, not publication-grade validation.

## Claim scope

In a deterministic synthetic queueing simulator with 3 load regimes, 8 workers, and 30 replicates per policy/regime, pressure-aware bounded work seeding reduced queue length and p95 root-task latency under bursty and saturated load compared with static bounded and eager unbounded baselines, while trading off speculative total value in lighter regimes.

## Why it stopped

Closed as no-paper useful signal: the local synthetic evidence supports the pressure-control mechanism but is mixed and not direct production evidence.

## Recommended next action

Run a bounded trace-driven follow-up against real Enoch queue logs or a local controller harness, with success requiring lower p95 root latency and no more than 5% loss in useful completed work versus static bounded.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-driven queue-pressure-aware seeding validation
- Success threshold: Pressure-aware bounded seeding reduces p95 root latency by at least 10% and mean queue length by at least 25% versus static bounded under bursty/saturated load, while total useful completed work is no worse than 5% below static bounded.
- Stop condition: Stop if pressure-aware seeding loses more than 5% useful completed work versus static bounded in two independent bursty/saturated trace regimes, or if no trace/harness can be run locally.

## Evidence references

- Artifact root: `<local-path>/projects/queue-pressure-aware-bounded-work-seeding-371a2310420c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
