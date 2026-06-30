# Doctrinal Memory vs Retrieval-Only on Repeated Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `doctrinal-memory-vs-retrieval-only-on-repeated-tasks-8281f76b813a`
Run ID: `doctrinal-memory-vs-retrieval-only-on-repeated-tasks-8281f76b813a-20260628T210431921141+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9213839e1be7

## What looked useful

Across 25 seeds, 20 tasks per seed, and 120 held-out tests per task, doctrinal memory reached 0.9481 to 0.9981 mean accuracy from 1 to 5 shots, matching retrieval-plus-induction within about 0.1 percentage points while reducing median prediction latency from 9.64-36.71 us to about 0.18 us and keeping memory at 20 rules instead of 20-100 exemplars.

## Boundaries and scale limits

Synthetic DSL only; no real LLM, natural-language tasks, noisy task identification, learned neural memory, large retrieval corpus, or serving-system benchmark was tested.

## Claim scope

On synthetic recurring string-transformation tasks with task labels and a fixed rule DSL, persistent doctrinal rule memory matches retrieval-plus-query-time-induction accuracy while using constant task-level memory and much lower prediction latency; pure nearest-exemplar retrieval fails on fresh inputs.

## Why it stopped

No-paper closure: this is a synthetic proxy useful signal, not direct publication-grade evidence for real doctrinal memory systems.

## Recommended next action

Run a bounded real LLM/agent repeated-instruction benchmark comparing retrieved traces against distilled doctrines under matched context and storage budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM Repeated-Instruction Doctrine vs Trace Retrieval
- Success threshold: Doctrine matches or exceeds retrieval-plus-reasoning accuracy within 1 percentage point while reducing context tokens or latency by at least 30% on held-out repeated tasks.
- Stop condition: Stop if doctrine accuracy is more than 3 percentage points below retrieval-plus-reasoning or if context/latency savings are below 10% under matched budgets.

## Evidence references

- Artifact root: `<local-path>/projects/doctrinal-memory-vs-retrieval-only-on-repeated-tasks-8281f76b813a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
