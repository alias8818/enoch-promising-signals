# 8-bit AdamW: blockwise vs per-tensor optimizer state quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `8-bit-adamw-blockwise-vs-per-tensor-optimizer-state-quantization-22848bf99cf4`
Run ID: `8-bit-adamw-blockwise-vs-per-tensor-optimizer-state-quantization-22848bf99cf4-20260628T131251349883+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dc6d1b4c93e6

## What looked useful

Per-tensor int8 AdamW state diverged in 0/15 medium training runs across lr=0.002, 0.001, and 0.0005 with 256-value blocks used for the blockwise comparator. Blockwise int8 state was stable in 2/5, 4/5, and 4/5 of those matched settings, and 5/5 stable with 64-value blocks at lr=0.0005. Stress tests showed per-tensor relative L2 reconstruction error was 5.74x to 17.15x higher than 256-block scaling and 9.17x to 30.42x higher than 64-block scaling under lognormal state scale dispersion sigma 1 to 3.

## Boundaries and scale limits

Evidence is limited to synthetic state tensors and a small synthetic MLP training proxy on one GB10 host. It does not validate language modeling, GPT-2-small-class training, production fused optimizer throughput, or end-to-end memory savings at larger model scale.

## Claim scope

In a local PyTorch CUDA proxy, blockwise int8 AdamW state quantization reduces optimizer-state reconstruction error versus per-tensor scaling and is substantially more stable on a 1000-step synthetic classification MLP; 64-value blocks were stable across 5/5 seeds at lr=5e-4 while per-tensor quantization diverged across all tested medium settings.

## Why it stopped

This run produced useful proxy evidence but not direct publication-grade language-model training or production optimizer evidence.

## Recommended next action

Run a bounded tiny-transformer language-modeling confirmation with fp32 AdamW, per-tensor int8 state, 256-block int8 state, and 64-block int8 state, measuring validation loss, state reconstruction error, actual optimizer memory, and throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-transformer confirmation of blockwise int8 AdamW state quantization
- Success threshold: Blockwise int8 state completes all seeds without NaNs, validation loss stays within 2 percent of fp32 AdamW, and per-tensor either diverges or has materially worse validation loss or reconstruction error under the same optimizer-state memory budget.
- Stop condition: Stop if blockwise and per-tensor both match fp32 within 2 percent across all seeds, or if blockwise diverges in two or more seeds at conservative learning rates.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-blockwise-vs-per-tensor-optimizer-state-quantization-22848bf99cf4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
