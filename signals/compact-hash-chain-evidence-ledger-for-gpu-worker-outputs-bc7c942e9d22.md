# Compact Hash-Chain Evidence Ledger for GPU Worker Outputs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compact-hash-chain-evidence-ledger-for-gpu-worker-outputs-bc7c942e9d22`
Run ID: `compact-hash-chain-evidence-ledger-for-gpu-worker-outputs-bc7c942e9d22-20260601T102101381502+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/268e803ebadc

## What looked useful

The compact hash-chain format is mechanically viable and materially smaller/faster than a JSONL evidence log in bounded local tests, but the result is an engineering mechanism signal rather than paper-ready research evidence.

## Boundaries and scale limits

Tested only with deterministic synthetic payload and metadata digests at 1k, 50k, and 200k records in a single-process sequential Python harness. Not validated with real GPU kernels, concurrent workers, fsync durability, crash recovery, external signing/timestamping, or adversaries able to rewrite both ledger and roots.

## Claim scope

A fixed-width binary BLAKE2s hash-chain ledger over synthetic GPU-worker output digests can preserve equivalent integrity evidence to canonical JSONL, detect one-byte tampering at the modified record, reduce raw evidence-log size to about 34% of JSONL, and verify about 2.7x faster on this local CPU benchmark.

## Why it stopped

No-paper closure: local synthetic evidence supports the ledger mechanism, but direct GPU-worker durability and threat-model evidence is still missing.

## Recommended next action

Run a bounded deepen experiment that embeds the compact ledger in a real or realistic GPU worker harness with concurrent append, fsync/checkpoint policy, crash injection, replay verification, and signed root publication.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-safe concurrent compact ledger in a GPU worker harness
- Success threshold: At 100k or more real worker-output records, compact ledger raw size is at least 2x smaller than JSONL, verification is at least 1.5x faster, tampering/truncation is localized by the verifier, and durable append overhead remains below 1% of end-to-end worker runtime.
- Stop condition: Stop if durable concurrent append overhead exceeds 5%, crash recovery cannot distinguish clean truncation from tampering, or signed checkpoint roots cannot be reproduced after replay.

## Evidence references

- Artifact root: `<local-path>/projects/compact-hash-chain-evidence-ledger-for-gpu-worker-outputs-bc7c942e9d22`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
