# Two-host gossip averaging on a real small dataset

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `two-host-gossip-averaging-on-a-real-small-dataset-d36bdd02a4`
Run ID: `two-host-gossip-averaging-on-a-real-small-dataset-d36bdd02a4-20260527T082703152872+0000`

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

- Parent run decision: Gossip-averaged tiny training across two CPU workers: enoch://control-plane/projects/gossip-averaged-tiny-training-across-two-cpu-workers-75f9a3feb6cb/runs/gossip-averaged-tiny-training-across-two-cpu-workers-75f9a3feb6cb-20260526T022911055046+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/77620b22bbc3

## What looked useful

Gossip achieved mean accuracy 0.74925, equal to centralized mean accuracy 0.74925, and exceeded mean isolated-host accuracy 0.67550 by 0.07375. The predeclared threshold was gossip at least 0.02 above isolated hosts and within 0.03 of centralized; the 10-seed run passed. Offline isolated weight averaging was close at 0.74625, limiting novelty claims.

## Boundaries and scale limits

One real small tabular dataset, one binary task, one logistic-regression model, two localhost worker processes rather than two physical machines, fixed non-IID shard recipe, 80 synchronous averaging rounds, and no latency/failure/privacy stress tests.

## Claim scope

In a controlled localhost two-process test on UCI Wine Quality red wine binary classification, periodic two-host gossip averaging on non-IID shards matched centralized logistic-regression accuracy and exceeded independently deployed isolated hosts across 10 seeds.

## Why it stopped

Tier 1 direct controlled validation succeeded, but publication readiness is not supported because the strongest diagnostic control, offline isolated weight averaging, nearly matched periodic gossip.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded follow-up that isolates whether periodic gossip consistently beats one-shot weight averaging under heterogeneity sweeps.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Periodic gossip versus one-shot weight averaging under two-host heterogeneity sweeps
- Success threshold: Periodic gossip must exceed one-shot weight averaging by at least 0.015 mean accuracy or show lower log loss by at least 0.02 in the high-heterogeneity condition while remaining within 0.03 accuracy of centralized training.
- Stop condition: Stop as negative if periodic gossip is within 0.005 accuracy and 0.01 log loss of one-shot weight averaging across all heterogeneity levels, or if it falls more than 0.03 accuracy below centralized in most settings.

## Evidence references

- Artifact root: `<local-path>/projects/two-host-gossip-averaging-on-a-real-small-dataset-d36bdd02a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
