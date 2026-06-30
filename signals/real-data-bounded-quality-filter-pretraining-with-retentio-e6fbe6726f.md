# Real-data bounded quality-filter pretraining with retention ablations

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-data-bounded-quality-filter-pretraining-with-retentio-e6fbe6726f`
Run ID: `real-data-bounded-quality-filter-pretraining-with-retentio-e6fbe6726f-20260619T203532558734+0000`

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

- Parent run decision: Tiny Quality Classifier Pre-filtering for Pretrain Mix: enoch://control-plane/projects/tiny-quality-classifier-pre-filtering-for-pretrain-mix-318e8c7a110b/runs/tiny-quality-classifier-pre-filtering-for-pretrain-mix-318e8c7a110b-20260619T201712030692+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cf144e17405a

## What looked useful

Across five Tier 1 metric files, only the deeper 2,000-step seed met the formal threshold. In that run, quality-only improved high-quality validation loss by only 0.0031 while increasing full-retention loss by 0.0300; 30% replay improved high-quality loss by 0.0071 and cut retention regression to 0.0085, a 71.8% reduction. Shallow multiseed runs showed replay reduced retention regression when present, but quality-only high-quality gains were unstable.

## Boundaries and scale limits

Tested a 1.9M-parameter Transformer trained from scratch on WikiText-2 with a heuristic text-quality score; not GPT-2-small-class, not broad web pretraining, not convergence, and not a learned/human quality classifier.

## Claim scope

Tier 1 real-data WikiText-2 tiny causal-Transformer test: 30% full-distribution replay can reduce retention-loss degradation from quality-filtered sampling when that degradation appears, but the quality-filter gain itself is tiny and seed-sensitive.

## Why it stopped

No paper-ready result: the retention mechanism has a useful bounded signal, but the upstream quality-filter benefit is too small and seed-sensitive in this Tier 1 test.

## Recommended next action

Run a bounded deepen test with a stronger real-data quality signal, at least three seeds, and a pre-registered minimum high-quality gain before considering any paper path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stronger quality-signal retention replay on real text
- Success threshold: Quality-only improves high-quality validation loss by at least 0.03 versus unfiltered baseline in at least 2 of 3 seeds, and quality-plus-retention preserves at least 75% of that gain while reducing full-distribution retention-loss regression by at least 30%.
- Stop condition: Stop if quality-only fails to achieve at least 0.03 high-quality validation-loss gain in 2 of 3 seeds, or if replay fails to reduce retention regression by at least 30% in the seeds where regression appears.

## Evidence references

- Artifact root: `<local-path>/projects/real-data-bounded-quality-filter-pretraining-with-retentio-e6fbe6726f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
