# PyTorch multi-process checkpoint/replay test for volunteer-style SGD

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pytorch-multi-process-checkpoint-replay-test-for-volunteer-6aaa18b708`
Run ID: `pytorch-multi-process-checkpoint-replay-test-for-volunteer-6aaa18b708-20260613T053349900912+0000`

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

- Parent run decision: Volunteer Distributed Training: Checkpoint-Based Fault Tolerance: enoch://control-plane/projects/volunteer-distributed-training-checkpoint-based-fault-tolerance-b646310a3117/runs/volunteer-distributed-training-checkpoint-based-fault-tolerance-b646310a3117-20260613T051232636974+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/3aa1f9434937

## What looked useful

Exact replay reached zero parameter and loss delta versus uninterrupted training; missing optimizer momentum state diverged, and unsorted queue arrival caused small FP32 drift before deterministic aggregation was added.

## Boundaries and scale limits

Tested one seed, one small MLP, 18 steps, 4 possible volunteers, CPU-only local process spawning, synchronous gradient averaging, and one checkpoint boundary. Did not test realistic networked volunteers, stragglers, worker failures, GPU/distributed process groups, large models, real datasets, or repeated checkpoint chains.

## Claim scope

In a small CPU PyTorch synthetic regression test with spawned volunteer worker processes, checkpoint/replay exactly matched uninterrupted volunteer-style SGD when model, optimizer, step/RNG state, deterministic schedule, and deterministic gradient aggregation order were preserved.

## Why it stopped

Tier 1 direct test produced a useful mechanism signal but not publication-grade evidence.

## Recommended next action

Run a bounded deepen test with persistent workers, multiple checkpoint boundaries, and injected worker drop/timeout events before considering any paper-oriented validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persistent-worker checkpoint replay with volunteer dropout and multiple checkpoints
- Success threshold: For all seeds, replay final parameters match uninterrupted training exactly or within a predeclared <=1e-9 absolute tolerance, traces match expected worker availability, and broken controls diverge detectably.
- Stop condition: Stop if any deterministic replay run diverges after all checkpointed state and aggregation ordering are verified, or if the persistent-worker harness cannot complete within a bounded CPU budget.

## Evidence references

- Artifact root: `<local-path>/projects/pytorch-multi-process-checkpoint-replay-test-for-volunteer-6aaa18b708`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
