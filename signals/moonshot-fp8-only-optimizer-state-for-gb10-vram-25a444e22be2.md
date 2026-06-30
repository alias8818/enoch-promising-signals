# Moonshot: fp8-only optimizer state for gb10 VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `moonshot-fp8-only-optimizer-state-for-gb10-vram-25a444e22be2`
Run ID: `moonshot-fp8-only-optimizer-state-for-gb10-vram-25a444e22be2-20260608T125350490618+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/95fc63a70833

## What looked useful

Raw FP8 storage gives the expected VRAM reduction, but unscaled FP8 moment quantization zeros or coarsens Adam states, especially the second moment, producing update explosions or stateless behavior. The raw fp8-only optimizer-state idea is not viable as stated without scaling or another representation.

## Boundaries and scale limits

This was a bounded synthetic GPU mechanism test, not full neural-network training. It does not validate transformer loss curves, checkpoint/resume, distributed training, or final downstream quality.

## Claim scope

On a controlled GB10/PyTorch quadratic optimizer-state probe, raw FP8 Adam moment tensors reduce moment-state memory to 25% of FP32 but do not preserve Adam-like optimizer behavior across tested gradient scales.

## Why it stopped

Proxy early falsification: the direct optimizer-state mechanism failed on a controlled GPU objective because raw FP8 moments frequently underflowed or became too coarse; this is not a full model-training validation.

## Recommended next action

Stop pursuing unscaled raw FP8-only Adam m/v state as stated; run a bounded follow-up on scaled or block-scaled FP8 moment state if VRAM reduction remains the target.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Block-scaled FP8 Adam state on a small transformer
- Success threshold: Scaled FP8 state reaches within 5% of FP32 validation loss at the same step budget, avoids sustained v zero fractions above 1%, and uses less memory than FP16 optimizer state after including scale metadata.
- Stop condition: Stop if scaled FP8 v zero fraction remains above 10% after calibration or if loss diverges/degrades by more than 20% versus FP32 under two learning rates.

## Evidence references

- Artifact root: `<local-path>/projects/moonshot-fp8-only-optimizer-state-for-gb10-vram-25a444e22be2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
