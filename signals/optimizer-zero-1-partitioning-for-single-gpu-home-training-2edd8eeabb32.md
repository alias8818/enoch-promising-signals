# Optimizer ZeRO-1 Partitioning for Single GPU Home Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `optimizer-zero-1-partitioning-for-single-gpu-home-training-2edd8eeabb32`
Run ID: `optimizer-zero-1-partitioning-for-single-gpu-home-training-2edd8eeabb32-20260605T141506189422+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4368a712410f

## What looked useful

Single-GPU optimizer-state offload/partitioning is a viable memory-for-time tradeoff for home training when AdamW state is the binding GPU-memory limit, but the evidence is not paper-ready and does not show end-to-end training improvement.

## Boundaries and scale limits

Synthetic optimizer-step benchmark only; no transformer forward/backward graph, no activation memory, no real dataset, no convergence measurement, and no long-run training persistence. Classical distributed ZeRO-1 has no true rank partitioning benefit at single rank; this tests a local offload analogue.

## Claim scope

On one NVIDIA GB10 with synthetic FP32 parameter tensors up to 268,435,456 elements, a CPU-resident chunked AdamW state update reduced initialized CUDA allocation by 50% and measured optimizer-step peak CUDA allocation by 40% versus GPU-resident AdamW, while increasing median optimizer-step time by about 2.0-2.24x.

## Why it stopped

Evidence supports a scoped optimizer-memory mechanism but remains synthetic/proxy-only and therefore is insufficient for a paper or broad validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should integrate the same CPU-sharded optimizer into a GPT-2-small-class training loop and compare max feasible batch/model size plus tokens/sec at matched loss trajectory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2-small single-GPU optimizer-state offload benchmark
- Success threshold: CPU-sharded optimizer fits at least one practically larger batch/model configuration than GPU AdamW under the same CUDA memory ceiling, while maintaining matched loss trend and no worse than 25% end-to-end tokens/sec loss for a memory-unlocked configuration or clearly documenting the tradeoff if slower.
- Stop condition: Stop if the real training loop cannot fit a larger batch/model than GPU AdamW, diverges under matched hyperparameters, or loses more than 50% end-to-end tokens/sec without unlocking a meaningful memory-bound configuration.

## Evidence references

- Artifact root: `<local-path>/projects/optimizer-zero-1-partitioning-for-single-gpu-home-training-2edd8eeabb32`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
