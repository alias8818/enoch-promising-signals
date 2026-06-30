# Real-trace crash-safe evidence ledger for small agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-crash-safe-evidence-ledger-for-small-agents-f0bf7440ee`
Run ID: `real-trace-crash-safe-evidence-ledger-for-small-agents-f0bf7440ee-20260607T190405353783+0000`

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

- Parent run decision: Cryptographic Evidence Ledger for Small Agents: enoch://control-plane/projects/cryptographic-evidence-ledger-for-small-agents-f8f165d73c81/runs/cryptographic-evidence-ledger-for-small-agents-f8f165d73c81-20260607T135205367284+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a62e72f4c9fb

## What looked useful

The Tier 1 direct test recovered all 36 real trace events in order, validated 144/144 independent crash-stage attempts and 108/108 resume-to-completion crash attempts, preserved the hash chain, and rejected a mutated committed record.

## Boundaries and scale limits

Single CPU worker, one local filesystem, one 36-event real trace, single writer, process hard exits only; no power-loss, kernel-crash, disk-full, concurrent-writer, rollback-adversary, network-filesystem, or high-volume validation.

## Claim scope

A per-record filesystem evidence ledger using temp write, file fsync, atomic rename, directory fsync, and hash-chain recovery preserved and verified one frozen 36-event real Codex agent trace under controlled hard process exits at four append stages.

## Why it stopped

No-paper closure: the mechanism is supported by a small direct real-trace crash test, but evidence is not publication-grade or broad enough for a paper.

## Recommended next action

Run a deepen follow-up on larger multi-agent real traces with SQLite WAL and naive JSONL baselines plus disk-full and concurrent-writer fault injection before considering any bounded paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-trace crash ledger baseline and fault comparison
- Success threshold: Filesystem ledger and SQLite WAL both recover 100% of expected committed events with zero invalid committed records across all traces and faults; naive JSONL shows at least one reproducible corruption/loss mode or the result is reframed as no advantage over simpler baselines.
- Stop condition: Stop if any ledger variant produces an invalid committed record, if source traces cannot be obtained locally, or if the filesystem ledger has materially worse integrity than SQLite WAL without a compensating operational advantage.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-crash-safe-evidence-ledger-for-small-agents-f0bf7440ee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
