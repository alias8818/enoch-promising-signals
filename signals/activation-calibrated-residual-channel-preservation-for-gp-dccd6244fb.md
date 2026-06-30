# Activation-calibrated residual channel preservation for GPT-2-small INT4 quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `activation-calibrated-residual-channel-preservation-for-gp-dccd6244fb`
Run ID: `activation-calibrated-residual-channel-preservation-for-gp-dccd6244fb-20260608T114958357854+0000`

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

- Parent run decision: 4-bit INT Quantization with Residual Channel Preservation on GPT-2-small: enoch://control-plane/projects/4-bit-int-quantization-with-residual-channel-preservation-on-gpt-2-small-485d8ad7ddd3/runs/4-bit-int-quantization-with-residual-channel-preservation-on-gpt-2-small-485d8ad7ddd3-20260608T043727392039+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7841a987ac2c

## What looked useful

Activation-calibrated preservation reduced main-setting INT4 delta loss from 0.405138 to 0.201136 at 5.34% preserved weights, outperforming matched random preservation at 0.381305 and weight-magnitude preservation at 0.334392. The same ordering held at approximately 1.13%, 2.68%, and 10.78% preserved weights.

## Boundaries and scale limits

Single GPT-2-small model, WikiText-2 validation windows only, block size 256, 24,480 evaluated tokens per Tier 1 condition, dequantized INT4 simulation rather than packed hardware INT4 kernels, no broad benchmark or multi-corpus robustness.

## Claim scope

On a Tier 1 direct GPT-2-small WikiText-2 validation slice, preserving activation-selected residual-stream channels during simulated Conv1D weight-only INT4 quantization reduces next-token loss damage more than uniform INT4, matched random channel preservation, and matched weight-magnitude channel preservation.

## Why it stopped

Tier 1 direct evidence supports the mechanism but is not robust or hardware-real enough for publication; close this run as no-paper useful signal.

## Recommended next action

Run a bounded medium direct validation on larger WikiText-2/OpenWebText slices with multiple calibration seeds, packed-kernel-aware accounting, and a predeclared threshold that activation-selected preservation must beat random and weight-magnitude controls by at least 25% relative delta-loss reduction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium robustness test for activation-selected GPT-2 INT4 residual channel preservation
- Success threshold: Activation-selected preservation beats both random and weight-magnitude controls by at least 25% relative reduction in INT4 delta loss versus FP at two or more preserved fractions, with no regression versus controls on the additional corpus.
- Stop condition: Stop if activation-selected preservation fails to beat either matched control on the larger primary evaluation slice or if packed-kernel accounting shows the preserved-channel budget removes the practical INT4 benefit.

## Evidence references

- Artifact root: `<local-path>/projects/activation-calibrated-residual-channel-preservation-for-gp-dccd6244fb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
