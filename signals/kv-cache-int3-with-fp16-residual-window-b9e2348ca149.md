# KV Cache INT3 with FP16 Residual Window

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-int3-with-fp16-residual-window-b9e2348ca149`
Run ID: `kv-cache-int3-with-fp16-residual-window-b9e2348ca149-20260516T143652236670+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3b8b513aeb52

## What looked useful

INT3 KV cache with a suffix FP16 residual window gives estimated 2.49x-4.78x compression for nontrivial windows, but long-context output error remains high: at seq_len 8192, a 512-token FP16 window improves mean relative RMSE only from 0.3726 to 0.3636 while compression drops from 4.92x to 3.95x. The naive path is 3.7x-22.1x slower than FP16.

## Boundaries and scale limits

No real transformer perplexity/task evaluation, no real KV activation traces, no fused INT3 attention kernel, and no production serving benchmark. Latency is for a naive PyTorch quantize/dequantize path.

## Claim scope

Synthetic GB10 decode-attention probe for batch=1, heads=8, head_dim=128, seq_len up to 8192, signed INT3 per-token group quantization with FP16 scales and suffix FP16 residual windows.

## Why it stopped

Bounded synthetic evidence is a useful early falsification of the simple suffix-residual INT3 KV-cache hypothesis, not a full validation or publication-grade result.

## Recommended next action

Stop this no-paper run; if continuing locally, run a bounded branch test using attention-mass-selected FP16 exceptions instead of a suffix-only residual window.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Attention-mass-selected FP16 exceptions for INT3 KV cache
- Success threshold: At seq_len 8192 with heads=8 and head_dim=128, adaptive FP16 exceptions must achieve at least 25% lower mean relative RMSE than all-INT3 at >=4x estimated compression and outperform the suffix residual window at the same FP16-token budget.
- Stop condition: Stop if adaptive exceptions fail to beat suffix residual error by at least 10% at the same FP16-token budget or cannot maintain >=4x estimated compression.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-int3-with-fp16-residual-window-b9e2348ca149`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
