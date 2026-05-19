# Rollback Ledger for Tool-Use Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `rollback-ledger-for-tool-use-agents-d6033c25f3ec`
Run ID: `rollback-ledger-for-tool-use-agents-d6033c25f3ec-20260515T184948803071+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1108e88b6f2f

## What looked useful

Rollback ledgers are a viable mechanism for atomic recovery of reversible tool effects under mid-workflow failures, and the experiment identifies the expected hard boundary at irreversible side effects.

## Boundaries and scale limits

Evidence is synthetic and in-memory. It does not validate real LLM planning, real external APIs, durable ledger persistence, process crashes, concurrency, authorization failures, or distributed service behavior.

## Claim scope

In a deterministic synthetic tool-use environment with reversible bank, reservation, and inventory operations, a rollback ledger restored pre-run state for 100% of 49,975 injected-failure workflows, while the no-ledger baseline restored 0%. In mixed workflows with append-only email side effects, the ledger restored reversible state for 100% of faulted cases but could not guarantee full external atomicity after irreversible emission.

## Why it stopped

No-paper closure: the current result is a useful synthetic mechanism signal, not direct production-agent or paper-grade evidence.

## Recommended next action

Run a bounded direct-evidence follow-up that integrates the ledger with a real agent/tool framework, persisted ledger records, idempotency keys, and injected crash/retry failures.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Durable rollback ledger for real tool adapters under crash and retry faults
- Success threshold: Rollback-ledger policy restores reversible external state in at least 99% of injected-failure/crash workflows, reduces duplicate or partial side effects by at least 10x versus retry-only, and has zero ledger leaks in the completed test set.
- Stop condition: Stop as unsupported if durable rollback fails to beat retry-only by at least 2x on partial-side-effect rate or if ledger leaks/rollback errors exceed 1% of faulted workflows.

## Evidence references

- Artifact root: `<local-path>/projects/rollback-ledger-for-tool-use-agents-d6033c25f3ec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
