# Low-Rank Residual Channels for Sub-2-bit Weight Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `low-rank-residual-channels-for-sub-2-bit-weight-quantization-9d2dbe9c0188`
Run ID: `low-rank-residual-channels-for-sub-2-bit-weight-quantization-9d2dbe9c0188-20260519T043133540707+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/eef056bc5fd5

## What looked useful

Binary+LRRC reduced transformer layer output NMSE versus binary on 12/12 layers, but was worse than plain ternary on 11/12 layers. Ternary+LRRC reduced transformer layer output NMSE versus ternary on 12/12 layers, but slightly reduced five-seed digits accuracy versus plain ternary.

## Boundaries and scale limits

No LLM perplexity, no calibration-trained residuals, no packed-kernel runtime, and no full-model 7B-scale validation were run. The downstream task was a small sklearn digits MLP with hidden-layer-only quantization.

## Claim scope

Post-training SVD low-rank residual channels under a sub-2-bit effective storage budget improve binary and ternary layer reconstruction on synthetic matrices and 12 distilgpt2 layers, but they did not improve the strongest downstream small-task accuracy control in this run.

## Why it stopped

Bounded local evidence is mixed: reconstruction improves, but the post-training residual did not improve downstream accuracy and is not a direct LLM-quality validation.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test is calibration-trained ternary+LRRC on GPT-2-small perplexity against matched-storage ternary and GPTQ/AWQ-style controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibration-trained ternary residual channels for GPT-2-small sub-2-bit perplexity
- Success threshold: At <=1.95 effective bits per weight, calibration-trained ternary+LRRC must reduce perplexity by at least 5% relative to plain ternary and avoid more than a 2% slowdown in an honest unfused prototype matmul path, or show a clear route to fusion.
- Stop condition: Stop if calibrated residuals fail to improve GPT-2-small perplexity over plain ternary across two seeds/ranks, or if the effective storage budget exceeds 2 bits per weight after all scales/factors are counted.

## Evidence references

- Artifact root: `<local-path>/projects/low-rank-residual-channels-for-sub-2-bit-weight-quantization-9d2dbe9c0188`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
