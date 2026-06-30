# Stragglers-First Async Aggregation with Staleness Compensation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `stragglers-first-async-aggregation-with-staleness-compensation-3dfafbb892af`
Run ID: `stragglers-first-async-aggregation-with-staleness-compensation-3dfafbb892af-20260612T235029544239+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3474a9ab489f

## What looked useful

Do not test stragglers-first or full staleness compensation as the first production variant. If pursuing the idea, test damped compensation under measured backlog pressure: in this probe compensation scale 0.25 beat arrival-order on 23/24 paired seeds by -0.00543 mean final-loss delta, while full compensation lost by +0.00197 and stragglers-first without compensation lost by +0.00487.

## Boundaries and scale limits

Synthetic convex task only; no real distributed runtime, GPU kernels, network transport, large model, optimizer-state interaction, or non-convex training dynamics. Low-backlog effects were much smaller, so the mechanism appears dependent on server backlog and high staleness.

## Claim scope

In a local CPU-only discrete-event convex logistic-regression simulation with heterogeneous worker delays, non-IID slow-worker shards, and server backlog, stragglers-first ordering was harmful by itself, full first-order staleness compensation was also worse than arrival-order, but damped compensation at scales 0.25-0.50 improved final validation loss versus arrival-order under high backlog.

## Why it stopped

Synthetic convex evidence gives conditional mechanism support but not direct publication-grade validation; full compensation and stragglers-first alone were negative under the main high-backlog setting.

## Recommended next action

Stop this run as no-paper useful signal; next concrete action is a bounded real async-training follow-up comparing arrival-order, freshest-first, stragglers-first, and damped compensation on a small neural model with measured worker delays.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real async trainer test of damped staleness compensation under measured backlog
- Success threshold: Damped compensation must improve mean time-to-target or final validation metric by at least 3% versus the best non-compensated baseline across paired seeds, with no increase in divergence or severe loss spikes.
- Stop condition: Stop if damped compensation fails to beat both arrival-order and freshest-first on at least 60% of paired seeds, or if measured backlog is too low to create staleness above the synthetic low-backlog regime.

## Evidence references

- Artifact root: `<local-path>/projects/stragglers-first-async-aggregation-with-staleness-compensation-3dfafbb892af`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
