# Adaptive challenge-gradient evasion in a small volunteer-training loop

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-challenge-gradient-evasion-in-a-small-volunteer-t-5c60b03fd9`
Run ID: `adaptive-challenge-gradient-evasion-in-a-small-volunteer-t-5c60b03fd9-20260628T063012103767+0000`

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

- Parent run decision: Held-Out Challenge Batches Detect Volunteer Gradient Cheating: enoch://control-plane/projects/held-out-challenge-batches-detect-volunteer-gradient-cheating-ed482257c392/runs/held-out-challenge-batches-detect-volunteer-gradient-cheating-ed482257c392-20260628T054933233293+0000
- Parent run decision: Challenge-gradient cheating detector in a small PyTorch volunteer-training loop: enoch://control-plane/projects/challenge-gradient-cheating-detector-in-a-small-pytorch-vo-bdc3c7c5f9/runs/challenge-gradient-cheating-detector-in-a-small-pytorch-vo-bdc3c7c5f9-20260628T060903388544+0000

## What looked useful

Adaptive challenge training produced a 47.03 point challenge-vs-clean-target gap in the adaptive-gradient condition and a 20.07 point clean-target deficit versus IID baseline, but adaptive_no_leak had similar clean-target collapse, making the gradient-specific causal attribution mixed.

## Boundaries and scale limits

80 small neural-volunteer runs over synthetic features only; no human volunteers, no text tasks, no real challenge platform, and no large-model training. The result is Tier 2 mechanism evidence, not paper-positive broad validation.

## Claim scope

In a synthetic binary volunteer-training loop with fixed seeds, adaptive hard-example challenge selection plus a correlated gradient-leak shortcut produces perfect challenge-domain accuracy but near-chance clean target accuracy; the gradient leak increases shortcut reliance, but clean-target collapse is not distinguishable from the adaptive no-leak control.

## Why it stopped

Tier 2 validation completed with fixed seeds, ablations, and a real IID baseline; evidence is useful but mixed and not paper-ready because the adaptive no-leak control also failed on clean target accuracy.

## Recommended next action

Run a sharpened deepen test that controls adaptive hard-example difficulty so adaptive_no_leak retains target accuracy, then measure whether only the gradient-leak condition collapses on clean target performance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Difficulty-matched adaptive challenge-gradient leak isolation
- Success threshold: After difficulty matching, adaptive_no_leak clean target accuracy is within 3 points of IID baseline, and adaptive_gradient is at least 10 points worse than adaptive_no_leak on clean target accuracy while reaching at least 95 percent correlated-challenge accuracy.
- Stop condition: Stop if adaptive_no_leak again collapses by more than 5 points versus IID baseline after two calibrated difficulty settings, because the setup cannot isolate gradient-specific evasion.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-challenge-gradient-evasion-in-a-small-volunteer-t-5c60b03fd9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
