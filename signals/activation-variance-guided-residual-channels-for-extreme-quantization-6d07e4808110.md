# Activation-Variance Guided Residual Channels for Extreme Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-variance-guided-residual-channels-for-extreme-quantization-6d07e4808110`
Run ID: `activation-variance-guided-residual-channels-for-extreme-quantization-6d07e4808110-20260527T113711124703+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/cb48439439d2

## What looked useful

Residual full-precision channels help under extreme 2-bit GPT-2 weight quantization, but activation variance alone is not a strong selector: at the main 2% budget activation variance loss was 8.3597 versus 8.3501 for weight magnitude and 8.3230 for the quant-error oracle, while no residual was 8.6814 and random-seed controls averaged 8.6702.

## Boundaries and scale limits

Single GPT-2-small-class model, Wikitext-2 only, 64 evaluation windows of length 256, post-training weight-only quantization, no activation quantization, no fine-tuning, no runtime kernel implementation, and no larger-model or downstream-task validation.

## Claim scope

On GPT-2 with Wikitext-2 fixed-window evaluation, 2-bit weight-only post-training quantization, and 0.5%-5% full-precision residual output-channel budgets, activation-variance selection improves over no-residual and random residual-channel controls but does not reliably beat simpler weight-magnitude or quantization-error-informed controls.

## Why it stopped

No-paper bounded result: the mechanism beats no-residual and random controls, but the proposed activation-variance-only selector fails to reliably outperform cheap stronger controls and remains far from full-precision quality under 2-bit quantization.

## Recommended next action

Stop the pure activation-variance selector as a paper candidate; if continuing, run a bounded deepen test of an activation-weighted quantization-error selector against weight magnitude on full Wikitext-2 and a second GPT-scale model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-weighted quantization-error residual channel selection
- Success threshold: Hybrid selector reduces evaluation loss by at least 0.05 versus weight magnitude at two or more residual budgets on both models, while remaining better than the mean random selector by at least two random-control standard deviations.
- Stop condition: Stop if the hybrid selector does not beat weight magnitude by at least 0.02 loss on GPT-2 full Wikitext-2 at the 2% budget, or if gains disappear on the second model.

## Evidence references

- Artifact root: `<local-path>/projects/activation-variance-guided-residual-channels-for-extreme-quantization-6d07e4808110`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
