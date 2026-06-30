# Full 2-bit draft transformer residual adapter acceptance test

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `full-2-bit-draft-transformer-residual-adapter-acceptance-t-f70300947f`
Run ID: `full-2-bit-draft-transformer-residual-adapter-acceptance-t-f70300947f-20260523T122948742907+0000`

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

- Parent run decision: Context-conditioned residual adapter for 2-bit draft speculation: enoch://control-plane/projects/context-conditioned-residual-adapter-for-2-bit-draft-specu-c24784c5cd/runs/context-conditioned-residual-adapter-for-2-bit-draft-specu-c24784c5cd-20260523T121812790418+0000
- Parent run decision: 2-bit Draft with Residual-Corrected Target Speculation: enoch://control-plane/projects/2-bit-draft-with-residual-corrected-target-speculation-69d5b4ac9634/runs/2-bit-draft-with-residual-corrected-target-speculation-69d5b4ac9634-20260523T113045486686+0000

## What looked useful

The adapter improved teacher-forced draft NLL from 33.14 to 18.95 but acceptance stayed around 6.2%, with only +0.00094 mean absolute acceptance versus the no-adapter 2-bit baseline and worse KL/top-1 agreement.

## Boundaries and scale limits

Single GPT-2-small-class model family member, 512 training blocks, 128 validation blocks, three fixed seeds, short adapter training, weight-only fake quantization stored in float tensors, no wall-clock serving throughput measurement, no 7B-class or production corpus validation.

## Claim scope

On distilgpt2 with WikiText-2 text, a rank-32 hidden residual adapter trained for 120 steps on a full 2-bit weight-quantized draft did not materially improve speculative acceptance against the full-precision parent target.

## Why it stopped

Tier 2 fixed-seed direct acceptance validation failed to show a meaningful acceptance gain over the real 2-bit no-adapter baseline despite improved NLL.

## Recommended next action

Stop this exact hidden-adapter follow-up as no-paper evidence; run a bounded adjacent test only if the adapter objective/placement changes to directly optimize KL or acceptance.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Acceptance-trained logit residual adapter for full 2-bit drafts
- Success threshold: Mean speculative acceptance improves by at least +0.03 absolute over the 2-bit no-adapter baseline across all three seeds without increasing KL above the no-adapter baseline.
- Stop condition: Stop negative if acceptance gain is below +0.01 absolute or if KL/top-1 agreement degrade while NLL improves, matching this run's failure mode.

## Evidence references

- Artifact root: `<local-path>/projects/full-2-bit-draft-transformer-residual-adapter-acceptance-t-f70300947f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
