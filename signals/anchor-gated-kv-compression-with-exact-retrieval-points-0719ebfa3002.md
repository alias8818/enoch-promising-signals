# Anchor-Gated KV Compression with Exact Retrieval Points

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-gated-kv-compression-with-exact-retrieval-points-0719ebfa3002`
Run ID: `anchor-gated-kv-compression-with-exact-retrieval-points-0719ebfa3002-20260527T204613450232+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3b8ae3aeba13

## What looked useful

Anchor-gated exact KV retention preserved dense-attention retrieval for anchor queries with 1.000 top-1 accuracy and 1.000 dense-output cosine at 1024, 4096, and 8192 tokens while using about 2% of KV slots. Uniform block compression and matched random-exact controls failed anchor retrieval. Non-anchor retrieval was not preserved, so the benefit is limited to correctly selected anchors.

## Boundaries and scale limits

Does not test trained language models, learned anchor selection, real retrieval datasets, multi-layer KV caches, positional encodings, long-context serving systems, or end-to-end quality/latency tradeoffs. The result is mechanistic and depends on knowing retrieval anchors in advance.

## Claim scope

Synthetic single-layer attention probe with known exact anchor positions, random normalized keys/values, sequence lengths 1024-8192, 64-dimensional KV, anchor stride 256, block-size 64 compression, 10 seeds, and 128 anchor plus 128 non-anchor queries per seed.

## Why it stopped

No-paper useful signal: the mechanism works in a synthetic known-anchor probe, but this is not direct model evidence and is too narrow for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on a small trained transformer retrieval task with a real anchor-selection rule before considering scale-out validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer retrieval validation for anchor-gated KV compression
- Success threshold: At a matched KV-slot ratio under 10%, non-oracle anchor gating recovers at least 95% of dense retrieval accuracy and improves absolute retrieval accuracy by at least 20 percentage points over uniform block compression on a held-out retrieval task.
- Stop condition: Stop if non-oracle anchor selection cannot beat uniform block compression by at least 5 percentage points absolute retrieval accuracy at matched budget after three seeds, or if oracle anchors succeed but heuristic/learned anchors fail to identify retrieval points reliably.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-gated-kv-compression-with-exact-retrieval-points-0719ebfa3002`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
