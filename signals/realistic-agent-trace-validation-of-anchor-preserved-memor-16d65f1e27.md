# Realistic agent-trace validation of anchor-preserved memory under noisy writes

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `realistic-agent-trace-validation-of-anchor-preserved-memor-16d65f1e27`
Run ID: `realistic-agent-trace-validation-of-anchor-preserved-memor-16d65f1e27-20260629T021837500067+0000`

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

- Parent run decision: Anchor-Preserved Semantic Memory for Long-Horizon Agent Tasks: enoch://control-plane/projects/anchor-preserved-semantic-memory-for-long-horizon-agent-tasks-dd76e8cb20c3/runs/anchor-preserved-semantic-memory-for-long-horizon-agent-tasks-dd76e8cb20c3-20260629T020214491757+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ed224b707225

## What looked useful

At noise_rate 0.55, anchor_preserved_memory achieved 1.000 exact-answer rate versus 0.037 for flat_retrieval and transcript_search, with conflict error reduced by 0.963 absolute. The mechanism works in the oracle-anchor synthetic setting but is not paper-ready.

## Boundaries and scale limits

Synthetic traces only; no real agent logs, no LLM extraction errors, no embedding retrieval baseline, no persistence stress beyond local JSON artifacts, and no multi-day or multi-user memory store.

## Claim scope

In a deterministic synthetic repeated-agent trace task with explicit user-anchor labels, anchor-preserved memory prevented noisy overwrite corruption and preserved all four required anchors across 600 episodes per noise level.

## Why it stopped

Synthetic proxy evidence supports the mechanism but does not constitute full real-agent trace validation.

## Recommended next action

Stop this run as no-paper useful signal; next, run the same protocol on real or human-written agent traces with non-oracle anchor extraction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace anchor extraction and preservation replay
- Success threshold: At least 20 percentage point absolute exact-answer improvement over the strongest baseline at a realistic noisy-write rate, with lower conflict error and no more than 5 percentage point increase in missing-anchor errors.
- Stop condition: Stop if anchor extraction F1 is below 0.80 on the replay corpus or if anchor-preserved memory fails to beat the strongest baseline by 10 percentage points in exact-answer rate.

## Evidence references

- Artifact root: `<local-path>/projects/realistic-agent-trace-validation-of-anchor-preserved-memor-16d65f1e27`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
