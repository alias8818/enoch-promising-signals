# 8-bit Lion vs 8-bit AdamW on 125M instruction tuning under 4GB VRAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `8-bit-lion-vs-8-bit-adamw-on-125m-instruction-tuning-under-4gb-vram-09d1a53812af`
Run ID: `8-bit-lion-vs-8-bit-adamw-on-125m-instruction-tuning-under-4gb-vram-09d1a53812af-20260621T011054648526+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b61001e528d9

## What looked useful

125M state accounting showed 8-bit Lion saves 119.33 MiB of optimizer state versus 8-bit AdamW. In the calibrated 3-seed proxy, best-LR Lion reached validation loss 1.3779 and accuracy 0.5137 versus AdamW loss 2.2473 and accuracy 0.3278.

## Boundaries and scale limits

No CUDA GPU was exposed and nvidia-smi was unavailable, so this does not validate real 125M transformer instruction tuning, bitsandbytes kernels, activation memory, CUDA allocator overhead, throughput, or quality under an enforced 4GB VRAM cap.

## Claim scope

For a dependency-light NumPy proxy with blockwise uint8 optimizer states, 8-bit Lion used one uint8 state instead of AdamW's two states at 125M parameters and outperformed swept 8-bit AdamW on a small synthetic supervised optimizer-dynamics task.

## Why it stopped

Stopped at no-paper useful signal because this worker lacked an exposed NVIDIA/CUDA path; the result is memory accounting plus proxy optimizer dynamics, not full instruction-tuning validation.

## Recommended next action

Run a bounded direct CUDA follow-up on a host with a real 4GB VRAM cap using the same 125M transformer, instruction data, checkpoint cadence, and LR sweeps for 8-bit Lion and 8-bit AdamW.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct 4GB VRAM 125M instruction-tuning comparison for 8-bit Lion vs 8-bit AdamW
- Success threshold: Lion must complete the same run under 4GB VRAM and achieve validation loss no worse than 1 percent above tuned 8-bit AdamW while saving measurable optimizer-state/peak VRAM or enabling a larger batch/sequence configuration.
- Stop condition: Stop if either optimizer cannot complete a smoke epoch under 4GB VRAM after ordinary batch, accumulation, and checkpointing adjustments, or if Lion is more than 1 percent worse in validation loss at matched compute.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-lion-vs-8-bit-adamw-on-125m-instruction-tuning-under-4gb-vram-09d1a53812af`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
