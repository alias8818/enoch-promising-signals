# Live dispatcher integration for externally anchored LLM-agent tool-call receipts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `live-dispatcher-integration-for-externally-anchored-llm-ag-030e1b2738`
Run ID: `live-dispatcher-integration-for-externally-anchored-llm-ag-030e1b2738-20260529T223630967296+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-agent integration test for tamper-evident tool-call ledger: enoch://control-plane/projects/real-agent-integration-test-for-tamper-evident-tool-call-l-756bd20643/runs/real-agent-integration-test-for-tamper-evident-tool-call-l-756bd20643-20260529T080133891282+0000
- Parent run decision: Real LLM-agent runtime test of anchored tamper-evident tool-call receipts: enoch://control-plane/projects/real-llm-agent-runtime-test-of-anchored-tamper-evident-too-7cea547445/runs/real-llm-agent-runtime-test-of-anchored-tamper-evident-too-7cea547445-20260529T162110992771+0000

## What looked useful

Across 5 fixed seeds and 100,000 tool calls per variant at a 2% fault rate, live anchoring accepted 0/10003 invalid receipts versus 10003/10003 for both controls, with 18.04 us mean latency and 49,646 events/s throughput. Fault-rate sweeps at 0%, 1%, and 5% preserved the same correctness pattern.

## Boundaries and scale limits

The anchor was an independent in-process verifier with in-memory state; the workload used synthetic tool-call payloads, not real LLM-agent traces; no durable storage, cross-process service, network jitter, crash/restart recovery, or production concurrency was validated.

## Claim scope

In a deterministic synthetic dispatcher benchmark, synchronous independent anchoring of HMAC hash-chain tool-call receipts rejected all injected tamper, replay, reorder, drop, and forged-MAC receipt-path faults live, while non-anchored and local-chain controls accepted all injected invalid receipts.

## Why it stopped

No-paper useful signal: bounded synthetic evidence supports the mechanism, but the validation is not a full live dispatcher deployment or durable external-anchor test.

## Recommended next action

Run one final bounded deepen test with a cross-process durable anchor service, crash/restart injection, and a small corpus of real or recorded agent tool-call traces before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cross-process durable anchor validation for live LLM-agent tool-call receipts
- Success threshold: Across at least 100,000 recorded or realistic tool calls and fixed seeds, accept 0 invalid injected receipts, keep false valid rejection below 0.1%, keep p95 dispatcher latency below 5 ms, and recover a valid durable audit chain after crash/restart.
- Stop condition: Stop as negative if any invalid injected receipt is accepted, false valid rejection exceeds 0.1%, p95 latency exceeds 5 ms by more than 2x after tuning, or crash/restart breaks the durable audit chain.

## Evidence references

- Artifact root: `<local-path>/projects/live-dispatcher-integration-for-externally-anchored-llm-ag-030e1b2738`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
