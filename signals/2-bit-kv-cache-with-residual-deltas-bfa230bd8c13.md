# 2-Bit KV Cache with Residual Deltas

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `2-bit-kv-cache-with-residual-deltas-bfa230bd8c13`
Run ID: `2-bit-kv-cache-with-residual-deltas-bfa230bd8c13-20260529T220823257804+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/731bd7b356aa

## What looked useful

Sparse residual deltas monotonically improved plain 2-bit KV quantization, but not nearly enough: at sequence length 2048 and the same estimated 4.5 bits/value as 4-bit, 2-bit plus 12.5% residuals had about 0.105 mean relative output MSE versus 0.00218 for 4-bit, and attention top-1 match of 0.344 versus 0.801. Even 50% residuals used 9.75 bits/value and still had 0.0255 relative output MSE.

## Boundaries and scale limits

No pretrained language model perplexity, next-token KL, real prompt distribution, packed low-bit kernel, end-to-end decode latency, or serving memory-pressure validation was run. Results cover sequence lengths 128, 512, and 2048 with up to 8 heads, 64 head dimension, and 5 synthetic trials.

## Claim scope

A synthetic transformer-shaped attention probe with AR(1)-correlated K/V tensors, mild outliers, fp16 reference attention, per-vector uniform quantization, and sparse top-error int8 residual deltas does not support 2-bit KV cache plus residual deltas as a practical memory-quality middle point versus a simple 4-bit KV baseline.

## Why it stopped

Proxy synthetic attention evidence provides an early falsification of the tested scheme rather than full validation: residuals help plain 2-bit, but the memory-quality tradeoff is far worse than 4-bit at equal or even higher estimated bits/value.

## Recommended next action

Stop this simple sparse top-error residual-delta design as a no-paper useful negative; only revisit if using a materially different residual selection or learned quantization method and test it directly inside a pretrained LM decode loop.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-residual-deltas-bfa230bd8c13`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
