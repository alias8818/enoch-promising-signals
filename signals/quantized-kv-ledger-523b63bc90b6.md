# Quantized KV Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-kv-ledger-523b63bc90b6`
Run ID: `quantized-kv-ledger-523b63bc90b6-20260526T111731140094+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b47c4530c038

## What looked useful

The ledger reduced 4-bit RMSE by 8.2% to 30.6% and 3-bit RMSE by 5.9% to 31.8% versus the best non-ledger baseline across tested synthetic regimes, but 2-bit remained too degraded and one stationary 2-bit case was worse than the best baseline.

## Boundaries and scale limits

Evidence is limited to synthetic KV tensors, 8 heads, 64 head dimension, 128 queries, six seeds, dequantized attention math, and no real transformer perplexity, task quality, fused kernel, or serving latency validation.

## Claim scope

In synthetic exact-attention KV-cache quantize-dequantize tests at sequence length 4096, a per-token/per-head fp16 scale ledger improves 3-bit and 4-bit attention-output fidelity versus global per-head and blockwise per-head scales, with a small compression penalty.

## Why it stopped

This run produced bounded proxy evidence only: synthetic attention supports the 3/4-bit ledger mechanism, but it is not publication-grade direct model or serving evidence, and 2-bit behavior is weak.

## Recommended next action

Run a bounded real-model KV-cache evaluation on a GPT-2-small-class model with 4-bit ledger versus blockwise scales, measuring perplexity or next-token KL plus actual KV bytes and latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model 4-bit KV ledger validation
- Success threshold: 4-bit ledger improves perplexity delta or next-token KL by at least 10% relative versus blockwise metadata while adding no more than 10% KV bytes and no more than 10% decode latency.
- Stop condition: Stop if 4-bit ledger does not beat blockwise metadata on real-model perplexity/KL, or if latency/byte overhead exceeds 10% without a compensating quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-kv-ledger-523b63bc90b6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
