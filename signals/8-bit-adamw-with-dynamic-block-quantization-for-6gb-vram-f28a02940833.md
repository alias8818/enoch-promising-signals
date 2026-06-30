# 8-bit AdamW with Dynamic Block Quantization for <6GB VRAM

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `8-bit-adamw-with-dynamic-block-quantization-for-6gb-vram-f28a02940833`
Run ID: `8-bit-adamw-with-dynamic-block-quantization-for-6gb-vram-f28a02940833-20260610T004613880162+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b33d95b272d0

## What looked useful

Dynamic block sizing alone did not solve the stability problem. Second-moment quantization produced zero or badly distorted denominators early in training; fp16 scales made this visible as all v scales underflowing to zero for four steps, and fp32 scale metadata still diverged. The dynamic heuristic also missed sparse outliers, choosing 4096 blocks where 256 blocks reduced rel-RMSE by about 4x.

## Boundaries and scale limits

Tested on synthetic tensors, one-step update error, and a 3.67M-parameter toy regression model for 60 steps on NVIDIA GB10. Did not test a real 6GB cap, GPT-2-small-class transformer training, long training, or production 8-bit optimizer safeguards.

## Claim scope

A bounded CUDA toy-training probe of naive blockwise int8 AdamW moment storage with static and dynamic block sizes showed the expected ~75% optimizer-state memory reduction, but all quantized variants diverged to NaN while fp32 AdamW converged.

## Why it stopped

Early direct falsification on a small CUDA training probe: memory savings were achieved, but all int8 moment variants reached NaN while fp32 AdamW converged. This is not a full-scale validation, but it is enough to reject the naive dynamic-block approach as paper-ready.

## Recommended next action

Stop this line as a paper candidate; run a bounded follow-up that keeps AdamW second moments numerically safe, such as quantizing sqrt(v), log-domain v, or guarding low-magnitude v in higher precision, before retesting dynamic blocks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Second-moment-safe 8-bit AdamW before dynamic block sizing
- Success threshold: No NaNs in 500 steps, final toy loss within 10% of fp32 AdamW, and dynamic blocks reduce state quantization rel-RMSE by at least 25% versus fixed 4096 without using more than 3% additional state memory.
- Stop condition: Stop if the safer second-moment representation still produces NaNs or final loss more than 2x fp32 AdamW by 100 steps on the same toy task.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-with-dynamic-block-quantization-for-6gb-vram-f28a02940833`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
