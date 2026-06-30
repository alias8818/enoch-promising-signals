# CPU-Paged 8-bit Optimizer for Tiny VRAM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-paged-8-bit-optimizer-for-tiny-vram-training-e7e6408dd96d`
Run ID: `cpu-paged-8-bit-optimizer-for-tiny-vram-training-e7e6408dd96d-20260529T204630742718+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b28e4609765d

## What looked useful

CPU paging optimizer state is mechanically plausible, but naive absmax blockwise int8 quantization of both Adam moments is numerically unsafe because second-moment under-quantization causes extreme updates. Future work should first fix the second-moment representation before spending compute on real-model tiny-VRAM training.

## Boundaries and scale limits

This was not full neural network training and did not enforce a hard VRAM cap. It tested optimizer-state mechanics and numerical behavior only; production 8-bit optimizers with non-linear maps, clipping, fused kernels, or error compensation were not evaluated.

## Claim scope

On a CUDA bfloat16 quadratic optimizer proxy with 1M, 4M, and 16M parameters, CPU paging of fp32 Adam states preserved baseline loss while reducing CUDA allocation, but a naive CPU-paged blockwise int8 Adam moment implementation diverged within 10 steps despite using about 25% of fp32 state bytes.

## Why it stopped

Early proxy falsification: the tested CPU-paged blockwise int8 Adam states diverged at all tested sizes, while CPU-paged fp32 Adam matched the baseline, isolating the failure to naive 8-bit moment quantization rather than paging.

## Recommended next action

Stop this naive design; test a bounded hybrid or non-linear second-moment quantizer against the same proxy before attempting real-model training.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid second-moment CPU-paged optimizer stability test
- Success threshold: Pass all required evidence items, with no NaN/Inf losses and no loss-ratio explosion on the proxy or real-model smoke test.
- Stop condition: Stop if the hybrid/non-linear second-moment variant diverges on the quadratic proxy at 4M parameters or exceeds 10x gpu_adam32 mean step time at 16M parameters.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-paged-8-bit-optimizer-for-tiny-vram-training-e7e6408dd96d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
