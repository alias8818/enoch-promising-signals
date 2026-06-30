# Small Real-Benchmark Gradient-Statistic Poison Detector

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-real-benchmark-gradient-statistic-poison-detector-e3677a2374`
Run ID: `small-real-benchmark-gradient-statistic-poison-detector-e3677a2374-20260629T151513445486+0000`

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

- Parent run decision: Tiny CPU-Trained Poisoning Discriminator on Gradient Statistics: enoch://control-plane/projects/tiny-cpu-trained-poisoning-discriminator-on-gradient-statistics-e7ceb445813c/runs/tiny-cpu-trained-poisoning-discriminator-on-gradient-statistics-e7ceb445813c-20260629T144822019031+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/68f1afa29ba0

## What looked useful

Gradient class-cosine/combination scores are viable poison indicators on a real small benchmark, especially at 20% label-flip poisoning, but the loss baseline is too strong at 5% and 10% poisoning for a paper-ready novelty claim.

## Boundaries and scale limits

Small tabular benchmark only; no deep network, image/text benchmark, clean-label poison, backdoor poison, adaptive attacker, larger dataset, or oracle-free threshold calibration was tested.

## Claim scope

On UCI Wine with a NumPy softmax classifier and random training-label flips at 5%, 10%, and 20%, per-example gradient statistics identify poisoned examples with high absolute ROC AUC, but do not consistently outperform simple training-loss and gradient-norm baselines.

## Why it stopped

Bounded local evidence supports the mechanism in absolute terms but gives a mixed comparative result against simple baselines, so this is not a publication-grade positive result.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should evaluate the same detector against loss and gradient-norm baselines on a harder real benchmark with oracle-free threshold selection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harder Real-Benchmark Gradient Poison Detector With Oracle-Free Thresholds
- Success threshold: Gradient-statistic detector improves mean average precision and thresholded precision by at least 0.05 over both loss and gradient norm across at least 30 seeds, without worse false-positive rate.
- Stop condition: Stop as negative if the gradient-statistic detector fails to beat loss and gradient norm by the success threshold on the harder benchmark or requires oracle poison-count tuning.

## Evidence references

- Artifact root: `<local-path>/projects/small-real-benchmark-gradient-statistic-poison-detector-e3677a2374`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
