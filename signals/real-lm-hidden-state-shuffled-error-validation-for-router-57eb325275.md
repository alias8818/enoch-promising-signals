# Real-LM hidden-state shuffled-error validation for router-calibrated KV adapters

Status: `useful_signal`
Project ID: `real-lm-hidden-state-shuffled-error-validation-for-router-57eb325275`
Run ID: `real-lm-hidden-state-shuffled-error-validation-for-router-57eb325275-20260517T234704367995+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Real-LM hidden-state shuffled-error validation for router-calibrated KV adapters: internal_generated:real-lm-hidden-state-shuffled-error-validation-for-router-57eb325275

## What looked useful

The adapter family is useful and the aligned error-feature router shows a small real-LM hidden-state signal: true error features beat shuffled-error training on attention MSE in 29/30 cells and KL in 24/30 cells. The margin is too small and CE too mixed for paper readiness.

## Boundaries and scale limits

Single small GPT-2-family model, Wikitext-2 only, post-hoc attention-output adapters, synthetic 2-4 bit K/V corruption policies, no integrated autoregressive KV-cache serving, no latency or memory-savings measurement, no larger model families.

## Claim scope

On distilgpt2 Wikitext-2 hidden states across layers 1, 2, and 4, two synthetic KV-cache pressure policies, and five fixed seeds, routed residual KV adapters improve corrupted-cache attention/logit metrics versus uncorrected and static baselines; true cache-error features add a small attention-MSE and KL benefit over no-error and shuffled-error controls, but not a robust cross-entropy benefit.

## Why it stopped

Real-LM multi-layer validation found only a modest metric-dependent advantage for true error features over shuffled/no-error controls, with no robust cross-entropy gain and no integrated serving evidence.

## Recommended next action

Stop this depth-4 follow-up and retain the bounded negative/useful artifact; the controller lineage is capped at depth 4 and the mechanism-specific evidence is not paper-ready.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-lm-hidden-state-shuffled-error-validation-for-router-57eb325275`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
