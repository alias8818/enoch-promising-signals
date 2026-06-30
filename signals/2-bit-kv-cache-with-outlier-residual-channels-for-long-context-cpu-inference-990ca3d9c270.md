# 2-bit KV-Cache with Outlier Residual Channels for Long-Context CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-outlier-residual-channels-for-long-context-cpu-inference-990ca3d9c270`
Run ID: `2-bit-kv-cache-with-outlier-residual-channels-for-long-context-cpu-inference-990ca3d9c270-20260613T111200050386+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/faf8d73e53c5

## What looked useful

Best residual strategy kept 12.5% of channels in fp16, reduced mean relative L2 attention-output error from 1.697225 to 0.546194 versus all-channel 2-bit, and used an estimated 11.8% of fp32 KV-cache memory. Residual variants improved 62 of 63 case-trials, with one recorded failure case.

## Boundaries and scale limits

No real LLM, tokenizer, transformer stack, packed 2-bit kernel, long-context task accuracy, perplexity, or end-to-end CPU serving throughput was tested. Evidence is mechanism-level and synthetic only.

## Claim scope

Synthetic NumPy CPU attention proxy with controlled outlier K/V channels, sequence lengths 512-4096, dim 128, and 63 case-trials: fp16 residual outlier channels reduce attention-output error versus all-channel 2-bit quantization at materially lower estimated KV-cache memory than fp32.

## Why it stopped

Proxy-only evidence supports the residual-channel mechanism but is insufficient for a paper or full validation of long-context CPU inference performance.

## Recommended next action

Stop this worker run as a proxy-only useful signal; next bounded action is to replay real KV traces from a small transformer and compare fp16, int8, all-channel 2-bit, and residual 2-bit on attention-output error and perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-transformer KV trace validation for residual 2-bit cache
- Success threshold: Residual 2-bit at <=15% fp32 cache memory reduces attention-output relative L2 by at least 50% versus all-channel 2-bit and keeps perplexity degradation within a predeclared bound versus fp16 on the tested small model.
- Stop condition: Stop if residual 2-bit fails to improve attention-output error by at least 25% versus all-channel 2-bit on real traces, or if perplexity degradation remains close to all-channel 2-bit despite residual channels.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-outlier-residual-channels-for-long-context-cpu-inference-990ca3d9c270`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
