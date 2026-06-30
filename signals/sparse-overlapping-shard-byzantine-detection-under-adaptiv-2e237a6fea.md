# Sparse Overlapping-Shard Byzantine Detection Under Adaptive Camouflage

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sparse-overlapping-shard-byzantine-detection-under-adaptiv-2e237a6fea`
Run ID: `sparse-overlapping-shard-byzantine-detection-under-adaptiv-2e237a6fea-20260620T024112082421+0000`

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

- Parent run decision: Overlapping-Shard Cross-Validation Tournament for Byzantine Detection: enoch://control-plane/projects/overlapping-shard-cross-validation-tournament-for-byzantine-detection-fe09c550cfab/runs/overlapping-shard-cross-validation-tournament-for-byzantine-detection-fe09c550cfab-20260620T001632806685+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bbf53c67e335

## What looked useful

Adaptive degree-8 overlap AUC mean was 0.9977 versus marginal baseline AUC 0.4997, with 0.9830 mean TPR at 5% FPR across 250 trials; degree 4 remained strong and degree 2 showed lower but useful recall.

## Boundaries and scale limits

Tier 1 controlled small direct test only; no real distributed traces, no adversarial shard placement, no non-Gaussian/correlated honest process, and no attacker optimized against the exact overlap detector.

## Claim scope

In a seeded synthetic shard graph with 72 shards, 16% Byzantine shards, sparse pairwise overlaps, Gaussian honest values, and Byzantine marginal camouflage by value permutation/rescaling, overlap-consistency scoring detects Byzantine shards far better than non-overlap marginal-moment scoring.

## Why it stopped

Synthetic Tier 1 mechanism support is useful but not paper-positive; closing as no-paper evidence under the strict paper gate.

## Recommended next action

Run a bounded deepen follow-up with an attacker that explicitly optimizes corruption utility subject to the overlap-consistency detector and adversarial shard placement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized Camouflage Against Sparse Overlap Consistency
- Success threshold: For overlap degree 4 or 8, optimized-attacker overlap AUC >= 0.85, TPR at 5% FPR >= 0.50, and attack utility retained >= 0.50 while marginal baseline AUC remains <= 0.60 under camouflage.
- Stop condition: Stop as negative if optimized camouflage drives overlap AUC below 0.75 or TPR at 5% FPR below 0.30 for both degree 4 and degree 8 while retaining attack utility >= 0.50.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-overlapping-shard-byzantine-detection-under-adaptiv-2e237a6fea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
