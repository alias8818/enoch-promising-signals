# Trainable FSM Anchor Memory Versus Parameter-Matched Sequence Models

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trainable-fsm-anchor-memory-versus-parameter-matched-seque-828de5c847`
Run ID: `trainable-fsm-anchor-memory-versus-parameter-matched-seque-828de5c847-20260520T030706953086+0000`

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

- Parent run decision: Differentiable Finite-State Memory for Exact Anchors: enoch://control-plane/projects/differentiable-finite-state-memory-for-exact-anchors-3bccd6b518cb/runs/differentiable-finite-state-memory-for-exact-anchors-3bccd6b518cb-20260519T225409227894+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/cd36c05e0d83

## What looked useful

The anchor-memory mechanism passed the predefined threshold twice: at 450 steps, length-128 mean accuracy was FSM 0.681, GRU 0.423, Transformer 0.255; at 1200 steps, FSM 0.750, GRU 0.502, Transformer 0.270.

## Boundaries and scale limits

Synthetic-only Tier 1 controlled test; no natural-language data, no GPT-2-small-class baseline, no large cardinality sweep, no extensive hyperparameter tuning, and no publication-grade robustness ablations.

## Claim scope

In a small synthetic last-value anchor retrieval task with 8 anchors, 4 values, train length 32, and eval length 128, a 1.3k-parameter trainable FSM anchor memory outperformed parameter-near GRU and Transformer baselines across 3 seeds.

## Why it stopped

Tier 1 direct evidence supports the mechanism but is synthetic and too small for publication readiness.

## Recommended next action

Run a medium bounded confirmation with stronger tuned parameter-matched baselines, larger anchor/value cardinalities, and a GPT-2-small-class sequence baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Anchor-Memory Confirmation Against Tuned Sequence Baselines
- Success threshold: FSM anchor memory mean longer-sequence accuracy exceeds the best tuned sequence baseline by >=0.10 absolute while matching or exceeding 0.80 in-distribution accuracy, with no single seed reversing the effect.
- Stop condition: Stop if tuned baselines close the length-generalization gap below 0.05 absolute or if FSM fails to exceed 0.80 in-distribution accuracy after documented reasonable tuning.

## Evidence references

- Artifact root: `<local-path>/projects/trainable-fsm-anchor-memory-versus-parameter-matched-seque-828de5c847`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
