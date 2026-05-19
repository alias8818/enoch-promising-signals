# Attention-aware residual codebooks for 1.58-bit KV cache

Status: `compute_scale_blocked`
Project ID: `attention-aware-residual-codebooks-for-1-58-bit-kv-cache-3f1bc04709`
Run ID: `attention-aware-residual-codebooks-for-1-58-bit-kv-cache-3f1bc04709-20260515T040447897599+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/08a94314b5ab

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 1 direct attention-output evidence supports the mechanism but is not full validation or paper-positive evidence.

## Recommended next action

Stop this Tier 1 run as no-paper but run a bounded deepen follow-up that evaluates actual autoregressive KV-cache replacement on GPT-2-small-class perplexity/logit KL with packed-cache metadata accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2 KV-cache evaluation for attention-aware 1.58-bit codebooks
- Success threshold: On at least 100k validation tokens, reduce perplexity or mean logit-KL degradation by at least 20% versus equal-bit unweighted ternary while staying within 10% of the 2-bit baseline quality after metadata accounting.
- Stop condition: Stop if the attention-aware 1.58-bit cache fails to improve perplexity/logit KL by at least 10% over equal-bit ternary on a 10k-token pilot, or if metadata/decode overhead eliminates the claimed 1.58-bit storage advantage.

## Evidence references

- Artifact root: `<local-path>/projects/attention-aware-residual-codebooks-for-1-58-bit-kv-cache-3f1bc04709`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
