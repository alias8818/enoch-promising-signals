# Tool-Router Ledger for Local Agent Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tool-router-ledger-for-local-agent-cascade-84119afcd5a4`
Run ID: `tool-router-ledger-for-local-agent-cascade-84119afcd5a4-20260601T073840900098+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5734810fcadd

## What looked useful

Do not pursue ledger-only cold-start routing as a replacement for a competent static router. A contextual outcome ledger appears useful as an adaptive layer seeded from an existing prior, especially after tool-quality drift.

## Boundaries and scale limits

Synthetic task generator only; no real LLM calls, real tool side effects, real local-agent traces, human quality judgments, multi-process orchestration overhead, or production failure modes were tested.

## Claim scope

In a deterministic synthetic local-agent cascade with context-specific tool reliability, costs, latencies, one mid-run drift event, and binary feedback, cold-start contextual ledgers underperform a strong static prior, while prior-seeded contextual ledgers slightly improve post-drift success/regret/cost/latency over that static prior.

## Why it stopped

No-paper closure: this is a synthetic/proxy useful signal with mixed results, not direct publication-grade validation.

## Recommended next action

Run a bounded real-trace replay where a seeded contextual ledger routes actual local-agent tool calls and is compared to the existing static router on success labels, cost, latency, and recovery depth.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace replay for seeded contextual tool-router ledger
- Success threshold: Seeded contextual ledger has post-shift success-rate delta above 0 with 95% paired CI excluding 0, mean regret at least 5% lower than static prior, and no statistically significant increase in mean cost or latency.
- Stop condition: Stop if the ledger fails to beat static prior on post-shift success or increases either cost or latency by more than 5% with paired CI excluding 0.

## Evidence references

- Artifact root: `<local-path>/projects/tool-router-ledger-for-local-agent-cascade-84119afcd5a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
