# Residual-Preserved Ternary Quantization for Small Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-preserved-ternary-quantization-for-small-models-eb4c40af43df`
Run ID: `residual-preserved-ternary-quantization-for-small-models-eb4c40af43df-20260602T141421322197+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ff39959f5956

## What looked useful

Top residual preservation is a decision-boundary accuracy and reconstruction-error mechanism, not an unqualified predictive-quality win: at 2% residual retention it improved accuracy by about +1.2 points over plain ternary at the same 2.96 estimated bits/weight, but increased NLL by about +0.34 versus dense and +0.20 versus random residual control.

## Boundaries and scale limits

Tested only synthetic nonlinear-teacher MLP classification with 5 seeds, no real datasets, no transformer/LM task, no quantization-aware training, no deployment kernel, and only a simple index-plus-fp16 residual storage estimate.

## Claim scope

Bounded synthetic small-MLP post-training quantization: top-magnitude residual side channels on ternary weights improve validation accuracy and weight reconstruction versus plain ternary and random residual controls, but worsen cross-entropy loss and wrong-prediction confidence.

## Why it stopped

Bounded synthetic evidence is mixed: top residual preservation improves accuracy/reconstruction but worsens cross-entropy and wrong-prediction confidence, so it does not support a paper-positive broad quality claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should test calibrated residual-preserved ternary quantization on real small-model tasks with accuracy and NLL/ECE success thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibration-aware residual-preserved ternary quantization on real small-model tasks
- Success threshold: Calibrated top residual ternary must beat plain ternary and random residual controls on accuracy while not increasing NLL or ECE by more than 1% relative at the same estimated bits/weight.
- Stop condition: Stop if top residual accuracy gains disappear on real tasks or calibration cannot remove the NLL/ECE regression at matched storage budgets.

## Evidence references

- Artifact root: `<local-path>/projects/residual-preserved-ternary-quantization-for-small-models-eb4c40af43df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
