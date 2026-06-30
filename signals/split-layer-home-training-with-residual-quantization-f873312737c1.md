# Split-Layer Home Training with Residual Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `split-layer-home-training-with-residual-quantization-f873312737c1`
Run ID: `split-layer-home-training-with-residual-quantization-f873312737c1-20260607T223405473710+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/291a0c948d7c

## What looked useful

Residual quantization preserved cut activations numerically, with residual_2x2bit reducing reconstruction MSE from 14.2180 to 0.6300 versus uniform_2bit, but mean final validation accuracy was effectively tied: 0.4584 for residual_2x2bit versus 0.4574 for uniform_2bit and 0.4462 for fp32.

## Boundaries and scale limits

Five-seed synthetic proxy only; no public dataset, transformer/GPT-2-small-class baseline, real home network transport, multi-device scheduling, privacy analysis, or long training run.

## Claim scope

On a synthetic split-MLP teacher task, residual-stage cut-activation quantization substantially reduces reconstruction error versus naive 2-bit uniform quantization, but does not produce a material validation-accuracy advantage over simpler uniform quantization baselines.

## Why it stopped

Bounded proxy evidence is mixed: residual quantization improves reconstruction, but this run does not show a meaningful training-quality advantage over simpler quantization controls.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up on a public small dataset or tiny language model only if the next experiment includes real split-learning transport metrics and matched uniform/residual bit-budget controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Public-data split learning with matched residual and uniform activation bit budgets
- Success threshold: Residual quantization must improve validation accuracy or convergence over matched uniform quantization by at least 1 absolute point or 10% fewer steps while staying within 2 points of fp32 split accuracy and preserving at least 4x activation compression.
- Stop condition: Stop if residual quantization is statistically tied with or worse than matched uniform quantization on validation quality, or if transport overhead dominates any compression benefit.

## Evidence references

- Artifact root: `<local-path>/projects/split-layer-home-training-with-residual-quantization-f873312737c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
