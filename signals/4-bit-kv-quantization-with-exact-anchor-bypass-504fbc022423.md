# 4-Bit KV Quantization with Exact Anchor Bypass

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `4-bit-kv-quantization-with-exact-anchor-bypass-504fbc022423`
Run ID: `4-bit-kv-quantization-with-exact-anchor-bypass-504fbc022423-20260525T230611019329+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/239c7a000d18

## What looked useful

Across 1536 synthetic trials, anchor-bypass benefit tracked anchor attention mass strongly (correlation 0.9743 with improvement; 0.9736 with anchor-vs-random delta). Medium anchor cases reduced relative L2 error by about 90-100% while random exact-token bypass stayed near 0%; no-anchor-bias controls showed only about 0-4% improvement.

## Boundaries and scale limits

No real transformer KV traces, no end-to-end perplexity or generation quality, no decode kernel, and memory overhead excludes scale/metadata layout costs. Tested seq_len <= 2048, dim <= 128, 32 trials per group.

## Claim scope

Synthetic single-step attention probe: exact fp16 bypass of known high-attention KV anchor rows reduces relative L2 attention-output error versus all-int4 KV and same-count random exact-row controls.

## Why it stopped

No-paper useful signal: the mechanism is supported by direct synthetic attention-output tests, but full validation requires real model KV traces and end-to-end metrics.

## Recommended next action

Run a bounded GPT-2-small-class trace replay measuring next-token logit/perplexity error and decode memory including quantization metadata for all-int4, exact-anchor bypass, and random-bypass controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small KV trace replay for exact anchor bypass
- Success threshold: Exact-anchor bypass improves logit/perplexity error by at least 25% over all-int4 and at least 15% over random bypass at <=5% measured KV-cache memory overhead on the replayed traces.
- Stop condition: Stop if anchor bypass is not better than random bypass on real traces, if measured overhead exceeds 5% for the tested anchor budget, or if real attention mass on selectable anchors is too low to affect output error.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-kv-quantization-with-exact-anchor-bypass-504fbc022423`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
