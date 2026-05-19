# End-to-end perplexity test for 2-bit outlier-channel residuals

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `83`
Project ID: `end-to-end-perplexity-test-for-2-bit-outlier-channel-resid-85f1d9e9fb`
Run ID: `end-to-end-perplexity-test-for-2-bit-outlier-channel-resid-85f1d9e9fb-20260514T225106746118+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/9f40511c351b

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 1 direct GPT-2/WikiText-2 perplexity test found that simple 2-bit projection quantization plus exact outlier-channel residuals remains unusable even at 25% residual channels; this is an early direct falsification of the simple method, not a full validation of all possible 2-bit schemes.

## Recommended next action

Do not write a paper from this result; if continuing, run one bounded direct follow-up that combines activation-outlier residuals with layer-wise mixed precision or reconstruction and requires near-baseline PPL.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-outlier residuals with layer-wise reconstruction for GPT-2-small perplexity
- Success threshold: PPL no worse than 1.2x the FP baseline while using no more than 3.5 estimated bits per quantized projection parameter, with improvement over same-budget random-channel control.
- Stop condition: Stop negative if the best bounded variant exceeds 2x FP PPL or needs more than 4.0 estimated bits per quantized projection parameter.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-perplexity-test-for-2-bit-outlier-channel-resid-85f1d9e9fb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
