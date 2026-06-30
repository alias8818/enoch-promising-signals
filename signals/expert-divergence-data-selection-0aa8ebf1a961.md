# Expert Divergence Data Selection

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `expert-divergence-data-selection-0aa8ebf1a961`
Run ID: `expert-divergence-data-selection-0aa8ebf1a961-20260526T011811490931+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6fe9efb9df68

## What looked useful

Naive high expert-divergence selection was informative relative to deliberately low-divergence selection, but it significantly underperformed random selection overall, especially on digits, suggesting that pure disagreement maximization can over-select unrepresentative difficult points.

## Boundaries and scale limits

Proxy only: no human expert labels, no LLM data-selection workload, no large-scale training, no multi-round active learning, and only three small built-in datasets.

## Claim scope

In a local proxy using three scikit-learn classification datasets, five model-family experts, one-shot active selection, 100 seeds per dataset, and a logistic-regression final learner, selecting the highest committee-divergence examples did not improve label efficiency over random selection and was roughly tied with single-model uncertainty.

## Why it stopped

The tested proxy directly contradicted the broad hypothesis that highest expert divergence is generally better than random selection; this is not a full-domain validation.

## Recommended next action

Stop this run as a proxy early falsification of naive divergence-only selection; if continuing, run a bounded follow-up that adds diversity or representativeness constraints before comparing to random.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-Constrained Expert Divergence Selection
- Success threshold: Diversity-constrained divergence must beat random by at least 0.5 percentage points mean balanced accuracy overall with a paired Wilcoxon p-value below 0.05, while not losing on more than one dataset.
- Stop condition: Stop if the constrained selector remains statistically tied with or worse than random overall, or if gains only come from one dataset while another dataset loses by more than 1 percentage point balanced accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/expert-divergence-data-selection-0aa8ebf1a961`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
