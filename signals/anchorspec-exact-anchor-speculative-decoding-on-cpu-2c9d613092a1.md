# AnchorSpec: exact-anchor speculative decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchorspec-exact-anchor-speculative-decoding-on-cpu-2c9d613092a1`
Run ID: `anchorspec-exact-anchor-speculative-decoding-on-cpu-2c9d613092a1-20260620T052542483747+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cc79cf7494ed

## What looked useful

Anchor gating is a plausible exact mechanism, but the CPU speedup claim is sensitive to batch efficiency and draft cost. In the conservative model at draft cost ratio 0.05, anchor-gated speedup was 0.711-0.993x and never beat direct decoding across 9 synthetic cases.

## Boundaries and scale limits

No real transformer target/draft pair was benchmarked; CPU batching, cache effects, tokenizer/model overhead, and BLAS/attention kernel behavior were represented only by cost models.

## Claim scope

Synthetic Markov-language-model proxy shows anchor-gated exact speculative decoding preserves the standard accept/reject exactness correction and can improve vanilla speculative oracle counts under draft-target mismatch, but it does not show robust speedup over direct decoding under a conservative CPU batch cost model.

## Why it stopped

Closed as a no-paper proxy result: exactness and mechanism are supported, but robust CPU throughput is not validated without real model wall-clock evidence.

## Recommended next action

Run a bounded direct CPU wall-clock benchmark with a small transformer target/draft pair and the same direct, vanilla speculative, and anchor-gated decoding controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU transformer benchmark for anchor-gated exact speculative decoding
- Success threshold: Anchor-gated decoding achieves at least 1.15x end-to-end CPU tokens/s over direct decoding and at least 1.05x over vanilla speculative decoding on the same model/prompt set, with exactness preserved by the standard accept/reject correction.
- Stop condition: Stop if anchor-gated decoding is below 1.0x direct tokens/s in two threshold settings or if measured draft plus batch overhead exceeds saved target scalar calls.

## Evidence references

- Artifact root: `<local-path>/projects/anchorspec-exact-anchor-speculative-decoding-on-cpu-2c9d613092a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
