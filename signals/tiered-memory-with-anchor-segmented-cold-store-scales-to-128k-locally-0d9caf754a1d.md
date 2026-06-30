# Tiered Memory With Anchor-Segmented Cold Store Scales to 128k Locally

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiered-memory-with-anchor-segmented-cold-store-scales-to-128k-locally-0d9caf754a1d`
Run ID: `tiered-memory-with-anchor-segmented-cold-store-scales-to-128k-locally-0d9caf754a1d-20260628T111247069101+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c6936620b079

## What looked useful

At 128k tokens and segment size 256, the anchor method used an 8192-byte hot index, scanned at most 4096 bytes/query versus 2097152 bytes/query for full scan, preserved exact correctness, and improved p95 latency by 18.90x in the local benchmark.

## Boundaries and scale limits

Tested up to 131072 synthetic records, 5000 queries per case, segment sizes 256 to 2048, CPU-only NumPy/memmap implementation. Does not test LLM training, natural language quality, learned anchor selection, approximate retrieval, concurrent serving, cache eviction, or contexts beyond 128k.

## Claim scope

Synthetic exact-recall benchmark shows that when queries include an anchor identifying a segment, a local anchor-segmented cold store can retrieve from 128k-token contexts with exact correctness while scanning only the addressed segment instead of the full cold store.

## Why it stopped

No-paper closure: this run produced a useful local mechanism signal, but it is synthetic/proxy evidence and not a full model-quality or publication-grade validation.

## Recommended next action

Run a bounded deepen test that plugs the anchor-segmented cold store into a small transformer retrieval task and compares accuracy/latency against full-context attention and retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-segmented cold store in a toy transformer retrieval task
- Success threshold: At 128k tokens, maintain at least 95% of the full-context baseline retrieval accuracy while reducing peak memory or p95 retrieval latency by at least 4x.
- Stop condition: Stop if anchor noise or integration overhead drops exact-match accuracy below 90% of baseline or removes the memory/latency advantage in two independent seeds.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-memory-with-anchor-segmented-cold-store-scales-to-128k-locally-0d9caf754a1d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
