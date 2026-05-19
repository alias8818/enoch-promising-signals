# Fused real-KV anchor router latency validation

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `fused-real-kv-anchor-router-latency-validation-1c251337a8`
Run ID: `fused-real-kv-anchor-router-latency-validation-1c251337a8-20260515T135606547548+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
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

- Internal Enoch project: Fused real-KV anchor router latency validation: internal_generated:fused-real-kv-anchor-router-latency-validation-1c251337a8

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 4 validation did not produce publication-grade support: anchor routing was slower than dense at 512-4096 tokens, long-context speedups traded off too much dense-output fidelity except narrow 16k cases, random same-sparsity routing was faster, and the long-context evidence used tiled real K/V rather than true long-context traces.

## Recommended next action

Stop this depth-4 follow-up: the direct operator evidence is mixed but fails the strict paper-readiness gate, and the controller lineage cap prevents recommending another chained deepen/retry run.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/fused-real-kv-anchor-router-latency-validation-1c251337a8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
