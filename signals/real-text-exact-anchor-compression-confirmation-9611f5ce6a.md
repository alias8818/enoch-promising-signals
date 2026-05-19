# Real-Text Exact Anchor Compression Confirmation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-text-exact-anchor-compression-confirmation-9611f5ce6a`
Run ID: `real-text-exact-anchor-compression-confirmation-9611f5ce6a-20260518T024404705292+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Real-Text Exact Anchor Compression Confirmation: internal_generated:real-text-exact-anchor-compression-confirmation-9611f5ce6a

## What looked useful

Exact anchors matched 10-25% of held-out bytes depending on selection, but dictionary and reference overhead erased practical gains. Frequency-selected anchors were best, yet only saved about 0.43% versus raw on average and lost badly to gzip, bz2, and lzma.

## Boundaries and scale limits

Validated on 44 cached real-text files, 273 chunks, five fixed train/test splits, and 1.05 MB held-out text per seed. It does not test entropy-coded anchor streams, neural compression, web-scale corpora, or jointly optimized anchor models.

## Claim scope

Standalone exact-byte anchor substitution learned from real training text does not provide meaningful held-out real-text compression when dictionary and token overhead are included; the best tested variant averaged 0.9957x raw bytes and 3.85x gzip size across five fixed seeds.

## Why it stopped

Medium fixed-seed real-text validation failed the practical compression threshold: the best exact-anchor variant was essentially raw-size and approximately 3.85x larger than gzip.

## Recommended next action

Stop this standalone exact-anchor compression line; only reopen as a distinct preprocessing study if the anchor stream is entropy-coded and compared against gzip/lzma/zstd on the same fixed splits.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Entropy-Coded Anchor Preprocessing Against Standard Compressors
- Success threshold: Anchor-preprocessed gzip or zstd must reduce total compressed bytes by at least 3% versus the same backend without anchors on at least 4 of 5 fixed seeds, with dictionary cost included.
- Stop condition: Stop if preprocessing improves mean compressed size by less than 1% or loses on two or more fixed seeds.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-exact-anchor-compression-confirmation-9611f5ce6a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
