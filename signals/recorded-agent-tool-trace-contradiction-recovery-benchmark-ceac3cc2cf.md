# Recorded Agent Tool-Trace Contradiction Recovery Benchmark

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `58`
Project ID: `recorded-agent-tool-trace-contradiction-recovery-benchmark-ceac3cc2cf`
Run ID: `recorded-agent-tool-trace-contradiction-recovery-benchmark-ceac3cc2cf-20260514T010336651431+0000`

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

- Internal Enoch project: Recorded Agent Tool-Trace Contradiction Recovery Benchmark: internal_generated:recorded-agent-tool-trace-contradiction-recovery-benchmark-ceac3cc2cf

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Bounded synthetic validation is an early falsification of paper-readiness, not a full validation: no real recorded agent traces were available and a modest local model achieved 90/90 contradiction recovery across trace conditions.

## Recommended next action

Stop at depth 4: the synthetic benchmark showed measurable contradiction-recovery behavior but failed the Tier 4 paper gate because it used no real recorded traces and was saturated by Qwen2.5-1.5B-Instruct.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/recorded-agent-tool-trace-contradiction-recovery-benchmark-ceac3cc2cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
