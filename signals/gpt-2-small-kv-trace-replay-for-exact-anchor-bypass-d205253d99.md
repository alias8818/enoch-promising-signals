# GPT-2-small KV trace replay for exact anchor bypass

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gpt-2-small-kv-trace-replay-for-exact-anchor-bypass-d205253d99`
Run ID: `gpt-2-small-kv-trace-replay-for-exact-anchor-bypass-d205253d99-20260526T012812868919+0000`

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

- Parent run decision: 4-Bit KV Quantization with Exact Anchor Bypass: enoch://control-plane/projects/4-bit-kv-quantization-with-exact-anchor-bypass-504fbc022423/runs/4-bit-kv-quantization-with-exact-anchor-bypass-504fbc022423-20260525T230611019329+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/239c7a000d18

## What looked useful

KV trace replay can hide an exact anchor string from the visible suffix while preserving the anchor's model-state effect in GPT-2-small; suffix-only, wrong-anchor, and zero-cache controls diverged strongly.

## Boundaries and scale limits

Single GPT-2-small model, synthetic prompts, local in-process past_key_values only; no larger models, production serving boundary, cache serialization protocol, or adversarial policy system tested.

## Claim scope

GPT-2-small local CPU inference with Hugging Face Transformers: replaying an exact anchor prefix KV cache while feeding only a visible suffix reproduces the full anchor+suffix continuation within 1e-3 max absolute logit drift and identical 12-token greedy continuations across 3 synthetic anchor cases.

## Why it stopped

No-paper useful signal: direct small-model mechanism support is clear, but publication-grade claims require serving-boundary validation and broader model coverage.

## Recommended next action

Run a bounded serving-boundary follow-up that exposes/imports serialized KV state and verifies whether prompt inspection over only the visible suffix can be bypassed while server-side cache binding prevents the attack.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Serving-boundary KV cache binding test for hidden-anchor replay
- Success threshold: For at least 3 prompts, imported or stale KV replay matches full anchor+suffix greedy continuations and stays below 1e-3 max absolute last-logit drift while prompt-only inspection cannot see the anchor; cache-bound controls must reject or diverge.
- Stop condition: Stop if the serving harness cannot import/reuse KV across visible prompts, or if replay fails to match full anchor+suffix behavior under the same float tolerance in two independently checked prompts.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-kv-trace-replay-for-exact-anchor-bypass-d205253d99`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
