# 4-bit Coupled Norms Enable 2x Context GPT2

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `4-bit-coupled-norms-enable-2x-context-gpt2-c5e11467afb9`
Run ID: `4-bit-coupled-norms-enable-2x-context-gpt2-c5e11467afb9-20260607T032837385881+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae5d5ea133b6

## What looked useful

4-bit KV accounting easily supports more than 2x fp16 context memory in all tested variants, but the coupled-norm variants did not improve fidelity over a simple per-vector separate-norm int4 control. On real GPT-2 first-layer activations at 1024 tokens, per-vector separate norm achieved rel_RMSE 0.147 and cosine 0.989, while coupled pair norm degraded to rel_RMSE 0.552 and cosine 0.842; coupled RMS norm was rel_RMSE 0.469 and cosine 0.887.

## Boundaries and scale limits

No full language-model perplexity, generation, training, or true 2048-token GPT-2 learned-position evaluation was run. The 2048-token evidence is synthetic attention only because stock GPT-2 learned positions are limited to 1024.

## Claim scope

Bounded probes of 4-bit KV-cache quantization for GPT-2-small-shaped attention at 1024 and 2048 synthetic tokens, plus real cached GPT-2 first-layer activations at 512 and 1024 tokens.

## Why it stopped

Proxy and direct first-layer evidence falsify the specific coupled-norm advantage; this is not a full validation of all 4-bit KV-cache methods or all 2x-context schemes.

## Recommended next action

Do not pursue the coupled-norm claim as stated; if continuing locally, test the stronger per-vector separate-norm 4-bit KV cache in an end-to-end GPT-2 perplexity/generation harness with explicit 1024-token and position-extension controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2 perplexity test for per-vector int4 KV cache
- Success threshold: Per-vector int4 KV cache changes 1024-token validation perplexity by less than 5% versus fp16 while reducing measured KV-cache bytes by at least 2x and outperforming coupled-norm variants on perplexity or logit error.
- Stop condition: Stop if per-vector int4 increases perplexity by 10% or more versus fp16, or if measured KV-cache savings are below 2x after scale overhead.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-coupled-norms-enable-2x-context-gpt2-c5e11467afb9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
