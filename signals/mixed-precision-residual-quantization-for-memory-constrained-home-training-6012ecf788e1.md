# Mixed-precision residual quantization for memory-constrained home training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `mixed-precision-residual-quantization-for-memory-constrained-home-training-6012ecf788e1`
Run ID: `mixed-precision-residual-quantization-for-memory-constrained-home-training-6012ecf788e1-20260614T123531922531+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/dba0ebcc1722

## What looked useful

Residual quantization lowered aggregate optimizer-state reconstruction error and saved 56-75% logical optimizer-state memory, but all compressed Adam variants suffered NaN/exploded loss or at least 45.5 percentage points lower validation accuracy than fp32 Adam over 3 seeds.

## Boundaries and scale limits

Synthetic teacher-generated MLP classification only; no transformer, real corpus, CUDA kernel, activation memory, checkpointing/offload, or long home-training run was tested.

## Claim scope

Bounded NumPy MLP proxy: naive per-tensor int8/residual-int8+int4 compression of Adam moments, including simple mixed policies with fp16 second moments or fp16 output-head moments, reduces logical optimizer-state memory but does not preserve stable convergence.

## Why it stopped

Early proxy falsification: the tested mixed/residual quantized Adam-state policies met memory-reduction goals but failed finite-loss/convergence criteria on a small direct optimizer-state training probe.

## Recommended next action

Stop this naive scheme; a bounded adjacent test should add optimizer-specific stabilizers such as block-wise scales and variance floors before any transformer-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Block-wise stabilized residual-quantized Adam moments
- Success threshold: At least one stabilized compressed policy achieves finite loss, >=50% optimizer-state memory reduction, and mean validation accuracy within 3 percentage points of fp32 Adam over 3 seeds.
- Stop condition: Stop if stabilized policies still produce NaN/exploded loss or more than 3 percentage points validation-accuracy loss after the bounded 3-seed MLP run.

## Evidence references

- Artifact root: `<local-path>/projects/mixed-precision-residual-quantization-for-memory-constrained-home-training-6012ecf788e1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
