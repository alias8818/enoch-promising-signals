# Memory-Mapped KV Pages with Anchor-Only GPU Residency

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `memory-mapped-kv-pages-with-anchor-only-gpu-residency-2367601f396b`
Run ID: `memory-mapped-kv-pages-with-anchor-only-gpu-residency-2367601f396b-20260607T103746926651+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b4703783d254

## What looked useful

Clustered pages achieved 32x always-resident KV reduction with 100% true-page recall and mean relative L2 0.0496, but adversarial non-anchor salient tokens had 0% true-page recall at top-32 and only 7.8% at top-512, with high output error.

## Boundaries and scale limits

Tested synthetic K/V pages up to 4096 pages, 16 tokens/page, 8 heads, dim 64, 128 queries, fp16; not tested on trained model KV traces, production decode engines, or host caches larger than available memory.

## Claim scope

On a GB10 synthetic paged-KV benchmark, single-anchor GPU residency with host mmap page fetches reduces always-resident KV bytes and preserves attention only when anchors represent page contents; it fails on salient non-anchor tokens.

## Why it stopped

Proxy synthetic evidence supports the memory-saving mechanism in clustered cases but early-falsifies single-anchor robustness for salient non-anchor tokens; this is not full validation on real model traces.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is testing multi-anchor or learned page summaries against the adversarial miss mode.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-anchor mmap KV page summaries for non-anchor retrieval
- Success threshold: At 4096 pages and top-32 selected pages, recover at least 90% adversarial true-page recall with mean relative L2 below 0.10 while keeping always-resident GPU summary bytes at least 8x smaller than full KV.
- Stop condition: Stop if 8 anchors per page fails to reach 50% adversarial true-page recall or if resident summary bytes exceed one quarter of full KV.

## Evidence references

- Artifact root: `<local-path>/projects/memory-mapped-kv-pages-with-anchor-only-gpu-residency-2367601f396b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
