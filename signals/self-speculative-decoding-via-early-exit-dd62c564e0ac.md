# Self-Speculative Decoding via Early Exit

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-decoding-via-early-exit-dd62c564e0ac`
Run ID: `self-speculative-decoding-via-early-exit-dd62c564e0ac-20260524T172851717624+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/90ccc2e70cdf

## What looked useful

The best exit was layer 11 of 12 with 51.0% top-1 agreement and only 1.22 accepted tokens for an 8-token draft block; the best optimistic speedup bound was 0.280x for block size 2, far below the >1.0 necessary condition before implementation overhead.

## Boundaries and scale limits

This is not a full serving benchmark and does not test trained auxiliary exits, confidence gating, larger model families, non-Shakespeare corpora, or production KV-cache scheduling.

## Claim scope

For GPT-2 small on a 16,256-token-position Tiny Shakespeare probe, untrained intermediate-layer exits using the final layer norm and tied LM head do not provide enough final-token agreement or accepted-prefix length to make self-speculative decoding viable.

## Why it stopped

Proxy/early falsification: direct GPT-2 hidden-state agreement and accepted-prefix metrics show the untrained early-exit draft path cannot plausibly speed up decoding, but this does not fully validate or refute trained early-exit methods.

## Recommended next action

Stop this untrained early-exit variant; only pursue a bounded follow-up if training or calibration of auxiliary exits is explicitly in scope.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train calibrated auxiliary early-exit heads for self-speculative drafting
- Success threshold: Layer 6-8 auxiliary exits achieve an optimistic block-4 speedup bound above 1.1 and an actual cached decoding speedup above 1.05x on held-out text.
- Stop condition: Stop if held-out block-4 speedup bound remains below 1.0 after auxiliary-head training or if actual cached decoding is not faster than baseline.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-dd62c564e0ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
