# Memory Doctrine: Do Stores Learn Reusable Operators?

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `memory-doctrine-do-stores-learn-reusable-operators-33800e434a53`
Run ID: `memory-doctrine-do-stores-learn-reusable-operators-33800e434a53-20260621T140942270171+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/55f35adcd078

## What looked useful

Layered doctrine memory reached 1.000 transfer accuracy versus 0.708 for the strongest non-layered raw-memory baseline, with the gain concentrated in renamed-doctrine transfer where raw retrieval had low lexical overlap.

## Boundaries and scale limits

10 seeds, 8 hand-specified operator families, synthetic examples, no LLM, no noisy trace extraction, no real vector/database store, no long-history interference, and no private/operator production data.

## Claim scope

In a deterministic synthetic replay benchmark with generator-provided canonical doctrine keys, layered doctrine memory transferred reusable operators across sparse low-lexical-overlap follow-up tasks better than no-memory, transcript, flat retrieval, and hybrid raw-memory baselines.

## Why it stopped

Synthetic proxy evidence supports the mechanism but does not directly validate real memory stores learning reusable operators.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should replace generator-provided doctrine keys with LLM-extracted doctrine from noisy replay traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy Trace Doctrine Extraction for Reusable Operator Memory
- Success threshold: Layered extracted-doctrine memory improves renamed-doctrine transfer accuracy by at least 0.15 absolute over raw_hybrid_retrieval while keeping wrong-transfer rate below 0.10 across at least 5 seeds.
- Stop condition: Stop as negative if extracted doctrines do not beat raw_hybrid_retrieval by 0.05 absolute on renamed-doctrine transfer or if wrong-transfer rate exceeds 0.25.

## Evidence references

- Artifact root: `<local-path>/projects/memory-doctrine-do-stores-learn-reusable-operators-33800e434a53`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
