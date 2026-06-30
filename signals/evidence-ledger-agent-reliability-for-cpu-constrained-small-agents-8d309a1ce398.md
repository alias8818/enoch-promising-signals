# Evidence-Ledger Agent Reliability for CPU-Constrained Small Agents

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `evidence-ledger-agent-reliability-for-cpu-constrained-small-agents-8d309a1ce398`
Run ID: `evidence-ledger-agent-reliability-for-cpu-constrained-small-agents-8d309a1ce398-20260607T082856412498+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/240bf78d3f82

## What looked useful

Evidence ledgers for constrained small agents need temporal/update-aware policies. A naive reliability-first ledger preserved stale high-reliability claims and was much worse than recency; a cautious ledger showed a limited abstention-based reliability signal only at larger budget and higher noise.

## Boundaries and scale limits

Synthetic stdlib benchmark only; no real LLM inference, natural-language parsing, tool-use traces, human-labeled supports, long-horizon tasks, or deployment-scale workloads. Medium run used 90,000 agent-scenario evaluations and completed in 5.923 seconds on one CPU process.

## Claim scope

In a deterministic synthetic mutable-fact claim-stream benchmark with fixed memory budgets of 4, 8, and 12 records, a source-reliability evidence ledger did not outperform a recency-window baseline on accuracy or unsupported-claim rate; a cautious ledger only reduced unsupported claims in some higher-noise, larger-budget conditions by abstaining more.

## Why it stopped

No-paper useful signal: bounded synthetic evidence early-falsified the broad claim that explicit evidence ledgers alone improve reliability for CPU-constrained small agents.

## Recommended next action

Run a bounded deepen follow-up testing an adaptive recency-plus-source ledger with calibrated abstention against the same recency baseline and at least one real small-agent trace dataset.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive temporal evidence ledger for mutable small-agent facts
- Success threshold: At least 30% relative unsupported-rate reduction versus recent_window, no more than 5 percentage points absolute accuracy loss, coverage at least 0.90, and throughput at least 20,000 synthetic scenarios/sec on one CPU process.
- Stop condition: Stop if adaptive scoring fails to beat recent_window on unsupported rate in at least two medium synthetic noise/budget regimes or requires more than 5 percentage points accuracy loss to do so.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-for-cpu-constrained-small-agents-8d309a1ce398`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
