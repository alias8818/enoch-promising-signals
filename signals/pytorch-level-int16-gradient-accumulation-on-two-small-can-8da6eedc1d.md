# PyTorch-level int16 gradient accumulation on two small canonical workloads

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pytorch-level-int16-gradient-accumulation-on-two-small-can-8da6eedc1d`
Run ID: `pytorch-level-int16-gradient-accumulation-on-two-small-can-8da6eedc1d-20260605T085413871695+0000`

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

- Parent run decision: Framework-level int16 gradient accumulation on a small real workload: enoch://control-plane/projects/framework-level-int16-gradient-accumulation-on-a-small-rea-c1d9e3732f/runs/framework-level-int16-gradient-accumulation-on-a-small-rea-c1d9e3732f-20260605T034453940411+0000
- Parent run decision: Int16 gradient accumulation for micro-batches: enoch://control-plane/projects/int16-gradient-accumulation-for-micro-batches-fe025cfd5226/runs/int16-gradient-accumulation-for-micro-batches-fe025cfd5226-20260604T225620907497+0000

## What looked useful

Dynamic int16 accumulation achieved mean gradient relative L2 of 4.3e-5 on MNIST and 5.4e-5 on Fashion-MNIST, with final accuracy deltas of +2.38 pp and -0.20 pp versus FP32. Stale-scale int16 and int8 controls had much larger gradient errors, supporting the dynamic scaling mechanism even though final accuracy on these small tasks was tolerant.

## Boundaries and scale limits

CPU PyTorch-level emulation only; no fused kernels, no measured production memory-bandwidth benefit, no GPU throughput result, no Adam/AdamW optimizer-state test, no mixed-precision stack, no CNN/transformer architecture, no full-dataset long training, and no large-model validation.

## Claim scope

On two small canonical PyTorch image-classification workloads (MNIST MLP and Fashion-MNIST MLP), 3 fixed seeds, SGD, 4-step microbatch accumulation, and short CPU training, a dynamic per-parameter int16 quantized gradient accumulator closely matched FP32 accumulated updates and did not degrade final evaluation accuracy.

## Why it stopped

Medium local evidence supports the mechanism, but it is not paper-positive because the validation is limited to short CPU PyTorch-level MLP/SGD runs and does not demonstrate real memory, speed, optimizer, or architecture robustness.

## Recommended next action

Stop as no-paper useful signal; if continued, run a bounded deepen test on AdamW plus a small CNN or transformer-class workload with measured peak gradient-storage memory and the same paired update-fidelity diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: AdamW and small-architecture validation for dynamic int16 gradient accumulation
- Success threshold: Dynamic int16 stays within 0.5 percentage points accuracy or equivalent validation metric of FP32, has mean update relative L2 below 1e-3, and shows a measured gradient-accumulator storage reduction close to 2x versus FP32 for the accumulator component.
- Stop condition: Stop if dynamic int16 loses more than 1.0 percentage point versus FP32 on two or more seeds, mean update relative L2 exceeds 1e-2, or measured accumulator storage reduction is not observable in the implementation.

## Evidence references

- Artifact root: `<local-path>/projects/pytorch-level-int16-gradient-accumulation-on-two-small-can-8da6eedc1d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
