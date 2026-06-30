# 2-bit KV cache with per-channel residual means for long context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-per-channel-residual-means-for-long-context-5f355af593d1`
Run ID: `2-bit-kv-cache-with-per-channel-residual-means-for-long-context-5f355af593d1-20260607T090305219836+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/26d63467276c

## What looked useful

Residual means consistently reduced K/V reconstruction MSE by about 0.8-1.0% with 5.9% estimated storage overhead and usually improved the attention-output proxy, but the effect was small and 4-bit remained much stronger.

## Boundaries and scale limits

No real transformer KV traces, no end-to-end model quality metrics, no long-context benchmark, no decode kernel or serving latency measurement, and CPU-only synthetic tensors.

## Claim scope

Bounded synthetic NumPy proxy: per-block/per-channel residual mean correction on 2-bit symmetric KV quantization for seq=8192, heads=8, dim=64 synthetic K/V tensors across Gaussian, biased, drift, and skew/outlier distributions.

## Why it stopped

Synthetic/proxy evidence supports a small bias-correction mechanism but not a publication-grade or full viability claim; attention proxy is noisy for skew/outlier tensors and 4-bit remains much better.

## Recommended next action

Stop this worker run as no-paper useful signal; the concrete next bounded test is to replay the same residual-mean correction on real transformer KV traces and evaluate perplexity or retrieval quality against plain 2-bit and 4-bit baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate 2-bit residual-mean KV quantization on real transformer KV traces
- Success threshold: 2-bit plus residual means improves at least one end-to-end quality metric by >=5% relative error reduction versus plain 2-bit without more than 10% KV storage overhead and without regressing decode latency by more than 5% in a prototype.
- Stop condition: Stop if real-trace K/V MSE improvement remains below 1% and end-to-end quality improvement is below 2% relative to plain 2-bit across tested prompts.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-per-channel-residual-means-for-long-context-5f355af593d1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
