# Sub-4-bit Optimizer States with Error-Feedback: 3-bit AdamW

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sub-4-bit-optimizer-states-with-error-feedback-3-bit-adamw-2eaf2c171fa0`
Run ID: `sub-4-bit-optimizer-states-with-error-feedback-3-bit-adamw-2eaf2c171fa0-20260628T044832216539+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3b3b24b7b337

## What looked useful

Naive symmetric quantization of AdamW second moments produced NaNs. Positive second-moment quantization stabilized 3-bit states. Error feedback preserved AdamW-like behavior, but only by carrying full-precision residuals that made estimated optimizer state 0.0686 MiB versus 0.0625 MiB for FP32 AdamW at dim 8192.

## Boundaries and scale limits

Synthetic regression only; no transformer, no real dataset, no packed optimizer kernel, no residual-compressed error feedback, and no datacenter-scale training.

## Claim scope

On a CUDA synthetic linear-regression proxy, 3-bit AdamW with positive second-moment quantization and full-precision error-feedback residuals tracks FP32 AdamW validation loss within about 0.2% to 2.7% across tested learning rates, but does not reduce total optimizer-state memory because residual buffers exceed the saved quantized-state storage.

## Why it stopped

Proxy evidence supports error feedback as a fidelity mechanism but early-falsifies the sub-4-bit memory-saving claim for the tested full-residual design; this is not a full-scale validation.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded test should compress or eliminate error-feedback residual buffers and require total optimizer-state memory below FP32 AdamW while matching tuned AdamW on the same proxy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-compressed 3-bit AdamW error feedback
- Success threshold: Total optimizer-state storage at least 25% below FP32 AdamW and validation loss within 5% of tuned FP32 AdamW on the regression proxy without NaNs across three seeds.
- Stop condition: Stop if residual-compressed error feedback either exceeds FP32 state memory or diverges/loses more than 10% versus tuned FP32 AdamW on the proxy.

## Evidence references

- Artifact root: `<local-path>/projects/sub-4-bit-optimizer-states-with-error-feedback-3-bit-adamw-2eaf2c171fa0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
