# Ternary KV cache with per-head residual scalars

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `ternary-kv-cache-with-per-head-residual-scalars-135a0ccfcb32`
Run ID: `ternary-kv-cache-with-per-head-residual-scalars-135a0ccfcb32-20260525T223541653720+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/85f01aa3b2bb

## What looked useful

Adding one per-head residual offset scalar to scale-only ternary K and V changed mean relative L2 attention-output error by only 0.28% at the best tested threshold, while the residual ternary cache still had high mean relative L2 error of 0.644.

## Boundaries and scale limits

No full perplexity, generation, long-context, kernel throughput, packing, or large-model validation; quantizer was a simple fixed-threshold ternary scheme.

## Claim scope

Bounded local attention-output fidelity test on synthetic KV tensors and four distilgpt2 attention-layer traces at 256 tokens; per-head residual offsets plus scales did not materially improve fixed-threshold ternary KV over per-head scale-only ternary.

## Why it stopped

Early bounded falsification: a direct attention-output proxy showed negligible residual-scalar benefit and high ternary KV error, but this is not a full model-quality validation.

## Recommended next action

Stop this exact mechanism; only revisit ternary KV if the follow-up tests a different quantizer or residual representation with a direct perplexity threshold.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Optimized ternary KV quantizer against int4 KV on GPT-2-small-class perplexity
- Success threshold: On GPT-2-small-class, optimized ternary KV must be within 10% relative perplexity degradation of fp16 KV and no worse than an int4 KV baseline at comparable or lower memory.
- Stop condition: Stop if a tuned ternary quantizer still has mean relative L2 attention-output error above 0.25 or loses to int4 KV on both perplexity and memory-adjusted fidelity.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-kv-cache-with-per-head-residual-scalars-135a0ccfcb32`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
