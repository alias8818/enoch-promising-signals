# KV-Cache Suffix-Tree Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-suffix-tree-speculative-decoding-dd2b477dffaa`
Run ID: `kv-cache-suffix-tree-speculative-decoding-dd2b477dffaa-20260515T205512695930+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f8aa642cf3d5

## What looked useful

Suffix-tree lookup improved emitted tokens per validation call over no draft, exact-context reuse, and fixed 8-token suffix indexing in controlled online traces, but required confidence gating and used roughly 12-16x more index entries than fixed suffix indexing on the large synthetic sweeps.

## Boundaries and scale limits

No production serving trace, no real model forward passes, no GPU KV-cache integration, and no direct latency measurement. Local text traces are small sanity checks, not representative LLM traffic.

## Claim scope

Online token-trace simulation shows suffix-based continuation lookup can increase accepted speculative tokens per target validation call when suffixes recur despite unique full contexts; the result does not claim real decoder wall-clock speedup.

## Why it stopped

Proxy simulator supports the mechanism but is insufficient for a paper or production claim; it lacks direct GPU decoder and KV-cache latency evidence.

## Recommended next action

Run a bounded direct implementation in a small GPT-2-class decoder with real KV-cache references, pruning, and wall-clock latency measurement; stop this run because the current result is a proxy useful signal rather than full validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-Model KV-Cache Suffix Drafting Latency Test
- Success threshold: At least 15% lower wall-clock time per emitted token than no draft and at least 5% lower than fixed 8-token suffix lookup on one repeated-suffix workload, with exact output equivalence and bounded index memory under 2x fixed-suffix memory.
- Stop condition: Stop as negative if wall-clock speedup is below 5%, correctness diverges, or suffix-tree memory exceeds 2x fixed-suffix memory without a compensating latency win.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-suffix-tree-speculative-decoding-dd2b477dffaa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
