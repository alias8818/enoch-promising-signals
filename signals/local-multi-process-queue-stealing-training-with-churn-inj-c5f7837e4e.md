# Local Multi-Process Queue-Stealing Training with Churn Injection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `local-multi-process-queue-stealing-training-with-churn-inj-c5f7837e4e`
Run ID: `local-multi-process-queue-stealing-training-with-churn-inj-c5f7837e4e-20260608T083612493593+0000`

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

- Parent run decision: Volunteer Grid Distributed Training with Queue-Based Work Stealing: enoch://control-plane/projects/volunteer-grid-distributed-training-with-queue-based-work-stealing-3556365f233e/runs/volunteer-grid-distributed-training-with-queue-based-work-stealing-3556365f233e-20260608T034343430250+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/19c7a26103ad

## What looked useful

Barriered controlled churn trials completed all tasks and showed stealing median makespan 1.1155 s versus static 3.3332 s, a 66.53% improvement; a matched no-churn control showed only 0.91% median improvement, tying the effect to churn tolerance.

## Boundaries and scale limits

Single host, single GPU, small synthetic MLP tasks, local optimizer/model copies, finite queues, pause-only churn, no real dataset, no DDP gradient synchronization, no crash/restart recovery, no checkpoint/replay correctness, no multi-node or large-model validation.

## Claim scope

In a controlled small local GB10 test with four CUDA PyTorch training worker processes, finite synthetic microbatch queues, skewed task assignment, and deterministic pause churn on one worker, peer queue stealing completed all tasks and reduced median makespan versus static per-worker queues.

## Why it stopped

The controlled small direct test supports the local scheduling mechanism, but evidence remains synthetic and small-scale and does not validate correctness or convergence in a real distributed training stack.

## Recommended next action

Stop this Tier 1 run as useful no-paper evidence; next run should test the same queue-stealing mechanism in a medium DDP/checkpoint-aware training harness with pause and crash/restart churn.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: DDP Checkpoint-Aware Queue Stealing Under Pause and Restart Churn
- Success threshold: Stealing completes all committed microbatches with no unrecovered duplicates/drops, improves median step throughput or makespan by at least 20% versus static queues under churn, and keeps final loss within 2% of the matched static/no-churn control.
- Stop condition: Stop as negative if stealing loses committed tasks, duplicates unreplayed tasks, fails to improve median throughput by 20%, or causes final loss drift greater than 2% in the matched medium DDP-style test.

## Evidence references

- Artifact root: `<local-path>/projects/local-multi-process-queue-stealing-training-with-churn-inj-c5f7837e4e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
