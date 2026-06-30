# Evidence ledger in a live retrieval-augmented agent workflow

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-in-a-live-retrieval-augmented-agent-workfl-ce8e96068f`
Run ID: `evidence-ledger-in-a-live-retrieval-augmented-agent-workfl-ce8e96068f-20260613T094429850793+0000`

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

- Parent run decision: Evidence Ledger for Agent Reliability: enoch://control-plane/projects/evidence-ledger-for-agent-reliability-b1c8740df42c/runs/evidence-ledger-for-agent-reliability-b1c8740df42c-20260613T091954999176+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f0a4cc9efb5b

## What looked useful

A persistent ledger for source, credibility, and effective-time evidence selection produced a reproducible local signal: 0.687 answer/citation accuracy versus 0.295/0.286 for the best rolling-context baseline on 1000 controlled episodes, with sensitivity runs showing the benefit persists through 40% update miss probability but not 70%.

## Boundaries and scale limits

Synthetic corpus and deterministic extraction only; no real vector store, production RAG traces, LLM extraction errors, human citation grading, or long-running deployment behavior. The mechanism fails the threshold under severe authoritative-update retrieval misses, showing it does not solve retrieval recall.

## Claim scope

In a controlled synthetic live-RAG workflow with stale records, low-credibility contradictions, distractors, and authoritative updates, a structured evidence ledger improved answer accuracy and citation validity over rolling-context baselines by 39.2 and 40.1 percentage points in the primary Tier 1 run.

## Why it stopped

Tier 1 controlled direct mechanism test completed and supports a useful no-paper signal, but evidence remains synthetic and not publication-grade.

## Recommended next action

Run a bounded deepen follow-up using a real vector-store plus LLM RAG trace and the same ledger-vs-baseline answer accuracy and citation validity metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate evidence ledger on real LLM/vector-store RAG traces
- Success threshold: At least 100 real-trace episodes; evidence ledger improves citation-supported answer accuracy by >=15 percentage points versus the best baseline and keeps unsupported answer rate no higher than baseline.
- Stop condition: Stop if the ledger improves citation-supported accuracy by <5 percentage points or increases unsupported answers by >5 percentage points after the fixed 100-episode evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-in-a-live-retrieval-augmented-agent-workfl-ce8e96068f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
