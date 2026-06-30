# Principled Residual Channels for KV-cache 2-bit

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `principled-residual-channels-for-kv-cache-2-bit-af6acae252ca`
Run ID: `principled-residual-channels-for-kv-cache-2-bit-af6acae252ca-20260526T070320984174+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/c5410934474a

## What looked useful

At seq_len 256, preserving the top 6.25% mean-absolute K/V channels in high precision reduced attention-output relative MSE from 0.5678 to 0.1527, while random residual channels at the same 2.875 effective bits/value averaged 0.5155. Preserving 12.5% reduced attention-output relative MSE to 0.1249 versus random residual mean 0.4607.

## Boundaries and scale limits

Tested only GPT-2-small activations with Wikitext-2 validation text, sequence lengths 128 and 256, calibration/eval splits up to 32/96 samples, per-token min/max 2-bit quantization, and offline attention-output reconstruction. No end-to-end KV-cache integration, perplexity, generation quality, long-context serving, larger model, or throughput validation was run.

## Claim scope

Activation-level GPT-2-small evidence shows that mean-absolute calibrated residual K/V head dimensions substantially reduce 2-bit KV tensor reconstruction error and causal attention-output relative MSE versus all-2-bit and random residual-channel controls at the same effective bit budget.

## Why it stopped

Closed as no-paper useful signal: the mechanism is supported by direct activation and attention-output proxy evidence, but paper-grade claims require end-to-end KV-cache perplexity and serving metrics.

## Recommended next action

Run a bounded end-to-end KV-cache decode/perplexity follow-up using the calibrated residual-channel quantizer, with fp16, all-2-bit, and random-residual controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end calibrated residual-channel KV-cache quantization
- Success threshold: At equal effective bits/value, calibrated residual channels reduce perplexity degradation by at least 50% versus random residual channels while retaining most of the all-2-bit memory reduction and without a decode throughput regression larger than 10% versus the random-residual implementation.
- Stop condition: Stop if calibrated residual channels fail to improve perplexity degradation over random residual channels on two independent evaluation slices, or if the residual-channel bookkeeping eliminates the practical memory/throughput benefit.

## Evidence references

- Artifact root: `<local-path>/projects/principled-residual-channels-for-kv-cache-2-bit-af6acae252ca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
