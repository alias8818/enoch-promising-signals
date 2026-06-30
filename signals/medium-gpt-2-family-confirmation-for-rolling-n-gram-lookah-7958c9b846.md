# Medium GPT-2-family confirmation for rolling n-gram lookahead

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `medium-gpt-2-family-confirmation-for-rolling-n-gram-lookah-7958c9b846`
Run ID: `medium-gpt-2-family-confirmation-for-rolling-n-gram-lookah-7958c9b846-20260530T000801581767+0000`

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

- Parent run decision: Real GPT-2 Decoder Test for Rolling N-gram Cache Lookahead: enoch://control-plane/projects/real-gpt-2-decoder-test-for-rolling-n-gram-cache-lookahead-0bd3406942/runs/real-gpt-2-decoder-test-for-rolling-n-gram-cache-lookahead-0bd3406942-20260529T161110896893+0000
- Parent run decision: Rolling N-gram Cache Lookahead: enoch://control-plane/projects/rolling-n-gram-cache-lookahead-29c12306aaed/runs/rolling-n-gram-cache-lookahead-29c12306aaed-20260529T081713137906+0000

## What looked useful

Aligned lookahead achieved higher auxiliary future-token accuracy than shuffled control (0.0708 vs 0.0563), but next-token validation loss was worse than baseline for all three seeds, with mean paired delta +0.00693. Zero-weight matched baseline exactly.

## Boundaries and scale limits

Main fair matrix used batch size 2, 200 update steps, and 20 validation batches because batch-8 and batch-32 full-vocabulary lookahead runs were terminated after early checkpoints on the GB10 host. This is not a long-horizon or large-batch validation.

## Claim scope

On a 4-layer, 256-hidden GPT-2-style causal transformer trained on WikiText-2 with fixed seeds 13, 17, and 19, a full-vocabulary rolling n-gram lookahead auxiliary objective for offsets 2, 3, and 4 learned measurable future-token signal but did not improve next-token validation loss versus a standard GPT-2 backbone baseline.

## Why it stopped

Direct fixed-seed target metrics did not support the hypothesis, and the full-vocabulary auxiliary objective showed practical stability limits before larger-batch confirmation.

## Recommended next action

Stop this formulation as no-paper evidence; only revisit with a memory-efficient tied or chunked auxiliary loss plus a predeclared batch-16-or-larger, multi-seed loss-improvement threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Memory-efficient tied-head rolling lookahead with auxiliary-weight sweep
- Success threshold: Mean paired validation next-token loss at least 0.02 below baseline across three seeds, with no seed worse than baseline by more than 0.005 and aligned lookahead outperforming shuffled control.
- Stop condition: Stop if tied/chunked lookahead still has nonnegative mean paired validation-loss delta versus baseline or cannot run batch 16 stably on GB10.

## Evidence references

- Artifact root: `<local-path>/projects/medium-gpt-2-family-confirmation-for-rolling-n-gram-lookah-7958c9b846`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
