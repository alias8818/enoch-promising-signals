# Position-Weighted Multi-Hot Objective for Token Superposition

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `87`
Project ID: `position-weighted-multi-hot-objective-for-token-superposition-24789cd22f88`
Run ID: `position-weighted-multi-hot-objective-for-token-superposition-24789cd22f88-20260514T112154317177+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `87`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 12}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- external source URL present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Efficient Pre-Training with Token Superposition: https://arxiv.org/abs/2605.06546
- Token Superposition for Long-Context Anchor Compression: https://arxiv.org/abs/2605.06546

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Synthetic proxy evidence supports a narrow mechanism but is mixed across weighting formulations and is not direct/full validation.

## Recommended next action

Stop this run as proxy-only, no-paper evidence; next action is a bounded real-corpus CE-plus-position-weighted-multi-hot auxiliary experiment if a deeper tier is launched.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus auxiliary position-weighted multi-hot objective for causal transformers
- Success threshold: Position-weighted auxiliary loss improves future-window nDCG or weighted recall by at least 5% relative over CE plus unweighted multi-hot while keeping validation CE within 1% of CE-only, with consistent direction across seeds.
- Stop condition: Stop if the position-weighted auxiliary fails to beat CE plus unweighted multi-hot on future-window metrics or degrades validation CE by more than 1%.

## Evidence references

- Artifact root: `<local-path>/projects/position-weighted-multi-hot-objective-for-token-superposition-24789cd22f88`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
