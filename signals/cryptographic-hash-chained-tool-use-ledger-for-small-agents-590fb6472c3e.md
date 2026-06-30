# Cryptographic Hash-Chained Tool-Use Ledger for Small Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cryptographic-hash-chained-tool-use-ledger-for-small-agents-590fb6472c3e`
Run ID: `cryptographic-hash-chained-tool-use-ledger-for-small-agents-590fb6472c3e-20260524T182839538786+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/0f353212c01e

## What looked useful

Hash-chained tool-use logging appears cheap enough for small agents, but the experiment falsifies any claim that an unanchored local hash chain alone detects deletion of a valid tail segment. External anchoring is a mandatory design component.

## Boundaries and scale limits

Synthetic payloads only; no real agent framework integration, no concurrent writers, no crash-consistency testing, no key rotation, no external transparency service, and no adversarial deployment where local log storage and anchor storage have separate trust boundaries.

## Claim scope

A single-process Python prototype of a canonical JSONL HMAC-SHA256 hash-chained tool-use ledger can write 10,000 synthetic small-agent tool records at about 70k entries/s for 512 B payloads and detect edits, middle deletions, reorders, and malformed truncation; valid suffix deletion requires an externally anchored final head hash and entry count.

## Why it stopped

Bounded local evidence supports practicality and identifies an anchoring requirement, but the result is synthetic/prototype-level rather than a full security or deployment validation.

## Recommended next action

Stop this run as a no-paper useful signal; next concrete work is to test an anchored ledger integrated with a real small-agent framework under crash/restart and concurrent writer scenarios.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored Tool-Use Ledger Integration Under Crash and Concurrency
- Success threshold: All tamper classes including valid suffix deletion are detected after restart, and median added per-tool-call latency remains below 5 ms on at least 10,000 real or framework-native tool events.
- Stop condition: Stop if anchored suffix deletion is not detected, crash recovery loses committed records without reporting corruption, or median overhead exceeds 5 ms per tool call in the integrated runner.

## Evidence references

- Artifact root: `<local-path>/projects/cryptographic-hash-chained-tool-use-ledger-for-small-agents-590fb6472c3e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
