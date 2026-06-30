# Evidence-Ledger Attestation Chains for CPU Agent Tool Calls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-attestation-chains-for-cpu-agent-tool-calls-e98be7807db5`
Run ID: `evidence-ledger-attestation-chains-for-cpu-agent-tool-calls-e98be7807db5-20260628T222049728668+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/edbe5c5bae6d

## What looked useful

The mechanism detected 6/6 tamper variants while accepting the valid chain with zero verification errors, showing the scaffold can support machine-checkable evidence-ledger claims for bounded CPU tool calls.

## Boundaries and scale limits

Synthetic 3-event CPU-only ledger; local reproducible HMAC key; no signer isolation, append-only storage, real agent harness integration, concurrency, crash/retry testing, private-data redaction, or production remote attestation.

## Claim scope

A small local Python verifier can accept a valid 3-event CPU subprocess evidence ledger and reject six controlled tamper cases using event hash continuity, HMAC attestations, evidence references, and claim predicates.

## Why it stopped

No-paper useful signal only: the result is a small local mechanism check, not a production trust or broad agent-runtime validation.

## Recommended next action

Run a bounded deepen test that captures real agent tool calls through an append-only writer with signer isolation, then replay the same tamper suite plus crash/retry cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signer-isolated append-only evidence ledger for real agent tool traces
- Success threshold: At least 20 real tool-call events across multiple tasks, 0 false rejects on valid traces, and 100% detection of the defined tamper suite with signer isolation documented.
- Stop condition: Stop if signer isolation cannot be implemented locally or if any tamper case is accepted after one verifier bug-fix pass.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-attestation-chains-for-cpu-agent-tool-calls-e98be7807db5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
