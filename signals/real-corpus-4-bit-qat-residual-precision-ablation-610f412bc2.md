# Real-corpus 4-bit QAT residual precision ablation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-4-bit-qat-residual-precision-ablation-610f412bc2`
Run ID: `real-corpus-4-bit-qat-residual-precision-ablation-610f412bc2-20260603T134913222344+0000`

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

- Parent run decision: Full-Precision Residual Skip Connections in 4-bit Training: enoch://control-plane/projects/full-precision-residual-skip-connections-in-4-bit-training-5e450e8c95ed/runs/full-precision-residual-skip-connections-in-4-bit-training-5e450e8c95ed-20260602T183711278919+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/878afbbb9b2b

## What looked useful

The Tier 1 real-corpus ablation indicates that the residual stream is the sensitive part of this 4-bit QAT setup: 4-bit residual activations fail the explicit +0.03 best-validation-loss threshold, but 6-bit and 8-bit residual activations remain close to the no-residual-quantization control.

## Boundaries and scale limits

Tiny model, byte-level tokenizer, context length 64, 1200 optimizer steps per condition, WikiText-2 only; not validated at GPT-2-small scale, with subword tokenization, longer contexts, larger corpora, longer training, downstream tasks, or real low-bit deployment kernels.

## Claim scope

In a small byte-level 2-layer GPT-style transformer trained on WikiText-2 with 4-bit fake-quantized linear weights, 4-bit residual activation quantization consistently degraded best validation loss by about +0.14 versus no residual quantization across three seeds, while 6-bit and 8-bit residual activations stayed within about +0.006 and +0.003 respectively.

## Why it stopped

Closed as no-paper useful signal: the direct small real-corpus replicated test falsified the 4-bit-residual viability threshold, but the evidence is not broad or mature enough for publication.

## Recommended next action

Run a bounded deepen follow-up on a GPT-2-small-class or parameter-matched subword-tokenized model comparing no residual quantization, 6-bit residuals, and 4-bit residuals for enough tokens to confirm whether 6 bits is a reliable residual precision floor.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class confirmation of 6-bit residual precision floor for 4-bit QAT
- Success threshold: 6-bit residual best validation loss within +0.03 of the no-residual-quantization control and at least 0.05 better than 4-bit residuals on mean best validation loss.
- Stop condition: Stop if 6-bit residuals exceed +0.03 validation-loss delta versus no residual quantization in two matched seeds, or if 4-bit residuals no longer show a material penalty under the improved recipe.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-4-bit-qat-residual-precision-ablation-610f412bc2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
