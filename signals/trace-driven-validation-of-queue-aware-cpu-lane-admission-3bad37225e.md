# Trace-driven validation of queue-aware CPU-lane admission

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `trace-driven-validation-of-queue-aware-cpu-lane-admission-3bad37225e`
Run ID: `trace-driven-validation-of-queue-aware-cpu-lane-admission-3bad37225e-20260611T093801953952+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Queue-aware admission policy for deep CPU lane: enoch://control-plane/projects/queue-aware-admission-policy-for-deep-cpu-lane-0084a1c24cca/runs/queue-aware-admission-policy-for-deep-cpu-lane-0084a1c24cca-20260611T085519869272+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7c9d6f5d0952

## What looked useful

Queue-aware CPU-lane admission failed to beat tuned static overflow by the required 10% p95 latency threshold. Across 101 policy configurations at CPU speed factor 2.6 and sensitivity factors 1.5, 2.0, 3.0, and 3.5, zero traces met the threshold; the best oracle trace gain was only 0.268%.

## Boundaries and scale limits

No production traces, no live serving executor, no batching/cache effects, and no datacenter-scale workload diversity. The result falsifies the Tier-1 controlled threshold, not all possible queue-aware admission designs.

## Claim scope

Controlled deterministic trace replay of CPU-lane admission on three synthetic but direct arrival/service traces, with bounded sweeps over static overflow and queue-aware policy parameters.

## Why it stopped

Tier-1 controlled direct replay and bounded sensitivity sweeps failed the stated threshold; this is an early controlled falsification rather than a full production validation.

## Recommended next action

Stop this branch as a no-paper useful negative signal unless real serving traces are available to test whether finish-time prediction contains information absent from tuned static overflow.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/trace-driven-validation-of-queue-aware-cpu-lane-admission-3bad37225e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
