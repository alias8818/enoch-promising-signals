# Queue Pressure with Zero Promotable Count

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-pressure-with-zero-promotable-count-6b7170b89936`
Run ID: `queue-pressure-with-zero-promotable-count-6b7170b89936-20260605T223355248328+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f9f83ddb00d4

## What looked useful

Pressure-only control wasted 100% of promotion actions in persistent-zero windows and 7.55% in delayed-eligibility windows; the promotable-count guard reduced wasted actions to 0% while preserving effectively the same completions and latency, and was identical to pressure-only when all queued work was immediately promotable.

## Boundaries and scale limits

Synthetic simulation only; no production scheduler code, real queue traces, distributed contention, priority classes, GPU memory pressure, or side-effectful promotion operations were tested.

## Claim scope

In a deterministic synthetic queue simulator with backlog pressure, eligibility delay, promotion cooldown, and service capacity, promotion decisions made during pressure windows with promotable_count == 0 are wasted; adding a promotable_count > 0 guard eliminates those wasted actions without changing behavior in the steady-promotable positive control.

## Why it stopped

Closed as useful no-paper evidence because the result is synthetic/proxy evidence for the mechanism, not a production or trace-level validation.

## Recommended next action

Run a bounded trace-driven scheduler replay that includes real zero-promotable pressure windows before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace replay for zero-promotable queue pressure gating
- Success threshold: Guarded policy reduces wasted zero-promotable promotion attempts by at least 95% while changing completion count by less than 1% and p95 wait after eligibility by less than 5% versus pressure-only.
- Stop condition: Stop if the trace contains no zero-promotable pressure windows, if promotion attempts have mandatory side effects not represented by promotion count, or if the guard worsens completion or p95 wait beyond the success thresholds.

## Evidence references

- Artifact root: `<local-path>/projects/queue-pressure-with-zero-promotable-count-6b7170b89936`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
