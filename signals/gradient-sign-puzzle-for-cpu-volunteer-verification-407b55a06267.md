# Gradient-Sign Puzzle for CPU Volunteer Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-sign-puzzle-for-cpu-volunteer-verification-407b55a06267`
Run ID: `gradient-sign-puzzle-for-cpu-volunteer-verification-407b55a06267-20260525T182141104599+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/01c5be3baed4

## What looked useful

Across 64 corrected main puzzles and 786432 observed bits, sign fractions were near 0.5, repeat mismatch was 0, float32/float64 mismatch was 0 with fixed verifier-selected coordinates, wrong-seed and wrong-parameter controls had mean Hamming distances near 0.5, and the random false-accept probability for 1024 checked bits at 98% match was 3.11e-267. Scaling runs showed mean solve times from 0.027 s to 0.172 s while preserving control behavior.

## Boundaries and scale limits

Tested only on one CPU worker with Python 3.14.4, NumPy 2.4.6, synthetic data, small MLPs up to 384 input by 256 hidden units, 64 main puzzles, and cheap wrong-seed controls. No heterogeneous CPU fleet, adversarial protocol analysis, answer-key leakage model, replay/collusion defense, or production volunteer network was tested.

## Claim scope

Synthetic local CPU experiments show that selected MLP gradient sign bits can form balanced, deterministic, seed-sensitive puzzles with tunable CPU cost and negligible random-guess acceptance under a 1024-bit 98% match check.

## Why it stopped

Synthetic local evidence supports the mechanism but not a paper-positive volunteer-verification protocol; security and deployment claims remain unvalidated.

## Recommended next action

Stop as no-paper useful-signal evidence; the next bounded action is a deepen follow-up that tests heterogeneous CPUs and simple adaptive cheating/replay models before considering any security claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Heterogeneous and adversarial checks for gradient-sign CPU puzzles
- Success threshold: Across heterogeneous hosts, honest mismatch must stay below 0.1% of checked bits, all tested cheating baselines must fail the 98% match threshold on at least 1000 challenges, and verifier online check time must be at least 100x cheaper than honest solve time when answer keys are precomputed.
- Stop condition: Stop if any ordinary CPU/BLAS stack exceeds 0.1% honest mismatch, if a cheap replay/stale/partial strategy passes the verifier threshold, or if online verification requires recomputing most gradients.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-sign-puzzle-for-cpu-volunteer-verification-407b55a06267`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
