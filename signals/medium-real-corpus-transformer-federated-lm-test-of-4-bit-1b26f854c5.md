# Medium Real-Corpus Transformer Federated LM Test of 4-bit Residual Uplinks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-real-corpus-transformer-federated-lm-test-of-4-bit-1b26f854c5`
Run ID: `medium-real-corpus-transformer-federated-lm-test-of-4-bit-1b26f854c5-20260527T141503467432+0000`

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

- Parent run decision: Quantized Residual Gradients for Home Federated Pretraining: enoch://control-plane/projects/quantized-residual-gradients-for-home-federated-pretraining-5a9f4d73fe71/runs/quantized-residual-gradients-for-home-federated-pretraining-5a9f4d73fe71-20260527T104621287955+0000
- Parent run decision: Real-Corpus Federated LM Test of 4-bit Residual Gradient Uplink Compression: enoch://control-plane/projects/real-corpus-federated-lm-test-of-4-bit-residual-gradient-u-701284dc9e/runs/real-corpus-federated-lm-test-of-4-bit-residual-gradient-u-701284dc9e-20260527T123811539362+0000

## What looked useful

4-bit quantized model-delta uplinks were benign in this small real-corpus Transformer LM regime, but residual feedback was not the active mechanism; no-residual 4-bit performed at least as well across the three fixed seeds.

## Boundaries and scale limits

This was not GPT-2-small-class, not subword tokenized, not multi-node, not privacy/noise aware, and not a large corpus or long-horizon training run. The residual/error-feedback mechanism was not isolated because the no-residual 4-bit ablation matched or slightly beat residual feedback.

## Claim scope

In a local 1.9M-parameter character-level Transformer federated LM simulation on WikiText-2 with 8 clients, 3 fixed seeds, and 60 rounds, 4-bit per-tensor uplinks matched full-precision FedAvg validation loss while reducing modeled uplink bytes by about 8x.

## Why it stopped

Medium direct evidence found useful 8x-compression behavior but did not support the residual-specific mechanism needed for a paper-positive result.

## Recommended next action

Stop paper escalation for residual 4-bit uplinks at this scope; if continuing, run a bounded non-IID or harsher-quantization stress test where residual error can accumulate and must beat the no-residual ablation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-IID Stress Test for Residual 4-bit Federated LM Uplinks
- Success threshold: q4_residual must beat q4_noresidual by at least 0.02 validation loss mean across at least 3 fixed seeds while staying within 0.03 validation loss of fp32 and preserving at least 6x uplink reduction.
- Stop condition: Stop if q4_noresidual remains statistically indistinguishable from or better than q4_residual under the chosen stressor, or if both quantized methods fall more than 0.05 validation loss behind fp32.

## Evidence references

- Artifact root: `<local-path>/projects/medium-real-corpus-transformer-federated-lm-test-of-4-bit-1b26f854c5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
