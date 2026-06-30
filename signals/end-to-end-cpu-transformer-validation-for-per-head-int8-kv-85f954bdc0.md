# End-to-end CPU transformer validation for per-head int8 KV cache

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `end-to-end-cpu-transformer-validation-for-per-head-int8-kv-85f954bdc0`
Run ID: `end-to-end-cpu-transformer-validation-for-per-head-int8-kv-85f954bdc0-20260605T121913826621+0000`

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

- Parent run decision: Per-Head Quantized KV-Cache on CPU for Long Context: enoch://control-plane/projects/per-head-quantized-kv-cache-on-cpu-for-long-context-a4e1700936dd/runs/per-head-quantized-kv-cache-on-cpu-for-long-context-a4e1700936dd-20260605T044814108706+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/752afe044432

## What looked useful

Per-head int8 KV cache preserved generated-token and top-1 logit agreement at 1.0 mean, with mean KL 1.394e-05 and 3.2x measured cache-byte reduction versus FP32 in a direct CPU autoregressive decode loop. The same test found naive dequantization is a performance risk.

## Boundaries and scale limits

Small random model only; no pretrained model quality, long-context benchmark, batch>1 serving, optimized CPU kernel, real RSS pressure study, or large-model validation. Naive dequantization was slower than FP32 by 1.41x in the calibrated run.

## Claim scope

Tier 1 small direct CPU validation: a NumPy decoder-only transformer with 3 layers, d_model 96, 6 heads, batch 1, prompt length 48, and generation length 64 preserved FP32 greedy decode outputs with per-token, per-head int8 KV cache across three prompt seeds while reducing measured KV cache bytes by 3.2x.

## Why it stopped

No-paper useful signal: the controlled Tier 1 direct test supports the correctness and memory mechanism but is too small and unoptimized for publication-grade or production-serving claims.

## Recommended next action

Run a bounded pretrained CPU decode follow-up using a small GPT-2-class or Llama-style checkpoint with FP32 KV versus per-head int8 KV, measuring logprob drift, token agreement, RSS, and optimized-kernel latency at longer context.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained CPU decode validation for per-head int8 KV cache
- Success threshold: Token agreement >= 0.98, mean KL(FP32||int8) <= 1e-3, cache or RSS reduction >= 3x, and latency overhead <= 10% at the largest tested context.
- Stop condition: Stop as no-paper negative if token agreement falls below 0.98, mean KL exceeds 1e-3, memory reduction is below 3x, or an optimized CPU path remains more than 10% slower than FP32 at the target context length.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-cpu-transformer-validation-for-per-head-int8-kv-85f954bdc0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
