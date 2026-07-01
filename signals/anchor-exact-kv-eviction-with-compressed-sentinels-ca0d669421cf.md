# Anchor-Exact KV Eviction with Compressed Sentinels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-exact-kv-eviction-with-compressed-sentinels-ca0d669421cf`
Run ID: `anchor-exact-kv-eviction-with-compressed-sentinels-ca0d669421cf-20260529T182651328003+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/770071bce95e

## What looked useful

Anchor-exact plus sentinels improves over sliding-window output reconstruction and greatly improves exact anchor-target retention on anchor-biased retrieval, but loses output MSE and cosine to a budget-matched compressed-sentinel baseline by about 2.03x MSE in all tested modes.

## Boundaries and scale limits

No real transformer perplexity or downstream task evaluation; no learned anchor selector; no multi-layer cache dynamics; no kernel or serving throughput measurement; four trials per synthetic mode only.

## Claim scope

Synthetic single-head attention reconstruction with oracle periodic anchors, mean-compressed sentinels, 512-item sequences, 64-dimensional K/V, and a 96-entry cache budget.

## Why it stopped

Closed as no-paper useful signal because the proxy test is mixed and the primary output-reconstruction metric does not beat a budget-matched sentinel baseline; this is an early proxy result, not full validation.

## Recommended next action

Run a bounded small-transformer cache-replay follow-up measuring perplexity/task accuracy with fixed cache budgets and H2O/sliding/sentinel baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-Transformer Cache Replay for Anchor-Exact Sentinels
- Success threshold: Anchor-exact-sentinel must improve task accuracy or perplexity over the best budget-matched baseline by at least 5% relative or reduce logit divergence by at least 10% without increasing cache entries.
- Stop condition: Stop if anchor-exact-sentinel fails to beat the best budget-matched baseline on both task quality and logit divergence in two independent seeds or datasets.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-exact-kv-eviction-with-compressed-sentinels-ca0d669421cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
