# Anchor-Indexed Sparse KV Cache with Entropy Selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-indexed-sparse-kv-cache-with-entropy-selection-5192f282b74f`
Run ID: `anchor-indexed-sparse-kv-cache-with-entropy-selection-5192f282b74f-20260525T032801437589+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/94d9ebb9dd35

## What looked useful

Capped anchor-entropy routing used about 22% of dense query-key dot products and consistently improved retained attention mass over recency baselines, especially in global-cluster regimes, but uncapped entropy routing often spent 68-90% dense compute and capped top-1 retention remained modest outside clustered cases.

## Boundaries and scale limits

No pretrained language model, perplexity, serving latency, GPU kernel, batching, long-context, or production KV-cache update test was run. Compute savings are dot-product-count proxies, not wall-clock inference measurements.

## Claim scope

Bounded synthetic sparse-attention approximation at 1024 keys, 512 queries per regime, budgets 32/64/128, four controlled regimes, and five seeds for the capped-routing variant.

## Why it stopped

Closed as a proxy useful-signal run rather than full validation because the evidence is synthetic approximation only and does not test real model quality or serving latency.

## Recommended next action

Run a bounded GPT-2-small attention-trace/perplexity follow-up comparing dense, recency, anchor_recent, capped anchor_entropy, and oracle_topk under matched KV budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small trace validation for capped anchor-entropy sparse KV selection
- Success threshold: At budgets of 64 and 128 on at least 1024 evaluated tokens, capped anchor_entropy should reduce loss gap versus dense by at least 20% relative to recency while staying below 25% dense query-key scoring.
- Stop condition: Stop if capped anchor_entropy is not better than recency on loss gap at both tested budgets or if routing overhead exceeds the configured 25% dense scoring target.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-sparse-kv-cache-with-entropy-selection-5192f282b74f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
