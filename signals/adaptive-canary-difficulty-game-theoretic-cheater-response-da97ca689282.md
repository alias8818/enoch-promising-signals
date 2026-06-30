# Adaptive Canary Difficulty: Game-Theoretic Cheater Response

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-canary-difficulty-game-theoretic-cheater-response-da97ca689282`
Run ID: `adaptive-canary-difficulty-game-theoretic-cheater-response-da97ca689282-20260612T232912008587+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3474a9ab489f

## What looked useful

Adaptive canary difficulty should not be assumed to dominate static high difficulty under strategic cheater response. The tested adaptive policies won defender-loss only 6/27 settings and never minimized attacker utility; their plausible niche is reducing honest-user cost when static high difficulty is expensive.

## Boundaries and scale limits

Synthetic toy model only: hand-specified detection, anomaly, evasion, and false-positive curves; no real anti-cheat telemetry, human behavior, multi-cheater population dynamics, or optimized defender policy search.

## Claim scope

In a small repeated Stackelberg proxy with discrete suspicion states, fixed adaptive canary difficulty policies did not improve deterrence against a dynamic-programming cheater; adaptive thresholding only improved defender loss in high false-positive-cost, longer-horizon settings.

## Why it stopped

Proxy-only local evidence found a narrow cost-tradeoff signal but falsified the broad deterrence claim; this is not full validation and not paper-ready.

## Recommended next action

Run a bounded follow-up that optimizes threshold and randomized policies over calibrated synthetic curves, then stop unless adaptive policies beat best static baselines on both defender loss and attacker utility across most settings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized Adaptive Canary Policies Against Dynamic Cheater Response
- Success threshold: Adaptive policy wins defender loss in at least 70% of held-out synthetic settings and reduces attacker expected utility to within 10% of the best static deterrence baseline without higher honest false-positive cost.
- Stop condition: Stop if optimized adaptive policies still fail to beat best static baselines on deterrence in more than half of held-out settings or if gains vanish under false-positive/detection curve perturbations.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-canary-difficulty-game-theoretic-cheater-response-da97ca689282`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
