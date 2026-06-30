# 2-bit KV Cache with Layer-Adaptive Residual Streams for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-layer-adaptive-residual-streams-for-long-context-f635be73ab5b`
Run ID: `2-bit-kv-cache-with-layer-adaptive-residual-streams-for-long-context-f635be73ab5b-20260630T012802127136+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d9402cc56d81

## What looked useful

Adaptive residual allocation can modestly improve 2-bit KV attention reconstruction under equal memory, but calibration can starve layers and 8 seed/layer cases regressed versus fixed residuals.

## Boundaries and scale limits

Synthetic single-head attention tensors only; no pretrained model, perplexity, generation quality, real 2-bit packing, GPU kernels, or serving throughput were tested.

## Claim scope

In a bounded synthetic NumPy attention probe, layer-adaptive allocation of recent full-precision residual KV tokens reduced held-out attention-output relative MSE by 2.26% versus a fixed per-layer residual window at the same estimated memory budget.

## Why it stopped

Proxy synthetic evidence is useful but insufficient for a paper or full validation; this run should close as no-paper evidence rather than continue scaling the proxy.

## Recommended next action

Run a bounded real-transformer follow-up on a GPT-2-small-class model or smaller local equivalent, measuring long-context perplexity and generation deltas for dense fp16, 2-bit fixed residual, and 2-bit layer-adaptive residual KV caches.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model 2-bit KV adaptive residual perplexity probe
- Success threshold: Adaptive residual condition improves long-context perplexity or next-token KL/error by at least 2% versus fixed residual at matched KV memory, with no worse than 0.5% degradation on short-context control prompts.
- Stop condition: Stop if adaptive fails to beat fixed residual on real-model metrics at matched memory across at least two seeds or dataset shards, or if implementation requires non-local/private model artifacts.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-layer-adaptive-residual-streams-for-long-context-f635be73ab5b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
