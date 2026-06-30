# Activation-Aware Residual Channel Selection for Packed INT4 GPT-2 Inference on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-aware-residual-channel-selection-for-packed-int-72a1e94925`
Run ID: `activation-aware-residual-channel-selection-for-packed-int-72a1e94925-20260608T232032278007+0000`

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

- Parent run decision: Extreme INT4 Quantization with Residual Channel Preservation on GB10: enoch://control-plane/projects/extreme-int4-quantization-with-residual-channel-preservation-on-gb10-b7b3f08dea9b/runs/extreme-int4-quantization-with-residual-channel-preservation-on-gb10-b7b3f08dea9b-20260608T205306297139+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/91e7721ea839

## What looked useful

Activation-aware residual channels consistently beat random and reduced INT4 reconstruction MSE by 18.8% to 70.3% versus no residual at 5% residual channels, but the best mean improvement over deterministic non-aware controls was only 1.375%, below the 10% Tier-1 threshold.

## Boundaries and scale limits

Layer-level GPT-2 small test only; short local prompts; no full-model perplexity, no autoregressive serving benchmark, and no fused packed INT4 CUDA kernel.

## Claim scope

On 8 early GPT-2 projection layers with short held-out prompts, activation-aware residual input-channel selection for packed-storage INT4 weights beat random residual selection and reduced no-residual reconstruction error, but did not materially outperform activation-only or weight-error-only controls.

## Why it stopped

Tier-1 direct layer-level GPT-2 test missed the explicit 10% improvement threshold over the best non-aware control; this is a bounded threshold miss rather than full-scale validation.

## Recommended next action

Stop this run as no-paper useful signal; if continuing, run a bounded full-block GPT-2 perplexity test with activation-aware versus activation-only and weight-error-only residual channels at equal packed INT4 budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Full-block GPT-2 perplexity test for residual INT4 channel selectors
- Success threshold: At the same residual budget, activation-aware selection improves end-to-end perplexity or NLL by at least 3% versus the best deterministic non-aware selector and does not add more than 10% latency versus the residual-control path.
- Stop condition: Stop if activation-aware selection is within 1% of activation-only or weight-error-only on end-to-end quality, or if residual correction overhead dominates any quality benefit.

## Evidence references

- Artifact root: `<local-path>/projects/activation-aware-residual-channel-selection-for-packed-int-72a1e94925`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
