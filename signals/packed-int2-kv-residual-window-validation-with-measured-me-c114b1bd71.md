# Packed int2 KV residual-window validation with measured memory

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `78`
Project ID: `packed-int2-kv-residual-window-validation-with-measured-me-c114b1bd71`
Run ID: `packed-int2-kv-residual-window-validation-with-measured-me-c114b1bd71-20260514T121946428496+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Packed int2 KV residual-window validation with measured memory: internal_generated:packed-int2-kv-residual-window-validation-with-measured-me-c114b1bd71

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier-3 bounded validation produced a mixed result: int2 with a 128-token residual window reached about 6.3x measured long-context memory reduction, but three fixed-seed GPT-2 cache evaluations showed mean delta NLL 0.1600 versus fp16, which is too large for publication readiness.

## Recommended next action

Stop the packed int2 residual-window claim as no-paper: measured memory savings are real, but direct GPT-2 cache-quality validation shows persistent NLL degradation; branch only to the bounded int4 residual-window variant if the controller wants one more depth-4 adjacent test.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Int4 KV residual-window validation with measured memory and standard language metrics
- Success threshold: Delta NLL <= 0.02 or task degradation <= 1% versus fp16 while maintaining at least 3x measured KV memory reduction at 65k tokens.
- Stop condition: Stop negative if int4 residual-window KV exceeds delta NLL 0.02 on standard language metrics, fails to reach 3x measured memory reduction, or requires dequantized full-cache residency that eliminates the memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/packed-int2-kv-residual-window-validation-with-measured-me-c114b1bd71`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
