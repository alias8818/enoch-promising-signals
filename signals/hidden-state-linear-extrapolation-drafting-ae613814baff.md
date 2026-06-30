# Hidden-State Linear Extrapolation Drafting

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `hidden-state-linear-extrapolation-drafting-ae613814baff`
Run ID: `hidden-state-linear-extrapolation-drafting-ae613814baff-20260531T205910917069+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/435fc4b4d6a3

## What looked useful

Corrected draft-only evaluation found linear hidden-state extrapolation matched 1/224 future greedy tokens (0.45%), below zero-order hidden reuse at 5/224 (2.23%), damped linear at 2/224 (0.89%), and a prompt-token unigram control at 20/224 (8.93%).

## Boundaries and scale limits

This was a CPU-only small-model inference probe, not a large-model, learned-transition, multi-layer, non-greedy, or end-to-end speculative decoding speedup validation.

## Claim scope

Plain first-order extrapolation of the final-layer hidden state from one distilgpt2 context pass does not produce useful greedy draft tokens on 32 fixed prompts and draft horizons 2-8.

## Why it stopped

Bounded real-model proxy produced an early falsification rather than full validation: the simple extrapolator failed on true draft horizons against cheap controls.

## Recommended next action

Stop this plain final-layer linear extrapolation path; only revisit with an explicitly different learned or layer-selected transition that first beats cheap controls on draft-only exact match.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/hidden-state-linear-extrapolation-drafting-ae613814baff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
