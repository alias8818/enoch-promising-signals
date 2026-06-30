# Sanitized real-trace anchor replay validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `63`
Project ID: `sanitized-real-trace-anchor-replay-validation-fcebb68f4d`
Run ID: `sanitized-real-trace-anchor-replay-validation-fcebb68f4d-20260629T031619390293+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `63`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 10, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- weak evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Realistic agent-trace validation of anchor-preserved memory under noisy writes: enoch://control-plane/projects/realistic-agent-trace-validation-of-anchor-preserved-memor-16d65f1e27/runs/realistic-agent-trace-validation-of-anchor-preserved-memor-16d65f1e27-20260629T021837500067+0000
- Parent run decision: Real-trace anchor extraction and preservation replay: enoch://control-plane/projects/real-trace-anchor-extraction-and-preservation-replay-64a7ce162b/runs/real-trace-anchor-extraction-and-preservation-replay-64a7ce162b-20260629T025540604705+0000

## What looked useful

A deterministic anchor replay harness now exists and shows that explicit layered anchor weighting can resolve a noisy metadata collision missed by transcript and flat retrieval baselines.

## Boundaries and scale limits

No actual sanitized real-trace corpus was present in the workspace; evidence is synthetic fixture-level and CPU-only, not production trace validation.

## Claim scope

On an 8-task local sanitized replay fixture, layered doctrine memory recovered all expected anchors and outperformed transcript_search and flat_retrieval by one task.

## Why it stopped

Proxy-only early result: the scaffold contained placeholder data, so this run can validate the harness mechanism but not the mission-level real-trace claim.

## Recommended next action

Run this harness on at least 50 independently labeled sanitized real-trace replay tasks before making any real-trace validation claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out sanitized real-trace anchor replay confirmation
- Success threshold: layered_doctrine_memory exact-anchor accuracy is at least 0.10 absolute higher than both transcript_search and flat_retrieval on at least 50 held-out real-trace tasks.
- Stop condition: Stop as negative if layered_doctrine_memory does not beat both baselines by at least 0.05 absolute after 50 labeled real-trace tasks or if labels cannot be independently established.

## Evidence references

- Artifact root: `<local-path>/projects/sanitized-real-trace-anchor-replay-validation-fcebb68f4d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
