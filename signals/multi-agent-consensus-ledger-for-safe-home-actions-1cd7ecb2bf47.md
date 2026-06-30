# Multi-Agent Consensus Ledger for Safe Home Actions

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-agent-consensus-ledger-for-safe-home-actions-1cd7ecb2bf47`
Run ID: `multi-agent-consensus-ledger-for-safe-home-actions-1cd7ecb2bf47-20260525T203351264325+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/abf77b336ae1

## What looked useful

Main benchmark mean unsafe execution rate was 0.089021 for single_agent, 0.008892 for majority_vote, and 0.000729 for consensus_ledger. Ledger hash-chain verification passed before tamper in all trials and sampled tamper detection was 1.0. Sensitivity sweep found the ledger had the lowest unsafe execution rate in all 9 tested validator/adversary settings.

## Boundaries and scale limits

Synthetic-only evidence: no real smart-home traces, no physical devices, no real LLM/tool-agent proposals, no user study, no network adversary, and no deployment latency or recovery testing. Main benchmark covered 240000 generated requests plus a 9-setting sensitivity sweep.

## Claim scope

In a local synthetic home-action benchmark with noisy proposers, noisy validators, hidden hazards, and sampled tamper checks, a policy-plus-quorum append-only consensus ledger reduced unsafe executions versus single-agent and majority-vote baselines while preserving similar safe-action success to majority vote.

## Why it stopped

Simulator-only evidence supports the mechanism but is not direct real-world validation and is not paper-ready.

## Recommended next action

Run a bounded integration-harness follow-up using real or high-fidelity smart-home event traces and actual LLM/tool-agent proposals; stop this run as no-paper synthetic useful signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Based Consensus Ledger Evaluation for Smart-Home Agent Actions
- Success threshold: At least 5x lower unsafe execution rate than majority vote, no more than 10 percent relative increase in safe-action blocks, median decision latency below 250 ms in the harness, and 100 percent sampled tamper detection.
- Stop condition: Stop if realistic traces show less than 2x unsafe-execution reduction versus majority vote or safe-action false blocks increase by more than 20 percent relative.

## Evidence references

- Artifact root: `<local-path>/projects/multi-agent-consensus-ledger-for-safe-home-actions-1cd7ecb2bf47`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
