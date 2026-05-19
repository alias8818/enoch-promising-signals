# Activation-aware learned residual channels for 1-bit recovery

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `activation-aware-learned-residual-channels-for-1-bit-recov-70ce4e2acc`
Run ID: `activation-aware-learned-residual-channels-for-1-bit-recov-70ce4e2acc-20260519T030004730707+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/eef056bc5fd5

## What looked useful

Learned residual adapters recover substantial 1-bit quantization error, but the activation-aware gate did not add value under parameter matching; a static parameter-matched residual adapter reduced validation NMSE by 89.66% versus raw 1-bit, while the activation-aware adapter reduced it by 72.38% and had about 2.67x higher NMSE than the static parameter-matched control.

## Boundaries and scale limits

Synthetic frozen linear target only; no transformer training, downstream perplexity, real-token activations, latency, or full model memory-efficiency validation.

## Claim scope

In a controlled target-layer recovery test with row-wise scaled 1-bit quantization, group-structured high-activation inputs, and 5 random seeds, activation-aware learned residual channels did not outperform a parameter-matched static residual adapter.

## Why it stopped

Tier 1 direct small test falsified the activation-aware success threshold rather than providing full validation: activation-aware NMSE was worse than the parameter-matched static residual on both primary and high-activation metrics.

## Recommended next action

Stop this activation-aware claim as no-paper evidence; any future work should first beat the static parameter-matched residual baseline on a bounded transformer/GPT-2-small-class recovery or perplexity test.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Static parameter-matched residual adapters for 1-bit recovery
- Success threshold: Static residual adapter improves held-out recovery error by at least 20% over raw 1-bit and is not worse than activation-aware residual by more than 3% on validation perplexity while using no more parameters.
- Stop condition: Stop if static residual fails to beat raw 1-bit by 10% on held-out recovery or if activation-aware residual beats static by at least 10% under matched parameters, which would refocus the mechanism question.

## Evidence references

- Artifact root: `<local-path>/projects/activation-aware-learned-residual-channels-for-1-bit-recov-70ce4e2acc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
