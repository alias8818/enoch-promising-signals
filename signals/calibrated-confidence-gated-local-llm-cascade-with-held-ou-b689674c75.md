# Calibrated confidence-gated local LLM cascade with held-out serving metrics

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `calibrated-confidence-gated-local-llm-cascade-with-held-ou-b689674c75`
Run ID: `calibrated-confidence-gated-local-llm-cascade-with-held-ou-b689674c75-20260515T043522861980+0000`

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

- Internal Enoch project: Calibrated confidence-gated local LLM cascade with held-out serving metrics: internal_generated:calibrated-confidence-gated-local-llm-cascade-with-held-ou-b689674c75

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Medium direct evaluation found a near-baseline cascade with 31.7% lower mean latency, but temperature calibration barely beat raw max-probability gating and the benchmark was sentiment classification rather than full local LLM serving.

## Recommended next action

Stop this run as no-paper: the medium SST-2 validation supports confidence gating for latency reduction but not a strong calibration-specific or generative local LLM serving claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Generative local LLM confidence cascade with actual server tail latency
- Success threshold: Held-out quality at least 98% of fallback-only quality, mean latency at least 25% lower than fallback-only, p95 latency at least 10% lower than fallback-only, and calibrated gate measurably better than raw max-probability routing on at least two task families.
- Stop condition: Stop if calibrated routing fails to beat raw max-probability routing by a meaningful margin, if quality falls below 98% of fallback-only, or if actual p95 served latency is not improved under load.

## Evidence references

- Artifact root: `<local-path>/projects/calibrated-confidence-gated-local-llm-cascade-with-held-ou-b689674c75`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
