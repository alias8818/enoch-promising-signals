# Learned Anchor Router for Exact KV Retrieval

Status: `useful_signal`
Project ID: `learned-anchor-router-for-exact-kv-retrieval-edc371259c`
Run ID: `learned-anchor-router-for-exact-kv-retrieval-edc371259c-20260515T105106870168+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8f955958c14a

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Small controlled synthetic evidence is mechanism-supporting but not publication-grade, and the learned router is training-sensitive and not clearly superior to the exact-anchor control.

## Recommended next action

Stop this run as no-paper: the small direct synthetic test supports the routing mechanism after sufficient training, but publication would require a medium direct benchmark on real or model-generated KV tensors with strong non-learned routing and optimized retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium real-KV anchor router benchmark
- Success threshold: Across all tested cache sizes and seeds, learned routing achieves >=99% exact target recall, scans <=10% of keys, and improves optimized end-to-end retrieval latency by >=20% versus the best non-learned routing baseline without material recall loss.
- Stop condition: Stop if learned routing fails to reach 99% recall at <=10% scan on real/model-generated KV tensors, or if it does not beat the best non-learned routing baseline after one bounded implementation pass.

## Evidence references

- Artifact root: `<local-path>/projects/learned-anchor-router-for-exact-kv-retrieval-edc371259c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
