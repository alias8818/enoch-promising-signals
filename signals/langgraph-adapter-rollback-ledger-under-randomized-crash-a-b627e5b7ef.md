# LangGraph adapter rollback ledger under randomized crash and concurrent retry faults

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `langgraph-adapter-rollback-ledger-under-randomized-crash-a-b627e5b7ef`
Run ID: `langgraph-adapter-rollback-ledger-under-randomized-crash-a-b627e5b7ef-20260515T185923156612+0000`

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

- Internal Enoch project: LangGraph adapter rollback ledger under randomized crash and concurrent retry faults: internal_generated:langgraph-adapter-rollback-ledger-under-randomized-crash-a-b627e5b7ef

## What looked useful

Across 1,500 Tier 2 jobs per variant plus a 300-job high-crash sensitivity run per variant, rollback_ledger achieved 1.000 invariant_ok_rate with zero duplicate-effect jobs and zero orphan charges/reserves; checkpoint_only had 1,467 duplicate-effect jobs and 349 orphan failed jobs in Tier 2, while idempotency_only and ledger_no_reconcile fixed duplicates but left all 349 permanent-failure jobs uncompensated.

## Boundaries and scale limits

Evidence is local and synthetic: crashes are injected exceptions rather than OS process kills, the external service is modeled with SQLite rows, the workflow is compact, and the test does not replay production Enoch controller traces or distributed storage behavior.

## Claim scope

In a bounded local LangGraph invocation harness with SQLite-backed durable checkpoints, side effects, and ledger state, a rollback-ledger adapter preserved exactly-once and rollback invariants across fixed-seed randomized crash injection and four-worker concurrent retries; checkpoint-only, idempotency-only, and no-reconcile controls did not.

## Why it stopped

No-paper closure: medium local evidence supports the mechanism, but the crash model and external-service model are not strong enough for publication-grade LangGraph adapter claims.

## Recommended next action

Run a deepen follow-up that replaces injected exceptions with process-level kill/restart and moves external effects to an independently durable service emulator while preserving the same fixed-seed invariant metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Process-kill rollback ledger validation with external service emulator
- Success threshold: rollback_ledger invariant_ok_rate >= 0.999 with zero orphan charge/reserve jobs and at least 100x fewer duplicate-effect jobs than checkpoint_only; idempotency_only or ledger_no_reconcile must fail the permanent-failure compensation invariant.
- Stop condition: Stop if rollback_ledger produces any reproducible orphan charge/reserve after recovery, leaves prepared ledger entries unreconciled after the recovery pass, or fails to outperform idempotency_only on permanent-failure compensation.

## Evidence references

- Artifact root: `<local-path>/projects/langgraph-adapter-rollback-ledger-under-randomized-crash-a-b627e5b7ef`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
