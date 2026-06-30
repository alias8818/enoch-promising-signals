# Heterogeneous Home Training Router

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `heterogeneous-home-training-router-627fcabb7cfc`
Run ID: `heterogeneous-home-training-router-627fcabb7cfc-20260526T081430936449+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12a892dcebd7

## What looked useful

Routing sophistication is secondary to memory-fit and CPU-spillover control in this probe. The router improved mean flow by 36.99-42.46% versus fastest-fit across light/moderate/stress loads, but p95 gains were only 7.69-15.10%, deadline miss rates stayed 0.9025-0.9946, and gains over earliest-finish-with-queue were about 0-1.2%. CPU fallback consumed roughly 71.6-75.0% of runtime under the router.

## Boundaries and scale limits

No real model training, real household trace, checkpoint migration, network contention, privacy constraint, or multi-host execution was tested. The result is simulator-only and should not be treated as full validation or rejection of heterogeneous home training.

## Claim scope

Synthetic discrete-event home-lab routing traces with four heterogeneous devices, memory constraints, daily availability windows, reliability penalties, and 30 seeds at 40/80/240 jobs per seed. The calendar-aware router improves mean flow versus always-fastest routing but adds negligible benefit over a simpler queue-aware earliest-finish baseline and does not solve deadline reliability under memory-heavy spillover.

## Why it stopped

Synthetic proxy evidence is mixed and insufficient for a paper: the router beats naive fastest-fit on mean flow, but barely beats a simple queue-aware baseline and fails deadline reliability because memory-heavy jobs spill to CPU fallback.

## Recommended next action

Stop this router-scoring line as no-paper evidence; the next bounded test should evaluate admission control or model reshaping for jobs that exceed local GPU memory before adding richer routing terms.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Memory-fit admission control for heterogeneous home training
- Success threshold: CPU-fallback runtime share under 30% and at least 25% p95-flow improvement versus earliest_finish_no_calendar without increasing rejected/deferred jobs above 15%.
- Stop condition: Stop if CPU-fallback share remains above 50% or p95-flow improvement is below 10% on the moderate 80-job trace.

## Evidence references

- Artifact root: `<local-path>/projects/heterogeneous-home-training-router-627fcabb7cfc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
