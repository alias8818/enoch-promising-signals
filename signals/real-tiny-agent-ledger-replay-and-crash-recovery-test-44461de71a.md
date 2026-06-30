# Real Tiny-Agent Ledger Replay and Crash-Recovery Test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-tiny-agent-ledger-replay-and-crash-recovery-test-44461de71a`
Run ID: `real-tiny-agent-ledger-replay-and-crash-recovery-test-44461de71a-20260529T084206951705+0000`

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

- Parent run decision: Tiny Agent Evidence Ledger: enoch://control-plane/projects/tiny-agent-evidence-ledger-a9d14b1b6ca9/runs/tiny-agent-evidence-ledger-a9d14b1b6ca9-20260528T145913291533+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5b66d5fcf0a5

## What looked useful

Ledger replay worked in the tested crash windows only when side effects were idempotent by durable op ID. The non-idempotent control failed in all six crash-after-effect-before-commit cases, duplicating side effects.

## Boundaries and scale limits

Local JSON/JSONL filesystem harness only; single worker; deterministic tasks; one injected process crash per case; no concurrent workers, torn writes, corrupt ledger recovery, remote APIs without idempotency keys, real LangGraph integration, or power-loss testing.

## Claim scope

In a six-task deterministic tiny-agent harness, an append-only intent/commit ledger plus durable sink-level idempotency op IDs recovered the exact no-crash final state across all 24 single hard-crash injection points and the no-crash reference.

## Why it stopped

Tier 1 direct test produced a useful mechanism signal but not publication-grade evidence; the result is intentionally scoped to a local tiny-agent crash harness.

## Recommended next action

Run a bounded deepen test with concurrent workers, repeated crashes, and corrupt/torn ledger records before considering any broader agent-runtime claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Concurrent Tiny-Agent Ledger Replay With Torn-Write Recovery
- Success threshold: 100% final-state equivalence to a serial no-crash reference across all planned concurrent crash/corruption cases, with zero duplicate sink effects and no lost committed tasks.
- Stop condition: Stop as negative if any committed task is lost, any sink op is duplicated, or recovery requires manual ledger repair in the bounded concurrent/corruption matrix.

## Evidence references

- Artifact root: `<local-path>/projects/real-tiny-agent-ledger-replay-and-crash-recovery-test-44461de71a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
