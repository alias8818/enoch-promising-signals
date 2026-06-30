# Residual-Split KV Cache Extreme Quantization

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `residual-split-kv-cache-extreme-quantization-ada8d591b08d`
Run ID: `residual-split-kv-cache-extreme-quantization-ada8d591b08d-20260604T094944032373+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8f397d98905f

## What looked useful

1-bit bulk KV quantization remained highly destructive even with residual fp16 channels: GPT-2-small mean attention-output relative RMSE was 3.63-3.55 for channel residual formats at 1.94-2.88 average raw bits, versus 0.92 for uniform 2-bit and 0.43 for uniform 3-bit. An optimistic residual-element oracle also failed, suggesting the binary bulk representation is the limiting factor. A 2-bit residual channel variant slightly improved over uniform 2-bit but was not competitive with near-equal-bit uniform 3-bit.

## Boundaries and scale limits

No end-to-end perplexity, generation-quality, long-context serving, kernel-throughput, metadata-overhead, or larger-model validation was run. Raw bit budgets exclude scale metadata; the element oracle also excludes sparse mask/index cost.

## Claim scope

Bounded negative result for simple residual-split KV cache quantization on synthetic heavy-tailed tensors and GPT-2-small activation attention reconstruction. The tested schemes kept 6.25% or 12.5% fp16 residual channels, or an optimistic top-element oracle, while quantizing the remaining K/V elements to 1-2 bits.

## Why it stopped

Proxy/early falsification: direct attention-reconstruction tests on GPT-2-small activations and synthetic outlier tensors did not support simple residual-split 1-bit KV quantization, and the modest 2-bit residual gain was not bit-budget competitive.

## Recommended next action

Stop this simple residual-split extreme-quantization line as a no-paper early falsification; only revisit with a bit-accounted 2-bit-plus residual design that directly beats uniform 3-bit on perplexity and attention error at the same serialized bits.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bit-accounted 2-bit residual KV cache versus uniform 3-bit on GPT-2-small perplexity
- Success threshold: At equal serialized bits, residual 2-bit KV must reduce perplexity delta and attention-output relative RMSE by at least 15% versus the best uniform 3-bit/groupwise baseline without adding unmodeled metadata or kernel costs.
- Stop condition: Stop if serialized-bit accounting makes residual 2-bit use at least as many bits as uniform 3-bit without lower perplexity delta, or if attention-output RMSE remains above the uniform 3-bit baseline.

## Evidence references

- Artifact root: `<local-path>/projects/residual-split-kv-cache-extreme-quantization-ada8d591b08d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
