# Two-stage MinHash plus exact-containment volunteer dedup validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `two-stage-minhash-plus-exact-containment-volunteer-dedup-v-81c68575ba`
Run ID: `two-stage-minhash-plus-exact-containment-volunteer-dedup-v-81c68575ba-20260522T061525530247+0000`

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

- Parent run decision: Local minhash volunteer cluster matches central deduplication: enoch://control-plane/projects/local-minhash-volunteer-cluster-matches-central-deduplication-1817ba95bd37/runs/local-minhash-volunteer-cluster-matches-central-deduplication-1817ba95bd37-20260521T194634213666+0000
- Parent run decision: Public-corpus volunteer minhash dedup validation: enoch://control-plane/projects/public-corpus-volunteer-minhash-dedup-validation-31cba8f7df/runs/public-corpus-volunteer-minhash-dedup-validation-31cba8f7df-20260522T044816585438+0000

## What looked useful

Medium validation found balanced-overlap recall up to 1.000 with 32 MinHash bands, but skewed-containment recall was only 0.0067 with 16 bands and 0.3867 with 32 bands despite mean exact containment 0.962. A token-sampling exact-containment control reached 0.795 skewed-containment recall, indicating the failure is the standard MinHash/Jaccard candidate stage rather than exact containment.

## Boundaries and scale limits

Synthetic records only; 1,000 base records plus 12% duplicates per seed; five fixed seeds; no private or production volunteer corpus; pure Python CPU implementation; no distributed indexing or production-latency validation.

## Claim scope

On fixed-seed synthetic volunteer-like token records, standard two-stage MinHash candidate generation followed by exact containment is high-precision and high-recall for similar-size duplicate records, but it fails under subset/superset size skew because true high-containment pairs have low Jaccard and are not proposed as candidates.

## Why it stopped

Medium direct validation with fixed seeds, ablations, and a real exact baseline showed mixed support and a central failure mode for size-skewed containment duplicates; mechanism support is not publication readiness.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should replace standard MinHash with a containment-aware candidate generator and test it against the same skewed-containment threshold plus a real volunteer-style corpus if available.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Containment-aware candidate generation for volunteer dedup
- Success threshold: Mean recall >= 0.95 and min-seed recall >= 0.90 on skewed_containment with precision >= 0.99 after exact filtering and candidate_pair_ratio <= 0.01.
- Stop condition: Stop if skewed_containment mean recall remains below 0.90 at candidate_pair_ratio <= 0.01, or if improvements only come from enumerating more than 1% of all possible pairs.

## Evidence references

- Artifact root: `<local-path>/projects/two-stage-minhash-plus-exact-containment-volunteer-dedup-v-81c68575ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
