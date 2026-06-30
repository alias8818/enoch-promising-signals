# Sensitivity-aware residual channels for INT4 MLP blocks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sensitivity-aware-residual-channels-for-int4-mlp-blocks-a09ec09e492e`
Run ID: `sensitivity-aware-residual-channels-for-int4-mlp-blocks-a09ec09e492e-20260629T083317034180+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/85c96a57ff49

## What looked useful

A small reproducible NumPy probe supports the residual-channel mechanism for INT4 MLP reconstruction. The signal is useful for prioritizing a real-checkpoint follow-up, but not enough for a paper claim.

## Boundaries and scale limits

No pretrained LLM checkpoints, token perplexity, downstream tasks, kernel latency, memory bandwidth, or production quantization baselines were tested. The strongest non-random baseline, activation_x_w2norm, was close to sensitivity; sensitivity beat it in 69/96 paired comparisons with only -0.000131 mean relative-MSE delta.

## Claim scope

In synthetic two-layer GELU MLP blocks with row-wise symmetric INT4 quantized weights, replacing 1-8% of hidden-channel contributions with full-precision residual contributions reduces output relative MSE versus all-INT4, random residual channels, and output-weight-norm-only channel selection. Sensitivity selection was best in 12/12 distribution-budget aggregates and beat random/w2_norm in 96/96 paired comparisons.

## Why it stopped

Proxy synthetic evidence is useful but insufficient for paper-positive closure; the run stops after bounded CPU evidence rather than claiming full validation.

## Recommended next action

Run the same residual-channel selector on pretrained transformer MLP layers and measure perplexity or held-out loss against AWQ/GPTQ-style baselines before considering a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained transformer MLP residual-channel INT4 evaluation
- Success threshold: Sensitivity residual channels at 1-4% budget must improve held-out loss or perplexity versus all-INT4 and beat activation_x_w2norm by a practically meaningful margin on most tested layers without unacceptable storage/latency overhead.
- Stop condition: Stop if sensitivity fails to beat activation_x_w2norm on real-checkpoint layer error or end-to-end loss, or if residual storage/latency overhead dominates the recovered accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/sensitivity-aware-residual-channels-for-int4-mlp-blocks-a09ec09e492e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
