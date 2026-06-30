# Per-Head 2-Bit KV on GPT-2-Small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `per-head-2-bit-kv-on-gpt-2-small-c61af9b8a3df`
Run ID: `per-head-2-bit-kv-on-gpt-2-small-c61af9b8a3df-20260528T132601054256+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/093bcd84ab6e

## What looked useful

Per-head 2-bit KV raised WikiText-2 PPL from 21.58 to 32786.99 (+7.326 NLL/token), while per-head 4-bit was much less damaged at PPL 56.91. Values-only 2-bit caused most of the degradation, indicating the value cache is the primary fragility for this naive scheme.

## Boundaries and scale limits

Small direct probe only: GPT-2-small, fp16 inference, 256 scored tokens per confirmation, simple min/max affine quantization, no packed 2-bit kernel, no calibration, no retraining, no long-context serving benchmark.

## Claim scope

Naive affine per-head 2-bit quantize-dequantize of GPT-2-small autoregressive KV cache is not numerically viable for a pretrained model on 256-token builtin-text and WikiText-2 probes.

## Why it stopped

Direct small-scale early falsification: the tested 2-bit per-head KV proxy catastrophically degrades GPT-2-small next-token NLL/PPL, so it is not worth paper development without a different quantization mechanism.

## Recommended next action

Stop this naive per-head 2-bit KV path; a bounded follow-up should test mixed-bit or residual-window KV where values receive at least 4 bits and only older keys are considered for 2-bit storage.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Mixed-bit GPT-2-small KV cache with 2-bit keys and protected values
- Success threshold: On WikiText-2, mixed-bit or residual-window KV should keep PPL ratio <= 1.25 versus fp16 while achieving at least 2.5x estimated KV-cache compression.
- Stop condition: Stop if all mixed-bit/residual variants exceed 1.5x fp16 PPL on a 1024-token direct autoregressive evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-2-bit-kv-on-gpt-2-small-c61af9b8a3df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
