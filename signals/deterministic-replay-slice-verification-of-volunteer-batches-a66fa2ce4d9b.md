# Deterministic Replay-Slice Verification of Volunteer Batches

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `deterministic-replay-slice-verification-of-volunteer-batches-a66fa2ce4d9b`
Run ID: `deterministic-replay-slice-verification-of-volunteer-batches-a66fa2ce4d9b-20260613T034332009766+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/908164cba090

## What looked useful

Replay-slice verification is mechanically viable when tasks are deterministic and canonicalized, but slice rate must be chosen from expected corruption density because low replay rates provide weak sparse-fault coverage.

## Boundaries and scale limits

No real volunteer payloads, hardware heterogeneity, adversarial behavior, privacy-safe payload reference flow, or production scheduler integration were tested. The evidence is synthetic and CPU-local.

## Claim scope

In a synthetic deterministic replay proxy with 500 batches of 200 records across 60 conditions, stable hash replay slices detected selected corrupt records with zero clean-batch false positives; dense corruption was detected reliably at moderate slice rates, while sparse corruption was often missed at cheap slice rates.

## Why it stopped

Synthetic proxy evidence is useful but insufficient for a production or paper-positive claim.

## Recommended next action

Stop this run as no-paper useful signal; next direct test should replay privacy-safe real volunteer batch traces with pre-registered detection and cost thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay-slice verification on privacy-safe real volunteer traces
- Success threshold: At 10% replay slice, detect at least 95% of batches with >=20% corrupted records, keep clean-batch false positives below 1%, and show deterministic replay agreement above 99.5% on clean real traces.
- Stop condition: Stop if clean real traces cannot be replayed deterministically above 99.5% agreement after environment canonicalization, or if privacy-safe replay inputs cannot be obtained.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-replay-slice-verification-of-volunteer-batches-a66fa2ce4d9b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
