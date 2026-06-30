# KV-Cache 2-bit Grouped Quantization: Direct GPT-2-Small CPU Test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-2-bit-grouped-quantization-direct-gpt-2-small-cpu-test-9dd24b3e62c2`
Run ID: `kv-cache-2-bit-grouped-quantization-direct-gpt-2-small-cpu-test-9dd24b3e62c2-20260629T181958455533+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0b7c62679c96

## What looked useful

Actual GPT-2-small past_key_values tolerated grouped 2-bit quantize/dequantize in a small CPU probe: group sizes 16/32/64 all kept top-1 unchanged across three prompts, with mean logit relative L2 between 0.0388 and 0.0600. Synthetic random GPT-2-shape caches showed much larger attention-output error, so the result is a bounded activation-distribution signal rather than a broad robustness claim.

## Boundaries and scale limits

Only short prompts up to 64 tokens, one next-token comparison per prompt, no packed int2 attention kernel, no perplexity or multi-step generation evaluation, and no 3-bit/4-bit baseline comparison.

## Claim scope

On three short prompts with real GPT-2-small CPU inference, dequantizing 2-bit grouped affine KV caches before next-token forward preserved top-1 prediction for all 9 prompt/group cases while modeling 4.0x to 6.4x KV-cache compression versus fp16.

## Why it stopped

This run produced useful small-scope direct evidence but not enough quality, robustness, or packed-kernel performance evidence for a paper.

## Recommended next action

Run a bounded GPT-2-small perplexity and multi-step generation evaluation over a small public text corpus, comparing 2-bit group sizes against fp16 plus 3-bit/4-bit KV baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small perplexity and generation check for grouped 2-bit KV-cache quantization
- Success threshold: Group-size-16 2-bit KV cache has <=5% perplexity regression versus fp16, top-1 next-token agreement >=95% over evaluated positions, and modeled KV-cache compression >=4x versus fp16.
- Stop condition: Stop if group-size-16 exceeds 10% perplexity regression, top-1 agreement falls below 90%, or quantize/dequantize overhead dominates decode time enough to make packed-kernel follow-up unjustified.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-2-bit-grouped-quantization-direct-gpt-2-small-cpu-test-9dd24b3e62c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
