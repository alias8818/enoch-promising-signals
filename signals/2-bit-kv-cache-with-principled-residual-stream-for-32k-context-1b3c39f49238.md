# 2-bit KV Cache with Principled Residual Stream for 32k Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `2-bit-kv-cache-with-principled-residual-stream-for-32k-context-1b3c39f49238`
Run ID: `2-bit-kv-cache-with-principled-residual-stream-for-32k-context-1b3c39f49238-20260621T113732149475+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2f909791b33b

## What looked useful

At 32,768 tokens, all-2-bit KV had attention-output relative MSE 0.261282. Keeping the most recent 1,024 tokens in fp16 had the same error because it captured no distant retrieval tokens. Calibration-attention residual selection reduced relative MSE to 0.031845 while retaining 27/32 retrieval tokens at 6.56x idealized KV compression; K-norm and oracle selection retained 32/32 and reached near-zero error.

## Boundaries and scale limits

No real LLM perplexity, passkey, LongBench, throughput, or custom kernel evaluation was run. The synthetic generator uses heavy-tailed activations and designed distant retrieval tokens, so it is a mechanism probe rather than a deployment validation.

## Claim scope

Synthetic direct attention-output fidelity probe at up to 32,768 context tokens shows that 2-bit KV quantization benefits from a principled fp16 residual selector when important tokens are distant; recency-only residuals did not improve the stressor.

## Why it stopped

No-paper useful signal only: this is synthetic/proxy mechanism evidence, not full validation, and adjacent prior work already establishes broad 2-bit KV plus residual-cache methods.

## Recommended next action

Run a bounded real-model 32k passkey/perplexity benchmark comparing all-2-bit, recent residual, calibration-mass residual, and K-norm residual using an existing KIVI/KVQuant-style implementation; stop if principled residuals do not beat recent residuals at matched memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model 32k residual-selector benchmark for 2-bit KV cache
- Success threshold: Principled residual selection beats recent-only residual by at least 25% relative error reduction or a statistically clear retrieval-accuracy gain at the same idealized KV memory budget, without more than 10% decoding overhead in the measured setup.
- Stop condition: Stop as negative if real-model metrics show no improvement over recent-only residual at matched memory on two seeds or if selector overhead dominates the compression benefit.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-principled-residual-stream-for-32k-context-1b3c39f49238`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
