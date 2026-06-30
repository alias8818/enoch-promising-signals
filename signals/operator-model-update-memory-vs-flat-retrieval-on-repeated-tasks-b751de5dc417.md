# Operator-Model Update Memory vs Flat Retrieval on Repeated Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `operator-model-update-memory-vs-flat-retrieval-on-repeated-tasks-b751de5dc417`
Run ID: `operator-model-update-memory-vs-flat-retrieval-on-repeated-tasks-b751de5dc417-20260630T131833521982+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6535d1d4d6f9

## What looked useful

Operator update memory is best interpreted here as a compact sufficient-statistics cache: it does not beat an equivalent flat replay ridge solver on accuracy, but it avoids storing/replaying all examples and beats simple kNN retrieval by 94.79% MAE at the final repeat.

## Boundaries and scale limits

Toy linear operators only: 8 seeds, 48 tasks, 18 repeats, 12-dimensional Gaussian inputs, 4-dimensional outputs, CPU-only single-process run under one minute. No natural-language tasks, LLMs, neural learned memory, non-linear operators, task drift, approximate vector indexes, or production retrieval systems were tested.

## Claim scope

On a synthetic repeated-task benchmark with stable linear task operators and known task IDs, per-task operator update memory matches flat replay ridge accuracy, uses fewer stored floats, and has much lower measured query-time reconstruction cost; it also strongly outperforms flat kNN retrieval on held-out MAE.

## Why it stopped

Bounded synthetic evidence is useful but not publication-grade: the strongest flat replay baseline matches update-memory accuracy, so the result is an efficiency signal rather than a broad predictive-quality win.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen follow-up should test non-linear or drifting task operators with equal storage and latency budgets before considering model-scale work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Nonlinear and drifting repeated-task operator memory under equal retrieval budgets
- Success threshold: At equal or lower storage and query-time budget, update memory achieves at least 20% lower final-repeat MAE than the best bounded flat retrieval baseline on at least two non-linear or drifting task families across 8 or more seeds.
- Stop condition: Stop if all-example replay remains accuracy-equivalent and bounded flat retrieval is within 5% MAE of update memory under equal budgets, or if the update-memory advantage appears only in the already-tested matched linear setting.

## Evidence references

- Artifact root: `<local-path>/projects/operator-model-update-memory-vs-flat-retrieval-on-repeated-tasks-b751de5dc417`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
