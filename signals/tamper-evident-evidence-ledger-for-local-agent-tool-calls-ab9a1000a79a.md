# Tamper-Evident Evidence Ledger for Local Agent Tool Calls

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tamper-evident-evidence-ledger-for-local-agent-tool-calls-ab9a1000a79a`
Run ID: `tamper-evident-evidence-ledger-for-local-agent-tool-calls-ab9a1000a79a-20260629T131056158351+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5878c4890a8e

## What looked useful

Hash chaining plus per-record HMAC is a practical local baseline for tamper-evident agent tool-call logs, but truncation requires an externalized count/tail checkpoint and the naive append implementation is not a scalable high-volume tracing design.

## Boundaries and scale limits

Synthetic tool-call events only; 1,000-record local run; no real agent adapter, hostile-key compromise test, independent remote checkpoint service, crash fault injection, or long-ledger scalability benchmark. Chain-only replay did not detect tail truncation without a preserved checkpoint.

## Claim scope

A standard-library Python prototype of a local JSONL hash-chain plus HMAC evidence ledger detected synthetic post-hoc mutation, deletion, reordering, unauthenticated forgery, and checkpoint-compared tail truncation across 1,000 synthetic local tool-call records.

## Why it stopped

Useful scoped mechanism evidence was produced, but the result is a standard construction validated on synthetic traces and is not publication-grade or broad enough for finalize_positive.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded step is to integrate the ledger with a real local agent tool-call wrapper and write checkpoints to an independent trust domain.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Adapter and External Checkpoint Validation for Local Tool-Call Evidence Ledgers
- Success threshold: At least 99.9% successful recording of real tool calls in a 10,000-call replay, p95 append overhead below 25 ms, detection of mutation/deletion/reordering/forgery/truncation in the tested corpus, and clean recovery or explicit failure on interrupted writes.
- Stop condition: Stop if real tool-call wrapping loses events, if checkpoint export cannot be made independent of the ledger host, or if append overhead exceeds 100 ms p95 after straightforward batching/segmentation.

## Evidence references

- Artifact root: `<local-path>/projects/tamper-evident-evidence-ledger-for-local-agent-tool-calls-ab9a1000a79a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
