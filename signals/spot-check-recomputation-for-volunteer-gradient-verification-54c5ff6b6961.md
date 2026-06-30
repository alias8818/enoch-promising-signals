# Spot-Check Recomputation for Volunteer Gradient Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `spot-check-recomputation-for-volunteer-gradient-verification-54c5ff6b6961`
Run ID: `spot-check-recomputation-for-volunteer-gradient-verification-54c5ff6b6961-20260619T025300552367+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2fb0acef370f

## What looked useful

Spot-check recomputation is useful as a component defense for broad gradient corruption, but the bounded experiment shows it is not a standalone low-overhead guarantee: at q=0.10, whole-volunteer attacks had 0.993-1.000 bad-round detection while sparse one-shard attacks had only 0.450 bad-round detection and 0.104 bad-shard rejection.

## Boundaries and scale limits

Synthetic CPU-only gradients, no real distributed system, no large-model bandwidth or nondeterminism effects, no adaptive cross-round adversary, no real volunteer churn or privacy constraints.

## Claim scope

In a 300-round synthetic logistic-regression simulation with 64 volunteers, 8 shards per volunteer, and exact recomputation, independent spot-checking plus whole-volunteer round rejection detects broad volunteer corruption well at 10-20% recomputation overhead but is weak against sparse one-shard corruption.

## Why it stopped

Bounded local evidence found a useful mechanism and a clear standalone failure mode; this is not full validation of volunteer gradient verification and is not paper-ready.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should add cross-round reputation or redundancy and test whether it closes the sparse-corruption failure mode without exceeding 10-20% recomputation overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cross-round reputation for sparse volunteer gradient corruption
- Success threshold: For sparse one-shard corruption with 10% bad volunteers, achieve at least 0.90 bad-round detection and at least 0.70 bad-volunteer detection at no more than 0.20 recomputation overhead, without increasing clean-volunteer false rejection above 0.02.
- Stop condition: Stop if reputation or targeted rechecks cannot exceed 0.70 sparse bad-round detection at 0.20 overhead, or if clean-volunteer false rejection exceeds 0.05 in benign/noisy runs.

## Evidence references

- Artifact root: `<local-path>/projects/spot-check-recomputation-for-volunteer-gradient-verification-54c5ff6b6961`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
