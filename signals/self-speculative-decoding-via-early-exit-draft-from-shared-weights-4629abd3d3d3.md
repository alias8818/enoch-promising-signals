# Self-Speculative Decoding via Early-Exit Draft from Shared Weights

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-via-early-exit-draft-from-shared-weights-4629abd3d3d3`
Run ID: `self-speculative-decoding-via-early-exit-draft-from-shared-weights-4629abd3d3d3-20260528T234013398160+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/792c980d2760

## What looked useful

Early exits become more aligned near the final layer, reaching 0.530 draft-sample acceptance and 0.549 greedy agreement at layer 11, but observed prefix-forward costs keep timing-adjusted no-reuse gamma-1 speedup below 1.0 for every tested exit. A useful implementation likely requires efficient reuse of early-layer work during verification.

## Boundaries and scale limits

No training, no fused KV/cache reuse implementation, no multi-token speculative block validation, no 7B+ model, and no production serving benchmark. Metrics cover 5,461 next-token positions on GPT-2-small.

## Claim scope

Bounded local probe of GPT-2-small early-exit hidden states as one-token draft distributions on WikiText-2 validation contexts. The result supports the mechanism only as a reuse-dependent signal and rejects the standalone no-reuse speedup variant.

## Why it stopped

Proxy/local early falsification: without real shared verification reuse, the measured draft acceptance is too low relative to observed early-prefix cost, so standalone early-exit drafting is slower than full-model decoding in this setup.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next test is a bounded implementation of shared-cache verification that must show end-to-end wall-clock speedup over ordinary GPT-2-small decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end shared-cache early-exit speculative decoding on GPT-2-small
- Success threshold: At least 1.15x median tokens/second speedup over ordinary GPT-2-small decoding across 256 or more generated continuations, with identical target distribution semantics and no more than 10% memory overhead.
- Stop condition: Stop if a correct shared-cache implementation cannot exceed 1.05x median tokens/second speedup or if cache reuse adds enough overhead to erase the acceptance-rate upper bound.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-draft-from-shared-weights-4629abd3d3d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
