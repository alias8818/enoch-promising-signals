# Merkle-Ledger Agent Tool-Call Integrity

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `merkle-ledger-agent-tool-call-integrity-f72fee77b0d4`
Run ID: `merkle-ledger-agent-tool-call-integrity-f72fee77b0d4-20260524T010404391720+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4d24ceda12ad

## What looked useful

The bounded mechanism worked on all tested tamper cases, but naive periodic prefix Merkle root recomputation was non-viable; incremental Merkle accumulator checkpointing reduced the 50,000-event confirmation to 26.02 seconds wall-clock including five repeats and attack verification.

## Boundaries and scale limits

Synthetic traces only; one CPU worker; no real agent framework integration, concurrency, crash recovery, external timestamp anchoring, malicious live logger model, key compromise test, or selective proof benchmark.

## Claim scope

On synthetic agent tool-call traces up to 50,000 events, a deterministic per-event hash chain plus incremental Merkle accumulator checkpoints and checkpoint MACs detected six post-hoc tamper classes with 1.0 detection rate and practical local CPU throughput.

## Why it stopped

No-paper closure: bounded synthetic evidence supports a useful mechanism and implementation constraint, but direct deployment evidence is missing.

## Recommended next action

Run a bounded follow-up on real agent tool-call traces with crash/restart recovery and external checkpoint anchoring before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Merkle Ledger Anchoring and Crash-Recovery Test
- Success threshold: All tamper classes detected on at least 10,000 real tool-call events with clean-ledger false positive rate 0 and median end-to-end logging overhead under 2x versus structured JSON logging.
- Stop condition: Stop if real-framework integration cannot preserve deterministic canonical events, if anchored rollback detection fails, or if median overhead exceeds 2x after one straightforward optimization pass.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-ledger-agent-tool-call-integrity-f72fee77b0d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
