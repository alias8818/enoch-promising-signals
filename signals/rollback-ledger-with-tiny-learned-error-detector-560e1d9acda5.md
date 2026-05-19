# Rollback Ledger with Tiny Learned Error Detector

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `83`
Project ID: `rollback-ledger-with-tiny-learned-error-detector-560e1d9acda5`
Run ID: `rollback-ledger-with-tiny-learned-error-detector-560e1d9acda5-20260515T174853188011+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6c0528d418f3

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Proxy mechanism support only; not a full validation. The learned detector nearly matched a structural guard on exposed synthetic state, so the result is not publication-grade.

## Recommended next action

Stop this run as proxy-only: the rollback-ledger mechanism worked on a synthetic task, but direct autoregressive-model evidence is required before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Rollback Ledger Detector on Real Structured Autoregressive Generation
- Success threshold: On at least one real structured generation task, learned rollback improves validity or task accuracy by at least 20% relative over the strongest non-learned baseline without more than 25% latency overhead, with stable results across at least three random seeds.
- Stop condition: Stop if learned rollback fails to beat constrained decoding or verifier-only reranking on validity/task accuracy at matched latency, or if detector calibration collapses into excessive false positives that exhaust the rollback budget.

## Evidence references

- Artifact root: `<local-path>/projects/rollback-ledger-with-tiny-learned-error-detector-560e1d9acda5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
