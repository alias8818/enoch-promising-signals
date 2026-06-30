# Real-Activation Per-Head KV Quantization Replay

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-activation-per-head-kv-quantization-replay-27df4ab333`
Run ID: `real-activation-per-head-kv-quantization-replay-27df4ab333-20260604T090916889131+0000`

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

- Parent run decision: Per-Head KV Quantization with Block-wise Scaling: enoch://control-plane/projects/per-head-kv-quantization-with-block-wise-scaling-197ab8d7f399/runs/per-head-kv-quantization-with-block-wise-scaling-197ab8d7f399-20260604T064304307265+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/368bec57e31c

## What looked useful

Per-head scaling produced 42.6-65.1% aggregate relative-MSE reductions at 3-4 bits and won all layers; 2-bit results were mixed with weak aggregate gains and layer regressions.

## Boundaries and scale limits

One small GPT-2-family model, 16 packed 128-token prompt chunks, replay-only attention-output metric, no end-to-end quantized-cache generation, no perplexity/logit propagation, no latency or bandwidth measurement, and no larger/GQA/MQA models.

## Claim scope

On a Tier 1 direct replay test using distilgpt2 real Wikitext-2 activations, per-head KV quantization reduces projected attention replay relative MSE versus a single per-tensor scale at 3 and 4 bits, but not reliably at 2 bits.

## Why it stopped

Tier 1 direct replay produced useful mechanism evidence but not direct end-to-end or publication-grade validation.

## Recommended next action

Run a bounded deepen test with end-to-end quantized KV-cache generation on a GPT-2-small-class model, measuring perplexity/logit drift and replay error for 3-bit and 4-bit per-head scaling against per-tensor and fp16 cache baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end per-head KV cache generation validation at 3-4 bits
- Success threshold: At 3 or 4 bits, per-head KV cache quantization reduces mean logit KL or cross-entropy drift versus per-tensor quantization by at least 20% without worse replay error, across all tested prompt lengths.
- Stop condition: Stop if per-head cache propagation fails to improve both replay error and at least one end-to-end quality metric versus per-tensor at 3 and 4 bits, or if implementation overhead prevents a valid controlled comparison.

## Evidence references

- Artifact root: `<local-path>/projects/real-activation-per-head-kv-quantization-replay-27df4ab333`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
