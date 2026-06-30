# Operator-doctrine memory vs flat vector retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-vs-flat-vector-retrieval-fc0e4875df62`
Run ID: `operator-doctrine-memory-vs-flat-vector-retrieval-fc0e4875df62-20260621T015827126028+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/736bfc6bce23

## What looked useful

The result isolates a plausible failure mode for flat vector retrieval: retrieval can include the correct doctrine in top-k while top-ranked lexical decoys or non-operative historical notes dominate answer selection. Encoding doctrine as typed rules with priority resolves that constructed failure mode.

## Boundaries and scale limits

Synthetic proxy only; no real doctrine corpus, learned embeddings, LLM context-reader baseline, human-authored query set, production latency measurement, or large-scale robustness validation was run.

## Claim scope

On a deterministic synthetic doctrine benchmark with typed applicability constraints, priority rules, and lexically similar non-operative decoys, structured operator-doctrine memory achieved 100% exact-action accuracy while flat TF-IDF top-1 action selection achieved 0.33%, even though the expected operative rule appeared in flat top-5 for 100% of queries. In a no-decoy control, both methods achieved 100%.

## Why it stopped

Closed as no-paper useful signal because current evidence is a synthetic proxy, not direct publication-grade validation on real doctrine corpora or modern embedding/LLM retrieval stacks.

## Recommended next action

Run a bounded real-corpus follow-up using 50-100 manually curated doctrine/rule excerpts with superseded and exception cases, comparing embedding retrieval plus LLM answer synthesis against structured doctrine-memory resolution.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus doctrine memory vs embedding RAG on superseded and exception rules
- Success threshold: Structured doctrine memory improves exact operative-action accuracy by at least 15 percentage points over the best embedding+LLM baseline while preserving at least 95% citation coverage of the gold applicable rule.
- Stop condition: Stop if embedding+LLM with metadata filtering reaches within 5 percentage points of structured memory or if structured rule extraction cannot be audited reliably on at least 90% of the curated corpus.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-flat-vector-retrieval-fc0e4875df62`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
