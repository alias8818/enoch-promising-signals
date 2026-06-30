# Quantized Evidence Ledger for Safer Small Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-evidence-ledger-for-safer-small-agents-72049aa3ca7a`
Run ID: `quantized-evidence-ledger-for-safer-small-agents-72049aa3ca7a-20260527T165744934367+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fe6b5049c075

## What looked useful

A 3-bit per-hazard ledger using 12 bits reduced unsafe execution by about 0.36 absolute versus recent_window_3 in random and late-signal conditions with similar false-block rates, while a 4-bit ledger matched the float ledger in this synthetic setup using 16 bits instead of 128 bits. The mechanism is order-sensitive: recent_window_3 beat the ledger in the misleading-prefix condition.

## Boundaries and scale limits

No real LLM agents, real tool traces, learned evidence extraction, or deployment feedback loops were tested. The benchmark uses synthetic independent binary evidence and fixed hand-coded policies over 160,000 episodes per evidence-order family.

## Claim scope

In a bounded synthetic safety-decision benchmark, compact per-hazard quantized evidence ledgers reduced unsafe execution versus a same-storage recent-context baseline when evidence order was random or when relevant signals arrived late, but failed against a recency baseline when the evidence order was adversarially favorable to recent items.

## Why it stopped

This is a proxy synthetic useful signal with a clear order-sensitivity counterexample, not full validation or paper-grade evidence.

## Recommended next action

Run a bounded real-trace follow-up that adds recency-aware or decayed ledger variants and compares them on actual small-agent tool-call safety decisions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Order-Robust Quantized Evidence Ledgers on Real Small-Agent Tool Traces
- Success threshold: Recency-aware quantized ledger reduces unsafe execution by at least 20% relative versus recent-context baseline with no more than 5 percentage point absolute false-block increase across all tested trace-order regimes.
- Stop condition: Stop if the recency-aware quantized ledger fails to beat recent-context unsafe execution in any trace-order regime or requires storage/context overhead comparable to a full-precision ledger.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-evidence-ledger-for-safer-small-agents-72049aa3ca7a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
