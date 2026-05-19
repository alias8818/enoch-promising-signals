# Real-LM Confidence-Gated Anchor KV Eviction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-lm-confidence-gated-anchor-kv-eviction-cc5be8c44e`
Run ID: `real-lm-confidence-gated-anchor-kv-eviction-cc5be8c44e-20260515T062122452644+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f7310c1b4b69

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 1 real-LM direct KV-pruning evidence supports the mechanism, but the validation is small and controlled rather than publication-grade.

## Recommended next action

Stop this run as Tier 1 mechanism-supported but not paper-ready; run a bounded medium confirmation with natural long-context tasks, decode accuracy, latency/memory metrics, and budget/threshold ablations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium real-LM benchmark for confidence-gated anchor KV eviction
- Success threshold: At matched retained KV fractions, confidence-gated anchor eviction improves decode accuracy or answer NLL degradation by at least 20% relative to recent-only on both synthetic and natural tasks, with measured memory reduction and no more than 10% latency regression versus recent-only pruning.
- Stop condition: Stop if confidence-gated anchor eviction fails to beat recent-only by 20% on either synthetic or natural tasks at two or more KV budgets, or if latency overhead erases the practical memory/retention benefit.

## Evidence references

- Artifact root: `<local-path>/projects/real-lm-confidence-gated-anchor-kv-eviction-cc5be8c44e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
