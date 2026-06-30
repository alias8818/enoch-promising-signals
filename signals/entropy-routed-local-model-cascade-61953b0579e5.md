# Entropy-Routed Local Model Cascade

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `entropy-routed-local-model-cascade-61953b0579e5`
Run ID: `entropy-routed-local-model-cascade-61953b0579e5-20260524T194219125923+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a9550f8d4233

## What looked useful

At 20% escalation, entropy routing beat random routing by +0.0643 accuracy on digits, +0.0227 on wine, and +0.0184 on breast_cancer, with entropy AUC for cheap-model errors between 0.8033 and 0.9571.

## Boundaries and scale limits

Evidence is limited to small classical classifiers and tiny local datasets. It does not validate LLM-scale cascades, production serving latency, robustness under distribution shift, or full application quality.

## Claim scope

On three small built-in scikit-learn classification datasets, routing high-entropy predictions from a cheap GaussianNB classifier to a stronger ExtraTrees classifier improved accuracy over the cheap model and beat random routing at the same escalation rate.

## Why it stopped

Closed as no-paper useful signal because the local mechanism is supported only by small classical-model evidence, not by direct LLM-cascade or production-serving validation.

## Recommended next action

Run one bounded deepen experiment on a medium text or small local language-model benchmark with measured quality and latency before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Text Benchmark for Entropy-Routed Local Model Cascades
- Success threshold: At 20-40% escalation, entropy routing recovers at least 50% of the strong-model quality gain over cheap-only, beats random routing by at least two random-routing standard deviations, and uses less than 60% of strong-only measured inference cost.
- Stop condition: Stop if entropy AUC for cheap-model errors is below 0.65 on the medium task or if entropy routing fails to beat random routing at matched escalation on at least two of three splits.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-routed-local-model-cascade-61953b0579e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
