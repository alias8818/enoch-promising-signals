# Quantization-aware gradient compression with error feedback for low-VRAM training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantization-aware-gradient-compression-with-error-feedback-for-low-vram-training-b5a7a2a589fa`
Run ID: `quantization-aware-gradient-compression-with-error-feedback-for-low-vram-training-b5a7a2a589fa-20260611T033742466424+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/49eaaab87def

## What looked useful

Residual-free int8 and int4 gradient quantization stayed within 1 percentage point of FP32 test accuracy with modeled gradient-buffer savings of 4.00x and 7.99x respectively. Error-feedback variants matched accuracy but achieved only 0.80x savings with FP32 residuals, 2.00x with int8 gradients plus int8 residuals, and 2.66x with int4 gradients plus int8 residuals, so error feedback was not the low-VRAM win in this probe.

## Boundaries and scale limits

CPU-only proxy with synthetic teacher data; no PyTorch/CUDA allocator measurements, no transformer workload, no activation-memory pressure, no optimizer-state-heavy baseline, and no long-run language-model validation.

## Claim scope

On a five-seed NumPy MLP synthetic classification probe, per-tensor int4/int8 gradient quantization preserved FP32-SGD accuracy, but error-feedback residual storage did not meet the predeclared low-VRAM memory-savings threshold when residual bytes were counted.

## Why it stopped

Bounded CPU-only proxy produced a useful early falsification of the error-feedback low-VRAM claim after residual memory was counted; it is not a full validation or full-scale falsification.

## Recommended next action

Stop this run as no-paper evidence; run a bounded PyTorch/CUDA follow-up comparing residual-free int4/int8 gradients against compressed-residual error feedback on a small transformer while measuring peak GPU memory and validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measure residual-free versus error-feedback gradient quantization on a small CUDA transformer
- Success threshold: A compressed error-feedback variant must improve validation loss by at least 1 percent relative to the matching no-EF quantized baseline while preserving at least 4x measured peak gradient/residual memory savings versus FP32 gradients and adding less than 10 percent wall-clock overhead.
- Stop condition: Stop if error-feedback variants fail the 4x measured memory-savings threshold or fail to improve validation loss versus matching no-EF quantization on the small transformer workload.

## Evidence references

- Artifact root: `<local-path>/projects/quantization-aware-gradient-compression-with-error-feedback-for-low-vram-training-b5a7a2a589fa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
