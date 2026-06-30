# KV-cache compression via grouped product quantization with offline codebook refresh

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-compression-via-grouped-product-quantization-with-offline-codebook-refresh-bae120540d4f`
Run ID: `kv-cache-compression-via-grouped-product-quantization-with-offline-codebook-refresh-bae120540d4f-20260628T030652120167+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a959f9b7cbe6

## What looked useful

Offline codebook refresh was the key mechanism: at 4 bits/value refreshed PQ mean relative attention MSE was 0.0157-0.0159 versus stale PQ 0.0405-0.0414 and int4 0.0176. More aggressive 2 bit/value PQ remained much worse than int4.

## Boundaries and scale limits

Only distilgpt2, 16 hand-written prompts, sequence length up to 128, attention-output reconstruction metrics, and offline CPU PQ training were tested. No online decoding, perplexity, long-context retrieval, throughput, codebook-overhead accounting, or 7B+ validation was performed.

## Claim scope

On a bounded distilgpt2 proxy with real past_key_values, grouped PQ with offline domain refresh reduced attention-output reconstruction error versus stale codebooks; at 4 index bits/value it slightly beat row-wise int4 on mean relative attention MSE but not on worst-layer error.

## Why it stopped

Bounded proxy evidence supports the refresh mechanism but is insufficient for a paper-ready KV-cache compression claim.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement online compressed-cache decoding and evaluate perplexity, token divergence, memory, and latency against int4 on a public corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online refreshed-PQ KV-cache decoding versus int4 on GPT-2-small-class text
- Success threshold: At 4 index bits/value, refreshed PQ must be no worse than int4 on perplexity or next-token divergence, no worse than 10% slower in decode latency after amortizing refresh, and must report actual memory including codebooks.
- Stop condition: Stop if refreshed PQ is worse than int4 on both quality and latency, or if codebook overhead removes the intended memory advantage for practical context lengths.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-via-grouped-product-quantization-with-offline-codebook-refresh-bae120540d4f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
