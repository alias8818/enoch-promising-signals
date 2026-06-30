# Activation-Aware INT8 Training for GPT-2-Small on 10GB VRAM

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `activation-aware-int8-training-for-gpt-2-small-on-10gb-vram-e602faaf1951`
Run ID: `activation-aware-int8-training-for-gpt-2-small-on-10gb-vram-e602faaf1951-20260609T011625839706+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6efc1435e55d

## What looked useful

The run provides a bounded negative signal: PyTorch int8 tensors cannot require gradients, CUDA int8 addmm for Char is unavailable, quantized Linear fails on this architecture, BF16 GPT-2-small already fits the bounded run at 2.37 GiB peak allocation, fake INT8 adds roughly 55-59% step-time overhead without memory savings, and the tested activation-aware scaling increases weighted quantization MSE in all 48 Conv1D modules.

## Boundaries and scale limits

Synthetic data only; 10 steps per training mode; sequence length 64 and batch size 1; fake quantization rather than true memory-saving int8 training; no real corpus validation or pretrained checkpoint quality measurement.

## Claim scope

On this GB10/PyTorch 2.12 CUDA stack, straightforward trainable int8 GPT-2-small training is not supported; fake-int8 GPT-2-small probes do not reduce memory versus BF16, slow the run, and the tested activation-aware input-channel scaling rule worsens activation-weighted quantization error on synthetic GPT-2-small activations.

## Why it stopped

Proxy/early falsification: the local stack lacks true trainable int8 support, fake quantization does not provide the claimed memory benefit, and the tested activation-aware mechanism performed worse than naive quantization on the direct diagnostic.

## Recommended next action

Stop this path as a proxy/early falsification; a next bounded investigation should replace the scaling rule with a proven activation-smoothing or rotation-based quantizer and test it on a pretrained GPT-2-small checkpoint before considering any larger run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2-small activation smoothing for weighted INT8 quantization error
- Success threshold: Reduce activation-weighted quantization MSE in at least 75% of Conv1D modules and keep validation loss degradation under 5% with peak allocation no higher than the BF16 baseline and mean step time no more than 20% slower.
- Stop condition: Stop if no activation-aware variant lowers weighted MSE in at least half of Conv1D modules or if fake-quant validation loss degrades by more than 10% versus BF16.

## Evidence references

- Artifact root: `<local-path>/projects/activation-aware-int8-training-for-gpt-2-small-on-10gb-vram-e602faaf1951`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
