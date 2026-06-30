# LRQ-Adam: Low-Rank Quantized Optimizer States for Tiny-VRAM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lrq-adam-low-rank-quantized-optimizer-states-for-tiny-vram-training-04d372c4dfec`
Run ID: `lrq-adam-low-rank-quantized-optimizer-states-for-tiny-vram-training-04d372c4dfec-20260526T105711242332+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/31d6205bf9bc

## What looked useful

Pure LRQ-Adam failed because low-rank quantized second moments dropped variance directions and produced huge Adam denominators/errors even for exactly low-rank gradients. A 1% mean-variance floor prevented blow-up and reached Adam-like synthetic regression loss, but update cosine remained weak for full-rank gradients.

## Boundaries and scale limits

Tested only dim=32 smoke and dim=64 synthetic matrix traces/regression on one GB10 host; no real transformer, no multi-seed statistical study, no production optimizer kernel, and no end-to-end tiny-VRAM training measurement.

## Claim scope

Bounded CUDA/PyTorch synthetic matrix-optimizer tests show pure low-rank int8 Adam moments are unstable, while adding a scalar second-moment floor can stabilize short synthetic matrix regression with 7.8x to 30.1x optimizer-state compression.

## Why it stopped

Proxy/synthetic early falsification of pure LRQ-Adam, not a full validation of tiny-VRAM training; guarded LRQ produced useful but insufficient evidence for a paper.

## Recommended next action

Stop this run as no-paper evidence; next bounded action is to test a guarded or hybrid LRQ-AdamW second-moment design on a small transformer with measured optimizer-state memory and validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Guarded or hybrid LRQ-AdamW on a small transformer
- Success threshold: Across at least 3 seeds on a small transformer proxy, guarded or hybrid LRQ-AdamW stays finite, reaches validation loss within 5% of AdamW, reduces optimizer-state memory by at least 4x, and has no more than 25% step-time overhead.
- Stop condition: Stop if pure or guarded variants diverge/nonfinite in 2 of 3 seeds, validation loss is more than 10% worse than AdamW, measured optimizer-state memory reduction is below 2x, or step-time overhead exceeds 50%.

## Evidence references

- Artifact root: `<local-path>/projects/lrq-adam-low-rank-quantized-optimizer-states-for-tiny-vram-training-04d372c4dfec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
