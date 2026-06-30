# Spot-Check Re-Computation Audit for Volunteer Gradient Submissions

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `spot-check-re-computation-audit-for-volunteer-gradient-submissions-e0299b6bf420`
Run ID: `spot-check-re-computation-audit-for-volunteer-gradient-submissions-e0299b6bf420-20260620T060535540398+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bbf53c67e335

## What looked useful

Coordinate spot checks caught dense corruptions but missed most 1% sparse corruptions at tiny budgets; random signed projections detected all tested sparse corruptions with zero observed honest false positives in 400 synthetic trials.

## Boundaries and scale limits

No real volunteer gradient submissions, adaptive adversaries, heterogeneous hardware tolerance study, cryptographic commitment protocol, or end-to-end training impact evaluation were tested.

## Claim scope

Synthetic mechanism-level audit of recomputing random gradient coordinates or random signed projections for logistic-regression gradients with controlled dense and sparse corruptions.

## Why it stopped

Synthetic/proxy evidence only; useful for audit design but not a full validation of volunteer gradient submissions.

## Recommended next action

Stop this run as a no-paper useful signal; next direct validation should replay the same coordinate/projection audit on real or faithfully captured volunteer gradient submissions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay projection and coordinate spot checks on real volunteer gradient traces
- Success threshold: Projection audit detects at least 95% of injected sparse and dense corruptions with less than 1% honest false positives at an audit cost below 5% of full recomputation.
- Stop condition: Stop if real-trace honest false positives exceed 5% after tolerance calibration or projection checks fail to outperform coordinate-only checks at matched recomputation cost.

## Evidence references

- Artifact root: `<local-path>/projects/spot-check-re-computation-audit-for-volunteer-gradient-submissions-e0299b6bf420`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
