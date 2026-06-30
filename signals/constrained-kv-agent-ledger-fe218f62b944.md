# Constrained KV Agent Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `constrained-kv-agent-ledger-fe218f62b944`
Run ID: `constrained-kv-agent-ledger-fe218f62b944-20260603T224913554560+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/71331c498ab7

## What looked useful

A constrained KV ledger is a scoped memory mechanism: it can perfectly retain a known 64-key watchlist under a 64-slot budget in the simulator, but it collapses to plain LRU behavior on unhinted or adversarial queries.

## Boundaries and scale limits

CPU-only deterministic simulation; no LLM extraction, natural-language traces, real agent planning, serving latency, or large-scale model evaluation. Main run used 500 trials per mode with 4000 events, 1024 keys, 64 watched keys, 64 queries, 32-event recent context, and 64 ledger slots.

## Claim scope

Synthetic event-stream lookup tasks show that a constrained key-value ledger improves exact recall over recent context and unfiltered LRU when query-relevant keys are explicitly known, but not when relevance is absent or wrong.

## Why it stopped

Synthetic proxy evidence supports the mechanism only under explicit relevance signals and is insufficient for publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should test model-in-the-loop ledger extraction and retrieval on natural-language task traces with equal token budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-in-the-loop constrained KV ledger on natural-language traces
- Success threshold: At least 20 percentage-point accuracy improvement over both recent-context and LRU baselines in focused traces, with no claimed advantage in unhinted/adversarial traces unless directly observed.
- Stop condition: Stop if ledger extraction or stale-write errors reduce focused-trace accuracy to within 5 percentage points of the best baseline across two seeds.

## Evidence references

- Artifact root: `<local-path>/projects/constrained-kv-agent-ledger-fe218f62b944`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
