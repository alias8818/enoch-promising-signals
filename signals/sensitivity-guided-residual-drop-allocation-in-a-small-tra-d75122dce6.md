# Sensitivity-guided residual-drop allocation in a small transformer language model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sensitivity-guided-residual-drop-allocation-in-a-small-tra-d75122dce6`
Run ID: `sensitivity-guided-residual-drop-allocation-in-a-small-tra-d75122dce6-20260528T041801033134+0000`

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

- Parent run decision: Sensitivity-Guided Layer-Wise Residual Budget Allocation: enoch://control-plane/projects/sensitivity-guided-layer-wise-residual-budget-allocation-759060888dd0/runs/sensitivity-guided-layer-wise-residual-budget-allocation-759060888dd0-20260528T024631007257+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d16359ce1dba

## What looked useful

Guided allocation consistently improved over uniform residual-drop in all three 2000-step seeds, with mean validation CE improvement 0.0106 nats, but it missed the predeclared 0.02 nats threshold and remained worse than no-drop by 0.0490 nats on average.

## Boundaries and scale limits

4-layer width-128 character model, 2000 training steps, one small corpus, three seeds, one residual-drop budget plus a no-drop sanity baseline; not GPT-2-scale, not tokenized web text, and not a broad hyperparameter sweep.

## Claim scope

Small causal transformer character-language-model test on Tiny Shakespeare: sensitivity-guided residual-drop allocation was compared against uniform residual-drop at matched mean drop probability 0.15 over three seeds.

## Why it stopped

Controlled small direct test showed a consistent but sub-threshold benefit versus uniform residual-drop, and residual-drop at p=0.15 was harmful versus no-drop in this setting.

## Recommended next action

Stop this run as no-paper useful signal; if continuing, run a bounded lower-drop-budget sweep with a no-drop control before any larger scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Lower-budget sensitivity-guided residual-drop sweep with no-drop control
- Success threshold: At any tested lower drop budget, guided improves final validation CE by at least 0.02 nats versus uniform residual-drop averaged over three seeds and is no worse than 0.005 nats behind no-drop.
- Stop condition: Stop if guided fails to clear 0.02 nats versus uniform at every lower budget or remains more than 0.005 nats worse than no-drop at the best budget.

## Evidence references

- Artifact root: `<local-path>/projects/sensitivity-guided-residual-drop-allocation-in-a-small-tra-d75122dce6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
