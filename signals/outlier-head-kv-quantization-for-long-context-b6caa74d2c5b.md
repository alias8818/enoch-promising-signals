# Outlier-Head KV Quantization for Long Context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `outlier-head-kv-quantization-for-long-context-b6caa74d2c5b`
Run ID: `outlier-head-kv-quantization-for-long-context-b6caa74d2c5b-20260607T044945200777+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/2342148c1368

## What looked useful

Head selection has a measurable effect over random controls, but aggressively quantizing most heads to 2 bit leaves too much distributed error. Uniform 4-bit KV quantization was the stronger baseline by a wide margin.

## Boundaries and scale limits

Single small causal LM, deterministic repeated text prompts, one-token decode metrics, context limited to 1023 tokens, simple symmetric per-head quantization, no fused serving kernel, no multi-token generation, no downstream benchmark, and no larger long-context model.

## Claim scope

On distilgpt2 KV-cache decode for sequence lengths 128 to 1023, a simple per-layer high-KV-energy outlier-head policy with 2-bit non-outlier heads and 8-bit preserved heads reduces error versus uniform 2-bit in some settings but is much worse than uniform 4-bit, including at the same 4.0 average bit budget.

## Why it stopped

Early bounded negative result: the same-average-bit outlier policy had mean KL 2.2602 versus 0.0779 for uniform 4-bit and mean NLL delta 2.0162 versus 0.1162, so the tested mechanism does not support a publication-grade long-context KV quantization claim.

## Recommended next action

Stop this policy as not paper-ready; only revisit with a bounded follow-up that tests a stronger head score or 3-bit non-outlier policy against uniform 4-bit on the same decode KL/NLL metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-Aware Outlier-Head KV Quantization with 3-Bit Non-Outlier Heads
- Success threshold: A mixed policy averages below 4 KV bits and has mean KL and mean NLL delta no more than 10 percent worse than uniform 4-bit on both tested models, while outperforming random-head controls.
- Stop condition: Stop if no mixed policy below 4 average bits beats uniform 3-bit or approaches uniform 4-bit within 10 percent on both KL and NLL delta.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-head-kv-quantization-for-long-context-b6caa74d2c5b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
