# Async two-node home training with 1-bit Adam overlap

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `async-two-node-home-training-with-1-bit-adam-overlap-83570dd2b3b9`
Run ID: `async-two-node-home-training-with-1-bit-adam-overlap-83570dd2b3b9-20260523T060604496498+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/01c8b93e0fc7

## What looked useful

1-bit packing reduces communication enough to be directionally useful, but overlap did not hide most communication. In the tied-head control, exposed 1-bit communication was 50.74 ms on 1 GbE, 20.53 ms on 2.5 GbE, and 5.43 ms on 10 GbE against a 31.18 ms median local step; fp32 remained non-viable even at 10 GbE.

## Boundaries and scale limits

No physical second node, no real network transport, no production 1-bit Adam optimizer/error feedback, and no convergence validation. Results apply to the measured small-model timing envelope and communication scheduler only.

## Claim scope

Single-GB10 timing proxy for async two-node training overlap using measured 58-67M parameter toy transformer-like backward bucket readiness, measured 1-bit sign packing costs, and simulated 1/2.5/10 GbE serial two-node communication.

## Why it stopped

Proxy timing study early-falsified the home 1/2.5 GbE overlap claim: even with measured 1-bit GPU packing, exposed communication was 66% of tied-head local step time at 2.5 GbE and 163% at 1 GbE. This is not a full distributed validation.

## Recommended next action

Stop as no-paper useful negative evidence unless a real two-node 10 GbE setup is available for a bounded direct validation with production 1-bit Adam/error feedback.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct two-node 10 GbE 1-bit Adam overlap validation
- Success threshold: Exposed communication below 10% of local median step time for at least 500 consecutive measured steps and validation/training loss within 2% of the AdamW baseline over the same token budget.
- Stop condition: Stop negative if exposed communication is at least 20% of local median step time after bucket-size tuning or if loss diverges more than 5% from AdamW over the bounded token budget.

## Evidence references

- Artifact root: `<local-path>/projects/async-two-node-home-training-with-1-bit-adam-overlap-83570dd2b3b9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
