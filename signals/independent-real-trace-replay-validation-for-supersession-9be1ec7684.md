# Independent real-trace replay validation for supersession-aware drift ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `independent-real-trace-replay-validation-for-supersession-9be1ec7684`
Run ID: `independent-real-trace-replay-validation-for-supersession-9be1ec7684-20260621T135903461765+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-agent repeated-task drift ledger verification: enoch://control-plane/projects/real-agent-repeated-task-drift-ledger-verification-a65d7d34c3/runs/real-agent-repeated-task-drift-ledger-verification-a65d7d34c3-20260621T095552837786+0000
- Parent run decision: Real agent trace validation for repeated-task drift ledgers: enoch://control-plane/projects/real-agent-trace-validation-for-repeated-task-drift-ledger-1854866d13/runs/real-agent-trace-validation-for-repeated-task-drift-ledger-1854866d13-20260621T101202194194+0000

## What looked useful

Supersession accounting eliminated stale current-state retrieval on the tested real local trace: supersession_ledger reached 5/5 current accuracy and 0/5 stale retrieval, while raw transcript and non-supersession ledgers reached 0/5 current accuracy and 5/5 stale retrieval.

## Boundaries and scale limits

Single worker run, five entities, rule-based and explicit TRACE_OBS observation extraction, deterministic current-state queries, no multi-session held-out corpus and no autonomous extraction validation.

## Claim scope

On five supersession current-state tasks extracted from one local Codex command-execution trace, an explicit supersession ledger returned the latest artifact observation while raw transcript search and non-supersession ledgers returned stale observations.

## Why it stopped

The mechanism is supported on a tiny local real-trace replay, but the evidence is too small and too instrumented to satisfy the requested broad Tier-3 validation or paper-positive threshold.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded deepen test should use at least 50 held-out real agent traces with naturally occurring supersessions and autonomous observation extraction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out multi-session supersession replay with autonomous observation extraction
- Success threshold: Supersession ledger current accuracy at least 0.80 and at least +0.10 absolute over the best non-supersession baseline, with stale retrieval rate at least 0.20 lower than best baseline on 50+ held-out traces.
- Stop condition: Stop if fewer than 50 held-out traces with genuine supersessions are available, autonomous extraction F1 is below 0.70, or the supersession ledger fails to beat the best non-supersession baseline by 10 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/independent-real-trace-replay-validation-for-supersession-9be1ec7684`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
