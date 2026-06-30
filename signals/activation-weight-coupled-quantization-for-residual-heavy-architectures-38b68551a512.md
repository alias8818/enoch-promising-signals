# Activation-Weight Coupled Quantization for Residual-Heavy Architectures

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-weight-coupled-quantization-for-residual-heavy-architectures-38b68551a512`
Run ID: `activation-weight-coupled-quantization-for-residual-heavy-architectures-38b68551a512-20260607T094345433526+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/be9b9f64c67c

## What looked useful

Activation geometry was consistently useful for int4 post-training weight quantization versus RTN, but the tested Gram-form objective was exactly equivalent to brute activation-output scale search and therefore did not establish a distinct novel method.

## Boundaries and scale limits

Synthetic residual MLP only; no transformer language modeling, no activation quantization, no deployment kernels, no large model validation, and short local runs only.

## Claim scope

In a small synthetic residual-heavy MLP regression probe, activation-weight coupled per-channel int4 clipping reduced fp32-to-quantized output perturbation versus RTN by 18.1%-23.5% across residual scales 0.1, 0.5, and 1.0.

## Why it stopped

Proxy evidence supports the mechanism but not a paper-ready or clearly novel method; the coupled objective tested here is algebraically equivalent to activation-output error search for linear layers.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded transformer PTQ follow-up that compares RTN, activation-aware search, and any non-equivalent coupled objective on GPT-2-small-class perplexity and output-delta metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer PTQ Test for Non-Equivalent Activation-Weight Coupling
- Success threshold: The coupled variant must improve perplexity degradation by at least 10% versus activation-aware clipping/search and reduce output perturbation in at least 75% of measured residual blocks without increasing average error elsewhere.
- Stop condition: Stop if the coupled variant is equivalent to activation-aware output-error minimization, fails to beat activation-aware search on perplexity, or only improves synthetic/output-delta metrics while worsening transformer validation loss.

## Evidence references

- Artifact root: `<local-path>/projects/activation-weight-coupled-quantization-for-residual-heavy-architectures-38b68551a512`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
