# Exact Anchor Guided 2-bit KV Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-guided-2-bit-kv-quantization-a64443fe946d`
Run ID: `exact-anchor-guided-2-bit-kv-quantization-a64443fe946d-20260531T190731957252+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1c64bc485425

## What looked useful

At 3.125% exact anchors, oracle-attention anchors improved relative output MSE by 13.01% on iid_normal and 9.00% on attention_sink versus all-2bit, while value-norm anchors improved value_outlier MSE by 42.50%. Random exact anchors at the same payload improved only 2.23% to 3.04% in the first two regimes and 2.55% in value_outlier.

## Boundaries and scale limits

No real transformer model, real text KV traces, perplexity/logit evaluation, packed 2-bit kernels, online selector, latency measurement, or metadata-overhead accounting was tested. Oracle-attention anchors use reference attention weights and are an upper bound rather than a deployable method.

## Claim scope

Synthetic scaled dot-product attention probes with sequence length 1024, dimension 64, 64 queries, and 12 seeds show that preserving 1.5625% to 6.25% of KV token positions exactly can reduce attention-output relative MSE versus all-token 2-bit per-token affine quantization when the selected anchors capture attention mass or value outliers.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but does not validate a deployable exact-anchor 2-bit KV quantization method on real models.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replay the same anchor-selector grid on actual KV caches from a small pretrained transformer and measure logit or perplexity error.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real KV Trace Validation for Exact-Anchor 2-bit Quantization
- Success threshold: At 3.125% exact anchors, the best deployable selector reduces next-token logit MSE or perplexity delta by at least 10% relative to all-token 2-bit quantization and beats random exact anchors on at least 80% of evaluated prompts.
- Stop condition: Stop if deployable selectors fail to beat random exact anchors by at least 5% relative error reduction on a 100-prompt small-model trace set, or if metadata overhead pushes effective payload above 3 bits/value.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-guided-2-bit-kv-quantization-a64443fe946d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
