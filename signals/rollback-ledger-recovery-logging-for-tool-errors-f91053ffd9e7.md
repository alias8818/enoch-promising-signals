# Rollback Ledger: Recovery Logging for Tool Errors

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `rollback-ledger-recovery-logging-for-tool-errors-f91053ffd9e7`
Run ID: `rollback-ledger-recovery-logging-for-tool-errors-f91053ffd9e7-20260609T031113668928+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/480fb0c46c7f

## What looked useful

Rollback ledgers are mechanistically useful for tool-error recovery when they capture enough inverse/pre-state information, but the naive full-snapshot design is expensive: about 60.2 KB mean log volume and 2.04 ms per trial versus 2.85 KB and 0.040 ms for plain replay in this harness.

## Boundaries and scale limits

Synthetic CPU-only simulation; no real filesystem/database tools, persisted crash recovery, concurrent calls, distributed state, fsync behavior, or agent-runtime integration were tested.

## Claim scope

In a deterministic synthetic stateful tool workflow with injected before/mid/after failures, full pre-state rollback-ledger entries recovered the exact committed-prefix state in 5000/5000 trials, while no recovery and naive attempted-operation replay did not.

## Why it stopped

Evidence is bounded to synthetic recovery and supports the mechanism, but it is not direct production or publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next implement a durable compact-inverse tool wrapper and test process-kill recovery on real file and SQLite side effects.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Durable compact rollback ledger for real tool-wrapper crashes
- Success threshold: At least 99% exact recovery over 1000 injected-kill trials per tool type with less than 5x mean log-volume overhead versus plain event logging and documented latency cost.
- Stop condition: Stop if compact inverse entries cannot restore exact committed-prefix state above 95% in the first 200 kill-injection trials or if durable logging overhead exceeds 10x without a clear optimization path.

## Evidence references

- Artifact root: `<local-path>/projects/rollback-ledger-recovery-logging-for-tool-errors-f91053ffd9e7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
