# Additive Residual Codebook for 1.58-Bit KV Cache

Status: `compute_scale_blocked`
Project ID: `additive-residual-codebook-for-1-58-bit-kv-cache-b4795df000ba`
Run ID: `additive-residual-codebook-for-1-58-bit-kv-cache-b4795df000ba-20260515T040004853927+0000`

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

Proxy/early falsification rather than full validation; no end-to-end perplexity, decode-quality, or serving-throughput evidence was produced, and the direct attention-output proxy was negative versus ternary.

## Recommended next action

Stop this run as a proxy/early falsification: vanilla ARCB at 1.58 nominal bits/scalar improved raw reconstruction only in the larger per-layer variant, but failed the target-relevant attention-output metric against same-rate ternary.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Attention-aware residual codebooks for 1.58-bit KV cache
- Success threshold: Beat scalar ternary by at least 10% relative mean attention-output NRMSE on layers 0/6/11 and keep end-to-end next-token loss within 2% of the uncompressed KV baseline at equal real cache bytes.
- Stop condition: Stop if attention-aware ARCB does not beat ternary on mean attention-output NRMSE in the GPT-2-small probe or if real byte accounting exceeds the 1.58-bit target by more than 10%.

## Evidence references

- Artifact root: `<local-path>/projects/additive-residual-codebook-for-1-58-bit-kv-cache-b4795df000ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
