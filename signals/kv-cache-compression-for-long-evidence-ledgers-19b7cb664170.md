# KV-Cache Compression for Long Evidence Ledgers

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `kv-cache-compression-for-long-evidence-ledgers-19b7cb664170`
Run ID: `kv-cache-compression-for-long-evidence-ledgers-19b7cb664170-20260602T171524195708+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/77930d8ad634

## What looked useful

Full KV attention retrieved the target evidence with 100% exact hit rate across 1024, 4096, and 8192 entry ledgers. At 8x compression, the best exact hit rates were only about 0.13, and even the favorable oracle topic mean summary reached only 0.679 to 0.772 mean cosine similarity to the full-cache output, below the 0.95 threshold.

## Boundaries and scale limits

Synthetic single-layer attention probe only; no real transformer generation, learned compressor, query-conditioned cache, production serving trace, or 7B+ long-context model validation was run.

## Claim scope

Simple lossy KV-cache compression policies, including sparse retention, contiguous block means, and oracle topic mean summaries, do not preserve rare exact-evidence retrieval on the synthetic long-ledger benchmark at 8x compression.

## Why it stopped

Proxy early falsification: simple lossy compression failed the exact-evidence and output-cosine thresholds despite a perfect full-cache baseline and an oracle topic-summary control.

## Recommended next action

Stop this run as a proxy early falsification of simple lossy KV summaries; next bounded work should test a query-conditioned exact-entry retrieval/cache scheme on the same benchmark before any larger model run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Query-conditioned exact-entry KV retrieval for evidence ledgers
- Success threshold: At 8x effective resident-cache compression, achieve at least 0.90 exact hit rate and at least 0.95 mean cosine similarity to full-cache output on all three medium ledger sizes, with measured latency overhead below 2x full attention for the synthetic benchmark.
- Stop condition: Stop if selected-block recall is below 0.90 or latency exceeds 2x full attention at 8x effective compression after vectorized implementation.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-for-long-evidence-ledgers-19b7cb664170`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
