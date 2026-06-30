# Block-wise Dynamic 8-bit Adam with Per-block Rescaling

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `block-wise-dynamic-8-bit-adam-with-per-block-rescaling-d0a9ae0b86d3`
Run ID: `block-wise-dynamic-8-bit-adam-with-per-block-rescaling-d0a9ae0b86d3-20260531T111743689121+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/adfffe8b5db1

## What looked useful

The simple per-block dynamic 8-bit moment design is memory-efficient but unstable: AdamW reached 0.000281 MLP loss while Block8Adam diverged to 4.8032e11 at block size 1024, and block sizes 256 and 64 also diverged. Gradient replay showed nontrivial update distortion, including 5.04x max relative update error at block size 1024 and 1.53x even at block size 64.

## Boundaries and scale limits

Bounded local synthetic tests only: 240 optimizer steps, small linear and MLP models, one NVIDIA GB10, no fused kernels, no real language-model pretraining, and no distributed or long-horizon validation.

## Claim scope

Naive GPU-resident Block8Adam that stores Adam first moments as signed int8 and second moments as uint8 with dynamic per-block FP32 scales was tested on synthetic linear regression, synthetic MLP classification, and controlled gradient replay. It reduced optimizer-state bytes by about 3.7x-4.0x but did not preserve AdamW optimization behavior.

## Why it stopped

Bounded direct evidence falsified the optimizer-behavior part of the hypothesis: despite about 4x state compression, the matched MLP benchmark diverged while AdamW converged, and smaller blocks or lower learning rates did not rescue the result.

## Recommended next action

Stop this naive design as a no-paper negative; only revisit with a bounded stabilized variant that specifically protects the second-moment denominator from blockwise quantization-to-zero error.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Stabilized 8-bit Adam second moments with denominator floors or log-domain v
- Success threshold: MLP final loss within 2x AdamW after 240 steps, linear regression final loss within 1.15x AdamW, shock-window mean relative update error below 0.05, and optimizer-state bytes at least 3x smaller than AdamW.
- Stop condition: Stop if the stabilized variant still diverges or exceeds 2x AdamW MLP final loss under matched initialization for two block sizes.

## Evidence references

- Artifact root: `<local-path>/projects/block-wise-dynamic-8-bit-adam-with-per-block-rescaling-d0a9ae0b86d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
