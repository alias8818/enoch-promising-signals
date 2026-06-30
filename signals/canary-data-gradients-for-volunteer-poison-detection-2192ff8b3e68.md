# Canary Data Gradients for Volunteer Poison Detection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `canary-data-gradients-for-volunteer-poison-detection-2192ff8b3e68`
Run ID: `canary-data-gradients-for-volunteer-poison-detection-2192ff8b3e68-20260525T212441474414+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e560ee96bbc0

## What looked useful

Across normalized-update stress conditions, canary poison-gradient AUROC was 0.986-1.000 with TPR@5%FPR 0.928-1.000, while norm AUROC was 0.466-0.520 and random-gradient AUROC was 0.501-0.534. Without update normalization, norm was also near-perfect, showing the canary direction matters mainly after clipping or norm matching.

## Boundaries and scale limits

Synthetic data only; linear model only; one-shot gradients only; no real federated benchmark, secure aggregation, multi-round training, deep model, adaptive canary-inference attack, or downstream attack-success filtering test.

## Claim scope

In a synthetic one-shot volunteer-gradient simulation with linear classification, Gaussian data, and trigger/relabel poisoning, cosine similarity to a secret canary poison-gradient signature separates poisoned from honest normalized client updates far better than norm-only or random-gradient baselines.

## Why it stopped

Proxy synthetic evidence supports the mechanism but does not validate real volunteer poison detection or publication-grade robustness.

## Recommended next action

Run a bounded real federated benchmark with client clipping, non-IID partitions, a small CNN or transformer-class model, and downstream attack-success reduction after filtering; stop here for this synthetic worker run because the current evidence is useful but not paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Federated Benchmark Validation of Canary Gradient Poison Detection
- Success threshold: Canary detector AUROC >= 0.90 and attack-success reduction >= 50% at <= 5% honest-client false positive rate without more than 2 percentage points clean-accuracy loss.
- Stop condition: Stop if canary AUROC is below 0.75 in two independent real benchmark settings or if filtering does not reduce attack success at fixed <= 5% honest-client false positive rate.

## Evidence references

- Artifact root: `<local-path>/projects/canary-data-gradients-for-volunteer-poison-detection-2192ff8b3e68`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
