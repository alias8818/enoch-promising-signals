# INT8 quantized training with per-channel smoothing

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `int8-quantized-training-with-per-channel-smoothing-4993d2442ea2`
Run ID: `int8-quantized-training-with-per-channel-smoothing-4993d2442ea2-20260609T081940735847+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/eca178203750

## What looked useful

Balanced inputs had no INT8 accuracy gap. With 1e-1 to 1e1 channel scales, unsmoothed INT8 averaged 0.6089 final validation accuracy versus FP32 0.6437, while smoothed INT8 alpha 0.75 averaged 0.6436. With 1e-2 to 1e2 channel scales, unsmoothed INT8 averaged 0.3200 versus FP32 0.4012, while smoothed INT8 alpha 0.75 averaged 0.4046. First-layer activation quantization MSE under severe imbalance dropped from 0.324888 to 3.76e-05 after smoothing.

## Boundaries and scale limits

Evidence is limited to synthetic teacher data, 64-dimensional inputs, 2x128 MLPs, 3 seeds per severity setting, PyTorch fake quantization with STE, and no real INT8 optimizer/kernel throughput measurement. It does not validate GPT-2-small-class or larger transformer training.

## Claim scope

On a synthetic small-MLP classification task with deliberately scale-imbalanced input channels, SmoothQuant-style per-input-channel smoothing recovers the validation-accuracy loss of INT8 fake-quantized training relative to an unsmoothed INT8 fake-quantized control.

## Why it stopped

No-paper closure: this run provides a reproducible synthetic mechanism signal, but it is not direct full validation of INT8 quantized transformer training or real low-precision kernel performance.

## Recommended next action

Run a bounded transformer follow-up on a real language-modeling task with FP32/BF16, unsmoothed INT8 fake-quantized, and smoothed INT8 fake-quantized controls before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded transformer validation of INT8 fake-quantized training with per-channel smoothing
- Success threshold: Smoothed INT8 closes at least 50% of the validation loss/perplexity gap between unsmoothed INT8 and FP32/BF16 without unstable training in the bounded transformer run.
- Stop condition: Stop if unsmoothed INT8 has no measurable quality gap, smoothing fails to improve quantization diagnostics, or smoothed INT8 recovers less than 25% of the observed quality gap across repeated runs.

## Evidence references

- Artifact root: `<local-path>/projects/int8-quantized-training-with-per-channel-smoothing-4993d2442ea2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
