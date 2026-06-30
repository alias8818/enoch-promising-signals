# Random Replay Audit for Lazy-Worker Detection in CPU Volunteer Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `random-replay-audit-for-lazy-worker-detection-in-cpu-volunteer-pretraining-0af8e3937c54`
Run ID: `random-replay-audit-for-lazy-worker-detection-in-cpu-volunteer-pretraining-0af8e3937c54-20260621T002702161079+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/871b7fc1a29f

## What looked useful

Random replay audit is locally viable only with an absolute tolerance floor; a relative-only threshold caused high false positives near small gradients, while the corrected threshold gave 100% mean detection at audit rates >=5% and exposed weak coverage at 1% for stale/zero replay.

## Boundaries and scale limits

Synthetic proxy only; not real language-model pretraining, not multi-node volunteer infrastructure, and not tested against adaptive partial-compute, colluding, non-IID, compressed-update, or audit-distribution-aware adversaries.

## Claim scope

In a synthetic 64-dimensional linear-gradient CPU volunteer proxy with 50 workers, 20% lazy workers, 500 rounds, and four cheap lazy-submit strategies, random replay audits with a norm-aware threshold and absolute tolerance floor detected all tested lazy strategies at audit rates of 5% or higher with zero observed honest-worker false positives.

## Why it stopped

Closed as no-paper useful signal: evidence is reproducible and mechanism-level, but proxy-only and insufficient for publication-grade validation.

## Recommended next action

Run a bounded toy distributed language-model pretraining test with the absolute-floor verifier, no-audit and deterministic-audit controls, and adaptive lazy workers before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Toy LM Random Replay Audit With Adaptive Lazy Workers
- Success threshold: At <=5% audit rate, detect >=95% of lazy workers within 500 worker assignments, honest-worker false positives <=0.5% per audit, audit overhead <=10%, and final validation loss no worse than 2% relative to honest/no-lazy control.
- Stop condition: Stop if false positives exceed 1% per honest audit after threshold calibration, detection stays below 80% for adaptive lazy workers, or audit overhead exceeds 20% in the toy trainer.

## Evidence references

- Artifact root: `<local-path>/projects/random-replay-audit-for-lazy-worker-detection-in-cpu-volunteer-pretraining-0af8e3937c54`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
