# CPU Cache-Locality Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-cache-locality-speculative-decoding-a66ae8f1568e`
Run ID: `cpu-cache-locality-speculative-decoding-a66ae8f1568e-20260628T102434941416+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/3ae7c4efc8f7

## What looked useful

Across four configs and five repeats per layout, contiguous layout was 1.77x-4.53x faster than scattered, and blocked time-major traversal was 2.27x-5.10x faster than scattered.

## Boundaries and scale limits

Synthetic candidate vectors only; no real language model, KV-cache runtime integration, acceptance-rate modeling, multi-thread serving, NUMA pinning, or hardware cache counters.

## Claim scope

Single-thread CPU microbenchmark of speculative-decoding-style candidate verification vector scans shows locality-preserving layouts reduce latency versus page-scattered random candidate-state access.

## Why it stopped

Proxy mechanism evidence is useful but not full validation; no end-to-end decoder or hardware-counter evidence, so stop as no-paper useful signal.

## Recommended next action

Run a bounded follow-up that implements blocked candidate/KV buffers in a small CPU speculative decoder and measures accepted tokens/sec plus cache counters.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU decoder integration for blocked speculative verification buffers
- Success threshold: At least 20% accepted tokens/sec improvement or verifier-latency reduction on a real small-model CPU speculative decoding workload across at least three seeds/prompts, with matching outputs.
- Stop condition: Stop if integrated decoder speedup is below 5% or correctness diverges after layout-only changes.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-cache-locality-speculative-decoding-a66ae8f1568e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
