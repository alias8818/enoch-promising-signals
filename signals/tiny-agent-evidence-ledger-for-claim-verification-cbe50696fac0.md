# Tiny Agent Evidence Ledger for Claim Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-agent-evidence-ledger-for-claim-verification-cbe50696fac0`
Run ID: `tiny-agent-evidence-ledger-for-claim-verification-cbe50696fac0-20260526T043111042737+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ff40aea468c3

## What looked useful

Across 40 seeds x 500 cases in the main update condition, ledger stale-citation rate was 0.000 versus 0.32285 for scratch and 0.3791 for the active-blind ledger. In the no-update control, all variants had 0.000 stale citations. Label accuracy gains versus scratch were confounded by structured matching because the active-blind ledger matched ledger accuracy.

## Boundaries and scale limits

Synthetic cases only; no open-web retrieval, no LLM agent traces, no external fact-checking dataset, no human citation audit, and no proof of real-world claim-verification accuracy gains.

## Claim scope

In a controlled synthetic claim-verification task with explicit active/superseded evidence records, a tiny status-aware evidence ledger eliminated stale citations compared with both a mutable scratchpad verifier and an active-status-blind structured ledger.

## Why it stopped

Proxy-only synthetic evidence supports a narrow stale-citation mechanism but is insufficient for a publication-grade claim about real claim verification.

## Recommended next action

Run the same ledger, active-blind, and scratchpad variants on a small external claim-verification dataset or logged LLM verifier traces with auditable citation labels before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger on Auditable Claim-Verification Traces
- Success threshold: Ledger stale-citation rate at least 50% lower than active-blind and scratch baselines with no more than 2 percentage points accuracy loss on at least 200 externally sourced or logged cases.
- Stop condition: Stop if no auditable real/benchmark evidence revisions are available or if ledger stale-citation reduction is under 20% relative to the strongest baseline.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-evidence-ledger-for-claim-verification-cbe50696fac0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
