# Broker-backed volunteer training coordinator crash-recovery test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `broker-backed-volunteer-training-coordinator-crash-recover-0a26c7cce0`
Run ID: `broker-backed-volunteer-training-coordinator-crash-recover-0a26c7cce0-20260610T211920739836+0000`

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

- Parent run decision: Volunteer Training Coordinator with Graceful Degradation on Node Failure: enoch://control-plane/projects/volunteer-training-coordinator-with-graceful-degradation-on-node-failure-b4d8887ec14a/runs/volunteer-training-coordinator-with-graceful-degradation-on-node-failure-b4d8887ec14a-20260610T025600160063+0000
- Parent run decision: Queue-backed volunteer training coordinator fault-injection prototype: enoch://control-plane/projects/queue-backed-volunteer-training-coordinator-fault-injectio-c2ed9e7633/runs/queue-backed-volunteer-training-coordinator-fault-injectio-c2ed9e7633-20260610T202149092806+0000

## What looked useful

The broker-backed design recovered 100% of seeds versus 0% for the volatile in-memory baseline, improved mean completion rate by 0.2193, removed 48.53 duplicate completions versus the no-dedup ablation, and avoided 7.57 incomplete tasks versus the no-requeue ablation.

## Boundaries and scale limits

Synthetic simulation only; no real broker, process-level crash injection, broker failover, network partition, persistence latency, real training workload, or production operator procedure was tested.

## Claim scope

In a deterministic event simulation with 30 fixed seeds, 500 tasks per seed, 24 workers, five coordinator crashes, volunteer dropouts, and lost result acknowledgments, a broker-backed coordinator with durable pending work, leases, completions, lease requeue, and idempotent completion handling recovered all work and avoided duplicate completions.

## Why it stopped

Tier 2 simulation produced useful mechanism evidence but remains proxy evidence, not direct production or publication-grade validation.

## Recommended next action

Implement a minimal real broker-backed coordinator using one durable broker and replay the same fixed-seed crash/dropout/ack-loss workload with process-level kill/restart faults before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real broker process-level crash recovery for volunteer training coordination
- Success threshold: Across at least 30 fixed seeds and 500 or more tasks per seed, the real broker-backed coordinator completes 100% of tasks with zero duplicate completions, while the volatile baseline fails to recover on at least 80% of crash seeds and each ablation exhibits its targeted failure mode.
- Stop condition: Stop if the real broker-backed coordinator loses tasks, emits duplicate completions, or fails to recover in more than one of 30 fixed seeds after implementation bugs are corrected, or if broker setup prevents process-level fault injection.

## Evidence references

- Artifact root: `<local-path>/projects/broker-backed-volunteer-training-coordinator-crash-recover-0a26c7cce0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
