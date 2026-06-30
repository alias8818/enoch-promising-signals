# Operator-Doctrine Memory vs Fact Memory for CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-vs-fact-memory-for-cpu-agents-412c62ff5218`
Run ID: `operator-doctrine-memory-vs-fact-memory-for-cpu-agents-412c62ff5218-20260619T225952136457+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d95f05653d68

## What looked useful

Main 500-trial run: fact_memory accuracy 0.525, doctrine_memory 0.953, layered_doctrine_memory 0.935. Doctrine minus fact accuracy was +0.428 and layered minus fact was +0.410. Five-seed sensitivity kept the useful-signal threshold true for every seed with mean doctrine minus fact +0.421 and mean layered minus fact +0.403.

## Boundaries and scale limits

Synthetic 10-task replay harness, simulated retrieval and decision policy, no LLM actions, no production operator payloads, no long-horizon persistence, and no full-scale deployment evidence. Doctrine-only slightly exceeded the current layered weighting in this task mix, so the result supports doctrine separation more than this specific layered combiner.

## Claim scope

In a deterministic synthetic CPU-agent replay proxy with noisy/stale retrieval, operator-doctrine memory substantially outperformed fact-only memory on operating-rule decisions; layered doctrine+fact memory also substantially outperformed fact-only memory.

## Why it stopped

Closed as no-paper useful signal because the evidence is reproducible and mechanism-relevant but remains a synthetic proxy rather than direct LLM/production-agent validation.

## Recommended next action

Run a bounded direct replay follow-up using a small LLM or rule-compatible CPU agent over redacted real historical tasks, comparing fact-only, doctrine-only, and doctrine-constrained layered memory with the same decision schema.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU-agent replay of operator-doctrine versus fact memory
- Success threshold: Doctrine-aware memory reduces doctrine violations by >= 25 percentage points versus fact-only retrieval while keeping factual success within 10 percentage points of fact-only or better.
- Stop condition: Stop if doctrine-aware memory fails to reduce doctrine violations by at least 10 percentage points in a smoke set of 30 real replay decisions, or if redacted real tasks cannot be obtained without private/human evidence.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-fact-memory-for-cpu-agents-412c62ff5218`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
