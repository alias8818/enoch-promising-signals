# Redundant evidence consensus with CPU-only small ensembles

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `redundant-evidence-consensus-with-cpu-only-small-ensembles-afa3d67df415`
Run ID: `redundant-evidence-consensus-with-cpu-only-small-ensembles-afa3d67df415-20260531T125643494446+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8408ff0055b8

## What looked useful

Redundant evidence consensus is conditionally useful: trimmed consensus improved redundant-regime accuracy over dense all-features by +0.0164 at 20% corruption and +0.0217 at 40% corruption, winning 20/20 seeds in both cases. In the single-informative control it was harmful, losing -0.1688 accuracy at 20% corruption and -0.0679 at 40% corruption. Majority vote was the strongest accuracy aggregator under redundant corruption.

## Boundaries and scale limits

Synthetic data only; no real dataset, no natural redundancy discovery, no large neural model, no retrieval/system benchmark, and no comparison to broader robust-learning baselines. The run was CPU-only and completed in under one minute.

## Claim scope

In a NumPy-only synthetic binary benchmark with 9 known evidence channels, channel-wise small logistic ensembles improve robustness to adversarial channel corruption only when redundant label evidence is actually present. The effect is consistent across 20 seeds for 20-40% corruption, but it is not a general-purpose method.

## Why it stopped

Synthetic controlled evidence supports the mechanism under known redundancy but also shows a serious failure mode when redundancy is absent; this is a proxy result, not a full validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should validate redundancy gating and consensus on a real or semi-real multi-view dataset before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data redundancy gating for CPU-only consensus ensembles
- Success threshold: On real or semi-real redundant data, gated consensus or majority consensus improves corrupted-condition accuracy by at least 1 percentage point over dense and plain mean baselines without losing more than 0.5 percentage points on clean data; on no-redundancy controls the gate disables consensus or limits harm below 0.5 percentage points.
- Stop condition: Stop if the redundancy gate cannot distinguish redundant from single-informative controls, or if consensus harms clean/no-redundancy accuracy by more than 0.5 percentage points in paired evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/redundant-evidence-consensus-with-cpu-only-small-ensembles-afa3d67df415`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
