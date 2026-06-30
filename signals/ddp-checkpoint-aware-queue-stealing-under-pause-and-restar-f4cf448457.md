# DDP Checkpoint-Aware Queue Stealing Under Pause and Restart Churn

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ddp-checkpoint-aware-queue-stealing-under-pause-and-restar-f4cf448457`
Run ID: `ddp-checkpoint-aware-queue-stealing-under-pause-and-restar-f4cf448457-20260608T123510907482+0000`

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

- Parent run decision: Local Multi-Process Queue-Stealing Training with Churn Injection: enoch://control-plane/projects/local-multi-process-queue-stealing-training-with-churn-inj-c5f7837e4e/runs/local-multi-process-queue-stealing-training-with-churn-inj-c5f7837e4e-20260608T083612493593+0000
- Parent run decision: Volunteer Grid Distributed Training with Queue-Based Work Stealing: enoch://control-plane/projects/volunteer-grid-distributed-training-with-queue-based-work-stealing-3556365f233e/runs/volunteer-grid-distributed-training-with-queue-based-work-stealing-3556365f233e-20260608T034343430250+0000

## What looked useful

Naive stealing captured most of the makespan benefit versus static ownership. Checkpoint-aware stealing improved makespan by only 0.74% to 3.14% versus naive stealing, below the 10% success threshold in all scenarios, while reducing waste ratio by 97.46% to 99.07%. Lease fencing mattered: pause flushing without fencing introduced restart conflicts and made wall-clock performance worse than naive stealing.

## Boundaries and scale limits

Simulation-only evidence; no actual torch.distributed process group, optimizer state, checkpoint I/O, NCCL/Gloo collective behavior, or multi-node preemption was executed. The Tier 2 sweep used 3 churn scenarios, 5 policies, and 40 fixed seeds per scenario.

## Claim scope

In a deterministic 8-worker DDP-style queue/checkpoint simulator with fixed pause/restart churn traces, checkpoint-aware stealing nearly eliminates volatile checkpoint-loss waste but does not produce a material wall-clock improvement over a real naive queue-stealing baseline.

## Why it stopped

Tier 2 fixed-seed simulator evidence failed the stated wall-clock success threshold versus the real naive stealing baseline; this is a no-paper useful signal, not a full systems validation.

## Recommended next action

Stop paper pursuit for the simulator-level claim; run one bounded PyTorch DDP pause/restart harness only if direct framework evidence is needed to test whether real checkpoint I/O makes waste reduction translate into wall-clock benefit.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch DDP pause/restart harness for checkpoint-aware stealing
- Success threshold: Checkpoint-aware stealing must improve mean wall-clock completion by at least 10% versus naive queue stealing in at least one checkpoint-I/O-heavy churn setting and must not increase duplicate work or sample coverage errors.
- Stop condition: Stop if checkpoint-aware stealing remains below 10% wall-clock improvement versus naive stealing in all tested DDP settings, or if lease/fencing overhead or correctness failures offset the waste reduction.

## Evidence references

- Artifact root: `<local-path>/projects/ddp-checkpoint-aware-queue-stealing-under-pause-and-restar-f4cf448457`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
