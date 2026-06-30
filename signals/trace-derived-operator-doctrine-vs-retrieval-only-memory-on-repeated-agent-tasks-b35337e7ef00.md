# Trace-derived operator doctrine vs. retrieval-only memory on repeated agent tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-derived-operator-doctrine-vs-retrieval-only-memory-on-repeated-agent-tasks-b35337e7ef00`
Run ID: `trace-derived-operator-doctrine-vs-retrieval-only-memory-on-repeated-agent-tasks-b35337e7ef00-20260629T144345474727+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/237047725527

## What looked useful

Across the main 80-seed held-out recombination test, trace doctrine reached mean F1 0.9352 with zero critical misses, versus retrieval_top1 F1 0.7502 with 0.8649 mean critical misses and retrieval_top3 F1 0.7670 with 0.8621 mean critical misses. Three alternate holdout checks showed the same direction.

## Boundaries and scale limits

Synthetic traces only; no real LLM agent runs, no production corrected-trace corpus, no embedding retrieval stack, and doctrine learner used structured features.

## Claim scope

In a deterministic synthetic repeated-agent-task benchmark with held-out recombinations of operator constraints, trace-derived feature-action doctrine transferred better than retrieval-only memory.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic proxy, not direct validation on real repeated agent tasks.

## Recommended next action

Run a bounded deepen follow-up on 100-300 real or realistic corrected agent traces using text-only doctrine extraction and the target retrieval stack.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Text-only doctrine extraction on real corrected agent traces
- Success threshold: Doctrine reduces critical misses by at least 25% relative to retrieval-top-k and does not reduce precision by more than 5 percentage points on held-out recombinations.
- Stop condition: Stop if doctrine fails the critical-miss threshold on two independently sampled held-out task families or requires privileged labels unavailable in real traces.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-operator-doctrine-vs-retrieval-only-memory-on-repeated-agent-tasks-b35337e7ef00`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
