# 8-bit AdamW with Error Feedback for Tiny-VRAM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adamw-with-error-feedback-for-tiny-vram-training-fbd213f69bae`
Run ID: `8-bit-adamw-with-error-feedback-for-tiny-vram-training-fbd213f69bae-20260628T145421952394+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/979f67b8f044

## What looked useful

Plain blockwise 8-bit AdamW used 25.4% of AdamW optimizer-state memory with mean final-loss ratio 1.2984. Adding full fp16 error feedback improved mean final-loss ratio only to 1.2701 while raising state memory to 75.4% of AdamW and tripling memory versus plain 8-bit. Naive uint8 second-moment quantization also needs a positive-code floor to avoid zero-denominator update explosions.

## Boundaries and scale limits

This is not a neural language-model training validation, not a GPT-2-small-class run, not an OOM boundary test, and not a fused-kernel runtime benchmark. It tests optimizer-state mechanics and memory accounting only.

## Claim scope

On a CUDA ill-conditioned quadratic optimizer-state mechanism probe with 4,194,304 fp32 parameters and three seeds, full fp16 residual error feedback for both 8-bit AdamW moments slightly reduces the convergence gap versus plain 8-bit AdamW but loses most of the optimizer-state memory advantage.

## Why it stopped

Bounded proxy evidence shows full fp16 residual error feedback has an unfavorable convergence-per-memory tradeoff for tiny-VRAM use; this is an early proxy falsification, not full-scale neural training validation.

## Recommended next action

Stop this full-residual EF variant as no-paper evidence; if continuing locally, run a bounded tiny-transformer ablation of compressed or moment-selective residuals against plain 8-bit AdamW.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compressed or moment-selective error feedback for 8-bit AdamW on a tiny transformer
- Success threshold: At matched steps, compressed or selective EF recovers at least 50% of the final-loss gap between plain 8-bit AdamW and AdamW while keeping optimizer-state memory no more than 35% of AdamW and avoiding NaN/Inf in three seeds.
- Stop condition: Stop if residual memory exceeds 35% of AdamW state memory, if the EF variant recovers less than 25% of the plain 8-bit convergence gap, or if any seed shows optimizer instability.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-with-error-feedback-for-tiny-vram-training-fbd213f69bae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
