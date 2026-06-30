# KVQ-Res: Per-Head Residual Scales for 2-bit KV Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kvq-res-per-head-residual-scales-for-2-bit-kv-cache-31403145d13e`
Run ID: `kvq-res-per-head-residual-scales-for-2-bit-kv-cache-31403145d13e-20260621T200522164434+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/934896233762

## What looked useful

2-bit KV cache quantization error has stable per-head structure that a tiny calibration payload can reduce at reconstruction level, but reconstruction gains did not reliably translate into lower next-token distribution drift.

## Boundaries and scale limits

Tested only distilgpt2, 12 calibration prompts, 12 held-out prompts, short prefix-cache next-token inference, and a transparent 2-bit per-token min/max proxy quantizer. No long-context generation, corpus perplexity, custom packed cache kernel, or large-model validation was run.

## Claim scope

On a bounded distilgpt2 held-out prompt probe, one affine correction per layer/head/K-or-V kind improved 2-bit KV cache reconstruction MSE by about 21.6% and average next-token logit MSE by about 20.1%, but did not improve held-out KL divergence.

## Why it stopped

No-paper useful signal: this bounded direct cache-forward probe supports the reconstruction mechanism but gives mixed downstream inference evidence, with KL slightly worse on average and worse on 8 of 12 held-out prompts.

## Recommended next action

Run one bounded deepening experiment that fits per-head corrections against downstream KL or loss on held-out corpus windows and compares no-correction, scale-only, and affine correction under the same 2-bit KV quantizer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KL-calibrated per-head correction for 2-bit KV cache
- Success threshold: Corrected 2-bit KV must improve held-out KL or perplexity by at least 10% relative to uncorrected 2-bit KV without worsening top-1 agreement or cache MSE, across at least 100 held-out windows.
- Stop condition: Stop if KL/perplexity is flat or worse than uncorrected 2-bit KV on held-out windows despite reconstruction improvement, because that would indicate the correction objective is misaligned with inference quality.

## Evidence references

- Artifact root: `<local-path>/projects/kvq-res-per-head-residual-scales-for-2-bit-kv-cache-31403145d13e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
