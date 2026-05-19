# Zero-floor or percentile-scaled sqrt-int8 Adam v-state parity test

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `28`
Project ID: `zero-floor-or-percentile-scaled-sqrt-int8-adam-v-state-par-af0d5936b2`
Run ID: `zero-floor-or-percentile-scaled-sqrt-int8-adam-v-state-par-af0d5936b2-20260516T055402923424+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `28`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Zero-floor or percentile-scaled sqrt-int8 Adam v-state parity test: internal_generated:zero-floor-or-percentile-scaled-sqrt-int8-adam-v-state-par-af0d5936b2

## What looked useful

Allowing sqrt-int8 v-state buckets to quantize to zero repeatedly caused nonfinite updates or severe loss degradation; a one-count floor ablation stayed finite across all 15 runs, indicating that a nonzero reconstructed v floor is a required stabilizer, but that ablation still was not uniformly AdamW-parity.

## Boundaries and scale limits

This run did not test GPT-2-small-class or larger pretraining, long-horizon full-corpus training, fused kernels, distributed training, or memory-throughput benefits; evidence is bounded to small local direct optimizer tests.

## Claim scope

On three deterministic local optimizer-parity workloads with five fixed seeds each, zero-floor and percentile-scaled sqrt-int8 AdamW v-state variants failed to preserve parity against PyTorch AdamW and a matching fp32-v AdamW control.

## Why it stopped

Bounded direct tests falsified zero-floor and percentile-scaled sqrt-int8 Adam v-state parity locally: zero-floor had 0/15 finite runs, percentile p99 had 4/15 finite runs, and percentile p95 failed all transformer seeds and badly degraded the quadratic.

## Recommended next action

Stop this depth-4 follow-up as a no-paper negative result; do not chain another follow-up from this run despite the one-count-floor signal because the controller lineage is already at the cap.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/zero-floor-or-percentile-scaled-sqrt-int8-adam-v-state-par-af0d5936b2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
