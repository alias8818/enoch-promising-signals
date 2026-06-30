# SpotCheck-GD: Random-Set Gradient Re-Verification for CPU Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `spotcheck-gd-random-set-gradient-re-verification-for-cpu-volunteer-training-96585b5f26ef`
Run ID: `spotcheck-gd-random-set-gradient-re-verification-for-cpu-volunteer-training-96585b5f26ef-20260620T051158491403+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dcea8b09bcc8

## What looked useful

At 12.5% verification budget, random withheld checks detected 0.919 of fixed-evasion malicious submissions and accepted 0.081 of poisoned vectors, while known fixed checks detected 0.000 and accepted 1.000. Whole-batch flips were detected at 1.000 with 12.5% random checking. No-attack controls had 0.000 false positives.

## Boundaries and scale limits

8 seeds, 50 SGD rounds, 32 simulated workers, batch size 64, 64-dimensional synthetic logistic regression. No real volunteer network, neural model, cryptographic commitment, GPU training, large dataset, or adaptive attacker with pre-challenge leakage was tested.

## Claim scope

In a bounded CPU simulation of volunteer SGD for synthetic logistic regression, withheld random per-example gradient spot checks detect poisoned worker submissions near the analytic subset-overlap probability and defeat a deterministic known-check evasion at the same check budget.

## Why it stopped

Bounded synthetic evidence supports the random-withheld spot-check mechanism, but the result is proxy-scale and not a full volunteer-training validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement commit-then-challenge verification in a small neural-network training harness and measure overhead plus validation impact.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-Then-Challenge SpotCheck-GD on a Small Neural Training Harness
- Success threshold: At 10-15% verification budget, random withheld checks detect at least 90% of fixed-evasion or sparse poisoned submissions, keep false positives below 1%, and recover validation accuracy to within 2 percentage points of the honest/no-attack run.
- Stop condition: Stop if random withheld checking detects below 70% of poisoned submissions at 15% budget, false positives exceed 5%, or recomputation overhead dominates the simulated training step by more than 2x.

## Evidence references

- Artifact root: `<local-path>/projects/spotcheck-gd-random-set-gradient-re-verification-for-cpu-volunteer-training-96585b5f26ef`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
