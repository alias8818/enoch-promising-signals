# Durable rollback ledger for real tool adapters under crash and retry faults

Status: `useful_signal`
Project ID: `durable-rollback-ledger-for-real-tool-adapters-under-crash-7d5a4300db`
Run ID: `durable-rollback-ledger-for-real-tool-adapters-under-crash-7d5a4300db-20260515T185406794265+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1108e88b6f2f

## What looked useful

Baseline retry left duplicate SQLite rows and/or receipt lines in 100/100 crash trials, while ledger recovery plus retry converged to one row and one receipt line in 100/100 trials.

## Boundaries and scale limits

Not integrated with LangGraph; no network APIs, concurrent workers, partial adapter writes, crashes during ledger commit, production credentials, or large adapter diversity were tested.

## Claim scope

A pre-effect durable compensation ledger restored exactly-once visible state in a controlled local subprocess crash/retry harness using real SQLite and filesystem adapters across five injected crash boundaries and 20 repetitions per boundary.

## Why it stopped

Controlled Tier 1 evidence supports the mechanism but is not broad or integrated enough for paper-ready claims.

## Recommended next action

Run a medium direct confirmation by wiring the same pre-effect compensation ledger into actual LangGraph tool adapter wrappers with local HTTP, SQLite, filesystem, randomized crash points, and concurrent retry workers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LangGraph adapter rollback ledger under randomized crash and concurrent retry faults
- Success threshold: Ledger variant preserves all adapter invariants in at least 99% of 1000 randomized crash/retry trials and beats the no-ledger baseline by at least 50 percentage points without any committed-run compensation errors.
- Stop condition: Stop as negative if any committed run is compensated, if recovery is non-idempotent under concurrent workers, or if invariant success is below 95% after fixing only harness bugs.

## Evidence references

- Artifact root: `<local-path>/projects/durable-rollback-ledger-for-real-tool-adapters-under-crash-7d5a4300db`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
