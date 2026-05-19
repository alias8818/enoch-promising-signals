# Rank-anchor frontier for quality-bounded low-rank KV compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `rank-anchor-frontier-for-quality-bounded-low-rank-kv-compr-4a9a64cb1e`
Run ID: `rank-anchor-frontier-for-quality-bounded-low-rank-kv-compr-4a9a64cb1e-20260517T223004112072+0000`

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

- Internal Enoch project: Rank-anchor frontier for quality-bounded low-rank KV compression: internal_generated:rank-anchor-frontier-for-quality-bounded-low-rank-kv-compr-4a9a64cb1e

## What looked useful

Rank-anchor KV compression is mechanism-supported locally: rank16 with 64 prefix+recent anchors reached +0.1377 mean NLL at 1.70x estimated compression, rank16 with 32 anchors reached +0.2100 at 2.15x, and rank8 with 32 anchors outperformed recent-only, random-anchor, and rank-only controls at comparable settings.

## Boundaries and scale limits

Single small pretrained model, WikiText-2 validation only, prefix length 192 and continuation length 80, naive SVD recompression every 16 tokens, estimated low-rank storage ratio rather than packed-cache serving memory or throughput.

## Claim scope

On distilgpt2 WikiText-2 cached continuation scoring with 3 fixed seeds, prefix+recent exact anchors plus low-rank SVD over non-anchor KV rows produced a better estimated cache-compression/quality frontier than rank-only, random-anchor, recent-only, full-cache, and sliding-window controls.

## Why it stopped

Tier 2 local evidence supports the mechanism but is not broad or systems-real enough for paper readiness.

## Recommended next action

Run a bounded deepen follow-up on GPT-2 small-class or another locally feasible pretrained LM with longer prefixes, adaptive rank selection, and packed-cache memory/latency measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive rank-anchor KV compression on GPT-2-small-class long-prefix decoding
- Success threshold: Across fixed seeds, prefix+recent adaptive rank-anchor compression keeps mean NLL delta <= 0.20 versus full KV, achieves >= 2.0x measured packed-cache memory reduction, and beats rank-only plus sliding-window controls at matched or better measured memory.
- Stop condition: Stop as negative if GPT-2-small-class mean NLL delta exceeds 0.30 at <= 2x measured memory reduction or if rank-anchor does not beat rank-only at matched memory across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/rank-anchor-frontier-for-quality-bounded-low-rank-kv-compr-4a9a64cb1e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
