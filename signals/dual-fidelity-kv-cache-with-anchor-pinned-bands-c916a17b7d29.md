# Dual-Fidelity KV Cache with Anchor-Pinned Bands

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dual-fidelity-kv-cache-with-anchor-pinned-bands-c916a17b7d29`
Run ID: `dual-fidelity-kv-cache-with-anchor-pinned-bands-c916a17b7d29-20260524T223141520638+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/500874881783

## What looked useful

At seq_len 8192 with int4 KV, anchor+recent pinning kept 3.32% of positions high fidelity, retained 3.64x compression versus FP16, and reduced relative L2 output error by 96.5-98.4% on structured recent/anchor/mixed traces. A same-budget random high-fidelity policy did not reproduce the effect.

## Boundaries and scale limits

No trained language model, tokenizer, perplexity, retrieval, or generation evaluation was run. Quantization was simulated with per-token symmetric quantize/dequantize and attention used materialized tensors, not a packed-cache fused serving kernel. Sequence lengths were 1024-8192 with 16 heads and 64-dim heads.

## Claim scope

Synthetic single-token decode-attention probes on NVIDIA GB10 show that keeping a recent band plus sparse anchor positions in FP16 while quantizing other KV entries to int4 can sharply reduce attention output error when attention mass is recent-biased, anchor-biased, or mixed; the same policy gives little benefit on random attention.

## Why it stopped

No-paper closure: this run produced a reproducible synthetic mechanism signal, but not direct trained-model or serving-kernel evidence.

## Recommended next action

Run a bounded real-model KV-cache evaluation on a small transformer, comparing all-low, recent-only, anchors-only, anchor+recent, and random-budget policies on perplexity and retrieval/generation accuracy before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model dual-fidelity KV cache policy evaluation
- Success threshold: Anchor+recent policy achieves at least 3x KV memory compression versus FP16 while keeping perplexity degradation under 5% relative to FP16 and outperforming same-budget random pinning on retrieval/generation accuracy.
- Stop condition: Stop if anchor+recent does not beat recent-only, anchors-only, and random-budget controls on either perplexity or retrieval/generation quality at comparable memory.

## Evidence references

- Artifact root: `<local-path>/projects/dual-fidelity-kv-cache-with-anchor-pinned-bands-c916a17b7d29`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
