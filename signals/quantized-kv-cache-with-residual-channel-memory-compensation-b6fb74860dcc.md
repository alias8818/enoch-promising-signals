# Quantized KV-Cache with Residual Channel Memory Compensation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-kv-cache-with-residual-channel-memory-compensation-b6fb74860dcc`
Run ID: `quantized-kv-cache-with-residual-channel-memory-compensation-b6fb74860dcc-20260530T062219767298+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/dfc6694998c2

## What looked useful

A single shared per-channel residual vector added to all cached keys does not change softmax attention weights beyond numerical noise because it induces a uniform logit shift per query. Value-side residual memory with small alpha improved output MSE in all 12 synthetic case/bit groups at best alpha, with gains from 5.34% to 60.21%, but larger alpha often worsened results.

## Boundaries and scale limits

Synthetic KV streams only; no pretrained model, perplexity, user-facing generation, latency, or real long-context trace validation. Alpha was swept post hoc over five small values, and memory overhead beyond one shared residual vector was not tested.

## Claim scope

Bounded synthetic causal-attention probe of a low-overhead residual channel memory vector added to dequantized KV cache entries after symmetric per-token quantization. Shared key compensation was inert for attention weights; tuned value compensation improved synthetic attention output MSE.

## Why it stopped

No-paper closure: the current evidence is synthetic/proxy-only and the key-cache part of the low-overhead KV-wide hypothesis is directly falsified in this formulation.

## Recommended next action

Run a bounded deepen test on real transformer KV traces or a small pretrained model decode loop, focusing on V-only residual compensation and comparing quality drift, latency, and memory against plain KV quantization at equal budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace V-only residual compensation for quantized KV cache
- Success threshold: At 3-bit or 4-bit KV quantization, V-only compensation reduces real-trace attention-output MSE or logits KL by at least 10% versus plain quantization without worsening perplexity proxy or decode latency by more than 2%.
- Stop condition: Stop if real traces show less than 5% drift reduction at all tested alphas, if latency overhead exceeds 5%, or if quality/perplexity proxy worsens relative to plain quantization.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-kv-cache-with-residual-channel-memory-compensation-b6fb74860dcc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
