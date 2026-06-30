# AdamW and small-architecture validation for dynamic int16 gradient accumulation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `adamw-and-small-architecture-validation-for-dynamic-int16-558fcfd969`
Run ID: `adamw-and-small-architecture-validation-for-dynamic-int16-558fcfd969-20260605T205138273373+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Framework-level int16 gradient accumulation on a small real workload: enoch://control-plane/projects/framework-level-int16-gradient-accumulation-on-a-small-rea-c1d9e3732f/runs/framework-level-int16-gradient-accumulation-on-a-small-rea-c1d9e3732f-20260605T034453940411+0000
- Parent run decision: PyTorch-level int16 gradient accumulation on two small canonical workloads: enoch://control-plane/projects/pytorch-level-int16-gradient-accumulation-on-two-small-can-8da6eedc1d/runs/pytorch-level-int16-gradient-accumulation-on-two-small-can-8da6eedc1d-20260605T085413871695+0000

## What looked useful

Across 48 harder-task runs, dynamic int16 had minimum architecture-level validation accuracy delta of 0.0 vs FP32, maximum loss ratio of 1.001787 vs FP32, mean accumulation relative error from 1.99e-05 to 3.74e-05, and zero saturation. Static int16 showed consistently larger relative error and a small residual-MLP accuracy drop.

## Boundaries and scale limits

No GPU, fused optimizer kernel, transformer/GPT-2-small-class run, long-corpus training, or throughput/memory-bandwidth validation was performed. Results are bounded small-architecture mechanism evidence only.

## Claim scope

Dynamic per-tensor int16 gradient accumulation preserved AdamW training metrics relative to FP32 accumulation on four small NumPy CPU architectures: linear, 1-layer MLP, 2-layer MLP, and residual 3-layer MLP, across four fixed seeds on a synthetic multiclass task.

## Why it stopped

The mechanism is supported at small NumPy CPU scale, but the evidence is not transformer-scale or systems-level enough for publication readiness.

## Recommended next action

Stop this run as no-paper useful signal; if the controller allows one depth-4 bounded follow-up, test the same FP32/dynamic/static AdamW accumulation comparison on a tiny transformer or GPT-style character model with memory and throughput metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-transformer AdamW validation for dynamic int16 gradient accumulation
- Success threshold: Dynamic int16 must have worst-seed validation loss ratio <= 1.05 vs FP32, validation metric delta >= -0.02 where applicable, mean accumulation relative error <= 1e-3, zero or negligible saturation, and no throughput regression that erases the memory/storage rationale.
- Stop condition: Stop if dynamic int16 exceeds 1.05 validation loss ratio vs FP32, drops validation metric by more than 0.02, shows sustained saturation, or cannot run a transformer workload within the local bounded budget.

## Evidence references

- Artifact root: `<local-path>/projects/adamw-and-small-architecture-validation-for-dynamic-int16-558fcfd969`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
