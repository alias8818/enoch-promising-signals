# Layered Memory Compression vs Flat Retrieval for Agent Task Reuse

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-compression-vs-flat-retrieval-for-agent-task-reuse-f0e90d68946c`
Run ID: `layered-memory-compression-vs-flat-retrieval-for-agent-task-reuse-f0e90d68946c-20260610T200243099877+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7baa2397cd09

## What looked useful

Across 32 seed/train-size conditions, layered compressed memory achieved 0.4600 mean step accuracy versus 0.0501 for the best flat baseline, used 6.97% as many memory tokens as flat k=5 on average, and beat the best flat baseline in every condition.

## Boundaries and scale limits

Synthetic generator only; no real agent traces, no LLM summarization errors, no deployed task-completion loop, and no large heterogeneous corpus. Exact full-plan reconstruction remained low.

## Claim scope

In a synthetic held-out task-composition benchmark with reusable primitive procedures and deterministic TF-IDF retrieval, compressed primitive-level layered memory recovered substantially more reusable steps than flat whole-episode retrieval while using fewer memory tokens.

## Why it stopped

No-paper closure: the result is a useful bounded synthetic mechanism signal, not direct publication-grade evidence for real agent task reuse.

## Recommended next action

Run a bounded deepen follow-up on real or LLM-generated agent traces with matched storage budgets and downstream plan/task-completion metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layered Memory Compression on Realistic Agent Trace Reuse
- Success threshold: Layered memory improves downstream plan correctness or task completion by at least 10 absolute percentage points over the best flat baseline at equal memory budget across at least three seeds or task-family splits.
- Stop condition: Stop if layered memory fails to beat the best flat baseline by 5 absolute percentage points on downstream metrics or if compression errors erase the synthetic advantage under equal budgets.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-compression-vs-flat-retrieval-for-agent-task-reuse-f0e90d68946c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
