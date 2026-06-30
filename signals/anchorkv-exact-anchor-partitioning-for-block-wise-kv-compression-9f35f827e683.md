# AnchorKV: Exact Anchor Partitioning for Block-wise KV Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchorkv-exact-anchor-partitioning-for-block-wise-kv-compression-9f35f827e683`
Run ID: `anchorkv-exact-anchor-partitioning-for-block-wise-kv-compression-9f35f827e683-20260519T223326083038+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b5f6da419786

## What looked useful

Exact anchor partitioning is algorithmically viable and never lost on its optimized weighted KV objective across 128 corrected sweep cells, but downstream attention-output MSE was mixed versus uniform blocks, especially on smooth and random synthetic traces.

## Boundaries and scale limits

No real LLM KV traces, no end-to-end perplexity or retrieval evaluation, no serving throughput measurement, sequence lengths only 64-192 in the smoke/sweep harness, and attention weights were fixed from uncompressed keys.

## Claim scope

Synthetic proxy evidence for exact contiguous anchor partitioning under fixed block budgets: exact DP reliably minimizes weighted KV reconstruction and improves attention-output MSE on structured piecewise/bursty traces, but not on all regimes.

## Why it stopped

Proxy evidence supports the mechanism but falsifies the broad claim that weighted exact anchor partitioning reliably improves downstream attention-output error versus simple uniform blocks.

## Recommended next action

Stop this run as no-paper useful signal; next run should test an attention-aware exact interval objective on real small-model KV/attention traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Attention-aware exact anchor partitioning on real small-model KV traces
- Success threshold: Exact attention-aware partitioning improves attention-output MSE by at least 10% versus uniform on at least 75% of real-trace cells without worsening perplexity delta relative to uniform at the same compression ratio.
- Stop condition: Stop if attention-aware exact partitioning fails to beat uniform on attention-output MSE in more than half of real-trace cells or if end-to-end perplexity degradation is consistently worse than uniform at matched compression.

## Evidence references

- Artifact root: `<local-path>/projects/anchorkv-exact-anchor-partitioning-for-block-wise-kv-compression-9f35f827e683`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
