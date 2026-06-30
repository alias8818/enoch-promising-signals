# Residual rollback draft: 1-bit draft with FP16 verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-rollback-draft-1-bit-draft-with-fp16-verification-c9f136f2ae91`
Run ID: `residual-rollback-draft-1-bit-draft-with-fp16-verification-c9f136f2ae91-20260602T160815241348+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/50c77ab4cb0d

## What looked useful

Rollback is a viable exactness guard, but the tested 1-bit residual draft accepted only about 8-18% of proposals versus about 87-97% for int8, creating thousands of rollbacks over 4096 emitted tokens. FP16-vs-FP32 verifier top-1 disagreement was small but nonzero at 0.00317.

## Boundaries and scale limits

Toy residual LM only; no trained Transformer, no GPT-2-small-class baseline, no fused 1-bit kernel, no GPU or serving benchmark. FP16 verification was CPU-emulated top-1 checking, not a production verifier implementation.

## Claim scope

On a NumPy residual autoregressive proxy, rollback verification preserves exact greedy outputs for quantized drafts, but naive 1-bit residual-state drafting has low proposal acceptance and only weak optimistic speed margin compared with an int8 control.

## Why it stopped

Early proxy falsification of naive 1-bit residual-state drafting efficiency, not a full-scale validation; rollback exactness worked, but 1-bit acceptance was too low to support a practical speed claim.

## Recommended next action

Stop this run as a proxy useful-signal negative; next run should test trained-small-LM int8, ternary or 2-bit, and 1-bit residual drafts with identical rollback verification and margin-aware FP16 fallback.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained-small-LM residual draft precision ladder with rollback verification
- Success threshold: At least one sub-8-bit draft precision achieves exact rollback-verified outputs, mean accepted prefix length >= 3 for block size 4 or >= 5 for block size 8, FP16 fallback rate below 1%, and an optimistic verifier-batch speed model above 2x with a documented draft-cost assumption.
- Stop condition: Stop if all sub-8-bit drafts have mean accepted prefix length below 2 or FP16 verifier instability requires fallback on more than 5% of generated positions.

## Evidence references

- Artifact root: `<local-path>/projects/residual-rollback-draft-1-bit-draft-with-fp16-verification-c9f136f2ae91`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
