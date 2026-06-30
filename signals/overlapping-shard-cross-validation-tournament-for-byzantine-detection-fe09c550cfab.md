# Overlapping-Shard Cross-Validation Tournament for Byzantine Detection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `overlapping-shard-cross-validation-tournament-for-byzantine-detection-fe09c550cfab`
Run ID: `overlapping-shard-cross-validation-tournament-for-byzantine-detection-fe09c550cfab-20260620T001632806685+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bbf53c67e335

## What looked useful

Across 80 seeds per fraction, overlap median peer AUC was 1.000 at 10%, 1.000 at 20%, 0.987 at 30%, and 0.756 at 40%, while disjoint shard peer AUC was 0.000, 0.000, 0.158, and 0.077. This supports overlap as a mechanism for breaking clustered local-majority capture, but also shows degradation near 40% Byzantine workers.

## Boundaries and scale limits

Synthetic only; no production validator traces, no adaptive adversaries, no unknown-count thresholding, no sparse item-subset workload, and no comparison to graph/community-detection baselines. The all-to-all oracle remains perfect in this setup, so the overlap claim is limited to sparse sharded deployments where all-to-all review is unavailable or too expensive.

## Claim scope

In a deterministic synthetic binary-label setting with 64 workers, clustered colluding Byzantine workers, 8-worker shards, and 4-way overlap, median overlapping-shard peer scoring detects Byzantine workers much better than isolated disjoint-shard peer scoring, especially at 10-30% Byzantine fractions.

## Why it stopped

Synthetic proxy evidence supports the mechanism but is not direct/full validation and is insufficient for paper writing.

## Recommended next action

Stop this run as no-paper useful synthetic evidence; if continuing, run a bounded sparse-workload follow-up with adaptive camouflage adversaries, unknown Byzantine count, threshold calibration, and graph/community-detection baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sparse Overlapping-Shard Byzantine Detection Under Adaptive Camouflage
- Success threshold: Overlap must improve AUC by at least 0.10 over the best non-oracle baseline and keep precision@estimated-B at or above 0.80 through 30% Byzantine workers without using the true Byzantine count.
- Stop condition: Stop if overlap fails to beat the best non-oracle baseline by 0.05 AUC in two independent 50-seed batches, or if threshold calibration causes false-positive rate above 20% at 20% Byzantine workers.

## Evidence references

- Artifact root: `<local-path>/projects/overlapping-shard-cross-validation-tournament-for-byzantine-detection-fe09c550cfab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
