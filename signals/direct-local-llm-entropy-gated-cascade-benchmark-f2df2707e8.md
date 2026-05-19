# Direct Local LLM Entropy-Gated Cascade Benchmark

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `83`
Project ID: `direct-local-llm-entropy-gated-cascade-benchmark-f2df2707e8`
Run ID: `direct-local-llm-entropy-gated-cascade-benchmark-f2df2707e8-20260515T042506776797+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7250694f55c4

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

The controlled direct local benchmark failed the predefined viability threshold: 95% large-model accuracy retention required 81-91% escalation and was slower than always-large, while speed-positive gates fell below the retention target.

## Recommended next action

Stop this entropy-only Tier 1 run as a direct threshold failure; only pursue a bounded follow-up with calibrated confidence features and real held-out serving metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated confidence-gated local LLM cascade with held-out serving metrics
- Success threshold: Held-out cascade accuracy is at least 95% of always-large accuracy, escalation rate is at most 70%, and measured end-to-end latency or throughput improves by at least 1.2x versus always-large.
- Stop condition: Stop if the calibrated held-out gate cannot exceed 1.0x measured speedup while meeting 95% accuracy retention, or if meeting retention still requires more than 70% escalation.

## Evidence references

- Artifact root: `<local-path>/projects/direct-local-llm-entropy-gated-cascade-benchmark-f2df2707e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
