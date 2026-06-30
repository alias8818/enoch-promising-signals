# Per-Channel 2-Bit KV Quantization for Extended Context on Small VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-channel-2-bit-kv-quantization-for-extended-context-on-small-vram-d5d8a95c5b43`
Run ID: `per-channel-2-bit-kv-quantization-for-extended-context-on-small-vram-d5d8a95c5b43-20260531T112253446285+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4d4231f33a1c

## What looked useful

Per-channel won 6/12 attention-output relative-MSE cases and reached 7.98x compression at 8192 tokens versus 6.4x for per-token. It strongly beat per-token on channel-outlier distributions but lost consistently on iid Gaussian and slow-drift distributions.

## Boundaries and scale limits

No real model perplexity, generation, layerwise accumulation, prompts beyond 8192 tokens, or fused packed 2-bit serving kernels were tested. The KV distributions are controlled synthetic proxies, not captured activations from a trained LLM.

## Claim scope

Synthetic attention-replay evidence up to 8192 tokens shows per-channel affine 2-bit KV quantization provides near-ideal 8x fp16-cache compression and is best when KV error is dominated by persistent high-variance channels, but it is not uniformly better than per-token 2-bit quantization.

## Why it stopped

Bounded proxy evidence is mixed and not paper-ready; it early-falsifies the broad claim that per-channel 2-bit KV is generally superior, while preserving a narrower mechanism worth testing on real model activations.

## Recommended next action

Run a bounded real-model replay using captured K/V and queries from a small transformer, measuring layerwise attention-output error plus perplexity drift for per-channel versus per-token 2-bit KV.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV replay for per-channel 2-bit cache quantization
- Success threshold: Per-channel must beat per-token on model-level perplexity or logit drift at equal or better compression in the layers/heads predicted to have stable channel outliers, without catastrophic degradation elsewhere.
- Stop condition: Stop if per-channel fails to beat per-token in any captured real-model layer/head category or if perplexity/logit drift is worse at the same context length despite better compression.

## Evidence references

- Artifact root: `<local-path>/projects/per-channel-2-bit-kv-quantization-for-extended-context-on-small-vram-d5d8a95c5b43`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
