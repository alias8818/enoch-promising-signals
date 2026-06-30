# Principled Residual Channels for 2-bit Weight Quantization on GPT-2-small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `principled-residual-channels-for-2-bit-weight-quantization-on-gpt-2-small-efd83f860a34`
Run ID: `principled-residual-channels-for-2-bit-weight-quantization-on-gpt-2-small-efd83f860a34-20260524T025551280387+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/156899663d7c

## What looked useful

The direct bounded test falsifies the naive residual-error-energy channel rule: at 1% residual channels it worsened NLL from 9.6863 for plain 2-bit to 10.6649, while random 1% residual channels scored 9.4899 on the same blocks; fraction sweeps also favored random over error-selected channels.

## Boundaries and scale limits

64 non-overlapping 512-token WikiText-2 validation blocks; simulated weight-only quantization in Torch modules; no packed 2-bit kernels, full WikiText test sweep, downstream tasks, activation calibration, GPTQ/AWQ reconstruction, or fine-tuning.

## Claim scope

On GPT-2-small with a simple symmetric per-output-channel 2-bit weight-only quantizer evaluated on 64 WikiText-2 validation blocks, keeping the largest per-channel quantization-residual/error channels in full precision did not improve quality and underperformed random residual channel selection at 0.5%, 1%, 2%, and 5% residual budgets.

## Why it stopped

Proxy-to-medium direct GPT-2-small evidence provides early falsification of the simple weight-residual-energy rule, not a full validation of the broader residual-channel idea.

## Recommended next action

Stop this paper path; a bounded follow-up should test activation-aware residual channel selection against random and plain 2-bit on the same GPT-2-small/WikiText-2 harness before any larger-scale work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware residual channels for GPT-2-small 2-bit quantization
- Success threshold: Activation-aware residual selection improves NLL by at least 0.2 versus the mean random residual baseline at the same residual budget on the fixed evaluation split and is not worse than plain 2-bit.
- Stop condition: Stop if activation-aware selection fails to beat mean random residual NLL at both 1% and 5% budgets or still worsens NLL versus plain 2-bit.

## Evidence references

- Artifact root: `<local-path>/projects/principled-residual-channels-for-2-bit-weight-quantization-on-gpt-2-small-efd83f860a34`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
