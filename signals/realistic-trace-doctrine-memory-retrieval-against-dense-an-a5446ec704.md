# Realistic Trace Doctrine-Memory Retrieval Against Dense and Hybrid Baselines

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `realistic-trace-doctrine-memory-retrieval-against-dense-an-a5446ec704`
Run ID: `realistic-trace-doctrine-memory-retrieval-against-dense-an-a5446ec704-20260619T223604559641+0000`

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

- Parent run decision: Trace-Derived Operator-Doctrine Memory vs Flat Vector Retrieval: enoch://control-plane/projects/trace-derived-operator-doctrine-memory-vs-flat-vector-retrieval-019de88d2a58/runs/trace-derived-operator-doctrine-memory-vs-flat-vector-retrieval-019de88d2a58-20260619T221912110757+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7fe93baac7cb

## What looked useful

Trace/doctrine-memory scoring met the Tier 1 threshold on all five confirmation seeds. Mean trace MRR was 0.5832 vs dense 0.3853 and hybrid 0.2656; mean trace nDCG@5 was 0.5950 vs dense 0.3969 and hybrid 0.2614. Worst-seed trace-minus-hybrid 95% bootstrap lower bounds were +0.2533 MRR and +0.2556 nDCG@5.

## Boundaries and scale limits

Generated corpus only; ideal normalized fields supplied by the generator; no real production traces, no noisy extraction layer, no human relevance labels, and no tuned cross-encoder or domain-specific embedding baseline.

## Claim scope

In a controlled generated incident-trace/doctrine-memory retrieval benchmark with 240 doctrine memories, 432 noisy paraphrased trace queries, MiniLM dense embeddings, and BM25+dense hybrid scoring, a structured trace/doctrine-memory scorer improved MRR and nDCG@5 over dense and hybrid baselines across five seeds.

## Why it stopped

Mechanism supported by Tier 1 controlled direct evidence, but evidence remains no-paper because the benchmark is generated and the trace/doctrine scorer has idealized structured fields.

## Recommended next action

Run a bounded deepen follow-up that replaces ideal generator fields with a noisy trace-field extractor and compares against a tuned hybrid plus cross-encoder reranker on the same controlled benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy Field Extraction Trace-Doctrine Retrieval Against Tuned Hybrid Reranking
- Success threshold: Trace/doctrine-memory with noisy extracted fields beats the best tuned hybrid/reranking baseline by >=0.05 absolute MRR and nDCG@5, with positive 95% bootstrap CI lower bounds on every seed or on the pooled multi-seed query set.
- Stop condition: Stop as no-paper negative if noisy extraction reduces trace/doctrine-memory below the best tuned baseline or if gains disappear under extractor ablation.

## Evidence references

- Artifact root: `<local-path>/projects/realistic-trace-doctrine-memory-retrieval-against-dense-an-a5446ec704`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
