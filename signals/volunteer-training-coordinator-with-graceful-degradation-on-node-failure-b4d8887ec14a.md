# Volunteer Training Coordinator with Graceful Degradation on Node Failure

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `volunteer-training-coordinator-with-graceful-degradation-on-node-failure-b4d8887ec14a`
Run ID: `volunteer-training-coordinator-with-graceful-degradation-on-node-failure-b4d8887ec14a-20260610T025600160063+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7021e6dc2932

## What looked useful

Across 60 main trials at 25% node failure, resilient coordination completed 100% of volunteers versus 76.15% for static assignment and reduced mean stranded volunteers from 57.23 to 0, at the cost of p95 completion time rising from 148.82 to 168.63 ticks. A 50% failure tight-deadline stress case still improved completion from 51.70% to 98.42% but SLA completion was only 79.68%, showing the mechanism is capacity/window-sensitive.

## Boundaries and scale limits

Synthetic simulation only; no live distributed service, persistence layer, network partition model, notification system, real volunteer behavior, or production fault injection was tested. Runs were short CPU-only local experiments.

## Claim scope

In a deterministic discrete-event simulation of 240 volunteers, 8 worker nodes, four training modules, and injected node failures, a lease/heartbeat/reserve-capacity reassignment coordinator reduced stranded volunteers and improved completion versus static node assignment.

## Why it stopped

Bounded synthetic simulation supports the graceful-degradation mechanism but does not provide direct deployment-grade evidence.

## Recommended next action

Stop this run as a no-paper useful signal; next run should build a minimal queue-backed prototype and inject real worker process failures to test recovery with durable task state.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Queue-backed volunteer training coordinator fault-injection prototype
- Success threshold: At 25% worker loss, resilient prototype completes at least 95% of volunteers with mean recovery lag no more than 2 lease timeouts and duplicate completed modules below 2%, while static assignment strands at least 10 percentage points more volunteers.
- Stop condition: Stop if durable-state recovery cannot beat static assignment by 10 percentage points completion after 30 seeded trials, or if duplicate completed modules exceed 5% despite lease fencing.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-training-coordinator-with-graceful-degradation-on-node-failure-b4d8887ec14a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
