# Tiny-Pretrain Data Quality Filter Ablation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-pretrain-data-quality-filter-ablation-205078d64063`
Run ID: `tiny-pretrain-data-quality-filter-ablation-205078d64063-20260613T145151942917+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ee0ff0d24823

## What looked useful

Score-based top-50% filtering improved clean eval bpc from 0.414067 to 0.394948 while retaining 77.9% of clean docs and 22.1% of noisy docs. The oracle clean-only control reached 0.358671 bpc. Hard threshold filtering worsened clean bpc to 0.499227 by rejecting too many clean documents.

## Boundaries and scale limits

Synthetic corpus, one seed, character n-gram model, no neural LM training, no real web corpus, and no full-scale pretraining validation.

## Claim scope

On a deterministic synthetic mixed-quality corpus with a character 5-gram LM proxy, rank-based data-quality filtering improved held-out clean bits/char versus no filtering, while hard repetition/threshold filters harmed the proxy metric.

## Why it stopped

Proxy-only useful signal; the run is not full pretraining validation and the hard-threshold heuristic is locally falsified.

## Recommended next action

Run a bounded tiny neural LM follow-up on a small real mixed-quality corpus with the same filter variants and at least three seeds before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny neural LM validation of rank-based quality filtering
- Success threshold: Mean clean validation loss improves by at least 2% versus no-filter with no worse than 1% degradation on an in-domain mixed validation set across at least three seeds.
- Stop condition: Stop if score-ranked filtering fails to improve mean clean validation loss versus no-filter, or if gains vanish when token budgets and seeds are matched.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-pretrain-data-quality-filter-ablation-205078d64063`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
