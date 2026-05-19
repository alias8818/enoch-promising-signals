# 2-bit KV cache with per-head residual correction for long context

Status: `useful_signal`
Project ID: `2-bit-kv-cache-with-per-head-residual-correction-for-long-context-7da3805285d2`
Run ID: `2-bit-kv-cache-with-per-head-residual-correction-for-long-context-7da3805285d2-20260514T115452243434+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c7106e4b8fcc

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Synthetic attention replay showed per-head mean residual correction reduces 2-bit output error in some regimes, but corrected 2-bit remains 2.7x-6.4x worse than 4-bit and does not improve top-32 attention ranking, so the long-context KV-cache claim is not paper-ready.

## Recommended next action

Stop this run as a proxy early falsification of paper-readiness; only deepen with a bounded real-LLM KV-cache evaluation if the controller wants direct model evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-transformer evaluation of 2-bit KV residual correction
- Success threshold: Corrected 2-bit KV must recover at least 90% of the 4-bit-vs-2-bit quality gap on perplexity/retrieval while preserving at least 6x effective KV compression versus FP16 and no more than 15% decode latency overhead versus uncorrected 2-bit.
- Stop condition: Stop if corrected 2-bit remains more than 2x worse than 4-bit on attention-output error or loses more than 10% absolute long-context retrieval accuracy versus 4-bit in the small-transformer evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-per-head-residual-correction-for-long-context-7da3805285d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
