# Queue-backed volunteer training coordinator fault-injection prototype

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-backed-volunteer-training-coordinator-fault-injectio-c2ed9e7633`
Run ID: `queue-backed-volunteer-training-coordinator-fault-injectio-c2ed9e7633-20260610T202149092806+0000`

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
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7021e6dc2932

## What looked useful

The direct small test supports the mechanism that durable queue state plus lease expiry and idempotent completion prevents volunteer training task loss under worker crashes. Primary run: durable queue 1.000 min/mean completion with 0 lost tasks and recovery in 12/12 crash-injected runs; naive control 0.911 mean completion and 32.0 mean lost tasks. No-duplicate ablation preserved the effect.

## Boundaries and scale limits

Synthetic single-process simulation; no real broker, multi-host concurrency, production volunteer data, network partitions, clock skew, operator workflow, privacy controls, or long-running service behavior tested.

## Claim scope

In a local deterministic Tier 1 prototype with 120 volunteers, 3 training modules per volunteer, 8 simulated workers, 12 seeds, injected claim-before-completion crashes, transient failures, and duplicate enqueue attempts, a SQLite-backed durable queue with leases, retries, and idempotent completion completed all unique training tasks in every run while a naive in-memory dispatcher lost tasks.

## Why it stopped

Tier 1 direct mechanism test passed, but evidence remains synthetic and single-process, so this is useful no-paper evidence rather than paper-positive validation.

## Recommended next action

Run a bounded multi-process or real-broker deepen test that measures zero task loss, duplicate completion suppression, and recovery latency under crash/restart and broker disruption faults.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Broker-backed volunteer training coordinator crash-recovery test
- Success threshold: Queue-backed coordinator completes 100% of unique tasks with zero duplicate logical completions across at least 20 seeded runs and p95 recovery latency below 5 lease intervals, while the non-durable baseline loses tasks or duplicates completions under the same faults.
- Stop condition: Stop if the durable coordinator loses any unique task, records any duplicate logical completion, cannot recover after restart/broker pause in a bounded run, or if the test requires infrastructure outside a local CPU worker without producing additional mechanism evidence.

## Evidence references

- Artifact root: `<local-path>/projects/queue-backed-volunteer-training-coordinator-fault-injectio-c2ed9e7633`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
