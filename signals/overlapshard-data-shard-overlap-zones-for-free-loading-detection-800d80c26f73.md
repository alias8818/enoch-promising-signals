# OverlapShard: Data-Shard Overlap Zones for Free-Loading Detection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `overlapshard-data-shard-overlap-zones-for-free-loading-detection-800d80c26f73`
Run ID: `overlapshard-data-shard-overlap-zones-for-free-loading-detection-800d80c26f73-20260614T110422013878+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6dfd71420de4

## What looked useful

Overlap-based detectors were chance at zero overlap and rose substantially when overlap zones were inserted. In the main 80-seed sweep at heterogeneity 0.8, residual overlap AUC at 8 overlap examples was 0.853 for private_only, 0.961 for random_norm_matched, 0.942 for replay_other, and 0.968 for zero. Detection degraded under higher heterogeneity, so the mechanism is promising but not closed.

## Boundaries and scale limits

The evidence is limited to synthetic one-step logistic regression with 16 clients, 25% freeloaders, controlled non-IID data, and no privacy-preserving aggregation. It does not validate deep models, multi-round training, adaptive overlap forgeries, or production-scale shard systems.

## Claim scope

In a synthetic server-known logistic-regression sharding setup, deliberate overlap zones provide gradient signatures that improve free-loading detection over no-overlap controls, especially for zero, norm-matched random, replayed, and small-overlap private-only adversaries.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is not direct production or deep-model validation, so this is not paper-ready.

## Recommended next action

Stop this run as a no-paper useful signal; next run should test the residual overlap detector in a small multi-round neural benchmark with adaptive overlap-forging controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-round neural OverlapShard residual detector with adaptive forgeries
- Success threshold: Residual overlap detector AUC >= 0.85 and false-positive rate <= 10% at 80% freeloader recall across at least three seeds, with less than 2% task-accuracy degradation from overlap insertion.
- Stop condition: Stop if no-overlap and overlap detectors are statistically indistinguishable, if adaptive forging defeats detection without meaningful full-shard training, or if overlap insertion degrades model utility by 2% or more.

## Evidence references

- Artifact root: `<local-path>/projects/overlapshard-data-shard-overlap-zones-for-free-loading-detection-800d80c26f73`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
