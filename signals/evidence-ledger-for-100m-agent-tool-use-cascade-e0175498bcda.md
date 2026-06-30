# Evidence ledger for 100M-agent tool-use cascade

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-100m-agent-tool-use-cascade-e0175498bcda`
Run ID: `evidence-ledger-for-100m-agent-tool-use-cascade-e0175498bcda-20260529T224504311518+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3ff0a491742f

## What looked useful

Digest-chain receipts verified successfully and reduced compressed bytes/event from 404.49 to 98.07 versus compressed inline JSONL, while writing about 11.3k events/sec and verifying about 256.6k events/sec on a short CPU-only local benchmark.

## Boundaries and scale limits

No direct 100M-agent cascade was run. The experiment did not test distributed writers, realistic tool payload distributions, raw evidence object storage, indexing, query latency, replay workflows, crash recovery, or adversarial conditions beyond digest-chain verification.

## Claim scope

A deterministic single-process synthetic benchmark of 200,000 tool-use events across 50,000 synthetic agents found that digest-only chained receipts provide tamper-evident ordering and substantially reduce ledger bytes compared with inline JSONL for 512-byte synthetic evidence payloads.

## Why it stopped

The result supports a compact receipt-ledger mechanism but remains synthetic, single-writer, and far below direct 100M-agent systems validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should test sharded multi-writer receipt generation plus content-addressed raw evidence retention on millions of events.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sharded evidence ledger with raw blob retention and replay audit
- Success threshold: At least 5,000,000 events ingested with no verification failures, compressed receipt ledger under 150 bytes/event excluding raw blobs, raw evidence recovery success for every sampled replay audit, and aggregate ingestion above 50,000 events/sec on CPU hardware.
- Stop condition: Stop if shard merge verification fails, raw evidence recovery is incomplete, compressed receipts exceed 250 bytes/event after realistic metadata, or aggregate ingestion remains below 10,000 events/sec after straightforward batching.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-100m-agent-tool-use-cascade-e0175498bcda`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
