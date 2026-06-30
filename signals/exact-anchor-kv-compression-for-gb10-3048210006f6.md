# Exact Anchor KV Compression for GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-compression-for-gb10-3048210006f6`
Run ID: `exact-anchor-kv-compression-for-gb10-3048210006f6-20260611T032701029964+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a1a3c6f35e71

## What looked useful

Periodic exact anchors preserve attention outputs on smooth synthetic KV traces with 0.1% to 1.1% mean relative L2 error and 4x to 32x nominal KV compression, but fail retrieval-like non-anchor spikes with about 0.85 mean relative L2 error; linear reconstruction loses target attention mass from 0.4359 to about 0.000316 and is slower than full attention in this implementation.

## Boundaries and scale limits

No real model KV traces, perplexity, QA, long-context serving, or optimized compressed-attention kernel were evaluated. The retrieval-spike case is synthetic but directly tests a known failure mode for periodic anchors.

## Claim scope

Bounded synthetic GB10 BF16 decode-attention test of periodic exact-anchor KV compression at seq_len=4096, heads=8, dim=64, n_queries=32, strides 4/8/16/32, comparing full KV attention with anchor-only exact attention and exact-anchor linear reconstruction.

## Why it stopped

Proxy/early falsification rather than full validation: a synthetic retrieval-like non-anchor token that full attention ranks first is omitted or erased by periodic exact anchors, causing large output error even at stride 4.

## Recommended next action

Stop this periodic-anchor version as no-paper evidence; if continuing locally, test adaptive salience-based anchor selection on real GPT-2-small-class KV traces against full KV and at least one established KV compression baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Salience Anchors for Retrieval-Safe KV Compression
- Success threshold: At 4x or greater KV memory reduction, adaptive anchors keep mean attention-output relative L2 below 0.05 on retrieval-heavy traces and recover at least 90% of full-KV retrieval target attention mass, while not regressing smooth-trace error versus periodic anchors.
- Stop condition: Stop if adaptive anchors still lose more than 25% of full-KV retrieval target attention mass at 4x compression or require full-cache reconstruction that is slower than full KV attention.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-gb10-3048210006f6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
