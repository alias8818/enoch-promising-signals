# Operator-Doctrine Memory vs Flat Retrieval on Repeated Agent Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-vs-flat-retrieval-on-repeated-agent-tasks-82b33427e799`
Run ID: `operator-doctrine-memory-vs-flat-retrieval-on-repeated-agent-tasks-82b33427e799-20260611T063301820911+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f3e4b47678f8

## What looked useful

Across 500 seeds at paraphrase strength 0.85, doctrine memory reached 1.0000 mean accuracy versus 0.1980 for flat k=5 retrieval, with a 43.19% lower context-token proxy. A 200-seed paraphrase sweep preserved a +0.557 to +0.808 accuracy advantage over flat k=5 retrieval.

## Boundaries and scale limits

Synthetic benchmark only; no real LLM agent, no natural language doctrine induction, no embedding/reranked retrieval baseline, no real operator transcripts, and no long-horizon preference changes.

## Claim scope

In a controlled synthetic repeated-task benchmark with oracle task structure, compact operator-doctrine memory outperformed flat lexical episode retrieval on held-out tasks with paraphrase drift while using a lower context-token proxy than retrieving five full prior episodes.

## Why it stopped

Closed as no-paper useful signal because the positive result is synthetic and oracle-structured rather than direct production-agent evidence.

## Recommended next action

Run a bounded direct LLM-agent follow-up where doctrine must be induced from transcripts and flat retrieval uses embedding/reranking under a matched context budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transcript-Induced Doctrine Memory vs Embedding Retrieval for Repeated Agent Tasks
- Success threshold: Doctrine memory improves held-out task accuracy by at least 10 percentage points over embedding/reranked flat retrieval at equal or lower context cost, with confidence intervals excluding zero.
- Stop condition: Stop if doctrine memory fails to beat the stronger flat retrieval baseline by 5 percentage points on two independent randomized benchmark suites or if doctrine induction accuracy is below 70%.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-flat-retrieval-on-repeated-agent-tasks-82b33427e799`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
