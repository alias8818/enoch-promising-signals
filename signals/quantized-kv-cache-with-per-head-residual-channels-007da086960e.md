# Quantized KV Cache with Per-Head Residual Channels

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantized-kv-cache-with-per-head-residual-channels-007da086960e`
Run ID: `quantized-kv-cache-with-per-head-residual-channels-007da086960e-20260523T190843160160+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/00855c71463b

## What looked useful

For int4 KV quantization on GPT-2, 4 residual channels per head reduced mean attention-output relative MSE from 0.05169 to 0.03862, a 0.747 error ratio, at a 1.176 byte ratio versus the int4 baseline. Random residual channels at the same count gave only a 0.914 error ratio. The int4 ablation improved all 12 layers and scaled monotonically: 1, 2, 4, and 8 residual channels gave selected error ratios of 0.903, 0.845, 0.747, and 0.591.

## Boundaries and scale limits

Tested only layer-local recomputation on cached gpt2 with 8x256-token chunks and one synthetic local text stream. No end-to-end generation, perplexity, held-out calibration split, long-context decode, fused-kernel latency, or non-GPT-2 architecture validation.

## Claim scope

On cached GPT-2 activations, variance-selected per-head fp16 residual channels reduce layer-local attention-output relative MSE versus ordinary per-token int4 KV quantization, with monotonic gains from 1 to 8 residual channels per head.

## Why it stopped

No-paper closure: this run produced a useful mechanism signal, but only layer-local attention-output distortion was directly tested; end-to-end quality and serving performance remain unvalidated.

## Recommended next action

Run a bounded held-out end-to-end decode/perplexity experiment that calibrates residual-channel masks on one text split, evaluates on another, and reinjects the quantized KV cache through generation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out end-to-end GPT-2 KV residual decode test
- Success threshold: At 4 residual channels per head, achieve at least 20% lower held-out logit KL or perplexity degradation than int4 baseline while keeping estimated KV-cache bytes within 1.25x of the int4 baseline, and outperform random residual channels.
- Stop condition: Stop if held-out end-to-end quality gains are under 10% versus int4 baseline, if random residual channels match selected channels, or if cache overhead exceeds 1.25x at the target residual count.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-kv-cache-with-per-head-residual-channels-007da086960e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
