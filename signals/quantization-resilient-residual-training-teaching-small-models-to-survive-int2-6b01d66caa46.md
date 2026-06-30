# Quantization-Resilient Residual Training: Teaching Small Models to Survive INT2

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantization-resilient-residual-training-teaching-small-models-to-survive-int2-6b01d66caa46`
Run ID: `quantization-resilient-residual-training-teaching-small-models-to-survive-int2-6b01d66caa46-20260610T032825100155+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/ef360c99b240

## What looked useful

Across five seeds, standard training reached 0.8835 mean INT2 accuracy, QAT reached 0.9409, and QRT reached 0.9368. QRT improved INT2 accuracy by 5.33 points over standard training and preserved 2.67 points more fp32 accuracy than QAT, but trailed QAT by 0.41 points INT2 accuracy on every seed.

## Boundaries and scale limits

MNIST only; small residual MLP only; weight-only per-layer signed INT2 quantization with fp32 biases; no activation quantization, transformer, language-model, real INT2 kernel, or large-dataset validation.

## Claim scope

On a NumPy residual MLP trained on MNIST with 12k train and 3k test examples, fake-INT2 residual consistency training improves post-training INT2 weight-quantized accuracy over ordinary fp32 training while preserving most fp32 accuracy, but it does not beat fake-INT2 QAT on the target INT2 metric.

## Why it stopped

Bounded local evidence is mixed: QRT helps relative to ordinary training but fails to outperform the simpler direct QAT control on the primary INT2 survival metric, so this is not paper-positive.

## Recommended next action

Stop this run as no-paper useful signal; run one bounded transformer or tiny language-model follow-up only if testing whether QRT's fp32-retention tradeoff matters under INT2 weight plus activation quantization.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer INT2 QRT vs QAT Under Weight and Activation Quantization
- Success threshold: QRT must match or exceed QAT INT2 quality by at least 1 percent relative error reduction while preserving at least half of the fp32-quality advantage observed here.
- Stop condition: Stop if QRT again trails QAT on quantized quality across three seeds or if the fp32-retention advantage disappears under activation quantization.

## Evidence references

- Artifact root: `<local-path>/projects/quantization-resilient-residual-training-teaching-small-models-to-survive-int2-6b01d66caa46`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
