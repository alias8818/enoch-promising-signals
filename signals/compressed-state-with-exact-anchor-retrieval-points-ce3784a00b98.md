# Compressed State with Exact Anchor Retrieval Points

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-state-with-exact-anchor-retrieval-points-ce3784a00b98`
Run ID: `compressed-state-with-exact-anchor-retrieval-points-ce3784a00b98-20260601T083930893254+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/51f0628e9d71

## What looked useful

Exact anchor retrieval points can reliably patch selected locations in a lossy compressed state, but the benefit is confined to anchored items and is sensitive to the routing threshold and query noise.

## Boundaries and scale limits

Synthetic random vectors only; no transformer KV-cache, no real language prompts, no learned anchor selection, no learned compression, no serving latency measurement, and poor non-anchor recall from the tested linear sketch.

## Claim scope

In a synthetic associative-recall benchmark with N=4096 normalized random key-value pairs, a linear sketch plus 128 exact anchors recovered 99.844% anchored retrieval accuracy at 3.906% of dense float storage when the anchor gate threshold was calibrated to 0.65 and query noise was 0.10.

## Why it stopped

Synthetic bounded evidence supports the anchor mechanism but does not validate a broad compressed-state method; the tested sketch has near-zero non-anchor recall.

## Recommended next action

Stop this run as no-paper useful evidence; a bounded follow-up should replace the toy linear sketch with a transformer KV-cache compression baseline on a real retrieval benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact Anchor Points in Transformer KV-Cache Compression
- Success threshold: At a fixed memory budget below 25% of dense KV storage, hybrid anchors improve anchored retrieval by at least 20 percentage points over compressed-only KV while keeping non-anchor accuracy no worse than 2 percentage points below compressed-only and false-anchor routes below 1%.
- Stop condition: Stop if hybrid anchors fail to improve anchored retrieval by at least 10 percentage points over compressed-only KV on the first real retrieval benchmark or if false-anchor routing exceeds 5% after calibration.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-with-exact-anchor-retrieval-points-ce3784a00b98`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
