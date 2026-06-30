# Retrieval-restored KV compression for long context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `retrieval-restored-kv-compression-for-long-context-10dd1e14e6f3`
Run ID: `retrieval-restored-kv-compression-for-long-context-10dd1e14e6f3-20260613T031842368127+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bfdae30b842d

## What looked useful

Restoration is not the hard part in the controlled sparse-recall setting: exact query-key routing gets 1.000 needle-block hit rate and near-zero relative MSE. The hard part is compact routing: centroid hit rates were only 0.069-0.433 and fixed four-landmark routing was generally worse; centroid restoration beat block-mean compression clearly only for block size 16 with 8 restored blocks.

## Boundaries and scale limits

No real language-model KV traces, no learned router, no autoregressive decode loop, no perplexity or downstream task metric, and no full memory/latency accounting for a token-key retrieval index. Exact-key routing demonstrates mechanism feasibility but retains/scans token-level keys, so it does not establish net KV-cache compression savings.

## Claim scope

Synthetic long-context attention reconstruction with planted sparse needle keys at sequence length 8192, dim 64, 256 queries, block sizes 16-128, restore budgets 1-8, and five seeds. Retrieval restoration reconstructs full attention when routed by exact token-key similarity, but naive compressed block-centroid and fixed-landmark routers miss sparse target blocks often enough to erase or reverse the benefit.

## Why it stopped

Proxy synthetic evidence is sufficient to reject naive centroid/fixed-landmark retrieval-restored KV compression as paper-ready, while preserving a bounded follow-up path for compact high-recall routing.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replace naive summaries with a learned or product-quantized router and evaluate sparse block recall plus attention reconstruction on real small-transformer KV traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned compact router for retrieval-restored KV compression
- Success threshold: At sequence length at least 8192, compact router achieves >=0.90 target-block recall and >=25% lower relative MSE than block-mean compression while using <=25% of full token-key index memory.
- Stop condition: Stop if compact router recall remains below 0.75 or total router plus restored-KV memory exceeds 50% of the uncompressed KV cache at equal or worse reconstruction error.

## Evidence references

- Artifact root: `<local-path>/projects/retrieval-restored-kv-compression-for-long-context-10dd1e14e6f3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
