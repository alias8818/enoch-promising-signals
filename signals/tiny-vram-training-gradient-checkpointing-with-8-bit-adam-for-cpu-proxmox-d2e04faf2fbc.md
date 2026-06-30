# Tiny-VRAM Training: Gradient Checkpointing with 8-bit Adam for CPU Proxmox

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-vram-training-gradient-checkpointing-with-8-bit-adam-for-cpu-proxmox-d2e04faf2fbc`
Run ID: `tiny-vram-training-gradient-checkpointing-with-8-bit-adam-for-cpu-proxmox-d2e04faf2fbc-20260614T080141983311+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/498077bb1909

## What looked useful

Checkpointing reduced peak RSS by 47.33 MB (7.65%) versus standard Adam. The local Adam8 state reduced persistent optimizer-state bytes by 63.23 MB (74.95%) but was slower. Combined checkpointing plus Adam8 reduced peak RSS by 96.55 MB (15.60%) with finite losses.

## Boundaries and scale limits

CPU-only proxy; no CUDA VRAM allocator measurements, no bitsandbytes/fused optimizer, no long-horizon convergence, no large model, and no full corpus training.

## Claim scope

On a CPU Proxmox-like worker, a 10.5M-parameter PyTorch Transformer training proxy showed that activation checkpointing and blockwise 8-bit persistent Adam-state compression reduce memory footprint, with the combined cell reducing isolated peak RSS by 15.60% versus standard Adam while keeping finite losses over 4 steps.

## Why it stopped

CPU proxy supports the memory mechanism but is not direct tiny-VRAM validation and is not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a direct small-CUDA replication using CUDA peak memory counters and a production 8-bit Adam implementation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-CUDA validation of checkpointing plus 8-bit Adam for tiny-VRAM training
- Success threshold: Combined checkpointing plus 8-bit Adam reduces peak CUDA allocated memory by at least 20% versus standard Adam and enables at least one larger batch or sequence setting that standard Adam cannot fit, while maintaining finite loss over the bounded run.
- Stop condition: Stop if CUDA peak memory reduction is below 10%, if the method cannot run without optimizer/runtime failures, or if loss becomes non-finite under the matched bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-vram-training-gradient-checkpointing-with-8-bit-adam-for-cpu-proxmox-d2e04faf2fbc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
