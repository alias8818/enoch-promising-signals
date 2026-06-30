# CPU-bound 8-bit AdamW with sparse momentum for tiny-VRAM training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-bound-8-bit-adamw-with-sparse-momentum-for-tiny-vram-training-7f472e51fccb`
Run ID: `cpu-bound-8-bit-adamw-with-sparse-momentum-for-tiny-vram-training-7f472e51fccb-20260612T004851030072+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a92f315cb597

## What looked useful

Dense int8 first-moment compression reduced optimizer-state bytes from 8.0 to 5.0 bytes/parameter with final loss ratio 1.00003 versus dense FP32 AdamW. Sparse first-moment updates degraded sharply: top75 ratio 1.43, top50 ratio 3.01, top25 ratio 13.96. Naive int8 second moments failed, reaching 679.86x loss or NaN in sparse-v mode.

## Boundaries and scale limits

No real tiny-VRAM GPU training, transformer task, host-device transfer measurement, or long-run convergence validation was performed. Results are optimizer-mechanism evidence only.

## Claim scope

On a deterministic sparse synthetic linear-regression proxy with 65,536 parameters and 180 AdamW steps, CPU-side blockwise int8 first-moment storage with FP32 second moment matched dense FP32 AdamW, but sparse top-k first-moment updates and naive int8 second-moment storage did not.

## Why it stopped

Bounded proxy evidence supports int8 first-moment CPU state but early-falsifies the sparse momentum variant as tested; this is not full validation of tiny-VRAM training.

## Recommended next action

Stop this run as no-paper useful signal; if continuing locally, test sparse momentum with error feedback or periodic dense refresh before attempting real tiny-VRAM GPU integration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Error-feedback sparse momentum for CPU-offloaded AdamW
- Success threshold: A sparse-momentum method updating at most 50% of first-moment coordinates per step achieves final-loss ratio <= 1.10 versus dense FP32 AdamW and keeps optimizer-state bytes per parameter <= 5.1 on the same proxy.
- Stop condition: Stop if top50 sparse momentum remains >1.25x dense final loss after error feedback and periodic refresh are both tested.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-bound-8-bit-adamw-with-sparse-momentum-for-tiny-vram-training-7f472e51fccb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
