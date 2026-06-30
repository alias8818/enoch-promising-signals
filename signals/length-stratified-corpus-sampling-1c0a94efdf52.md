# Length-stratified corpus sampling

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `length-stratified-corpus-sampling-1c0a94efdf52`
Run ID: `length-stratified-corpus-sampling-1c0a94efdf52-20260607T195700744343+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/236f68721ce2

## What looked useful

Length stratification was essentially tied with uniform sampling across five seeds, with mean overall loss difference -0.001217 nats/token and mixed per-seed signs. Token-proportional sampling lowered aggregate loss by -0.026445 nats/token but worsened the shortest validation bin by +0.205079 nats/token, showing that aggregate gains can hide length-regime regressions.

## Boundaries and scale limits

This is a bounded small-model Wikitext-2 test, not a production web-corpus, tokenizer-level, GPT-2-small-class, or long-horizon validation. It does not rule out gains from other stratification weights, larger models, larger corpora, matched-token training schedules, or downstream-task evaluation.

## Claim scope

On a tiny byte-level causal Transformer trained for 1000 steps on Wikitext-2, equal-quartile length-stratified document sampling did not materially improve overall or per-length-bin validation loss versus uniform document sampling.

## Why it stopped

Bounded direct small-model evidence does not support equal-bin length-stratified sampling as a standalone improvement; this is not a full validation and larger matched-token evidence would be required to overturn it.

## Recommended next action

Stop this run as no-paper evidence; any next study should use a tokenizer-level GPT-2-small-class model with matched train-token budgets and predeclared per-length fairness metrics against uniform and token-proportional baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Matched-token tokenizer-level length sampling comparison
- Success threshold: Length-aware sampling must improve overall validation loss by at least 0.01 nats/token versus uniform while keeping the shortest-bin loss within 0.02 nats/token of uniform and within 0.05 nats/token better than token-proportional.
- Stop condition: Stop if the tuned length-aware sampler is worse than uniform overall by more than 0.005 nats/token or worsens the shortest-bin loss by more than 0.03 nats/token after matched-token training.

## Evidence references

- Artifact root: `<local-path>/projects/length-stratified-corpus-sampling-1c0a94efdf52`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
