# Ephemeral optimizer state reconstruction for CPU tiny model training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ephemeral-optimizer-state-reconstruction-for-cpu-tiny-model-training-b61d2e16ec77`
Run ID: `ephemeral-optimizer-state-reconstruction-for-cpu-tiny-model-training-b61d2e16ec77-20260608T021252107987+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/aa1218c962cc

## What looked useful

K=1/K=2 reconstruction matched Adam on the spiral proxy using 0%/50% persistent optimizer-state bytes, but teacher-task results were mixed and short windows capture only 1.0%-7.7% of beta2=0.99 second-moment EMA mass for K=1..8. The mechanism is better viewed as a short-memory adaptive optimizer than standard Adam state reconstruction.

## Boundaries and scale limits

Tested only synthetic MLP classification tasks with thousands of parameters, 3 seeds, and 1200 steps on a CPU worker. No transformer, real corpus, large memory-pressure run, or exact replay-based reconstruction was tested.

## Claim scope

On two NumPy CPU MLP toy tasks, finite-window Adam moment reconstruction can match Adam-like validation metrics in some regimes while reducing persistent optimizer state, but it is not a faithful drop-in reconstruction of standard long-memory Adam moments.

## Why it stopped

Bounded proxy evidence is mixed: the method can work on a toy nonlinear task, but it does not faithfully reconstruct standard Adam second moments and has not been validated on the target tiny-model training setting.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up on a tiny transformer CPU language-model task with direct RSS telemetry before making any broader claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny transformer validation of short-window reconstructed Adam
- Success threshold: K=1 or K=2 reconstructed Adam reaches validation loss within 5% of AdamW at equal tokens while reducing persistent optimizer state by at least 50% and losing no more than 15% throughput.
- Stop condition: Stop if reconstructed variants are more than 10% worse in validation loss after the matched token budget, become unstable in two or more seeds, or memory savings are not observable in direct RSS/allocator telemetry.

## Evidence references

- Artifact root: `<local-path>/projects/ephemeral-optimizer-state-reconstruction-for-cpu-tiny-model-training-b61d2e16ec77`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
