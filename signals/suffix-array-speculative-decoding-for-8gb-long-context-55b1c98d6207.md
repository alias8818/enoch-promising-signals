# Suffix-Array Speculative Decoding for 8GB Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-decoding-for-8gb-long-context-55b1c98d6207`
Run ID: `suffix-array-speculative-decoding-for-8gb-long-context-55b1c98d6207-20260525T083241485830+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2ed250168d09

## What looked useful

Suffix-array exact-copy drafting works on repetitive/code-like contexts, reaching about 12-15 accepted bytes per 16-byte draft, but the fixed-k table is nearly as effective. Across non-random cases the suffix array gained only 0.615 accepted bytes/query on average while mean query latency was 8.26x higher; a full suffix array over an 8 GiB byte context needs at least 32 GiB of positions alone.

## Boundaries and scale limits

No neural target model, no tokenizer-level traces, no online incremental suffix-array maintenance, and no direct 8 GiB allocation. The 8 GiB conclusion is a storage-floor extrapolation from one suffix-array position per input byte.

## Claim scope

Byte-level static suffix-array exact-copy drafting on synthetic random, repeated-block, and code-like contexts up to 16 MB, compared with a fixed 16-byte previous-occurrence table baseline.

## Why it stopped

Bounded proxy evidence supports the exact-copy mechanism but early-falsifies the practical full suffix-array 8GB-context version: memory floor exceeds the target budget and acceptance gains over a simpler control are small.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should evaluate a compact or sampled suffix-array variant against a compact rolling n-gram table on tokenizer-level model traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compact suffix-index drafting on tokenizer-level traces
- Success threshold: At 128 MB or larger tokenizer traces, compact suffix indexing must fit under 1.5x the memory of the compact n-gram table, deliver at least 20% more accepted draft tokens/query, and keep p90 query latency within 2x of the n-gram baseline.
- Stop condition: Stop if the compact suffix index still needs more than 2x n-gram memory or fails to improve accepted draft tokens/query by at least 10% on two trace families.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-for-8gb-long-context-55b1c98d6207`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
