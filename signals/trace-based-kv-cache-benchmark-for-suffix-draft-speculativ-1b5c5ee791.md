# Trace-Based KV-Cache Benchmark for Suffix-Draft Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trace-based-kv-cache-benchmark-for-suffix-draft-speculativ-1b5c5ee791`
Run ID: `trace-based-kv-cache-benchmark-for-suffix-draft-speculativ-1b5c5ee791-20260608T162713836261+0000`

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

- Parent run decision: Draft-from-Suffix Speculative Decoding for Small Local Models: enoch://control-plane/projects/draft-from-suffix-speculative-decoding-for-small-local-models-484b9438506e/runs/draft-from-suffix-speculative-decoding-for-small-local-models-484b9438506e-20260608T140525931192+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/92313955d92d

## What looked useful

Moderate suffix reuse saved 36.0% of KV bytes and reached 5.005x isolated materialization speedup when suffix keys were precomputed, but the naive per-request suffix hashing implementation was slower than baseline at 0.829x. The mechanism depends on very cheap incremental suffix-key lookup.

## Boundaries and scale limits

No transformer model forward pass, GPU KV layout, production trace replay, or end-to-end serving scheduler was measured. Acceptance was simulated, and the traces were controlled synthetic traces rather than private/real workloads.

## Claim scope

Controlled Tier 1 synthetic-trace KV-cache materialization benchmark for suffix-draft speculative decoding, measuring suffix hit rate, KV bytes avoided, and direct cache materialization time on CPU.

## Why it stopped

No-paper useful signal: the controlled direct benchmark supports KV traffic savings but falsifies the naive implementation path and lacks end-to-end model/GPU evidence for a paper claim.

## Recommended next action

Run a bounded deepen test that integrates incremental suffix-key maintenance into a small real speculative decoding loop and requires end-to-end decode throughput improvement over baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Incremental suffix-key speculative decoding loop benchmark
- Success threshold: On the moderate-reuse trace, end-to-end decode throughput improves by at least 1.10x while suffix lookup overhead remains below 10% of per-step wall time and output token acceptance is unchanged relative to baseline verification.
- Stop condition: Stop if moderate-reuse end-to-end throughput is below 1.05x or suffix lookup overhead exceeds 20% of per-step wall time after incremental-key implementation.

## Evidence references

- Artifact root: `<local-path>/projects/trace-based-kv-cache-benchmark-for-suffix-draft-speculativ-1b5c5ee791`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
