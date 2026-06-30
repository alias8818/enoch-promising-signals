# Activation error-feedback residual channels for sub-4-bit draft models in speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-error-feedback-residual-channels-for-sub-4-bit-draft-models-in-speculative-decoding-413096cb8d54`
Run ID: `activation-error-feedback-residual-channels-for-sub-4-bit-draft-models-in-speculative-decoding-413096cb8d54-20260613T204231946387+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/63c9cb3c594b

## What looked useful

Residual reconstruction gives a bounded mechanism signal: projection-only 3-bit rank-16 improved expected acceptance by +0.079 absolute, reduced KL from 1.625566 to 1.221263, and improved top-1 agreement from 0.335227 to 0.411932 with about 2.78% weighted residual side-path parameters. The 2-bit result improved expected acceptance but remained noisy/mixed.

## Boundaries and scale limits

Only 16 prompts and 352 scored positions; no actual speculative decoding loop, no wall-clock serving benchmark, no custom quantized low-rank kernel, no separate smaller draft architecture, no large model or benchmark-corpus validation.

## Claim scope

On distilgpt2 with transformer projection weights quantized to 2 or 3 bits, dense low-rank reconstruction of quantization error improves one-step target/draft distribution overlap used as a speculative-decoding expected-acceptance proxy; strongest local result is 3-bit rank-16 improving expected acceptance from 0.400466 to 0.479716 on 16 fixed prompts.

## Why it stopped

Proxy evidence is useful but not paper-ready: the run measured one-step distribution overlap under simulated dense residual reconstruction, not real speculative decoding throughput.

## Recommended next action

Run a bounded deepen experiment implementing a real low-rank residual side path inside an actual speculative decoding loop and compare accepted tokens per verifier call plus tokens/sec against no-residual quantized and full-precision draft controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Actual speculative decoding loop for low-rank residual quantized draft projections
- Success threshold: At 3-bit rank <=16, improve accepted tokens per verifier call by at least 10% over no-residual quantized draft and retain a net tokens/sec improvement after residual overhead.
- Stop condition: Stop if acceptance improves but wall-clock tokens/sec is not better than the no-residual quantized draft, or if acceptance gain is below 5% across two benchmark slices.

## Evidence references

- Artifact root: `<local-path>/projects/activation-error-feedback-residual-channels-for-sub-4-bit-draft-models-in-speculative-decoding-4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
