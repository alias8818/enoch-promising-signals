# Entropy-Coded Anchor Preprocessing Against Standard Compressors

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `88`
Project ID: `entropy-coded-anchor-preprocessing-against-standard-compre-d69ad54fb5`
Run ID: `entropy-coded-anchor-preprocessing-against-standard-compre-d69ad54fb5-20260518T025452770968+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `88`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Entropy-Coded Anchor Preprocessing Against Standard Compressors: internal_generated:entropy-coded-anchor-preprocessing-against-standard-compre-d69ad54fb5

## What looked useful

Anchor tokenization can reduce final size on some highly repetitive structured files, especially silesia/nci, reymont, webster, and gzip level 1 aggregate. The same preprocessing causes frequent regressions on small files and stronger compressors, with xz level 6 worsening by 3.934% aggregate and most files losing for all level-6 compressors.

## Boundaries and scale limits

Local bounded validation only: 26 public corpus files, per-file anchor discovery, max 128 anchors, 8 MiB training prefix, no learned gating, no production/private corpora, and no standalone arithmetic/Huffman-coded anchor stream beyond downstream compressor entropy coding.

## Claim scope

A reversible fixed-anchor byte-token preprocessor was tested on 26 public Canterbury/Large/Silesia corpus files before gzip, zstd, and xz at levels 6 and 1. The broad claim of general improvement against standard compressors was not supported; selective improvements appeared on repetitive structured files and gzip level 1.

## Why it stopped

Bounded direct validation found selective mechanism support but no broad robust improvement against standard compressors; this is no-paper evidence, not full publication support.

## Recommended next action

Stop the general-purpose paper claim; only pursue a final bounded gated-preprocessor follow-up if the controller wants to test whether file-type prediction can retain the positive outliers while skipping harmful cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Gated Anchor Preprocessing for Fast Compression Only
- Success threshold: On held-out mixed corpora, gated-anchor must improve gzip level 1 aggregate compressed size by at least 2.0% versus raw, have median gzip-1 file delta no worse than 0%, and keep default zstd/xz aggregate delta within +0.25% when included as safety baselines.
- Stop condition: Stop if the gate fails the gzip-1 aggregate threshold, worsens median gzip-1 file size, or still permits more than +0.25% aggregate regression on zstd/xz safety baselines.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-coded-anchor-preprocessing-against-standard-compre-d69ad54fb5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
