# Tamper-Evident Agent Action Ledgers via Merkleized KV Fingerprints

Status: `useful_signal`
Project ID: `tamper-evident-agent-action-ledgers-via-merkleized-kv-fingerprints-2559c9727f37`
Run ID: `tamper-evident-agent-action-ledgers-via-merkleized-kv-fingerprints-2559c9727f37-20260519T170623374157+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a632fe50dec5

## What looked useful

The tamper-evidence mechanism is technically sound when the final head hash is externally anchored: anchored verification detected 6/6 mutation scenarios, while unanchored verification missed a wholesale self-consistent rewrite. Sparse Merkle updates sustained about 19k writes/sec and 16.8k verifies/sec at 10k synthetic actions, with about 26x write-time and 3x size overhead versus plain JSONL.

## Boundaries and scale limits

Synthetic set/delete actions only; no real agent traces, no production signing or transparency-log anchoring, no concurrent writers, no mature authenticated-map library, and local benchmarks only. Full recomputation was only measured to 1k actions and became too slow for the attempted 5k x 5 run.

## Claim scope

A local Python prototype using chained action records and per-action Merkleized KV roots detected all tested anchored tamper scenarios on synthetic KV action streams up to 10k actions; an incremental sparse Merkle map was much faster than full root recomputation but still substantially slower and larger than a plain JSONL log.

## Why it stopped

No-paper useful signal: the local synthetic evidence supports the mechanism but does not provide direct real-agent or production anchoring evidence, and the prototype's overhead/novelty are not enough for a paper.

## Recommended next action

Run a bounded deepen study on real agent traces with signed or transparency-log anchored heads and compare against simpler chained-hash logs plus a mature incremental authenticated-map library.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Trace Validation for Anchored Merkleized Action Ledgers
- Success threshold: Detect 100% of anchored tamper cases and keep p95 per-action ledger overhead below 10 ms or below 10% of agent-loop latency on the tested trace harness, while documenting storage overhead.
- Stop condition: Stop if anchored tamper detection is incomplete, canonicalization/signing ambiguity permits undetected rewrites, or overhead exceeds the success threshold on realistic traces.

## Evidence references

- Artifact root: `<local-path>/projects/tamper-evident-agent-action-ledgers-via-merkleized-kv-fingerprints-2559c9727f37`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
