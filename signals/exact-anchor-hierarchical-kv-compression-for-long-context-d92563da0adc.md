# Exact-Anchor Hierarchical KV Compression for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-hierarchical-kv-compression-for-long-context-d92563da0adc`
Run ID: `exact-anchor-hierarchical-kv-compression-for-long-context-d92563da0adc-20260525T100411345529+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3646626a8185

## What looked useful

Exact anchors are valuable when future queries need those exact anchor KV entries: anchor retrieval top-1 was 0.998 with mean relative output error 0.390, compared with 0.000 top-1 and 0.882 mean relative error for fine block summaries. The same compression failed for non-anchor exact retrieval, with top-1 below 0.01 and mean relative error about 0.884.

## Boundaries and scale limits

No full language model, no learned anchor selector, no multi-layer error accumulation, no real-corpus prompt distribution, no serving kernel throughput, and no 7B-class or datacenter-scale validation were tested.

## Claim scope

Synthetic one-step softmax attention at 8192 sequence items, 64-dimensional K/V, three random seeds: exact-anchor hierarchical KV compression at 7.8% retained KV ratio preserves anchor-aligned exact retrieval far better than no-anchor summaries or uniform exact-token retention, but does not preserve exact retrieval for summarized non-anchor tokens.

## Why it stopped

Proxy synthetic attention evidence supports only a scoped mechanism boundary, not a publication-grade long-context KV compression claim.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should instrument a small transformer inference stack and measure logit divergence plus retrieval accuracy for anchor-aligned and non-anchor prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer validation of exact-anchor KV compression boundary
- Success threshold: At least 95% anchor-aligned retrieval accuracy and materially lower logit KL than matched-budget controls, while explicitly reporting non-anchor degradation rather than hiding it.
- Stop condition: Stop if anchor-aligned retrieval drops below 90% at compression ratios near 8% or if matched-budget controls match exact-anchor logit/retrieval quality.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-hierarchical-kv-compression-for-long-context-d92563da0adc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
