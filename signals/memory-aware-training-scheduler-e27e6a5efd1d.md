# Memory-Aware Training Scheduler

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `memory-aware-training-scheduler-e27e6a5efd1d`
Run ID: `memory-aware-training-scheduler-e27e6a5efd1d-20260614T103030496697+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/49180dbfc469

## What looked useful

Measured toy transformer steps rose from 168 MB at sequence length 64 to 359 MB at 512. In a 24-seed scheduler simulation, memory-aware best-fit improved overall mean tokens/s by 2.60% and memory utilization by 2.09 percentage points versus FIFO, with +6.49% and +5.58% gains at two budgets but -3.98% at the middle budget. Fairness worsened: starvation ratio increased from 1.12 to 5.86.

## Boundaries and scale limits

Toy transformer only; synthetic arrivals/durations; no real concurrent PyTorch process admission, allocator-fragmentation stress, GPT-2-small-class baseline, multi-GPU, multi-node, or production trace replay.

## Claim scope

On a GB10 worker, a toy-transformer-measured discrete-event scheduler simulation showed that greedy memory-aware admission can improve accelerator-memory packing and throughput under some heterogeneous sequence-length workloads, but the effect is budget-dependent and fairness-regressive.

## Why it stopped

Bounded local evidence is mixed and proxy-based: it supports the packing mechanism but also reveals budget sensitivity and fairness regression, so it is not publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement a real-process PyTorch admission controller with an aging/fairness term and replay the same memory-budget scenarios.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fairness-Aware Real-Process Memory Admission for PyTorch Training Jobs
- Success threshold: Fairness-aware memory admission improves tokens/s by at least 3% over FIFO at two of three budgets, has zero OOMs, and keeps starvation ratio below 1.5 while retaining at least 80% of greedy best-fit's utilization lift.
- Stop condition: Stop if real-process overhead or fairness constraints erase throughput gains below 1% at all budgets, or if zero-OOM admission cannot be maintained without serializing to FIFO-equivalent behavior.

## Evidence references

- Artifact root: `<local-path>/projects/memory-aware-training-scheduler-e27e6a5efd1d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
