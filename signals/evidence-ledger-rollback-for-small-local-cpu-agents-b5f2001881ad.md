# Evidence-ledger rollback for small local CPU agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-rollback-for-small-local-cpu-agents-b5f2001881ad`
Run ID: `evidence-ledger-rollback-for-small-local-cpu-agents-b5f2001881ad-20260526T024931004654+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/77620b22bbc3

## What looked useful

Rollback ledgers reached 100% accuracy and 0 stale corrected facts when budget could hold the 80 target facts, degraded predictably to 50%/75% accuracy at smaller budgets, and outperformed baselines that either forgot relevant facts or retained stale corrected facts.

## Boundaries and scale limits

Synthetic structured events only; no LLM natural-language parsing, no real tool traces, no multi-step planning tasks, and relevance compaction used explicit item/distractor key namespaces. The result should not be claimed for deployed agents without a real harness validation.

## Claim scope

In a deterministic synthetic memory benchmark for small CPU-agent context managers, an explicit evidence ledger with rollback/retraction semantics preserved current factual answers and eliminated stale active corrected facts better than append-only windows and naive summary memory under fixed token budgets.

## Why it stopped

Synthetic-only evidence supports the mechanism but is not direct/full validation of real small local CPU agents.

## Recommended next action

Stop this run as no-paper useful signal; next run should embed the ledger API in a real small local agent harness with natural-language observations and logged correction/retraction tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-agent rollback harness for evidence-ledger memory
- Success threshold: Ledger reduces stale-evidence answer rate by at least 50% relative to the best baseline while preserving or improving overall task success and adding less than 20% wall-clock overhead on the local CPU worker.
- Stop condition: Stop if natural-language/event adapters cannot reliably identify retraction targets above 90% on a labeled smoke set, or if ledger overhead exceeds 20% while task success is not better than the best baseline.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-for-small-local-cpu-agents-b5f2001881ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
