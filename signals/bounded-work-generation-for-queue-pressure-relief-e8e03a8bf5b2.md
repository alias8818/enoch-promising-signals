# Bounded Work Generation for Queue Pressure Relief

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-work-generation-for-queue-pressure-relief-e8e03a8bf5b2`
Run ID: `bounded-work-generation-for-queue-pressure-relief-e8e03a8bf5b2-20260607T183809909574+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4965522b9dfe

## What looked useful

Pressure-sensitive work generation reduced main-run p95 queue by 95.8% versus unbounded generation and 93.2% versus a static one-child cap, reduced p95 wait by 88.9% versus unbounded and 88.8% versus static cap, dropped zero tasks, and retained 11.7% more utility than admission-only dropping.

## Boundaries and scale limits

Evidence is simulation-only. It does not validate real service traces, distributed queues, non-FIFO schedulers, multi-tenant fairness, cancellation costs, delayed pressure signals, or production task utility.

## Claim scope

In a local synthetic FIFO queue simulation with recursive child-work generation, bursty arrivals, 16 workers, depth-decayed utility, and 40 main-run seeds, pressure-sensitive child-work bounding sharply reduced p95 queue and wait while retaining more utility than static child caps or admission-only dropping.

## Why it stopped

The mechanism is supported by reproducible synthetic evidence, but the result is not paper-ready because production trace behavior and real utility/drop costs were not directly measured.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next concrete step is a bounded trace-replay follow-up using real or realistic queue traces with the same baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace Replay of Pressure-Sensitive Work Generation
- Success threshold: Pressure-sensitive generation achieves at least 50% lower p95 wait than static cap and at least 5% higher retained utility than admission-only dropping without reducing completed exogenous work by more than 1%.
- Stop condition: Stop if pressure-sensitive generation fails to beat either static cap on p95 wait or admission-only on retained utility in two representative trace classes.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-work-generation-for-queue-pressure-relief-e8e03a8bf5b2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
