# Principled Residual Channels for 2-bit Weight Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `principled-residual-channels-for-2-bit-weight-quantization-5cf1d5018d3c`
Run ID: `principled-residual-channels-for-2-bit-weight-quantization-5cf1d5018d3c-20260527T033718543938+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/06b896041af3

## What looked useful

Activation-weighted residual-channel selection is a plausible mechanism for recovering part of the quality lost to 2-bit weight quantization, but this run only supports a bounded synthetic signal and shows mixed behavior at tiny budgets.

## Boundaries and scale limits

No pretrained transformer, language-model perplexity, real corpus calibration, hardware latency, or large-model memory/throughput evidence was produced. At 2% and 4% budgets the simpler quant-error selector was competitive or better on validation loss.

## Claim scope

In a five-seed synthetic trained-MLP probe, restoring residual input channels selected by diagonal activation-weighted quantization error improved 2-bit validation loss and direct layer-output MSE at 8% and 16% residual-channel budgets versus random, weight-norm, activation-variance, and usually quant-error heuristics.

## Why it stopped

Synthetic/proxy evidence supports the mechanism at moderate residual budgets but is mixed at low budgets and lacks direct transformer/perplexity validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should evaluate the same selectors on a small pretrained transformer with real calibration activations and validation perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-channel selection on a small pretrained transformer
- Success threshold: At 8% or lower residual-channel budget, activation-weighted selection should recover at least 25% of the plain-2-bit perplexity gap to the float model and beat the strongest non-random baseline by at least 5% relative gap recovery.
- Stop condition: Stop as negative if the activation-weighted selector fails to beat quant-error-only selection on both perplexity gap recovery and direct layer-output MSE at all tested budgets.

## Evidence references

- Artifact root: `<local-path>/projects/principled-residual-channels-for-2-bit-weight-quantization-5cf1d5018d3c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
