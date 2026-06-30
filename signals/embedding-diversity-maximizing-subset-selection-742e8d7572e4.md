# Embedding-Diversity Maximizing Subset Selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `embedding-diversity-maximizing-subset-selection-742e8d7572e4`
Run ID: `embedding-diversity-maximizing-subset-selection-742e8d7572e4-20260525T121602181176+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8cd4bb28951f

## What looked useful

Pure diversity objectives over-spread: in the main synthetic run k-center and DPP selected about 18% outliers from a 3.5% outlier population and had average nearest-distance coverage about 0.073-0.075 worse than facility-location. The no-outlier control retained a similar coverage gap, so the weakness is not only explicit outlier sensitivity.

## Boundaries and scale limits

Validated only on synthetic embeddings up to n=1600, d=64, k=100, 12 clusters, 15 outlier trials and 10 no-outlier control trials. No real embedding corpus, downstream model training, retrieval task, or large-scale approximate implementation was tested.

## Claim scope

On controlled synthetic unit-normalized clustered embeddings with imbalance and optional outliers, pure embedding-diversity subset selectors such as k-center and greedy DPP increase selected pairwise distance and class coverage but are worse representative subset selectors than facility-location on nearest-distance coverage and label-distribution match.

## Why it stopped

Synthetic proxy evidence is sufficient to reject standalone diversity maximization as paper-ready here, but not sufficient for a full real-world validation claim.

## Recommended next action

Run a bounded real-embedding follow-up comparing k-center, DPP, facility-location, and density-aware hybrids on labeled retrieval or classification embeddings with downstream utility metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Embedding Density-Aware Subset Selection Benchmark
- Success threshold: A density- or facility-aware method beats pure k-center and DPP on downstream utility by at least 2 percentage points or reduces average nearest-distance coverage by at least 5% at matched subset size without losing rare-class coverage.
- Stop condition: Stop if real datasets show no downstream or coverage improvement over random selection, or if gains only appear when rare-class coverage is lower than pure diversity.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-diversity-maximizing-subset-selection-742e8d7572e4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
