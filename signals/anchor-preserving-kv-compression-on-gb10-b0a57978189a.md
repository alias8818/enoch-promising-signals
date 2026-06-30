# Anchor-Preserving KV Compression on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-preserving-kv-compression-on-gb10-b0a57978189a`
Run ID: `anchor-preserving-kv-compression-on-gb10-b0a57978189a-20260628T070042086129+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b49dbf04196f

## What looked useful

Anchor-preserving KV compression appears conditionally viable as a gated mechanism: exact in synthetic high-anchor-mass cases, but high-error in unbiased controls where middle-token attention mass dominates. The simple PyTorch weighted pooling path speeds 8192-token attention but is slower at 2048/4096.

## Boundaries and scale limits

No full decoder integration, no perplexity or generation-quality measurement, no paged-attention serving benchmark, no real model attention traces, and only batch=1/query_len=1 synthetic BF16 cases up to 8192 tokens.

## Claim scope

Synthetic single-step CUDA attention microbenchmarks on GB10 show that preserving prefix/recent anchors while block-pooling middle KV can save 75-87% KV memory and preserve attention output only when full attention mass is already almost entirely on preserved anchors/recent tokens.

## Why it stopped

Proxy-only useful signal: synthetic attention supports the anchor-mass gating mechanism but unbiased controls falsify a broad quality-preserving compression claim.

## Recommended next action

Do not write a paper from this run; run a bounded real-decoder follow-up that measures per-layer/head anchor mass and applies compression only above a predeclared threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-decoder anchor-mass gating for KV compression
- Success threshold: At least 50% KV memory reduction on eligible heads/layers with less than 2% relative next-token-loss increase and non-negative decode throughput change versus the uncompressed baseline.
- Stop condition: Stop if fewer than 25% of heads/layers exceed the anchor-mass threshold or if gated compression exceeds 2% relative next-token-loss increase at less than 50% KV memory reduction.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserving-kv-compression-on-gb10-b0a57978189a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
