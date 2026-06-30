# Mixed-Precision CPU Training with Dynamic Gradient Checkpointing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `mixed-precision-cpu-training-with-dynamic-gradient-checkpointing-4870bff50e83`
Run ID: `mixed-precision-cpu-training-with-dynamic-gradient-checkpointing-4870bff50e83-20260609T210425353367+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/9e213a0d0d2c

## What looked useful

Dynamic checkpointing successfully adapted checkpoint stride and held saved-tensor bytes below a configured budget. The mechanism-level memory reduction did not translate into end-to-end RSS reduction on this small CPU workload, so saved-tensor accounting alone is insufficient evidence for a practical CPU-training advantage.

## Boundaries and scale limits

Synthetic residual MLP only; 8 measured optimizer steps per mode; CPU worker with Intel Xeon Silver 4114 class CPUs lacking explicit BF16 ISA support; no GPT-2-small-class transformer, long convergence run, or BF16-capable CPU validation.

## Claim scope

On a bounded PyTorch CPU residual-MLP training benchmark, bfloat16 autocast plus a dynamic checkpoint policy reduced autograd saved-tensor bytes versus fp32 no checkpoint, but did not reduce process RSS and was slower than bf16 without checkpointing.

## Why it stopped

Bounded local evidence is mixed: the mechanism works in autograd saved-tensor accounting, but practical memory and throughput claims are not supported by process RSS or bf16-only comparison.

## Recommended next action

Stop this run as no-paper useful signal; deepen only with a bounded transformer-like benchmark on a BF16-capable CPU requiring both RSS reduction and acceptable throughput overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BF16-capable CPU transformer benchmark for dynamic checkpoint budgets
- Success threshold: Dynamic bf16 checkpointing reduces process peak RSS by at least 20% versus bf16 no checkpoint and keeps median step-time overhead below 35%, with comparable short-run loss behavior.
- Stop condition: Stop as negative if dynamic checkpointing reduces saved tensors but not process RSS, or if RSS improves only with median step-time overhead of 35% or more.

## Evidence references

- Artifact root: `<local-path>/projects/mixed-precision-cpu-training-with-dynamic-gradient-checkpointing-4870bff50e83`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
