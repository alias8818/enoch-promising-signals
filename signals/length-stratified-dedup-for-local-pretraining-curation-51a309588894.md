# Length-Stratified Dedup for Local Pretraining Curation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `length-stratified-dedup-for-local-pretraining-curation-51a309588894`
Run ID: `length-stratified-dedup-for-local-pretraining-curation-51a309588894-20260604T005143776287+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0464243693d3

## What looked useful

Length stratification is best viewed as a tunable cost/recall policy rather than a free dedup improvement. Strict buckets saved 13.0% candidate pairs in the 6000-doc run and 24.9% on average across three 4000-doc replicates, but recall fell to about 0.989. Adjacent buckets restored 1.000 recall in these runs but saved only about 3% candidates.

## Boundaries and scale limits

Synthetic-only evidence at 800, 4000, and 6000 documents; no real corpus shard, no manual labels, no downstream language-model training, and one MinHash/LSH parameterization.

## Claim scope

On controlled synthetic pretraining-curation corpora with same-length near duplicates, boilerplate singletons, and cross-length containment-style related documents, strict length-bucketed MinHash-LSH reduced candidate pairs but lost about 1% near-duplicate recall; adjacent-bucket matching preserved recall but reduced candidate pairs only modestly.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only and shows a mixed tradeoff rather than a publication-grade positive result.

## Recommended next action

Run the same policy comparison on a real local pretraining-corpus shard with audited duplicate and containment labels before considering model-training validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-shard audit of length-stratified MinHash dedup
- Success threshold: Adjacent-bucket policy achieves at least 0.995 audited near-duplicate recall relative to global LSH and at least 10% fewer candidate verifications without increasing audited false removals.
- Stop condition: Stop if adjacent buckets reduce candidate verifications by less than 5% or miss more than 1% of audited near duplicates versus global LSH.

## Evidence references

- Artifact root: `<local-path>/projects/length-stratified-dedup-for-local-pretraining-curation-51a309588894`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
