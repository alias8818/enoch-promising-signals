# Real-data containment-aware volunteer dedup candidate validation

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `73`
Project ID: `real-data-containment-aware-volunteer-dedup-candidate-vali-8543c3ff2c`
Run ID: `real-data-containment-aware-volunteer-dedup-candidate-vali-8543c3ff2c-20260522T101804314993+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `73`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Containment-aware candidate generation for volunteer dedup: enoch://control-plane/projects/containment-aware-candidate-generation-for-volunteer-dedup-8bd963ce81/runs/containment-aware-candidate-generation-for-volunteer-dedup-8bd963ce81-20260522T073224464611+0000
- Parent run decision: Two-stage MinHash plus exact-containment volunteer dedup validation: enoch://control-plane/projects/two-stage-minhash-plus-exact-containment-volunteer-dedup-v-81c68575ba/runs/two-stage-minhash-plus-exact-containment-volunteer-dedup-v-81c68575ba-20260522T061525530247+0000

## What looked useful

Across missingness rates 0.0, 0.3, and 0.6, containment_adaptive achieved candidate recall 0.9996, 0.9889, and 0.9311 versus 0.8260, 0.6853, and 0.5167 for the strongest ordinary union-blocking baseline. Pair reduction remained above 99.7% in all settings.

## Boundaries and scale limits

Single public benchmark; volunteer/contact-list containment was modeled by seeded missingness on real records rather than measured on a real volunteer CRM dataset; no MinHash/LSH or learned-blocking production baselines; no external replication.

## Claim scope

On the FEBRL4 real person-record linkage benchmark with seeded partial-record ablations, adaptive containment-aware candidate generation improves true duplicate candidate recall over fixed blocking and sorted-neighborhood baselines while retaining high pair reduction.

## Why it stopped

The run produced useful bounded mechanism evidence but did not meet Tier 4 paper-readiness because the volunteer-specific containment condition was simulated on FEBRL4 rather than validated on real volunteer data.

## Recommended next action

Stop this depth-4 follow-up chain; do not claim paper readiness without an actual volunteer/contact dedup dataset and external baseline replication.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-data-containment-aware-volunteer-dedup-candidate-vali-8543c3ff2c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
