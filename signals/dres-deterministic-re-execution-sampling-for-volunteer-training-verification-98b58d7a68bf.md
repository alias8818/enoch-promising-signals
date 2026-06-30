# DRES: Deterministic Re-Execution Sampling for Volunteer Training Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dres-deterministic-re-execution-sampling-for-volunteer-training-verification-98b58d7a68bf`
Run ID: `dres-deterministic-re-execution-sampling-for-volunteer-training-verification-98b58d7a68bf-20260614T043751971992+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9ba846459ffd

## What looked useful

DRES works as a replay-and-sample mechanism when honest replay is exact and tolerance is tighter than attack deviation; 5% sampling detected all synthetic attack trials in the sweep at about 5-6% replay overhead. A tolerance stress test showed small forged perturbations below tolerance evade even 100% sampling.

## Boundaries and scale limits

Evidence is limited to a small synthetic MLP, simple SGD-like deltas, local CUDA replay, and synthetic attack modes. It does not validate real volunteer hardware heterogeneity, network protocol commitments, large-model training, mixed precision drift, or nondeterministic production kernels.

## Claim scope

In a local synthetic PyTorch training-step simulator on GB10 CUDA with deterministic algorithms enabled, random deterministic replay sampling detects sampled dishonest volunteer updates with zero observed honest false positives and replay overhead roughly proportional to the sampling rate.

## Why it stopped

No-paper useful signal: the synthetic deterministic mechanism is supported, but production viability depends on cross-device replay fidelity and tolerance policy that were only proxied here.

## Recommended next action

Run a bounded heterogeneous-replay follow-up using two different devices or precision modes to measure the honest replay tolerance floor and whether small malicious deviations can remain below it while affecting model quality.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Heterogeneous Replay Tolerance Floor for DRES
- Success threshold: Honest replay false-positive rate below 0.1% at a fixed tolerance, while forged updates causing at least 0.5% validation loss degradation are detected in at least 95% of runs at 5% sampling.
- Stop condition: Stop early if honest cross-device replay requires a tolerance larger than the smallest malicious deviation that measurably changes validation loss, because DRES would lack a usable verification margin in that setting.

## Evidence references

- Artifact root: `<local-path>/projects/dres-deterministic-re-execution-sampling-for-volunteer-training-verification-98b58d7a68bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
