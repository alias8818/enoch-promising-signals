# Exact-anchor suffix memory vs flat-vector retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-suffix-memory-vs-flat-vector-retrieval-3bfa05a03872`
Run ID: `exact-anchor-suffix-memory-vs-flat-vector-retrieval-3bfa05a03872-20260620T170002623589+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/982c005a47ec

## What looked useful

Exact anchors behave like keys, not semantic concepts. Route exact-anchor suffix/value questions through exact or hybrid lexical lookup before semantic vector retrieval.

## Boundaries and scale limits

Synthetic in-memory corpus only; no production embedding model, real repeated-agent trace corpus, persistent vector database, approximate nearest-neighbor index, or LLM answer generation was tested.

## Claim scope

In a deterministic synthetic repeated-agent memory benchmark with 1k-10k records and opaque exact anchors, exact-anchor suffix lookup achieved 1.000 accuracy and far lower latency than flat hashed vector scanning; semantic anchor-blind vector retrieval failed, and lexical hash vectors degraded under finite dimensions and anchor-like noise.

## Why it stopped

Useful synthetic mechanism signal, but not publication-grade because production embeddings and real traces were only proxied.

## Recommended next action

Stop this no-paper worker run; run a bounded deepen follow-up on real repeated-agent traces with a production embedding model and exact/hybrid retriever controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace exact-anchor hybrid retrieval vs flat embedding retrieval
- Success threshold: Hybrid or exact-anchor retrieval improves suffix top-1 recall by at least 20 absolute percentage points over flat embedding retrieval on anchor-keyed queries while keeping p95 retrieval latency below 100 ms for the bounded corpus.
- Stop condition: Stop as unsupported if flat embedding retrieval matches exact/hybrid recall within 5 absolute percentage points across anchor-keyed queries or if real traces lack enough opaque anchor/suffix cases for a valid test.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-suffix-memory-vs-flat-vector-retrieval-3bfa05a03872`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
