# Real agent trace validation for repeated-task drift ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-trace-validation-for-repeated-task-drift-ledger-1854866d13`
Run ID: `real-agent-trace-validation-for-repeated-task-drift-ledger-1854866d13-20260621T101202194194+0000`

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

- Parent run decision: Real-agent repeated-task drift ledger verification: enoch://control-plane/projects/real-agent-repeated-task-drift-ledger-verification-a65d7d34c3/runs/real-agent-repeated-task-drift-ledger-verification-a65d7d34c3-20260621T095552837786+0000
- Parent run decision: Evidence-Ledger Agent: Direct Artifact Verification on Repeated Tasks: enoch://control-plane/projects/evidence-ledger-agent-direct-artifact-verification-on-repeated-tasks-5b6213df6916/runs/evidence-ledger-agent-direct-artifact-verification-on-repeated-tasks-5b6213df6916-20260621T093532303887+0000

## What looked useful

Drift ledger accuracy was 1.000 with 0.000 stale drift violation rate over 60 queries per strategy. Transcript search reached 0.667 accuracy with 0.333 stale drift violation rate. The no-supersession ledger ablation had 0.000 accuracy and 1.000 stale drift violation rate, supporting supersession tracking as the active mechanism.

## Boundaries and scale limits

The validation uses deterministic memory mechanisms and hand-authored agent-like traces, not independent production agent traces or live LLM agent execution. It should be treated as bounded mechanism evidence, not publication-grade real-trace validation.

## Claim scope

On 12 hand-authored repeated-task drift traces expanded across five fixed seeds, an explicit supersession-aware drift ledger eliminated stale carryover and outperformed transcript-search, recent-window, flat-retrieval, no-memory, and no-supersession controls.

## Why it stopped

No-paper closure because the result is a bounded hand-authored trace replay mechanism signal rather than independent real-agent trace validation.

## Recommended next action

Run the same harness on an independently collected real agent trace corpus with naturally occurring repeated-task corrections and held-out domains.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Independent real-trace replay validation for supersession-aware drift ledgers
- Success threshold: At least 100 labeled real-trace queries, drift_ledger stale violation rate at least 25 percentage points lower than transcript_search, accuracy at least 10 percentage points higher than transcript_search, and ledger_no_supersession materially worse than drift_ledger.
- Stop condition: Stop if no independent labeled trace corpus is available, if transcript_search matches ledger within 5 percentage points on stale violation rate, or if ledger unknown/wrong-nonstale errors exceed transcript_search by more than 10 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-trace-validation-for-repeated-task-drift-ledger-1854866d13`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
