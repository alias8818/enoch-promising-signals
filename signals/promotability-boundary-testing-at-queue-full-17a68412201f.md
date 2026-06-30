# Promotability Boundary Testing at Queue Full

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `promotability-boundary-testing-at-queue-full-17a68412201f`
Run ID: `promotability-boundary-testing-at-queue-full-17a68412201f-20260608T135114144446+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/9a735872710e

## What looked useful

Across 2000 trials per policy, capacity-gated promotion had zero overflows, zero dropped jobs, zero invariant failures, and completed all 96 jobs every trial; drop-on-full lost 161632 jobs and overflow violated capacity in all 2000 trials.

## Boundaries and scale limits

Simulator only; no production scheduler, distributed concurrency, database transaction, lock, retry, preemption, or real workload implementation was tested.

## Claim scope

In a local bounded-queue simulator, promotable waiting jobs evaluated while the active queue is full must remain waiting until capacity is available to preserve both hard capacity and no-loss accounting.

## Why it stopped

Bounded simulator produced a useful mechanism signal but is not direct production or publication-grade evidence.

## Recommended next action

Stop this no-paper worker run; the concrete next action is to test the same full-queue boundary against a real queue implementation with concurrent promotion attempts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Concurrent Full-Queue Promotion Test Against a Real Scheduler
- Success threshold: Zero over-capacity admissions, zero dropped/duplicated jobs, and eventual promotion of all eligible waiting jobs after capacity frees across at least 1000 concurrent boundary trials.
- Stop condition: Stop if any over-capacity admission, silent drop, duplicate job accounting, or permanent starvation occurs in the tested implementation.

## Evidence references

- Artifact root: `<local-path>/projects/promotability-boundary-testing-at-queue-full-17a68412201f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
