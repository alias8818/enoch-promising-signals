# K-means++ embedding coverage selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `k-means-embedding-coverage-selection-1f000ff6b618`
Run ID: `k-means-embedding-coverage-selection-1f000ff6b618-20260604T051131038951+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/1c04344dcd6a

## What looked useful

K-means++ won 12/12 synthetic scenario-size cases on mean nearest-selected squared distance versus random with 20.94% average improvement, but selected 90-94% outliers from a pool with 2.5% outliers in the contaminated scenario.

## Boundaries and scale limits

Tested only synthetic 10,000-vector, 64-dimensional mixtures with known labels; no real embedding corpora, no downstream training/retrieval/labeling metrics, and no large-scale validation.

## Claim scope

Synthetic embedding-like Gaussian mixtures show k-means++ seeding can improve nearest-selected coverage and component recall versus random sampling in clean or pre-filtered pools, but raw D^2 sampling is not robust to far outliers.

## Why it stopped

Synthetic proxy evidence supports the clean-coverage mechanism but exposes an outlier failure mode, so this is not a full validation or paper-ready result.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up comparing robust k-means++ variants with whitening, distance clipping, and outlier filtering on real public embedding corpora.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust k-means++ embedding selection on real corpora
- Success threshold: A robust k-means++ variant improves mean or p95 coverage by at least 10% over random while keeping outlier/duplicate selection and label/topic drift within 2x random, and improves or matches downstream utility across both corpora.
- Stop condition: Stop if robust variants fail the outlier/drift threshold on either corpus or if coverage gains disappear after whitening/filtering.

## Evidence references

- Artifact root: `<local-path>/projects/k-means-embedding-coverage-selection-1f000ff6b618`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
