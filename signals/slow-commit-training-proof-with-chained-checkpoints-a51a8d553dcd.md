# Slow-commit training proof with chained checkpoints

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `slow-commit-training-proof-with-chained-checkpoints-a51a8d553dcd`
Run ID: `slow-commit-training-proof-with-chained-checkpoints-a51a8d553dcd-20260610T100658962785+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d02fcf38374a

## What looked useful

The mechanism is locally implementable and reproducible: all calibrated commitment chains verified, deliberate loss tampering was rejected, and overhead scaled monotonically with slow-round difficulty while preserving identical training loss across variants.

## Boundaries and scale limits

Evidence is limited to one small MLP, synthetic linear-teacher data, one GB10 GPU, 600 steps, 30 checkpoint records per variant, and SHA-256-loop slow commits. It does not establish cryptographic security, non-repudiation against an adaptive trainer, efficient verification at large scale, or usefulness for GPT-2-small/large model training.

## Claim scope

On a toy deterministic GPU training task, hash-chained checkpoint commitments with a tunable sequential slow-commit loop can bind an improving optimization trace and detect single-record tampering, with measured overhead from 0.6% at 1,000 rounds to 34.7% at 50,000 rounds for 30 commits over 600 steps.

## Why it stopped

The run provides a bounded toy proof and overhead curve, but it is not direct publication-grade evidence for slow-commit training proofs on realistic model training.

## Recommended next action

Stop this worker run as no-paper useful signal; next bounded action is a GPT-2-small-class or parameter-matched real-data follow-up with adversarial trace editing and verifier-cost measurements.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Slow-commit checkpoint proofs on a GPT-2-small-class training trace
- Success threshold: At least 95% of adversarial edits detected in the tested threat model, all honest chains verify, and overhead remains below 10% for one practical checkpoint cadence over a run long enough to show non-trivial validation-loss improvement.
- Stop condition: Stop if overhead exceeds 25% at every practical cadence, if verifier cost scales worse than linearly in checkpoint count, or if any tested trace edit passes verification without changing the trust assumptions.

## Evidence references

- Artifact root: `<local-path>/projects/slow-commit-training-proof-with-chained-checkpoints-a51a8d553dcd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
