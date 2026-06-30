# Composition-aware activation exponent sweep for GPT-2 INT2 layer/split quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `composition-aware-activation-exponent-sweep-for-gpt-2-int2-863306ea59`
Run ID: `composition-aware-activation-exponent-sweep-for-gpt-2-int2-863306ea59-20260523T130502558867+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Robust split-and-layer diagnostic for activation-aware INT2 residual salience on GPT-2: enoch://control-plane/projects/robust-split-and-layer-diagnostic-for-activation-aware-int-82125c2c98/runs/robust-split-and-layer-diagnostic-for-activation-aware-int-82125c2c98-20260523T125449718377+0000
- Parent run decision: Activation-aware INT2 residual salience on GPT-2 linear weights: enoch://control-plane/projects/activation-aware-int2-residual-salience-on-gpt-2-linear-we-85cf4f46d1/runs/activation-aware-int2-residual-salience-on-gpt-2-linear-we-85cf4f46d1-20260523T124002690437+0000

## What looked useful

Greedy composition-aware exponents reduced held-out NLL from 17.1183 global and 17.7335 MSE to 12.9608 in the split-projection INT2 run, and from 12.3887 global and 9.6215 MSE to 9.4965 in the activation-only ablation. However, the primary greedy result remained worse than INT2 weight-only NLL 12.6709 and far worse than FP NLL 3.7118.

## Boundaries and scale limits

Single GPT-2 small checkpoint, WikiText-2 test text, 65,280 held-out evaluation tokens, post-training fake quantization only, split projection sites only, no training-aware calibration, no groupwise/per-channel activation scales, no downstream tasks, no hardware INT2 kernel measurement.

## Claim scope

On GPT-2 small evaluated on a deterministic WikiText-2 held-out slice, composition-aware greedy activation exponent selection at attention/MLP split projection outputs improves NLL versus global and local-MSE exponent controls under INT2 fake quantization, but does not recover the INT2 split-projection weight-only baseline or approach FP perplexity.

## Why it stopped

Direct bounded validation found mechanism support versus exponent controls but negative practical performance versus the real INT2 weight-only and FP baselines.

## Recommended next action

Stop this branch as no-paper useful evidence; a bounded adjacent test should replace scalar split activation exponents with residual-aware groupwise or per-channel activation scales and require beating the INT2 weight-only baseline on held-out GPT-2 perplexity.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Residual-aware groupwise activation scaling for GPT-2 split INT2 quantization
- Success threshold: Held-out NLL for INT2 weights plus the new activation quantizer must be no worse than INT2 weight-only NLL + 0.05 and at least 0.5 NLL better than the scalar composition-aware exponent baseline under the same protocol.
- Stop condition: Stop if the new quantizer remains worse than INT2 weight-only by more than 0.25 NLL or fails to beat scalar composition-aware exponents by at least 0.2 NLL on the held-out slice.

## Evidence references

- Artifact root: `<local-path>/projects/composition-aware-activation-exponent-sweep-for-gpt-2-int2-863306ea59`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
