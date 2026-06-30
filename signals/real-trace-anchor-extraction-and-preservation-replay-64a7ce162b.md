# Real-trace anchor extraction and preservation replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-anchor-extraction-and-preservation-replay-64a7ce162b`
Run ID: `real-trace-anchor-extraction-and-preservation-replay-64a7ce162b-20260629T025540604705+0000`

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

- Parent run decision: Realistic agent-trace validation of anchor-preserved memory under noisy writes: enoch://control-plane/projects/realistic-agent-trace-validation-of-anchor-preserved-memor-16d65f1e27/runs/realistic-agent-trace-validation-of-anchor-preserved-memor-16d65f1e27-20260629T021837500067+0000
- Parent run decision: Anchor-Preserved Semantic Memory for Long-Horizon Agent Tasks: enoch://control-plane/projects/anchor-preserved-semantic-memory-for-long-horizon-agent-tasks-dd76e8cb20c3/runs/anchor-preserved-semantic-memory-for-long-horizon-agent-tasks-dd76e8cb20c3-20260629T020214491757+0000

## What looked useful

Anchor extraction achieved 0.9583 mean exact replay versus 0.7222 for the best control, a 0.2361 mean lift, and won all tested token budgets.

## Boundaries and scale limits

No raw/private real traces were available in this project; labels and replay oracle are synthetic/rule-based; no LLM summarizer, embedding retriever, or human-labeled trace export was evaluated.

## Claim scope

On 48 deterministic synthetic real-trace-shaped replay tasks, explicit latest-anchor extraction improved exact replay of buried updated anchors under 48-192 token memory budgets versus no-memory, recency-tail, flat-summary, and simple transcript-search controls.

## Why it stopped

Closed as no-paper useful signal because evidence supports the mechanism only on synthetic/proxy traces, not direct real-trace validation.

## Recommended next action

Run the same harness on 50-100 sanitized real repeated-agent traces with schema-derived or human-reviewed anchor labels before making any real-trace or paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sanitized real-trace anchor replay validation
- Success threshold: Anchor extraction improves mean exact replay by at least 0.10 over the best non-anchor control and wins at least 3 of 4 tested token budgets.
- Stop condition: Stop if labeled real traces cannot be obtained without exposing private payloads, or if anchor extraction lift is below 0.05 versus the best control across two independent trace samples.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-anchor-extraction-and-preservation-replay-64a7ce162b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
