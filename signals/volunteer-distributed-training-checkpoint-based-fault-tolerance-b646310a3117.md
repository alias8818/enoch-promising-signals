# Volunteer Distributed Training: Checkpoint-Based Fault Tolerance

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `volunteer-distributed-training-checkpoint-based-fault-tolerance-b646310a3117`
Run ID: `volunteer-distributed-training-checkpoint-based-fault-tolerance-b646310a3117-20260613T051232636974+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/3aa1f9434937

## What looked useful

At coordinator crash probability 0.01, no persistent checkpointing averaged 85.9065x attempted work, while checkpoint intervals of 100, 25, and 5 updates averaged 1.8426x, 1.1811x, and 1.0528x respectively; all completed trials had zero loss delta versus the no-failure deterministic reference.

## Boundaries and scale limits

Synthetic linear regression only; 600 committed updates; 12 seeds per crash-rate/policy cell; single-process CPU simulation; no real volunteer nodes, network churn, large model optimizer state, checkpoint bandwidth, scheduler state, adversarial behavior, or multi-node framework integration.

## Claim scope

Local deterministic simulation of volunteer-style SGD with worker pre-gradient failures and coordinator crashes shows that stateful checkpoints preserving model, committed step, and data RNG state reproduce the no-failure training trajectory and sharply reduce rollback work versus no persistent checkpointing.

## Why it stopped

The result is a reproducible local proxy with useful mechanism evidence, but not full validation of volunteer distributed training and not paper-ready.

## Recommended next action

Run a bounded real PyTorch multi-process fault-injection follow-up that persists model, optimizer, sampler/RNG, scheduler, and in-flight task ledger, then kill and restart workers/coordinator to test exact resumed-step equivalence and overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch multi-process checkpoint/replay test for volunteer-style SGD
- Success threshold: Checkpointed policy completes at least 95% of runs, matches no-failure final loss within deterministic tolerance or documents only intentional replay differences, and stays below 1.25x attempted work at the selected crash rate while no-persistent-checkpoint is materially worse.
- Stop condition: Stop if persisted state cannot reproduce deterministic resumed training after two implementation attempts, or if checkpoint I/O overhead alone exceeds the 1.25x work threshold on the small harness.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-distributed-training-checkpoint-based-fault-tolerance-b646310a3117`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
