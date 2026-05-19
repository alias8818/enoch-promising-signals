# Medium Transformer Validation of Neural Chunk Commitment Under Trace-Driven Lazy Workers

Status: `useful_signal`
Project ID: `medium-transformer-validation-of-neural-chunk-commitment-u-0962eea1a9`
Run ID: `medium-transformer-validation-of-neural-chunk-commitment-u-0962eea1a9-20260518T073653499286+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Medium Transformer Validation of Neural Chunk Commitment Under Trace-Driven Lazy Workers: internal_generated:medium-transformer-validation-of-neural-chunk-commitment-u-0962eea1a9

## What looked useful

NCC reached OOD commitment F1 0.9988 but OOD target accuracy 0.0000, while an oracle pre-attention input mask reached OOD target accuracy 0.6784. The failure is consistent with unavailable chunk information contaminating hidden states before late commitment pooling.

## Boundaries and scale limits

Synthetic stochastic traces only; 3 seeds; 700 training steps; no real production traces, large-corpus language modeling, multi-node training, or learned pre-attention commitment policy.

## Claim scope

In a fixed-seed synthetic trace-driven lazy-worker sequence task with 821k-parameter transformers, late neural chunk-commitment gating learned the commitment mask but did not improve OOD target accuracy over a dense transformer baseline.

## Why it stopped

Medium fixed-seed validation directly falsified the tested late-gating NCC mechanism for the OOD target metric, despite strong commitment-mask learning.

## Recommended next action

Stop this branch as a no-paper negative and run one bounded deepen follow-up that tests learned pre-attention or attention-mask commitment under the same fixed-seed trace protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Pre-Attention Commitment Masks for Trace-Driven Lazy Workers
- Success threshold: Learned pre-attention commitment improves mean OOD target accuracy by at least 0.20 absolute over dense and late-gated NCC, reaches at least 0.60 OOD accuracy, and preserves at least 0.90 OOD commitment F1 across three seeds.
- Stop condition: Stop if learned pre-attention commitment fails to exceed 0.20 OOD accuracy or commitment F1 remains below 0.80 after the same budget, because the oracle diagnostic would not translate to a deployable mechanism.

## Evidence references

- Artifact root: `<local-path>/projects/medium-transformer-validation-of-neural-chunk-commitment-u-0962eea1a9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
