# Cost-matched robust lottery versus robust top-k at boundary score noise

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `cost-matched-robust-lottery-versus-robust-top-k-at-boundar-ac22ab74d3`
Run ID: `cost-matched-robust-lottery-versus-robust-top-k-at-boundar-ac22ab74d3-20260519T061043531008+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Cost-matched robust lottery versus robust top-k at boundary score noise: internal_generated:cost-matched-robust-lottery-versus-robust-top-k-at-boundar-ac22ab74d3

## What looked useful

Across 32 fixed seeds, 200 trials per seed, four scenarios, and 153600 metric rows, the best lottery variant was worse than standard top-k in every scenario. Boundary-noise retained-oracle-utility deltas versus standard top-k were -0.009228, -0.010916, and -0.004717 with non-overlapping negative 95% CIs.

## Boundaries and scale limits

Synthetic candidate utilities and score noise only; no production feedback loop, real recommender/retrieval task, fairness objective, diversity utility, or long-horizon exploration value was tested.

## Claim scope

In a controlled one-shot top-k selection simulator with linear latent utility, fixed selection cost, fixed seeds, boundary-concentrated Gaussian score noise, deterministic top-k baselines, and lottery ablations, cost-matched robust lotteries do not outperform robust or standard top-k on retained oracle utility, lower-tail utility, regret, or oracle overlap.

## Why it stopped

Tier 2 controlled evidence directly falsified the cost-matched robust lottery advantage for the tested boundary-noise top-k utility objective.

## Recommended next action

Stop this no-paper branch for the one-shot utility-retention claim; only reopen under a different objective with explicit non-linear value, fairness, diversity, or exploration metrics.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/cost-matched-robust-lottery-versus-robust-top-k-at-boundar-ac22ab74d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
