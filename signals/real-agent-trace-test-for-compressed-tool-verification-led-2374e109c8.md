# Real-Agent Trace Test for Compressed Tool Verification Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-trace-test-for-compressed-tool-verification-led-2374e109c8`
Run ID: `real-agent-trace-test-for-compressed-tool-verification-led-2374e109c8-20260604T003038546915+0000`

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

- Parent run decision: Compressed State Ledger for Small Agent Tool Verification: enoch://control-plane/projects/compressed-state-ledger-for-small-agent-tool-verification-36d639504452/runs/compressed-state-ledger-for-small-agent-tool-verification-36d639504452-20260603T183845227647+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/810c7576d010

## What looked useful

Compressed tool verification ledgers are mechanically viable on a real agent trace when they include output hashes; a span-only control without output hashes missed output tampering.

## Boundaries and scale limits

Single local self-trace; one tool-event type; five deterministic mutation classes; no multi-agent, multi-tool-schema, cross-runtime, streaming, privacy, or adversarial canonicalization validation.

## Claim scope

On one real Codex worker JSONL trace with 9 completed command_execution events, a compressed SHA-256 hash-chain ledger containing command hashes, output hashes, identity/order metadata, and exit/status fields detected all tested command, output, exit-code, deletion, and reorder mutations while using about 5.75% of the bytes of a full event-embedding ledger.

## Why it stopped

Tier 1 direct evidence supports the mechanism but is too small and self-trace-specific for publication readiness.

## Recommended next action

Run a bounded multi-trace follow-up over at least 20 heterogeneous real agent traces and multiple tool schemas, with the same full-ledger baseline and a larger mutation suite.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-Trace Validation of Compressed Tool Verification Ledgers
- Success threshold: Compressed ledger detects 100% of the defined tamper cases on every trace and is at least 5x smaller than the full event-embedding ledger on median and on at least 18 of 20 traces.
- Stop condition: Stop if any required tamper class is accepted by the compressed ledger, median compression is below 5x, or trace-format heterogeneity requires manual/private evidence unavailable to the worker.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-trace-test-for-compressed-tool-verification-led-2374e109c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
