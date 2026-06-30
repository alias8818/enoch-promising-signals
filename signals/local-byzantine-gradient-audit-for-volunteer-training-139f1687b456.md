# Local Byzantine Gradient Audit for Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `local-byzantine-gradient-audit-for-volunteer-training-139f1687b456`
Run ID: `local-byzantine-gradient-audit-for-volunteer-training-139f1687b456-20260527T183903233675+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c397c3a251f1

## What looked useful

A small trusted probe-gradient audit is a plausible defense mechanism for local volunteer-gradient screening in this toy setting. At 30% Byzantine clients, audit-filtered mean reached 0.9345 accuracy on sign-flip, 0.9345 on label-flip, 0.9320 on drift, and 0.9339 on Gaussian attacks, versus clean mean accuracy of 0.9355. The result is a no-paper useful signal because the evidence is synthetic and non-adaptive.

## Boundaries and scale limits

Not validated on neural networks, real volunteer hardware, real networking, privacy-preserving protocols, adaptive attackers, audit-data leakage, or large-scale training. Audit-set representativeness is material: 8-16 audit samples rejected many honest gradients and reduced accuracy in the ablation.

## Claim scope

In a synthetic non-IID logistic-regression volunteer-training simulation with 40 clients, 80 training rounds, 12 random seeds, non-adaptive Byzantine gradient attacks, and a 96-sample trusted audit batch, audit-filtered mean aggregation preserved near-clean test accuracy through 30% Byzantine clients and outperformed unaudited mean and coordinate-trimmed mean on sign-flip, label-flip, and drift attacks.

## Why it stopped

Closed as no-paper useful signal: the local synthetic mechanism is supported, but this is not direct/full validation for volunteer neural-network training.

## Recommended next action

Run a bounded deepen follow-up on a real small neural-network task with client partitions, adaptive attacks, and stronger robust aggregation baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural-network audit-filtered aggregation under adaptive Byzantine clients
- Success threshold: At 20-30% Byzantine clients, audit-filtered aggregation maintains validation accuracy within 2 percentage points of clean training and beats all tested baselines by at least 3 percentage points on at least two adaptive attack families without rejecting more than 15% of honest gradients.
- Stop condition: Stop as unsupported if adaptive attacks reduce audit-filtered validation accuracy to within 1 percentage point of unaudited mean or cause more than 25% honest-gradient rejection in two independent seeds.

## Evidence references

- Artifact root: `<local-path>/projects/local-byzantine-gradient-audit-for-volunteer-training-139f1687b456`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
