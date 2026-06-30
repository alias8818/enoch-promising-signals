# Channel-Wise Residual KV Quant for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `channel-wise-residual-kv-quant-for-long-context-848724642fde`
Run ID: `channel-wise-residual-kv-quant-for-long-context-848724642fde-20260527T105630862404+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9544abdcc655

## What looked useful

The mechanism is conditionally promising: channel-wise scaling plus sparse per-channel residual restoration helps when KV activations have channel-local heavy tails, but it is not a universal improvement and depends on real model caches exhibiting that structure.

## Boundaries and scale limits

No real pretrained transformer KV caches, no end-to-end perplexity or retrieval benchmark, no serving latency or memory-bandwidth measurement, and no production paged-cache integration. Synthetic tensors stress the intended mechanism but do not establish model-quality preservation.

## Claim scope

Synthetic long-context KV-cache attention probe up to 16,384 tokens, 8 heads, 64-dimensional heads, 64 query positions, 4-bit symmetric quantization, and 3.125% residual restoration. Channel-wise residual quantization reduced attention-output MSE versus per-token baselines on heavy-tailed channel tensors at 1k-8k tokens and reached rough parity at 16k, but was worse on IID Gaussian controls.

## Why it stopped

Closed as no-paper useful signal because the local evidence is synthetic/proxy only, although it identifies a concrete mechanism and a clear negative boundary.

## Recommended next action

Run the same quantization comparison on dumped KV caches from a small real long-context transformer and require both layer-level attention-output distortion gains and no task-level quality regression before considering a paper path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV cache validation for channel-wise residual quantization
- Success threshold: At least 10% lower mean attention-output MSE than per-token recent-residual quantization on real KV caches, no worse than 1% relative degradation on the chosen task metric, and no more than 10% latency overhead at matched effective bit budget.
- Stop condition: Stop if real KV caches do not show channel-local heavy-tail structure or if channel-wise residual fails to beat per-token recent-residual attention-output MSE on a majority of evaluated layers.

## Evidence references

- Artifact root: `<local-path>/projects/channel-wise-residual-kv-quant-for-long-context-848724642fde`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
