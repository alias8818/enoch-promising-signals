# Operator-Doctrine Memory vs Flat Retrieval for Repeated Agent Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-vs-flat-retrieval-for-repeated-agent-tasks-1fd703e1aa22`
Run ID: `operator-doctrine-memory-vs-flat-retrieval-for-repeated-agent-tasks-1fd703e1aa22-20260610T110420807195+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b3efcd0e635c

## What looked useful

Doctrine memory achieved 65.595% mean accuracy versus 52.575% for flat retrieval in the stable condition, with 29.16% lower mean context proxy and 26.2x faster prediction. With doctrine drift at task 1,000, doctrine memory achieved 49.72% versus 42.015% for flat retrieval, but both degraded sharply immediately after drift.

## Boundaries and scale limits

Synthetic symbolic tasks only; no natural-language retrieval, no tuned vector index, no LLM-in-the-loop decisions, no real operator traces, and only 10 seeds x 2,000 tasks per condition.

## Claim scope

In a synthetic online repeated-task benchmark with stable seeded operator doctrine, compact doctrine memory outperformed simple flat Jaccard episode retrieval on accuracy, context-footprint proxy, and prediction latency; under one abrupt drift condition it still outperformed overall but remained brittle immediately after drift.

## Why it stopped

No-paper closure: the result is useful synthetic evidence for the mechanism, but not direct publication-grade validation of operator-doctrine memory in real repeated agent tasks.

## Recommended next action

Run a bounded direct-evidence follow-up using real or LLM-generated repeated agent traces, a tuned vector-retrieval baseline, and an explicit doctrine-memory update method with drift handling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Based Doctrine Memory vs Tuned Flat Retrieval
- Success threshold: Doctrine memory improves mean online accuracy by at least 5 percentage points over tuned flat retrieval while using at least 25% fewer context tokens, and recovers to within 10 percentage points of pre-drift accuracy within 200 post-drift tasks when drift is present.
- Stop condition: Stop if tuned flat retrieval matches doctrine memory within 2 percentage points at comparable context budget, or if doctrine memory fails to recover after drift in two independent trace shards.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-flat-retrieval-for-repeated-agent-tasks-1fd703e1aa22`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
