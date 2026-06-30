# Gradient-norm outlier detection for volunteer screening

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-norm-outlier-detection-for-volunteer-screening-c9f61287617e`
Run ID: `gradient-norm-outlier-detection-for-volunteer-screening-c9f61287617e-20260531T211931378155+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/10a1b7271a83

## What looked useful

Gradient norm reached ROC-AUC 0.9959 and top-decile precision 1.0, but average loss reached ROC-AUC 0.9999 and precision-at-bad-count 0.9979 versus gradient norm 0.9563. Gradient norm and loss were highly correlated at r=0.9594, making average loss the required baseline for future work.

## Boundaries and scale limits

Synthetic Gaussian data, small MLP, 8 seeds, 1280 total volunteer batches; no real volunteer data, no adaptive adversary, no privacy constraints, and no production threshold calibration.

## Claim scope

In a synthetic 3-class volunteer-batch screening proxy with label-flipped, feature-noisy, out-of-domain, clean, and clean-hard-minority cohorts, per-volunteer gradient norm is a strong anomaly score but does not outperform average loss.

## Why it stopped

Synthetic evidence supports the mechanism but early falsifies the novelty/advantage claim because a simpler loss baseline was stronger; this is not full real-world validation.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test whether gradient norm beats loss on real image/text volunteer cohorts with corruptions and hard legitimate subpopulations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data gradient-norm versus loss screening under volunteer corruptions
- Success threshold: Gradient norm or a gradient-plus-loss detector improves ROC-AUC by at least 0.03 or reduces hard-legitimate false positives by at least 25% at matched bad-volunteer recall versus loss alone across at least 3 seeds.
- Stop condition: Stop if loss alone matches or exceeds gradient-based scoring on all datasets/seeds, or if hard legitimate volunteers dominate gradient-norm false positives at useful recall.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-outlier-detection-for-volunteer-screening-c9f61287617e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
