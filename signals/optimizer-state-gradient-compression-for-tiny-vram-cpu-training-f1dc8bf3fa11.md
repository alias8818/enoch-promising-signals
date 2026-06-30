# Optimizer State Gradient Compression for Tiny-VRAM CPU Training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `optimizer-state-gradient-compression-for-tiny-vram-cpu-training-f1dc8bf3fa11`
Run ID: `optimizer-state-gradient-compression-for-tiny-vram-cpu-training-f1dc8bf3fa11-20260619T122902038993+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7da1fd2a2c28

## What looked useful

The tested scheme achieved the expected memory reductions: optimizer-state bytes fell to about 25.0% of fp32, total persistent trainable bytes fell to 62.5% with int8 state only and 43.8% with int8 state plus int8 gradients. Convergence failed: default LR accuracy dropped from 0.5371 to 0.0674 with int8 state, and int8 gradients produced non-finite loss. Lowering LR to 0.0005 reproduced the failure.

## Boundaries and scale limits

Evidence is limited to a deterministic NumPy MLP teacher-student classification proxy with 180-step runs. It does not validate GPU tiny-VRAM execution, transformer-scale training, offload bandwidth, activation pressure, or more sophisticated 8-bit optimizer designs.

## Claim scope

Naive whole-tensor symmetric int8 requantization of Adam optimizer moments, with optional int8 gradient buffers, is not a viable drop-in compression method on the bounded CPU MLP proxy tested here.

## Why it stopped

Proxy early falsification: memory savings were real, but the naive optimizer-state and gradient compression mechanism did not preserve convergence in two bounded confirmation runs.

## Recommended next action

Stop this run as a reproducible proxy early falsification; any next bounded test should replace whole-tensor quantization with blockwise/nonnegative second-moment handling and error feedback before scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blockwise Int8 Adam State With Error-Feedback Gradient Buffers
- Success threshold: Blockwise/error-feedback variant reaches final validation accuracy within 0.05 absolute of fp32 Adam while keeping optimizer-state bytes at or below 35% of fp32.
- Stop condition: Stop if the improved variant produces non-finite loss or remains more than 0.10 absolute validation accuracy below fp32 Adam after the same 180-step budget at two learning rates.

## Evidence references

- Artifact root: `<local-path>/projects/optimizer-state-gradient-compression-for-tiny-vram-cpu-training-f1dc8bf3fa11`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
