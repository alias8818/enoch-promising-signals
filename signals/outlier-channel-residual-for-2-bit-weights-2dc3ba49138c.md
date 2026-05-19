# Outlier-Channel Residual for 2-bit Weights

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `83`
Project ID: `outlier-channel-residual-for-2-bit-weights-2dc3ba49138c`
Run ID: `outlier-channel-residual-for-2-bit-weights-2dc3ba49138c-20260514T224300639618+0000`

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

Layer-output proxy evidence supports the mechanism, but this is not full validation: no end-to-end perplexity, calibrated quantization baseline, or packed-kernel memory/latency evidence was produced.

## Recommended next action

Stop this run as a no-paper proxy result; run a bounded end-to-end perplexity follow-up on a GPT-2-small-class model with matched effective-bit baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end perplexity test for 2-bit outlier-channel residuals
- Success threshold: Selected residual channels reduce perplexity degradation by at least 10% relative to plain 2-bit and beat random residual channels at the same effective bits on at least two residual budgets without increasing storage beyond the declared budget.
- Stop condition: Stop if selected residual channels fail to beat random residual channels on end-to-end perplexity at matched effective bits, or if gains disappear against a calibrated baseline.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-channel-residual-for-2-bit-weights-2dc3ba49138c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
