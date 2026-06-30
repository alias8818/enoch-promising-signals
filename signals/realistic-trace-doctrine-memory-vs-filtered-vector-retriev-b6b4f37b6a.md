# Realistic Trace Doctrine Memory vs Filtered Vector Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `realistic-trace-doctrine-memory-vs-filtered-vector-retriev-b6b4f37b6a`
Run ID: `realistic-trace-doctrine-memory-vs-filtered-vector-retriev-b6b4f37b6a-20260620T075102478722+0000`

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

- Parent run decision: Semantic Operator Doctrine vs Flat Vector Memory: enoch://control-plane/projects/semantic-operator-doctrine-vs-flat-vector-memory-300142d613e8/runs/semantic-operator-doctrine-vs-flat-vector-memory-300142d613e8-20260620T073742135582+0000
- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/8326b63f3b9a

## What looked useful

Across the primary run and a five-seed sweep, layered_doctrine_memory achieved 1.000 answer accuracy while filtered_vector_retrieval achieved 0.000; failures for filtered retrieval came from retrieving project_fact entries rather than target doctrine.

## Boundaries and scale limits

Generated trace-shaped records only; deterministic retrieval only; no real operator traces, no embedding model, no LLM answerer, no long-horizon deployed agent sessions.

## Claim scope

In a deterministic Tier-1 generated trace benchmark with 60 doctrine-recall cases per seed, explicit doctrine-layer retrieval outperformed metadata-filtered bag-of-words retrieval when project-scoped trace snippets had stronger lexical overlap than durable global doctrine.

## Why it stopped

No-paper useful signal: the controlled direct test supports the mechanism, but generated traces and deterministic retrieval are insufficient for publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up with an embedding-based retriever, layer-aware and layer-blind controls, an LLM answerer, and a small hand-authored trace set before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Embedding and LLM answerer check for layered doctrine memory
- Success threshold: Layered doctrine memory beats the strongest layer-blind filtered embedding baseline by >= 0.15 answer accuracy and >= 0.10 doctrine-compliance accuracy, with no severe regression on project-specific fact recall.
- Stop condition: Stop if the embedding baseline closes the answer-accuracy gap below 0.05 or if LLM answer generation fails to use correctly retrieved doctrine in more than 20% of target cases.

## Evidence references

- Artifact root: `<local-path>/projects/realistic-trace-doctrine-memory-vs-filtered-vector-retriev-b6b4f37b6a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
