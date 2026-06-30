# Volunteer CPU Training with Proof-of-Work Validation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `volunteer-cpu-training-with-proof-of-work-validation-282add10f43f`
Run ID: `volunteer-cpu-training-with-proof-of-work-validation-282add10f43f-20260613T063621968504+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e553faf733bb

## What looked useful

Proof-of-work is cheap to verify and costly to solve, but PoW-only validation accepted malicious training updates at the same rate as honest updates. Correctness came from a separate audit-loss check, not from PoW.

## Boundaries and scale limits

No real volunteer network, large model, privacy-preserving validation, or adaptive adversary was tested; evidence is local synthetic CPU-only.

## Claim scope

Synthetic logistic-regression volunteer-training simulator with SHA-256 Hashcash-style proof-of-work over model and update hashes.

## Why it stopped

Bounded proxy/early falsification: the local simulator directly tested PoW-only acceptance and found it cannot distinguish harmful from honest updates.

## Recommended next action

Stop treating PoW alone as a training validator; use it only as rate-limit/Sybil-cost accounting unless paired with a training-aware audit or cryptographic verification protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PoW plus semantic audit for volunteer CPU training
- Success threshold: PoW+audit rejects at least 95% of harmful updates with less than 5% honest rejection and less than 20% throughput loss versus audit-only on the bounded task.
- Stop condition: Stop if audit rejection is bypassed by the adaptive adversary above 20% malicious acceptance or if PoW overhead dominates useful training throughput.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-cpu-training-with-proof-of-work-validation-282add10f43f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
