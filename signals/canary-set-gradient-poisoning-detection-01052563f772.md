# Canary-Set Gradient Poisoning Detection

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `canary-set-gradient-poisoning-detection-01052563f772`
Run ID: `canary-set-gradient-poisoning-detection-01052563f772-20260621T023554178382+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/656162164e51

## What looked useful

Canary-gradient conflict averaged 0.399 AUROC and 0.013 TPR at 5% FPR across 48 config groups; its best AUROC config reached 0.720 but only 0.001 TPR at 5% FPR. Batch loss averaged 0.995 AUROC on the same attacks, so the canary score adds no practical advantage in this setup.

## Boundaries and scale limits

Synthetic Gaussian data, logistic regression only, 48 config groups, 5 seeds per group, candidate-batch detection only; no deep networks, real datasets, adaptive attacks, distributed/federated setting, or multi-step accepted-update persistence.

## Claim scope

In a bounded NumPy logistic-regression synthetic binary-classification probe, the tested detector score (-cosine between candidate batch gradient and clean canary-set gradient) is not a useful standalone poisoning detector for label-flip or trigger-style poisoned batches at low false-positive rate.

## Why it stopped

Proxy/local early falsification: the direct synthetic test failed the practical low-FPR detection threshold and was dominated by a trivial batch-loss baseline; this is not a full validation of canary-set defenses broadly.

## Recommended next action

Stop this simple canary-gradient-cosine formulation as no-paper useful negative evidence; any next work should first design a detector that beats batch-loss controls on the same bounded synthetic matrix.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/canary-set-gradient-poisoning-detection-01052563f772`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
