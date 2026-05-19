# Layerwise and multi-layer direct-fidelity residual substitutes

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `58`
Project ID: `layerwise-and-multi-layer-direct-fidelity-residual-substit-5e515aa9cc`
Run ID: `layerwise-and-multi-layer-direct-fidelity-residual-substit-5e515aa9cc-20260514T190138308373+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Layerwise and multi-layer direct-fidelity residual substitutes: internal_generated:layerwise-and-multi-layer-direct-fidelity-residual-substit-5e515aa9cc

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Direct robustness run with dense and zero-skip baselines found contiguous multi-layer substitutes still incur large LM-loss deltas (+0.212 to +1.526 nats/token for MLP), so the result is not paper-ready despite layerwise mechanism support.

## Recommended next action

Stop this depth-4 follow-up branch: direct GPT-2-small patched-loss evidence supports single-layer substitution but falsifies the multi-layer preservation threshold, and the controller cap prevents recommending another deepen/retry follow-up.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/layerwise-and-multi-layer-direct-fidelity-residual-substit-5e515aa9cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
