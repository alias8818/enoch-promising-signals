# Joint Residual-Channel Quantization and Speculative Decoding for Small Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `joint-residual-channel-quantization-and-speculative-decoding-for-small-agents-39fd40287e93`
Run ID: `joint-residual-channel-quantization-and-speculative-decoding-for-small-agents-39fd40287e93-20260524T164031044611+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5c558e37ba4a

## What looked useful

Best residual-channel method top64_i6_tail_i3 improved medium-run acceptance bound from 0.926055 to 0.953493 and simulated accept rate from 0.925803 to 0.953295 at 0.755859 of the uniform int4 payload. Robustness sweep showed positive acceptance-bound deltas of 0.008286, 0.030031, and 0.048082 for sharpness 0.8, 1.1, and 1.4.

## Boundaries and scale limits

No real small-agent model logits, tokenizer, prompt distribution, target/draft model pair, GPU kernel, KV-cache behavior, or end-to-end tokens/sec serving measurement was tested. Evidence is CPU-only and synthetic.

## Claim scope

On synthetic Zipf-like next-token distributions, a residual-channel draft-logit quantizer that preserves a small high-probability token channel and separately quantizes the tail improves speculative decoding acceptance over uniform int4 logit quantization while using less payload.

## Why it stopped

Proxy-only synthetic evidence supports the mechanism but does not validate real small-agent speculative decoding performance.

## Recommended next action

Stop this run as no-paper useful signal; next run should replay the acceptance diagnostic on real draft and target model logits before any paper-writing decision.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-logit residual-channel quantization for small-model speculative decoding
- Success threshold: At matched or lower payload than uniform int4, residual-channel quantization improves mean acceptance bound by at least 0.01 and measured tokens/sec by at least 5% without worse task output quality on the prompt set.
- Stop condition: Stop if real-logit acceptance-bound gain is below 0.005 or end-to-end tokens/sec does not improve after controlling for quantization/dequantization overhead.

## Evidence references

- Artifact root: `<local-path>/projects/joint-residual-channel-quantization-and-speculative-decoding-for-small-agents-39fd40287e93`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
