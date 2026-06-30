# Sensitivity-Guided Layer-Wise Residual Budget Allocation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sensitivity-guided-layer-wise-residual-budget-allocation-759060888dd0`
Run ID: `sensitivity-guided-layer-wise-residual-budget-allocation-759060888dd0-20260528T024631007257+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d16359ce1dba

## What looked useful

Layer ablation sensitivity was highly non-uniform. Under the same expected residual-drop budget of 3.5 dropped blocks over 10 layers with probabilities capped at 0.75, sensitivity-protect improved paired loss delta versus uniform by 0.322 on average and preserved about 5.7 percentage points more accuracy across four seeds.

## Boundaries and scale limits

Synthetic teacher classification task only; residual MLP only; inference-time residual-drop/skip allocation only; no real language-modeling corpus, transformer baseline, train-time schedule, parameter-matched GPT-2-small-class comparison, or full-scale validation.

## Claim scope

In a four-seed synthetic 10-block residual MLP probe, allocating an equal expected residual-drop budget away from layers with high ablation sensitivity preserved validation performance better than uniform allocation and much better than sensitivity-attacking allocation.

## Why it stopped

The mechanism is supported in a bounded synthetic residual-MLP proxy, but the evidence is not direct enough for a paper or broad transformer-training claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same allocator on a small transformer language-modeling task with real held-out loss and equal-compute uniform/drop-path controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sensitivity-guided residual-drop allocation in a small transformer language model
- Success threshold: Sensitivity-protect must beat uniform by at least 2 percent relative held-out loss degradation or at least 0.02 nats/token absolute loss degradation in paired comparisons across most seeds/checkpoints, with sensitivity-attack worse than uniform.
- Stop condition: Stop if sensitivity is not meaningfully non-uniform, if sensitivity-protect fails to beat uniform in paired held-out loss on two independent seeds/checkpoints, or if equal-budget invariants cannot be maintained.

## Evidence references

- Artifact root: `<local-path>/projects/sensitivity-guided-layer-wise-residual-budget-allocation-759060888dd0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
