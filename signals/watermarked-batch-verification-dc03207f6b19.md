# Watermarked Batch Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `watermarked-batch-verification-dc03207f6b19`
Run ID: `watermarked-batch-verification-dc03207f6b19-20260525T150851966104+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4c49dab1e186

## What looked useful

Ordered keyed aggregate watermarks detected all tested non-adaptive corruption, drop, duplicate, and swap mutations in 400/400 trials each, while order-insensitive tags missed all swap mutations and every scheme failed when the attacker could recompute the tag.

## Boundaries and scale limits

Standard-library CPU simulation only; no production batch service, no model-inference pipeline, no real operational failure trace, and no external adversary evaluation. The largest completed calibrated run used 400 trials per mutation and completed in 19.63 seconds.

## Claim scope

Synthetic local benchmark of compact keyed aggregate watermarks for batch integrity verification on 1024-record batches with payload corruption, drop, duplicate, swap, and adaptive-recompute mutations.

## Why it stopped

Synthetic evidence supports the mechanism under a narrow non-adaptive threat model but exposes decisive limitations for order-insensitive tags and adaptive recomputation, so it is not publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next, test ordered keyed aggregate tags against a real or realistic batch inference pipeline with Merkle/per-record verification as the baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic batch-pipeline verification with ordered aggregate watermarks
- Success threshold: At least 99.9% detection of non-adaptive injected faults over 10000 or more realistic batch items, with metadata reduction versus per-record tags and documented localization tradeoff.
- Stop condition: Stop if ordered aggregate tags miss any non-adaptive reorder/drop/duplicate/payload-corruption class that the Merkle baseline detects, or if metadata/runtime savings are negligible after accounting for localization needs.

## Evidence references

- Artifact root: `<local-path>/projects/watermarked-batch-verification-dc03207f6b19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
