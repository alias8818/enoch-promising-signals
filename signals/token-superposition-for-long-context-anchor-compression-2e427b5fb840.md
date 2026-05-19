# Token Superposition for Long-Context Anchor Compression

Status: `useful_signal`
Project ID: `token-superposition-for-long-context-anchor-compression-2e427b5fb840`
Run ID: `token-superposition-for-long-context-anchor-compression-2e427b5fb840-20260514T103817560204+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Efficient Pre-Training with Token Superposition: https://arxiv.org/abs/2605.06546
- Token Superposition for Long-Context Anchor Compression: https://arxiv.org/abs/2605.06546

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Synthetic anchor-value superposition beat simple controls, but this is proxy evidence only and does not validate long-context transformer anchor compression or publication-grade claims.

## Recommended next action

Stop this run as a proxy-only negative paper-gate result; run one bounded direct model-level follow-up if the controller wants to test whether the synthetic mechanism transfers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-level superposed anchor compression on long-context recall
- Success threshold: At 4x or greater anchor/KV memory reduction, superposed anchors retain at least 95% of dense-baseline task quality and outperform pooling/random-compression controls by at least 10 percentage points absolute exact-match or an equivalent predeclared perplexity margin.
- Stop condition: Stop if superposed anchors fail to beat pooling/random controls at 2x compression on the small model task, or if quality drops below 90% of dense baseline before reaching 4x compression.

## Evidence references

- Artifact root: `<local-path>/projects/token-superposition-for-long-context-anchor-compression-2e427b5fb840`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
