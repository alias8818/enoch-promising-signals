# Residual-Channel KV Cache to 1.58-bit for Long Context on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-kv-cache-to-1-58-bit-for-long-context-on-cpu-a45973e03161`
Run ID: `residual-channel-kv-cache-to-1-58-bit-for-long-context-on-cpu-a45973e03161-20260529T095301013906+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/396d993366fb

## What looked useful

Ternary_channel_all achieved about 1.599 bits/scalar and 10.0x fp16 compression; attention-output MSE ratios vs the 2-bit proxy were 0.45 on Gaussian, 0.50 on outlier-channel, and 1.98 on residual-correlated distributions. Ternary_asym exceeded the 1.75 bits/scalar target after metadata and failed badly on correlated values.

## Boundaries and scale limits

No trained LLM, tokenizer, real KV traces, perplexity, retrieval benchmark, LongBench/RULER evaluation, or optimized packed ternary CPU kernel was tested. Results are limited to T=2048, H=8, D=64, 64 synthetic queries, 5 seeds, and unpack-to-fp32 NumPy attention.

## Claim scope

NumPy CPU proxy over synthetic KV caches shows per-channel residual ternary coding can reach about 1.60 effective bits per KV scalar including metadata and can beat a simple KIVI-style 2-bit affine proxy on attention-output relative MSE for Gaussian and outlier-channel synthetic distributions, but not for residual-correlated synthetic KV structure.

## Why it stopped

Mixed proxy evidence: the mechanism is compact and sometimes better than the 2-bit proxy, but fails the predeclared error threshold on residual-correlated KV structure and lacks direct real-model quality evidence.

## Recommended next action

Stop paper development for this run; run a bounded follow-up that captures real KV traces from a small open decoder model and evaluates layer-wise residual-channel ternary KV against fp16 and 2-bit baselines on perplexity or long-context retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV trace validation for residual-channel ternary cache
- Success threshold: At <=1.75 effective bits/scalar, residual-channel ternary must have downstream quality degradation no worse than the 2-bit proxy and attention-output relative MSE <=1.25x the 2-bit proxy on at least 80% of tested layers, with no more than 1.2x CPU decode slowdown using an implementation that includes packing/unpacking cost.
- Stop condition: Stop if real-model layer traces show residual-channel ternary exceeds 1.25x the 2-bit proxy attention-output error on more than 20% of layers or if metadata/packing overhead keeps effective storage above 1.75 bits/scalar.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-kv-cache-to-1-58-bit-for-long-context-on-cpu-a45973e03161`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
