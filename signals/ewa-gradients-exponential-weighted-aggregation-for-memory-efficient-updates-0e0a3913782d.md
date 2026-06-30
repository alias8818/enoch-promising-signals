# EWA Gradients: Exponential Weighted Aggregation for Memory-Efficient Updates

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `ewa-gradients-exponential-weighted-aggregation-for-memory-efficient-updates-0e0a3913782d`
Run ID: `ewa-gradients-exponential-weighted-aggregation-for-memory-efficient-updates-0e0a3913782d-20260605T200915199764+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/65dfebca2186

## What looked useful

EWA gradient EMA is numerically identical to classical momentum under learning-rate scaling, with the same one-buffer optimizer-state footprint. Replacing arithmetic microbatch averaging with exponential weighting produced about 38% relative gradient error and strong order dependence in the bounded probe.

## Boundaries and scale limits

No transformer-scale or real-corpus training was run; memory was assessed by optimizer-state slot accounting plus process RSS, not by framework allocator telemetry on a large model.

## Claim scope

Bounded NumPy evidence for EWA gradients implemented as either an optimizer gradient EMA or an exponential microbatch aggregation rule on synthetic softmax classification and random-gradient equivalence tests.

## Why it stopped

Early bounded falsification: the optimizer interpretation reduces to known momentum, while the virtual-batch interpretation changes the target gradient with substantial order-dependent bias. This is not a full-scale transformer validation.

## Recommended next action

Stop this line unless a new EWA variant is specified that is not algebraically equivalent to momentum and has a concrete memory mechanism beyond one full-size gradient aggregate buffer.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/ewa-gradients-exponential-weighted-aggregation-for-memory-efficient-updates-0e0a3913782d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
