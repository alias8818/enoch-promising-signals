# Operator-Doctrine Memory Beats Flat Vector Retrieval on Repeated Multi-Turn Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-beats-flat-vector-retrieval-on-repeated-multi-turn-tasks-7b99d40be8c8`
Run ID: `operator-doctrine-memory-beats-flat-vector-retrieval-on-repeated-multi-turn-tasks-7b99d40be8c8-20260629T152901995504+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/65a9515b260a

## What looked useful

Layered doctrine memory reached 1.0000 slot accuracy and exact-match rate at top_k=8; flat global retrieval reached 0.1715 slot accuracy and 0.0000 exact-match rate; flat operator-scoped retrieval reached 0.1125 slot accuracy and 0.0000 exact-match rate. Top-k sensitivity at 4 and 16 preserved large layered advantages.

## Boundaries and scale limits

No 7B model, learned memory writer, embedding model, real operator trace corpus, production metadata, or live multi-turn agent loop was tested. Evidence is limited to a stdlib TF-IDF/rule-extraction proxy over 288 generated tasks.

## Claim scope

In a deterministic synthetic repeated-task proxy with noisy transcripts, one-off overrides, and cross-operator distractors, separating stable operator doctrine from flat transcript retrieval improved doctrine-slot recall over flat global and operator-scoped vector-style retrieval.

## Why it stopped

Stopped as a useful no-paper result because the evidence is synthetic/proxy-only and does not validate the original 7B or real repeated-operator-task claim.

## Recommended next action

Run a bounded direct-evidence follow-up using real or LLM-generated multi-turn traces, embedding retrieval, reranking controls, LLM answer synthesis, and imperfect doctrine extraction labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Trace Doctrine Memory vs Reranked Flat Retrieval
- Success threshold: Layered doctrine memory beats the strongest flat/reranked baseline by at least 10 percentage points in slot accuracy and exact-match rate across at least three seeds or corpus splits.
- Stop condition: Stop if the strongest flat/reranked baseline is within 5 percentage points of layered memory on both slot accuracy and exact-match rate, or if doctrine extraction noise removes the layered advantage.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-beats-flat-vector-retrieval-on-repeated-multi-turn-tasks-7b99d40be8c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
