# Real-data audit of margin-band synthetic negative selection

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `real-data-audit-of-margin-band-synthetic-negative-selectio-2f7bab2cc3`
Run ID: `real-data-audit-of-margin-band-synthetic-negative-selectio-2f7bab2cc3-20260520T172707007248+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Contrastive margin selection with synthetic negatives: enoch://control-plane/projects/contrastive-margin-selection-with-synthetic-negatives-e468329e3be2/runs/contrastive-margin-selection-with-synthetic-negatives-e468329e3be2-20260520T155826142939+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b491ee72200a

## What looked useful

Margin-band selected negatives had 25.8% mean true-positive contamination at the main 10th-percentile margin setting, versus 16.6% for random and 1.9% for far-negative selection; mean AUROC was 0.819 for margin-band versus 0.952 random and 0.973 far. Sensitivity at 5%, 10%, and 20% margin quantiles all failed the <=5% contamination threshold.

## Boundaries and scale limits

Small built-in real datasets; pseudo-negatives were real unlabeled pool items audited with hidden labels, not generated synthetic examples; margin scorer was centroid distance from labeled positives, not a task-specific foundation-model uncertainty scorer.

## Claim scope

Tier 1 controlled small direct real-label audit over 9 sklearn real binary tasks and 20 seeds: centroid-margin pseudo-negative selection failed the <=5% contamination threshold and underperformed random and far-negative controls in mean AUROC.

## Why it stopped

Controlled small real-data audit directly failed the contamination and performance threshold; this is not a full validation of all margin-band methods, but it is sufficient to reject this naive margin-band selection mechanism for paper escalation.

## Recommended next action

Stop this follow-up as an early direct falsification of the stated Tier 1 threshold; any future escalation should first use the actual target generator and scorer and require <=5% contamination plus no AUROC/F1 deficit against random and far-negative controls.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-data-audit-of-margin-band-synthetic-negative-selectio-2f7bab2cc3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
