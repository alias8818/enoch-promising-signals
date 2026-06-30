# Activation-Variance Residual Channels at INT1

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `activation-variance-residual-channels-at-int1-a7612ad4ace3`
Run ID: `activation-variance-residual-channels-at-int1-a7612ad4ace3-20260523T184743756538+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e93004b3c107

## What looked useful

Calibration channel variance was highly predictive of held-out INT1 quantization error: correlation 0.9935 on distilgpt2 and 0.9994 on GPT-2. With 5% FP residual channels, variance selection reduced activation relative MSE versus random by 96.0% on distilgpt2 and 98.7% on GPT-2, and reduced logit relative MSE versus random by 98.9% and 99.7%, respectively.

## Boundaries and scale limits

Only final residual-stream activations were quantized; no in-block injection, perplexity evaluation, packed INT1 kernel, latency/memory-bandwidth measurement, training adaptation, larger corpus, or 7B-class robustness test was run. Evaluation used 127 calibration tokens and 119 held-out tokens per model.

## Claim scope

On held-out short text for pretrained distilgpt2 and GPT-2 small final residual-stream activations, calibration-variance-selected FP residual channels at 1-20% channel budgets sharply reduce signed INT1 activation and LM-head logit MSE versus random residual-channel selection, with variance selection close to an eval-set oracle for activation MSE.

## Why it stopped

No-paper closure: evidence supports the local activation-error mechanism, but it is still a small activation/logit proxy rather than full model-quality or systems validation.

## Recommended next action

Stop this worker run as no-paper useful signal; next concrete test is an end-to-end GPT-2 perplexity evaluation with residual-channel INT1 activations injected at every block and matched random/mean-abs/oracle controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-End GPT-2 Perplexity Test for INT1 Variance Residual Channels
- Success threshold: Variance-selected residual channels should cut the perplexity degradation from plain INT1 by at least 50% and outperform random residual-channel selection by at least 25% relative degradation at 5% and 10% FP residual-channel budgets.
- Stop condition: Stop as negative if variance selection does not beat random selection on perplexity degradation at both 5% and 10% budgets or if layerwise injection erases the activation-error advantage.

## Evidence references

- Artifact root: `<local-path>/projects/activation-variance-residual-channels-at-int1-a7612ad4ace3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
