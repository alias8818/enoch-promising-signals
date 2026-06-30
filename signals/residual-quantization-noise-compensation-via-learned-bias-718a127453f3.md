# Residual Quantization-Noise Compensation via Learned Bias

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-quantization-noise-compensation-via-learned-bias-718a127453f3`
Run ID: `residual-quantization-noise-compensation-via-learned-bias-718a127453f3-20260609T230623074004+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d8f6cd0106d5

## What looked useful

Per-channel bias reduced direct linear residual MSE when input activations had nonzero stable mean, with 26.51% mean improvement at 2-bit and 28.61% at 3-bit across three confirmation seeds. In the frozen MLP proxy, learned biases reduced held-out KL-to-FP by 98.01% at 2-bit and 95.07% at 3-bit versus no compensation, while random-bias controls did not show the same reduction. Accuracy delta was 0.0 because the proxy task was too easy.

## Boundaries and scale limits

No real transformer, language-model perplexity, public text calibration corpus, serving benchmark, or large-model validation was run. The synthetic MLP task was accuracy-saturated after quantization, so downstream recovery was not demonstrated.

## Claim scope

On synthetic linear maps and frozen synthetic MLP classifiers, learned per-layer additive bias vectors can compensate stable residual quantization-noise components and substantially reduce held-out KL-to-full-precision logits under 2-bit and 3-bit per-row symmetric quantization.

## Why it stopped

Closed as a synthetic/proxy useful signal rather than full validation; learned bias improves residual/logit-matching metrics but did not demonstrate downstream task recovery or real transformer behavior.

## Recommended next action

Run a bounded deepen follow-up on a GPT-2-small-class public transformer with real text calibration, reporting validation perplexity and logit KL against no-compensation, random-bias, and standard quantization baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Quantization Bias on GPT-2-Small Text Perplexity
- Success threshold: Learned bias must reduce validation perplexity degradation from quantization by at least 10% relative to no-compensation and beat random-bias controls across at least three seeds or calibration splits.
- Stop condition: Stop if learned bias fails to improve held-out perplexity or logit KL over no-compensation and random-bias controls on the small public transformer.

## Evidence references

- Artifact root: `<local-path>/projects/residual-quantization-noise-compensation-via-learned-bias-718a127453f3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
