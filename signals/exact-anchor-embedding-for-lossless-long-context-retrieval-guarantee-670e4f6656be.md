# Exact Anchor Embedding for Lossless Long-Context Retrieval Guarantee

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `exact-anchor-embedding-for-lossless-long-context-retrieval-guarantee-670e4f6656be`
Run ID: `exact-anchor-embedding-for-lossless-long-context-retrieval-guarantee-670e4f6656be-20260602T143054599181+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a991488e6086

## What looked useful

A 1536-dim float32 embedding can losslessly encode at most 3148 tokens from a 50000-token vocabulary under a finite-state counting bound; 4096 dims can encode at most 8396 tokens. A 16384-token context requires at least 7993 float32 dimensions, and a 1000000-token context requires at least 487802. Compressed anchor-code simulations show birthday-bound collisions that break exact retrieval unless an external exact table is retained; the exact-table positive control remains 100% because it stores the mapping.

## Boundaries and scale limits

CPU-only standard-library experiment; no neural model training, no semantic retrieval benchmark, and no datacenter-scale long-context serving test. The result is sufficient against the broad fixed-size lossless guarantee but not against narrower bounded-index designs with storage that scales with context.

## Claim scope

Early falsification of the strong claim that a fixed-size finite-precision anchor embedding can guarantee lossless retrieval for arbitrary long contexts without an auxiliary exact index/table. Evidence covers finite-state capacity bounds and salted hash-code collision simulations, not trained neural retrieval quality.

## Why it stopped

Proxy/early falsification: finite-precision capacity bounds and collision simulations refute the broad fixed-size lossless embedding guarantee, though they do not constitute full neural-system validation.

## Recommended next action

Stop this broad claim as an early/proxy negative; a future bounded result should restate the method as an exact anchor index with storage that scales with context and prove limits for a specified maximum context, vocabulary, precision, and storage budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded Exact Anchor Index With Explicit Storage Scaling
- Success threshold: For a fixed stated budget, exact anchor lookup recovers 100% of inserted spans across at least 1 million synthetic anchors and a real text corpus sample, while reporting storage overhead and latency; semantic embedding components are not credited with lossless recovery unless they recover exactly without the table.
- Stop condition: Stop if the design cannot maintain 100% exact recovery without unbounded hidden state, or if storage/latency reduces to an ordinary exact key-value index with no distinct mechanism beyond standard indexing.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-embedding-for-lossless-long-context-retrieval-guarantee-670e4f6656be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
