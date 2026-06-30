# Challenge-gradient cheating detector in a small PyTorch volunteer-training loop

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `challenge-gradient-cheating-detector-in-a-small-pytorch-vo-bdc3c7c5f9`
Run ID: `challenge-gradient-cheating-detector-in-a-small-pytorch-vo-bdc3c7c5f9-20260628T060903388544+0000`

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

- Parent run decision: Held-Out Challenge Batches Detect Volunteer Gradient Cheating: enoch://control-plane/projects/held-out-challenge-batches-detect-volunteer-gradient-cheating-ed482257c392/runs/held-out-challenge-batches-detect-volunteer-gradient-cheating-ed482257c392-20260628T054933233293+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/befc816e0544

## What looked useful

Main sweep: flip_all mean AUC 0.981-0.989 and mean TPR@~5%FPR 0.916-0.947 across challenge sizes 2-16; random_labels mean AUC 0.971-0.976 and TPR 0.873-0.893; noise mean AUC 0.931-0.963 but TPR weak at small challenge sizes. Challenge-weight 2.0 improved noise TPR to 0.979 at challenge size 8 and 1.000 at size 16.

## Boundaries and scale limits

Tested only 12 seeds, 40 rounds, 8 volunteers, 25% cheaters, synthetic 2D data, and a tiny MLP. Not tested on real data, large models, secure aggregation, heterogeneous clients beyond random batches, collusion, or adaptive attackers that optimize to pass the challenge score.

## Claim scope

In a toy PyTorch volunteer-training loop with a tiny MLP on synthetic binary Gaussian data, cosine alignment with a coordinator-known challenge gradient reliably detects non-adaptive wrong-label volunteer gradients and often detects norm-matched random-noise gradients when the challenge signal is large enough.

## Why it stopped

Tier 1 direct small test supports the mechanism but remains toy-scale and non-adaptive, so it is useful no-paper evidence rather than paper-positive validation.

## Recommended next action

Run a bounded adaptive-evasion follow-up where cheaters combine malicious local gradients with enough honest challenge gradient to pass the cosine threshold, measuring both detection failure rate and poisoning effect.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive challenge-gradient evasion in a small volunteer-training loop
- Success threshold: Find an adaptive attacker that passes the 5% honest-FPR cosine threshold in at least 80% of cheating updates while reducing final test accuracy by at least 5 percentage points versus honest-only training, or show this fails across at least 12 seeds.
- Stop condition: Stop if blended/adaptive attackers cannot both pass the detector and measurably harm the model in the small loop, or if they trivially evade and poison under the stated threshold.

## Evidence references

- Artifact root: `<local-path>/projects/challenge-gradient-cheating-detector-in-a-small-pytorch-vo-bdc3c7c5f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
