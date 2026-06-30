# Per-Head KV Quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `per-head-kv-quantization-bfca23eac609`
Run ID: `per-head-kv-quantization-bfca23eac609-20260523T051744474729+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bb1f540afb65

## What looked useful

Per-head scaling reduced relative KV MSE by 61.9% at 4-bit and 62.7% at 3-bit versus global scaling; it reduced the NLL penalty versus fp16 cache from 0.5094 to 0.2048 at 4-bit and from 2.2414 to 0.9010 at 3-bit.

## Boundaries and scale limits

Small local evaluation only: one small pretrained model, eight built-in text snippets, short contexts up to 96 tokens, Python quantize/dequantize path, no standard validation corpus, no fused kernel, no long-context serving or large-model evidence.

## Claim scope

On a bounded distilgpt2 sequential decode probe over 316 scored tokens, per-head affine min/max KV-cache quantization reduced reconstruction error and next-token NLL degradation versus whole-cache affine quantization at equal 4-bit and 3-bit widths.

## Why it stopped

The run produced a bounded positive mechanism signal but not direct publication-grade evidence; it lacks standard-corpus scale, larger-model coverage, long-context serving, and kernel-level latency/memory validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded evidence should evaluate GPT-2-small or larger on a standard validation set with a production-like per-head KV cache implementation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Standard-corpus per-head KV quantization validation
- Success threshold: Per-head 4-bit KV quantization reduces NLL degradation versus global 4-bit by at least 25% without more than 10% decode latency regression versus the global quantized implementation.
- Stop condition: Stop if per-head 4-bit fails to improve NLL degradation by at least 10% over global 4-bit on the standard validation corpus or if implementation overhead erases practical memory/latency value.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-kv-quantization-bfca23eac609`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
