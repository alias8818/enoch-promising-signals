# Tamper-Evident KV Ledger for Agent Steps

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tamper-evident-kv-ledger-for-agent-steps-1cb4fdaf8de7`
Run ID: `tamper-evident-kv-ledger-for-agent-steps-1cb4fdaf8de7-20260603T165953705206+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/788c4883ed21

## What looked useful

The prototype verified hash-chain/HMAC/checkpoint tamper detection in all tested cases, but append throughput was only 198 appends/s at 5000 records, about 22% of fsync JSONL and 58% of per-append SQLite in the conservative durability benchmark.

## Boundaries and scale limits

Tested on generated local traces up to 5000 records with 3 repeats and synthetic tamper edits only; not validated for production traces, adversarial key management, remote anchoring, crash recovery, multi-writer concurrency, replication, or high-throughput serving.

## Claim scope

A local Python stdlib append-only KV ledger for agent-step-shaped records can detect direct payload, previous-hash, and HMAC tampering while preserving latest-value lookup and Merkle inclusion proofs at toy/local scale.

## Why it stopped

Local mechanism was supported, but evidence is toy/synthetic and the construction combines established primitives without enough novelty or production validation for a paper.

## Recommended next action

Stop as no-paper useful signal; run a bounded optimized follow-up with batched fsync/WAL group commit only if pursuing practical throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Batched durable tamper-evident agent-step ledger
- Success threshold: At 5000 records and 3 repeats, optimized ledger mean throughput is at least 500 appends/s while all tamper tests and full verification pass.
- Stop condition: Stop if batching cannot exceed 300 appends/s at 5000 records or if any tamper/verification check fails under the optimized write path.

## Evidence references

- Artifact root: `<local-path>/projects/tamper-evident-kv-ledger-for-agent-steps-1cb4fdaf8de7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
