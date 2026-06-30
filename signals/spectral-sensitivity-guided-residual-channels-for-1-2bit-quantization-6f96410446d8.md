# Spectral-Sensitivity-Guided Residual Channels for 1-2bit Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `spectral-sensitivity-guided-residual-channels-for-1-2bit-quantization-6f96410446d8`
Run ID: `spectral-sensitivity-guided-residual-channels-for-1-2bit-quantization-6f96410446d8-20260520T185531192316+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/32934b6f2703

## What looked useful

A simple static spectral score was not robustly better than magnitude or random residual-channel selection. It beat the inverse-spectral control on average, especially in 1-bit settings, but lost to the best non-spectral control in 20 of 24 nonzero seed/bit/budget cases.

## Boundaries and scale limits

Not validated on transformers, language modeling, GPT-2-small-class models, real datasets, activation-gradient or Hessian spectral sensitivity, or low-bit inference kernels. The 2-bit setting was near saturated, leaving little recovery headroom.

## Claim scope

Small synthetic 8x8 image-classification MLP with 1-bit and 2-bit weight quantization, restoring selected hidden channels to full precision. The tested selector is a static first-layer FFT high-frequency energy ratio multiplied by outgoing channel norm.

## Why it stopped

Bounded local evidence does not support the simple spectral-score residual-channel selector as practically superior; this is a proxy-scale mixed/negative result rather than full validation.

## Recommended next action

Stop this run as no-paper useful signal; if continuing, run a bounded deepen test with empirical band-limited loss sensitivity on a small transformer and require clear wins over magnitude and random controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Empirical Spectral Loss-Sensitivity Residual Channels for Low-Bit Transformer Quantization
- Success threshold: At 1-bit or 2-bit weights, empirical spectral selection recovers at least 10% more of the quantization loss gap than the best non-spectral control at the same residual-channel budget across at least 3 seeds.
- Stop condition: Stop if empirical spectral selection does not beat the best non-spectral control on mean recovery fraction in the first bounded transformer-scale experiment.

## Evidence references

- Artifact root: `<local-path>/projects/spectral-sensitivity-guided-residual-channels-for-1-2bit-quantization-6f96410446d8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
