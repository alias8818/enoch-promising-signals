# Real-corpus fixed-budget confirmation of quality-filtered pretraining subsets

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-corpus-fixed-budget-confirmation-of-quality-filtered-d2bc9dc6c3`
Run ID: `real-corpus-fixed-budget-confirmation-of-quality-filtered-d2bc9dc6c3-20260630T050803883918+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Data-Selection Pretraining: Quality-Filter Subset vs Full Corpus at Fixed Budget: enoch://control-plane/projects/data-selection-pretraining-quality-filter-subset-vs-full-corpus-at-fixed-budget-8f391d913159/runs/data-selection-pretraining-quality-filter-subset-vs-full-corpus-at-fixed-budget-8f391d913159-20260630T045109240336+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/258725c218cc

## What looked useful

Quality-top selection produced cleaner text and lower training loss, but worse held-out WikiText validation/test bits-per-character than random in all three seeds. Mean test BPC was 3.2905 for quality_top vs 3.1763 for random, a +0.1142 BPC / +3.60% relative degradation.

## Boundaries and scale limits

Small corpus, character-level GRU proxy, 180k-character training subsets, 250 optimizer steps, 3 seeds, and one simple heuristic quality score; not evidence about web-scale token-level Transformer pretraining or learned quality filters.

## Claim scope

Bounded WikiText-2 character-level GRU probe with equal character budgets and equal optimizer steps: the tested transparent quality heuristic did not improve fixed-budget pretraining subset selection over random sampling.

## Why it stopped

Bounded direct/proxy evidence early-falsified the simple quality-filter hypothesis in this setup; it is not a full-scale validation, but the consistent paired degradation makes the current heuristic not worth paper escalation.

## Recommended next action

Stop this run as a no-paper useful signal; next run should test whether diversity-matched quality filtering avoids the observed held-out degradation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-matched quality filtering for fixed-budget real-corpus pretraining subsets
- Success threshold: Diversity-matched quality filtering beats random by at least 1% relative held-out loss/BPC without reducing document diversity below the random baseline.
- Stop condition: Stop if diversity-matched quality filtering is not better than random on mean held-out loss/BPC across seeds or if gains disappear when length/topic diversity is matched.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-fixed-budget-confirmation-of-quality-filtered-d2bc9dc6c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
