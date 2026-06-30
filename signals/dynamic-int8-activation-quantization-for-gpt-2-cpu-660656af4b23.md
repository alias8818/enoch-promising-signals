# Dynamic INT8 Activation Quantization for GPT-2 CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-int8-activation-quantization-for-gpt-2-cpu-660656af4b23`
Run ID: `dynamic-int8-activation-quantization-for-gpt-2-cpu-660656af4b23-20260523T235613139146+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12311a2acc01

## What looked useful

Activation byte accounting is favorable, but a hook-based dynamic INT8 activation QDQ path is not a practical GPT-2 CPU speedup by itself. The mechanism needs fused/runtime support and broader quality checks before it can support a positive claim.

## Boundaries and scale limits

Single CPU worker, batch size 1, sequence length 128, one fixed prompt batch, forward-pass benchmark only; no fused INT8 kernels, no KV-cache generation benchmark, no broad corpus quality evaluation.

## Claim scope

For cached GPT-2-small CPU forward passes at sequence length 128, naive per-token INT8 activation quantize/dequantize between transformer blocks reduces theoretical inter-block activation bytes by about 3.98x but does not produce a robust latency improvement and causes a measurable cross-entropy/logit perturbation on the tested prompt batch.

## Why it stopped

Proxy/early falsification of the practical naive implementation: direct GPT-2-small CPU evidence showed no robust latency win despite theoretical activation-byte compression, and broader/fused evidence would be required to overturn this result.

## Recommended next action

Stop this run as a bounded early negative for naive activation QDQ; only revisit if implementing a fused INT8 activation path that keeps block-boundary activations compressed and benchmarks end-to-end CPU generation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused INT8 Block-Boundary Activation Storage for GPT-2 CPU Generation
- Success threshold: At least 10% median CPU generation latency reduction versus fp32 GPT-2-small with cross-entropy or perplexity degradation below 1% on the evaluation corpus.
- Stop condition: Stop if the fused path cannot exceed a 5% median speedup or if quality degradation exceeds 1% after selective scaling/quantization calibration.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-int8-activation-quantization-for-gpt-2-cpu-660656af4b23`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
