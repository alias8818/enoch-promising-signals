# Dynamic Queue-Aware Cascade Scheduling with Priority Inheritance for GPU Workers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-queue-aware-cascade-scheduling-with-priority-inheritance-for-gpu-workers-a76423c7e111`
Run ID: `dynamic-queue-aware-cascade-scheduling-with-priority-inheritance-for-gpu-workers-a76423c7e111-20260607T101501976039+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2fe9114ac6a6

## What looked useful

DQACSPI reduced high-priority p99 flow versus FIFO by 6.7%, 33.7%, and 62.3% at loads 0.65, 0.8, and 0.9, and beat cascade-aware no-inheritance by 6.1% and 5.7% at loads 0.65 and 0.8. At load 0.9 it had worse high-priority deadline miss rate than cascade_no_inherit and inherit_only, indicating the queue-aware migration heuristic is not robust near saturation.

## Boundaries and scale limits

No real CUDA scheduler integration, real trace replay, multi-GPU routing, launch overhead accounting, kernel interference, or memory-pressure validation. GPU use was limited to a CUDA availability smoke test.

## Claim scope

Synthetic discrete-event GPU-worker queue model with 8 non-preemptive workers, Poisson arrivals, lognormal 1-4 stage cascades, high/low priorities, 20 seeds per load, and loads 0.65, 0.8, and 0.9.

## Why it stopped

Proxy evidence is mixed: useful medium-load latency gains, but high-load deadline robustness fails, so this is not full validation and not paper-ready.

## Recommended next action

Stop paper path for this combined policy; next run should implement a bounded real GPU-worker replay comparing inherit_only, cascade_no_inherit, and a deadline-gated queue-aware migration variant.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Deadline-gated priority inheritance replay for GPU worker cascades
- Success threshold: At load 0.9, deadline-gated migration must match or improve inherit_only high-priority deadline miss rate while retaining at least 5% high-priority p99 flow improvement over cascade_no_inherit and without increasing low-priority p95 flow by more than 10%.
- Stop condition: Stop if deadline-gated migration still has worse high-priority deadline miss rate than inherit_only at load 0.9 or scheduler overhead exceeds 5% of median task service time.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-queue-aware-cascade-scheduling-with-priority-inheritance-for-gpu-workers-a76423c7e111`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
