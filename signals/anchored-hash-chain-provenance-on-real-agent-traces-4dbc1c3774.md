# Anchored Hash-Chain Provenance on Real Agent Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchored-hash-chain-provenance-on-real-agent-traces-4dbc1c3774`
Run ID: `anchored-hash-chain-provenance-on-real-agent-traces-4dbc1c3774-20260529T093553434652+0000`

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

- Parent run decision: Hash-Chain Evidence Ledger for Agent Decision Provenance: enoch://control-plane/projects/hash-chain-evidence-ledger-for-agent-decision-provenance-53d83111f1c6/runs/hash-chain-evidence-ledger-for-agent-decision-provenance-53d83111f1c6-20260529T014550997657+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/91d47f7f6764

## What looked useful

Tier 1 controlled direct test supported the core mechanism: baseline verification accepted the real trace, 5/5 tamper cases were rejected, and measured build/verify throughput was about 13.4k events/s on the real 27-event trace and about 12k events/s on a 2700-event replayed workload.

## Boundaries and scale limits

Single local trace with 27 events; replayed x100 workload only estimates overhead and does not add trace diversity. Anchors are local HMACs, not public timestamps, transparency-log entries, KMS-backed signatures, or independent notary records. No live concurrent ingestion, restart recovery, multi-agent corpus, key-compromise, or cross-implementation canonicalization test was performed.

## Claim scope

A local offline verifier over one real Codex JSONL trace can build a canonical SHA-256 hash-chain with periodic authenticated HMAC anchors and reject controlled post-hoc mutation, deletion, reordering, insertion, and truncation attempts when the verifier retains the original anchors.

## Why it stopped

No-paper closure: the Tier 1 mechanism is supported, but evidence is not paper-positive because external anchoring, corpus diversity, live ingestion behavior, and key-separation adversary tests were not validated.

## Recommended next action

Run a bounded deepen test on at least 10 real agent traces with anchors persisted outside the mutable trace directory via an append-only store or public timestamp/KMS-backed signature, then repeat tamper, restart, and concurrent-write checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Externally Persisted Anchors Across Multiple Real Agent Traces
- Success threshold: All tested tamper cases are rejected on all traces, restart recovery preserves verifiability, concurrent ingestion produces no false accepts or false rejects, and p95 ingestion overhead remains below 5% versus raw JSONL writing.
- Stop condition: Stop if any tamper case is accepted with uncompromised external anchors, if canonicalization differs across verifier runs, or if p95 ingestion overhead exceeds 10% after one straightforward optimization pass.

## Evidence references

- Artifact root: `<local-path>/projects/anchored-hash-chain-provenance-on-real-agent-traces-4dbc1c3774`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
