# Residual Channels for KV Cache Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channels-for-kv-cache-compression-c0dc427ee79b`
Run ID: `residual-channels-for-kv-cache-compression-c0dc427ee79b-20260602T170010693345+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/96eff9dcdbc4

## What looked useful

Across 50 seeds, heavy-tail KV residual4 saliency + int3 remainder achieved relative MSE 0.012522 versus uniform int4 0.147754, a 91.5% reduction at 3.8125 average bits/value; random residual channels were worse than uniform int4. In isotropic KV, residual4 saliency + int3 was 5.22x worse than uniform int4.

## Boundaries and scale limits

No pretrained transformer, real text, perplexity, long-context decoding, or serving-kernel throughput was tested. The positive result is mechanism evidence from synthetic tensors only.

## Claim scope

Synthetic NumPy attention proxy with per-token symmetric KV quantization: exact residual channels selected by saliency or variance reduce attention-output error when persistent heavy-tail KV channel outliers are present, but they are not a general improvement under isotropic KV distributions.

## Why it stopped

Closed as no-paper useful signal: synthetic evidence supports the mechanism only under structured outlier channels and does not validate the method on real model KV caches.

## Recommended next action

Run a bounded direct trace validation on a pretrained small transformer, measuring KV attention-output error and next-token KL/perplexity for residual-channel int3+exact versus uniform int4.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-channel KV compression on real small-transformer traces
- Success threshold: Residual4 saliency + int3 remainder beats uniform int4 by at least 20% relative attention-output MSE and does not worsen next-token KL/perplexity beyond a predeclared small tolerance, while random residual channels fail to match the gain.
- Stop condition: Stop if real KV traces do not show persistent high-saliency channels, if saliency residual channels fail to beat uniform int4 on direct attention-output metrics, or if next-token KL/perplexity degradation exceeds the tolerance.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channels-for-kv-cache-compression-c0dc427ee79b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
