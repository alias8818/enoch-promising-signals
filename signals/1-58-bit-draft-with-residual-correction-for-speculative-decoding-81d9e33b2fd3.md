# 1.58-bit draft with residual correction for speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-58-bit-draft-with-residual-correction-for-speculative-decoding-81d9e33b2fd3`
Run ID: `1-58-bit-draft-with-residual-correction-for-speculative-decoding-81d9e33b2fd3-20260608T110416206140+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f51065dc37c2

## What looked useful

Residual correction monotonically improved KL, acceptance alpha, top-1 agreement, and top-5 teacher-token retention, with rank-64 reducing KL by 34.2% and increasing alpha by 0.0230 absolute versus pure ternary. The same rank reduced the gamma-4 speed proxy from 2.2978 to 1.7792 because residual compute outweighed the acceptance gain.

## Boundaries and scale limits

No trained transformer, no real prompt distribution, no learned residual adapter, no ternary/residual latency kernel, and no end-to-end target verification benchmark. The result is a bounded proxy and early practical falsification, not full-scale validation.

## Claim scope

In a synthetic structured logit-head proxy with d_model=512, vocab=4096, and five seeds, oracle low-rank residual correction on top of a 1.58-bit ternary draft improves teacher-distribution fidelity and speculative acceptance alpha, but not the cost-adjusted gamma-4 speed proxy under the stated dense-equivalent cost model.

## Why it stopped

Bounded proxy supports residual-fidelity improvement but early-falsifies the practical speedup claim under the local cost model; this is not direct/full validation.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next, test a learned and selectively gated residual adapter in a trained small transformer and require cost-adjusted wall-clock speculative throughput to beat a pure ternary draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned gated residual correction for a trained small ternary draft
- Success threshold: Selective residual correction improves wall-clock tokens/sec by at least 10% over the pure ternary draft at equal target model and block size, while preserving exact target distribution verification.
- Stop condition: Stop if learned/gated residual correction fails to beat the pure ternary draft in wall-clock tokens/sec or requires residual invocation on most tokens.

## Evidence references

- Artifact root: `<local-path>/projects/1-58-bit-draft-with-residual-correction-for-speculative-decoding-81d9e33b2fd3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
