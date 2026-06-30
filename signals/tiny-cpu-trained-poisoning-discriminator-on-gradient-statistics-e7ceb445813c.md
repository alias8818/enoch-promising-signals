# Tiny CPU-Trained Poisoning Discriminator on Gradient Statistics

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-cpu-trained-poisoning-discriminator-on-gradient-statistics-e7ceb445813c`
Run ID: `tiny-cpu-trained-poisoning-discriminator-on-gradient-statistics-e7ceb445813c-20260629T144822019031+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/68f1afa29ba0

## What looked useful

Gradient-statistics features are sufficient for strong poisoned-example ranking in this toy setting. The signal is not uniquely gradient-derived in all regimes: loss-only is nearly as strong for zero/low-trigger label flips, and input norm is strong when the trigger is large.

## Boundaries and scale limits

CPU-only synthetic logistic target model; no real corpus, deep network, adaptive poisoning, clean-label attack, cross-architecture transfer, or production-scale training was tested.

## Claim scope

On synthetic binary classification tasks with 10% label/backdoor-style poisoning, a tiny NumPy logistic discriminator trained on per-example gradient statistics detects poisoned examples on held-out seeds with ROC-AUC 0.929-0.978 across trigger strengths 0.5, 1.0, and 2.0, and 0.943-0.944 for zero/low-trigger label-flip controls.

## Why it stopped

Closed as no-paper useful signal: local synthetic evidence supports the mechanism but is insufficient for publication-grade or broad poisoning-defense claims.

## Recommended next action

Run a bounded direct follow-up on a small real benchmark such as MNIST or AG News with a tiny MLP/CNN target, comparing gradient-statistic discriminator against loss-only and input-only baselines under fixed poison rates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Real-Benchmark Gradient-Statistic Poison Detector
- Success threshold: Mean held-out ROC-AUC >= 0.80 and at least 0.10 above the best single-feature baseline in a non-input-obvious poison regime.
- Stop condition: Stop if gradient-statistic AUC is below 0.70 or does not beat the best simple baseline by 0.05 in two independently seeded real-data runs.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-cpu-trained-poisoning-discriminator-on-gradient-statistics-e7ceb445813c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
