# Trace-Derived Operator-Doctrine Memory vs Flat Vector Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-derived-operator-doctrine-memory-vs-flat-vector-retrieval-019de88d2a58`
Run ID: `trace-derived-operator-doctrine-memory-vs-flat-vector-retrieval-019de88d2a58-20260619T221912110757+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7fe93baac7cb

## What looked useful

Across 5,000 synthetic queries and five seeds, doctrine memory improved MRR from 0.4598 to 0.9613 and Recall@1 from 0.3012 to 0.9234 versus flat TF-IDF; paraphrase queries showed Recall@1 improvement from 0.1667 to 0.9252.

## Boundaries and scale limits

Synthetic traces only; hand-authored doctrine alias table; lexical TF-IDF baseline only; no real operator logs, learned doctrine extraction, dense embedding baseline, or production retrieval stack.

## Claim scope

In a deterministic synthetic trace benchmark where multiple doctrine traces share the same operational scenario context, a structured doctrine-memory retriever with trace-derived fields and doctrine aliases outperforms flat raw-text TF-IDF retrieval for paraphrased doctrine-intent queries.

## Why it stopped

Stopped at useful-signal closure because the current evidence is a bounded synthetic proxy, not direct real-trace validation.

## Recommended next action

Run a bounded direct follow-up using realistic operator traces, learned doctrine extraction, and dense/hybrid retrieval baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic Trace Doctrine-Memory Retrieval Against Dense and Hybrid Baselines
- Success threshold: Doctrine-memory retrieval improves Recall@1 by at least 10 percentage points over the best dense or hybrid baseline on held-out paraphrased doctrine queries, with no more than a 5 percentage point Recall@5 regression.
- Stop condition: Stop as negative if doctrine memory fails to beat the strongest dense/hybrid baseline on Recall@1 or if gains disappear under noisy doctrine extraction.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-operator-doctrine-memory-vs-flat-vector-retrieval-019de88d2a58`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
