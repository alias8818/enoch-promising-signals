# Chunked INT8 AdamW with Error Feedback on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `chunked-int8-adamw-with-error-feedback-on-cpu-cecf57a8b960`
Run ID: `chunked-int8-adamw-with-error-feedback-on-cpu-cecf57a8b960-20260629T005732117963+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d1376a4c5689

## What looked useful

Naively quantizing AdamW first and second moments as signed linear INT8 per chunk is unstable in this harness. The second-moment state can quantize small coordinates toward zero, causing excessive Adam updates; FP16 residual error feedback overflowed instead of correcting the error.

## Boundaries and scale limits

Not tested on transformer pretraining, GPT-2-small, PyTorch models, mixed precision kernels, or long training runs. The result isolates optimizer-state mechanics on a deterministic proxy task and should not be read as a universal rejection of all 8-bit Adam variants.

## Claim scope

Bounded CPU NumPy logistic-regression evidence against naive chunked signed-INT8 AdamW moment-state storage with FP16 residual error feedback. FP32 AdamW converged; INT8 no-error-feedback collapsed to high loss; FP16 residual error feedback diverged to non-finite loss across all main seeds and chunk sizes.

## Why it stopped

Early proxy falsification: the tested naive chunked signed-INT8 AdamW with FP16 residual error feedback failed a deterministic CPU optimizer-state convergence test, so it is not ready for transformer-scale validation.

## Recommended next action

Stop this formulation; before any model-scale training, test a bounded revised optimizer that stores the second moment with nonnegative/log-domain or relative quantization plus denominator floors and bounded residuals on the same harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Guarded nonnegative second-moment quantization for INT8 AdamW
- Success threshold: Mean validation loss within 5% of FP32 AdamW and no non-finite runs across 5 seeds for at least two chunk sizes while using less than 60% of FP32 optimizer-state bytes.
- Stop condition: Stop if any guarded variant still produces non-finite loss or exceeds 2x FP32 validation loss on two or more seeds at chunk size 256.

## Evidence references

- Artifact root: `<local-path>/projects/chunked-int8-adamw-with-error-feedback-on-cpu-cecf57a8b960`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
