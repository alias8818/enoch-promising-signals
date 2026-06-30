# 4-bit Quantized Adam: VRAM Reduction via Aggressive Optimizer State Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-quantized-adam-vram-reduction-via-aggressive-optimizer-state-compression-c93d9103c8cc`
Run ID: `4-bit-quantized-adam-vram-reduction-via-aggressive-optimizer-state-compression-c93d9103c8cc-20260607T045512947633+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/8b1a34cc0646

## What looked useful

The memory-compression mechanism works directly on GPU tensors, but naive 4-bit quantization of both Adam moments is numerically fragile. Future work should protect or redesign the second-moment representation before scaling.

## Boundaries and scale limits

No LLM fine-tuning, real dataset training, distributed training, or production fused kernel was tested. Throughput is from an eager PyTorch prototype and should not be generalized beyond showing implementation overhead in this probe.

## Claim scope

CUDA-resident prototype evidence for a naive blockwise int4 AdamW state format on synthetic memory and teacher/student regression probes: optimizer-state bytes shrink by about 86-87%, but the optimizer diverges at practical AdamW learning rates and only remains finite at a very low learning rate with worse loss.

## Why it stopped

Bounded early falsification rather than full validation: the simple aggressive 4-bit state swap reduced memory but failed the small direct convergence probe across learning-rate and block-size checks.

## Recommended next action

Stop this project as no-paper useful-signal evidence; a new bounded test should add second-moment floors or log-domain variance quantization before any larger model run.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Stabilized 4-bit Adam via protected second-moment quantization
- Success threshold: No NaNs and final loss within 2x AdamW while preserving at least 70% optimizer-state byte reduction on CUDA.
- Stop condition: Stop if the stabilized variant still diverges at 0.0002 or if memory reduction drops below 70%.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-quantized-adam-vram-reduction-via-aggressive-optimizer-state-compression-c93d9103c8cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
