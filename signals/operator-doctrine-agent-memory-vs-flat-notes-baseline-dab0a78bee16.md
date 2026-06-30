# Operator-doctrine agent memory vs flat-notes baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `operator-doctrine-agent-memory-vs-flat-notes-baseline-dab0a78bee16`
Run ID: `operator-doctrine-agent-memory-vs-flat-notes-baseline-dab0a78bee16-20260629T195252913227+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1df4e6c7b29e

## What looked useful

Structured memory is useful against raw context truncation and for low-latency doctrine lookup, but the accuracy advantage disappears against a simple recency-aware flat-note retriever in this proxy. Future evaluations should include strong flat-note retrieval controls.

## Boundaries and scale limits

Synthetic symbolic notes only; no LLM-in-the-loop decisions, no human-authored doctrine corpus, no production agent traces, and no vector/BM25 retrieval baseline beyond simple lexical and recency-aware controls.

## Claim scope

On a deterministic synthetic operator-doctrine retrieval benchmark, structured doctrine memory matched the best flat-note hybrid retriever at 100% accuracy, strongly outperformed naive recent-note truncation, and answered roughly 1,241x faster than the hybrid flat-note retriever.

## Why it stopped

Bounded synthetic proxy found mixed evidence: structured memory improves over naive flat notes and latency, but not accuracy versus the strongest flat-note control.

## Recommended next action

Stop this run as no-paper useful signal; next run should test LLM-in-the-loop doctrine compliance against structured memory, recent-note truncation, and strong flat-note retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop operator doctrine memory versus strong flat-note retrieval
- Success threshold: Structured memory achieves at least a 10 percentage point absolute doctrine-compliance gain over the best flat-note retrieval baseline at equal token budget, or equal accuracy with at least 50% lower prompt tokens and no increase in violations.
- Stop condition: Stop if the best flat-note retrieval baseline matches structured memory within 2 percentage points at equal or lower token budget across 500 or more LLM-scored decisions.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-agent-memory-vs-flat-notes-baseline-dab0a78bee16`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
