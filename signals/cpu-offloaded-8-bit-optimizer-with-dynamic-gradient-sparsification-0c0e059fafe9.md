# CPU-Offloaded 8-bit Optimizer with Dynamic Gradient Sparsification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offloaded-8-bit-optimizer-with-dynamic-gradient-sparsification-0c0e059fafe9`
Run ID: `cpu-offloaded-8-bit-optimizer-with-dynamic-gradient-sparsification-0c0e059fafe9-20260601T031502025962+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/fc10a27ae0c3

## What looked useful

At 10% sparse density and 320 steps, q8 sparse Adam reached mean loss 0.508207 and accuracy 0.966634 versus FP32 Adam loss 0.497848 and accuracy 0.977295, while using 25.05% of FP32 optimizer-state bytes and an estimated 0.270x FP32 update traffic. In a 262144-parameter update microbenchmark, 10% sparse q8 averaged 4.567 ms/update versus FP32 Adam 5.046 ms/update and dense q8 21.051 ms/update. Small-vector training-loop optimizer time was still slower than FP32, and the naive dense q8 implementation was unstable.

## Boundaries and scale limits

No real GPU offload path, no transformer training, no PCIe/NVLink transfer measurement, no overlap measurement, and dense 8-bit baseline is a simple signed blockwise proxy that diverged on the toy task.

## Claim scope

CPU-only NumPy proxy for optimizer mechanics: synthetic logistic-regression convergence across three seeds and isolated large-vector update timing for FP32 Adam, naive dense signed blockwise 8-bit Adam, and dynamic sparse signed blockwise 8-bit Adam.

## Why it stopped

Closed as no-paper useful signal: current evidence is synthetic/proxy-only and mixed, not a direct full validation of CPU-offloaded 8-bit optimizer training.

## Recommended next action

Run a bounded end-to-end PyTorch CPU-offload prototype on a small transformer task with a production-grade unsigned/blockwise 8-bit optimizer, measuring validation loss, tokens/s, transfer bytes, and optimizer memory against FP32 Adam and dense q8 CPU-offload controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-transformer CPU-offloaded sparse 8-bit Adam prototype
- Success threshold: At 10% or 25% sparsity, validation loss within 2% of dense q8 or FP32 Adam, measured host-device optimizer transfer bytes reduced by at least 30%, optimizer-state memory reduced by at least 60%, and wall-clock throughput no worse than 10% below dense q8 CPU-offload.
- Stop condition: Stop if a stable dense q8 baseline cannot be established, or if sparse q8 misses the validation-loss threshold by more than 5% at all tested densities, or if measured transfer savings fail to improve end-to-end throughput on the small-transformer task.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-8-bit-optimizer-with-dynamic-gradient-sparsification-0c0e059fafe9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
