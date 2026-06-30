# Ternary Weights with FP16 Residual Outlier Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-weights-with-fp16-residual-outlier-channels-120416dd6a1f`
Run ID: `ternary-weights-with-fp16-residual-outlier-channels-120416dd6a1f-20260602T181653572245+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/878afbbb9b2b

## What looked useful

At 4% residual channels, synthetic median output relative RMSE improved from 0.6621 plain ternary to 0.3182, while GPT-2 matrix median improved only from 0.4699 to 0.4338. In a small GPT-2 loss probe, dense loss was 4.8322, plain ternary was 9.1969, and 4% residual channels reduced that to 6.5328.

## Boundaries and scale limits

Tested synthetic matrices up to 1024x4096, 12 GPT-2-small matrices, and a fixed local GPT-2 text loss probe. No packed kernel, no benchmark validation perplexity, no activation-aware selector, and no larger model evaluation were run.

## Claim scope

Bounded local evidence shows that selecting FP16 residual input channels by ternary residual energy improves reconstruction and small GPT-2 fixed-text loss versus plain ternary, but only synthetic channel-outlier matrices show large matrix-level gains.

## Why it stopped

No-paper useful signal: the mechanism improves over plain ternary, but naive residual-energy channel selection leaves substantial GPT-2 loss degradation and does not support a publication-grade compression claim.

## Recommended next action

Run a bounded activation-aware residual-channel selection follow-up on GPT-2-small with a real validation perplexity benchmark before considering kernel work or larger models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware FP16 residual channels for ternary GPT-2 projections
- Success threshold: At 4% residual channels, activation-aware selection should reduce validation perplexity degradation by at least 50% versus weight-residual channel selection and remain at least 5.5x compressed versus dense FP16 under explicit storage accounting.
- Stop condition: Stop if activation-aware selection fails to materially outperform weight-residual selection on validation perplexity at matched storage, or if degradation remains too large for a plausible compression method.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-weights-with-fp16-residual-outlier-channels-120416dd6a1f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
