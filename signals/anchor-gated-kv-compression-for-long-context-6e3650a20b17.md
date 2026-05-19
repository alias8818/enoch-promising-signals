# Anchor-Gated KV Compression for Long Context

Status: `useful_signal`
Project ID: `anchor-gated-kv-compression-for-long-context-6e3650a20b17`
Run ID: `anchor-gated-kv-compression-for-long-context-6e3650a20b17-20260518T152914434710+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/0f8adfba42ee

## What looked useful

Anchor-gated routing achieved 1.000 mean accuracy at anchor noise 0.05/0.15 across all tested budgets and contexts; at noise 0.30 it averaged 0.927 accuracy, while high anchor noise 0.60 exposed a failure mode with mean 0.571 accuracy. Best non-oracle controls stayed near their retained-token fractions.

## Boundaries and scale limits

No real transformer KV activations, no learned anchors, no perplexity or downstream QA metrics, no production attention kernel, and no datacenter-scale model validation were run. Context lengths were 4096 and 8192 with generated vectors only.

## Claim scope

Synthetic long-context key/query retrieval shows anchor-gated segment selection can preserve old-token retrieval at roughly 4.7-24.0% retained KV when anchor keys are informative, beating local, stride, and random cache controls at matched nominal budgets.

## Why it stopped

Proxy-only synthetic evidence supports the mechanism under informative anchors but does not validate real model KV compression, latency, or task quality.

## Recommended next action

Stop this run as a proxy useful signal; next, run a bounded small-transformer follow-up with learned anchors and matched KV-compression baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Anchor-Gated KV Compression in a Small Transformer Retrieval Task
- Success threshold: At 12.5-25% retained KV, learned anchor-gated compression should recover at least 90% of full-cache retrieval accuracy and beat the best matched-memory non-oracle baseline by at least 10 percentage points across three seeds.
- Stop condition: Stop if learned anchors fail to beat the best matched-memory non-oracle baseline by 5 percentage points at both 12.5% and 25% retained KV, or if anchor routing overhead erases the memory/latency benefit in the small-model implementation.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-gated-kv-compression-for-long-context-6e3650a20b17`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
