# Quantized Agent with Unquantized Evidence Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-agent-with-unquantized-evidence-ledger-7f7a8ffa6b5e`
Run ID: `quantized-agent-with-unquantized-evidence-ledger-7f7a8ffa6b5e-20260607T220900953511+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/291a0c948d7c

## What looked useful

Exact ledger replay fully restored fp32-reference decisions after quantized state updates, but naive ledger storage cost 48x the fp32 working state. Selective margin replay was only practically attractive at 8-bit state, where replaying 9.0% of tasks reduced decision mismatch from 3.36% to 0.62%; 2-4 bit states either required heavy replay or left substantial mismatch.

## Boundaries and scale limits

120,000 synthetic tasks only; no real LLM agent, retrieval corpus, tool traces, learned quantization, serving latency, or compressed ledger storage tested.

## Claim scope

Synthetic evidence-accumulation benchmark with quantized online state and exact unquantized evidence replay at decision time.

## Why it stopped

Closed as no-paper useful signal because evidence is a synthetic proxy: it supports the ledger replay mechanism but does not validate real-agent behavior or an efficient ledger design.

## Recommended next action

Run a bounded deepen test on a small real retrieval/tool-agent trace with 8-bit quantized state summaries and hash-addressed exact evidence records.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace 8-bit agent state with hash-addressed exact evidence ledger
- Success threshold: Recover at least 90% of the decision mismatches introduced by 8-bit quantized state while replaying at most 25% of cases, with zero audit reconstruction error for replayed cases.
- Stop condition: Stop if 8-bit quantized state introduces under 0.5% decision mismatch on the real trace, if margin-gated replay must exceed 25% of cases to recover 90% of mismatches, or if exact evidence storage remains larger than the fp32 baseline without an auditability benefit.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-agent-with-unquantized-evidence-ledger-7f7a8ffa6b5e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
