# Residual Channel Preservation in INT2 Quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-channel-preservation-in-int2-quantization-b5e66ee85e13`
Run ID: `residual-channel-preservation-in-int2-quantization-b5e66ee85e13-20260611T115328298341+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/749fa37361d0

## What looked useful

Top-activation preservation improved loss over random preservation by about 5.6 to 7.6 nats at 1-20% preserved channels, but absolute quality remained poor: even 20% preservation had loss 12.736 versus 4.501 full precision.

## Boundaries and scale limits

Single pretrained distilgpt2 model, 64 calibration chunks, 128 evaluation chunks, sequence length 128, simulated dequantized INT2 weights rather than packed kernels, no large-model, long-context, task-accuracy, or production-throughput validation.

## Claim scope

On a bounded distilgpt2/WikiText-2 probe with simulated affine INT2 weight-only quantization of GPT projection layers, preserving high-activation residual/input channels consistently reduced evaluation loss versus preserving the same fraction of random channels.

## Why it stopped

No-paper useful signal: the mechanism is supported locally, but residual channel preservation alone did not make INT2 quantization practically usable in the bounded direct test.

## Recommended next action

Run a medium confirmation on GPT-2-small-class with groupwise INT2 baselines and AWQ/GPTQ-style controls; stop paper writing unless activation-selected preservation reaches an explicit perplexity degradation threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium GPT-2 INT2 Residual Channel Preservation With Realistic Quantization Baselines
- Success threshold: At a preserved-channel budget no greater than 10%, activation-selected preservation should beat the best random control and the strongest implemented INT2 baseline while keeping perplexity within 25% of full precision on the bounded evaluation.
- Stop condition: Stop if groupwise INT2 plus activation-selected preservation still has more than 2x full-precision perplexity or fails to beat an established low-bit baseline at matched budget.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-preservation-in-int2-quantization-b5e66ee85e13`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
