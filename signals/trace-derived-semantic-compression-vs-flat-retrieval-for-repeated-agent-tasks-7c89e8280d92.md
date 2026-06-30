# Trace-Derived Semantic Compression vs Flat Retrieval for Repeated Agent Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-derived-semantic-compression-vs-flat-retrieval-for-repeated-agent-tasks-7c89e8280d92`
Run ID: `trace-derived-semantic-compression-vs-flat-retrieval-for-repeated-agent-tasks-7c89e8280d92-20260620T060612257120+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/09b091fae8ea

## What looked useful

Across 4 noise/change settings, 6 seeds, 80 projects per seed, and top-k budgets 1/3/5/10, compressed retrieval averaged 0.9047 accuracy versus 0.7173 for flat retrieval, with mean indexed token compression to 0.0247 of raw trace tokens.

## Boundaries and scale limits

Synthetic traces only; deterministic field extraction instead of LLM semantic summarization; exact-value retrieval metric instead of downstream agent task success; no real multi-agent or production trace corpus.

## Claim scope

On a deterministic synthetic repeated-agent trace benchmark with noisy and changing project facts, trace-derived compressed memory cards improved exact fact-recovery accuracy over flat raw-event retrieval while reducing indexed trace tokens.

## Why it stopped

No-paper closure: the mechanism is supported by bounded synthetic evidence, but this is proxy-only evidence rather than direct validation on real repeated agent tasks.

## Recommended next action

Run the same flat-vs-compressed comparison on a small real agent trace corpus using LLM-generated memory cards and graded answer/task-success metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace Memory Card Evaluation for Repeated Agent Task Recall
- Success threshold: Compressed memory cards improve graded answer accuracy by at least 10 percentage points over flat retrieval at equal or lower retrieved-token budget on at least 100 held-out real trace queries.
- Stop condition: Stop if memory cards fail to beat flat retrieval by 5 percentage points on the first 50 real held-out queries or require more retrieved tokens than the flat baseline for similar accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-semantic-compression-vs-flat-retrieval-for-repeated-agent-tasks-7c89e8280d92`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
