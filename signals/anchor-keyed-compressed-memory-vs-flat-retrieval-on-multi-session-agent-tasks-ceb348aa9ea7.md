# Anchor-Keyed Compressed Memory vs Flat Retrieval on Multi-Session Agent Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-keyed-compressed-memory-vs-flat-retrieval-on-multi-session-agent-tasks-ceb348aa9ea7`
Run ID: `anchor-keyed-compressed-memory-vs-flat-retrieval-on-multi-session-agent-tasks-ceb348aa9ea7-20260613T015419652438+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/db5f0839bd52

## What looked useful

Anchor-keyed compressed memory only beat flat retrieval when the flat top-k context budget was smaller than the number of required facts; with enough top-k, exact BM25 reached 1.000 accuracy.

## Boundaries and scale limits

CPU-only pure-Python benchmark; no LLM answering, no noisy extraction, no aliases, no conflicting updates, no real agent transcripts, and no production retrieval index.

## Claim scope

Synthetic oracle-scored multi-session memory benchmark with exact anchor IDs and deterministic fact extraction.

## Why it stopped

Proxy synthetic evidence is mixed: it supports a context-budget mechanism but does not validate a broad advantage over flat retrieval.

## Recommended next action

Stop this run as no-paper useful signal; deepen only with a bounded noisy-extraction LLM benchmark before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy LLM Extraction Test for Anchor-Keyed Memory
- Success threshold: At matched context budget, anchor-keyed memory improves answer accuracy by at least 10 percentage points over flat retrieval while keeping extraction/update error below 5%.
- Stop condition: Stop if flat retrieval is within 5 percentage points at all tested budgets or if extraction/update errors erase the compression advantage.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-keyed-compressed-memory-vs-flat-retrieval-on-multi-session-agent-tasks-ceb348aa9ea7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
